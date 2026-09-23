# Slack Design System — Full Analysis

Adapted from the Slack marketing-site design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/slack/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Slack's marketing surface revolves around one enduring asset: a deep
aubergine primary (`colors.primary`, `#4a154b`) that shows up on every
filled button, the featured pricing tier, the footer band, and the
wordmark itself. Around that anchor color the system builds something
surprisingly delicate — cream and pale-lavender hero canvases
(`colors.canvas-cream`, `colors.canvas-lavender`) washed with soft
pastel-mesh gradients (peach, lavender, dusty green) that sit behind
floating product-UI screenshots rendered at roughly 3:2.

Type splits across two proprietary humanist sans families. The display
face runs at weight 700 across 32-64px with negative letter-spacing for a
tight, editorial headline density. The body/UI face relaxes to a 1.55
line-height so paragraph copy reads quietly and never competes with the
aubergine moments.

Every button in the system is a pill at the full 90px radius, and the
padding is unusually generous (28-30px horizontal) — buttons feel
deliberately over-padded rather than snug. The primary aubergine pill is
typically the only filled button on a given screen; secondary actions use
a soft lavender pill instead. Inline links break from aubergine entirely
into a saturated blue (`colors.link-blue`) — the system's only other
chromatic color.

**Key characteristics:**
- Single aubergine primary reused across CTAs, the featured pricing tier,
  the footer band, and the wordmark — brand "chromatic monotheism."
- Cream-lavender hero canvas with diffused pastel-mesh gradients and
  floating product-UI mockups composited on top, never inside a card.
- Pill buttons at the full 90px radius with generous 28-30px horizontal
  padding — deliberately over-padded by typical SaaS standards.
- Tight negative letter-spacing on display sizes (down to -0.768px at
  64px) for editorial-density headlines.
- Blue inline links — the only non-aubergine chromatic accent in body
  copy.
- Pastel-mesh gradient atmospherics behind every hero band; product UI
  sits above the gradient, never nested inside it.
- Statistics rendered as massive aubergine numerals on white — scale
  alone carries quantitative emphasis.

## Colors

### Brand & accent
- **Primary** — the aubergine surface and CTA color; filled buttons, the
  featured pricing tier, the footer band, the wordmark.
- **Primary deep / press / tint** — near-identical siblings and pressed/
  bordered variants of the same hue.
- **Link blue / link hover** — the sole chromatic alternative to
  aubergine, used only in body copy.

### Surface
- **Canvas** — default white content surface.
- **Canvas cream** — warm off-white for hero gradients and feature bands.
- **Canvas lavender** — pale lavender used as the secondary-button surface
  and as a soft section band.
- **Surface aubergine** — the primary color reused as a full surface fill
  (featured tier, footer, dark bands).
- **Hairline** — 1px borders on cards and table dividers.

### Text
- **Ink** — primary body text on light surfaces, just shy of pure black.
- **Ink mute** — secondary text, captions, helper copy.
- **On primary** — white text on aubergine surfaces and filled CTAs.
- **On aubergine mute** — desaturated mauve for secondary text on
  aubergine surfaces.

### Semantic
- **Error** — form error and destructive-action color.
- **Success** — inline success indicators.

## Typography

### Families
The display tier is **Salesforce Avant Garde**, a proprietary humanist
sans with broad apertures and a mildly geometric character; it falls back
to the system stack. The UI tier is **Salesforce Sans**, a separate
proprietary face for body, captions, and button labels. Neither face is
publicly licensed — **Inter** is the recommended open-source substitute
for both tiers, since it approximates both the display weight behavior
and the body warmth reasonably well. **Lato** is a softer alternative for
body sizes specifically.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale (display-xxl at
64px down to micro-cap at 12px). Governing principles:
- Tight negative tracking across every display size (from -0.768px at
  64px up through smaller sizes) pulls the naturally wide proprietary
  face into editorial density.
- Body copy sits at a relaxed 1.55 line-height — readable without
  drifting into airy 1.7+ territory.
- Eyebrows render in all caps with positive tracking (0.96px down to
  0.144px depending on size).

## Layout

- Base spacing unit: 8px, with 4/12/16/20/24/28px sub-tokens for finer
  vertical rhythm (full scale in `design-tokens.yaml → spacing`).
- Section padding runs 64-96px on marketing surfaces, tightening to 48px
  on transactional pages.
- Card interior padding: 32px on pricing cards, 48px on aubergine band
  cards.
- Marketing pages center in a roughly 1240px container, with pastel-mesh
  gradients deliberately bleeding past the container edge.
- Pricing grids collapse 4-up → 2-up → 1-up at 992px / 768px.
- On marketing pages the pastel-mesh gradients themselves fill most of
  the negative space, so sections feel expansive without being literally
  empty; on transactional pages the gradients drop and whitespace reverts
  to a more conventional 48px section rhythm.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 | Flat | Default surface |
| 1 | `rgba(0,0,0,0.1) 0 5px 20px 0` | Floating buttons on hero |
| 2 | `rgba(0,0,0,0.1) 0 0 32px 0` | Product-UI mockup composites |
| 3 | `rgba(0,0,0,0.2) 0 1px 10px 0` | Toast / notification chrome |
| 4 | `rgb(97,31,105) 0 0 0 1px inset` | Aubergine inset border (focus, special chrome) |

The brand's real depth language is the pastel-mesh gradient itself: peach,
lavender, and dusty-green stops blurred at large radii create a luminous
backdrop that reads as "lift" for the product screenshot floating above
it, without any literal box-shadow doing the work.

## Shapes

| Token | Value | Use |
|---|---|---|
| rounded.xs | 2px | Hairline tags, rare status pills |
| rounded.sm | 4px | Form inputs |
| rounded.md | 8px | Compact card chrome, video frames |
| rounded.lg | 12px | Mid-size cards, secondary surfaces |
| rounded.xl | 16px | Pricing cards, feature cards |
| rounded.xxl | 48px | Stat badge backdrops |
| rounded.pill | 90px | All buttons, without exception |

Product photography plays a smaller role than product-UI screenshots,
which sit atop the pastel-mesh gradient at roughly 4:3 with no shadow —
the gradient supplies the visual lift instead. Real photography, where it
appears (customer-logo strips, case-study cards), sits full-bleed inside
`rounded.xl` containers.

## Components

Definitions live in `design-tokens.yaml → components`. Summary:
- **Buttons** — primary pill (aubergine fill, with a distinct pressed
  state), secondary pill (lavender fill), and outline variants for both
  light and aubergine surfaces. All buttons share the 90px pill shape.
- **Cards** — standard pricing card, the inverted aubergine featured
  pricing tier, a cream feature card, a full aubergine "band" card for
  closing CTAs, and a stat card that renders a single number in massive
  aubergine display type.
- **Inputs** — a simple text-input with hairline border and 4px radius.
- **Navigation** — light top nav with wordmark left, links center, and a
  secondary + primary pill pair on the right.
- **Signature elements** — the pastel-mesh gradient backdrop, the
  floating product-UI mockup, the full-bleed aubergine footer band
  (roughly 480-600px tall on desktop), and the small all-caps eyebrow
  pill used above pricing-tier titles.

## Do's and don'ts

**Do**
- Reserve aubergine for filled CTAs, the featured pricing tier, and the
  closing band — treat it as the brand's one true chromatic color.
- Use the full 90px pill for every button; never a rounded-rectangle
  button.
- Pair display type with negative letter-spacing; the proprietary face
  needs the tracking pull to read as edited rather than loose.
- Compose hero bands as pastel-mesh gradient plus floating product-UI
  mockup — the gradient supplies the depth.
- Use the link-blue for inline links; it is the brand's one intentional
  departure from aubergine.

**Don't**
- Don't add a third accent color — aubergine plus link-blue is the
  complete palette.
- Don't shrink button padding below 14px/28px; the over-padded pill is
  part of the feel.
- Don't set display type at neutral tracking — without negative
  letter-spacing the headlines read loose and unedited.
- Don't nest product-UI screenshots inside bordered cards — they float
  above the gradient, not inside chrome.
- Don't use aubergine as a body-text color; it is a surface/CTA color
  only.
- Don't replace the pill shape with a square button anywhere in the
  system.

## Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Wide | ≥1440px | Full-bleed pastel-mesh hero; pricing 4-up |
| Desktop | 1024-1440px | Default content max-width; pricing 4-up |
| Tablet | 768-1023px | Pricing 2-up; product-UI mockups crop to focal panel |
| Mobile | <768px | Pricing 1-up; hamburger nav; display-xxl drops 64px → 40px |

Pill buttons naturally clear 48×48px touch targets thanks to their
generous padding (WCAG AAA). Display type stair-steps 64 → 50 → 32 → 28 →
24px across breakpoints, pastel-mesh gradients re-tile on mobile so the
wash never disappears, and floating product-UI mockups crop to their most
actionable inner panel on small screens. The top nav collapses to a
hamburger below 768px, inheriting the canvas color.

## Known gaps

- The token values are extracted directly from the source analysis;
  treat them as canonical for this skill.
- Both proprietary type families (Salesforce Avant Garde, Salesforce
  Sans) are not publicly licensed — use the Inter/Lato substitutes noted
  under Typography.
- Careers- or product-specific sub-pages beyond the analyzed home,
  features, pricing, and contact-sales pages were not captured.
