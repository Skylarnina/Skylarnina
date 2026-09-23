# HashiCorp Design System — Full Analysis

Adapted from the HashiCorp marketing-site design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/hashicorp/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

HashiCorp's marketing pages run on a near-black ground that manages to
serve a multi-product portfolio without ever feeling generic. The dominant
surface is `{colors.canvas}` (pure black), layered with `{colors.surface-1}`
charcoal cards and 1px translucent gray hairlines. The chrome itself is
monochrome — white pill-rounded buttons, white type, gray secondary text —
but the system's real identity comes from a **palette of per-product
accent colors**, each one signaling which HashiCorp-style tool a section
belongs to: Terraform purple, Vault yellow, Consul red, Waypoint cyan,
Vagrant blue, Nomad green, Boundary coral.

Display type runs **hashicorpSans** at weight 600/700 with tight
line-heights (1.17–1.21); body type sits in the same family at weight 500
with deliberately relaxed line-heights (1.50–1.71) — the contrast between
the two feels editorial rather than templated-enterprise. CTAs use a small
`{rounded.md}` (8px) corner rather than a pill, which keeps the whole
system reading as developer-facing instead of consumer-y.

The defining device is the **product-card** family — each product gets its
own colored card variant on the home and infrastructure pages, lifting
Terraform into violet, Vault into yellow, Waypoint into cyan. These aren't
decorative gradients; they're identity surfaces. A reader scanning the page
can tell which product a section covers from the corner of their eye,
without reading a word.

**Key characteristics:**
- Black-canvas marketing system: `{colors.canvas}` is the surface for hero,
  body, pricing, comparison tables, and footer alike.
- **Per-product color identity**: Terraform, Vault, Waypoint, Vagrant,
  Consul, Nomad, and Boundary each get their own button + card variant.
- Display headlines run at 600/700 with tight 1.17–1.21 line-height; body
  runs the same family at 500 with relaxed 1.50–1.71 line-height — the gap
  between the two IS the brand's voice.
- CTA shape is `{rounded.md}` (8px) — not a pill — reading as
  developer-tool rather than consumer-app.
- Charcoal surface lift (canvas → surface-1 → surface-2) stands in for
  shadow-driven elevation.
- 1px translucent gray hairlines define cards and dividers — borders are
  felt more than seen.
- An uppercase eyebrow (12–13px, 600 weight, 0.6px tracking) marks every
  meaningful section as a category label.

## Colors

### Brand & accent
- **Black** — the system's primary surface: canvas, footer, comparison
  tables, and hero are all black.
- **White** — inverse text on black; the canvas of `button-primary`.
- **Accent blue** — used for hyperlinks across the marketing surface.
- **Visited purple** — the visited-link state.

### Surface
- **Canvas** — default page background.
- **Surface 1** — charcoal, one step above canvas: feature cards, pricing
  cards, resource tiles.
- **Surface 2** — two steps above: featured pricing card, secondary
  buttons, hovered product chrome.
- **Surface 3** — three steps above: small chips, badges, sub-nav
  backgrounds.
- **Hairline / hairline soft** — 1px dividers on cards and comparison-table
  rows.
- **Inverse canvas** — pure white, used only as the surface of
  `button-primary`.

### Text
- **Ink** — every headline and emphasized body line, pure white.
- **Ink muted** — secondary type used for meta info and footer columns.
- **Ink subtle** — tertiary type used for form helper text, timestamps, and
  footnotes.

### Per-product identity (signature)
HashiCorp's marketing doesn't hold together with a single accent color —
it holds together with a system of product-specific accents, each marking
which tool a section represents:
- **Terraform purple** — Terraform sections, Terraform CTAs, the violet 3D
  cube on the hero. A brighter variant handles link emphasis on Terraform
  pages.
- **Vault yellow** — Vault sections and CTAs.
- **Consul red** — Consul sections.
- **Waypoint cyan** — Waypoint sections, with a deeper variant for
  hover/active.
- **Vagrant blue** — Vagrant sections.
- **Nomad green** — Nomad sections.
- **Boundary coral** — Boundary sections.

### Semantic
- **Success / warning / error** — the standard status trio (success also
  doubles as Nomad green; warning as Vault yellow; error as Consul red).
- **Amber 100 / 200** — soft and saturated amber, used sparingly for
  caution badges.
- **Blue 7** — a deep navy used inside "unified core" gradients.

## Typography

### Family
- **hashicorpSans** — HashiCorp's proprietary marketing typeface: geometric,
  clean, slightly humanist. Fallback: system sans stack. The same family
  carries display, body, button, and caption — there's no separate
  display/body pairing. Hierarchy comes from weight (500 body / 600
  emphasis / 700 display) and from a deliberate line-height contrast
  (tight on display, relaxed on body).

### Hierarchy
See `design-tokens.yaml → typography` for the full scale (display-xl 80px
down to eyebrow 12px). Principles:
- Tight on display, relaxed on body: display sits at line-height
  1.17–1.21; body lifts to 1.50–1.71 — the size/line-height contrast
  carries hierarchy on its own.
- Weight hierarchy stays small: 500 body / 600 emphasis / 700 display —
  no light/black extremes, which keeps the system reading as engineered.
- Eyebrow type (uppercase, positive-tracked, 12px) sits above every
  meaningful section header.
- No mono anywhere on marketing, despite this being a developer-tools
  brand — code voice is reserved for in-product surfaces only.

### Font substitutes
Without hashicorpSans, reasonable open substitutes include **Inter**
(closest geometric character set), **Geist Sans**, or **IBM Plex Sans**.
Inter at weights 500/600/700 closely approximates hashicorpSans's
proportions; expect to trim line-heights slightly to match.

## Layout

- Base spacing unit: 8px, with primary increments of 4/8/12/16/24/32/48.
  Full scale in `design-tokens.yaml → spacing`.
- Card interior padding: 24px on product cards, 32px on pricing cards, 48px
  on CTA banners.
- Button padding: 10px vertical, 18px horizontal on the primary button.
- `spacing.section` (96px) is the constant vertical gap between major
  sections.
- Max content width sits around 1280px, with gutters scaling from
  `spacing.xxl` on desktop down to `spacing.lg` on mobile.
- Product-card grids run 3-up desktop, 2-up tablet, 1-up mobile; the
  pricing tier grid stays 3-up across desktop; the resource/PDF directory
  uses a dense 4-up thumbnail grid.
- The dark canvas functions as the whitespace: sections separate through
  surface lift (canvas → surface-1) rather than gaps in white. Within a
  section, generous 32px gaps separate cards and 24px separates rows.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 (flat) | No shadow, no border | Canvas-mounted display type, hero, footer |
| 1 (charcoal lift) | `{colors.surface-1}` + 1px translucent gray border | Default cards, resource tiles, pricing cards |
| 2 (surface-2 lift) | `{colors.surface-2}` + 1px `{colors.hairline}` border | Featured pricing card, hovered cards, sub-nav |
| 3 (product chromatic) | Per-product accent background | Product showcase cards |

The product-chromatic level isn't a "modal lift" in the usual sense — it's
an identity device. A Terraform card sits at the same z-plane as a generic
feature card; the difference is meaning, not depth.

Decorative depth otherwise comes from isometric, product-tinted 3D
illustrations (purple cubes for Terraform, translucent yellow safes for
Vault) sitting in the hero's right column, and from the 1px translucent
gray hairlines that define nearly every edge. There are no drop shadows on
dark — cards lift purely through surface change.

## Shapes

| Token | Value | Use |
|---|---|---|
| rounded.xs | 4px | Small chips / badges |
| rounded.sm | 6px | Inline tag |
| rounded.md | 8px | All CTA buttons, form inputs, list items |
| rounded.lg | 12px | Feature cards, product cards, pricing cards |
| rounded.xl | 16px | Large illustrative tiles |
| rounded.xxl | 24px | CTA banner panels |
| rounded.pill | 9999px | Eyebrow-style product pills (small chips) |
| rounded.full | 9999px | Avatar circles (rare on marketing) |

Product 3D illustrations render full-bleed within their container with no
rounded inner mask. Logo chips in the customer marquee sit on `rounded.sm`
tiles with a 1px hairline; resource thumbnails use `rounded.lg`.

## Components

Definitions live in `design-tokens.yaml → components`. Summary:
- **Buttons** — button-primary (white rounded-rect, 8px), button-secondary
  (charcoal), button-tertiary (bare ghost), and per-product CTAs
  (button-product-terraform/vault/waypoint, following the same pattern for
  Vagrant/Nomad/Consul/Boundary with their own tokens).
- **Cards & containers** — product-card (neutral charcoal), per-product
  variants (product-card-terraform/vault/waypoint and siblings),
  feature-card, pricing-card / pricing-card-featured, resource-card.
- **Inputs** — text-input / text-input-focused, focus signaled by a 1px
  accent-blue outline.
- **Pills & chips** — product-pill, the small product-name chip above
  hero headlines and on resource cards.
- **Comparison table** — comparison-row, using `body-sm` and a
  hairline-soft row separator.
- **CTA banner** — cta-banner, a large 24px-rounded panel closing
  long-form pages.
- **Navigation & footer** — top-nav (64px, logomark left, nav center,
  primary + secondary CTA pair right), footer (dense caption-sized link
  grid).

## Do's and don'ts

**Do**
- Treat `{colors.canvas}` (black) and `{colors.surface-1}` (charcoal) as
  the system's two anchor surfaces.
- When a section covers a specific product, use that product's accent
  token consistently — for the section pill, the CTA, and (where
  appropriate) the showcase card background.
- Keep CTA corners at `{rounded.md}` (8px); the brand reads as engineered,
  not consumer.
- Pair tight display line-heights (1.17–1.21) with relaxed body
  line-heights (1.50–1.71).
- Put the eyebrow type above every meaningful section.
- Use surface lift (canvas → surface-1 → surface-2) to express hierarchy
  on dark.
- Reserve product-chromatic cards for product identity; keep generic
  feature cards on `{colors.surface-1}`.

**Don't**
- Don't ship a light-mode marketing page — the brand IS dark.
- Don't introduce mid-tone gray text outside the documented ink/ink-muted/
  ink-subtle set.
- Don't square off CTA corners — 8px, not 0px.
- Don't use a product's accent color for a CTA on a page that isn't about
  that product — that's a brand violation, not a stylistic choice.
- Don't combine multiple product accents in the same viewport — mixing
  breaks the "this section is about THIS tool" signal.
- Don't add drop shadows on dark; surface lift carries elevation instead.
- Don't split display and body into two different type families — one
  family across the full hierarchy is what holds the brand together.

## Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Desktop-XL | 1440px | Default desktop layout |
| Desktop | 1280px | Pricing 3-up grid maintained |
| Tablet | 1024px | Product card grid 3-up → 2-up |
| Mobile-Lg | 768px | Pricing comparison becomes per-tier accordion; nav becomes hamburger |
| Mobile | 480px | Single-column everything; display-xl scales 80px → ~36px |

Touch targets: CTA buttons hold at least 40px tap height across viewports;
product pills grow from 24px to 28px on touch; form inputs hold at least
44px on touch. The nav collapses to a hamburger overlay below 768px while
the primary CTA stays visible; the product-card grid steps 3-up → 2-up →
1-up; the pricing comparison table folds into per-tier accordions below
768px; display type scales from 80px down toward 40px on mobile while
preserving the negative-tracking percentage. 3D product illustrations keep
their aspect ratio and shrink rather than reflow below 768px; the customer
logo marquee may wrap to a second row at narrow widths.

## Known gaps

- The per-product color hex values come directly from the site's
  `--mds-color-*` CSS variables — treat them as HashiCorp's canonical
  brand spec.
- Shadow tokens aren't extensively documented because the dark surface
  system relies on surface lift rather than shadow elevation.
- Form-field error and validation styling isn't visible on the inspected
  pages.
- Dark mode is the only marketing mode — light-mode adaptation isn't
  documented.
- Product-card variants for Consul, Nomad, Vagrant, and Boundary follow
  the documented Terraform/Vault/Waypoint pattern but are referenced only
  in prose in the source analysis; add formal `product-card-*` entries for
  them if a build needs to reference them directly.
