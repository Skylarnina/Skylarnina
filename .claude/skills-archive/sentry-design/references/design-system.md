# Sentry Design System — Full Analysis

Adapted from the developer-observability design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/sentry/DESIGN.md`, MIT License; the source file frames this as
an "inspired interpretation" of an observability brand). Token names below
refer to `references/design-tokens.yaml` in this skill.

## Overview

The system reads like a debugging console wearing a leather jacket. Home
and product pages sit on a near-black violet midnight
(`{colors.surface-canvas-dark}` / `{colors.surface-night}`), scattered with
starfield texture and floating sticker-style mascots — astronauts,
monsters, traffic cones — that undercut the seriousness of an observability
product. Headlines run in a chunky proprietary display sans where the most
important keyword in a headline is wrapped in a lime-green highlight chip
(`{colors.accent-lime}`), as if the copy had been syntax-highlighted by a
developer marking up their own console output.

The palette stays deliberately narrow: deep midnight as the dominant
canvas, electric lime as the primary attention-getter, hot pink
(`{colors.accent-pink}`) as secondary punctuation, and a mid-violet
(`{colors.accent-violet-mid}`) for tag chips and hairline strokes. White
appears in two roles — text on dark, and the canvas for pricing/contact/
content-heavy pages where visitors need to scan dense tables. The single
primary CTA visually flips polarity depending on context: filled
black-violet with white type on light surfaces, or filled white with dark
type on dark surfaces — but it always reads as the strongest affordance on
the page regardless of which way it's flipped.

Typography splits across three families: a custom display sans for hero and
section openers (chunky, near-condensed, slightly playful), Rubik for every
UI text role (body, captions, eyebrow caps, button labels), and Monaco for
code. Buttons and eyebrows run almost universally in uppercase with a 0.2px
tracking lift, giving the UI the snap of console output.

**Key characteristics:**
- Two-polarity canvas system: deep violet midnight for marketing hero and
  product-feature pages, white for pricing/contact/dense-reference content
  — the system never blurs the two.
- The lime keyword highlight is treated as a typographic device, not a
  color swatch — it wraps single words inside display headlines like a
  syntax highlight.
- A sticker-illustration system of floating mascots with hand-drawn
  outlines appears at section junctions, never inside cards.
- Uppercase eyebrow and button caps with a consistent 0.2px tracking lift
  give the brand its "developer console" cadence.
- Single-primary-CTA hierarchy: one filled button per page, polarity-
  flipped to match canvas; outlined and ghost variants are downgraded.
- Card surfaces follow the canvas — dark sections nest dark cards, light
  sections nest white cards — chrome stays consistent, only polarity
  flips.
- Pricing uses cream-white tiers with one dark-inverted "featured" tier,
  avoiding the typical accent-bordered featured-card pattern.

## Colors

### Brand & accent
- **Midnight Violet** — the primary action color and deepest surface tone;
  filled primary buttons on light surfaces, code-block backgrounds, and the
  strongest dark cards.
- **Ink Violet** — slightly lifted from primary; the marketing hero canvas
  and default body-text color on light surfaces, doing double duty as
  background and ink.
- **Electric Lime** — the signature highlight; wraps individual headline
  keywords in a highlight chip and forms the squiggly footer divider
  stroke. Never a button background.
- **Hot Pink** — secondary punctuation for sticker outlines, chart points,
  and supporting accents — never buttons, never body-size type.
- **Violet Link** — inline link color when emphasis is needed beyond
  underline.
- **Deep Violet** — the select-dropdown fill on contact forms and the fill
  for spotlight cards inside dark sections.
- **Mid Violet** — tag-chip fill and faint accent on dark surfaces.

### Surface
- **Dark Canvas** — hero, product, and feature-page background, the
  deepest atmospheric weight.
- **Night** — cards on dark canvas, code blocks, and the "featured" pricing
  tier.
- **Light Canvas** — pricing, contact, and dense-reference page background.
- **Surface Press Light / Press Stronger** — the pressed/active fill of
  inverted buttons on dark surfaces.
- **Hairline Violet** — 1px borders on dark cards.
- **Hairline Cool** — 1px borders on text inputs and form fields.
- **Hairline Cloud** — pricing-table dividers and pricing-card borders on
  light canvas.

### Text
- **On Primary** — white text on dark canvas, all CTA labels on filled
  dark buttons.
- **Ink** — body text on light canvas, sharing its hex with the dark
  canvas, repurposed here as type.
- **Ink Press** — the pressed/active state of inverted buttons.
- **On Dark Muted / On Dark Faint** — secondary text/captions on dark
  canvas, and translucent surface-on-dark for ghost-button fills and
  dimmed nav items.

### Semantic
- **Focus Ring** — translucent blue, the only blue in the system, reserved
  for keyboard focus on form fields.

## Typography

### Families
The display tier is a proprietary geometric sans with chunky, near-
condensed proportions and a slightly subversive personality. When
unavailable, fall back to Rubik at heavier weights. The UI tier is
**Rubik** — open-source, with system fallbacks — handling every body,
caption, button, and eyebrow role. The code tier is **Monaco** with Menlo
and Ubuntu Mono fallbacks.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale (display-hero 88px
down to code-strong 16px). Principles:
- Two leading worlds: marketing copy runs `lineHeight: 2.0` on body-lg —
  extremely airy — while functional UI copy runs `lineHeight: 1.5` on
  body-md, denser and closer to console output. The distinction is
  deliberate: marketing reads like prose, product reads like a log.
- All button labels and eyebrows are uppercase with 0.2px tracking — the
  brand's typographic signature, a console-prompt cadence applied to UI
  affordances.
- The hero display is structured so a single keyword can sit inside a lime
  highlight chip without disrupting the reading order — treat the chip as
  a glyph-level decoration, not a separate component.

### Note on font substitutes
Rubik is open-source (Google Fonts) and safe to use directly for everything
except the hero display. For the proprietary display sans, **Space
Grotesk** (heavier weights), **Archivo** (semi-condensed weights), or
**Hubot Sans** (optical-size axis at heavier ends) all carry a similar
chunky, near-condensed silhouette. Reduce line-height by about 0.05 when
substituting, since the proprietary face has tighter leading at large
sizes.

## Layout

- Base spacing unit: 8px; full scale in `design-tokens.yaml → spacing`.
- Section padding: 96px between major bands on desktop, collapsing to
  32-48px on mobile.
- Card interior padding: 32px on pricing/large feature cards, 16px on
  compact tag/badge groups.
- Form field padding: 8px vertical, 12px horizontal.
- Marketing pages use a wide centered container (~1152px max width) with
  generous outer gutters; pricing runs a 4-tier row at desktop, 2-up at mid
  widths, 1-up on mobile; the contact form uses a 2-column field layout
  inside a single light-canvas panel.
- On dark surfaces, section spacing stretches generously so floating
  mascots and starfield textures have room to breathe. On light surfaces
  (pricing, contact) whitespace tightens because visitors are scanning and
  comparing rather than reading. Hero/feature surfaces are spacious;
  transactional surfaces are dense.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 | flat on canvas, no shadow | default surface, dark or light |
| 1 | soft shadow (~8% opacity) | inverted buttons on dark canvas |
| 2 | layered shadow stack | floating cards on light canvas, modals |
| 3 | dark canvas-colored glow | halo around the primary CTA on dark hero — the canvas color itself becomes the shadow, vignetting the button |
| 4 | deeper shadow (~18% opacity) | pressed inverted button on dark canvas |

Depth doesn't come primarily from drop shadows — it comes from the
starfield texture on the hero canvas (subtle white-on-violet pinpricks at
low opacity), the floating sticker mascots (hand-rendered outlines with
saturated fills, layered above the canvas with no shadow), and the lime
squiggly divider above the footer. These illustrative elements do the work
that shadow stacks do in flatter systems — telling the eye where one
section ends and the next begins.

## Shapes

| Token | Value | Use |
|---|---|---|
| rounded.xs | 4px | badges, status pills, lime keyword highlight chips |
| rounded.sm | 6px | text inputs, search boxes |
| rounded.md | 8px | primary/inverted buttons, code blocks, select dropdowns |
| rounded.lg | 10px | generic divs, container blocks |
| rounded.xl | 12px | pricing cards, feature cards, navigation pill chrome |
| rounded.xxl | 18px | image containers, large hero illustrations |
| rounded.full | 9999px | avatars, circular icon buttons |

The system doesn't use traditional photography — it uses illustrated
stickers and product UI screenshots in roughly equivalent geometric roles.
Product UI mocks sit inside `rounded.xxl` (18px) containers, often tilted
slightly off-axis, with no border. Sticker mascots have no container at
all — they're layered directly on canvas, often overlapping section
boundaries. Customer-logo strips render as simple greyscale wordmarks, not
photos.

## Components

Definitions live in `design-tokens.yaml → components`. Summary (only
Default and Pressed/Active states are documented — no hover states):
- **Buttons** — button-primary (dominant CTA on light), button-inverted
  (dominant CTA on dark), button-ghost-on-dark (secondary, translucent
  fill), button-violet-token (pill tag/category button), and
  button-disabled.
- **Cards** — card-pricing / card-pricing-featured (dark inversion for the
  featured tier), card-feature-dark, card-spotlight-violet (deep-violet
  feature highlight), and a code-block.
- **Inputs** — text-input with a focus state that adds an inward inset
  shadow, and select-violet, a deliberately branded dropdown rather than a
  plain field.
- **Navigation** — nav-bar-light (standard top nav) and a dark-canvas
  variant with polarity-flipped buttons; mobile collapses to a hamburger
  accordion below 768px.
- **Pills & signature components** — pill-neutral-dark, chip-lime-keyword,
  a sticker mascot layer, a lime squiggly footer divider, a starfield hero
  texture, a window-chrome UI mock, link-on-dark/link-on-light, and a
  multi-column light-canvas footer.

## Do's and don'ts

**Do**
- Reserve lime for keyword-highlight chips inside display headlines and
  the footer squiggle divider — never as a button background or body text.
- Pair every primary button with uppercase Rubik at 0.2px tracking.
- Treat the dark and light canvases as two complete worlds — one owns
  marketing/feature pages, the other owns transactional pages, no
  half-measures.
- Let sticker mascots overlap, tilt, and float across section boundaries;
  constraining them inside cards drains their personality.
- Use the dark-inverted featured pricing tier instead of an accent-
  bordered light tier.
- Default body line-height to 1.5 on functional UI surfaces and 2.0 on
  marketing surfaces.

**Don't**
- Don't introduce additional accent colors beyond lime and pink — adding
  teal, orange, or yellow dilutes the violet-and-lime signature.
- Don't apply drop shadows to cards on dark canvas — depth comes from
  texture and illustration, not shadows that would muddy the violet.
- Don't use the 88px hero display size for anything except the marketing
  hero — sub-pages cap at the 60px display-large size.
- Don't put body text in lime — it's a chip color, not a type color.
- Don't soften the primary button to a lighter brand-violet — the
  near-black reads as the most authoritative action on either polarity.
- Don't put illustrated mascots inside cards or constrained containers.

## Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Wide | ≥1440px | full 4-tier pricing row, hero illustration sits beside headline at full scale |
| Desktop | 1152-1440px | default content max-width 1152px, all 4-tier patterns hold |
| Laptop | 992-1151px | pricing collapses to 2-up rows, nav stays horizontal |
| Tablet | 768-991px | 2-column feature grids collapse to 1-up; nav compresses |
| Mobile Large | 640-767px | hamburger nav appears; hero display drops from 88px to ~56px |
| Mobile | 576-639px | single-column everything; section padding collapses from 96px to 32-48px |
| Small Mobile | 1-575px | sticker mascots shrink or hide to preserve content priority |

Touch targets: primary buttons hit a minimum 44×44px on mobile (WCAG AAA).
Pill tags and badges stay above 32×32px even at small mobile breakpoints.
Form fields stay at 44px minimum height.

Collapsing strategy: the hero display drops 88px → 60px → 48px across the
breakpoint stair, with the lime keyword chip preserving padding and corner
radius at every step. Pricing tiers stair-step 4-up → 2-up → 1-up, and the
featured dark tier never loses its inversion. Sticker mascots progressively
de-emphasize — overlapping at desktop, inline at tablet, hidden at small
mobile. Top nav collapses to hamburger below 768px, inheriting the page's
canvas polarity. Code blocks preserve 16px Monaco at every breakpoint and
switch to horizontal scroll rather than wrapping.

Image behavior: product UI mocks scale proportionally, anchoring to one
edge with horizontal overflow on small mobile rather than shrinking to
illegibility. Sticker mascots scale 50-70% at mobile breakpoints. The lime
footer squiggle scales its SVG to container width while keeping stroke
width visually consistent.
