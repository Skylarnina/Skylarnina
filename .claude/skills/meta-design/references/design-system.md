# Meta Design System — Full Analysis

Adapted from the Meta design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/meta/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Meta's commerce surfaces — homepage, Quest configurator, Ray-Ban product
detail, prescription-lens upsell — present as a confident hardware
merchandiser. The voice is photography-first: large, full-bleed product
imagery dominates above-the-fold space, with white space and tight
typographic hierarchy carrying the rest. A recognizable dual-CTA pattern
runs through the system — a black pill-shaped primary on marketing
surfaces, switching to a saturated cobalt blue (`colors.primary`) only
inside buy-now flows, paired with an outlined ghost button for secondary
navigation.

Optimistic VF, Meta's variable display face, anchors every typographic
surface, ranging from a 64px hero display down to a 12px caption. The
face's `ss01` and `ss02` stylistic sets are switched on together across
every heading role, giving the type a slightly humanist, friendly
character. Below 768px the system collapses cleanly: the hero stacks, the
pill nav becomes a hamburger, three-up feature grids flatten to a single
column, and product configurators drop their right-rail summary into a
sticky bottom bar.

**Key characteristics:**
- Stark white canvas carrying full-bleed product photography, softened with
  32px (`rounded.xxxl`) corners on showcase tiles.
- Two-tier primary button system: marketing CTAs use black
  (`colors.ink-button`) pills; commerce CTAs use cobalt (`colors.primary`)
  pills inside buy-now panels only.
- Optimistic VF as the universal display and body face, always with
  `ss01, ss02` OpenType features switched on together.
- Pill-shaped buttons (`rounded.full`) and 32-40px (`rounded.xxxl`/
  `rounded.feature`) cards as the dominant geometric signature.
- Saturated promotional banners (yellow `colors.warning`, dark
  `colors.ink-deep`) used sparingly above the nav for time-bound offers.
- Photographic feature cards carry no chrome at all — no border, no
  shadow — the product imagery itself is the surface treatment.

## Colors

> Source pages: meta.com/ homepage, the Ray-Ban Meta Skyler Gen 2 PDP, the
> Quest 3S buy-now configurator, and the prescription lens upsell page.
> Token coverage was identical across all four pages.

### Brand & accent
- **Cobalt primary** — the buy-now CTA color; used on every "Add to cart",
  "Configure", and "Pre-order" button inside the commerce flow and the
  right-rail purchase panel.
- **Deep cobalt** — the pressed-state and dark-surface variant of cobalt;
  also the active link color.
- **Soft cobalt** — a translucent background tint (roughly 15% alpha) for
  informational callouts.
- **Facebook blue** — the selected radio/checkbox activation color inside
  form controls.
- **Meta link blue** — reserved for legacy navigation and footer link
  affordances.
- **Oculus purple** — a VR-specific accent used inside Quest-branded
  surfaces for category emphasis.

### Surface
- **Canvas white** — page background and primary card surface.
- **Soft cloud** — subtle product-thumbnail and warranty-card background,
  also the search-pill rest state.
- **Hairline gray** — 1px input border and form-control divider.
- **Hairline soft** — quieter divider used on cards, footer separators, and
  section breaks.

### Text
- **Deep ink** — primary headline and body text on light surfaces.
- **Ink** — standard body and secondary headline text.
- **Charcoal** — tertiary body text and form-button labels.
- **Slate** — section-header copy and supporting microcopy.
- **Steel** — quieter caption text and footer link hierarchy.
- **Stone** — disabled or de-emphasized labels.

### Semantic
- **Success** — "In stock", "Free returns" affirmations.
- **Attention** — mid-priority alerts and timed callouts.
- **Warning** — promotional banners and limited-time tags.
- **Critical / critical strong** — validation errors and destructive
  feedback, plus form-input error borders.

## Typography

### Family
Optimistic VF is Meta's proprietary variable display face, with Montserrat,
Helvetica, Arial, and Noto Sans as fallbacks. The variable weight axis runs
from 300 (light heading, used for editorial intro copy like "Look
forward") through 500 (display/hero/heading-sm) up to 700 (subtitle, body
emphasis, button labels). The `ss01` and `ss02` stylistic sets are switched
on together across every heading role — they soften the geometry and give
the type a slightly humanist breathing room. A secondary Helvetica
fallback chain handles 12px technical microcopy inside spec sheets and
footer fine print.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale (hero-display at
64px down to caption at 12px). Principles:
- Negative letter-spacing on body roles (-0.14px to -0.16px) tightens the
  type fractionally — Optimistic VF is designed for this snug-but-not-
  condensed setting.
- Editorial subheads use the 300 weight deliberately, introducing a visual
  rest step between the 500-weight display headlines and the 400-weight
  body — a three-tier rhythm.
- Headings always carry `ss01, ss02` together, never one without the
  other.
- Buttons, pill tabs, and footer headings all share the same 14px/700/
  -0.14px style, creating a tight visual relationship between interactive
  elements.

## Layout

### Spacing system
- Base unit: 4px, with 8px as the dominant primary step.
- Section rhythm: marketing sections separate at 80px; product-detail
  sections compress to 64px; FAQ stacks tighten further to 32px.
- Card internal padding: 32px standard; icon-feature tiles compress to
  24px; promo-strip cards expand to 64px for hero presence.

### Grid & container
- Marketing pages sit around a 1280px max-width with 32-48px gutters.
- The PDP layout uses a 2-column split: hero gallery at roughly 58% width
  plus a sticky purchase rail at roughly 42% (capped at 380px).
- Three-up feature grids use a 24px column gap; six-up product-thumbnail
  rows (color/SKU pickers) tighten to a 12px gap.

### Whitespace philosophy
Whitespace is product-photography-first: hero sections give imagery 50-70%
of the viewport height, with copy given room to breathe in 32-40px blocks
above and below. Inside the configurator, whitespace tightens
significantly — the buy-now panel is information-dense, with a 16-20px
rhythm between option groups.

## Elevation & depth

The system runs predominantly flat. Elevation is reserved for two
interaction layers:

| Level | Treatment | Use |
|---|---|---|
| 0 (flat) | No shadow; 32px rounding + soft hairline border | Default product cards, why-buy tiles |
| 1 (subtle) | `rgba(0,0,0,0.2) 1px 1px 0px 0px` | Pill-tab activation indicator |
| 2 (sticky panel) | `rgba(20,22,26,0.3) 0px 1px 4px 0px` | PDP right-rail purchase summary, sticky mobile checkout bar |

### Decorative depth
Full-bleed product imagery on rounded cards creates atmospheric layering
without any shadow. Translucent overlays (roughly 10-12% opacity, white or
near-black) sit over dark hero photography to lift text legibility.
Decorative pastel tints inside accessory cards — soft pink, ice-blue, mint
— appear briefly behind product cutouts but are treated as photographic
content rather than formalized system colors.

## Shapes

### Border radius scale

| Token | Value | Use |
|---|---|---|
| xs | 2px | Inline checkbox marks, fine UI corners |
| sm | 4px | Tags, micro-controls |
| md | 6px | Square thumbnail rounding |
| lg | 8px | Form inputs, radio-option containers |
| xl | 16px | Standard feature cards, FAQ accordion items |
| xxl | 24px | Warranty/accessory tiles, ghost-style action cards |
| xxxl | 32px | Photographic feature cards, big promo strips |
| feature | 40px | Accessory hero panels ("Built for prescriptions") |
| full | 100px | Pill buttons, tab chips, badges |
| circle | 50% | Color swatches, circular icon buttons |

### Photography geometry
Product hero photography more often sits in 32px-rounded frames than plain
rectangles. Color/material swatches are perfect circles (32px diameter,
2px white ring when selected). Square product thumbnails use 16px
rounding, while the tighter six-up color/SKU picker grid uses 8px corners
to visually distinguish selection-grid context from showcase context.

## Components

Definitions live in `design-tokens.yaml → components`.

> Per the no-hover policy in the source analysis, hover states are not
> documented — only default and pressed/active states.

### Buttons
- **Primary** — black pill for marketing CTAs ("Shop", "Pre-order"), with
  a charcoal pressed state and a disabled state using muted gray.
- **Buy CTA** — cobalt pill for commerce flows ("Add to cart", "Configure",
  "Continue"), with a deep-cobalt pressed state; appears only inside the
  buy-now configurator and PDP purchase rail.
- **Secondary** — transparent with a 2px deep-ink border, often paired
  with primary in dual-CTA hero patterns.
- **Ghost** — a quieter outlined variant for tertiary CTAs, using a
  low-opacity border.
- **Pill tab** — inactive/active category-navigation pills ("Glasses /
  Quest / Apps"), the active state filling solid dark with no border.
- **Icon circular** — 40×40px circular utility buttons for carousel
  controls, share, and favorite.

### Cards & containers
- **Product feature** — white card with product photography and copy, 32px
  rounding, soft hairline border.
- **Feature photo** — edge-to-edge photographic tile with zero chrome; the
  image fills the card and copy overlays it bottom-left in white.
- **Promo strip** — dark full-width card ("Meta Quest brings the magic of
  virtual reality") with embedded copy and CTAs.
- **Icon feature** — three-up tile with a line icon, headline, and short
  copy for reassurance content ("Free 2-day delivery", warranty, etc.).
- **Checkout summary** — PDP right-rail sticky panel with title, price,
  color picker, and add-to-cart button, carrying the system's one notable
  card shadow.
- **Product thumbnail** — square image cell for color/SKU pickers and
  "People also bought" rows.
- **Warranty / why-buy** — promo callouts and a 4-up reassurance-tile row
  in the lower marketing zone.

### Inputs & forms
- **Text input** — standard field with hairline border, 44px height;
  focused state switches to a 2px Facebook-blue border; error state
  switches to a critical-red border with an inline error label.
- **Search pill** — top-nav search field on a soft-cloud background.
- **Radio option** — configurator option cards (storage, color, shipping),
  selected state switching to a deep-cobalt 2px border — the cobalt theme
  persists into form-control selection signaling.
- **Color swatch circle** — 32px round color/material picker with a white
  ring on selection.

### Badges & status
Promo-yellow, attention, success, and critical badges all share the same
pill shape and caption typography, differing only in background/text
color. The promo banner sits full-width above the top nav for time-bound
offers.

### Navigation
Desktop top navigation is a sticky white bar (~64px) with the Meta
wordmark left, a pill-tab category nav center, and search/account/cart
icons right. Mobile compresses to logo + hamburger + cart, with the
pill-tab nav sliding into a full-screen drawer below 768px. A breadcrumb
sits above the PDP hero.

### Signature components
- **Hero band marketing** — full-bleed photographic hero with overlaid
  white copy and the dual-CTA pair below.
- **Product gallery PDP** — a 4-up vertical thumbnail strip, large central
  product image, and sticky purchase rail using the checkout-summary card.
- **Color/SKU picker row** — six-up grid of square variants with name and
  price below each, active tile bordered in deep ink.
- **Feature icon row** — the four reassurance-benefit tiles.
- **FAQ accordion** — question in bold subtitle, chevron right, expanded
  answer in body text.
- **Tech specs table** — two-column key/value spec rows with hairline
  separators.
- **Testimonial card** — author photo, byline, and quote on a bordered
  white card.
- **Footer** — dense six-column link grid with a bottom row for language/
  region pickers and legal links.

## Do's and don'ts

**Do**
- Reserve `colors.primary` (cobalt) for buy-now CTAs only — its visual
  weight matters precisely because it never appears on marketing pages.
- Use `colors.ink-button` (black) for marketing-surface primary CTAs,
  paired with the ghost-outline secondary.
- Apply `rounded.full` to every button, category pill, badge, and chip —
  buttons are never squared.
- Apply `rounded.xxxl` to photographic product cards and `rounded.xl` to
  icon-feature tiles to keep the card hierarchy visually legible.
- Switch on `ss01, ss02` together for any Optimistic VF heading.
- Use the 300-weight editorial subhead style to create the brand's
  signature rhythm against 500-weight displays.

**Don't**
- Don't use cobalt for marketing-surface primary buttons — it conflicts
  with Meta's black-CTA-on-white marketing positioning.
- Don't introduce additional accent colors beyond cobalt and Oculus
  purple — the hardware brand stays deliberately monochromatic outside its
  product photography.
- Don't soften pill-button corners below full pill — it's a brand
  signature.
- Don't run feature cards without rounding — 32px is the minimum for any
  photographic surface.
- Don't reduce body line-height below 1.50 — the negative letter-spacing
  already tightens the metric.
- Don't apply heavy shadows to marketing cards — elevation is a
  commerce-flow signal, not a marketing flourish.

## Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Mobile small | < 480px | Single column; hero drops to display-lg or smaller; pill tabs collapse into a hamburger drawer; PDP gallery stacks above the purchase rail, which becomes a sticky bottom bar |
| Mobile large | 480-767px | Same as small, but feature tiles render two-up |
| Tablet | 768-1023px | Two-column feature grids; pill-tab nav returns; PDP gallery and purchase rail sit side-by-side at a compressed ~60/40 split |
| Desktop | 1024-1359px | Full three/four-up feature grids; full pill-tab nav; PDP at the standard 58/42 split |
| Wide desktop | ≥ 1360px | Same as desktop with wider hero gutters and larger product photography |

Touch targets stay comfortable: pill buttons render at 40-44px effective
height, circular icon buttons sit at the 40×40px AA floor (bumped to 44px
on mobile), and color swatches carry a 12px clear hit-zone around their
32px circle for an effective ~56px target. Form inputs render at 44px to
match primary button height. The promo banner stays full-width at every
size, truncating on small mobile; the PDP purchase summary collapses into
a sticky bottom bar below 768px; feature grids step from 3/4-up to 2-up at
tablet and 1-up at mobile; hero typography steps from 64px down to 36px
and then 24px as the viewport narrows; and the footer reflows from six
columns to two and then an accordion.

## Known gaps

- Selected/checked states for non-button form controls (toggle,
  multi-select) weren't visible on the captured surfaces — implement
  following the cobalt-on-white pattern used for `radio-option-selected`.
- Animation/transition timings aren't extracted; 150-250ms ease-out for
  primary surface transitions and 300ms ease-in-out for accordion
  expand/collapse are reasonable defaults.
- Specific dark-mode token values for canvas, surface, ink, and hairline
  aren't defined — the brand hasn't surfaced a published dark-mode token
  set on these commerce pages.
- Pastel decorative tints inside accessory cards (soft pink, ice blue,
  mint) appear visually but aren't formalized as system tokens — treat
  them as photographic content, not system colors.
