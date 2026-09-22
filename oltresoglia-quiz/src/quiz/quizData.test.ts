import { describe, expect, it } from 'vitest'
import { QUESTIONS, computeTotals, isValidAnswerArray, pickResult, type ProfileTotals } from './quizData'

const totals = (t: Partial<ProfileTotals>): ProfileTotals => ({ ORBITA: 0, ZENIT: 0, AFELIO: 0, ECLISSI: 0, ...t })

describe('quiz data', () => {
  it('has 8 questions in the brief order with the expected option counts', () => {
    expect(QUESTIONS.map((q) => q.id)).toEqual([1, 2, 3, 4, 5, 6, 7, 8])
    expect(QUESTIONS.map((q) => q.options.length)).toEqual([4, 4, 3, 4, 4, 4, 4, 4])
  })

  it('matches the scoring table exactly', () => {
    const table = QUESTIONS.map((q) => q.options.map((o) => (o.award ? `${o.award.profile} ${o.award.points}` : '—')))
    expect(table).toEqual([
      ['ORBITA 8', 'ZENIT 6', 'AFELIO 8', 'ECLISSI 6'],
      ['—', 'AFELIO 3', 'AFELIO 8', 'AFELIO 15'],
      ['ORBITA 12', 'ORBITA 4', '—'],
      ['ECLISSI 8', 'ZENIT 10', 'ZENIT 13', 'ORBITA 6'],
      ['ZENIT 8', 'ECLISSI 13', 'ORBITA 6', 'AFELIO 8'],
      ['ORBITA 4', 'ZENIT 4', 'AFELIO 4', 'ECLISSI 4'],
      ['ORBITA 4', 'ZENIT 4', 'AFELIO 4', 'ECLISSI 4'],
      ['ORBITA 5', 'ZENIT 5', 'AFELIO 5', 'ECLISSI 5'],
    ])
  })
})

describe('computeTotals', () => {
  it('keeps four independent totals', () => {
    // Q1 opt1, Q2 opt4, Q3 opt1, Q4 opt3, Q5 opt2, Q6 opt3, Q7 opt4, Q8 opt2
    expect(computeTotals([0, 3, 0, 2, 1, 2, 3, 1])).toEqual({ ORBITA: 20, ZENIT: 18, AFELIO: 19, ECLISSI: 17 })
  })

  it('awards nothing for no-award options and unanswered questions', () => {
    expect(computeTotals([null, 0, 2, null, null, null, null, null])).toEqual(totals({}))
  })
})

describe('pickResult', () => {
  it('returns the highest total', () => {
    expect(pickResult(totals({ ZENIT: 30, AFELIO: 12 }))).toBe('ZENIT')
    expect(pickResult(totals({ ECLISSI: 9, ORBITA: 8 }))).toBe('ECLISSI')
  })

  it('breaks ties AFELIO › ORBITA › ZENIT › ECLISSI, only among the leaders', () => {
    expect(pickResult(totals({ AFELIO: 20, ORBITA: 20, ZENIT: 20, ECLISSI: 20 }))).toBe('AFELIO')
    expect(pickResult(totals({ ORBITA: 20, ZENIT: 20, ECLISSI: 20 }))).toBe('ORBITA')
    expect(pickResult(totals({ ZENIT: 20, ECLISSI: 20, AFELIO: 19 }))).toBe('ZENIT')
    expect(pickResult(totals({ ECLISSI: 21, AFELIO: 20, ORBITA: 20 }))).toBe('ECLISSI')
  })

  it('resolves ties that real answer sets produce', () => {
    const cases: [number[], string][] = [
      [[0, 0, 1, 0, 3, 1, 2, 1], 'AFELIO'], // ORBITA 12 = AFELIO 12
      [[0, 0, 0, 0, 1, 1, 3, 0], 'ORBITA'], // ORBITA 25 = ECLISSI 25
      [[0, 0, 0, 2, 0, 1, 2, 0], 'ORBITA'], // ORBITA 25 = ZENIT 25
      [[0, 0, 1, 1, 1, 1, 1, 3], 'ZENIT'], // ZENIT 18 = ECLISSI 18
      [[0, 1, 1, 0, 0, 1, 2, 2], 'AFELIO'], // AFELIO = ORBITA = ZENIT = 12
    ]
    for (const [answers, expected] of cases) expect(pickResult(computeTotals(answers))).toBe(expected)
  })
})

describe('isValidAnswerArray', () => {
  it('accepts well-formed arrays and rejects stale or tampered data', () => {
    expect(isValidAnswerArray([0, null, 2, 3, null, null, null, null])).toBe(true)
    expect(isValidAnswerArray([0, 0, 3, 0, 0, 0, 0, 0])).toBe(false) // Q3 has only 3 options
    expect(isValidAnswerArray([0, 0, 0])).toBe(false)
    expect(isValidAnswerArray({ answers: [] })).toBe(false)
    expect(isValidAnswerArray([0.5, null, null, null, null, null, null, null])).toBe(false)
  })
})
