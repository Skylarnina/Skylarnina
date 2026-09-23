Adapted from the Nike design analysis in [voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md) (`design-md/nike/DESIGN.md`, MIT License). Token names below refer to `references/design-tokens.yaml` in this skill.

## Overview

Nike's commerce system is built on a single, almost violently simple idea:
photography speaks, the chrome doesn't. Every page reads as an athletic
editorial — towering uppercase Futura display lockups
(`typography.display-campaign`) burned into full-bleed campaign imagery,
with everything else (nav, filters, buttons, cards, footer) reduced to
neutral typography and pill geometry on `colors.canvas` and
`colors.soft-cloud`. There is no decorative gradient, no soft-shadow
nostalgia, no accent color used for "tone" — all chromatic energy is saved
for product photography and a small handful of moments that actually need
to signal: sale price (`colors.sale`), success (`colors.success`), and
swatch dots.

The result feels physical — campaign hero, product grid, sport tile,
footer — stacked like a printed catalog rather than animated like a
typical SaaS landing page. Density is high but never crowded, thanks to
three relentless devices: square or near-square 1:1 product imagery on
`colors.soft-cloud`, pill-shaped black CTAs (`rounded.full`) anchoring
every actionable surface, and a tight 8px-base spacing scale that keeps
cards and filters mathematically aligned across PLP, PDP, and editorial
pages.

Across the men's homepage, a trail-running listing, a product detail page,
the membership page, and Jordan Golf, the same chrome appears in identical
proportions — only the photography and copy change. That consistency is
the system's signature: maximum editorial expression in the imagery,
maximum mechanical restraint everywhere else.

**Key characteristics:**
- Editorial campaign heroes with `typography.display-campaign` (Futura ND,
  96px, line-height 0.9, uppercase) burned directly into full-bleed
  photography.
- A pure black/white/single-gray UI palette — `colors.ink`, `colors.canvas`,
  and `colors.soft-cloud` carry roughly 95% of the chrome surface area.
- Pill geometry everywhere — every CTA, search field, filter chip, and
  badge uses `rounded.full` (30px) or `rounded.md` (24px); there are no
  sharp-cornered buttons.
- Product cards sit at zero radius, zero shadow, directly on
  `colors.soft-cloud` swatch backgrounds — the photograph is the card.
- Two-tone CTA hierarchy — `button-primary` (black on anything light)
  versus `button-secondary` (soft-cloud gray on anything bright) — never
  both at full strength on the same surface.
- An 8px spacing system with section rhythm at `spacing.section` (48px)
  keeps consistent vertical breathing across PLP, PDP, and editorial pages.
- Sale signaling is the only non-neutral color in retail chrome:
  `colors.sale` price plus strike-through original price, with no badge
  background.

## Colors

> Source pages: `/men` (primary), a trail-running PLP, the ACG Zegama PDP,
> `/membership`, and a Jordan Golf PLP. The chrome palette is identical
> across all five — only photography varies.

### Brand & accent
- **Nike Black** (`ink`, `#111111`) — the brand's only "color." It is the
  primary CTA, the swatch dot, the active filter chip, the campaign
  overlay, the headline color, and the body text. When Nike wants to
  assert anything, it goes black.
- **Pure White** (`on-primary`/`canvas`, `#ffffff`) — an equal partner to
  black, carrying every page background, the on-image CTA, and inverse
  text on ink surfaces.

### Surface
- **Soft Cloud** (`soft-cloud`, `#f5f5f5`) — the most-used non-white
  surface in the system: product-card image backgrounds, search pill,
  secondary CTA, utility bar, sport-category swatch tiles. It is the
  "color" of every product photograph's stage.
- **Hairline** (`#cacacb`) — 1px dividers between filter rows, footer
  columns, and PDP disclosure rows.
- **Hairline Soft** (`#e5e5e5`) — the inset 1px shadow under sticky bars
  and tab strips, the only "shadow" the system uses.

### Text
- **Ink** — primary text on light surfaces: headlines, product names,
  prices, nav.
- **Charcoal** — a slightly softer body weight where ink is too heavy.
- **Ash** — disabled secondary border on dark surfaces and low-emphasis
  utility text.
- **Mute** — product category subtitles ("Men's Trail Running Shoes"),
  footer link text, secondary metadata.
- **Stone** — inverse secondary text on dark surfaces and the lowest-
  emphasis utility text.

### Semantic
- **Sale / Sale Deep** — discounted price color and "% off" copy (the only
  red in retail chrome), with a deeper hover/pressed/dark-mode variant.
- **Success / Success Bright** — confirmation messages, in-stock
  indicators, eligibility ticks, with an inverse-on-dark variant.
- **Info / Info Deep** — informational link/badge accent in
  member-experience callouts, with a pressed variant.

### Category accents (sport/collection chips)
These appear sparingly — almost exclusively as small chip backgrounds,
swatch dots, or category illustrations in editorial tiles, never as text
or primary CTA color:
- **Accent Pink / Pink Soft** — SKIMS/women's collection moments and soft
  tinting on member-experience tiles.
- **Accent Purple Soft / Purple Pale** — an editorial swatch dot and the
  lightest soft-tile fill.
- **Accent Teal** — trail/outdoor/ACG editorial accent in lockups.
- **Accent Pink Deep** — the deepest editorial overlay tint, used as a wash
  on heritage/Jordan tiles.

## Typography

### Font family
- **Nike Futura ND** (display campaign only) — a proprietary geometric
  sans for the towering uppercase headlines burned into campaign hero
  photography, falling back to Helvetica Now Text Medium → Helvetica →
  Arial.
- **Helvetica Now Display Medium** (headings 16–32px) — a modern Helvetica
  cut tuned for display sizes, carrying every section title, PDP product
  name, and dialog headline.
- **Helvetica Now Text Medium** (UI 12–16px) — buttons, captions, swatch
  labels, badge text; the system's UI workhorse.
- **Helvetica Now Text** (body and links) — long-form body and underlined
  inline links.
- **Neue Frutiger Arabic** — the RTL pairing for Arabic locales.
- **Helvetica Neue 9px** — the legal fine-print utility row only.

When substituting on systems without proprietary Nike fonts: pair **Inter**
(700 for body chrome, 500 for buttons) with **Bebas Neue** or **Anton** at
96px/0.9 line-height for the campaign headline tier, tightening
letter-spacing slightly (-0.5%) to approximate Futura ND's optical weight.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale (96px uppercase
campaign display down to a 9px legal fine-print row). The system runs on
extreme typographic contrast — a single 96px uppercase display tier for
editorial moments, and a quiet 12–16px Helvetica Now Text/Medium tier
carrying everything else. There is almost no middle ground: the jump from
`heading-xl` (32px) straight to `body-strong` (16px) is intentional and
creates a "billboard above, catalog below" effect on every page.
Letter-spacing stays at 0 throughout — both Futura ND and Helvetica Now are
cut for tight optical fit at scale.

### Note on font substitutes
The closest open-source path to Nike's display tier is **Bebas Neue**
(free, geometric condensed) at 96px/0.9/uppercase/500. For UI text,
**Inter** is the safest substitute, matching weights 400/500 closely at
button and caption sizes.

## Layout

### Spacing system
Base unit 8px. Full scale: `spacing.xxs` (2px) · `spacing.xs` (4px) ·
`spacing.sm` (8px) · `spacing.md` (12px) · `spacing.lg` (18px) ·
`spacing.xl` (24px) · `spacing.xxl` (30px) · `spacing.section` (48px+).
Every page in the set uses `spacing.section` (48px) as the vertical gap
between major content blocks (campaign hero → trending row → featured row
→ shop-by-sport → latest-in-clothing → footer). PLP card grids use 8px
gutters; PDP disclosure rows stack at 24px vertical padding. Product cards
use zero internal padding — the image is full-bleed, with metadata rows
sitting directly below at an 8px gap.

### Grid & container
Max content width sits around 1440px, with edge gutters growing to ~80px
at 1920px — the system lets very wide viewports breathe rather than
stretch. PLP listings use 3-up at desktop, collapsing to 2-up at 1023px
and 1-up at 599px. The men's homepage mixes a 2-up campaign hero row, a
3- or 4-up "Trending Now" row, a horizontal-scroll "Shop by Sport" rail,
and a 4-up "Latest in Clothing" thumbnail grid. The filter sidebar is a
~220px fixed-width left rail at desktop, collapsing into a "Hide Filters"
toggle at narrow widths.

### Whitespace philosophy
Whitespace is a tool for separation, not for breath. Sections butt
directly against each other with the section rhythm, and product photos
tile edge-to-edge within their grid — there is no padding wrapped around
the product image itself. The "air" comes from the soft-cloud background
of the photograph, not from layout margin, and headlines sit immediately
under the section divider line rather than floating in decorative space.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 — Flat | no shadow, no border | default for cards, buttons, sections — the dominant treatment |
| 1 — Hairline divider | 1px solid hairline | filter row separators, footer column borders, PDP disclosure-row separators |
| 2 — Inset bottom-line | `box-shadow: inset 0 -1px 0 hairline-soft` | sticky utility/sub-nav bar bottom edge, tab strip underline |

There is no drop-shadow elevation in the retail chrome at all — cards never
lift on the page. The only depth cue is the 1px inset hairline on sticky
strips and the contrast between full-bleed photography and soft-cloud
product backdrops.

### Decorative depth
Depth comes entirely from photography, not CSS effects. Editorial campaign
tiles create depth via cinematic perspective (a runner on a trail, a model
in a courtyard) with the Futura display headline overlaid in white or ink
directly on the image. Product-card photography is shot flat on
soft-cloud to remove background depth, so the product itself is the only
thing with form on the page. Sport-category tiles use full-bleed cinematic
photography with a small `button-outline-on-image` pill anchored
bottom-left, giving a crisp white pill against atmospheric imagery.

## Shapes

| Token | Value | Use |
|---|---|---|
| `rounded.none` | 0px | cards, campaign tiles, product imagery, navigation, footer — every container |
| `rounded.sm` | 18px | avatar/icon container in member-benefit lockups |
| `rounded.md` | 24px | search pill, search submit, filter input |
| `rounded.lg` | 30px | every CTA pill — primary, secondary, on-image, filter chip, geo-selector, "Notify Me" |
| `rounded.full` | 9999px | color swatch dots and circular icon buttons (back, share, favorite, carousel paddle) |

### Photography geometry
Product cards use a consistent 1:1 square or near-square (~4:5 portrait on
tall crops), full-bleed with no padding, on a soft-cloud backdrop. The
editorial campaign hero uses a ~16:9 or wider cinematic crop, full-bleed
across the content max-width, with the Futura display headline burned into
the lower-left or upper-left third. The sport-category rail uses 4:5
portrait full-bleed thumbnails with a small CTA pill bottom-left. The PDP
main image is square, with a vertical thumbnail rail (~5–7 thumbnails) to
its left for rapid color/angle browsing.

## Components

Definitions live in `design-tokens.yaml → components` (default and
active/pressed states only — hover states are not documented per system
policy):

- **`button-primary`** — the universal Nike CTA: ink background, white
  text, 30px pill, 48px height. Pressed state (`button-primary-active`)
  keeps the ink fill but shrinks to `scale(0.5)` at `opacity: 0.5` — Nike's
  signature "tap collapse" feedback.
- **`button-secondary`** — soft-cloud background, ink text, the
  lower-emphasis alternate when a primary CTA already exists.
- **`button-outline-on-image`** — the crisp white pill that anchors the
  bottom-left of every full-bleed sport-category and editorial tile.
- **`button-icon-circular`** — 40px circular controls for back-arrow,
  carousel paddle, wishlist heart, share, and "Hide Filters."
- **`filter-chip`/`filter-chip-active`** — a fully-inverted flip from
  outlined to ink-filled when selected; no middle state.
- **`search-pill`/`search-pill-focused`** — 24px-radius pill that gains a
  2px ink border and a 12px soft-cloud outer halo on focus.
- **`product-card`** — zero-padding container; image area
  (`product-card-image`) is full-bleed on soft-cloud; below it (in order,
  with 8px gaps): swatch-dot row, optional promo badge, product name
  (`body-strong`), category subtitle (`caption-md`, muted), and a price row
  where sale items show `colors.sale` discounted price + strike-through
  original + "% off."
- **`campaign-tile`** — the brand's signature editorial unit: full-bleed
  photography with the 96px uppercase display headline burned in, color
  chosen per-asset (white or ink) to read against the image, anchored by a
  single `button-outline-on-image` pill.
- **`category-icon-card`** — a centered ~80px category illustration with a
  caption label below, used in icon-strip grids.
- **`member-benefit-card`** — full-bleed photographic card on a dark
  background with a heading and an "Explore" outline pill at bottom-left.
- **`swatch-dot`/`swatch-dot-active`** — a 12px circle filled with the
  colorway's actual product color; the active state adds a 2px ink ring
  with a 2px white interior gap — Nike's signature concentric-ring
  selected state, with no size change.
- **`badge-promo`** — a hairline-bordered pill ("Just In", "Coming Soon",
  "Recycled Materials") sitting on top of product imagery.
- **`badge-sale-text`** — inline sale-red price-row text with no
  container, the only "badge" without a background.

### Navigation
- **`utility-bar`** — a top strip (~36px) with a right-aligned cluster:
  "Find a Store · Help · Join Us · Sign In." Always present, never
  collapses.
- **`primary-nav`** — the main nav (56–64px): Nike swoosh at left,
  centered links ("New & Featured · Men · Women · Kids · Jordan · Nike
  SKIMS · Sport"), and a right cluster (search pill, wishlist heart, bag
  icon). The active section gets a 2px bottom underline, no background
  fill.
- **Sub-nav strip (PLP)** — breadcrumb + sort + "Hide Filters" controls
  under the primary nav, with an inset hairline-soft bottom edge.
- **Mobile top nav** — hamburger (left), swoosh (center), search + bag
  (right); search collapses to icon-only until tapped; primary nav
  collapses into a full-height left-side drawer.

### Signature components
- **`pdp-disclosure-row`** / **`faq-row`** — stacked accordion rows for
  "View Product Details," "Shipping & Returns," "Reviews," or membership
  FAQs, each with a 24px vertical padding and a 1px hairline divider.
- **`filter-sidebar`** — the PLP left rail, with section headers separated
  by 18px vertical gaps, an ink underline for active filters, and muted
  counts in parentheses.
- **`footer`** — a single 1px hairline top divider above four link columns
  (Resources / Help / Company / Promotions & Discounts) and a fine-print
  row (`utility-xs`, muted) with copyright, locale switcher, terms, and
  privacy.

## Do's and don'ts

**Do**
- Reserve `typography.display-campaign` exclusively for editorial campaign
  hero lockups — never for section headers or product titles.
- Use `button-primary` (ink pill) as the single primary action per
  viewport, pairing it at most with `button-secondary` for a soft
  alternative.
- Stage every product photograph on `colors.soft-cloud` — the gray is the
  system's "studio."
- Keep all CTAs pill-shaped at `rounded.lg` (30px); never introduce a
  square or `rounded.sm` button.
- Use `colors.sale` only on price rows — never on backgrounds, badges, or
  chrome.
- Stack content sections at `spacing.section` (48px) rhythm with no
  decorative dividers — the photography's bleed-edge is the divider.
- Anchor on-image CTAs with `button-outline-on-image` (white pill) at
  bottom-left — the system's universal "shop this image" position.

**Don't**
- Don't introduce drop shadows or card elevation — cards sit flat, and the
  only depth cue is the 1px inset hairline on sticky bars.
- Don't use the category accent colors for primary chrome — they belong to
  swatch dots, soft tile fills, and editorial moments only.
- Don't replace `colors.ink` with a near-black gray like `colors.charcoal`
  for a CTA — Nike's primary pill is true `#111111`.
- Don't pad inside product cards — the image is full-bleed, metadata sits
  directly below with an 8px gap.
- Don't put two campaign-tile lockups in the same row at the same scale —
  Nike alternates a single full-bleed editorial tile with a 2-up or 4-up
  grid.
- Don't underline anything other than inline links and the active
  primary-nav indicator — buttons, headings, and prices stay un-underlined.
- Don't introduce a third button shape — pill or icon-circular is the
  entire vocabulary.

## Responsive behavior

### Breakpoints
| Name | Width | Key changes |
|---|---|---|
| ultrawide | 1920px+ | content max-width holds at ~1440px; outer gutters grow to ~80px per side |
| desktop-large | 1440px | default desktop — 3-up product grid, 4-up clothing strip, full primary nav |
| desktop | 1200px | same as large with slightly narrower outer gutters |
| desktop-small | 1024px | filter sidebar starts compressing; sport rail shows ~3 visible tiles |
| tablet | 1023–961px | 3-up PLP collapses to 2-up; "Hide Filters" becomes a default toggle |
| tablet-narrow | 960–640px | primary nav center cluster collapses to a hamburger drawer; search pill becomes icon-only |
| mobile-landscape | 639–600px | 2-up PLP collapses to 1-up; product cards go full-width, stacking image and metadata |
| mobile | 599–320px | single-column everything; campaign tiles run full screen width at shorter Futura sizes (~64px) |

### Touch targets
All interactive elements meet WCAG AAA (44×44px minimum). Pills
(`button-primary`, `button-secondary`) sit at 48px height with 32px
horizontal padding. Icon-circular buttons sit at 40px — just under AAA but
above AA — with hit-target padding extending the tappable area to 48px+.
Filter-chip pills are 40px height with 16px padding.

### Collapsing strategy
The primary nav's desktop center cluster collapses to a mobile drawer
triggered by a hamburger left of the swoosh. The PLP grid steps 3-up →
2-up → 1-up at 1023, 599, and below, with gutters dropping from 8px to 4px
on mobile. The filter sidebar goes 220px fixed → "Hide Filters" toggle →
off-canvas full-screen drawer at mobile. The sport rail's desktop
horizontal scroll (~5 visible) becomes a mobile peek-next-card pattern
(~1.5 visible). Section spacing steps from 48px desktop → 32px tablet →
24px mobile, and the editorial campaign headline steps 96px → 64px → 48px
with line-height holding at 0.9 throughout.

### Image behavior
Product imagery is responsive at the same 1:1 ratio across all
breakpoints — the image scales, the ratio doesn't. Editorial campaign
tiles use art-direction crops: a 16:9 wide hero on desktop swaps to a 4:5
portrait on mobile so the figure stays centered with room for the headline
burn-in. All non-critical product imagery lazy-loads as the user scrolls
into the next grid row.

## Known gaps

- Mobile screenshots were not captured — the responsive behavior above
  synthesizes Nike's known mobile pattern (hamburger drawer, 1-up grid,
  headline downscale) from desktop evidence and the extracted breakpoint
  list.
- Hover states are not documented by system policy; Nike's CSS uses
  `--pds-color-element-hover` and `--pds-color-text-hover` tokens, but
  their values are not included here.
- Dialog/modal styling beyond the geo-selector and country-confirmation
  pill pair is not confirmed; bag, wishlist, and login overlays are not
  documented.
- Form-field styling for checkout, sign-up, and address forms is not
  present in the captured surfaces — only the search pill is documented.
- Bag and wishlist icon-state variants (filled count badges) are not
  visible in the captured pages.
