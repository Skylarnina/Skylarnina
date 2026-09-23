# Cursor Design System — Full Analysis

Adapted from the Cursor design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/cursor/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Cursor's marketing site reads as a quietly-confident developer brand that
believes in editorial calm over IDE-darkness. The base canvas is **warm
cream** (`colors.canvas`, `#f7f7f4`) holding warm near-black ink
(`colors.ink`, `#26251e`) for body and display alike. The single brand
voltage is **Cursor Orange** (`colors.primary`, `#f54e00`), reserved for
primary CTAs and the wordmark — used scarcely.

Type runs **CursorGothic** as the single sans family. Display sits at
weight 400 with negative letter-spacing — a magazine-editorial voice rather
than a tech-bombastic one. JetBrains Mono carries every code surface, and
code surfaces make up roughly half the page.

The brand's strongest visual signature is the **AI-timeline pill palette**:
five pastel pills (peach `timeline-thinking`, mint `timeline-grep`, blue
`timeline-read`, lavender `timeline-edit`, gold `timeline-done`) marking AI
agent-action stages inside in-product timeline visualizations. They live
strictly inside product UI — never used as system action colors.

**Key characteristics:**
- Warm cream canvas, not white. Ink is warm (`#26251e`), not pure black.
- A single CTA color — Cursor Orange — used scarcely.
- Display weight stays at 400, never bold; the editorial "magazine" voice.
- Five dedicated tokens for in-product agent action-stage pastels.
- Compact 8px CTA radius — a developer dialect.
- Hairline-only depth; no drop shadows.
- 80px section rhythm.

## Colors

### Brand & accent
- **Cursor Orange** — primary CTA pills, wordmark, hero accent, used
  scarcely.
- **Cursor Orange active** — press state.

### Surface
- **Canvas** — warm cream page floor.
- **Canvas soft** — IDE-pane background inside mockups.
- **Surface card** — pure white card surface, a slight contrast against
  the cream canvas.
- **Surface strong** — badges, tag pills.

### Hairlines
Three tiers — `hairline`, `hairline-soft`, `hairline-strong` — for default
dividers up through stronger panel outlines.

### Text
- **Ink** — display and emphasized body, warm near-black.
- **Body / body strong** — default running text and emphasis.
- **Muted / muted soft** — sub-titles down through disabled text.
- **On primary** — white text on Cursor Orange.

### Timeline (AI-action signature)
- **Thinking** — peach, used only inside the in-product agent timeline.
- **Grep** — mint.
- **Read** — pastel blue.
- **Edit** — lavender.
- **Done** — warm gold.

### Semantic
- **Success** — confirmation indicators.
- **Error** — validation errors.

## Typography

### Font family
**CursorGothic** is the licensed display+body family. Fallback:
`system-ui, "Helvetica Neue", Helvetica, Arial, sans-serif`. Code surfaces
switch to **JetBrains Mono**.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale — `display-mega`
(72px/400/-2.16px) down through `nav-link` (14px/500).

### Principles
- **Display weight stays at 400** — a magazine voice, never bold.
- **Negative letter-spacing on display only** — from -0.11px to -2.16px.
- **JetBrains Mono on every code surface.**

### Note on font substitutes
CursorGothic is licensed. Open-source substitute: **Inter** at weight 400
with -1.5% letter-spacing, or **GT Sectra** for a more editorial feel.

## Layout

- Base spacing unit: 4px; full ladder in `design-tokens.yaml → spacing`.
- Section padding: 80px.
- Max content width ~1200px; editorial body on a 12-column grid.
- Feature-card grids: 2-up desktop for splits, 3-up for benefits; footer
  runs 5-column at desktop.
- Generous editorial pacing — closer to a print magazine than a tech
  site. The cream canvas has plenty of breathing room; cards within bands
  sit close (16-24px gap).

## Elevation & depth

The system uses **hairline-only depth** — no drop shadows, no elevation
tiers. Cards float above the canvas via 1px hairlines and the slight
white-on-cream contrast.

| Level | Treatment | Use |
|---|---|---|
| Flat (canvas) | `canvas` (#f7f7f4) | Body bands, footer |
| Card | `surface-card` (#ffffff) | Content cards |
| Hairline border | 1px `hairline` | Card outlines, dividers |
| IDE pane | `canvas-soft` (#fafaf7) | Inside IDE-mockup cards |

The IDE-mockup card is the only "elevated" element — a white card on cream
canvas with internal pane structure mimicking the actual Cursor editor.
The timeline pastel pills add chromatic depth without any surface
elevation.

## Shapes

| Token | Value | Use |
|---|---|---|
| `rounded.none` | 0px | Reserved |
| `rounded.xs` | 4px | Inline tags |
| `rounded.sm` | 6px | Compact rows |
| `rounded.md` | 8px | CTA buttons, form inputs |
| `rounded.lg` | 12px | Cards, IDE panes |
| `rounded.xl` | 16px | Larger feature cards (rare) |
| `rounded.pill` | 9999px | Timeline pills, badges |
| `rounded.full` | 9999px | Avatars (rare) |

## Components

Definitions live in `design-tokens.yaml → components`. Summary:
- **`top-nav`** — wordmark left, primary menu (Pricing / Features /
  Enterprise / Blog / Forum / Careers), Sign In + Download CTA right.
- **Buttons** — `button-primary` (the signature orange CTA), active
  state, `button-secondary` (white card pill on cream), inline
  `button-tertiary-text`, and a larger `button-download` (ink background,
  44px) for "Download for macOS"-type CTAs.
- **`hero-band`** — full-width display headline, subhead, two CTAs
  (download + text link), and a centered IDE-mockup card below the hero
  copy.
- **`ide-mockup-card`** — a white card containing a multi-pane IDE mockup
  (sidebar + main editor + chat panel + terminal), no internal padding so
  panes fill the card edge-to-edge.
- **`ide-pane`** — individual pane inside the mockup, in JetBrains Mono.
- **`feature-card`** / **`comparison-card`** / **`testimonial-card`** —
  white cards with hairline borders.
- **Timeline pills** — five pill variants (`timeline-pill-thinking`,
  `-grep`, `-read`, `-edit`, `-done`), each marking one agent action stage
  in `caption-uppercase` type.
- **`code-block`** — inline code block, white surface, hairline border.
- **`pricing-tier-card`** / **`pricing-tier-featured`** — the featured
  tier inverts to ink background with cream text, signaling "highlighted"
  without a colored ribbon.
- **`text-input`** / **`badge-pill`** — forms and tags.
- **`cta-band`** — pre-footer "Try Cursor now" band, centered display
  headline, single Cursor Orange CTA.
- **`footer`** — closing footer, 5-column link list.

## Do's and don'ts

**Do**
- Reserve Cursor Orange for primary CTAs and the brand wordmark.
- Keep display weight at 400 — the editorial voice depends on it.
- Use the cream canvas page floor, never pure white.
- Render every code surface (inline, blocks, IDE panes) in JetBrains Mono.
- Use timeline pastels only inside in-product agent visualizations.

**Don't**
- Don't introduce a secondary brand action color — Cursor Orange is the
  only one.
- Don't drop display to bold weights (700+) — the magazine voice depends
  on 400.
- Don't add drop shadows — hairlines plus ink-on-cream contrast carry the
  depth.
- Don't use timeline pastels on non-timeline UI — they're scoped to the
  agent timeline only.
- Don't extract a CTA color from a third-party widget (cookie consent,
  OneTrust) — the brand's CTA is what appears on actual product CTAs.

## Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Mobile | < 640px | Hero h1 72→32px; IDE mockup collapses to a single-pane preview; feature grid 1-up; nav hamburger |
| Tablet | 640–1024px | Hero h1 56px; IDE mockup compresses; feature grid 2-up |
| Desktop | 1024–1280px | Full hero h1 72px; full multi-pane IDE mockup; feature grid 3-up |
| Wide | > 1280px | Content caps at 1200px |

Touch targets: the primary CTA sits at 40px height (WCAG AA, padded for
AAA); the download CTA at 44px is at AAA. Nav switches to hamburger below
768px; the IDE mockup's multi-pane layout collapses to a single primary
pane preview on mobile; feature grids collapse 3 → 2 → 1.

## Known gaps

- CursorGothic is a licensed typeface; Inter is the documented substitute.
- Animation timings (timeline-pill entrance, IDE-pane reveal) are out of
  scope.
- In-app surfaces (code editor, chat panel, agent timeline) are only
  partially captured via marketing IDE mockups.
- Form validation states beyond focus aren't visible on captured surfaces.
