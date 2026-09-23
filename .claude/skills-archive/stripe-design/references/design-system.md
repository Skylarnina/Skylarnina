# Stripe Design System — Full Analysis

Adapted from the Stripe marketing-site design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/stripe/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Stripe's design language opens with the gradient mesh: a wide horizontal band
of pastel cream, sherbet orange, lavender, electric indigo, and ruby pink that
occupies the upper third of nearly every marketing page — the brand's
instantly-recognizable atmospheric backdrop. Type and product-UI mockups float
above it on `colors.canvas` (white). The lower part of the page returns to
white, with feature explanations on `colors.canvas-soft` (a barely-tinted
cool off-white) and dashboard mockups composited as faux IDE/console panels
in deep navy.

Color plays two roles here. **Indigo** (`colors.primary`, `#533afd`) is the
signature CTA color, used sparingly — one filled pill per band. **Deep navy**
(`colors.ink`, `#0d253d`) is the universal body-text color and also the fill
of dashboard mockups and the featured pricing tier. Ruby and magenta show up
inside the gradient mesh and as accent dots in product mockups, but never as
button fills.

Typography runs on **Sohne** at weight 300 with negative letter-spacing — the
brand's editorial-density display signature. Display sizes (32–56px) carry
-0.64px to -1.4px tracking; body sizes sit at 0; any cell holding money or a
numeric count switches on the OpenType `tnum` feature plus a slight tightening
tracking. The `ss01` stylistic set is applied everywhere.

**Key characteristics:**
- A gradient-mesh backdrop on every marketing hero — cream, orange, lavender,
  indigo, and ruby washed horizontally across the top third of the page.
- Single-indigo CTA hierarchy — the filled indigo pill is the only filled
  button on marketing surfaces.
- Sohne at thin weight 300 with negative tracking scaling from -1.4px down to
  -0.2px depending on size.
- Tabular figures (`tnum`) on any cell containing money or numerics — a quiet
  financial-data signal.
- A dark-app dashboard track: deep-navy product-UI mockups composited above
  the white canvas, often rendering code or dashboard tables inside.
- Pill-shaped buttons at a tight 8px/16px padding — short, decisive,
  transactional.
- Cream-band feature cards introduce a warm interlude between the blue/white
  sections without breaking the brand's chromatic logic.

## Colors

> Source pages: home (`/`), `/payments`, `/pricing`,
> `dashboard.stripe.com/register/payments`.

### Brand & accent
- **Indigo** — the signature CTA color: filled pill, link emphasis, gradient
  anchor.
- **Indigo deep** — a deeper indigo used in gradient mid-stops and the
  press-state's warmer alternative.
- **Indigo press** — the pressed-state lift of the primary.
- **Indigo soft** — a lighter indigo used in product-UI accents and chart
  highlights.
- **Indigo subdued** — a pale indigo fill for soft tag backgrounds.
- **Brand dark 900** — the deep navy used on the featured pricing tier and
  dashboard chrome.
- **Ruby / magenta / lemon** — gradient and chart accents; never used as
  buttons.

### Surface
- **Canvas** — the default page background, white.
- **Canvas soft** — a cool-tinted off-white for feature bands beneath the
  gradient hero.
- **Canvas cream** — a warm cream used for the feature-band chromatic
  interlude.
- **Hairline / hairline input** — 1px border tiers on cards, tables, and
  form inputs.

### Text
- **Ink** — the default body-text color, deep navy, never pure black.
- **Ink secondary / ink mute / ink mute 2** — descending secondary and
  helper-text tiers.
- **On primary** — white text used on indigo/navy surfaces.

### Semantic
Stripe's marketing system doesn't maintain a separate semantic palette — error
and success states live specifically inside dashboard product UI, not on the
marketing surface.

## Typography

### Families
- **Sohne** (proprietary, Klim Type Foundry) at weights 300 and 400, with
  `font-feature-settings: "ss01"` enabled globally for the display/UI tier.
- Fallback chain: **SF Pro Display** at thin weights, then system-ui.

Substitute with **Inter** at weight 300, `letter-spacing: -1.4px` on display
sizes, and `font-feature-settings: "ss01"` — Inter is the closest open-source
analogue.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale (display-xxl 56px
down to micro-cap 10px). Principles:
- Thin weight (300) is the brand — bumping display type to 400+ removes the
  editorial air.
- Negative tracking scales from -1.4px at 56px down to -0.2px at 20px.
- Money and numeric counts always use `tnum` plus a tightening tracking.
- `ss01` is applied on the body element so the stylistic-set substitution
  covers every text role.

## Layout

- Base spacing unit: 8px, with 2/4/12px sub-tokens for fine work.
- Section padding runs 64–96px on marketing surfaces, 32–48px on
  dashboard/product surfaces.
- Card interior padding: 32px on feature cards, 24px on dashboard mockups.
- Marketing pages center in a ~1200px container with the gradient mesh
  extending edge-to-edge above it.
- Pricing collapses 4-up → 2-up → 1-up at 1024/768px.
- The gradient mesh occupies the upper third of the page; the white canvas
  below is generously padded, with section gaps around 96px tightening to
  32px on dashboard/pricing pages where users compare and act.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 | Flat | Default surface |
| 1 | `rgba(0,55,112,0.08) 0 1px 3px` | Card lift on white |
| 2 | `rgba(0,55,112,0.08) 0 8px 24px, rgba(0,55,112,0.04) 0 2px 6px` | Floating panels, dashboard mockup chrome |
| 3 | Gradient-mesh backdrop | The brand's primary depth medium — atmospheric color, not a literal shadow |

### Decorative depth
The gradient mesh *is* the depth system, implemented as a layered SVG or large
background image rather than a flat CSS gradient (the real mesh has organic
blob shapes). Literal box-shadows are reserved for product-UI mockups and
stay subtle.

## Shapes

| Token | Value | Use |
|---|---|---|
| rounded.xs | 4px | Hairline tags, table chrome |
| rounded.sm | 6px | Form inputs |
| rounded.md | 8px | Compact cards, alerts |
| rounded.lg | 12px | Pricing cards, feature cards |
| rounded.xl | 16px | Dashboard mockup chrome |
| rounded.pill | 9999px | All buttons, tag pills |

Product-UI mockups outnumber photography. Dashboard composites render as faux
IDE/terminal/dashboard chrome inside 12px containers with a subtle shadow.
Real photography, where it appears (customer logo strips, rare case studies),
sits inset at 4:3 with no shadow.

## Components

Definitions live in `design-tokens.yaml → components`. Summary:
- **Buttons** — `button-primary-pill` (the dominant CTA, with a pressed
  variant), `button-secondary` (outline), `button-on-dark` (used on dashboard
  surfaces).
- **Cards** — `card-feature-light`, `card-pricing` and its inverted
  `card-pricing-featured` (deep navy), `card-cream-band` (the warm interlude),
  `card-dashboard-mockup` (tabular money type, nested mini-mockups).
- **Inputs** — `text-input` / `text-input-focused`, indigo focus border.
- **Navigation** — `nav-bar-on-mesh`, floating over the gradient hero.
- **Tags** — `pill-tag-soft`, subdued indigo.
- **Footer** — `footer-light`, 4–6 link columns plus a legal row.

## Do's and don'ts

**Do**
- Reserve indigo for filled CTAs and inline link emphasis — one filled button
  per band.
- Apply the gradient mesh to every marketing hero.
- Render display tiers at weight 300 with negative letter-spacing.
- Use `tnum` on every money/numeric cell, and `ss01` globally.
- Pair every feature explanation with a composited product-UI mockup.

**Don't**
- Don't bump display weight above 300.
- Don't add accent colors outside the documented gradient stops.
- Don't use indigo as body text.
- Don't shrink button padding below 8px/16px.
- Don't render money cells without `tnum`.
- Don't swap the pill shape for rounded rectangles on buttons.

## Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Wide | ≥1440px | Full gradient mesh edge-to-edge; dashboard composite at full scale |
| Desktop | 1024–1440px | Default max-width; pricing 4-up |
| Tablet | 768–1023px | Pricing 2-up; dashboard composite simplifies to 2 panels |
| Mobile | <768px | Pricing 1-up; hamburger nav; display drops 56 → 36px |

Pill buttons hit ≥40×40px on mobile, sizing up to 44×44px for WCAG AAA; form
fields stay at a 40px minimum. Display tiers stair-step 56 → 48 → 32 → 26 →
22px through the breakpoints, the gradient mesh re-tiles to preserve the wash
on mobile, and dashboard composites simplify to a single panel below desktop.
Product-UI composites use `srcset` with mobile crops focused on the most
actionable inner panel.

## Known gaps

- The gradient mesh's organic blob shapes aren't reproducible as a flat CSS
  gradient — treat the documented stops as a starting point for an SVG/image
  asset, not a literal `linear-gradient()`.
- Sohne is proprietary; the Inter substitute approximates but doesn't exactly
  match its thin-weight metrics.
- Dashboard/product-UI error and validation states live in-product and aren't
  captured on the marketing surface.
