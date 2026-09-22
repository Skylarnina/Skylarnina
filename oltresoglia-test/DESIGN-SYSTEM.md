# Test Oltresoglia: UX/UI System

**"Scopri che tipo di professionista ad alta pressione sei"**

This is a multi-step profiling test for Oltresoglia. It asks 8 questions, collects the user's email, then shows a short analysis before the result. The result feeds the funnel: guide → VSL → WhatsApp.

The working prototype is [`index.html`](./index.html), a single file whose only external dependency is Manrope from Google Fonts.

## Sources

| What | Source | Used for |
|---|---|---|
| Questions, answers, points, tie-breaker, email position | `test.pdf` (4 pages) | Copied word for word into the `QUESTIONS` array |
| Wordmark, icon, favicon, social marks, colours | `Source Files - Oltresoglia.fig` | Logo SVG paths extracted from the file (no redrawing), colour tokens |
| Typeface | Same `.fig` (the only typeface used) | Manrope for all text |

> **What the Figma file does not include.** It is a logo source file. It has the marks in 5 colour variants, but no type scale, spacing scale, component or tone-of-voice guidelines. The scale, spacing, radii and UI microcopy below are built from the brand's own elements: the wide italic wordmark, the ~10° forward lean, the rounded-square icon and the direct Italian of the test copy. If a fuller brand guide exists, the tokens in §3 are the only place to update.

---

## 1. Screen-by-screen breakdown

```
[Ingresso] → D1 → D2 → D3 → D4 → D5 → D6 → D7 → D8 → [Email] → [Analisi 2 s] → Result page (separate)
```

| # | Screen | Purpose | Main action | Where it leads |
|---|---|---|---|---|
| 0 | **Ingresso** (entry) | Promise, time estimate, curiosity | **Inizia il test** | D1 |
| 1–8 | **Domanda N** (question) | One decision per screen | Tap an answer (it moves on by itself) | Next question → Email |
| 9 | **Email** | Collect the lead before the reveal | **Mostrami il risultato** | Analisi |
| 10 | **Analisi** (analysis) | Makes the result feel earned (≈2 s) | None (moves on automatically) | Result page |
| 11 | **Risultato** *(built separately)* | Reveals the profile and starts the funnel | Vedi il tuo risultato | Guide → VSL → WhatsApp |

The prototype also contains a result preview: the profile name, the points per profile and the JSON the result page receives. This lets the funnel team see the exact handoff.

---

## 2. Layout of each screen

All screens share the same base:

- **Column:** a single column up to **560 px** wide, with **20 px** side margins.
- **Background:** `#050505` (Dark Charcoal).
- **Top bar:** 64 px, pinned to the top.
- **Bottom action area:** pinned to the bottom of the screen, where the thumb rests.

```
┌──────────────────────────────┐
│ ‹   ▰▰▰▱▱▱▱▱            3/8  │  Top bar: back · 8 slanted segments · counter
│                              │
│ DOMANDA 3 DI 8               │  Eyebrow (Saffron, caps, +16% tracking)
│ Ti capita di lavorare di     │  Question (Manrope 800, 24–32 px)
│ notte, o di iniziare prima   │
│ delle sei del mattino?       │
│                              │
│ ┌──────────────────────────┐ │
│ │ A  Sì, fa parte del mio  ○│ │  Answer card ≥ 64 px, full width, 10 px gap
│ │    giro di turni          │ │
│ └──────────────────────────┘ │
│ ┌──────────────────────────┐ │
│ │ B  Ogni tanto, quando    ●│ │  Selected: Saffron border + tint + check
│ └──────────────────────────┘ │
│ ┌──────────────────────────┐ │
│ │ C  Mai                   ○│ │
│ └──────────────────────────┘ │
│                              │
│ Scegli quella più vicina…    │  Action area: hint, or "Avanti" when revisiting
└──────────────────────────────┘
```

### 0 · Entry
- **Top bar:** the OLTRESOGLIA wordmark in Porcelain (vector taken straight from the Figma file).
- **Eyebrow:** `8 DOMANDE · 60–90 SECONDI`, so the time estimate is visible before the title.
- **Title (H1):** *Scopri che tipo di professionista **ad alta pressione** sei*. "ad alta pressione" is in Saffron because it is the phrase the reader identifies with.
- **Supporting line (optional):** "Otto domande sulla tua settimana vera: orari, trasferte, serate, pasti."
- **"Quale dei quattro sei?":** four chips reading ORBITA · ZENIT · AFELIO · ECLISSI. The names alone create curiosity without giving the result away.
- **Action area:** a full-width **Inizia il test** button with the micro-line `RISULTATO IMMEDIATO · NESSUNA APP DA SCARICARE`.
- **Returning user:** the button changes to **Riprendi dalla domanda N**, with "Ricomincia da capo" as a secondary link.

### 1–8 · Question
- **Eyebrow:** `DOMANDA N DI 8`.
- **Question:** the exact text from the PDF.
- **Answers:** 3 or 4 cards, each with a letter tile (A–D), the full answer text and a check circle.
  - Long answers bold their first clause (up to ":" or "."). Example: **"Cambiano da una settimana all'altra:"** ruoto su fasce diverse o faccio turni.
  - This helps scanning without changing a word.
- **Action area:**
  - Before answering, a small hint. On question 1 it reads "Tocca una risposta per andare avanti", which teaches the auto-advance.
  - On an already-answered question (after going back), an **Avanti** button appears. On D8 it reads **Continua**.
- **Question 3 has 3 answers.** The layout adapts and the keyboard shortcut only accepts A–C.

### 9 · Email
- **Eyebrow:** `ULTIMO PASSO`.
- **Title:** "Il tuo profilo è pronto. Dove te lo mandiamo?"
- **Why we ask:** "Lo vedi subito nella pagina successiva. Via email ti arriva anche la guida pensata per il tuo profilo, da rileggere con calma."
- **Email field:** labelled "La tua email", with placeholder `nome@email.it`.
- **Button:** **Mostrami il risultato**, placed directly under the field, *not* in the pinned bottom area, so it stays visible above the phone keyboard.
- **Reassurance** (lock icon): "Usiamo la tua email solo per il risultato e la guida. Niente spam: ti cancelli con un clic." plus an **Informativa privacy** link.
- The progress bar stays full (8/8) and the back button stays available.

### 10 · Analysis
- No back button.
- The **Oltresoglia icon draws itself** in a Saffron outline, then fills in. The loader is the brand mark.
- **Title:** "Stiamo analizzando le tue risposte…"
- **Checklist in sequence:** Incrocio orari, turni e trasferte → Calcolo quanto pesa davvero la tua giornata → Individuo il tuo profilo.
- **Duration:** 2.0 s plus a 0.3 s pause. If sending the email takes longer, this screen waits for it.

---

## 3. Component system

### Colours (from the Figma file)

| Token | Hex | Brand name | Role |
|---|---|---|---|
| `--charcoal` | `#050505` | Dark Charcoal | Background, text on Saffron |
| `--saffron` | `#EFC04D` | Saffron Mango | The only accent: main button, selection, progress, eyebrows |
| `--porcelain` | `#EBF0F2` | Porcelain | Text, wordmark |
| — | `#000000` / `#FFFFFF` | BlackOut / WhiteOut | Reserved for single-colour logo versions |
| `--surface` / `--surface-2` | `#0F1112` / `#171A1C` | *derived* | Cards / card hover (Charcoal lightened, slightly cool toward Porcelain) |
| `--muted` / `--faint` | `#9CA3A7` / `#697075` | *derived* | Secondary text / labels |
| `--error` | `#FF7A6B` | *functional* | Email errors only |

- **Why dark.** Saffron on Porcelain is only ≈1.5:1 contrast and can't be read as text. On Charcoal, Saffron reaches ≈12:1 and Porcelain ≈17:1. The funnel therefore uses the brand's Dark variant.

### Background photo
A full-bleed training photo (`assets/allenamento.jpg`, set via `CONFIG.backgroundImage`) sits behind every screen:

- **Black and white** (`grayscale(1) contrast(1.12)`), so Saffron stays the only colour on the page.
- **Charcoal scrim:** 72% dark at the top, 58–70% behind the headline, 86% by mid-screen and solid `#050505` at the bottom where cards and buttons sit. It was tested with a bright white stand-in image and the text stayed readable.
- **Strength per screen:** entry 95% → questions and email 38% → analysis 55% → result 70%. The photo sells the brand on the first screen, then steps back so the questions stay the focus.
- It fades in only once loaded. If the file is missing or slow, the plain Charcoal background is shown and nothing is blocked.
- `CONFIG.backgroundFocus` sets which part of the photo stays in frame on narrow phones.

### Typography: Manrope

| Role | Size | Weight | Tracking |
|---|---|---|---|
| Entry title | `clamp(34px, 9.4vw, 50px)` / 1.04 | 800 | −3% |
| Email/analysis title | `clamp(27px, 7.4vw, 36px)` / 1.1 | 800 | −3% |
| Question | `clamp(24px, 6.6vw, 32px)` / 1.16 | 800 | −3% |
| Body | 17 px / 1.5 | 450 | — |
| Answer text | 16 px / 1.38 | 450 (lead clause 700) | — |
| Button | 17 px | 800 | −1% |
| Eyebrow / labels | 11–12 px caps | 700 | +12–16% (echoes the wide wordmark) |
| Profile name | `clamp(48px, 15vw, 76px)` caps | 800 | +4% |

### Brand motif: the ~10° lean
The wordmark and icon lean forward by about 10°. The progress segments reuse the same angle (`skewX(-10deg)`). No other element is slanted, so the motif stays recognisable without clutter.

### Buttons

| Variant | Spec | States |
|---|---|---|
| **Primary** | Full width · 58 px tall · 12 px radius · Saffron with Charcoal text · Manrope 800 · arrow → | Hover `#F5CF6E` with the arrow moving 3 px · press `scale(.975)` · focus: 2 px Porcelain ring · loading `aria-busy` at 75% opacity |
| **Text** | 44 px tall · muted text | Hover Porcelain · focus Saffron ring |
| **Back** | 44×44 · chevron | Hover surface · hidden on entry, analysis and result |

### Answer card

| State | Look |
|---|---|
| Rest | Surface `#0F1112`, 1 px border at 10% opacity, 12 px radius, soft shadow, min 64 px tall, the whole card is tappable |
| Hover (mouse only) | `#171A1C`, stronger border |
| Pressed | `scale(.982)` |
| **Selected** | Saffron border + 1 px inner ring + 9% Saffron tint + glow. The A–D tile turns Saffron. The check circle pops (0.55 → 1.14 → 1) and the tick draws itself |
| While moving on | The other cards fade to 40% |

Accessibility: each question is a `radiogroup` of `radio` cards with `aria-checked`, the arrow keys move between cards, and focus is always visible.

### Progress bar
- **8 slanted segments, one per question.** Completed segments are Saffron. The current one is 40% filled and slowly breathes. Future ones are a 22% Porcelain line.
- A `N/8` counter sits on the right. `role="progressbar"` plus an `aria-live` announcement ("Domanda 3 di 8").
- A faint Saffron glow at the top of the page grows with progress, a quiet sense of crossing the threshold ("oltre la soglia").

### Email field
- **Size:** 58 px tall, 17 px text (≥ 16 px stops iOS from zooming the page when the field is focused).
- **Phone behaviour:** `type="email"`, `inputmode="email"`, `autocomplete="email"`, `autocapitalize="off"`, `enterkeyhint="go"`.
- **Focus:** Saffron border plus a 4 px ring. **Error:** red border and ring, with the message underneath (`aria-invalid`, `aria-describedby`).

---

## 4. Interaction behaviour

| Moment | Behaviour | Timing |
|---|---|---|
| Tap an answer | Immediate selection, 8 ms vibration (Android), other cards fade | 0 ms |
| Auto-advance | Next screen. A second tap within the window changes the answer and restarts the countdown | 380 ms |
| Moving forward | Current screen: fade + 17 px slide left. New screen: from 28 px right | 170 ms out / 380 ms in |
| Moving back | Same animation, mirrored | Same |
| Screen entrance | Eyebrow → title → cards rise 10 px one after another | 45 ms stagger |
| Progress bar | Segment fills | 500 ms ease-out |
| Invalid email | Form shakes, message appears, focus returns to the field | 360 ms |
| Mistyped domain | On leaving the field, `mario@gmial.com` → "Intendevi **mario@gmail.com**?" (tap to correct) | On blur |
| Analysis | Icon draws (1.4 s) + fills; checklist at 30/62/92% | 2.0 s + 0.3 s |

Easing: `cubic-bezier(.2,.8,.2,1)` when entering, `cubic-bezier(.4,0,1,1)` when leaving.

**Navigation and safety**
- **No page reloads.** It is a single page that swaps content.
- **Back works everywhere.** The browser or Android back button goes to the previous question instead of leaving the test (`history.pushState` for each step).
- **Answers are remembered.** Going back shows the previous answer selected, with the **Avanti** button available.
- **Leaving is safe.** Progress is saved in `localStorage` after every tap, and on return the button offers "Riprendi dalla domanda N". The email is **not** saved on the device.
- **Keyboard (desktop):** A–D or 1–4 to answer, ↑/↓ to move, Enter to continue, Esc/Backspace/← to go back.
- **Phone keyboard:** the email field is focused automatically only on desktop, so the keyboard doesn't cover the explanation on phones. On submit the field loses focus, which closes the keyboard before the transition.
- **Reduced motion:** slides become short fades, staggers and loops are switched off, the icon appears already filled, and auto-advance drops to 220 ms.

---

## 5. Mobile-first considerations

- **Designed at 360–430 px.** On desktop the same column simply sits centred.
- **Thumb zone.** Actions live in the pinned bottom area, with a fade behind it and room for the iPhone home indicator (`env(safe-area-inset-bottom)`, `viewport-fit=cover`).
- **Keyboard exception.** On the email screen the button sits directly under the field, because iOS doesn't resize the page when the keyboard opens and a pinned button would end up hidden behind it.
- **Tap targets.** Cards are at least 64 px tall, the button 58 px, and the back and secondary buttons 44×44. 10 px between cards stops accidental taps.
- **Long answers.** Cards grow with their text (up to 3 lines at 360 px). The bold first clause makes them readable at a glance.
- **Fluid type** with `clamp()` and `text-wrap: balance` on titles, so there are no single-word last lines.
- **Hover effects only on mouse devices** (`@media (hover: hover)`), so nothing stays "stuck" on touch screens.
- **Desktop (≥ 720×700):** the content block is vertically centred and the button sits under the answers.
- **Weight:** about 48 KB of HTML, no images, no frameworks. The logo is inline SVG, and animations only use `transform` and `opacity`.

---

## 6. How the scoring works (and how it shows in the UX)

**Rules (from the PDF)**
- Each answer adds its points to one profile. "Nessuna" (D2) and "Mai" (D3) are worth 0.
- The highest total wins.
- **Ties** go by priority: **AFELIO › ORBITA › ZENIT › ECLISSI**.

**Implementation**

```js
const TIE_ORDER = ['AFELIO', 'ORBITA', 'ZENIT', 'ECLISSI'];
// each answer: { text, p: 'ORBITA' | null, pts: 8 }
scores  = sum of pts per profile over the 8 answers given
max     = Math.max(...scores)
profile = TIE_ORDER.find(p => scores[p] === max)   // first in priority order among the tied
```

- **Recalculated from the final answers**, not added up as the user goes. If someone goes back and changes an answer, the result is still correct.
- **Tested on all 49,152 possible combinations** (4·4·3·4·4·4·4·4):
  - Every tie resolves in the correct priority order.
  - Ties occur in 4.3% of combinations.
  - With random answers, results split AFELIO 29% · ORBITA 28% · ZENIT 25% · ECLISSI 17%.
- **The score stays hidden until the end.** No per-profile counters are shown during the test, so the user answers honestly instead of "steering" the result.
- **Computed before the analysis screen** (on email submit), so the result page is ready the instant the animation finishes.

**Handoff to the result page**

When the test finishes it sends a `window` event, `oltresoglia:complete`, with this data:

```json
{
  "email": "mario@gmail.com",
  "profile": "ORBITA",
  "scores": { "AFELIO": 20, "ORBITA": 24, "ZENIT": 17, "ECLISSI": 13 },
  "tieBrokenFrom": null,
  "answers": { "q1": 1, "q2": 4, "q3": 1, "q4": 3, "q5": 2, "q6": 1, "q7": 2, "q8": 3 },
  "durationSec": 58
}
```

- **Sending the lead:** `CONFIG.submitLead()` is where your email platform or CRM gets called. It runs *during* the analysis, so it adds no waiting time.
- **Redirect:** with `CONFIG.resultUrl = '/risultato/{profile}'` the test goes straight to the result page.
- **Analytics** go to `dataLayer`:
  - `oltresoglia_test_start` / `_resume`
  - `_question_view`, `_answer` (with response time in ms), `_back`
  - `_email_view`, `_email_error`, `_email_submit`
  - `_complete`

---

## 7. How to increase completion rate

**Already in the prototype**
1. **One tap per question** thanks to auto-advance: the 8 questions take 8 taps.
2. **Time and question count stated upfront** ("8 domande · 60–90 secondi").
3. **Curiosity loop:** the four profile names are visible from the start, and only by finishing do you find out which one you are.
4. **The first question is the easiest and most factual** (working hours). The personal ones come once the user is already invested.
5. **Email is asked for at peak investment** (after 8 answers), with the title "Il tuo profilo è pronto": the value already exists and they only have to unlock it.
6. **Reassurance at the moment of friction:** why we ask, no spam, privacy link, lock icon.
7. **Typo correction for email domains:** fewer bounces, and fewer people who never receive the guide.
8. **Resume where you left off**, and the back button that never kicks you out of the test.
9. **The analysis doubles as brand reinforcement**, and makes the result feel calculated, not random.

**Next steps**
1. **GDPR/marketing check with your lawyer.** If the email will also be used for newsletters or sales follow-ups (beyond sending the result), you need **separate, optional consent** (an unticked checkbox). The prototype only has the privacy notice link.
2. **Track drop-off per question.** Compare `_question_view` with `_answer`. If a question loses more than 8% of users or takes more than 7 s on median, that's where to step in. **Email is the biggest risk point:** measure `_email_view` against `_email_submit` from day one.
3. **Social proof** on the entry and email screens, only with real numbers ("Già fatto da N professionisti") or a short quote from a client.
4. **A/B tests worth running:**
   - with vs without the "Quale dei quattro sei?" chips
   - email title "Il tuo profilo è pronto" vs "Dove ti mandiamo la guida?"
   - 380 vs 250 ms auto-advance
   - adding an *optional* WhatsApp field on the email screen (it would shorten the funnel)
5. **A midway moment.** If data shows a drop between D4 and D5, add a light "Sei a metà" (you're halfway) screen. It isn't included because it's not in the brief.
6. **Recovering people who drop off:** anyone who arrives from an email/WhatsApp link and leaves gets "Ti mancano 3 domande" (3 questions left) with a link to resume, which works because progress is saved.
7. **Speed budget:** under 1 s to visible content on 4G. Keep Manrope as the only font (already limited to weights 400–800).
