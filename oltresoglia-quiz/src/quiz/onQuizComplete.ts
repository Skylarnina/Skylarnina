import type { ProfileId, ProfileTotals } from './quizData'

export interface SubmittedAnswer {
  questionId: number
  question: string
  /** 0-based index of the chosen option, in the order shown. */
  optionIndex: number
  answer: string
}

/** Everything stored together at submission — not just the winning profile. */
export interface QuizSubmission {
  answers: SubmittedAnswer[]
  totals: ProfileTotals
  result: ProfileId
  email: string
  /** ISO timestamp of when the GDPR consent box was ticked and submitted. */
  consentedAt: string
}

export type OnQuizComplete = (submission: QuizSubmission) => Promise<void>

/**
 * PLACEHOLDER — replace the body with the real email-platform API call.
 *
 * Resolve when the submission is stored; reject (throw) on any failure and the quiz
 * shows a retry message instead of the result. Do not log the payload: it contains
 * the profile totals, which must never be exposed to the visitor.
 *
 * For QA, add `?simulateError` to the page URL to exercise the failure path.
 */
export const onQuizComplete: OnQuizComplete = async (_submission) => {
  await new Promise((resolve) => setTimeout(resolve, 1200))
  if (new URLSearchParams(window.location.search).has('simulateError')) {
    throw new Error('Simulated submission failure')
  }
}
