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
import { suggestEmail } from './emailSuggestion'
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

// Intro copy from Pietro (test feedback, Oct 2026). Pairs of lines render as one paragraph.
const INTRO_PARAGRAPHS = [
  'Il problema non è la tua disciplina.\nÈ che hai sempre cercato di seguire programmi costruiti per una vita che non è la tua.',
  '8 domande per capire come sono davvero fatte le tue giornate.\nAl termine riceverai via email un piano personalizzato: come strutturare alimentazione, allenamento e abitudini intorno ai tuoi impegni reali.',
  'Per perdere grasso, costruire forza e fiato, e avere le energie per performare ovunque.\nNel lavoro, sul fisico e nella vita.',
  'Non è il solito test che ti dice chi sei.\nÈ il primo passo per costruire un sistema che funzioni anche quando la tua settimana non va come previsto.',
]
const INTRO_META = '8 domande · 60–90 secondi'

// Steps shown on the analysis screen between question 8 and the email step.
const ANALYSIS_STEPS = ['Incrocio orari, turni e trasferte', 'Calcolo quanto pesa davvero la tua giornata', 'Individuo il tuo profilo']
const ANALYSIS_STEP_MS = 900

// Result description per profile, from Pietro. `null` keeps a visible placeholder until the text arrives.
const PROFILE_DESCRIPTIONS: Record<ProfileId, string[] | null> = {
  ORBITA: [
    'La sveglia cambia, i pasti si spostano, il sonno segue il turno.\nReggi notti e cambi che manderebbero in tilt chiunque, e a volte hai persino più ore libere degli altri. Solo che non stanno mai nello stesso posto.',
    'Quello che ti manca non è il tempo, è un riferimento stabile.\nUn piano scritto per chi ha il lunedì salta alla prima rotazione.',
    'Ti abbiamo inviato per email la guida che fa per te.\nPerché un sistema che regge solo quando tutto va come previsto non è un sistema.',
  ],
  ZENIT: [
    "La tua giornata ha un inizio preciso e una fine che decide il lavoro: il rientro delle 19 diventa 21, poi una telefonata, una mail, un cliente che si trattiene. La chiudi quando l'hai vinta, non quando segna l'orologio. A quel punto la forza per allenarti ce l'hai ancora, ma le decisioni le hai finite molto prima.",
    "Quello che ti manca è una fine affidabile della giornata. La prima cosa che si rompe è la sera: l'allenamento rimandato, la cena che diventa il pasto più grande.",
    'Ti abbiamo inviato per email la guida che fa per te.\nPerché la sera non può continuare a essere il momento in cui molli tutto.',
  ],
  // Only partly visible in the screenshot we received: full text pending from Pietro.
  AFELIO: null,
  ECLISSI: null,
}

/** Where "Vedi il tuo risultato" leads (per-profile page or video). Placeholder until confirmed. */
const RESULT_CTA_HREF: Record<ProfileId, string> = { ORBITA: '#', ZENIT: '#', AFELIO: '#', ECLISSI: '#' }

/** Renders "line one\nline two" as one paragraph with a line break. */
function Lines({ text }: { text: string }) {
  return text.split('\n').map((line, i) => (
    <span key={i}>
      {i > 0 && <br />}
      {line}
    </span>
  ))
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
const OVERLAY_OPACITY: Record<Step['kind'], number> = { intro: 0.2, question: 0.6, analysis: 0.6, email: 0.6, result: 0.3 }

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
  | { kind: 'analysis' }
  | { kind: 'email' }
  | { kind: 'result'; profile: ProfileId }

type SubmitStatus = 'idle' | 'submitting' | 'error'

const SUBMIT_TIMEOUT_MS = 20_000
const EMAIL_PATTERN = /^[^\s@]+@[^\s@.]+(\.[^\s@.]+)*\.[^\s@.]{2,}$/
const EMAIL_ERROR_DELAY_MS = 700
const EMAIL_FORMAT_ERROR = 'Questa email non sembra completa. Controlla, ad esempio: nome@email.it'

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
  // A returning visitor lands on the intro, which offers "Riprendi dalla domanda N".
  const [initialAnswers] = useState(() => loadSavedAnswers() ?? emptyAnswers())

  const [answers, setAnswers] = useState<AnswerIndices>(initialAnswers)
  const [step, setStep] = useState<Step>({ kind: 'intro' })
  const [direction, setDirection] = useState(1)
  // Headings only take focus after the visitor has navigated — never on first page load.
  const [hasNavigated, setHasNavigated] = useState(false)

  const [email, setEmail] = useState('')
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
      submittedAt: new Date().toISOString(),
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
      screen = (
        <IntroScreen
          focusOnMount={hasNavigated}
          resumeAt={answers.some((a) => a != null) ? resumeStep(answers) : null}
          onStart={(next) => go(next, 1)}
        />
      )
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
          onNext={() => go(i + 1 < TOTAL_QUESTIONS ? { kind: 'question', index: i + 1 } : { kind: 'analysis' }, 1)}
        />
      )
      break
    }
    case 'analysis':
      screen = <AnalysisScreen focusOnMount={hasNavigated} onDone={() => go({ kind: 'email' }, 1)} />
      break
    case 'email':
      screen = (
        <EmailScreen
          focusOnMount={hasNavigated}
          email={email}
          status={submitStatus}
          onEmailChange={setEmail}
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
          {(step.kind === 'question' || step.kind === 'analysis' || step.kind === 'email') && <Progress step={step} />}
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

function Progress({ step }: { step: Extract<Step, { kind: 'question' } | { kind: 'analysis' } | { kind: 'email' }> }) {
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
          <span className="text-saffron">{step.kind === 'analysis' ? 'Analisi in corso' : 'Ultimo passo'}</span>
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

interface IntroScreenProps {
  focusOnMount: boolean
  /** Where a returning visitor picks up, or null for a first visit. */
  resumeAt: Step | null
  onStart: (next: Step) => void
}

function IntroScreen({ focusOnMount, resumeAt, onStart }: IntroScreenProps) {
  const headingRef = useScreenHeading(focusOnMount)
  const resumeLabel =
    resumeAt?.kind === 'question' ? `Riprendi dalla domanda ${resumeAt.index + 1}` : resumeAt ? "Riprendi dall'ultimo passo" : null
  return (
    <section className="flex flex-1 flex-col justify-center py-12">
      <h1
        ref={headingRef}
        tabIndex={-1}
        className="font-display text-[2rem] leading-[1.08] font-black text-balance outline-none sm:text-5xl"
      >
        {QUIZ_TITLE}
      </h1>
      <div className="mt-6 max-w-[60ch] space-y-4 text-base leading-relaxed text-porcelain/80 sm:text-[17px]">
        {INTRO_PARAGRAPHS.map((text) => (
          <p key={text}>
            <Lines text={text} />
          </p>
        ))}
      </div>
      <p className="mt-8 font-display text-xs font-normal tracking-[0.18em] text-saffron uppercase">{INTRO_META}</p>
      <PrimaryButton
        onClick={() => onStart(resumeAt ?? { kind: 'question', index: 0 })}
        className="mt-5 w-full sm:w-auto sm:self-start"
      >
        {resumeLabel ?? 'Inizia'}
        <span aria-hidden="true">→</span>
      </PrimaryButton>
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
  const optionRefs = useRef<(HTMLButtonElement | null)[]>([])
  const hasSelection = selected != null

  // Avanti stays focusable while inactive; pressing it sends focus to the answers.
  const tryNext = () => {
    if (hasSelection) onNext()
    else optionRefs.current[0]?.focus()
  }

  const choose = (option: number) => onSelect(option)

  // Letter keys pick an answer (A, B, C, D), matching the letters on screen.
  useEffect(() => {
    const onKey = (event: globalThis.KeyboardEvent) => {
      if (event.metaKey || event.ctrlKey || event.altKey) return
      const target = event.target as HTMLElement | null
      if (target?.closest('input, textarea')) return
      const i = 'abcd'.indexOf(event.key.toLowerCase())
      if (i >= 0 && i < question.options.length) {
        onSelect(i)
        optionRefs.current[i]?.focus()
      }
    }
    window.addEventListener('keydown', onKey)
    return () => window.removeEventListener('keydown', onKey)
  }, [onSelect, question.options.length])

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
              className={`flex min-h-14 w-full cursor-pointer items-center gap-4 rounded-xl border px-4 py-4 text-left backdrop-blur-sm transition-[border-color,background-color,box-shadow] duration-200 sm:px-5 ${focusRingTight} ${
                isSelected
                  ? 'border-saffron bg-porcelain/[0.06] shadow-[inset_0_0_0_1px_var(--oltre-saffron-mango)]'
                  : 'border-porcelain/15 bg-porcelain/[0.03] hover:border-porcelain/40 hover:bg-porcelain/[0.05]'
              }`}
            >
              <span
                aria-hidden="true"
                className={`flex size-7 shrink-0 items-center justify-center rounded-md border text-xs font-semibold transition-colors duration-200 ${
                  isSelected ? 'border-saffron bg-saffron text-charcoal' : 'border-porcelain/20 bg-charcoal/60 text-porcelain/80'
                }`}
              >
                {'ABCD'[i]}
              </span>
              <span className="flex-1 text-base leading-snug font-normal text-porcelain">{option.label}</span>
              <span
                aria-hidden="true"
                className={`flex size-5 shrink-0 items-center justify-center rounded-full border-2 transition-colors duration-200 ${
                  isSelected ? 'border-saffron' : 'border-porcelain/35'
                }`}
              >
                <span
                  className={`size-2.5 rounded-full bg-saffron transition-transform duration-200 ${
                    isSelected ? 'scale-100' : 'scale-0'
                  }`}
                />
              </span>
            </button>
          )
        })}
      </div>

      <ActionBar>
        <div className="flex items-center gap-3">
          <BackButton onClick={onBack} />
          <PrimaryButton inactive={!hasSelection} onClick={tryNext} className="flex-1 sm:flex-none">
            Avanti
            <span aria-hidden="true">→</span>
          </PrimaryButton>
        </div>
      </ActionBar>
    </section>
  )
}

function AnalysisScreen({ focusOnMount, onDone }: { focusOnMount: boolean; onDone: () => void }) {
  const headingRef = useScreenHeading(focusOnMount)
  const [done, setDone] = useState(0)
  const onDoneRef = useRef(onDone)
  useEffect(() => {
    onDoneRef.current = onDone
  })
  useEffect(() => {
    const last = done === ANALYSIS_STEPS.length
    const timer = window.setTimeout(() => (last ? onDoneRef.current() : setDone(done + 1)), last ? 500 : ANALYSIS_STEP_MS)
    return () => window.clearTimeout(timer)
  }, [done])

  return (
    <section className="flex flex-1 flex-col items-center justify-center py-16 text-center" aria-busy="true">
      {/* Placeholder mark: swap for the brand icon (Figma "Icon - Saffron Mango"). */}
      <span aria-hidden="true" className="size-14 animate-spin rounded-full border-[3px] border-saffron/25 border-t-saffron" />
      <h1
        ref={headingRef}
        tabIndex={-1}
        className="mt-8 font-display text-[1.5rem] leading-[1.2] font-black text-balance outline-none sm:text-[2rem]"
      >
        Stiamo analizzando le tue risposte…
      </h1>
      <ul className="mt-6 space-y-3 text-left text-sm" role="status">
        {ANALYSIS_STEPS.map((label, i) => {
          const state = i < done ? 'done' : i === done ? 'active' : 'todo'
          return (
            <li key={label} className={`flex items-center gap-3 ${state === 'todo' ? 'text-porcelain/40' : 'text-porcelain'}`}>
              <span
                aria-hidden="true"
                className={`flex size-5 shrink-0 items-center justify-center rounded-full border-2 ${
                  state === 'done' ? 'border-saffron bg-saffron' : state === 'active' ? 'border-saffron' : 'border-porcelain/25'
                }`}
              >
                {state === 'done' && (
                  <svg viewBox="0 0 16 16" className="size-3 text-charcoal">
                    <path d="M3 8.5 6.5 12 13 4.5" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" />
                  </svg>
                )}
              </span>
              {label}
              <span className="sr-only">{state === 'done' ? ' (fatto)' : state === 'active' ? ' (in corso)' : ''}</span>
            </li>
          )
        })}
      </ul>
    </section>
  )
}

interface EmailScreenProps {
  focusOnMount: boolean
  email: string
  status: SubmitStatus
  onEmailChange: (value: string) => void
  onBack: () => void
  onSubmit: () => void
}

function EmailScreen({ focusOnMount, email, status, onEmailChange, onBack, onSubmit }: EmailScreenProps) {
  const headingRef = useScreenHeading(focusOnMount)
  const emailRef = useRef<HTMLInputElement>(null)
  const headingId = useId()
  const emailId = useId()
  const emailErrorId = useId()
  const noticeId = useId()

  const emailValid = EMAIL_PATTERN.test(email.trim())
  const suggestion = emailValid ? suggestEmail(email.trim()) : null
  // Once flagged, email errors track the value live; before that they wait for a short typing pause.
  const [emailFlagged, setEmailFlagged] = useState(() => email.trim() !== '' && !emailValid)
  const flagTimer = useRef<number | undefined>(undefined)
  useEffect(() => () => window.clearTimeout(flagTimer.current), [])

  const submitting = status === 'submitting'
  const emailError =
    emailFlagged && !emailValid ? (email.trim() ? EMAIL_FORMAT_ERROR : 'Inserisci la tua email per continuare.') : null

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
    if (!emailValid) {
      setEmailFlagged(true)
      emailRef.current?.focus()
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
        Il tuo profilo è pronto. Dove te lo mandiamo?
      </h1>
      <p className="mt-4 text-base leading-relaxed text-porcelain/75">
        Lo vedi subito nella pagina successiva. Via email ti arriva anche la guida pensata per il tuo profilo, da
        rileggere con calma.
      </p>

      <form noValidate onSubmit={handleSubmit} className="flex flex-1 flex-col" aria-busy={submitting}>
        <div className="mt-8">
          <label htmlFor={emailId} className="block text-sm font-semibold text-porcelain">
            La tua email
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
            placeholder="nome@email.it"
            value={email}
            readOnly={submitting}
            onChange={(e) => handleEmailChange(e.target.value)}
            onBlur={() => {
              if (email.trim() && !emailValid) setEmailFlagged(true)
            }}
            aria-invalid={emailError ? true : undefined}
            aria-describedby={`${emailError ? emailErrorId : ''} ${noticeId}`.trim()}
            className={`mt-2 block min-h-14 w-full rounded-xl border bg-porcelain/[0.04] px-4 backdrop-blur-sm text-base text-porcelain transition-colors duration-200 placeholder:text-porcelain/35 focus:outline-2 focus:outline-offset-2 focus:outline-saffron ${
              emailError ? 'border-saffron' : emailValid ? 'border-porcelain/40' : 'border-porcelain/20'
            }`}
          />
          <div id={emailErrorId} aria-live="polite" className="min-h-6 pt-2 text-sm text-porcelain">
            {emailError && <FieldMessage>{emailError}</FieldMessage>}
            {suggestion && (
              <p className="text-porcelain/75">
                Intendevi{' '}
                <button
                  type="button"
                  onClick={() => onEmailChange(suggestion)}
                  className={`cursor-pointer font-semibold text-saffron underline-offset-4 hover:underline ${focusRingTight}`}
                >
                  {suggestion}
                </button>
                ?
              </p>
            )}
          </div>
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
              inactive={!emailValid}
              loading={submitting}
              className="flex-1 sm:flex-none"
            >
              {submitting ? (
                <>
                  <Spinner />
                  Invio in corso…
                </>
              ) : (
                <>
                  Mostrami il risultato
                  <span aria-hidden="true">→</span>
                </>
              )}
            </PrimaryButton>
          </div>
          <p id={noticeId} className="mt-3 flex items-start gap-2 text-xs leading-relaxed text-porcelain/60">
            <svg aria-hidden="true" viewBox="0 0 16 16" className="mt-0.5 size-3.5 shrink-0 text-saffron">
              <rect x="3" y="7" width="10" height="7" rx="1.5" fill="none" stroke="currentColor" strokeWidth="1.5" />
              <path d="M5.5 7V5a2.5 2.5 0 0 1 5 0v2" fill="none" stroke="currentColor" strokeWidth="1.5" />
            </svg>
            <span>
              Usiamo la tua email solo per il risultato e la guida. Niente spam.{' '}
              {/* Privacy policy URL pending. */}
              <a href="#" className="text-porcelain/80 underline underline-offset-2 hover:text-porcelain">
                Informativa privacy
              </a>
            </span>
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
  const name = PROFILE_NAMES[profile]
  const description = PROFILE_DESCRIPTIONS[profile]

  return (
    <section className="flex flex-1 flex-col pt-10 pb-12 sm:pt-16">
      <h1 ref={headingRef} tabIndex={-1} className="outline-none">
        <span className="block font-display text-xs font-normal tracking-[0.18em] text-saffron uppercase">
          Il tuo profilo
        </span>
        <span className="mt-3 block font-display text-[3.25rem] leading-none font-black break-words text-porcelain uppercase sm:text-7xl">
          {name}
        </span>
      </h1>

      <div className="mt-8 max-w-[62ch] space-y-4 text-base leading-relaxed text-porcelain/85 sm:text-[17px]">
        {description ? (
          description.map((text) => (
            <p key={text}>
              <Lines text={text} />
            </p>
          ))
        ) : (
          <p className="rounded-xl border border-dashed border-porcelain/30 p-4 text-sm text-porcelain/60">
            [Descrizione del profilo {name}: testo in arrivo da Pietro]
          </p>
        )}
      </div>

      <a
        href={RESULT_CTA_HREF[profile]}
        className={`mt-10 inline-flex min-h-14 w-full items-center justify-center gap-2.5 rounded-full bg-saffron px-7 text-base font-semibold text-charcoal transition-[background-color,transform] duration-200 hover:bg-saffron/90 active:scale-[0.98] sm:w-auto sm:self-start ${focusRing}`}
      >
        Vedi il tuo risultato
        <span aria-hidden="true">→</span>
      </a>
    </section>
  )
}
