# Composio Design System — Full Analysis

Adapted from the Composio design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/composio/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Composio's marketing site reads like a serious developer-infrastructure
brand — closer in atmosphere to Vercel or Stripe Docs than to a typical
AI-tools startup. The base canvas is a near-black `colors.canvas`
(`#0f0f0f`) holding white type and a single voltage of **deep electric
blue** (`colors.primary`, `#0007cd`) that carries every primary CTA, the
brand wordmark, and the atmospheric spotlight glow behind the homepage
hero.

Type runs **abcDiatype** as a single sans family across display, body,
navigation, and captions — display sits at weight 500, confident but not
bombastic. Code blocks and terminal mockups switch to JetBrains Mono.

The page rhythm is monolithic: a dark canvas runs top to bottom with
subtle elevation via card-surface brightness steps rather than color
changes. The brand's strongest visual signature is a **four-pane terminal-
style mockup** — a 2x2 grid of dark code/output panels with a central blue
spotlight glow behind them.

**Key characteristics:**
- Single accent (`#0007cd`) for primary CTAs, wordmark, and spotlight
  glows.
- Single sans family — abcDiatype carries everything except code
  (JetBrains Mono).
- Dark monolithic canvas; depth comes from `surface-card` and
  `surface-card-elevated` brightness steps, not shadows.
- The 2x2 terminal-mockup hero is the brand signature.
- Compact CTA geometry at `rounded.md` (8px), not full pills — a
  developer-tool dialect.
- Spotlight-glow atmospheric backdrop: a radial blue glow centered behind
  hero content.
- 96px section rhythm.

## Colors

### Brand & accent
- **Composio Blue** — primary CTAs, wordmark, spotlight-glow center.
- **Composio Blue active** — press state.
- **Spotlight glow tone** — a brighter blue used inside radial atmospheric
  glows.
- **Accent cyan** — sparingly on data-flow visualizations.
- **Accent violet** — inside specific product illustrations only.

### Surface
- **Canvas** — near-black page floor.
- **Canvas deep** — pure black, reserved for terminal-mockup grids and
  code blocks.
- **Surface card** — default content card.
- **Surface card elevated** — terminal panes, secondary buttons.
- **Surface strong** — dropdown menus.

### Hairlines
Three tiers — `hairline`, `hairline-soft`, `hairline-strong` — for default
dividers up through stronger panel outlines.

### Text
- **Ink / body strong** — display headlines (white).
- **Body** — default running text, soft gray.
- **Muted / muted soft** — sub-titles, breadcrumbs, disabled text.
- **On primary** — white text on blue CTAs.

### Semantic
- **Success** — "online"/"active" indicators.
- **Error** — validation errors.

## Typography

### Font family
**abcDiatype** (Lineto) runs across every text role; code blocks switch to
**JetBrains Mono**. Fallback: `ui-sans-serif, system-ui, sans-serif`.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale — `display-mega`
(72px/500/-2.16px) down through `nav-link` (14px/500).

### Principles
- **Display weight stays at 500** — confident but not display-bold.
- **abcDiatype across every role** — no display/body family split.
- **JetBrains Mono on every code surface.**

### Note on font substitutes
abcDiatype is a Lineto licensed typeface. Open-source substitute: **Inter**
at weight 500 with -1.5% letter-spacing.

## Layout

- Base spacing unit: 4px; full ladder in `design-tokens.yaml → spacing`.
- Section padding: 96px for major bands.
- Max content width ~1200px; editorial body on a 12-column grid; the
  terminal-mockup grid is a 2x2 equal-size layout.
- Toolkit grid: 4-up desktop → 2-up tablet → 1-up mobile; footer runs
  5-column at desktop.
- The dark canvas creates its own depth, so whitespace can stay tight
  without feeling crowded — 96px between bands, 24px between cards inside
  a band.

## Elevation & depth

The system uses **brightness-step elevation**: surfaces step up in
brightness instead of casting drop shadows. Combined with subtle radial
blue glows, this creates a focused dark-mode atmosphere.

| Level | Treatment | Use |
|---|---|---|
| Flat (canvas) | `canvas` (#0f0f0f) | Body bands, footer |
| Recessed | `canvas-deep` (#000000) | Terminal-mockup grid background, code blocks |
| Card | `surface-card` (#181818) | Default content cards |
| Card elevated | `surface-card-elevated` (#222222) | Terminal panes, secondary buttons |
| Atmospheric glow | Radial gradient using `primary-glow` | Hero spotlight backdrop |

Decorative depth comes from spotlight-glow backdrops (a radial blue
gradient centered behind hero content) and the terminal-pane brightness
ladder — the 2x2 mockup uses a canvas-deep outer frame with
surface-card-elevated panes inside.

## Shapes

| Token | Value | Use |
|---|---|---|
| `rounded.none` | 0px | Reserved |
| `rounded.xs` | 4px | Inline tags |
| `rounded.sm` | 6px | Compact rows |
| `rounded.md` | 8px | CTA buttons, form inputs |
| `rounded.lg` | 12px | Toolkit cards, code blocks, terminal panes |
| `rounded.xl` | 16px | Feature cards, terminal-mockup grids |
| `rounded.pill` | 9999px | Section-label badges |
| `rounded.full` | 9999px | Avatar plates (rare) |

Compact developer-ergonomic radii — 8px CTAs, 12-16px cards — signal
"developer tool" rather than "consumer brand."

## Components

Definitions live in `design-tokens.yaml → components`. Summary:
- **`top-nav-dark`** — 64px bar; wordmark left, primary menu (Product /
  Toolkits / Docs / Pricing / Customers / Blog), GitHub stars + Sign In +
  "Get started" right.
- **Buttons** — `button-primary` (the signature blue CTA, 8px radius),
  active state, `button-secondary-dark`, `button-outline`,
  `button-tertiary-text`.
- **`hero-band`** — full-width display headline plus subhead, two CTAs,
  and a spotlight-glow backdrop emanating from behind the centered
  terminal-mockup grid.
- **`terminal-mockup-grid`** — the brand's strongest signature: a 2x2
  grid of dark code/output panels inside a 16px-radius container.
- **`terminal-pane`** — individual code/output panel inside the grid.
- **`spotlight-glow-card`** — a large feature card with centered display
  headline and a radial blue glow behind it.
- **`feature-card`** — 3-up benefit grid.
- **`toolkit-card`** + **`toolkit-icon`** — 4-up toolkit grid (Slack,
  GitHub, Stripe, Notion, Linear, etc.), each with a 40px square icon
  plate, toolkit name, and one-line description.
- **`testimonial-card`** — quote card.
- **`code-block`** — inline code/terminal block.
- **`text-input`** / **`search-input`** — dark-surface form fields.
- **`badge-pill`** — small uppercase section-label pill.
- **`cta-band-spotlight`** — pre-footer band with a centered radial
  spotlight glow, display headline, and a single primary CTA.
- **`footer-dark`** — closing footer, 5-column link list.

## Do's and don'ts

**Do**
- Reserve the electric-blue accent for primary CTAs, wordmark, and
  spotlight glows.
- Use `rounded.md` (8px) for every CTA — not full pills.
- Use the brightness-step ladder for elevation; avoid drop shadows.
- Pair every hero with a centered radial blue spotlight glow.
- Render code/CLI commands in JetBrains Mono.
- Use the 2x2 terminal-mockup grid as the homepage hero anchor.

**Don't**
- Don't introduce a secondary brand color — cyan and violet are
  illustrative-only.
- Don't use full pills on CTAs.
- Don't drop display weight to 400.
- Don't add extra shadow tiers.
- Don't use canvas-deep (#000000) outside terminal/code surfaces.
- Don't extract a CTA color from a third-party widget (cookie consent,
  OneTrust) — the brand's CTA color is what appears on actual page CTAs.

## Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Mobile | < 640px | Hero h1 72→36px; terminal-mockup grid collapses to a single pane; toolkit grid 1-up; nav hamburger |
| Tablet | 640–1024px | Hero h1 56px; terminal-mockup grid stays 2x2; toolkit grid 2-up |
| Desktop | 1024–1280px | Full hero h1 72px; full 2x2 terminal mockup; toolkit grid 4-up |
| Wide | > 1280px | Content caps at 1200px |

Touch targets: the primary CTA sits at 40px height (WCAG AA, padded for
AAA); the search input is 40px. Nav switches to a hamburger below 768px;
the terminal-mockup 2x2 grid collapses to a single pane on mobile; the
toolkit grid collapses 4 → 2 → 1; the hero spotlight glow persists at
every breakpoint.

## Known gaps

- abcDiatype is licensed; Inter is the documented substitute.
- Animation timings are out of scope.
- In-product surfaces (toolkit dashboards, agent playground) sit behind
  login walls.
- Form validation states beyond focus aren't visible on captured surfaces.
