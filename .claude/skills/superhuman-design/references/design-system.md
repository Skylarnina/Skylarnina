# Superhuman Design System — Full Analysis

Adapted from the Superhuman marketing-site design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/superhuman/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Superhuman's marketing pages open in an editorial dark register: a deep
indigo-navy `colors.primary` (`#1b1938`) canvas overlaid with a soft
violet-and-sky atmospheric backdrop and a half-bleed portrait subject — often
a person looking off-frame, photographed at twilight. Headlines render at
`typography.display-xxl` (64px / weight 540) with negative tracking, set in
white over the indigo. A single rounded-rectangle CTA button anchors each
band; the brand never stacks two or three buttons together.

The body of every page then flips to white. `colors.canvas` (`#ffffff`) takes
over below the hero, with body type in `colors.ink` (`#292827` — a slightly
warm dark grey, never pure black) and feature rows alternating between white
and `colors.canvas-soft` (a barely-tinted off-white). Pricing tiers sit on
this white surface; the featured tier inverts to indigo navy, completing the
brand's binary polarity.

Every page closes with a **deep-teal CTA band** (`colors.surface-teal-deep`,
`#0e3030`) — a single chromatic interlude, rich and almost-black green-blue,
that breaks up what would otherwise be an indigo/white-only page. The band
always contains the closing headline at `typography.display-lg` paired with
one white-pill button.

Typography runs on **Super Sans VF**, a proprietary variable display sans at
unusual mid-weights (460, 540, 600). The variable axes let the brand pick
precise sub-default weights that read warmer and more human than a typical
400/500/700 SaaS scale. Display sizes carry negative tracking from -1.32px
down to -0.315px depending on size, and line-heights run unusually tight
(0.96 at 48–64px).

**Key characteristics:**
- A three-canvas system: indigo navy for the hero, white for the body, deep
  teal for the closing CTA.
- A half-bleed portrait subject in the hero with a violet-sky atmospheric
  backdrop — a person looking off-frame is a recurring visual.
- A single CTA per band; marketing pages never crowd actions.
- Super Sans VF at sub-default weights (460, 540, 600) — the brand's
  typographic warmth signature.
- Tight line-heights (0.96) on display sizes for a vertically compressed,
  editorial feel.
- Off-warm-grey body ink (`#292827`), never pure black.
- A pale-violet pill CTA on the hero only; rounded-rectangle CTAs everywhere
  else.

## Colors

> Source pages: home (`/`), `/products/go-ai-assistant`, `/contact-sales`,
> `/plans`.

### Brand & accent
- **Primary indigo navy** — the brand's primary surface and CTA color: hero
  canvas, filled rounded-rectangle button, featured pricing tier.
- **Indigo deep** — a pressed-state / deeper navy used in hero gradient
  stops.
- **Surface violet soft** — the hero pill-button fill, a pale violet over the
  indigo canvas; also appears in atmospheric backdrops.
- **Surface teal deep** — the signature closing-CTA band color, rich
  green-blue, almost black.
- **Surface teal mid** — a slightly lifted teal for nested chrome inside the
  band.

### Surface
- **Canvas** — the default body background, white.
- **Canvas soft** — a barely-warm off-white for alternating feature-row
  bands.
- **Hairline / hairline dark** — 1px border tiers for light and dark
  surfaces.

### Text
- **Ink** — default body text, warm dark grey, never pure black.
- **Ink mute / ink faint** — secondary and tertiary/disabled tiers.
- **On primary** — white text on dark navy/teal surfaces.
- **On dark mute / on dark faint** — translucent-white secondary and
  tertiary text on dark.

## Typography

### Families
- **Super Sans VF** — a proprietary variable sans using sub-default weights
  (460 / 540 / 600). Fallback: the system font stack.

Substitute with **Inter Variable** at the same weight values (460/540/600) —
its variable axes behave closely. Avoid fixed-weight Inter at plain
400/500/600; the brand specifically picks the in-between weights.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale (display-xxl 64px
down to micro 12px). Principles:
- Sub-default weights (460/540/600) give the type a quiet warmth that
  distinguishes it from default SaaS type scales.
- Display leading stays unusually tight (0.96 at 48–64px).
- Negative tracking on display sizes scales proportionally from -1.32px at
  48px.

## Layout

- Base spacing unit: 8px, with 2/4/12px sub-tokens for fine work.
- Section padding runs 64–96px on most sections; the closing teal band opens
  up to 96–128px for editorial weight.
- Card interior padding: 32px on pricing cards, 24px on alternating feature
  rows.
- The hero spans full viewport width with the violet-sky backdrop
  edge-to-edge; content centers in a ~960px column, matching the body's
  960–1100px column.
- Pricing collapses 3-up → 2-up → 1-up at 1024/768px.
- The brand uses generous editorial whitespace on both polarities — section
  gaps trend toward 96px, and the teal closing band gets up to 128px of
  vertical air, part of the brand's "considered, slow-tempo" feel.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 | Flat | Default surface |
| 1 | `0 1px 3px rgba(0,0,0,0.08)` | Subtle card lift |
| 2 | `0 8px 24px rgba(0,0,0,0.12)` | Floating panels, modals |
| 3 | Atmospheric backdrop (violet-sky over indigo) | The hero's depth medium |

### Decorative depth
The hero's depth comes from a **violet-sky atmospheric backdrop** — a soft
indigo-to-violet-to-sky-blue radial wash sitting behind the portrait subject,
implemented as a CSS radial gradient or large background image. Below the
hero, depth stays minimal; the white canvas is flat.

## Shapes

| Token | Value | Use |
|---|---|---|
| rounded.xs | 4px | Hairline tags |
| rounded.sm | 6px | Form inputs |
| rounded.md | 8px | Buttons — the brand's signature rounded-rectangle shape, never a pill |
| rounded.lg | 12px | Pricing cards, feature cards |
| rounded.xl | 16px | Modal dialogs, large feature cards |
| rounded.full | 9999px | Pill tabs in feature rows, hero CTA |

The hero uses **half-bleed portrait subjects** — a person photographed at
twilight, looking off-frame, occupying the right half of the hero. The
portrait extends edge-to-edge vertically and stops mid-canvas horizontally;
type sits on the left. Other photography is rare — product-UI mockups handle
most other illustrative needs.

## Components

Definitions live in `design-tokens.yaml → components`. Summary:
- **Buttons** — `button-primary-dark` (the dominant rounded-rectangle CTA,
  with a pressed variant), `button-on-dark-pill` (hero-only pale-violet
  pill), `button-secondary-outline`, `button-on-teal` (closing-band CTA).
- **Cards** — `card-feature-light`, `card-pricing` and its inverted
  `card-pricing-featured` (indigo), `card-teal-band` (the closing CTA panel),
  `card-feature-row` (alternating body rows).
- **Inputs** — `text-input`, 6px radius.
- **Navigation** — `nav-bar-dark` (over the indigo hero) and `nav-bar-light`
  (body/pricing pages).
- **Tabs** — `pill-tab-light`, the feature-category picker below the hero.
- **Footer** — `footer-light`, 4 link columns plus a legal row.

## Do's and don'ts

**Do**
- Pair every hero with the violet-sky atmospheric backdrop and a half-bleed
  portrait subject when possible.
- Render display tiers at sub-default weights (460/540) — the warmth is the
  typographic signature.
- Use 8px rounded-rectangle CTAs everywhere except the hero, where pill-shaped
  is the rule.
- Close every marketing page with a deep-teal CTA band.
- Use warm dark grey for body text, never pure black.
- Apply tight 0.96 line-height on display sizes.

**Don't**
- Don't use pill-shaped buttons in the body of the page; the pill is
  hero-only.
- Don't bump display weight above 540 unless rendering emphasized inline body
  at 700.
- Don't render body text in pure black.
- Don't omit the closing teal band.
- Don't introduce accent colors beyond indigo, violet-soft, teal, and the
  off-warm-greys.

## Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Wide | ≥1440px | Half-bleed portrait at full scale; teal band 128px tall |
| Desktop | 1024–1440px | Default max-width; pricing 3-up |
| Tablet | 768–1023px | Pricing 2-up; portrait crops tighter |
| Mobile | <768px | Pricing 1-up; hamburger nav; display drops 64 → 36px |

Buttons hit ≥44×44px on mobile via 12px vertical padding, meeting WCAG AAA;
form fields stay at the 44px minimum. Display tiers stair-step 64 → 48 → 36 →
28 → 22px, the half-bleed portrait crops to head-and-shoulders on mobile, and
the closing teal band's vertical padding reduces from 128px to 64px. Hero
portrait imagery uses `srcset` with desktop favoring the full half-bleed
composition and mobile cropping to head-and-shoulders.

## Known gaps

- Super Sans VF is proprietary; the documented Inter Variable substitute
  approximates but doesn't reproduce its exact sub-default weight metrics.
- Form validation/error styling wasn't captured from the inspected pages.
- The precise atmospheric-gradient stops behind the portrait subject are
  approximated as a radial wash rather than extracted pixel-exact.
