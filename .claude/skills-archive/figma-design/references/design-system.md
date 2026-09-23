# Figma Design System — Full Analysis

Adapted from the Figma marketing-site design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/figma/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

At the chrome level, Figma's marketing pages are a strictly black-and-white
editor frame: the top nav, body copy, footer, and default CTA are all
monochrome. Headlines run oversized in `{typography.display-xl}`, set in
`figmaSans` with aggressive negative tracking; body copy sits at a light
weight around 320–340 of the same variable family; and small all-caps
`figmaMono` labels (`{typography.eyebrow}`, `{typography.caption}`) mark
section taxonomy. Every CTA is a pill (`{rounded.pill}`), and the same
black `{components.button-primary}` paired with the white
`{components.button-secondary}` recurs across the whole site.

What makes the system distinctive happens between those monochrome
bookends: the page keeps dropping into oversized pastel **color-block
sections** — lime, lavender, cream, mint, pink, coral, and a deep navy —
that stretch the full content width with `{rounded.lg}` corners and
`{spacing.xxl}` interior padding. These aren't small accents tucked in a
card; they take over a full viewport's height, like giant sticky notes
placed on a clean desk. That's where the storytelling actually happens.
FigJam leans hardest into the pastel rotation, the homepage cycles through
the whole set, and the pricing page closes with a lime FAQ panel — same
vocabulary, different pacing per route.

The whole thing works because of contrast: the monochrome chrome makes each
color block feel like a deliberate choice rather than decoration, and the
color blocks in turn keep the black-and-white chrome from reading as flat
enterprise SaaS. Density stays generous, display line-heights stay tight,
and nothing ever reaches for a shadow or gradient — the color blocks and
confident typography are doing that job already.

**Key characteristics:**
- Monochrome core: `{colors.primary}` black and `{colors.canvas}` white
  carry every CTA, every body line, every footer link.
- Oversized pastel color-block sections define the narrative rhythm of
  every long-form page.
- Pill is the only button shape (`{rounded.pill}` for text CTAs,
  `{rounded.full}` for icon buttons) — no square buttons anywhere.
- `figmaSans` used at unusually fine weight increments (320, 330, 340, 450,
  480, 540) so the type reads as one voice flexing, not a stepped family.
- Tight negative tracking on display sizes (-1.72px at 86px, -0.96px at
  64px) gives a confident editorial cadence.
- `figmaMono` is reserved for eyebrows and captions — always uppercase,
  positive tracking — never body copy.
- A typical home-page rhythm: white hero → marquee strip → white feature →
  lime block → navy block → coral block → white template grid → footer.

## Colors

### Brand & accent
- **Black** — the system primary: every primary CTA, every headline, every
  body line, the marquee strip, and the inverse-canvas of dark sections.
- **White** — inverse text on black surfaces, and also the foreground of
  the secondary pill button.
- **Magenta promo** — one saturated pink reserved for promotional inline
  CTAs (e.g., a "Save your spot" banner). Used scarcely — this is not a
  section color.

### Surface
- **Canvas** — default page background and the body of every white card.
- **Inverse canvas** — footer, marquee strip, and a subset of story
  sections.
- **Surface soft** — off-white tile background for icon buttons, template
  cards, and feature illustration tiles sitting on the white canvas.
- **Hairline / hairline soft** — subtle dividers on form inputs, pricing
  cards, and table rows.
- **Block lime** — the signature systems / FAQ / contact-form color.
- **Block lilac** — hero block on the design page; also the Release Notes
  promo banner.
- **Block cream** — a soft warm background for the FigJam hero strip and
  template grid.
- **Block mint / pink** — FigJam pastel sections.
- **Block coral** — the "ship products" story block on the homepage.
- **Block navy** — the one dark-indigo story block above the footer.

### Text
- **Ink** — every headline, body, and caption on light surfaces. There's no
  separate mid-gray text role — hierarchy comes from weight, not opacity.
- **Inverse ink** — type on inverse-canvas surfaces.
- **On-inverse soft** — translucent white used on circular icon buttons
  over dark sections.

### Semantic
- **Success green** — comparison-table checkmarks on pricing; a glyph
  fill, not a surface.
- **Overlay scrim** — black at reduced opacity behind modal/video overlays.

## Typography

### Family
- **figmaSans** — Figma's proprietary variable typeface (fallback:
  `figmaSans Fallback, SF Pro Display, system-ui, helvetica`). Its weight
  axis is exercised at unusually fine steps (320, 330, 340, 450, 480, 540,
  700) so the system reads as one voice modulating rather than a stepped
  family.
- **figmaMono** — proprietary monospace (fallback: `figmaMono Fallback, SF
  Mono, menlo`), used exclusively for eyebrows and captions, always
  uppercase with positive tracking.

`kern` is enabled everywhere.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale (display-xl 86px
down to caption 12px). Principles:
- Weight, not size, carries emphasis in body copy — a 20px paragraph at
  330 sits right next to a 20px link at 480, and the eye reads the
  difference without a size change.
- Negative tracking scales with size: display-xl pulls -1.72px, subhead
  only -0.26px, body stays near zero — editorial display type without
  hurting body readability.
- Mono is reserved for taxonomy (eyebrows/captions), never for setting a
  paragraph.
- Line-heights are tight on display (1.00–1.10) and generous on body
  (1.40–1.45) — headlines read as graphics, body reads as text.

### Font substitutes
Without figmaSans/figmaMono, **Inter** (or **Geist**) is a solid sans
substitute, and **JetBrains Mono** (or **Geist Mono**) covers the mono
role. Inter's variable weights approximate figmaSans's fine-grained axis
reasonably well; expect to trim line-heights slightly since Inter's
x-height runs a bit taller.

## Layout

- Base spacing unit: 8px. Full scale in `design-tokens.yaml → spacing`.
- Color-block section interior padding: `spacing.xxl` (48px).
- Pricing card / template tile interior padding: `spacing.lg` (24px).
- Form input padding: 12px vertical, 14px horizontal.
- Button padding: roughly 8px vertical / 24px horizontal for pills — the
  asymmetric `8px 18px 10px` on the secondary button nudges its label
  optically inside the pill.
- `spacing.section` (96px) is the constant vertical gap between major
  content sections, holding across home, pricing, and FigJam.
- Max content width sits around 1280px, with gutters scaling from
  `spacing.xxl` on desktop down to `spacing.lg` on mobile.
- Color-block sections break the column grid entirely — they go full
  content width inside `{rounded.lg}` corners, then place a single
  editorial column of headline + body inside.
- White space exists specifically to make each color block feel
  deliberate: `spacing.section` of canvas separates every two blocks, and
  inside a block the type gets generous side margins so it reads as a
  poster rather than a wall of copy.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 (flat) | No shadow, no border | Color-block sections, inverse-canvas footer, hero |
| 1 (hairline) | 1px `{colors.hairline}` border on canvas | Pricing cards, form inputs, comparison cells |
| 2 (soft elevation) | Subtle drop shadow ~0 4px 16px rgba(0,0,0,0.06) | Floating template tiles, dropdown menus |
| 3 (modal) | Stronger shadow + `{colors.overlay-scrim}` behind | Video/image lightbox overlays |

Figma's system is deliberately shadow-light — color-block sections
substitute for traditional elevation. Where most SaaS sites shadow a white
card to draw the eye, Figma switches the background to a saturated pastel
instead, which makes the rare real shadow (a floating template card over a
cream section) feel like an intentional exception.

Decorative depth otherwise comes from: color-block section transitions as
the primary device; FigJam's slightly off-axis pastel "sticky note"
component thumbnails, which read as collage rather than card-stack; and
embedded product-UI mockups (Design panels, FigJam canvas snippets) shown
as flat compositions with subtle internal shadows that stay inside the
mock.

## Shapes

| Token | Value | Use |
|---|---|---|
| rounded.xs | 2px | Anchor/link decoration corners |
| rounded.sm | 6px | Small chips, sub-nav tabs |
| rounded.md | 8px | Form inputs, list items, image frames |
| rounded.lg | 24px | Pricing cards, color-block sections, large image containers |
| rounded.xl | 32px | Hero feature panels, oversized callouts |
| rounded.pill | 50px | All text CTAs (primary, secondary, tab toggles) |
| rounded.full | 9999px | Circular icon buttons, comparison-checkmark glyphs |

Image frames sit at `rounded.md` (8px) — friendly but still editorial.
Template thumbnails on the home grid use the same radius with
`spacing.md` interior padding around the preview. FigJam's pastel
sticky-note thumbnails keep a smaller `rounded.sm` corner that mimics
actual sticky paper. There are no avatar circles in marketing — Figma's
marketing surfaces avoid personification.

## Components

Definitions live in `design-tokens.yaml → components`. Summary:
- **Buttons** — button-primary (black pill), button-secondary (white pill,
  asymmetric padding), button-tertiary-text (inline link styled as a
  button), button-icon-circular / -inverse (40px circles for light/dark
  surfaces), button-magenta-promo (the one-shot pink promo pill).
- **Pricing tabs** — pricing-tab-default / -selected; selected uses the
  same black fill as button-primary, so "selected" always reads as
  "active," not just "different."
- **Inputs** — text-input / text-input-focused, focus communicated via
  ring rather than fill change.
- **Cards & containers** — pricing-card, pricing-card-feature-row,
  template-card, feature-illustration-tile.
- **Color-block sections (signature)** — color-block-section (lime),
  color-block-section-lilac, color-block-section-navy (the one inverse
  surface above the footer); cream/mint/pink/coral variants follow the
  same shape with their respective `block-*` background.
- **Promo banner** — promo-banner-lilac, carrying a button-magenta-promo
  on its right edge.
- **Navigation** — top-nav (56px, white), marquee-strip (36px, black
  ribbon of scrolling customer logos).
- **Comparison glyph** — comparison-checkmark, green fill on white.
- **Footer** — dense link grid on white canvas.

## Do's and don'ts

**Do**
- Reserve `{colors.primary}` for genuine primary CTAs and selected states
  (like `pricing-tab-selected`) — never as decoration.
- Choose exactly one `block-*` color per story section and let it span
  full content width with `{rounded.lg}` corners and `{spacing.xxl}`
  padding.
- Stay inside the `figmaSans` weight set (320, 330, 340, 480, 540, 700) to
  express hierarchy.
- Keep `figmaMono` limited to eyebrows and captions, always uppercase with
  the documented positive tracking.
- Make every CTA a pill and every icon button a circle.
- Let the page return to white canvas between any two color blocks so each
  one reads as deliberate.
- Pair button-primary with button-secondary whenever a section needs both
  a primary and a secondary/sales action.

**Don't**
- Don't introduce mid-gray text — hierarchy comes from `figmaSans` weight,
  not opacity.
- Don't add drop shadows to color-block sections; the color itself is the
  depth device.
- Don't add accent colors outside the documented `block-*` palette plus
  magenta.
- Don't show more than one color block in a single viewport — Figma always
  separates them with white canvas.
- Don't square off CTAs — square buttons read as a different brand.
- Don't set body copy in `figmaMono` — it's a taxonomy tool only.
- Don't swap the black `pricing-tab-selected` fill for a colored tab; the
  pattern is "selected = primary surface."

## Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| 4k | 1920px | Max content width holds at 1280px; gutters expand |
| Desktop-XL | 1440px | Default desktop layout |
| Desktop | 1400px | Comparison-table columns normalize |
| Desktop-S | 1280px | Pricing 4-up tier grid maintained |
| Tablet | 960px | Pricing collapses 4-up → 2-up; nav becomes hamburger |
| Mobile-L | 768px | Color-block sections go full-bleed (corners drop) |
| Mobile | 560px | Display-xl shrinks from 86px to ~48px; pills go full-width |
| Mobile-XS | 559px | Two-column footer collapses to one column |

Touch targets: pill buttons hold a minimum 44px tap height at every
viewport; circular icon buttons are 40px on desktop and grow to 44px on
touch; the contact-form input's minimum tap target is 48px. Nav collapses
to a hamburger overlay below 960px while the two right-anchored pills stay
visible above 560px; the pricing tier grid steps 4-up → 2-up → 1-up; the
comparison matrix folds into per-tier accordions below 960px; product
mockups inside color blocks scale proportionally and never crop; FigJam's
sticky-note thumbnails keep their slight off-axis rotation at every size,
since the rotation is a brand signal, not a desktop-only flourish.

## Known gaps

- The exact pastel hex values of the `block-*` colors were derived from
  screenshot pixels rather than named CSS tokens — treat them as faithful
  approximations, not exact brand specs.
- Dark mode isn't documented; the marketing site doesn't ship one — the
  closest analog is the navy color-block and the inverse-canvas footer.
- Form-field error/validation styling isn't visible on the inspected
  contact page; inputs use hairline borders and `rounded.md` corners, but
  error treatment isn't documented.
- The animated marquee-strip and color-block reveal animations aren't
  documented, consistent with the no-interaction-state policy.
