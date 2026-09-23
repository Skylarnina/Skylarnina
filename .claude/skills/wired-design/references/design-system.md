# Wired Design System — Full Analysis

Adapted from the Wired design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/wired/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Wired is the flagship technology-magazine brand under Condé Nast, and its
web surface refuses to dress itself up as a SaaS marketing site. The page
is unmistakably editorial: a white canvas, a strict black wordmark set in
the proprietary `WiredDisplay` (a tall, narrow, high-contrast serif used at
64px), and stacked story cards that read as a printed magazine grid
carried over to the screen. There's no atmospheric gradient, no decorative
chrome, no chromatic accent — the only color beyond the black-and-white
duet is the small `colors.link` (`#057dbc`), used exclusively for inline
body links inside long-form articles.

Type carries the whole identity. Three families ladder the system:
`WiredDisplay` (the proprietary high-contrast serif) for hero and section
headlines; `BreveText` (a humanist serif) for long-form body and bylines;
and `Apercu` (a humanist sans) for metadata, captions, eyebrow tags, and
buttons. The pairing is editorial-grade — serifs for narrative, sans for
navigation and structural labels.

Buttons are square. `rounded.none` (0px) applies across the entire
interface — newsletter sign-ups, login forms, and "Read more" CTAs all
render as sharp rectangles. The one circular shape is the icon button used
for social-share affordances. There are no soft drop-shadows; the brand
relies on hairline borders for elevation wherever it's needed.

**Key characteristics:**
- A strict black-and-white duet with no chromatic accent except the inline
  link blue — the brand reads as a printed magazine.
- A three-face typographic system: `WiredDisplay` serif for display,
  `BreveText` serif for body, `Apercu` sans for metadata and buttons.
- Square buttons (`rounded.none`) throughout — the brand never softens
  corners on interactive elements.
- A magazine-style story grid: a large feature card at top, a 2-up
  secondary row, then a vertical stack of bylined story rows separated by
  1px hairline dividers.
- The brand's one signature decorative move is the masthead band — a thin
  black strip with the wordmark centered, nothing else.
- A near-black footer band with no graphics — just text columns and a
  repeating wordmark.

## Colors

### Brand & accent
- **Ink black** (`colors.primary`, `#000000`) — the brand's only
  "accent": wordmark, headlines, CTAs, footer fill. Pure black, never
  softened.

### Surface
- **Canvas** (`colors.canvas`, `#ffffff`) — the default page background.
- **Canvas soft** (`colors.canvas-soft`, `#f5f5f5`) — a rare tint used for
  the comment-section background and search-result hover states, outside
  the main page rhythm.
- **Hairline** (`colors.hairline`, `#e0e0e0`) — 1px dividers between story
  rows, the brand's only "line."

### Text
- **Ink** (`colors.ink`, `#000000`) — every headline and body paragraph
  set in BreveText.
- **Ink soft** (`colors.ink-soft`, `#1a1a1a`) — a near-black variant used
  for caption-strong text and footer-link emphasis.
- **Body** (`colors.body`, `#757575`) — secondary metadata: bylines,
  timestamps, supporting body lines.

### Semantic
Wired operates with one inline link color and no separate error/success/
warning palette on the marketing surface; validation cues on form pages
lean on the ink-black-plus-body-gray hierarchy.
- **Link** (`colors.link`, `#057dbc`) — the inline body-link blue, used
  only inside long-form article body copy, never on UI buttons or
  navigation.

## Typography

### Font family
Three families ladder the system:
1. **WiredDisplay** — the proprietary tall-narrow, high-contrast serif
   used exclusively for display headlines, from a 64px hero down to 26px
   sub-displays; the brand's most-recognizable typographic signature.
2. **BreveText** — the proprietary humanist serif for long-form body,
   bylines, and editorial captions, set at 16–19px with 1.45–1.50
   line-height for comfortable reading density.
3. **Apercu** — a humanist sans for nav, button labels, category eyebrows,
   metadata, and captions, at weights 400/700.

Inter loads as a fourth fallback face for embedded utility surfaces (the
comment section, account pages) but doesn't appear on the main marketing or
article surface.

### Hierarchy
Full scale in `design-tokens.yaml → typography`: `display-hero` 64px/400
with -0.5px tracking for the cover-story headline, `display-lg` 48px,
`display-md` 32px, `display-sm` 26px (all WiredDisplay), and `display-xs`
20px/700 in Apercu for sans display micro-headings. Body runs
`body-serif-lg` 19px and `body-serif-md` 16px in BreveText, `body-md`
17px in Apercu for nav/metadata, down through `body-sm` 14px; `byline`
12.73px/700 uses BreveText at a relaxed 2.2 line-height.

### Principles
- Serif carries narrative, sans carries structure — the serif faces never
  set button labels or nav text, and the sans face never sets article
  body.
- Display weight stays at 400 — the proprietary WiredDisplay reads as
  elegant through its thin, tall, narrow proportions rather than through
  heavy weight.
- Bylines use BreveText weight 700 with a relaxed 2.2 line-height — that
  vertical breathing room is part of the editorial signature.

### Font substitutes
The three proprietary faces have no exact open-source match. *Playfair
Display* weight 400 at large sizes captures the high-contrast didone feel
of WiredDisplay, though it runs wider than the brand's tall-narrow
proportions. *Lora* or *Source Serif Pro* at 16–19px approximate
BreveText. *Inter* or *Manrope* at weights 400/700 approximate Apercu.

## Layout

- Base unit: 4px. Full scale in `design-tokens.yaml → spacing`, from
  `xxs` 2px to `4xl` 48px.
- Hero and story-grid sections use 48px top/bottom padding on desktop;
  bylined story rows use 16px vertical padding between them.
- The marketing container runs wide (~1400px max). The cover-story grid
  combines one large hero, a 2-up secondary-story row, and a vertical
  stack of story rows with hairline dividers.

### Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Mobile | <768px | Cover hero scales from 64px to 40px; all grids drop to 1-up; hamburger nav. |
| Tablet | 768–1023px | Secondary story grid runs 2-up. |
| Desktop | ≥1024px | Full magazine grid. |

`button-primary` renders around 44px tall (clearing WCAG AAA). Nav shows a
full link row plus a Subscribe CTA at desktop, collapsing to a hamburger at
mobile; the magazine grid keeps the hero full-width while the 2-up
secondary row drops to 1-up on mobile; story rows stay single-column at
every viewport. Cover images run full-bleed 16:9 (hero) or 4:3
(secondary); article body images stay full-width inside the article
column; author avatars crop to small inline circles beside bylines.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 — flat | none | default — nearly every surface lives here |
| 1 — hairline | 1px solid `colors.hairline` | story-row dividers, input borders |
| 2 — heavy black border | 2px solid `colors.ink` | Subscribe CTA on certain campaign moments |

Wired uses no drop-shadows anywhere; surface contrast and hairline borders
carry the entire visual hierarchy.

## Shapes

| Token | Value | Use |
|---|---|---|
| `rounded.none` | 0px | every interactive shape — buttons, inputs, cards. The brand's signature square geometry. |
| `rounded.full` | 9999px | circular icon containers only (social-share, account avatar). |

Cover stories run 16:9 edge-to-edge; secondary story cards run 4:3;
article body images hold native aspect at full column width; bylines and
avatars crop to circular 28px frames.

## Components

Full specs in `design-tokens.yaml → components`. Summary:
- **Buttons** — `button-primary` (square black CTA), `button-outline`
  (white outline), and `button-icon-circular` for share icons.
- **Cards** — `story-card-large` (the cover-story card), `story-card`
  (secondary story card), and `story-row` (the bylined list row with a
  hairline bottom border).
- **Inputs** — `text-input`, a square field with a 1px ink border.
- **Navigation** — `nav-bar` (hamburger left, masthead center, Subscribe
  right), `nav-link`, and a black `footer`.
- **Signature pieces** — `hero-band` (the white band hosting the
  cover-story headline), `masthead-band` (the thin wordmark strip),
  `category-eyebrow` (uppercase category label), `byline-row` (author
  avatar plus name plus date), and `hairline-divider`.
- **Example surfaces** (`ex-*`) — auto-derived kit-mirror demonstrations
  (pricing tier, product selector, app-shell row, data-table cell, auth
  card, modal, empty state, toast) re-skinning the brand's primitives onto
  ten common product surfaces.

## Do's and don'ts

**Do**
- Reserve `colors.primary` black for the wordmark, every CTA, and the
  footer fill — the brand IS the strict black-on-white duet.
- Set hero headlines in `typography.display-hero` (WiredDisplay 64px/400)
  — the proprietary serif is the brand's typographic signature.
- Use `rounded.none` (0px) on every button and form input — the brand
  reads as a printed magazine, and square corners are non-negotiable.
- Pair WiredDisplay (serif display) with BreveText (serif body) and Apercu
  (sans labels) — three faces, three strict roles.
- Render story rows with hairline dividers — the brand's only elevation
  cue.

**Don't**
- Don't introduce a chromatic brand accent — the link blue is reserved
  for inline body links inside articles only.
- Don't round button corners — the brand never softens its rectangular
  geometry.
- Don't drop a soft shadow on cards — surface contrast and hairlines
  carry elevation.
- Don't substitute the proprietary serif faces with a generic sans for
  display — the serif voice is the brand.
- Don't promote display weight beyond 400 — the brand's elegance comes
  from the typeface design itself, not bold weight.

## Known gaps

- The `ex-*` example components are auto-derived kit-mirror surfaces, not
  directly observed, and should be treated as reasonable extrapolations.
- Font substitutes are recommendations only — WiredDisplay, BreveText, and
  Apercu are proprietary and not publicly distributed.
