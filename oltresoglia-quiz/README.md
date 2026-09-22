# OLTRESOGLIA — quiz profilo

Multi-step quiz page (React + TypeScript + Tailwind v4 + Framer Motion) that classifies a visitor into
Orbita, Zenit, Afelio or Eclissi.

```bash
npm install
npm run dev       # local dev server
npm test          # scoring + data-integrity tests
npm run build     # typecheck + production build
```

## Where things live

| File | What |
| --- | --- |
| `src/quiz/OltresogliaQuiz.tsx` | The page: intro → 8 questions → email + consent → result |
| `src/quiz/quizData.ts` | Verbatim copy, per-option scoring, totals, tie-break |
| `src/quiz/onQuizComplete.ts` | **Placeholder** submit hook — connect the email platform here |
| `src/index.css` | Brand tokens (`--oltre-*`) and the `Bounded` `@font-face` rules |
| `public/fonts/` | Drop `bounded-black.ttf`, `bounded-regular.ttf`, `bounded-extralight.ttf` here |

## Still to supply

- **Bounded font files** → `public/fonts/` (no code change needed; Archivo Black is the stand-in until then).
- **Result copy per profile** → `RESULT_COPY` in `OltresogliaQuiz.tsx` (`[PIETRO TO PROVIDE …]`).
- **GDPR consent wording + privacy link** → email screen, marked `[PIETRO TO PROVIDE …]`.
- **WhatsApp link** → `whatsappHref` in `RESULT_COPY` (currently `#`).
- **Email platform** → `onQuizComplete` (or pass `onQuizComplete` as a prop). It receives
  `{ answers, totals, result, email, consentedAt }`; throw/reject on failure to show the retry state.

Add `?simulateError` to the URL to test the failed-submission path with the placeholder.
