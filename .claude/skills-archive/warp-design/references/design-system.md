# Warp Design System — Full Analysis

Adapted from the Warp design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/warp/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Warp describes itself as an "agentic development environment" — a terminal
application wrapping an AI agent — and its marketing site mirrors that
posture directly: one dark band running the entire page, warmer than pure
black (`colors.canvas` `#2b2622` carries a hint of brown-beige, resolved
from `oklch(22.0% 0.004 84.6)`), set almost entirely in Inter. The overall
effect reads closer to a developer's reading-mode editor than a typical
marketing page.

Decoration is minimal by design. Two terminal screenshots open the hero,
split between the product's two main modes (agent and terminal). Below
that sits a partner-logo strip (Anthropic, OpenAI, Google, Stanford) on a
slightly warmer tile surface, a single testimonial card with a portrait
photograph, a press-coverage list, and finally download tiles for Mac,
Linux, and Windows. There's no gradient, no atmospheric backdrop, no
illustration system anywhere.

Type is the second decisive choice. The hero display sits at 64px Inter
weight 400 with -1.6px tracking — restrained for a hero, deliberately
quiet rather than loud. DM Mono is the brand's monospace face for code
blocks, and Instrument Serif occasionally appears in italics for editorial
moments. Body text runs 16px Inter at 1.5 line-height, comfortably
readable.

**Key characteristics:**
- No chromatic accent at all — the "primary" is really a warm off-white
  (`colors.primary`, `#f7f5f0`) that doubles as text on canvas and the
  button-primary fill.
- The warm dark canvas is the only page surface; the defining tone is its
  brown-warmth, not a pure black.
- Extremely tight button radii — 3–4px, never a generous pill for CTAs.
  Only icon containers use the full circle.
- Inter paired with DM Mono is the canonical typographic pairing;
  Instrument Serif adds a third editorial face for occasional italics.
- Terminal-mockup imagery is the only consistent decorative system — no
  gradients, no atmospheric overlays.
- A subtle warm tint runs through every neutral; even body text and
  dividers carry a hint of warmth rather than reading as cool gray.

## Colors

### Brand & accent
- **Off-white primary** (`colors.primary`, `#f7f5f0`) — the brand's
  "primary" is a warm off-white used as the button-primary fill, the
  default text color on canvas, and the wordmark color. There's no
  chromatic brand accent — the off-white tone itself is what distinguishes
  the brand.

### Surface
- **Canvas** (`colors.canvas`, `#2b2622`) — the warm dark page background,
  resolved from `oklch(22.0% 0.004 84.6)`; slightly browner than pure
  black, slightly warmer than neutral gray. That warmth is the identity.
- **Canvas soft** (`colors.canvas-soft`, `#383330`) — a lighter warm-dark
  fill for cards, mockup chrome, and partner-logo tiles.
- **Hairline** (`colors.hairline`, `#3f3a36`) — a 1px solid divider on
  dark surfaces.

### Text
- **Ink** (`colors.ink`, `#f7f5f0`) — default text on canvas, the same
  off-white as the primary, intentionally unified.
- **Body strong** (`colors.body-strong`, `#dad2c1`) — mid-emphasis body
  text.
- **Body** (`colors.body`, `#c9c0ad`) — secondary body text — captions,
  supporting copy, press-coverage rows.
- **Mute** (`colors.mute`, `#aea69c`) — the lowest-priority text —
  timestamps, fine print, footer secondary lines, resolved from
  `oklch(71.5% 0.008 84.6)`.

### Semantic
Warp doesn't surface a separate error/warning/success palette on its
marketing pages; validation cues rely on the unified off-white system,
while any in-product semantic colors live inside the terminal application
itself.

## Typography

### Font family
Three faces ladder the system:
1. **Inter**, for every display, body, button, link, and label role, at
   weights 400/500, paired with the brand's own "Inter Fallback" for
   metric-compatible system fallback.
2. **DM Mono** for terminal mockups, command snippets, and code blocks, at
   weight 400 only.
3. **Instrument Serif** for rare editorial italic moments — documented as
   a third face for emphasized tagline-style phrases, though sparingly
   used on the marketing surface. **Abel** loads as a fourth fallback for
   headline emphasis.

### Hierarchy
Full scale in `design-tokens.yaml → typography`: `display-xl` 64px/400
with -1.6px tracking for the hero, `display-lg` 48px, `display-md` 32px,
`display-sm` 24px, and `display-serif` 48px for the Instrument Serif
italic moments. Body runs `body-lg` 18px through `caption` 12px; `code`
13px and `code-md` 14px carry DM Mono; buttons use `button-md` 14px/500.

### Principles
- Hero display at weight 400 reads as quietly confident rather than
  billboard-loud.
- Negative tracking is part of the voice — -1.6px at 64px, scaling down
  through the display levels.
- Inter carries the narrative; DM Mono carries anything technical — the
  role split is strict.

### Font substitutes
All three faces are open and freely loadable: *Inter* and *DM Mono* are on
Google Fonts, and *Instrument Serif* is open-source as well — no
substitution is actually needed.

## Layout

- Base unit: 4px, with occasional 6px and 10px values for button padding.
  Full scale in `design-tokens.yaml → spacing`, from `xxs` 2px to `5xl`
  96px.
- Hero and content bands use 96px top/bottom padding on desktop; cards sit
  at 24px interior padding.
- The marketing container centers around 1200px. The hero runs 2-column at
  desktop (split between two terminal screenshots), stacking on mobile;
  partner logos wrap in a 5-up flex row; download tiles run 3-up desktop
  (Mac/Linux/Windows), 1-up mobile.

### Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Mobile | <768px | Hero stacks; grids drop to 1-up; hamburger nav. |
| Tablet | 768–1023px | Grids run 2-up. |
| Desktop | ≥1024px | Full hero split; 3-up download tiles. |

Buttons render around 36px tall (8px vertical padding plus 20px
line-height), with mobile padding growing to meet the WCAG 44×44px floor.
Nav shows a full link row plus Sign in/Download at desktop, collapsing to
a hamburger at mobile; the hero's terminal-mockup split stacks vertically
below desktop; press and job rows stay single-column at every width.
Terminal mockups hold roughly a 3:2 aspect ratio; partner logos render as
monochrome SVGs on dark tiles; testimonial portraits crop to 1:1 inside
4px card chrome.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 — flat | none | default for the hero band |
| 1 — hairline | 1px solid `colors.hairline` on `canvas-soft` | default card chrome |
| 2 — inset card | `canvas-soft` against `canvas` with 1px hairline | mockup cards, download tiles, testimonial cards |

Surface contrast and hairline borders carry all elevation; soft
drop-shadows don't appear anywhere in the marketing surface.

## Shapes

| Token | Value | Use |
|---|---|---|
| `rounded.none` | 0px | full-bleed bands |
| `rounded.xxs` | 1px | tightest in-text indicator |
| `rounded.xs` | 2px | inline very-small chips |
| `rounded.sm` | 3px | default button radius — extremely tight |
| `rounded.md` | 4px | card chrome (the brand's base `--radius` value) |
| `rounded.lg` | 6px | slightly larger cards |
| `rounded.pill` | 9999px | icon containers, status pills |

Terminal mockups run roughly 3:2 inside 4px card chrome; partner logos
render as monochrome SVGs at consistent 24px height inside tile cards;
testimonial portraits crop to a 1:1 square inside the same 4px radius.

## Components

Full specs in `design-tokens.yaml → components`. Summary:
- **Buttons** — `button-primary` (off-white fill on dark), `button-
  secondary-ghost` (transparent, ink text), and `button-icon-circular`
  for nav controls like search and theme toggle.
- **Cards** — `card-content` (default content card), `card-mockup`
  (terminal-screenshot card), `download-tile` (Mac/Linux/Windows CTA
  tiles), `partner-logo-tile`, and `testimonial-card`.
- **Lists** — `press-row` and `job-row`, both hairline-bottom-bordered
  single rows with no card chrome.
- **Inputs** — `text-input`, a hairline-bordered field on `canvas-soft`.
- **Navigation** — `nav-bar`, `nav-link`, and a `footer` band.
- **Signature pieces** — `hero-band` (hosting the 64px Inter headline
  above a 2-column terminal-mockup split) and `content-band` (standard
  content sections).
- **Example surfaces** (`ex-*`) — auto-derived kit-mirror demonstrations
  (pricing tier, product selector, app-shell row, data-table cell, auth
  card, modal, empty state, toast) re-skinning the brand's primitives onto
  ten common product surfaces.

## Do's and don'ts

**Do**
- Reserve `colors.primary` off-white for primary CTA buttons and default
  text — there's no chromatic accent to lean on instead.
- Use tight 3px or 4px button radii throughout; the brand never reaches
  for generous pills on CTAs.
- Set hero headlines in Inter weight 400 with -1.6px tracking — quiet
  confidence over volume.
- Pair Inter (sentence-case) with DM Mono (code blocks, terminal
  mockups).
- Keep the warm-dark canvas tone; pure black would break the brand's
  identity.

**Don't**
- Don't introduce a chromatic brand accent — the off-white-on-warm-dark
  pairing is the entire voice.
- Don't render the hero headline in a heavy weight (700+); the display is
  intentionally light.
- Don't use generous pill CTAs; the button radius stays at 3–4px, nearly
  rectangular.
- Don't swap the warm dark canvas for neutral gray or pure black; the
  warmth is the brand.
- Don't drop a soft shadow on cards; hairlines plus surface contrast carry
  all elevation.

## Known gaps

- The `ex-*` example components are auto-derived kit-mirror surfaces, not
  directly observed, and should be treated as reasonable extrapolations.
- No dedicated marketing-facing semantic palette is documented; any status
  colors live inside the terminal application itself.
