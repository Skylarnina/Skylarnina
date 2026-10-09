## Part 1 — The system

### Fonts and the only weights allowed

| Font | Weights allowed | Used for |
|---|---|---|
| **Bounded** | Black, Regular, ExtraLight | Headings, statements, numerals. Nothing else. |
| **Manrope** | Light (300), Regular (400), Medium (500), SemiBold (600) | Everything that is read: body, labels, nav, buttons, captions. |

Bounded is a wide display face. Wide faces look bigger than their pixel size, so the sizes below are deliberately smaller than a normal scale. Never go above the Display size anywhere.

### The 12 roles

Every piece of text on the site is exactly one of these. Sizes use `clamp(min, fluid, max)` so there is one value per role, not one per breakpoint. The columns show what that resolves to.

| Role | Font / weight | Case | 1440 | 1024 | 390 | Line-height | Tracking | Max width | How many |
|---|---|---|---|---|---|---|---|---|---|
| **Display** | Bounded Black | UPPER | 112px | 84px | 52px | 0.92 | -0.02em | 10ch | **One per page**, hero only |
| **H1** (section statement) | Bounded Black | UPPER | 64px | 52px | 36px | 1.0 | -0.01em | 14ch | One per section |
| **H2** (section title) | Bounded Black | UPPER | 40px | 34px | 28px | 1.05 | 0 | 18ch | One per section if no H1 |
| **H3** (sub-heading, card title) | Bounded Regular | Sentence | 24px | 22px | 20px | 1.2 | 0 | 28ch | As needed |
| **Statement** (the quiet big line) | Bounded ExtraLight | Sentence | 48px | 40px | 30px | 1.1 | -0.01em | 24ch | Max two per page |
| **Numeral** (stats like 14 / 17) | Bounded Black | — | 64px | 52px | 40px | 1.0 | -0.02em | — | Same size as H1, never bigger |
| **Eyebrow** (01 · WHERE I COME FROM) | Manrope Medium | UPPER | 11px | 11px | 11px | 1.4 | 0.14em | — | One above each section heading |
| **Lead** (intro paragraph) | Manrope Light | Sentence | 20px | 19px | 17px | 1.5 | 0 | 56ch | One per section max |
| **Body** | Manrope Regular | Sentence | 16px | 16px | 16px | 1.6 | 0 | 64ch | — |
| **Small** (captions, meta, legal) | Manrope Regular | Sentence | 13px | 13px | 13px | 1.5 | 0.01em | 48ch | — |
| **Button** | Manrope SemiBold | UPPER | 13px | 13px | 13px | 1 | 0.12em | — | — |
| **Nav** | Manrope Regular | Sentence | 14px | 14px | 14px | 1 | 0 | — | — |

Colour opacities (Porcelain #F4F1EA on the dark ground): headings and Display 100%; Lead and Body 64%; Small, Eyebrow, placeholders 40%. Eyebrow may be Saffron #EFC04E instead of 40% porcelain when it sits above an H1.

### Rules that stop the drift

1. **No raw sizes.** `font-size`, `line-height`, `letter-spacing` and `font-weight` appear only in `type.css`. Every text element gets a role class. A grep for `font-size:` outside that file must return zero.
2. **One Display per page**, and only in the hero. "OLTRESOGLIA STARTS HERE." and "AT THE CENTRE OF THE JOURNEY…" are both H1, so they are the same size as each other and smaller than the hero.
3. **Numerals never outrank H1.** The 14 / 17 stats are Numeral (= H1 size), not Display.
4. **Bounded ExtraLight is only the Statement role.** "I've lived both extremes." and "For those who demand the same level…" are both Statement, so they match each other exactly.
5. **One accent phrase per section**, in Saffron, inside an H1 or Statement only. Never inside body.
6. **Case follows the role**, not the mood. Display/H1/H2/Eyebrow/Button are uppercase; everything else is sentence case. No all-caps body, no sentence-case H1.
7. **Max widths are part of the role.** A Display wider than 10ch wraps badly; a body paragraph wider than 64ch is unreadable. The class sets the max-width; layout doesn't override it.
8. **Spacing is tied to the type.** Eyebrow → heading: 16px. Heading → Lead/Body: 24px (desktop) / 16px (mobile). Section padding: 160px desktop / 96px tablet / 72px mobile. These live in `type.css` too, as variables.
9. **Mobile is not "desktop smaller".** The clamp minimums above are the floor; Claude Code may not go below 36px for H1 or above 52px for Display on a 390 screen, whatever the section "needs".
10. **Italian only.** Every string on every page is Italian. English is a build error, not a draft.

### The CSS (reference; Claude Code writes the real file)

```css
:root{
  --font-display:"Bounded",sans-serif;
  --font-text:"Manrope",sans-serif;

  --t-display:clamp(52px,7.8vw,112px);
  --t-h1:clamp(36px,4.5vw,64px);
  --t-h2:clamp(28px,2.8vw,40px);
  --t-h3:clamp(20px,1.7vw,24px);
  --t-statement:clamp(30px,3.4vw,48px);
  --t-numeral:var(--t-h1);
  --t-eyebrow:11px;
  --t-lead:clamp(17px,1.4vw,20px);
  --t-body:16px;
  --t-small:13px;
  --t-button:13px;
  --t-nav:14px;

  --space-section:clamp(72px,11vw,160px);
  --space-eyebrow:16px;
  --space-heading:clamp(16px,1.7vw,24px);
}
.t-display{font:900 var(--t-display)/0.92 var(--font-display);text-transform:uppercase;letter-spacing:-0.02em;max-width:10ch}
.t-h1{font:900 var(--t-h1)/1 var(--font-display);text-transform:uppercase;letter-spacing:-0.01em;max-width:14ch}
.t-h2{font:900 var(--t-h2)/1.05 var(--font-display);text-transform:uppercase;max-width:18ch}
.t-h3{font:400 var(--t-h3)/1.2 var(--font-display);max-width:28ch}
.t-statement{font:200 var(--t-statement)/1.1 var(--font-display);letter-spacing:-0.01em;max-width:24ch}
.t-numeral{font:900 var(--t-numeral)/1 var(--font-display);letter-spacing:-0.02em}
.t-eyebrow{font:500 var(--t-eyebrow)/1.4 var(--font-text);text-transform:uppercase;letter-spacing:0.14em}
.t-lead{font:300 var(--t-lead)/1.5 var(--font-text);max-width:56ch}
.t-body{font:400 var(--t-body)/1.6 var(--font-text);max-width:64ch}
.t-small{font:400 var(--t-small)/1.5 var(--font-text);letter-spacing:0.01em;max-width:48ch}
.t-button{font:600 var(--t-button)/1 var(--font-text);text-transform:uppercase;letter-spacing:0.12em}
.t-nav{font:400 var(--t-nav)/1 var(--font-text)}
.accent{color:#EFC04E}
```

### Framer handoff

In Framer these become 12 **Text Styles** with the same names (Display, H1, H2, H3, Statement, Numeral, Eyebrow, Lead, Body, Small, Button, Nav), each with its three breakpoint values from the table (Framer doesn't do clamp; set Desktop / Tablet / Phone sizes per style). Every text layer uses a style; no detached text.
