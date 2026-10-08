/** Email domain typo suggestion ("Intendevi mario@gmail.com?") for the quiz email step. */

const COMMON_DOMAINS = [
  'gmail.com', 'hotmail.com', 'hotmail.it', 'outlook.com', 'outlook.it', 'live.com', 'live.it', 'icloud.com',
  'yahoo.com', 'yahoo.it', 'libero.it', 'virgilio.it', 'alice.it', 'tiscali.it', 'tim.it', 'fastwebnet.it', 'pec.it',
]

function editDistance(a: string, b: string) {
  const d = Array.from({ length: a.length + 1 }, (_, i) => [i, ...Array<number>(b.length).fill(0)])
  for (let j = 1; j <= b.length; j++) d[0][j] = j
  for (let i = 1; i <= a.length; i++)
    for (let j = 1; j <= b.length; j++)
      d[i][j] = Math.min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1))
  return d[a.length][b.length]
}

/** "mario@gmial.com" → "mario@gmail.com"; null when the domain looks fine or is unknown. */
export function suggestEmail(value: string): string | null {
  const at = value.lastIndexOf('@')
  if (at < 1) return null
  const domain = value.slice(at + 1).toLowerCase()
  if (!domain.includes('.') || COMMON_DOMAINS.includes(domain)) return null
  let best: string | null = null
  let bestDist = 3
  for (const known of COMMON_DOMAINS) {
    const dist = editDistance(domain, known)
    if (dist < bestDist) [best, bestDist] = [known, dist]
  }
  return best && bestDist <= 2 ? value.slice(0, at + 1) + best : null
}
