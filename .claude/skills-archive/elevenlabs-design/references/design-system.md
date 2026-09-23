# ElevenLabs Design System — Full Analysis

Adapted from the ElevenLabs design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/elevenlabs/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

ElevenLabs reads like a quietly editorial print magazine that happens to
be a voice-AI product. The base canvas is off-white `colors.canvas`
(`#f5f5f5`) holding warm near-black ink `colors.ink` (`#0c0a09`). The
brand's voltage is photographic, not chromatic: soft pastel atmospheric
gradient orbs (mint, peach, lavender, sky, rose) drift through the page as
the only "color" moments. There is no neon accent, no saturated CTA color,
no dark-canvas dev-tools atmosphere anywhere in the system.

Type pairs Waldenburg Light (a custom serif at weight 300) for display
with Inter for body, navigation, and captions. The display weight staying
at 300 — never bold — is the editorial signature.

CTAs stay subtle: a near-black ink pill is the primary action, a
transparent outline is the secondary. The brand trusts atmospheric
photography and modest type weights, rather than loud color, to carry the
brand work.

**Key characteristics:**
- Off-white canvas with warm near-black ink; no saturated CTA color
  anywhere.
- A single primary action treatment — an ink pill at full radius —
  while atmospheric gradients carry the visual brand voltage instead of a
  second accent color.
- Display runs Waldenburg Light at weight 300, an editorial-magazine
  voice.
- Body runs Inter at weight 400 with subtle positive letter-spacing
  (+0.15 to 0.18px).
- Five pastel gradient-orb tokens (mint, peach, lavender, sky, rose) used
  strictly as atmospheric brand decoration.
- Soft pill geometry throughout — pill radius for CTAs, `xl` (16px)
  radius for cards.
- A 96px section rhythm.

## Colors

### Brand & accent
- **Ink Primary** (`#292524`) — the primary action color, a warm near-black
  pill, used scarcely.
- **Ink Primary Active** (`#0c0a09`) — the press state.

### Surface
- **Canvas** (`#f5f5f5`) — the off-white page floor.
- **Canvas Soft** (`#fafafa`) — a lighter band for subtle alternating
  sections.
- **Canvas Deep** (`#0c0a09`) — the same value as ink, used for the rare
  dark-mode hero on the Agents page.
- **Surface Card** (`#ffffff`) — pure white card surface.
- **Surface Strong** (`#f0efed`) — badges and voice-icon plates.
- **Surface Dark** (`#0c0a09`) — the dark hero/CTA band canvas.
- **Surface Dark Elevated** (`#1c1917`) — cards placed on the dark canvas.

### Hairlines
- **Hairline** (`#e7e5e4`) — the default 1px divider.
- **Hairline Soft** (`#f0efed`) — a lighter divider.
- **Hairline Strong** (`#d6d3d1`) — a stronger panel outline.

### Text
- **Ink** (`#0c0a09`) — display and primary text.
- **Body** (`#4e4e4e`) — default running text.
- **Body Strong** (`#292524`) — the same value as primary, used for
  emphasis.
- **Muted** (`#777169`) — sub-titles.
- **Muted Soft** (`#a8a29e`) — disabled text.
- **On Primary** (`#ffffff`) — white text on the ink pill.
- **On Dark** (`#ffffff`) — white text on the dark hero.
- **On Dark Soft** (`#a8a29e`) — muted off-white on dark surfaces.

### Atmospheric gradient stops (signature)
Mint (`#a7e5d3`), peach (`#f4c5a8`), lavender (`#c8b8e0`), sky (`#a8c8e8`),
and rose (`#e8b8c4`) — five soft orb colors that appear only as radial-
gradient atmospheric blooms inside `gradient-orb-card` or behind hero
copy. They never fill a button, never color text.

### Semantic
- **Success** (`#16a34a`) — confirmation states.
- **Error** (`#dc2626`) — validation errors.

## Typography

### Font family
Waldenburg Light is the licensed display serif at weight 300; Inter
carries body, navigation, captions, and buttons. Fallback stacks:
`'Times New Roman', serif` for Waldenburg, `sans-serif` for Inter.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale. Key entries:
`display-mega` (64/300, -1.92px tracking, homepage hero h1), `display-xl`
(48/300, -0.96px, subsidiary heroes), `display-lg` (36/300, -0.36px,
section heads), `display-md` (32/300, -0.32px, sub-section heads),
`display-sm` (24/300, 0px, card group titles), `title-md` (20/500, Inter,
component titles), `body-md` (16/400, +0.16px, default body),
`caption-uppercase` (12/600, +0.96px, section labels and badges), `button`
(15/500, CTA pill label).

### Principles
Display weight stays fixed at 300 — Waldenburg Light is the editorial
signature, and display copy is never bolded. Body type carries subtle
positive letter-spacing at +0.15 to 0.18px on Inter, slightly looser than
default Inter, for a more editorial feel. Display type pulls the opposite
direction, with negative letter-spacing tightening from -0.32px up to
-1.92px at the largest sizes.

### Font substitutes
Waldenburg is licensed. Open-source substitutes: **EB Garamond** at weight
300 (slightly more humanist) or **GT Sectra** (closer to Waldenburg's
modernity). Inter is used directly for body since it's the same family
ElevenLabs uses.

## Layout

- **Base unit:** 4px. Full scale: `xxs` 4px, `xs` 8px, `sm` 12px, `base`
  16px, `md` 20px, `lg` 24px, `xl` 32px, `xxl` 48px, `section` 96px.
- **Section padding:** 96px.
- **Max content width:** roughly 1200px.
- **Grid:** a 12-column editorial-body grid; feature card grids run 2-up
  at desktop for hero splits, 3-up for benefit grids; the footer runs
  5-column at desktop.
- **Whitespace philosophy:** generous, print-magazine pacing — 96px
  between bands, with cards inside a band sitting close together (16-24px
  gap). The atmospheric gradient orbs occupy generous breathing space
  without competing with copy.

## Elevation & depth

The system runs on hairline-plus-soft-drop: cards float above the
off-white canvas via 1px hairlines and a single subtle shadow tier.
Atmospheric depth comes from the gradient orbs rather than shadow layers.

| Level | Treatment | Use |
|---|---|---|
| Flat (canvas) | `canvas` (#f5f5f5) | body bands, footer |
| Card | `surface-card` (#ffffff) | content cards |
| Hairline border | 1px `hairline` | card outlines |
| Soft drop | `0 4px 16px rgba(0,0,0,0.04)` | hovered cards, the system's single shadow tier |
| Gradient orb | radial gradient in one of the five `gradient-*` colors | atmospheric depth, never a card surface |

The pastel gradient orbs are the brand's strongest atmospheric pattern —
soft radial blooms in mint, peach, lavender, sky, or rose drift through
hero bands and feature sections without containing any content; they are
pure atmosphere.

## Shapes

| Token | Value | Use |
|---|---|---|
| `rounded.none` | 0px | reserved, effectively unused |
| `rounded.xs` | 4px | inline tags |
| `rounded.sm` | 6px | compact rows |
| `rounded.md` | 8px | form inputs |
| `rounded.lg` | 12px | compact cards |
| `rounded.xl` | 16px | feature cards, pricing tiers |
| `rounded.xxl` | 24px | gradient-orb cards, the extra-soft variant |
| `rounded.pill` | 9999px | all CTA buttons, badges |
| `rounded.full` | 9999px | voice-icon circles, avatars |

## Components

Definitions live in `design-tokens.yaml → components`. Summary:
- **top-nav** — canvas background, 64px tall; ElevenLabs wordmark left, a
  primary menu (Creative / Agents / Video / Pricing / Enterprise / Docs),
  Sign In plus a "Try free" primary CTA on the right.
- **Buttons** — `button-primary` (near-black ink pill, 40px height, full
  radius), `button-primary-active` (darker press state), `button-outline`
  (transparent pill with a 1px ink border), `button-tertiary-text` (inline
  ink text link).
- **Hero & atmospheric** — `hero-band` (canvas background, `display-mega`
  headline, subhead, two CTAs, and an atmospheric orb behind the centered
  headline), `gradient-orb-card` (a large card with a soft radial orb
  behind centered display copy, 24px radius, one of the five gradient
  tokens per variant), `audio-waveform-card` (a waveform visualization
  with a play button and voice metadata).
- **Cards** — `feature-card` (white, 16px radius, 24px padding, hairline
  border, used in 2-up or 3-up grids), `product-card-stack` (stacked
  product previews with no internal padding so children fill edge-to-
  edge), `testimonial-card` (quote card, 32px padding).
- **Voice library** — `voice-row` (horizontal row with a 32px circular
  voice icon, name/accent stack, and an optional preview button, divided
  by hairlines), `voice-icon-circular` (32px circle holding initials or a
  voice glyph).
- **Pricing** — `pricing-tier-card` (white, hairline border, 32px
  padding), `pricing-tier-featured` (inverts to the dark surface with
  on-dark text, same shape).
- **Forms & tags** — `text-input` (white, 8px radius, 44px height, 1px
  strong-hairline border that thickens to 2px ink on focus), `badge-pill`
  (surface-strong fill, uppercase caption type, full pill radius).
- **CTA / footer** — `cta-band` (canvas background, centered `display-lg`
  headline, a single ink pill CTA, 96px padding), `footer` (canvas
  background, 5-column link list, 64×48px padding), `footer-link` (plain
  text link in the body color).

## Do's and don'ts

**Do**
- Reserve the ink pill for primary CTAs.
- Use Waldenburg Light at weight 300 for every display headline — never
  bold.
- Use Inter at +0.15 to 0.18px tracking for body — the editorial dialect.
- Use atmospheric gradient orbs (mint/peach/lavender/sky/rose) as
  decoration only.
- Use the pill shape for every CTA and badge.

**Don't**
- Don't introduce a saturated brand action color — the ink pill is the
  only CTA color in the system.
- Don't bold display copy; it sits at weight 300, and bolding it shifts
  the voice from editorial to generic consumer-marketing.
- Don't use gradient orbs as button fills, text colors, or component
  backgrounds — they are pure atmosphere.
- Don't use sharp `rounded.none` (0px) on CTAs — pill geometry is the
  brand button.
- Don't drop body Inter to weight 300 to match Waldenburg — body stays at
  400/500 for legibility.
- Don't extract a CTA color from a third-party widget (cookie consent,
  OneTrust) — the brand's CTA color is only what appears on actual product
  CTAs.

## Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Mobile | < 640px | hero h1 scales 64→32px; feature cards 1-up; nav becomes a hamburger; gradient orbs shrink |
| Tablet | 640–1024px | hero h1 at 48px; feature cards 2-up |
| Desktop | 1024–1280px | full hero h1 at 64px; feature cards 3-up |
| Wide | > 1280px | content caps at 1200px |

Touch targets: the primary pill sits at 40px height (WCAG AA, padded
toward AAA); voice-icon circles are 32px but the padded row creates an
effective 48px tap zone. Collapsing strategy: top nav switches to a
hamburger below 768px; the feature grid steps 3-up → 2-up → 1-up; gradient
orbs reduce diameter at every breakpoint but never disappear entirely.

## Known gaps

- Waldenburg is a licensed typeface; EB Garamond and GT Sectra are
  documented substitutes.
- Animation timings (orb drift, waveform pulse, hero entrance) are out of
  scope.
- In-product surfaces (the voice-library editor, the agent playground)
  are only partially captured via marketing mockups.
- Form validation states beyond the focus state aren't visible on the
  captured surfaces.
