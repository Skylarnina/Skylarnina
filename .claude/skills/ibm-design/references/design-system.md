# IBM Design System — Full Analysis

Adapted from the IBM marketing-site design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/ibm/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

IBM's marketing system is a faithful application of **Carbon Design
System**, IBM's own open-source enterprise design system. The dominant
surface is `{colors.canvas}` pure white, with `{colors.surface-1}` light
gray providing elevation, charcoal `{colors.ink}` (#161616) carrying text,
and IBM Blue `{colors.primary}` (#0f62fe) as the single brand accent.

The defining choice is **flat geometry**: every CTA, every card, every
input, every container uses square corners (`{rounded.none}` 0px) with
thin 1px borders. There are no rounded pills, no soft shadows, no
atmospheric gradients — the system is engineered, not stylized.

**IBM Plex Sans** carries the entire type hierarchy. Display sizes
(76/60/42px) run at weight **300** — IBM's signature light-display
treatment, which makes even a 76px headline feel calmer than a competing
brand's bold 700-weight display. Body type sits at weight 400 with a
Carbon precision detail of `letter-spacing: 0.16px` and a 1.50 line-height.
The voice reads as careful, technical, and trustworthy.

The system reaches for color rarely — IBM Blue marks links, primary CTAs,
and the occasional full-bleed CTA banner. Charcoal carries every other
surface that isn't white. The result is enterprise gravitas without
enterprise stiffness: rigorous, light-weighted, and intentionally
restrained.

**Key characteristics:**
- **Carbon Design System** — the marketing chrome IS Carbon. Buttons are
  square, inputs are square with a bottom rule, corners never round.
- **Light-weight display type**: Plex Sans at weight 300 for 42–76px
  headlines is the brand's typographic signature.
- **One accent color**: `{colors.primary}` IBM Blue carries every link,
  primary CTA, and CTA banner — there's no second brand color.
- White canvas + light gray + charcoal cover roughly 95% of surfaces.
- The footer inverts to charcoal (`{colors.inverse-canvas}` #161616) — the
  only dark surface above the page break.
- Card hierarchy comes from 1px hairlines and surface change, never drop
  shadow.
- `letter-spacing: 0.16px` on body is a small Carbon precision detail
  that's part of the brand voice.
- Typical rhythm: utility bar → top nav → light-weight hero headline →
  feature card grid → customer logo marquee → enterprise feature row →
  training section → newsletter/sign-in CTA → dark footer.

## Colors

### Brand & accent
- **IBM Blue** — the single brand accent: links, primary CTAs, CTA banner
  backgrounds, focus rings.
- **Blue 60** — hovered link state.
- **Blue 80** — pressed primary button.
- **Blue hover** — hover state for primary buttons.

### Surface
- **Canvas** — default page background.
- **Surface 1** — light gray (#f4f4f4): input fields, alternate-row
  stripes, subtle section bands.
- **Surface 2** — slightly darker gray (#e0e0e0): disabled fields,
  hairline-as-fill for separators.
- **Hairline** — 1px borders on cards, inputs, and dividers.
- **Hairline strong** — the 1px charcoal underline on focused inputs,
  Carbon's signature focus treatment.
- **Inverse canvas** — charcoal #161616, the footer surface.
- **Inverse surface 1** — one step lighter than inverse canvas: footer
  column dividers, hovered footer items.

### Text
- **Ink** — every headline and emphasized body line, charcoal #161616.
- **Ink muted** — secondary type at #525252 — meta, sub-headlines, footer
  body.
- **Ink subtle** — tertiary type at #8c8c8c — disabled, helper text,
  captions.
- **Inverse ink / inverse ink muted** — white and light-gray type on the
  charcoal footer.

### Semantic
- **Success green / warning yellow / error red** — the standard status
  trio, drawn from Carbon's green-50, yellow-30, and red-60.
- **Info blue** — identical to primary; used for informational badges.

## Typography

### Family
**IBM Plex Sans** — IBM's own open-source typeface (free for any use),
geometric and slightly humanist, designed specifically for enterprise UI.
Fallback: `Helvetica Neue, Arial, sans-serif`. The same family carries
display, body, and caption — there's no display/body pairing. Hierarchy
comes from size and weight rather than family change. Because Plex Sans is
free under the SIL Open Font License, it's also the easiest custom face on
this list to substitute for exactly — the recommended substitute IS the
real typeface.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale (display-xl 76px
down to eyebrow 14px). Principles:
- Light-weight display is the brand voice: Plex Sans at weight 300 for
  76px headlines reads as quietly authoritative — switching to 700 would
  make it look like every other enterprise site.
- Carbon's `letter-spacing: 0.16px` on body sizes is a precision detail
  worth preserving.
- No mono appears on marketing surfaces — Plex Mono exists but lives in
  product surfaces only.
- Eyebrow type uses sentence case at 14px — Carbon resists the all-caps
  tracked eyebrow common to other enterprise brands.
- Line-heights tighten on display and relax on body: 1.17 at display-xl,
  1.50 at body — proportional to size.

### Font substitutes
IBM Plex Sans is free and open-source (SIL OFL) and available on Google
Fonts — it's the recommended implementation directly, with no substitute
needed. The Plex family also includes Plex Mono and Plex Serif if a build
needs expanded typographic roles.

## Layout

- Base spacing unit: 4px — Carbon's signature 4-pixel grid.
- Full scale in `design-tokens.yaml → spacing`. Card interior padding:
  24px on feature cards, 32px on product cards, 48px on hero cards and CTA
  banners.
- Button padding: 12px vertical, 16px horizontal (Carbon spec). Form input
  padding: 11px vertical, 16px horizontal.
- Carbon's 16-column grid runs at desktop, scaling to 8/4 columns at
  tablet/mobile; max content width sits around 1584px (Carbon's max-grid
  breakpoint).
- Card grids run 4-up at desktop, 2-up at tablet, 1-up at mobile. The
  customer logo marquee uses fixed-width tiles in a flex row, scrolling
  horizontally on smaller viewports.
- Whitespace follows Carbon's precise 4-pixel grid alignment. Sections
  separate via thin gray rows (`{colors.surface-1}`) rather than large
  vertical gaps — content is dense by design, because IBM's audience
  expects to see a lot on a page, not a lot of air.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 (flat) | No shadow, no border | Default for body type, hero text, footer body |
| 1 (hairline) | 1px `{colors.hairline}` border on canvas | Feature cards, inputs, list items |
| 2 (surface lift) | `{colors.surface-1}` background on canvas | Alternate-row banners, hovered cards |
| 3 (focus ring) | 2px `{colors.primary}` outline + 1px hairline-strong underline | Focused input, focused button |

Carbon resists drop shadows on marketing — depth comes from surface change
and 1px hairlines instead. The exception is product/app surfaces, where
Carbon documents shadow tokens for elevated panels, but the marketing site
itself barely uses them. A soft blue gradient backdrop occasionally appears
behind hero illustrations — a faint blue-to-white wash that warms the
canvas without competing with the headline — but otherwise there's no
atmospheric depth: no spotlight cards, no pastel section blocks, no
gradient panels.

## Shapes

| Token | Value | Use |
|---|---|---|
| rounded.none | 0px | Default — every button, card, input, container |
| rounded.xs | 2px | Small badges (rare exception) |
| rounded.sm | 4px | Squared avatar circles, dropdown menus |
| rounded.md | 6px | Used rarely; documented for completeness |
| rounded.lg | 8px | Used rarely; documented for completeness |
| rounded.pill | 9999px | Status pills, badges in product UI (rare on marketing) |

The brand commits to flat 0px corners as the default; the other tokens
exist for product/mobile surfaces but rarely surface on marketing pages.
IBM uses photography (people, hardware, sports cars) and abstract
illustration (geometric mesh, dotted patterns) interchangeably, and image
frames stay flat — no rounded corners. Customer logo tiles sit on
`rounded.none` tiles with thin 1px borders.

## Components

Definitions live in `design-tokens.yaml → components`. Summary:
- **Buttons** — button-primary (blue solid), button-primary-pressed
  (shifts to blue-80), button-secondary (charcoal solid — Carbon's
  "secondary" treatment), button-tertiary (white with a blue border and
  text), button-ghost (plain text + chevron), button-danger (Carbon's
  destructive red variant).
- **Cards & containers** — feature-card / feature-card-elevated (on
  surface-1), product-card, hero-card (light-weight title composition),
  cta-banner (full-width blue panel), resource-tile, customer-logo-tile.
- **Inputs** — text-input / text-input-focused / text-input-error (focus
  replaces the bottom hairline with a 2px blue underline — Carbon's
  signature focus treatment; error adds a 2px red underline),
  newsletter-input.
- **Tabs** — product-tab / product-tab-selected (selected gets
  body-emphasis weight plus a bottom 2px blue underline).
- **Navigation** — top-nav (48px, logomark left, categories center, search/
  sign-in right, 1px bottom hairline), utility-bar (32px slim gray ribbon
  above the nav).
- **Footer** — the charcoal footer, the only inverted surface above the
  page break, with a 5–6 column caption-sized link grid.

## Do's and don'ts

**Do**
- Use `{rounded.none}` 0px on every CTA, card, input, and container — the
  flat-square aesthetic is the brand.
- Pair Plex Sans weight 300 for display sizes (42px+) with weight 400 for
  body — resist bolding the headline.
- Reserve `{colors.primary}` IBM Blue for primary CTAs, links, focused-
  input underlines, and the CTA banner — not as a card background or
  eyebrow color.
- Apply `letter-spacing: 0.16px` to body sizes — it's a Carbon precision
  detail and part of the typographic voice.
- Use surface change (canvas → surface-1) plus 1px hairlines for card
  hierarchy — skip drop shadows.
- Stick to sentence case for eyebrows and section labels — Carbon resists
  all-caps tracking.
- Invert to `{colors.inverse-canvas}` only at the footer; the rest of the
  page stays light.

**Don't**
- Don't round corners on buttons, cards, or inputs — even a 4px rounding
  breaks the Carbon look.
- Don't bold display headlines — weight 300 is the brand voice; 700 makes
  it look generic.
- Don't add atmospheric depth (gradient backdrops, drop shadows,
  atmospheric overlays) outside the documented soft-blue hero gradient.
- Don't introduce a second brand color — status semantics use the
  documented green/yellow/red, but the only chromatic accent is IBM Blue.
- Don't replace IBM Plex Sans with Inter or Helvetica without preserving
  the 0.16px tracking and weight-300 display treatment.
- Don't use pill-shaped buttons — square corners are the identity; pills
  read as a different brand.
- Don't write all-caps tracked eyebrows — Carbon's eyebrows are sentence
  case at 14px.

## Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Max | 1584px | Carbon max grid; gutters expand |
| Desktop-XL | 1312px | Default desktop layout |
| Desktop | 1056px | Card grid 4-up maintained |
| Tablet | 672px | Card grid 4-up → 2-up; nav becomes hamburger |
| Mobile | 320px | Single-column; display-xl scales 76px → ~32px |

Touch targets: Carbon spec calls for a 48px minimum tap target — buttons
and inputs hold 48px on touch viewports; top-nav links grow from 36px to
48px on touch; tab-strip rows hold 48px tap height. Nav links collapse to
a hamburger overlay below 672px while the logomark and search icon stay on
the bar; the utility bar hides below 672px to reclaim vertical space; the
card grid steps 4-up → 2-up → 1-up; display type scales from 76px toward
42px on mobile while preserving the weight-300 treatment; the footer's
6-column link grid collapses to 3 columns at tablet and 1 column at
mobile. Customer logos in the marquee keep aspect ratio and may collapse
to a 2-row scroll below 672px; hero illustrations scale proportionally and
may stack above the headline rather than beside it below 672px.

## Known gaps

- IBM's product surfaces (Cloud Pak, Watson, Datacap) have richer Carbon
  component usage (data tables, graph cells, breadcrumbs, contextual
  menus) than what appears on the marketing pages inspected — those
  components live in Carbon's own documentation rather than in this
  marketing extraction.
- Form-field error and validation styling is documented in Carbon's own
  docs, but the inspected marketing pages didn't render error states.
- Dark mode is documented in Carbon as a Gray-100 theme, but it isn't
  exposed on these marketing pages — only the footer inverts. The full
  dark theme is a separate Carbon palette not captured here.
- The community.ibm.com sub-domain uses a different chrome (a
  community-platform white-label) that approximates Carbon without being
  strict — the documented system applies to ibm.com proper.
