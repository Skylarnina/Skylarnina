# The Schedule Test: UX/UI System

A multi-step lifestyle quiz for a high-end fitness coaching brand. It shows one question per screen and sorts each user into one of four profiles. From there the user goes to a personalized guide, then a VSL, then WhatsApp.

The working prototype is in [`index.html`](./index.html). It's one file with no dependencies apart from Google Fonts.

> Design stance: this should feel like **Apple onboarding, not a form**. Each screen asks for one decision and shows one clear next action, and nothing else competes for attention. The user should feel *"this is reading me"*, not *"this is surveying me"*.

---

## 0. Profiles and scoring model

| Key | Profile | Who | Core need |
|---|---|---|---|
| `operator` | **The Operator** | Founders, owners, self-employed | Short, high-return sessions with no decisions to make |
| `rotator` | **The Rotator** | Shift workers (nights, rotations, on-call) | Training, sleep and food synced to the current shift |
| `nomad` | **The Nomad** | Frequent travelers | A system that works in any hotel room or time zone |
| `grinder` | **The Grinder** | Long desk days, 9+ hours seated | Undo the desk and build strength around fixed hours |

Each answer adds weighted points to one or two profiles. The highest total wins. **Q1 (work type) breaks ties** because it's the most direct signal.

| # | Screen label | Question | Weight | Purpose |
|---|---|---|---|---|
| 1 | Your work | What does your work look like? | 3 | Primary signal and tie-breaker |
| 2 | Your week | How predictable is a normal week? | 2 | Confirms the pattern |
| 3 | Recovery | How much do you sleep on a normal night? | 1–2 | Recovery load (split across profiles) |
| 4 | Timing | When could you realistically train? | 2 | Training window |
| — | *Halfway moment* | "Halfway there" + early read | — | Keeps momentum (not a question) |
| 5 | Session length | How much time can you give each session? | 1 | Session format |
| 6 | Obstacles | What usually knocks you off track? | 2 | Pain point, used in result copy |
| 7 | Your goal | What do you want most in the next 90 days? | 0 | Adds a `goal` tag to personalize the guide and VSL |
| 8 | Nutrition | How do you eat on a typical day? | 1 | Nutrition angle |

Question order is deliberate. It starts easy and factual (work, week) and moves to more personal ground (sleep, obstacles) once the user has already committed. The goal question sits near the end so the user's intent is fresh when the result appears.

---

## 1. Screen-by-screen structure

```
[Entry] → Q1 → Q2 → Q3 → Q4 → [Halfway] → Q5 → Q6 → Q7 → Q8 → [Analyzing…] → Result page (separate)
```

| Screen | Job | Primary action | Exit to |
|---|---|---|---|
| **Entry** | Hook the user, set expectations, spark curiosity | Start the test | Q1 |
| **Q1–Q8** | One decision each | Tap an answer (auto-advances) | Next Q, Halfway, or Analyzing |
| **Halfway** | Reward progress and show the quiz is "thinking" | Keep going | Q5 |
| **Analyzing** | Make the result feel earned (2 s) | None (automatic) | Result page |
| **Result** *(separate build)* | Reveal the profile and lead into guide → VSL → WhatsApp | See my plan | Funnel |

The prototype also includes a result **preview** with profile, match breakdown and handoff JSON. It shows exactly what the result page receives.

---

## 2. Layout for each screen

Everything sits in one column, max **560px** wide, with **20px** side gutters. On phones, the layout follows the thumb: content reads from the top and the action sits in a sticky dock at the bottom.

```
┌──────────────────────────────┐
│ ‹   ▰▰▰▱▱▱▱▱            3/8  │  ← Top bar (60px, sticky)
│                              │
│ 03 / 08 · RECOVERY           │  ← Eyebrow (mono, accent)
│ How much do you sleep        │  ← Question (display, 27–36px)
│ on a normal night?           │
│                              │
│ ┌──────────────────────────┐ │
│ │ A  Under 5 hours       ○ │ │  ← Answer cards, min 68px tall,
│ │    Running on fumes      │ │     10px apart
│ └──────────────────────────┘ │
│ ┌──────────────────────────┐ │
│ │ B  5–6 hours           ● │ │  ← Selected: accent border, glow, check
│ └──────────────────────────┘ │
│ …                            │
│                              │
│   Tap the one that fits best │  ← Dock: hint, or Continue if answered
└──────────────────────────────┘
```

### Entry
- **Top bar:** brand mark and wordmark on the left, "60-sec test" pill on the right.
- **Eyebrow:** THE SCHEDULE TEST
- **Headline (hook):** *"Your schedule isn't the problem. **Your plan is.**"* The second sentence is set in the accent color. It tells a busy professional that the problem isn't their fault.
- **Lede (what they get):** "Eight quick questions about how you actually live. Get your lifestyle profile — and a training plan built around it."
- **Curiosity grid:** "Which one are you?" above a 2×2 grid of the four profiles. It works like an open loop: people take the test to find out which one they are.
- **Dock:** a full-width **Start the test** button. Below it: `60 SECONDS · 8 QUESTIONS · NO SIGN-UP`.
- **Returning users:** the button becomes **Pick up at question N**, with a quieter "Start over" link below it.

### Question (×8)
- **Top bar:** back chevron (44×44 px), progress bar with 8 segments, `N/8` counter.
- **Eyebrow:** `03 / 08 · RECOVERY`. The number is repeated here because the eyebrow is what users look at first.
- **Question:** 5–9 words, conversational, no jargon.
- **4 answer cards:** a bold label of 2–5 words plus a muted sub-line so people recognize themselves ("Nights, rotations, on-call").
- **Dock:** before an answer, a hint ("Tap an answer — you'll move on automatically" on Q1 only). After an answer, for example when the user comes back, a **Continue** button. On the last question the button reads **See my result**.

### Halfway (after Q4)
- A progress ring animates to 50%, with "Halfway there."
- An **Early read** card gives a one-line insight based on the leading profile so far. Example: *"Your body clock keeps moving. Most plans assume a 9-to-5 — yours won't."*
- **Keep going** button. Below it: `4 QUESTIONS LEFT · ABOUT 30 SECONDS`.

### Analyzing
- There's no back button, and the progress bar shows 8/8.
- The ring fills from 0 to 100% with the percentage in the center.
- Headline: "Analyzing your responses…"
- A three-step checklist ticks off in order: *Mapping your weekly schedule → Weighing sleep and recovery → Matching your lifestyle profile*.
- The whole screen lasts **2.0 s** plus a 0.3 s hold, then moves on by itself.

---

## 3. Component system

### Tokens

| Token | Value | Use |
|---|---|---|
| `--ground` | `#0D0C0B` | Page background (warm near-black) |
| `--surface` | `#171513` | Answer cards, insight card |
| `--surface-2` | `#211E1B` | Card hover |
| `--line` / `--line-strong` | warm white at 9% / 18% | Hairlines, empty progress segments |
| `--text` | `#F6F2EE` | Primary text |
| `--muted` | `#A39A91` | Sub-lines, lede |
| `--faint` | `#756D66` | Labels, meta, hints |
| `--ember` | `#FF6B1A` | Accent: selection, CTA, progress |
| `--ember-hi` | `#FF8A47` | CTA hover |
| `--ember-ink` | `#1A0900` | Text on the accent color |

All neutrals lean slightly warm toward the orange, so the palette reads as one piece and the grays don't look like defaults.

**Type**
- **Archivo** (wide 112%, weight 750, tracking −2.5%) for headlines and questions. It's wide and athletic, closer to sportswear branding than to SaaS.
- **Geist** 400–620 for body text and buttons.
- **Geist Mono** 500, uppercase, +0.1–0.14em tracking, for eyebrows, counters and meta. It gives the quiz a "precision instrument" feel.

| Role | Size | Line height |
|---|---|---|
| Display (entry, result) | `clamp(38px, 10.6vw, 56px)` | 1.02 |
| Question | `clamp(27px, 7.4vw, 36px)` | 1.1 |
| Lede | 17px | 1.5 |
| Option label | 16.5px, weight 560 | — |
| Option sub-line | 14px | — |
| Meta | 11.5px mono | — |

**Radius:** 18px for cards and the insight card, 14px for options, 16px for the CTA, 9px for key tiles. **Elevation:** a 1px inner top highlight plus a long, soft drop shadow. Only the selected card and the CTA get an orange glow.

### Buttons

| Variant | Spec | States |
|---|---|---|
| **Primary** | Full width, 58px tall, 16px radius, accent fill, dark ink text, trailing arrow | Hover: lighter fill and the arrow moves 3px right · Press: `scale(.975)` · Focus: 2px white ring, 3px offset |
| **Text** | 44px tall, muted text | Hover: text color · Focus: accent ring |
| **Back** | 44×44 icon button, muted chevron | Hover: surface fill · Hidden on entry, analyzing and result |

### Answer card
- Grid layout: `32px key tile | label + sub-line | 22px check`. Minimum 68px tall with 13–16px padding. The **whole card** is the tap target.
- **Rest:** surface background, hairline border, soft shadow.
- **Hover (pointer devices only):** raised surface, stronger border.
- **Press:** `scale(.982)`.
- **Selected:** accent border, a 1px inner accent ring, 11% accent tint, orange glow. The key tile fills with the accent. The check circle pops (0.55 → 1.14 → 1) and the check mark draws in.
- **While committing:** the unselected cards fade to 42%. This confirms the choice before the screen moves on.
- **Accessibility:** `role="radiogroup"` with `role="radio"` on each card, `aria-checked`, roving tabindex, and a visible focus ring.

### Progress indicator
- **8 segments** instead of one continuous bar. Each segment is one question, so users can count what's left at a glance.
- Finished segments are filled with the accent. The current segment is filled 40% and pulses slowly. Upcoming segments stay as hairlines.
- A mono `N/8` counter sits on the right. The bar uses `role="progressbar"`, and each step is announced through an `aria-live` region.
- **Ambient glow:** a soft orange radial glow at the top of the page brightens as progress goes from 0 to 1. Progress feels like building heat, which fits a fitness brand.

### Inputs
There are **no text inputs** in the quiz. Every answer is a tap. If lead capture is added, it belongs on the result page (see §6).

---

## 4. Interaction behaviors

| Moment | Behavior | Timing |
|---|---|---|
| Tap an answer | Selected state, haptic tick (`vibrate(8)` on Android), other cards fade | Instant |
| Auto-advance | Moves to the next screen. Tapping a different card within the window switches the answer and restarts the timer. | 380 ms |
| Screen change (forward) | Old screen fades and slides 17px left. New screen slides in from 28px right. | 170 ms out, 380 ms in |
| Screen change (back) | Same motion, mirrored | Same |
| Content entrance | Eyebrow, title and cards rise 10px and fade in, one after another | 45 ms stagger |
| Progress | Segment fills | 500 ms ease-out |
| Halfway ring | Fills to 50% | 1 s |
| Analyzing | Ring 0→100% (ease-in-out), checklist ticks at 30% / 62% / 92% | 2.0 s + 0.3 s hold |

**Easing:** `cubic-bezier(.2,.8,.2,1)` for entrances, `cubic-bezier(.4,0,1,1)` for exits.

**Navigation**
- **No page reloads.** The quiz is one screen that swaps its content.
- **The browser or Android back button** goes to the previous question instead of leaving the quiz. The prototype adds one `history.pushState` entry per step to make this work.
- Going **back** keeps the earlier answer selected and shows a **Continue** button, so nothing needs re-entering.
- Coming **back from Q5** skips the Halfway screen and goes straight to Q4. The Halfway screen only shows once.
- **Keyboard:** `A–D` or `1–4` picks an answer. `↑`/`↓` moves between cards. `Enter` continues. `Esc`, `Backspace` or `←` goes back.
- **Focus:** after each change, focus moves to the new headline so screen readers announce it.
- **Reduced motion:** slides turn into short fades, the stagger, glow drift and pulse are switched off, and auto-advance drops to 220 ms.

**Persistence**
- Answers save to `localStorage` after every tap. If the user leaves and returns, the entry screen offers "Pick up at question N".
- The saved state is cleared when the quiz completes.

**Handoff**
When the quiz finishes, it fires a `scheduletest:complete` window event carrying this data:

```json
{
  "profile": "rotator",
  "goal": "energy",
  "scores": { "operator": 3, "rotator": 13, "nomad": 4, "grinder": 1 },
  "answers": { "work": "I work shifts", "...": "..." },
  "durationSec": 41
}
```

- If `CONFIG.resultUrl` is set (for example `/result/{profile}?goal={goal}`), the quiz redirects there.
- Analytics events go to `dataLayer` as `schedule_test_start`, `_question_view`, `_answer` (with time-to-answer in ms), `_back`, `_resume` and `_complete`.

---

## 5. Mobile responsiveness

- **Mobile first.** Everything is built for widths of 360–430px. Desktop just centers the same column.
- **Thumb zone.** The primary action lives in a sticky bottom dock with a gradient fade behind it, so it never gets scrolled away. The dock respects `env(safe-area-inset-bottom)`, and the page uses `viewport-fit=cover`.
- **Tap targets.** Answer cards are at least 68px tall and the CTA is 58px. Back and text buttons are at least 44×44. Cards sit 10px apart so a slight mis-tap doesn't hit the neighbor.
- **Fits one screen.** The title and all 4 answers fit above the dock on a typical 390×740 phone viewport. On shorter screens the page scrolls and the dock stays pinned. Sub-lines are written to stay on one line at 360px.
- **Fluid type.** Headlines use `clamp()` so they scale smoothly between 360px phones and desktop, and `text-wrap: balance` prevents a lonely last word.
- **Hover is pointer-only.** Hover styles sit behind `@media (hover: hover)` so they never stick on touch devices. The "Keys A–D work too" hint only shows with a fine pointer.
- **Desktop (≥720px wide and ≥700px tall).** The content block is vertically centered and the dock sits right under the answers, so there's no gap to the bottom of a tall screen.
- **Performance.** There are no images and no frameworks. It's one HTML file plus fonts, and all motion uses `transform` and `opacity` only.

---

## 6. Improving completion rate

**Already built into the prototype**
1. **Auto-advance.** One tap per question: 8 questions means 8 taps.
2. **Question count up front.** "60 seconds · 8 questions · No sign-up" answers "how long will this take?" before the user asks.
3. **Curiosity loop.** "Which one are you?" and the four profiles create a question only finishing can answer.
4. **Halfway reward.** An early read at 50% shows the quiz is already working, right where drop-off usually peaks.
5. **Easy questions first.** Factual questions come before personal ones. Once people have answered 3–4, they tend to finish.
6. **Resume.** Answers persist, and returning users jump straight back in.
7. **Back button safety.** The hardware back button never throws someone out of the quiz.
8. **Earned result.** The 2-second analysis makes the profile feel calculated, which raises trust in the funnel after it.
9. **No typing and no email gate before the result.** Asking for contact details before the value is the biggest drop-off in quiz funnels.

**Recommended next**
1. **Ask for contact details after the reveal, not before.** Put the WhatsApp opt-in on the result page ("Send my plan to WhatsApp"). Users say yes more often once they've seen their profile.
2. **Social proof on entry.** Add *real* numbers ("Taken by N professionals") or one short quote from a client who fits a profile. Don't invent them.
3. **Coach presence.** A small circular coach photo on entry and on the Analyzing screen ("Coach X is reviewing your answers") adds a human touch.
4. **Instrument drop-off per question.** Watch `_question_view` against `_answer` for each step. Any question with more than 8% drop-off or a median answer time over 6 s needs rewording.
5. **A/B tests worth running:** the headline hook, whether the Halfway screen appears, 380 ms vs 250 ms auto-advance, and "Start the test" vs "Find my profile".
6. **Traffic-source aware entry.** Pass `?src=ig` or similar and adjust the hook (for example, lead with shift workers for ads aimed at nurses).
7. **Re-engagement.** For people who drop out and gave a WhatsApp number earlier in the funnel, send "You're 3 questions from your profile" with a link to resume.
8. **Speed budget.** Keep the page under 100 KB and visible in under 1 s on 4G. Every extra second of load time costs more completions than any design tweak can win back.
