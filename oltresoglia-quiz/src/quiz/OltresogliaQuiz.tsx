import { AnimatePresence, MotionConfig, motion, type Variants } from 'framer-motion'
import {
  useCallback,
  useEffect,
  useId,
  useRef,
  useState,
  type ButtonHTMLAttributes,
  type FormEvent,
  type KeyboardEvent,
  type ReactNode,
} from 'react'
import afelioBg from '../assets/backgrounds/afelio.svg'
import eclissiBg from '../assets/backgrounds/eclissi.svg'
import orbitaBg from '../assets/backgrounds/orbita.svg'
import sogliaBg from '../assets/backgrounds/soglia.svg'
import zenitBg from '../assets/backgrounds/zenit.svg'
import { onQuizComplete as placeholderOnQuizComplete, type OnQuizComplete } from './onQuizComplete'
import {
  PROFILE_NAMES,
  QUESTIONS,
  QUIZ_TITLE,
  TOTAL_QUESTIONS,
  computeTotals,
  emptyAnswers,
  isComplete,
  isValidAnswerArray,
  pickResult,
  type AnswerIndices,
  type ProfileId,
} from './quizData'

/* ------------------------------------------------------------------ */
/* Copy that is not in the brief — to be confirmed by Pietro.         */
/* ------------------------------------------------------------------ */

const INTRO_VALUE_PROP = 'Otto domande sulle tue giornate reali. Un profilo che le descrive davvero.'
const INTRO_META = '8 domande · circa 2 minuti'

interface ResultCopy {
  definingLine: string | null
  narratedDay: string | null
  whatChanges: string | null
  whatsappLabel: string
  /** Placeholder until the real WhatsApp link is supplied. */
  whatsappHref: string
}

// [PIETRO TO PROVIDE — final result copy per profile not yet written]
// Fill a slot and its placeholder disappears; leave it null to keep the marked placeholder.
const RESULT_COPY: Record<ProfileId, ResultCopy> = {
  ORBITA: { definingLine: null, narratedDay: null, whatChanges: null, whatsappLabel: 'Scrivici su WhatsApp', whatsappHref: '#' },
  ZENIT: { definingLine: null, narratedDay: null, whatChanges: null, whatsappLabel: 'Scrivici su WhatsApp', whatsappHref: '#' },
  AFELIO: { definingLine: null, narratedDay: null, whatChanges: null, whatsappLabel: 'Scrivici su WhatsApp', whatsappHref: '#' },
  ECLISSI: { definingLine: null, narratedDay: null, whatChanges: null, whatsappLabel: 'Scrivici su WhatsApp', whatsappHref: '#' },
}

/* ------------------------------------------------------------------ */
/* Background imagery                                                  */
/* ------------------------------------------------------------------ */

// Swap any of these for brand photography: every image is shown in grayscale under a
// Dark Charcoal overlay, so it stays inside the palette whatever its original colours.
const BACKGROUND_QUIZ = sogliaBg
const BACKGROUND_RESULT: Record<ProfileId, string> = {
  ORBITA: orbitaBg,
  ZENIT: zenitBg,
  AFELIO: afelioBg,
  ECLISSI: eclissiBg,
}

// Overlay strength per screen: light where there is little text, heavier behind the questions.
const OVERLAY_OPACITY: Record<Step['kind'], number> = { intro: 0.2, question: 0.6, email: 0.6, result: 0.3 }

/* ------------------------------------------------------------------ */
/* Persistence — answers only, never totals or the result.            */
/* ------------------------------------------------------------------ */

const STORAGE_KEY = 'oltresoglia-quiz:answers:v1'

function loadSavedAnswers(): AnswerIndices | null {
  try {
    const raw = window.localStorage.getItem(STORAGE_KEY)
    if (!raw) return null
    const parsed: unknown = JSON.parse(raw)
    return isValidAnswerArray(parsed) && parsed.some((a) => a != null) ? parsed : null
  } catch {
    return null
  }
}

function saveAnswers(answers: AnswerIndices) {
  try {
    window.localStorage.setItem(STORAGE_KEY, JSON.stringify(answers))
  } catch {
    // Storage unavailable (private mode, quota): the quiz still works, it just won't survive a refresh.
  }
}

function clearSavedAnswers() {
  try {
    window.localStorage.removeItem(STORAGE_KEY)
  } catch {
    // ignore
  }
}

/* ------------------------------------------------------------------ */
/* Flow                                                                */
/* ------------------------------------------------------------------ */

type Step =
  | { kind: 'intro' }
  | { kind: 'question'; index: number }
  | { kind: 'email' }
  | { kind: 'result'; profile: ProfileId }

type SubmitStatus = 'idle' | 'submitting' | 'error'

const SUBMIT_TIMEOUT_MS = 20_000
const EMAIL_PATTERN = /^[^\s@]+@[^\s@.]+(\.[^\s@.]+)*\.[^\s@.]{2,}$/
const EMAIL_ERROR_DELAY_MS = 700

function stepKey(step: Step) {
  return step.kind === 'question' ? `question-${step.index}` : step.kind
}

/** Where to land after a refresh: the first unanswered question, or the email step. */
function resumeStep(answers: AnswerIndices): Step {
  const firstOpen = answers.findIndex((a) => a == null)
  return firstOpen === -1 ? { kind: 'email' } : { kind: 'question', index: firstOpen }
}

function withTimeout<T>(promise: Promise<T>, ms: number): Promise<T> {
  return new Promise<T>((resolve, reject) => {
    const timer = window.setTimeout(() => reject(new Error('Submission timed out')), ms)
    promise.then(
      (value) => {
        window.clearTimeout(timer)
        resolve(value)
      },
      (error: unknown) => {
        window.clearTimeout(timer)
        reject(error)
      },
    )
  })
}

const slide: Variants = {
  enter: (direction: number) => ({ opacity: 0, x: direction * 24 }),
  center: { opacity: 1, x: 0, transition: { duration: 0.22, ease: [0.22, 1, 0.36, 1] } },
  exit: (direction: number) => ({ opacity: 0, x: direction * -24, transition: { duration: 0.14, ease: 'easeIn' } }),
}

export interface OltresogliaQuizProps {
  /** Called once with the full submission after the email step. Defaults to the placeholder. */
  onQuizComplete?: OnQuizComplete
}

export default function OltresogliaQuiz({ onQuizComplete = placeholderOnQuizComplete }: OltresogliaQuizProps) {
  const [initial] = useState(() => {
    const saved = loadSavedAnswers()
    return saved
      ? { answers: saved, step: resumeStep(saved), resumed: true }
      : { answers: emptyAnswers(), step: { kind: 'intro' } as Step, resumed: false }
  })

  const [answers, setAnswers] = useState<AnswerIndices>(initial.answers)
  const [step, setStep] = useState<Step>(initial.step)
  const [direction, setDirection] = useState(1)
  const [showResumeNotice, setShowResumeNotice] = useState(initial.resumed)
  // Headings only take focus after the visitor has navigated — never on first page load.
  const [hasNavigated, setHasNavigated] = useState(false)

  const [email, setEmail] = useState('')
  const [consent, setConsent] = useState(false)
  const [submitStatus, setSubmitStatus] = useState<SubmitStatus>('idle')
  const submittingRef = useRef(false)

  useEffect(() => {
    if (step.kind === 'result') return
    if (answers.some((a) => a != null)) saveAnswers(answers)
    else clearSavedAnswers()
  }, [answers, step.kind])

  const go = useCallback((next: Step, dir: 1 | -1) => {
    setDirection(dir)
    setHasNavigated(true)
    setShowResumeNotice(false)
    setStep(next)
  }, [])

  const selectAnswer = useCallback((questionIndex: number, optionIndex: number) => {
    setAnswers((prev) => {
      if (prev[questionIndex] === optionIndex) return prev
      const next = [...prev]
      next[questionIndex] = optionIndex
      return next
    })
  }, [])

  const submit = useCallback(async () => {
    if (submittingRef.current) return
    if (!isComplete(answers)) {
      go(resumeStep(answers), -1)
      return
    }

    const totals = computeTotals(answers)
    const result = pickResult(totals)
    const submission = {
      answers: answers.map((optionIndex, i) => ({
        questionId: QUESTIONS[i].id,
        question: QUESTIONS[i].text,
        optionIndex,
        answer: QUESTIONS[i].options[optionIndex].label,
      })),
      totals,
      result,
      email: email.trim(),
      consentedAt: new Date().toISOString(),
    }

    submittingRef.current = true
    setSubmitStatus('submitting')
    try {
      await withTimeout(Promise.resolve().then(() => onQuizComplete(submission)), SUBMIT_TIMEOUT_MS)
      clearSavedAnswers()
      setSubmitStatus('idle')
      go({ kind: 'result', profile: result }, 1)
    } catch {
      setSubmitStatus('error')
    } finally {
      submittingRef.current = false
    }
  }, [answers, email, go, onQuizComplete])

  let screen: ReactNode
  switch (step.kind) {
    case 'intro':
      screen = <IntroScreen focusOnMount={hasNavigated} onStart={() => go({ kind: 'question', index: 0 }, 1)} />
      break
    case 'question': {
      const i = step.index
      screen = (
        <QuestionScreen
          focusOnMount={hasNavigated}
          index={i}
          selected={answers[i]}
          onSelect={(option) => selectAnswer(i, option)}
          onBack={() => go(i === 0 ? { kind: 'intro' } : { kind: 'question', index: i - 1 }, -1)}
          onNext={() => go(i + 1 < TOTAL_QUESTIONS ? { kind: 'question', index: i + 1 } : { kind: 'email' }, 1)}
        />
      )
      break
    }
    case 'email':
      screen = (
        <EmailScreen
          focusOnMount={hasNavigated}
          email={email}
          consent={consent}
          status={submitStatus}
          onEmailChange={setEmail}
          onConsentChange={setConsent}
          onBack={() => {
            setSubmitStatus('idle')
            go({ kind: 'question', index: TOTAL_QUESTIONS - 1 }, -1)
          }}
          onSubmit={submit}
        />
      )
      break
    case 'result':
      screen = <ResultScreen focusOnMount={hasNavigated} profile={step.profile} />
      break
  }

  return (
    <MotionConfig reducedMotion="user">
      <div className="relative isolate flex min-h-dvh flex-col bg-charcoal font-sans text-porcelain">
        <Backdrop
          src={step.kind === 'result' ? BACKGROUND_RESULT[step.profile] : BACKGROUND_QUIZ}
          overlay={OVERLAY_OPACITY[step.kind]}
        />
        <header className="relative mx-auto w-full max-w-2xl px-4 pt-5 sm:px-8 sm:pt-8">
          {/* Text wordmark in Whiteout — swap for the official logo SVG when available. */}
          <p className="font-display text-sm font-black tracking-[0.22em] text-whiteout">OLTRESOGLIA</p>
          {(step.kind === 'question' || step.kind === 'email') && <Progress step={step} />}
          {showResumeNotice && (
            <p role="status" className="mt-4 text-sm text-porcelain/70">
              Bentornato: abbiamo ripreso da dove eri rimasto.
            </p>
          )}
        </header>

        <main className="relative mx-auto flex w-full max-w-2xl flex-1 flex-col overflow-x-clip px-4 sm:px-8">
          <AnimatePresence mode="wait" initial={false} custom={direction}>
            <motion.div
              key={stepKey(step)}
              custom={direction}
              variants={slide}
              initial="enter"
              animate="center"
              exit="exit"
              className="flex flex-1 flex-col"
            >
              {screen}
            </motion.div>
          </AnimatePresence>
        </main>
      </div>
    </MotionConfig>
  )
}

/* ------------------------------------------------------------------ */
/* Shared pieces                                                       */
/* ------------------------------------------------------------------ */

/** Full-bleed background image with a charcoal overlay; crossfades when the image changes. */
function Backdrop({ src, overlay }: { src: string; overlay: number }) {
  return (
    <div aria-hidden="true" className="pointer-events-none fixed inset-0 -z-10 overflow-hidden bg-charcoal">
      <AnimatePresence initial={false}>
        <motion.img
          key={src}
          src={src}
          alt=""
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          transition={{ duration: 0.6 }}
          className="absolute inset-0 size-full object-cover grayscale"
        />
      </AnimatePresence>
      <motion.div
        className="absolute inset-0 bg-charcoal"
        initial={false}
        animate={{ opacity: overlay }}
        transition={{ duration: 0.4 }}
      />
    </div>
  )
}

/** Moves focus to the screen's heading (and the page to the top) when it mounts. */
function useScreenHeading(focusOnMount: boolean) {
  const ref = useRef<HTMLHeadingElement>(null)
  useEffect(() => {
    if (!focusOnMount) return
    window.scrollTo({ top: 0 })
    ref.current?.focus({ preventScroll: true })
  }, [focusOnMount])
  return ref
}

const focusRing = 'focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-saffron'
const focusRingTight = 'focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-saffron'

interface PrimaryButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  /** Looks and announces as disabled but stays focusable, so a press can explain what's missing. */
  inactive?: boolean
  loading?: boolean
}

function PrimaryButton({ inactive, loading, className = '', children, ...props }: PrimaryButtonProps) {
  const off = inactive || loading
  return (
    <button
      type="button"
      aria-disabled={off || undefined}
      aria-busy={loading || undefined}
      className={`inline-flex min-h-14 cursor-pointer items-center justify-center gap-2.5 rounded-full px-7 text-base font-semibold transition-[background-color,color,transform] duration-200 ${focusRing} ${
        off
          ? 'bg-porcelain/10 text-porcelain/45'
          : 'bg-saffron text-charcoal hover:bg-saffron/90 active:scale-[0.98]'
      } ${loading ? 'cursor-progress' : inactive ? 'cursor-not-allowed' : ''} ${className}`}
      {...props}
    >
      {children}
    </button>
  )
}

function BackButton({ onClick, disabled }: { onClick: () => void; disabled?: boolean }) {
  return (
    <button
      type="button"
      onClick={onClick}
      disabled={disabled}
      className={`inline-flex min-h-14 shrink-0 cursor-pointer items-center justify-center gap-2 rounded-full border border-porcelain/20 px-5 text-base font-medium text-porcelain transition-colors duration-200 hover:border-porcelain/50 disabled:cursor-not-allowed disabled:opacity-40 ${focusRing}`}
    >
      <span aria-hidden="true">←</span>
      Indietro
    </button>
  )
}

function Spinner() {
  return (
    <span
      aria-hidden="true"
      className="size-5 animate-spin rounded-full border-2 border-porcelain/25 border-t-porcelain"
    />
  )
}

function Progress({ step }: { step: Extract<Step, { kind: 'question' } | { kind: 'email' }> }) {
  const current = step.kind === 'question' ? step.index : TOTAL_QUESTIONS
  return (
    // The heading of each question carries the same info for screen readers.
    <div className="mt-6" aria-hidden="true">
      <p className="font-display text-xs font-normal uppercase tracking-[0.18em] text-porcelain/70">
        {step.kind === 'question' ? (
          <>
            Domanda <span className="text-saffron">{current + 1}</span> di {TOTAL_QUESTIONS}
          </>
        ) : (
          <span className="text-saffron">Ultimo passo</span>
        )}
      </p>
      <div className="mt-3 grid grid-cols-8 gap-1.5">
        {QUESTIONS.map((q, i) => (
          <span
            key={q.id}
            className={`h-1 rounded-full transition-colors duration-300 ${i <= current ? 'bg-saffron' : 'bg-porcelain/15'}`}
          />
        ))}
      </div>
    </div>
  )
}

/** Keeps the step's actions in view on small screens, however long the content. */
function ActionBar({ children }: { children: ReactNode }) {
  return (
    <div className="sticky bottom-0 -mx-4 mt-auto border-t border-porcelain/10 bg-charcoal/85 px-4 backdrop-blur-md pt-4 pb-[max(1rem,env(safe-area-inset-bottom))] sm:static sm:mx-0 sm:border-0 sm:bg-transparent sm:px-0 sm:pb-12 sm:backdrop-blur-none">
      {children}
    </div>
  )
}

/* ------------------------------------------------------------------ */
/* Screens                                                             */
/* ------------------------------------------------------------------ */

function IntroScreen({ focusOnMount, onStart }: { focusOnMount: boolean; onStart: () => void }) {
  const headingRef = useScreenHeading(focusOnMount)
  return (
    <section className="flex flex-1 flex-col justify-center py-12">
      <h1
        ref={headingRef}
        tabIndex={-1}
        className="font-display text-[2rem] leading-[1.08] font-black text-balance outline-none sm:text-5xl"
      >
        {QUIZ_TITLE}
      </h1>
      <p className="mt-6 max-w-prose text-lg leading-relaxed text-porcelain/75">{INTRO_VALUE_PROP}</p>
      <div className="mt-10 flex flex-col gap-4 sm:flex-row sm:items-center sm:gap-6">
        <PrimaryButton onClick={onStart} className="w-full sm:w-auto">
          Inizia
          <span aria-hidden="true">→</span>
        </PrimaryButton>
        <p className="text-sm text-porcelain/55">{INTRO_META}</p>
      </div>
    </section>
  )
}

interface QuestionScreenProps {
  focusOnMount: boolean
  index: number
  selected: number | null
  onSelect: (option: number) => void
  onBack: () => void
  onNext: () => void
}

function QuestionScreen({ focusOnMount, index, selected, onSelect, onBack, onNext }: QuestionScreenProps) {
  const question = QUESTIONS[index]
  const headingRef = useScreenHeading(focusOnMount)
  const headingId = useId()
  const hintId = useId()
  const optionRefs = useRef<(HTMLButtonElement | null)[]>([])
  const [nudged, setNudged] = useState(false)
  const hasSelection = selected != null

  const tryNext = () => {
    if (hasSelection) {
      onNext()
    } else {
      setNudged(true)
      optionRefs.current[0]?.focus()
    }
  }

  const choose = (option: number) => {
    setNudged(false)
    onSelect(option)
  }

  const onOptionKeyDown = (event: KeyboardEvent<HTMLButtonElement>, i: number) => {
    const count = question.options.length
    let target: number
    switch (event.key) {
      case 'ArrowDown':
      case 'ArrowRight':
        target = (i + 1) % count
        break
      case 'ArrowUp':
      case 'ArrowLeft':
        target = (i - 1 + count) % count
        break
      case 'Home':
        target = 0
        break
      case 'End':
        target = count - 1
        break
      case 'Enter':
        // Enter on the chosen answer advances; on any other answer it selects (native click).
        if (selected === i) {
          event.preventDefault()
          onNext()
        }
        return
      default:
        return
    }
    event.preventDefault()
    choose(target)
    optionRefs.current[target]?.focus()
  }

  return (
    <section aria-labelledby={headingId} className="flex flex-1 flex-col pt-8 sm:pt-12">
      <h1
        id={headingId}
        ref={headingRef}
        tabIndex={-1}
        className="font-display text-[1.5rem] leading-[1.15] font-black text-balance break-words outline-none sm:text-[2.25rem]"
      >
        <span className="sr-only">
          Domanda {index + 1} di {TOTAL_QUESTIONS}:{' '}
        </span>
        {question.text}
      </h1>

      <div role="radiogroup" aria-labelledby={headingId} aria-required="true" className="mt-8 grid gap-3">
        {question.options.map((option, i) => {
          const isSelected = selected === i
          return (
            <button
              key={option.label}
              ref={(el) => {
                optionRefs.current[i] = el
              }}
              type="button"
              role="radio"
              aria-checked={isSelected}
              onClick={() => choose(i)}
              onKeyDown={(e) => onOptionKeyDown(e, i)}
              className={`flex min-h-14 w-full cursor-pointer items-start gap-4 rounded-xl border px-4 py-4 text-left backdrop-blur-sm transition-[border-color,background-color,box-shadow] duration-200 sm:px-5 ${focusRingTight} ${
                isSelected
                  ? 'border-saffron bg-porcelain/[0.06] shadow-[inset_0_0_0_1px_var(--oltre-saffron-mango)]'
                  : 'border-porcelain/15 bg-porcelain/[0.03] hover:border-porcelain/40 hover:bg-porcelain/[0.05]'
              }`}
            >
              <span
                aria-hidden="true"
                className={`mt-0.5 flex size-5 shrink-0 items-center justify-center rounded-full border-2 transition-colors duration-200 ${
                  isSelected ? 'border-saffron' : 'border-porcelain/35'
                }`}
              >
                <span
                  className={`size-2.5 rounded-full bg-saffron transition-transform duration-200 ${
                    isSelected ? 'scale-100' : 'scale-0'
                  }`}
                />
              </span>
              <span className="text-base leading-snug font-normal text-porcelain">{option.label}</span>
            </button>
          )
        })}
      </div>

      <ActionBar>
        <div className="flex items-center gap-3">
          <BackButton onClick={onBack} />
          <PrimaryButton
            inactive={!hasSelection}
            aria-describedby={hintId}
            onClick={tryNext}
            className="flex-1 sm:flex-none"
          >
            Avanti
            <span aria-hidden="true">→</span>
          </PrimaryButton>
        </div>
        <p
          id={hintId}
          role="status"
          className={`mt-2 min-h-5 text-sm transition-colors ${nudged ? 'text-porcelain' : 'text-porcelain/55'}`}
        >
          {hasSelection ? '' : 'Seleziona una risposta per continuare.'}
        </p>
      </ActionBar>
    </section>
  )
}

interface EmailScreenProps {
  focusOnMount: boolean
  email: string
  consent: boolean
  status: SubmitStatus
  onEmailChange: (value: string) => void
  onConsentChange: (value: boolean) => void
  onBack: () => void
  onSubmit: () => void
}

function EmailScreen({
  focusOnMount,
  email,
  consent,
  status,
  onEmailChange,
  onConsentChange,
  onBack,
  onSubmit,
}: EmailScreenProps) {
  const headingRef = useScreenHeading(focusOnMount)
  const emailRef = useRef<HTMLInputElement>(null)
  const consentRef = useRef<HTMLInputElement>(null)
  const headingId = useId()
  const emailId = useId()
  const emailErrorId = useId()
  const consentId = useId()
  const consentErrorId = useId()
  const hintId = useId()

  const emailValid = EMAIL_PATTERN.test(email.trim())
  // Once flagged, email errors track the value live; before that they wait for a short typing pause.
  const [emailFlagged, setEmailFlagged] = useState(() => email.trim() !== '' && !emailValid)
  const [consentFlagged, setConsentFlagged] = useState(false)
  const flagTimer = useRef<number | undefined>(undefined)
  useEffect(() => () => window.clearTimeout(flagTimer.current), [])

  const submitting = status === 'submitting'
  const ready = emailValid && consent

  const emailError =
    emailFlagged && !emailValid
      ? email.trim()
        ? "Controlla l'indirizzo: sembra incompleto (es. nome@dominio.it)."
        : 'Inserisci la tua email per continuare.'
      : null
  const consentError = consentFlagged && !consent ? 'Per continuare serve il tuo consenso.' : null

  const hint = ready
    ? ''
    : !emailValid && !consent
      ? "Inserisci un'email valida e spunta il consenso per continuare."
      : !emailValid
        ? "Inserisci un'email valida per continuare."
        : 'Spunta il consenso per continuare.'

  const handleEmailChange = (value: string) => {
    onEmailChange(value)
    window.clearTimeout(flagTimer.current)
    if (value.trim() && !EMAIL_PATTERN.test(value.trim())) {
      flagTimer.current = window.setTimeout(() => setEmailFlagged(true), EMAIL_ERROR_DELAY_MS)
    }
  }

  const handleSubmit = (event?: FormEvent) => {
    event?.preventDefault()
    if (submitting) return
    if (!ready) {
      setEmailFlagged(true)
      setConsentFlagged(true)
      ;(emailValid ? consentRef : emailRef).current?.focus()
      return
    }
    onSubmit()
  }

  return (
    <section aria-labelledby={headingId} className="flex flex-1 flex-col pt-8 sm:pt-12">
      <h1
        id={headingId}
        ref={headingRef}
        tabIndex={-1}
        className="font-display text-[1.5rem] leading-[1.15] font-black text-balance outline-none sm:text-[2.25rem]"
      >
        Dove ti mandiamo il risultato?
      </h1>
      <p className="mt-4 text-base leading-relaxed text-porcelain/75">
        Inserisci la tua email e il tuo profilo compare subito dopo.
      </p>

      <form noValidate onSubmit={handleSubmit} className="flex flex-1 flex-col" aria-busy={submitting}>
        <div className="mt-8">
          <label htmlFor={emailId} className="block text-sm font-semibold text-porcelain">
            Email
          </label>
          <input
            ref={emailRef}
            id={emailId}
            type="email"
            name="email"
            inputMode="email"
            autoComplete="email"
            autoCapitalize="none"
            autoCorrect="off"
            spellCheck={false}
            placeholder="nome@dominio.it"
            value={email}
            readOnly={submitting}
            onChange={(e) => handleEmailChange(e.target.value)}
            onBlur={() => {
              if (email.trim() && !emailValid) setEmailFlagged(true)
            }}
            aria-invalid={emailError ? true : undefined}
            aria-describedby={emailError ? emailErrorId : undefined}
            className={`mt-2 block min-h-14 w-full rounded-xl border bg-porcelain/[0.04] px-4 backdrop-blur-sm text-base text-porcelain transition-colors duration-200 placeholder:text-porcelain/35 focus:outline-2 focus:outline-offset-2 focus:outline-saffron ${
              emailError ? 'border-saffron' : emailValid ? 'border-porcelain/40' : 'border-porcelain/20'
            }`}
          />
          <p id={emailErrorId} aria-live="polite" className="min-h-6 pt-2 text-sm text-porcelain">
            {emailError && <FieldMessage>{emailError}</FieldMessage>}
          </p>
        </div>

        <div className="mt-2">
          <div className="flex items-start gap-3">
            <span className="relative mt-0.5 flex size-6 shrink-0">
              <input
                ref={consentRef}
                id={consentId}
                type="checkbox"
                checked={consent}
                disabled={submitting}
                required
                onChange={(e) => onConsentChange(e.target.checked)}
                aria-invalid={consentError ? true : undefined}
                aria-describedby={consentError ? consentErrorId : undefined}
                className={`peer size-6 cursor-pointer appearance-none rounded-md border-2 bg-transparent transition-colors duration-200 checked:border-saffron checked:bg-saffron ${focusRingTight} ${
                  consentError ? 'border-saffron' : 'border-porcelain/40'
                }`}
              />
              <svg
                aria-hidden="true"
                viewBox="0 0 16 16"
                className="pointer-events-none absolute inset-0 m-auto size-4 text-charcoal opacity-0 transition-opacity peer-checked:opacity-100"
              >
                <path d="M3 8.5 6.5 12 13 4.5" fill="none" stroke="currentColor" strokeWidth="2.25" strokeLinecap="round" strokeLinejoin="round" />
              </svg>
            </span>
            <label htmlFor={consentId} className="cursor-pointer text-sm leading-relaxed text-porcelain/80">
              {/* [PIETRO TO PROVIDE — final GDPR consent wording + privacy policy link] */}
              Acconsento al trattamento dei miei dati per ricevere il risultato e comunicazioni da OLTRESOGLIA.{' '}
              <span className="text-porcelain/55">
                [PIETRO TO PROVIDE — testo legale definitivo del consenso GDPR e link all'informativa privacy]
              </span>
            </label>
          </div>
          <p id={consentErrorId} aria-live="polite" className="min-h-6 pt-2 pl-9 text-sm text-porcelain">
            {consentError && <FieldMessage>{consentError}</FieldMessage>}
          </p>
        </div>

        <ActionBar>
          {status === 'error' && (
            <div role="alert" className="mb-4 rounded-xl border border-porcelain/25 bg-porcelain/[0.04] p-4">
              <FieldMessage>
                Non siamo riusciti a inviare le tue risposte. Controlla la connessione e riprova: le risposte sono
                ancora qui.
              </FieldMessage>
              <button
                type="button"
                onClick={() => handleSubmit()}
                className={`mt-3 ml-7 inline-flex min-h-11 cursor-pointer items-center rounded-full border border-porcelain/40 px-5 text-sm font-semibold text-porcelain transition-colors hover:border-porcelain ${focusRing}`}
              >
                Riprova
              </button>
            </div>
          )}
          <div className="flex items-center gap-3">
            <BackButton onClick={onBack} disabled={submitting} />
            <PrimaryButton
              type="submit"
              inactive={!ready}
              loading={submitting}
              aria-describedby={hintId}
              className="flex-1 sm:flex-none"
            >
              {submitting ? (
                <>
                  <Spinner />
                  Invio in corso…
                </>
              ) : (
                <>
                  Scopri il risultato
                  <span aria-hidden="true">→</span>
                </>
              )}
            </PrimaryButton>
          </div>
          <p id={hintId} role="status" className="mt-2 min-h-5 text-sm text-porcelain/55">
            {submitting ? 'Stiamo preparando il tuo profilo…' : hint}
          </p>
        </ActionBar>
      </form>
    </section>
  )
}

/** Error/help line: icon + text, so meaning never depends on colour alone. */
function FieldMessage({ children }: { children: ReactNode }) {
  return (
    <span className="flex items-start gap-2">
      <svg aria-hidden="true" viewBox="0 0 20 20" className="mt-0.5 size-4 shrink-0 text-saffron">
        <circle cx="10" cy="10" r="8.5" fill="none" stroke="currentColor" strokeWidth="1.75" />
        <path d="M10 5.5v5.5" stroke="currentColor" strokeWidth="1.75" strokeLinecap="round" />
        <circle cx="10" cy="14.25" r="1.1" fill="currentColor" />
      </svg>
      <span>{children}</span>
    </span>
  )
}

function ResultScreen({ focusOnMount, profile }: { focusOnMount: boolean; profile: ProfileId }) {
  const headingRef = useScreenHeading(focusOnMount)
  const copy = RESULT_COPY[profile]
  const name = PROFILE_NAMES[profile]
  const slots = [
    { label: 'Frase che definisce il profilo', text: copy.definingLine },
    { label: 'La tua giornata, raccontata', text: copy.narratedDay },
    { label: 'Cosa cambia', text: copy.whatChanges },
  ]
  const hasMissingCopy = slots.some((slot) => slot.text == null)

  return (
    <section className="flex flex-1 flex-col pt-10 pb-12 sm:pt-16">
      <h1 ref={headingRef} tabIndex={-1} className="outline-none">
        <span className="block font-display text-xs font-normal tracking-[0.18em] text-porcelain/70 uppercase">
          Il tuo profilo è
        </span>
        <span className="mt-3 block font-display text-[3.25rem] leading-none font-black break-words text-porcelain sm:text-7xl">
          {name}
        </span>
      </h1>

      <div
        className={`mt-10 space-y-6 rounded-2xl bg-charcoal/60 p-5 backdrop-blur-md sm:p-7 ${
          hasMissingCopy ? 'border border-dashed border-porcelain/30' : ''
        }`}
      >
        {hasMissingCopy && (
          <p className="text-xs font-semibold tracking-wide text-porcelain/70 uppercase">
            [PIETRO TO PROVIDE — final result copy per profile not yet written]
          </p>
        )}
        {slots.map((slot) =>
          slot.text != null ? (
            <p key={slot.label} className="text-lg leading-relaxed text-porcelain">
              {slot.text}
            </p>
          ) : (
            <div key={slot.label}>
              <p className="text-sm font-semibold text-porcelain">{slot.label}</p>
              <p className="mt-1 text-sm text-porcelain/55">[Testo per il profilo {name} da scrivere]</p>
            </div>
          ),
        )}
      </div>

      {/* Brand palette has no green: WhatsApp CTA uses the primary accent + WhatsApp-style glyph. */}
      <a
        href={copy.whatsappHref}
        className={`mt-10 inline-flex min-h-14 w-full items-center justify-center gap-3 rounded-full bg-saffron px-7 text-base font-semibold text-charcoal transition-[background-color,transform] duration-200 hover:bg-saffron/90 active:scale-[0.98] sm:w-auto sm:self-start ${focusRing}`}
      >
        <ChatIcon />
        {copy.whatsappLabel}
      </a>
    </section>
  )
}

function ChatIcon() {
  return (
    <svg aria-hidden="true" viewBox="0 0 24 24" className="size-5">
      <path
        d="M12 3.25a8.75 8.75 0 0 0-7.6 13.07L3.25 20.75l4.55-1.12A8.75 8.75 0 1 0 12 3.25Z"
        fill="none"
        stroke="currentColor"
        strokeWidth="1.8"
        strokeLinejoin="round"
      />
      <path
        d="M9.1 8.2c.2-.4.5-.4.7-.4h.5c.2 0 .4.1.5.4l.7 1.6c.1.2 0 .5-.1.6l-.5.6c-.1.1-.1.3 0 .5.6 1 1.4 1.8 2.5 2.4.2.1.4.1.5-.1l.6-.7c.2-.2.4-.2.6-.1l1.5.8c.2.1.3.3.3.5 0 .7-.4 1.4-1.1 1.7-.6.3-1.4.3-2.4-.1-2-.8-3.6-2.4-4.4-4.3-.4-1-.4-2.1.1-2.9Z"
        fill="currentColor"
      />
    </svg>
  )
}
