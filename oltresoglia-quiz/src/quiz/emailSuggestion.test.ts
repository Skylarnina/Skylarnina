import { describe, expect, it } from 'vitest'
import { suggestEmail } from './emailSuggestion'

describe('suggestEmail', () => {
  it('suggests the likely domain for common typos', () => {
    expect(suggestEmail('mario@gmial.com')).toBe('mario@gmail.com')
    expect(suggestEmail('mario@hotmial.it')).toBe('mario@hotmail.it')
    expect(suggestEmail('mario@libro.it')).toBe('mario@libero.it')
  })
  it('stays quiet for correct or unrelated domains', () => {
    expect(suggestEmail('mario@gmail.com')).toBeNull()
    expect(suggestEmail('mario@oltresoglia.it')).toBeNull()
    expect(suggestEmail('mario@')).toBeNull()
  })
})
