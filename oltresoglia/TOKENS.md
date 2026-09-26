# OLTRESOGLIA — design tokens (extracted from the test build)

Source of truth read: `oltresoglia-quiz/src/index.css` (tokens) and
`oltresoglia-quiz/src/quiz/OltresogliaQuiz.tsx` (how they are used).
Opacities are Tailwind `/NN` modifiers on the named colour, i.e. alpha over the page ground.

Status key: **=** matches the Contact brief · **≠** differs (decision needed) · **∅** not in the test build.

## Colour

| Token (CSS var) | Test build value | Contact brief says | Status |
| --- | --- | --- | --- |
| `--oltre-dark-charcoal` (ground) | `#050505` | `#050505` | = |
| `--oltre-blackout` | `#000000` (only inside background artwork) | — | — |
| `--oltre-whiteout` | `#FFFFFF`, wordmark only | borders "white at 10–14%" | ≠ test draws borders in Porcelain, not white |
| `--oltre-saffron-mango` (accent) | `#EFC04D` | `#EFC04E` | ≠ 1 step in blue. `#EFC04D` came from the original brief ("exact hex from logo source files") |
| `--oltre-porcelain` (text) | `#EBF0F2` (cool, blue-grey tint) | `#F4F1EA` (warm cream) | ≠ visibly different hue |
| Surface (cards, fields) | no token; `porcelain/3%` answer cards (≈ `#0C0C0C`), `porcelain/4%` input (≈ `#0E0E0E`), `porcelain/6%` selected card | `#101113` surface, `#0B0C0E` nested card | ∅ no solid surface tokens |
| Error | none: palette had no red, so errors use a saffron border and an icon | `#E06B5A` | ≠ new colour |
| WhatsApp | CTA is a saffron pill, since the original brief banned green | `#25D366` fill | ≠ the two pages would style the same action differently |
| Page glow | none; ground is flat charcoal over line-art images (`src/assets/backgrounds/*.svg`) under a charcoal overlay (20–60%) | faint warm radial glow, top centre | ≠ the quiz brief banned gradients, and the test has no glow |

### Text opacity (Porcelain)

| Role | Test build | Contact brief | Status |
| --- | --- | --- | --- |
| Headings | 100% | 100% | = |
| Body / supporting line | 75% (intro, email helper), 80% (consent label) | 64% | ≠ |
| Small labels (progress, eyebrow-like) | 70% | eyebrow is saffron | ≠ progress label is Porcelain 70% with only the current number in saffron |
| Helper / hint | 55% | 40% | ≠ |
| Placeholder | 35% | 40% | ≠ |
| Disabled button text | 45% on `porcelain/10%` fill | — | — |

### Borders (Porcelain)

10% action-bar hairline · 15% answer card · 20% input and secondary button · 25–30% alert and placeholder panels ·
40% hover / valid input · saffron for selected, focused or invalid.
Contact brief: white 10–14% (banner 10%, form card 8%, inputs 12%). **≠** alpha range and base colour.

## Typography

| Role | Test build | Contact brief | Status |
| --- | --- | --- | --- |
| Display family | `'Bounded', 'Archivo Black', …`; `@font-face` 200/400/900 → `/fonts/bounded-{extralight,regular,black}.ttf` | Bounded ExtraLight / Regular / Black / Variable | ∅ **font files not in repo**; stand-in Archivo Black has only one (heavy) weight |
| Display weights used | 900 (question, title, profile name), 400 (progress label, "Il tuo profilo è") | 200 ExtraLight for large, 900 for emphasis | ≠ ExtraLight is never used in the test. With the stand-in, "Domande?" (200) and "Contattaci." (900) would look identical |
| Display case | sentence case for headlines; uppercase + `0.18em` tracking only for small labels | "uppercase where the test does it" | = small labels only |
| Display sizes | intro title 32px → 48px (sm) · question 24px → 36px · profile name 52px → 72px | headline 56px | — new size |
| Body family | Manrope via Google Fonts, variable 200–800 | Manrope local files Light → ExtraBold in `oltresoglia/fonts/` | ≠ source; ∅ files not in repo |
| Body sizes / weights | 16px/400 answers & inputs · 18px intro line · 14px labels & hints · 16px/600 buttons | 16px/300 supporting line · 15px/400 inputs · 11px/500 eyebrow · 12px/300 privacy | ≠ the test never uses weight 300 |
| Button label | Manrope 600, 16px, sentence case ("Avanti →") | Manrope 600–700 caps, tracked 0.12–0.14em ("INVIA", "WHATSAPP") | ≠ |
| Wordmark | retyped text "OLTRESOGLIA", Bounded/Archivo Black 900, 14px, tracking 0.22em, Whiteout, upright | client's italic geometric logotype SVG, never retyped | ≠ **logo SVG not in repo** |

## Shape

| Element | Test build | Contact brief | Status |
| --- | --- | --- | --- |
| Primary / secondary buttons | full pill, height 56px | full pill, 56px | = |
| Answer cards | 12px radius | cards 12–16px | = |
| Inputs | 12px radius, **56px** tall, 16px text | 12px radius, **52px** tall, 15px text | ≠ height and size. Note: text under 16px makes iOS Safari zoom the page on focus |
| Result panel | 16px radius | form card 16px | = |
| Checkbox | 24px, 6px radius, saffron when checked | — | — |
| Page container | max-width 672px, 16px gutters (32px ≥ 640px) | banner max 1200px, 64px padding (24px mobile) | — new layout |
| Banner container | — | 24px radius (20px mobile) | ∅ |

## States and interaction

| State | Test build | Contact brief | Status |
| --- | --- | --- | --- |
| Focus | 2px saffron **outline**, offset 2–4px; border unchanged | saffron **border**, no glow | ≠ |
| Primary hover | `saffron/90` (≈ 10% darker over charcoal) | darken 6% | ≠ minor |
| Primary active | scale 0.98 | opacity 0.85 | ≠ |
| Disabled primary | stays focusable (`aria-disabled`), Porcelain 10% fill, 45% text | — | — |
| Field error | saffron border + saffron "!" icon + Porcelain text; appears after a 0.7s typing pause, clears on valid | `#E06B5A` border + message "Campo obbligatorio." | ≠ colour |
| Success | the result screen replaces the form | check mark in saffron + "Messaggio inviato. Ti rispondiamo presto." | — new |
| Blur | `backdrop-blur` on answer cards, inputs, mobile action bar, result panel | "no glassmorphism" | ≠ the test uses frosted panels over its background art |
| Shadows | only an inset 1px saffron ring on the selected card | none | = |

## Motion

Step change: slide 24px + fade, 220ms in / 140ms out · colour transitions 200ms · progress segments 300ms ·
background crossfade 600ms · overlay 400ms · all respect `prefers-reduced-motion`. No fade on first load (`initial={false}`).
Contact brief: soft fade on load, 220–300ms colour transitions. **≠** the test has no load fade.

## Page chrome

| Element | Test build | Contact brief | Status |
| --- | --- | --- | --- |
| Header | wordmark only, then progress bar | wordmark · Home · Metodo · Programma · Guide · Test · "Fai il test" pill | ∅ no nav to reuse |
| Footer | **none** | "reuse the test's footer exactly" | ∅ nothing to reuse |

## Missing assets (needed before step 2)

- `oltresoglia/references/contact-reference.jpg`: not in the repo or in this session's uploads
- Bounded files (ExtraLight, Regular, Black, Variable): not in the repo
- Manrope static files: not in the repo (Google Fonts works meanwhile)
- Logo pack / wordmark SVG: not in the repo
- WhatsApp number, social URLs, email, city, hours: placeholders, as the brief expects

## Decisions (client, after this audit)

- The test's values win everywhere: Saffron `#EFC04D`, Porcelain `#EBF0F2`, the test's opacities, focus ring and field sizes.
  The test itself is unchanged; the Contact page follows it.
- No rule changes on either page: no red, no green, no gradients.
  WhatsApp is the saffron pill with the WhatsApp glyph; errors use the test's pattern (saffron border, saffron "!" icon, Porcelain text).
- Background: exactly the test's (line artwork + charcoal overlay, frosted panels). The "no glassmorphism" line and the glow are dropped.
- Inputs keep 16px text (iOS zoom).
- Footer: none until the homepage is designed (`<!-- footer: pending homepage -->`).

## Client feedback, round 1 (Contact page only; the test is unchanged)

- More contrast: text, border and fill opacities one step brighter than the test; background overlay 45% instead of 60%.
- Banner "grey": two options in the prototype (dark grey `#232526` / light Porcelain `#EBF0F2`), pending the client's choice.
- Buttons: black fill (Blackout), Saffron border and text, soft Saffron glow, per the client's reference image.
  This reverses the earlier "no drop shadows" rule for buttons only.
- Copy: supporting line replaced with "Nessun bot, nessuna attesa. Ti rispondiamo noi, e in fretta.";
  "Vuoi una risposta ancora più rapida? Scrivici su WhatsApp" added directly above the WhatsApp button.
