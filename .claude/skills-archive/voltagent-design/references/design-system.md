# Voltagent Design System — Full Analysis

Adapted from the Voltagent design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/voltagent/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Voltagent is an AI agent engineering platform built for developers, and its
brand wears that audience proudly. The page background is a near-black
`colors.canvas` (`#101010`) that runs edge-to-edge with no light-mode
counterpart, lit only by a single electric-green accent
(`colors.primary`, `#00d992`) reserved for CTAs, status pills, and the
brand's lightning glyph. Typography pairs sentence-case Inter with SF Mono
for inline code and command snippets. The overall effect is closer to
polished documentation than a typical marketing page — one that happens to
also sell something.

Decoration stays deliberately sparse: no gradient mesh, no atmospheric
backdrop, no illustration suite. Instead, the brand signals identity
through small typographic gestures — a green code chip reading `npx
voltagent ...`, hairline-outlined feature cards sitting flush against the
same near-black canvas, and a green hairline divider marking section
breaks. Every card carries a hairline border, every code snippet has a
copy button, and every metric renders in numeric monospace — the page
feels engineered down to its smallest details.

Type stays quiet. The hero display sits at 60px in regular weight with
-0.65px tracking — closer to a documentation H1 than a billboard headline
— stepping down through 36px and 24px section headings at similarly
restrained weights. Body copy runs 16px Inter at a generous 1.65
line-height for long-form legibility. Uppercase eyebrows ("EVERYTHING YOU
NEED" style labels above section headlines) use Inter at weight 600 with
wide positive tracking (2.52px at 14px).

**Key characteristics:**
- A single electric-green accent carries every CTA, status pill, and the
  lightning logo — there is no second accent anywhere.
- The near-black canvas is the only page surface; the whole site reads as
  one continuous dark plane broken only by card boundaries.
- Hairline-bordered feature cards (1px solid `colors.hairline`) are the
  primary chrome — no shadows, no fills, just precise hairline rectangles.
- A quiet dashed-border rhythm cue (`1px dashed rgba(79,93,117,.4)`)
  separates sections — the brand's only ornamental line.
- Inter and SF Mono are the entire typographic system; SF Mono is reserved
  strictly for code blocks, command snippets, and metric counters.
- Buttons are tight 6px rounded rectangles, never pills — only inline
  status tags use the full 9999px pill.

## Colors

### Brand & accent
- **Electric green** (`colors.primary`, `#00d992`) — the single brand
  accent: every primary CTA, status pill, "live" indicator, and the
  lightning glyph itself. Fully reserved.
- **Primary soft** (`colors.primary-soft`, `#2fd6a1`) — a more muted green
  used inside ghost-button variants and tooltip/focus indicators.
- **Primary deep** (`colors.primary-deep`, `#10b981`) — the darker green
  used for inline link color in body copy.

### Surface
- **Canvas** (`colors.canvas`, `#101010`) — the default near-black page
  background, the brand's only surface mode.
- **Canvas soft** (`colors.canvas-soft`, `#1a1a1a`) — a slightly lighter
  dark fill for code blocks and form inputs, marking them as visually
  distinct against the canvas.
- **Hairline** (`colors.hairline`, `#3d3a39`) — 1px solid borders on
  feature cards, buttons, and row dividers; the system's universal edge
  color.
- **Hairline soft** (`colors.hairline-soft`, `#b8b3b0`) — a lighter
  divider tint reserved for rare on-light secondary contexts.

### Text
- **Ink** (`colors.ink`, `#f2f2f2`) — default text on the dark canvas,
  slightly off-white to ease contrast strain.
- **Ink strong** (`colors.ink-strong`, `#ffffff`) — pure white for hero
  headlines and high-emphasis copy.
- **Body** (`colors.body`, `#bdbdbd`) — secondary text and long-form body
  paragraphs.
- **Mute** (`colors.mute`, `#8b949e`) — the lowest-priority on-dark text —
  captions, fine print, footer lines.
- **Canvas text soft** (`colors.canvas-text-soft`, `#f5f6f7`) — used inside
  code mockups to keep code color a touch cooler than surrounding body
  text.

### Semantic
Voltagent doesn't surface a separate error/warning palette on its public
marketing pages — the underlying Docusaurus default semantic palette
exists in the broader design system but is reserved for in-product/docs
contexts. On the marketing surface, validation cues use the primary green
for success and a muted body gray for anything missing.

## Typography

### Font family
Two faces carry the system:
1. **Inter** for every display, body, button, and link role, at weights
   400/500/600/700, with OpenType features `"calt"` and `"rlig"` enabled so
   the geometric ligatures and contextual alternates render correctly.
2. **SF Mono** (`SFMono-Regular` with Menlo/Monaco/Consolas/Liberation
   Mono fallbacks) for inline code, command snippets, terminal mockups, and
   numeric counters. An unusual 549/550 sub-bold weight appears alongside
   400/700, giving the mono a "slightly heavier than regular" emphasis
   option.

### Hierarchy
Full scale in `design-tokens.yaml → typography`: `display-xl` 60px/400
with -0.65px tracking for the hero, down through `display-lg` 36px,
`display-md` 24px/700, `display-sm` 20px/600; `eyebrow-mono` 14px/600 with
+2.52px tracking for uppercase eyebrows; body runs `body-lg` 18px through
`caption` 12px; `code`/`code-strong` at 13px carry the technical voice.

### Principles
- Regular-weight Inter at 60px display is a deliberate counter to loud AI
  marketing — the light tracking and modest weight read as documentation,
  not a pitch.
- Two-face contrast carries the technical voice: Inter for narrative, SF
  Mono for anything that could be typed at a terminal.
- The uppercase eyebrow with wide positive tracking (2.52px at 14px) is the
  brand's signature label style.

### Font substitutes
Inter is the brand's actual face, so no substitute is needed when
self-hosting is available. For SF Mono (an Apple-system face), *JetBrains
Mono* or *Geist Mono* are the closest free substitutes.

## Layout

- Base unit: 4px, with small 5/6.4px values appearing inside code-mockup
  line-height compensation. Full scale in `design-tokens.yaml → spacing`,
  from `xxs` 2px to `6xl` 64px.
- Hero and content bands use 48px top/bottom padding; feature cards sit at
  24px interior padding.
- The marketing container centers around 1200–1400px, staying edge-to-edge
  in color with 32px desktop gutters; feature-card grids run 2-up to 3-up
  at desktop, dropping to 1-up on mobile.

### Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Mobile | <768px | Hero scales from 60px to ~32px; cards drop to 1-up; hamburger nav. |
| Tablet | 768–1023px | Cards run 2-up; nav stays horizontal. |
| Desktop | ≥1024px | Full 3-up card grids. |

Buttons render around 44px tall (12px vertical padding plus 24px
line-height), clearing WCAG AAA at every breakpoint. Nav collapses to a
hamburger overlay on mobile, keeping the green CTA pinned at the bottom of
the menu; hero typography scales fluidly. Code-editor mockups render as
image-like cards with copy-to-clipboard affordances — there's no
photography anywhere in the marketing surface.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 — flat | none | full-bleed bands |
| 1 — hairline | 1px solid `colors.hairline` on canvas | default for every feature card and button |
| 2 — inset glow | `0 0 15px rgba(92,88,85,.2)` | hovering/featured cards |
| 3 — modal stack | `0 20px 60px rgba(0,0,0,.7), 0 0 0 1px rgba(148,163,184,.1) inset` | modal/dialog surfaces in-product |

Hairline cards on the dark canvas are the brand's only true elevation
mode. A 2px solid green border occasionally marks a "featured" or "active"
card state, and a 1px dashed `rgba(79,93,117,.4)` divider sits between
section bands as a quiet rhythm cue.

## Shapes

| Token | Value | Use |
|---|---|---|
| `rounded.none` | 0px | full-bleed bands |
| `rounded.xs` | 4px | smallest inline pills, code chips |
| `rounded.sm` | 6px | default button and input radius |
| `rounded.md` | 8px | card chrome, code-block chrome |
| `rounded.pill` | 9999px | inline status tags ("Live", "Beta") |
| `rounded.full` | 9999px | circular icon containers |

## Components

Full specs in `design-tokens.yaml → components`. Summary:
- **Buttons** — `button-primary` (electric-green fill), `button-outline-
  on-dark` (hairline secondary), `button-ghost-green` (text-only
  tertiary), and `button-pill-tag` for inline category/status labels.
- **Cards** — `card-feature` (the default hairline card), `card-feature-
  emphasized` (same chrome with a 3px border), `code-mockup` (dark
  code-editor card with copy-to-clipboard), and `code-inline-chip` for
  inline command snippets.
- **Inputs** — `text-input`, a hairline-bordered field on `canvas-soft`.
- **Navigation** — `nav-bar`, `nav-link`, and a dark `footer`.
- **Signature pieces** — `hero-band` (the dark hero hosting the 60px
  Inter headline with a mono eyebrow above it), `content-band` (standard
  feature-grid section), and `green-divider-band` (the brand's only
  chromatic divider, a 2px green top/bottom border).
- **Example surfaces** (`ex-*`) — auto-derived kit-mirror demonstrations
  (pricing tier, product selector, app-shell row, data-table cell, auth
  card, modal, empty state, toast) re-skinning the brand's primitives onto
  ten common product surfaces.

## Do's and don'ts

**Do**
- Reserve `colors.primary` (`#00d992`) for every primary CTA, the
  lightning logo glyph, and live-status indicators — the green is the
  brand's center of gravity.
- Use the dark `colors.canvas` (`#101010`) as the only page surface;
  there's no light-mode rhythm to fall back on.
- Build cards from 1px hairline borders, not shadows — hairlines on dark
  ARE the elevation system.
- Pair Inter (sentence-case) with SF Mono (inline code, command
  snippets); set every uppercase moment in Inter weight 600 with 2.52px
  tracking, not a separate mono face.
- Use 6px radius for buttons, 8px for cards, and reserve the 9999px pill
  for inline status tags only.

**Don't**
- Don't introduce a light-mode counterpart — the brand is dark-canvas
  only.
- Don't use the primary green as a body-text fill — it's CTA-only.
- Don't drop a soft shadow on cards; the brand uses hairlines plus an
  occasional glow, never material shadows.
- Don't render the hero headline in heavy weight (700+); the display is
  intentionally calm at weight 400.
- Don't swap Inter or SF Mono for a different family — both faces and
  their pairing are part of the brand's voice.

## Known gaps

- The `ex-*` example components are auto-derived kit-mirror surfaces, not
  directly observed, and should be treated as reasonable extrapolations.
- No dedicated marketing-facing error/warning palette is documented — the
  underlying Docusaurus semantic palette is reserved for in-product/docs
  contexts.
