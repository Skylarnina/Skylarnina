/**
 * OLTRESOGLIA quiz — copy and scoring.
 *
 * Copy is verbatim from the client brief. Questions and options are rendered in
 * exactly this order: never shuffle, reorder or reword them.
 *
 * Scoring lives here only. The UI renders `label` and nothing else from an
 * option, and totals are never kept in component state, persisted or logged.
 */

export type ProfileId = 'ORBITA' | 'ZENIT' | 'AFELIO' | 'ECLISSI'

export type ProfileTotals = Record<ProfileId, number>

/** Each option awards points to at most one profile (`null` = no award). */
export interface QuizOption {
  label: string
  award: { profile: ProfileId; points: number } | null
}

export interface QuizQuestion {
  id: number
  text: string
  options: QuizOption[]
}

/** Index of the chosen option per question, or `null` while unanswered. */
export type AnswerIndices = (number | null)[]

export const QUIZ_TITLE = 'Scopri che tipo di professionista ad alta pressione sei'

export const PROFILE_NAMES: Record<ProfileId, string> = {
  ORBITA: 'Orbita',
  ZENIT: 'Zenit',
  AFELIO: 'Afelio',
  ECLISSI: 'Eclissi',
}

/** Tie-break, applied only among tied leaders. */
export const TIE_BREAK_ORDER: readonly ProfileId[] = ['AFELIO', 'ORBITA', 'ZENIT', 'ECLISSI']

const award = (profile: ProfileId, points: number) => ({ profile, points })

export const QUESTIONS: readonly QuizQuestion[] = [
  {
    id: 1,
    text: 'Come sono i tuoi orari di lavoro?',
    options: [
      { label: "Cambiano da una settimana all'altra: ruoto su fasce diverse o faccio turni", award: award('ORBITA', 8) },
      { label: "Entro sempre alla stessa ora. L'ora di uscita la decide la giornata", award: award('ZENIT', 6) },
      { label: 'Dipende da dove sono: alcune settimane lavoro fuori sede', award: award('AFELIO', 8) },
      { label: 'Entro ed esco quasi sempre alla stessa ora', award: award('ECLISSI', 6) },
    ],
  },
  {
    id: 2,
    text: 'Quante notti al mese passi fuori città per lavoro (in albergo, alloggio ecc.)?',
    options: [
      { label: 'Nessuna', award: null },
      { label: 'Una o due', award: award('AFELIO', 3) },
      { label: 'Tre o cinque', award: award('AFELIO', 8) },
      { label: 'Sei o più', award: award('AFELIO', 15) },
    ],
  },
  {
    id: 3,
    text: 'Ti capita di lavorare di notte, o di iniziare prima delle sei del mattino?',
    options: [
      { label: 'Sì, fa parte del mio giro di turni', award: award('ORBITA', 12) },
      { label: 'Ogni tanto, quando serve', award: award('ORBITA', 4) },
      { label: 'Mai', award: null },
    ],
  },
  {
    id: 4,
    text: 'Contando anche mail, messaggi e chiamate fuori orario, il tuo lavoro occupa:',
    options: [
      { label: 'Otto ore o meno', award: award('ECLISSI', 8) },
      { label: 'Nove o dieci ore', award: award('ZENIT', 10) },
      { label: 'Più di dieci ore', award: award('ZENIT', 13) },
      { label: 'Dipende dal turno che ho quella settimana', award: award('ORBITA', 6) },
    ],
  },
  {
    id: 5,
    text: 'Chiudi la giornata di lavoro. Cosa succede subito dopo?',
    options: [
      { label: 'Non chiude davvero: continuo a rispondere e a pensarci', award: award('ZENIT', 8) },
      { label: 'Comincia il resto: figli da prendere, spesa, casa, un genitore da sentire', award: award('ECLISSI', 13) },
      { label: 'Dipende dal turno: a volte è mattina, a volte è notte', award: award('ORBITA', 6) },
      { label: 'Inizio a pensare alla prossima trasferta', award: award('AFELIO', 8) },
    ],
  },
  {
    id: 6,
    text: 'Qual è il momento in cui il tuo piano salta più spesso?',
    options: [
      { label: 'Il giorno in cui cambia il turno', award: award('ORBITA', 4) },
      { label: 'La sera in cui esco più tardi del previsto', award: award('ZENIT', 4) },
      { label: 'I giorni in cui dormo fuori casa', award: award('AFELIO', 4) },
      { label: 'Nessuno in particolare: non salta di colpo, si consuma un pezzo alla volta', award: award('ECLISSI', 4) },
    ],
  },
  {
    id: 7,
    text: 'Qual è il pasto più difficile della tua settimana?',
    options: [
      { label: 'Quello del turno di notte, che non so nemmeno come chiamare', award: award('ORBITA', 4) },
      { label: 'La cena tardi, dopo un pranzo saltato o mangiato in dieci minuti', award: award('ZENIT', 4) },
      { label: "Il buffet dell'hotel, l'autogrill, la cena con il cliente", award: award('AFELIO', 4) },
      { label: 'Quello che mangio in piedi, mentre preparo per gli altri', award: award('ECLISSI', 4) },
    ],
  },
  {
    id: 8,
    text: 'Quale di queste frasi ti sei detto più spesso?',
    options: [
      { label: '«Con i miei orari è impossibile»', award: award('ORBITA', 5) },
      { label: '«Da lunedì mi organizzo»', award: award('ZENIT', 5) },
      { label: '«Quando torno riprendo»', award: award('AFELIO', 5) },
      { label: "«In teoria il tempo ce l'avrei»", award: award('ECLISSI', 5) },
    ],
  },
]

export const TOTAL_QUESTIONS = QUESTIONS.length

/** Four independent running totals — never a single combined score. */
export function computeTotals(answers: AnswerIndices): ProfileTotals {
  const totals: ProfileTotals = { ORBITA: 0, ZENIT: 0, AFELIO: 0, ECLISSI: 0 }
  QUESTIONS.forEach((question, i) => {
    const choice = answers[i]
    if (choice == null) return
    const awarded = question.options[choice]?.award
    if (awarded) totals[awarded.profile] += awarded.points
  })
  return totals
}

/** Highest total wins; ties among the leaders resolve AFELIO › ORBITA › ZENIT › ECLISSI. */
export function pickResult(totals: ProfileTotals): ProfileId {
  const max = Math.max(...TIE_BREAK_ORDER.map((p) => totals[p]))
  return TIE_BREAK_ORDER.find((p) => totals[p] === max)!
}

export function isComplete(answers: AnswerIndices): answers is number[] {
  return answers.length === TOTAL_QUESTIONS && answers.every((a) => a != null)
}

export function emptyAnswers(): AnswerIndices {
  return QUESTIONS.map(() => null)
}

/** True when `raw` is a well-formed answer array for this exact quiz (used to vet localStorage). */
export function isValidAnswerArray(raw: unknown): raw is AnswerIndices {
  return (
    Array.isArray(raw) &&
    raw.length === TOTAL_QUESTIONS &&
    raw.every(
      (a, i) => a === null || (Number.isInteger(a) && a >= 0 && a < QUESTIONS[i].options.length),
    )
  )
}
