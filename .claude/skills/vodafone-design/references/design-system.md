# Vodafone Design System — Full Analysis

Adapted from the Vodafone design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/vodafone/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Vodafone is a global telecom super-brand, and its web surface plays that
posture straight: heroic editorial photography — sometimes cropped so
tight only an eyeline and a phone-holding hand are visible — with one
colossal uppercase headline floating on top in the brand's proprietary,
extremely heavy display weight. The page reads more like a campaign poster
than a corporate site before settling into a calmer rhythm of light-canvas
story cards, anchored by a single red marker (the iconic speechmark logo)
that pulls the eye back to the brand's center of gravity. Nothing competes
for a second accent color — the entire decorative palette is
`colors.primary` Vodafone red, near-black `colors.ink`, and the surrounding
white/grayscale neutrals.

Typography is the second decisive voice. The custom `Vodafone` display sans
carries every headline at an almost absurdly heavy weight 800 in uppercase
for hero scale (`typography.display-hero` 144px, `typography.display-xxl`
126px), then drops to a much lighter weight 300 for the sub-displays that
follow. Body text stays in the same family at weight 400 with neutral
tracking. That swing from 800 to 300 IS the brand's typographic story — a
shout, then a calm sentence.

Every interactive CTA renders as a generously rounded pill
(`rounded.pill-lg` 60px) — Vodafone hasn't shipped a square marketing
button in years, and the pill scale ladders from 32px badge pills through
60px CTA pills up to a fully circular 9999px for icon containers. Cards
stay gentler at `rounded.card` 6px.

**Key characteristics:**
- A single primary CTA color, `colors.primary` (`#e60000`) Vodafone Red —
  filled pill for primary actions, outline pill for secondary. No third
  button variant exists.
- Massive uppercase weight-800 display type is the brand's signature; the
  lighter weight-300 siblings handle calmer secondary moments.
- The `speechmark-logo-orb` — a red square hosting Vodafone's quotation-
  mark icon — is the only piece of decorative chrome that isn't a CTA, and
  it anchors the visual center of every page.
- Pill geometry runs through every interactive shape: 60px for buttons,
  32px for inline badges. Card chrome stays at a modest 6px.
- A strict two-band page rhythm — dark ink hero, light canvas content — with
  no mid-tone grays used for elevation; the brand relies on surface
  contrast, not soft neutrals.
- Editorial photography (real portraits, real cities, real cabling) is the
  only consistent decorative system — no illustration, no gradients.

## Colors

### Brand & accent
- **Vodafone Red** (`colors.primary`, `#e60000`) — the single brand accent:
  every primary CTA pill, every speechmark logo, every conversion target.
  Never desaturated, and never used at scale for body fills; it's reserved
  for high-attention surfaces.

### Surface
- **Canvas** (`colors.canvas`, `#ffffff`) — the default light content
  background.
- **Canvas soft** (`colors.canvas-soft`, `#f2f2f2`) — a near-white tint
  used as the badge-chip background.
- **Ink** (`colors.ink`, `#25282b`) — the brand's near-black surface,
  used as the dark hero band, nav background, and footer fill; it also
  doubles as the primary text color on light surfaces.

### Text
- **Ink** (`colors.ink`, `#25282b`) — every heading and body paragraph on
  light surfaces.
- **Body** (`colors.body`, `#7e7e7e`) — secondary body text on light
  surfaces — captions, metadata, supporting copy.
- **Mute** (`colors.mute`, `#bebebe`) — the lowest-priority text color —
  placeholder text and low-key footer links.
- **On dark** (`colors.on-dark`, `#ffffff`) — all text on `colors.ink`
  surfaces (hero, footer, nav).

### Semantic
Vodafone doesn't maintain a separate semantic palette on its marketing
surface — the primary red doubles as a validation/destructive signal where
needed, while success/warning states are reserved for in-product contexts
and aren't part of the documented marketing system.

## Typography

### Font family
A single custom face — **Vodafone**, the brand's proprietary display sans
— carries the entire system, spanning weights 300, 400, 600, 700, and 800.
There's no mono companion; the rare technical label on the marketing
surface just borrows the same face at a smaller size. An icomoon icon-font
is loaded for proprietary glyphs but never functions as a typographic role.

### Hierarchy
Full scale in `design-tokens.yaml → typography`. Highlights:
`display-hero` 144px/800 uppercase (the brand's signature stencil size),
`display-xxl` 126px/800, `display-xl` 90px/800, then a shift to weight 300
for `display-lg` 48px and `display-md` 40px, weight 700 returns for
`display-sm` 32px and `display-xs` 24px, and `eyebrow-uppercase` 16px/800
marks section labels. Body runs `body-lg` 22px down to `caption-uppercase`
12px with +0.57px positive tracking for footer eyebrows.

### Principles
- Weight 800 plus uppercase is the hero voice — it's the entire reason the
  brand reads as a billboard rather than a tech site.
- Weight 300 is the calmer secondary voice, used at 40–48px and never
  smaller (to protect legibility).
- The system never mixes in a serif or a mono face — that single-family
  consistency is part of what makes it feel calm despite the shouting hero.
- Tracking stays tight at display sizes; -1px at 144px is the brand's
  calibration, and reverting to neutral tracking softens the stencil look.

### Font substitutes
The Vodafone display sans is proprietary. *Inter* at weight 800 with
`letter-spacing: -1px` at hero scale is the closest free match; *Geist*
weight 700–800 is the runner-up. For the lighter 300 weight, *Inter*
weight 300 holds its line-height well at 48px display sizes.

## Layout

- Base unit: 4px, mostly multiples of 4 with a few 5/7px values inside
  icon-padding compensation. Full scale in `design-tokens.yaml → spacing`.
- Hero and content bands use 32px gutters; vertical spacing inside the
  hero is fluid, filling the band.
- Story cards use 16px interior padding around image plus headline; button
  rows and chip rows use 12px gaps between siblings.
- Marketing content runs wide (effectively edge-to-edge with 32px desktop
  gutters, shrinking on mobile); story-card grids run 2-up desktop / 1-up
  mobile, and hero photography fills the viewport with the headline
  overlaying the top-left.
- The hero headline owns the whole top of the page; whitespace below is
  generous to let the second band breathe. Inside content cards, headline
  and copy hug close (8px gap) before a wider 32px gap to the next card.
  The footer band stays dark and dense.

### Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Mobile | <600px | Hero display scales to ~64px; story-card grid drops to 1-up; hamburger nav. |
| Tablet | 600–1023px | Story-card grid 2-up; display headlines drop to 90–110px. |
| Desktop | 1024–1399px | Full display headline at 126–144px; 2-up story grid. |
| Ultra-wide | ≥1400px | Container caps ~1400px; bands stay edge-to-edge in color. |

`button-primary` renders ~52px tall (comfortably meeting WCAG AAA at every
breakpoint). Nav collapses to a dark hamburger overlay; at mobile, the hero
photography crop tightens to the figure's face only. The speechmark logo
orb never shrinks below ~48px. Hero photography runs full-bleed 16:9/4:3;
story thumbnails run 16:9 inside 6px card chrome.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 — flat | none | most cards and panels — surface contrast does the work |
| 1 — hairline | 1px solid `colors.ink` | form inputs, footer column dividers |
| 2 — border on dark | 1px solid `colors.on-dark` on ink surfaces | outline buttons on the dark hero band |

Vodafone doesn't use soft drop-shadows; depth comes purely from the
polarity flip between `colors.ink` and `colors.canvas` bands. The hero
photograph itself is the brand's only true atmospheric effect, and the
speechmark logo orb acts as a single point of focal depth in an otherwise
flat content rhythm.

## Shapes

| Token | Value | Use |
|---|---|---|
| `rounded.none` | 0px | full-bleed hero bands, footer, banner strips |
| `rounded.xs` | 1px | tightest inline indicator (rarely used) |
| `rounded.sm` / `rounded.card` | 6px | the brand's canonical content radius — images, inputs, cards |
| `rounded.pill-md` | 32px | badge/chip pills |
| `rounded.pill-lg` | 60px | the brand's signature CTA pill — every primary/secondary button |
| `rounded.full` | 9999px | circular icon containers (video play/pause) |

Hero portraits run edge-to-edge at 16:9 or 4:3 with no internal frame;
story-card thumbnails hold 16:9 inside `rounded.card` chrome; the
speechmark logo orb is a square with 6px corners, with the SVG mark itself
filling the shape.

## Components

Full specs in `design-tokens.yaml → components`. Summary:
- **Buttons** — `button-primary` (red pill), `button-outline-red` (red
  text/border on white), `button-outline-dark` (ink text/border on white),
  and `button-icon-circular` for play/pause/chevron controls.
- **Cards** — `card-content` (the default story card) and `card-hero` (the
  larger lead-story variant).
- **Inputs** — `text-input`, a 6px-radius field with a 1px ink border.
- **Navigation** — a dark `nav-bar`, `nav-link`, and a dark `footer` with
  uppercase column eyebrows.
- **Signature pieces** — `hero-band-dark` (the primary dark photo hero),
  `hero-band-red` (rare full-bleed red campaign hero),
  `content-band-light` (the white band following every hero),
  `speechmark-logo-orb` (the brand's visual anchor), `badge-chip` (inline
  category tags), and `divider-on-dark` (hairline between dark sections).
- **Example surfaces** (`ex-*`) — auto-derived kit-mirror demonstrations
  (pricing tier, product selector, app-shell row, data-table cell, auth
  card, modal, empty state, toast) re-skinning the brand's primitives onto
  ten common product surfaces.

## Do's and don'ts

**Do**
- Reserve `colors.primary` Vodafone Red for primary CTAs and the
  speechmark-logo orb — every conversion target uses the red pill.
- Set hero headlines in weight 800 UPPERCASE with tight -1px tracking —
  that stencil look is the brand voice.
- Round every interactive element to the 60px pill; the brand never uses
  square corners on CTAs.
- Cycle page surfaces dark hero → light content → dark footer; surface
  contrast is the depth cue.
- Pair editorial portrait photography with the massive display headline
  overlay — that combination is the brand's signature.
- Keep the speechmark logo orb at a consistent size relative to
  surrounding content; it's the brand's center of gravity on every page.

**Don't**
- Don't add a second accent color; the brand operates with red, ink, and
  grayscale only.
- Don't render hero headlines in sentence case — hero display IS
  uppercase weight 800.
- Don't render the primary CTA as a square rectangle; the 60px pill is
  non-negotiable.
- Don't drop a soft shadow on cards — the brand relies on surface-color
  contrast, not shadow.
- Don't substitute the speechmark logo orb with a wordmark or different
  shape; the orb is the iconic mark.
- Don't pair the weight-800 display face with zero letter-spacing at
  144px — the -1px tracking is part of the calibration.

## Known gaps

- The `ex-*` example components are auto-derived kit-mirror surfaces, not
  directly observed, and should be treated as reasonable extrapolations.
- No separate error/success/warning palette is documented for the public
  marketing surface — Vodafone Red doubles as the validation signal.
- Font substitutes are recommendations only — the Vodafone display sans is
  proprietary and not publicly distributed.
