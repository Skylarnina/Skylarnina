# Conversion Portfolio — Design & Build Spec

A single-page portfolio for a premium Framer/Webflow developer selling to SaaS,
agencies and service brands. Six sections, one job: turn a warm visitor into an
enquiry inside 90 seconds of scrolling.

`index.html` in this folder is a working prototype of everything below
(GSAP + ScrollTrigger, no build step, opens straight in a browser).

> **Sample content.** Client names, case studies and metrics in the prototype are
> written as realistic placeholders so the layout can be judged with real-shaped
> copy. Swap in verifiable numbers before the site goes live.

---

## 0. Design system

### Palette — monochrome with one signal colour

The brief is black/white; the risk is that pure `#000`/`#fff` reads cheap. Both
neutrals are pulled slightly off-axis (a green-grey bias) so they look chosen.

| Token | Light | Dark | Use |
|---|---|---|---|
| `--paper` | `#F1F1ED` | `#0B0C0C` | page ground |
| `--ink` | `#0F1011` | `#EDEDE8` | headings, primary text |
| `--ink-2` | `#5D6061` | `#8E918E` | body, labels, meta |
| `--line` | `#DBDBD4` | `#242626` | hairlines, grid separators |
| `--band-bg` / `--band-fg` | ink / paper | paper / ink | inverted final-CTA band |
| `--signal` | `#27503C` | `#8FC9A8` | **only** availability dot, outcome numbers, list bullets |

The signal colour appears on maybe 1% of the page. That restraint is what makes
a metric chip read as *a result* rather than decoration.

### Typography — three roles, one voice

| Role | Face | Settings |
|---|---|---|
| Display + UI | **Schibsted Grotesk** 500/600 | `letter-spacing: -.035em`, `line-height: 1.02` on headlines |
| Editorial accent | **Newsreader** italic 300 | one emphasis phrase per major headline, nothing else |
| Data / labels | **Geist Mono** 400/500 | `.6875rem`, `letter-spacing: .14em`, uppercase; all numbers `tabular-nums` |

Scale is fluid via `clamp()` and there are only six steps. Headlines are set to
`text-wrap: balance`; body copy is capped at `62ch`, leads at `34ch`.

The mono face does real work here: it marks everything that is *evidence*
(metrics, timelines, stack, section indices) and separates it from everything
that is *claim*. A reader can skim only the mono and still get the argument.

### Layout

12-column grid, `max-width: 1280px`, fluid gutter `clamp(20px, 5vw, 64px)`.
Vertical rhythm is one token: `--sec: clamp(88px, 11vw, 176px)` of section
padding, so every section breathes identically.

Two structural devices carry the whole page:

1. **Sticky section label.** Each section is a 3/9 split — a mono label
   (`01 — Selected work`) sticks in the left column while the content scrolls
   past it in the right. It gives orientation without a progress bar.
2. **Hairline grids.** Proof strip, value grid and services are 1px-gap grids on
   a `--line` background, so the separators *are* the layout. No cards, no
   shadows, no radii — the only rounded things on the page are buttons and chips,
   which is also the only thing that should look clickable.

---

## 1. HERO

### Wireframe

```
┌────────────────────────────────────────────────────────────────────┐
│ Skylar Nina  FRAMER / WEBFLOW    Work  Why me  Process  Services   │ ← fixed, 68px
│                                            [ Start a project → ]   │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│ ● BOOKING DECEMBER — 2 BUILD SLOTS LEFT                            │ mono, signal dot
│                                                                    │
│ Your website is a sales rep.                                       │ display, 15ch max
│ Mine hit quota.                          ← serif italic line       │
│                                                                    │
│ ┌──────────────── 7 col ───────────┐  ┌──── 5 col ─────┐           │
│ │ Lead paragraph, 34ch             │  │ ──────────────  │           │
│ │                                  │  │ THE SHORT VERSION│          │
│ │ [Start a project →] [View work]  │  │ Supporting note  │          │
│ └──────────────────────────────────┘  └─────────────────┘           │
│                                                                    │
│ ┌────────┬────────┬────────┬────────┐                              │
│ │ +41%   │ 0.8s   │ 3 wks  │ 47     │  ← proof strip, hairline grid │
│ │ demo   │ LCP    │ build  │ sites  │                              │
│ └────────┴────────┴────────┴────────┘                              │
│                                                                    │
│ TRUSTED BY  Northbeam · Quorum HQ · Basefold · Tandem · Verdant     │
└────────────────────────────────────────────────────────────────────┘
```

### Copy

- **Eyebrow:** `Booking December — 2 build slots left`
- **Headline:** *Your website is a sales rep. **Mine hit quota.***
- **Lead:** "I design and build Framer & Webflow sites for SaaS, agencies and
  service brands — the kind that load in under a second, read like a pitch, and
  put more qualified calls on your calendar."
- **Aside:** "Ten years of conversion work, compressed into a three-week build.
  No page builders held together with tape, and no handoff you can't maintain."
- **CTAs:** `Start a project →` (primary, filled) · `View selected work` (ghost)
- **Proof:** `+41%` median lift in demo requests · `0.8s` average LCP ·
  `3 wks` kickoff to live · `47` sites shipped

Why this headline: it names the *function* of the site (a sales rep) and makes a
claim only someone with numbers would make. A generic "I build beautiful,
high-performing websites" is interchangeable with 10,000 other portfolios.

### Layout notes

- Hero is **not** `100vh`. Top padding `clamp(128px, 18vh, 200px)`, and the proof
  strip is deliberately cut by the fold on a laptop — the clipped row is what
  makes someone scroll.
- Headline caps at 15ch so it always breaks into three lines at desktop. The
  italic line lands third: the punchline gets its own line.
- The availability dot is the page's first use of the signal colour and the only
  looping animation on the page.

### Animation

| Element | Motion | Timing |
|---|---|---|
| Headline | Word-level mask reveal, `yPercent: 115 → 0` inside `overflow: hidden` spans | `1.05s`, `expo.out`, stagger `0.045` |
| Eyebrow, lead, CTAs, aside | `y: 18 → 0`, opacity | `0.8s`, `power3.out`, stagger `0.08`, delay `0.18` |
| Proof cells | `y: 22 → 0`, opacity | stagger `0.07`, delay `0.42` |
| Proof numbers | Count from 0 to value, tabular figures | `1.4s`, `power2.out`, delay `0.5` |
| Availability dot | 2.8s box-shadow pulse | infinite, the only loop |

The whole hero sequence finishes in ~1.6s. Nothing waits on a scroll event, and
`gsap.from()` is used throughout so the resting DOM is fully visible — if the CDN
fails or JS is off, the page still reads.

---

## 2. SELECTED WORK

### Wireframe

```
01 — SELECTED WORK │ Four builds. Four numbers that moved.
     (sticky)      │ Intro, 62ch
                   │
┌─ text 6col ──────────────────┐  ┌─ media 6col ──────────────┐
│ CLIENT · SECTOR · YEAR · STACK│  │ ┌───────────────────────┐ │
│ ─────────────────────────────│  │ │ ○○○        domain.com │ │
│ Project headline (22ch)      │  │ │  ▮▮▮▮▮▮▮▮▮            │ │
│ Scope line                   │  │ │  ▮▮▮▮▮▮                │ │
│                              │  │ │  ▭▭ ▭▭ ▭▭             │ │
│ PROBLEM   Two sentences.     │  │ └───────────────────────┘ │
│ SOLUTION  Two sentences.     │  └───────────────────────────┘
│ OUTCOME   The number.        │
│ (+58%) (0.7s LCP) (18 days)  │  ← mono chips, signal numbers
│ Read the case study →        │
└──────────────────────────────┘
        ↕ next project flips media to the left
```

### Copy pattern

Every entry is the same three-beat argument, never more than two sentences each:

| Beat | Job | Example (Northbeam Labs) |
|---|---|---|
| Problem | A business symptom with a number or a consequence | "Traffic was healthy, demo requests were not. The homepage led with architecture diagrams; buyers couldn't tell who the product was for within the first screen." |
| Solution | What you *decided*, not what you installed | "Rewrote the page around one outcome-led claim, moved proof above the fold, rebuilt pricing as a comparison a buyer can defend internally." |
| Outcome | One number plus the second-order effect | "Demo requests up 58% in the first 60 days on flat traffic. Sales stopped re-explaining the product on calls one and two." |

Four projects: a SaaS marketing site, an agency rebuild, a paid-traffic landing
page, a fast launch site. Between them they cover every service sold below — the
work section *is* the proof for the services section.

### Layout notes

- 6/6 split, alternating sides (`.proj--flip`) so the eye zig-zags down.
- Metadata row on top with a hairline under it reads like a plate caption —
  editorial, not card-like.
- Problem/Solution/Outcome is a `<dl>`: 78px mono term column, definition capped
  at 46ch. Outcome row is set in full-strength ink while the other two sit in
  `--ink-2`, so the result is the thing you see when skimming.
- The media plate is built in CSS (gradient ground, 6-column grid overlay, mock
  browser chrome, abstract content bars) — zero image bytes in the prototype.
  In production this becomes a real screenshot or a 6-second muted WebM loop.
- Stacks to one column below 900px, media first, so mobile still leads with an image.

### Animation

| Element | Motion | Timing |
|---|---|---|
| Section headline | Same masked word reveal as hero | `0.9s`, `expo.out`, stagger `0.035`, `start: "top 88%"`, `once: true` |
| Text block | `y: 20 → 0`, opacity, staggered across meta → title → rows → chips → link | `0.7s`, stagger `0.055`, `start: "top 78%"` |
| Plate | `y: 34 → 0`, opacity, offset `0.08s` behind the text | `0.95s` |
| Plate (scroll) | Parallax `yPercent: 4 → -4`, scrubbed, desktop only | `scrub: 0.6`, `ease: "none"` |
| Plate (hover) | Card `translateY(-6px)` + border darkens, inner UI `scale(1.025)` | `0.8s`, `cubic-bezier(.22,1,.36,1)` |

Two hover speeds on purpose: the arrow in "Read the case study" moves at `0.45s`
(responsive, feels direct), the plate at `0.8s` (slow, feels heavy and expensive).

---

## 3. VALUE / EDGE

### Wireframe

```
02 — THE EDGE │ Most sites are designed. Yours gets engineered to sell.
              │ Intro
┌──────────────────────────┬──────────────────────────┐
│ CONVERSION-FIRST         │ SPEED OF DELIVERY        │
│ The copy and the layout  │ Three weeks, fixed, with │
│ are decided together     │ dates you can plan around│
│ 3-4 line proof paragraph │ 3-4 line proof paragraph │
├──────────────────────────┼──────────────────────────┤
│ CLEAN CMS BUILDS         │ PERFORMANCE-CONSCIOUS    │
│ Your team ships content  │ Animation on a budget,   │
│ without opening a ticket │ measured on a mid phone  │
└──────────────────────────┴──────────────────────────┘
```

Each cell is mono label → heading (16ch) → paragraph (42ch). The heading states
the *benefit*; the paragraph gives one concrete, checkable detail — "No layer
called 'Frame 27'", "Transform and opacity only", "One project in flight at a
time". Specifics are what separate this from a features list.

**Animation:** cells fade up individually (`y: 22`, `0.85s`, `start: "top 90%"`,
`once`). Deliberately *not* staggered as a group — each cell triggers on its own
entry, so scrolling fast doesn't leave half a grid mid-animation.

---

## 4. PROCESS

### Wireframe

```
03 — PROCESS │ Four steps. No mystery, no scope creep.
─────────────────────────────────────────────────────────────
01 │ Wireframe  │ Paragraph, 52ch
   │ DAYS 1–3   │ (Positioning call)(Message map)(Wireframe)(Copy)
─────────────────────────────────────────────────────────────
02 │ Design     │ …  DAYS 4–8
─────────────────────────────────────────────────────────────
03 │ Build      │ …  DAYS 9–13
─────────────────────────────────────────────────────────────
04 │ Launch     │ …  DAYS 14–15
─────────────────────────────────────────────────────────────
```

This is the one place numbered markers are honest — it is a real sequence, and
the day ranges are the reason the section converts. "Days 9–13" is a promise;
"we build it" is not. Each step carries 3–4 mono deliverable pills so scope is
visibly bounded (the antidote to scope-creep anxiety).

**Animation:** rows fade up on their own trigger; the hairline borders are static.
No pinning — a pinned process section is the single most common way portfolios
turn a 15-second read into a 40-second scroll fight.

---

## 5. SERVICES

Three productized offers in a hairline 3-up: **Conversion Page** (from $2,400,
1 week), **Full Website** (from $6,800, 3 weeks), **CMS & Templates** (from
$3,200, 1–2 weeks). Each: scope label + timeline (mono) → name → price → one
positioning sentence → four bullets pinned to the bottom edge with `margin-top: auto`
so the bullet lists align across all three regardless of paragraph length.

Prices are visible on purpose. Publishing "from" pricing filters out the wrong
enquiries before they reach the inbox, which is itself a conversion improvement.
The intro line — "I'll tell you on the call if you need the smaller one" — does
more for trust than any testimonial.

**Animation:** same single fade-up per column. Prices do **not** count up; two
counters on one page is a gimmick, one is a detail.

---

## 6. FINAL CTA

Full-bleed inverted band (`--band-bg`), the only tonal flip on the page, so it
reads as a hard stop rather than another section.

- **Headline:** "Tell me what the site needs to do. I'll tell you if I'm the right build."
- **Lead:** "Send two lines about the business and the deadline you're working
  toward. You'll get a straight answer within one working day — including when
  the answer is 'you don't need a new site yet.'"
- **CTAs:** `hello@skylarnina.com →` (filled, `mailto:` with a prefilled subject)
  · `Book a 20-minute call` (ghost)
- **Footer meta, 3-up:** Response time · Availability · Good fit

Turning work away in the CTA is the strongest available trust signal for
high-ticket work: only someone with a pipeline can afford to say it.

**Animation:** headline word reveal, then the meta row fades up. The band edge
itself doesn't animate — the colour flip is already the transition.

---

## 7. Framer implementation

### Components

| Framer component | Variants | Notes |
|---|---|---|
| `Nav` | Default / Scrolled | Scrolled adds the hairline + 90% background blur. Drive it with an Appear-on-scroll or a small code override on `scrollY > 24`. |
| `Button` | Primary / Ghost / Band / Band-ghost | One component, four variants. Arrow is a nested layer with a `+4px` x-offset on hover, `0.45s` ease-out. |
| `ProjectRow` | Left-media / Right-media | CMS-connected. Flip is a variant, not a duplicated layout. |
| `Plate` | — | Replace the CSS mock with a real image + `Scale 1.025` hover on an inner frame, parent `overflow: hidden`. |
| `Chip` | — | Text layer, mono, `tabular-nums` on. |
| `StepRow`, `OfferCard` | — | Both CMS-connected so they can be reordered without touching layout. |

### CMS collections

- **Projects** — `title`, `client`, `sector`, `year`, `stack`, `scope`,
  `problem`, `solution`, `outcome`, `metric1/2/3` (label + value), `cover`,
  `slug`, `featured` (boolean), `order` (number).
  The homepage list filters `featured = true`, sorts by `order`, limit 4.
  The same collection powers `/work/[slug]` case-study pages later — build the
  fields now even if detail pages ship in phase two.
- **Services** — `name`, `scope_label`, `timeline`, `price_from`, `summary`,
  `inclusions` (rich text list), `order`.
- **Process** — `step`, `title`, `days`, `body`, `deliverables`.

### Motion in Framer

Native effects cover ~80% of this page:

- **Appear effects** on section wrappers: *Fade + Move Y 22px*, duration `0.85s`,
  custom ease `[0.22, 1, 0.36, 1]`, threshold `0.15`, "animate once" on.
- **Stagger** children at `0.055s` for project text blocks and `0.07s` for the
  proof strip.
- **Scroll transforms** for the plate parallax: `Y: 2% → -2%` across the section,
  desktop breakpoint only. (Framer's is more conservative than the prototype's
  ±4% — keep it under 6% or it looks like drift.)
- **Hover** on `ProjectRow`: variant transition, `0.8s`, same ease.

Two things need a code override:

1. **Masked word reveal for headlines** — Framer has no word-level split. A small
   override that splits `textContent` into `overflow: hidden` spans and animates
   `yPercent: 115 → 0` at `0.045s` stagger (see `splitWords()` in `index.html`).
   Apply it to the four `h2`s and the hero `h1` only.
2. **Counting numbers** — a `useInView` + `requestAnimationFrame` override on the
   four proof figures, easing `power2.out` over `1.4s`. Format with
   `toLocaleString()` and keep the font `tabular-nums` so the strip doesn't
   reflow while counting.

Skip a smooth-scroll library. Lenis or Locomotive adds 15–20KB, fights native
scroll on trackpads, and this page has nothing that needs it.

### Breakpoints

`Desktop 1280` → `Tablet 900` (projects stack, media first; edge grid to 1 col at 760)
→ `Phone 390` (nav collapses to mark + CTA, proof strip to 2×2, offers stack).
Design the phone layout in parallel, not by scaling the desktop down: on mobile
the proof strip and the CTA carry almost all the conversion weight.

### Webflow equivalents

Same structure with CSS Grid and `1px` gap on a background-coloured parent.
Use GSAP + ScrollTrigger from a CDN in the before-`</body>` custom code exactly
as in `index.html`; Webflow Interactions can do the fades but not the word split
cleanly. Collections map 1:1 with the Framer CMS fields above.

---

## 8. Performance

Targets: **LCP < 1.0s**, **CLS < 0.01**, **INP < 120ms**, Lighthouse mobile 95+.
These are also sales claims on this page — the site has to survive being audited
by a prospect.

**Fonts** — three families, one stylesheet request, `display=swap`,
`preconnect` to both Google hosts. Only the weights actually used are requested
(400/500/600/700 grotesk, one serif italic, two mono). In Framer, upload the
subset WOFF2 files and self-host instead: it removes a third-party round trip and
is usually worth 100–200ms on LCP. `font-synthesis-weight: none` prevents faux-bold
flashes during the swap.

**Images** — the prototype ships zero images: the project plates are CSS gradients
plus a repeating-linear-gradient grid. In production, every plate gets
`width`/`height` attributes (or an `aspect-ratio` box) so nothing shifts, WebP/AVIF
with a responsive `srcset`, `loading="lazy"` + `decoding="async"` on everything
below the fold, and `fetchpriority="high"` on nothing — the LCP element here is
text, which is exactly where you want it.

**JavaScript** — GSAP core + ScrollTrigger (~38KB gzipped, from cdnjs, pinned to
3.12.5). No jQuery, no smooth-scroll library, no cursor library, no analytics
until after launch. If the budget gets tight, the entire hero can be rewritten with
CSS `@keyframes` and the rest with `IntersectionObserver` for ~1KB.

**Animation cost** — `transform` and `opacity` only; nothing animates `width`,
`height`, `top` or `box-shadow` during scroll. Every scroll reveal uses
`once: true` so ScrollTrigger kills its listener after firing. The one scrubbed
animation (plate parallax) is registered inside `ScrollTrigger.matchMedia` at
`min-width: 901px`, so phones run zero scroll-linked work. `will-change` is set on
exactly one selector (`.btn`) — declaring it broadly costs more than it saves.

**Accessibility, which is also performance** — `prefers-reduced-motion: reduce`
exits the script before a single tween is created and collapses all CSS transitions
to `0.001ms`; semantic `<header>/<main>/<section>/<article>` with one `h1`;
`:focus-visible` rings in the signal colour; `aria-hidden` on decorative arrows and
plate chrome; contrast ≥ 7:1 for body text in both themes.

**Fallbacks** — every reveal uses `gsap.from()`, never a CSS `opacity: 0` resting
state, so a blocked CDN or a JS error leaves a fully readable page instead of a
blank one. That single choice is the difference between a slow first paint and a
lost lead.
