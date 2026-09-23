# PlayStation Design System — Full Analysis

Adapted from the PlayStation marketing-site design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/playstation/DESIGN.md`, MIT License). Token names below refer
to `references/design-tokens.yaml` in this skill.

## Overview

PlayStation's marketing system reads like a console launch trailer
scrolling past the viewer in chapters. Each section is a full-bleed band —
pure black (`colors.canvas-dark`), true white (`colors.canvas-light`), or
PlayStation Blue (`colors.primary`, `#0070d1`) — and each chapter owns one
editorial moment: hero console photography, a games-coming-soon strip, the
PlayStation Plus tier banner, the "30 Years of PlayStation" anniversary
band, or the news strip pulled from the PlayStation Blog. There's no
decorative chrome between chapters — the section's background color change
*is* the divider. Sections stack at the system's largest token,
`spacing.section` (96px), with the next band's color taking over the page
edge to edge.

The system runs two alternating surface modes down the page: a **dark
canvas mode** for editorial product moments (hero, "ON PLAYSTATION" band,
marathon game pages) and a **light canvas mode** for utility surfaces (the
PS5 games listing, support pages, the news index). Both modes share the
same chrome vocabulary — fully-rounded pill buttons, 8px-radius product
cards, the proprietary PlayStation SST face — only the surface and
on-surface colors swap. A third mode, the **PlayStation Blue band**, is
reserved for the highest-priority moments: the Marathon launch CTA strip,
the footer, and any "action required" banner.

Typography is the system's most distinctive choice. PlayStation SST
renders display headlines at **weight 300** (light) — an unusual pick for
a gaming brand that could easily reach for something bolder. The light
weight gives the chrome an airy, almost editorial quality that lets the
imagery speak; copy behaves as information rather than decoration. Heading
sizes drop in tight increments (54 → 44 → 35 → 28 → 22 → 18), and body
settles at 18px with 1.5 line-height for comfortable reading on support
and games pages.

**Key characteristics:**
- A three-canvas chapter system — black, white, and PlayStation Blue —
  alternating down the page.
- PlayStation Blue is the universal primary CTA, always a fully-rounded
  pill.
- Commerce orange (`colors.commerce`, `#d53b00`) is the secondary CTA
  reserved strictly for "Buy now"/"Pre-order"/store actions.
- PlayStation SST's display tier renders at weight 300 with -0.1px to
  +0.4px tracking — the brand's signature airy, editorial voice.
- 8px radius for product cards and feature panels, 4px for inputs, pill
  for every CTA.
- Game tiles, console renders, and PS Plus illustrations occupy 60-90% of
  each section — imagery does the storytelling.
- A representative page rhythm: dark hero → light console showcase → dark
  games rail → light PS Plus tier band → light anniversary callout → dark
  "ON PLAYSTATION" band → light news strip → blue footer.

## Colors

> **Source pages:** home, the PS5 games listing, a single game page
> (Marathon), and the support center. The chrome palette is identical
> across all four; the support page uses only the light-canvas mode while
> marketing pages alternate.

### Brand & accent
- **PlayStation Blue** (`#0070d1`) is the universal primary — every
  primary CTA pill, the active filter chip, the footer surface, badge
  fills, and the inline link color on dark surfaces.
- **PlayStation Blue Pressed** (`#0064b7`) is the pressed state for the
  primary pill, and doubles as the inline link color on light surfaces.
- **Commerce Orange** (`#d53b00`) is the only warm color in the system,
  reserved exclusively for store/buy/pre-order actions.
- **Marathon Yellow** (`#deff20`) is a single high-saturation accent
  extracted from Marathon's own product palette, used only inside that
  dedicated game page and not part of the system's general vocabulary.

### Surface
- **Canvas Dark** (`#000000`) — the pure-black hero band, primary nav
  background, and footer base; the dominant surface for editorial product
  moments.
- **Surface Dark Elevated** (`#121314`) — inset dark panels and the PS
  Plus tier banner background.
- **Surface Dark Card** (`#181818`) — game-tile fill and dark product-card
  background.
- **Canvas Light** (`#ffffff`) — the true-white console-showcase band,
  support page body, and news strip.
- **Surface Card** (`#f5f7fa`) — a cool-blue-tinted product/tier-card
  background on light canvas.

### Text
- **Ink** (`#000000`) is primary text on light canvas; **On Dark**
  (`#ffffff`) is primary text on dark canvas. **Body Light**
  (`rgba(0,0,0,0.6)`) and **Body Dark** (`rgba(255,255,255,0.7)`) carry
  the default translucent paragraph tone on each canvas respectively, with
  **Mute Light** (`#6b6b6b`) and **Mute Dark** (`rgba(229,229,229,0.55)`)
  for metadata.

### Semantic & gradient
- **Warning** (`#c81b3a`) marks validation errors.
- **Link Light** (`#0064b7`) and **Link Dark** (`#53b1ff`) are the inline
  body-link colors on each canvas.
- The **PlayStation Plus gold gradient** — a three-stop horizontal blend
  from `#ffce21` through `#f5a623` to `#ee8e00` — is the only gradient in
  the system, reserved exclusively for the PS Plus tier banner.

## Typography

### Font family
**PlayStation SST** is the proprietary sans used across every text role,
carrying weights 300/400/500/600/700 and falling back through `sst` →
`Arial` → `Helvetica`. The defining choice is using **weight 300 (light)**
for display headlines — unusual for gaming, and the source of the system's
airy, editorial character.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale (display-xl 54px
down to caption-sm 12px). The hierarchy works on a 1.25 line-height ladder
almost exclusively — even body sits at 1.5 rather than a looser 1.6 —
keeping long-form support pages tight and console showcases efficient. The
weight contrast between display (300) and button (700) is dramatic: an
18px chrome line might host a heavyweight CTA right next to a
feather-light 22px headline, giving the system its editorial,
gaming-magazine feel.

### Font substitutes
PlayStation SST is proprietary. **Roboto Light (300)** is the closest
substitute for the display tier; **Inter** at weights 400/500/600 covers
body and chrome; **Source Sans Pro Light (300)** is an alternative for
display when Roboto reads too utilitarian. Preserve the +0.1px to +0.45px
tracking on display and button tiers when substituting — the spacing is
part of what makes the light weight feel premium rather than thin.

## Layout

- **Base unit:** 8px, with finer 4/12px steps for tight inline gaps.
- **Universal section rhythm:** `spacing.section` (96px) between major
  blocks; card grids use `spacing.lg` (24px) gutters.
- **Hero band padding:** 96px vertical / 48px horizontal — the largest
  spacing in the system, reserved for full-bleed chapter bands.
- **Max width:** ~1280px for body text at desktop, expanding to ~48px
  gutters at ultrawide; hero bands and game-tile rails go full-bleed with
  no max-width constraint on imagery.
- **Game tile carousel:** 4-up at desktop, collapsing to 3-up at 1024px
  and 2-up at 768px, each tile at 16:9 with `rounded.md` corners.
- **Support page:** a desktop 30/70 sidebar/article split that collapses
  to a single column with a top accordion at mobile.

Whitespace is structural and band-defined — the 96px section gap reads as
silence between trailer cuts, with no decorative wash or mid-section
divider. Content stays left-aligned in a tight column (~520px at desktop)
while imagery breathes in the right 60-70% of the band.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 — Flat | No border, no shadow | Hero bands, footer, full-bleed sections — the dominant treatment |
| 1 — Hairline divider | 1px `hairline-light` or `hairline-dark` | Card borders, support row dividers |
| 2 — Soft active shadow | `0 4px 12px rgba(0,0,0,0.16)` | Active/pressed CTAs, lifted product card |
| 3 — Section gradient | Soft top-to-bottom darkening | "ON PLAYSTATION" band only |

The system has effectively no resting shadow — depth is built from
surface-color contrast across chapters, and cards lift only on press.
Decorative depth otherwise comes from console product photography (shot on
neutral white with crisp edge lighting), full-bleed cinematic game key art
with title lockups in the lower-left, the PS Plus gold gradient, and the
"ON PLAYSTATION" band's top-to-bottom darkening from `surface-dark-
elevated` to `canvas-dark`.

## Shapes

| Token | Value | Use |
|---|---|---|
| `rounded.none` | 0px | Hero bands, nav, footer, sub-nav, support body — every full-bleed structural surface |
| `rounded.sm` | 4px | Text inputs, support search field |
| `rounded.md` | 8px | Game tiles, product cards, feature cards, PS Plus banner |
| `rounded.lg` | 16px | Rare large containers (dialog cards) |
| `rounded.full` | 9999px | Every CTA pill, filter chips, pagination dots, carousel paddles |

The radius vocabulary works on a 4 / 8 / pill rhythm for chrome, with
structural surfaces staying flat at 0px. Hero console renders sit large
and centered on white at roughly 70% band width; game tiles use 16:9 key
art at 8px radius in a 4-up carousel; the Marathon game-page hero is a
full-bleed cinematic still with the wordmark rendered light-weight in the
lower-left.

## Components

Full specs live in `design-tokens.yaml → components`. Summary:

- **Buttons** — `button-primary` (blue pill, universal CTA), `button-
  commerce` (orange pill, store actions only), `button-secondary-light` /
  `-dark` (outline variants per canvas), `button-disabled`.
- **Filter chips** — `filter-pill` / `filter-pill-active` (translucent
  default, opaque white when active) in the PS5 games filter strip.
- **Inputs** — `text-input` / `text-input-focused` (2px blue border on
  focus, no halo) and the signature `support-search-bar` (pill, 56px tall).
- **Cards & bands** — `product-card` / `product-card-dark`, `game-tile`
  (16:9 cover art with title overlay), `feature-card`, `hero-band-blue` /
  `-dark` / `-light` (the three full-bleed chapter types), `ps-plus-
  banner` (gold-gradient accent bar), `carousel-paddle`, `pagination-dot`.
- **Navigation** — `primary-nav` (48px, dark, centered link row), `sub-
  nav` (40px secondary strip on games/PS Plus pages).
- **Footer** — `footer-section` (blue surface, multi-column link grid —
  the system's "we're done, return to the brand" anchor).
- **Support-specific** — `support-row` (FAQ/category rows with a chevron).

## Do's and don'ts

**Do**
- Reserve PlayStation Blue for primary CTAs and the footer surface only —
  at most one full-bleed blue band per page.
- Reserve commerce orange for store/buy/pre-order CTAs only.
- Set display headings in PlayStation SST at weight 300 — the light
  weight is the brand voice.
- Stack sections at the 96px rhythm with the next band's color taking over
  edge to edge, no decorative dividers.
- Use pill radius on every CTA and 8px on every product card — the
  two-radius vocabulary is the entire shape system aside from inputs.
- Let full-bleed game key art and console renders occupy 60-90% of a
  band's vertical height.
- Use the gold PS Plus gradient exclusively for the PS Plus banner.

**Don't**
- Don't introduce drop shadows on resting cards — the system is flat on
  canvas; cards lift only on press.
- Don't replace PlayStation Blue with another shade of blue.
- Don't use commerce orange on marketing/hero CTAs.
- Don't introduce a sans-serif body font, italic, or monospace style.
- Don't soften pill geometry — CTAs are always fully rounded, never
  medium-radius.
- Don't use the gold gradient on anything besides the PS Plus banner.
- Don't add gradients to chrome beyond the gold accent and the "ON
  PLAYSTATION" darkening.

## Responsive behavior

| Name | Width | Key changes |
|---|---|---|
| ultrawide | 1920px+ | Hero stays at 1280px content max-width |
| desktop-large | 1440px | Default — 4-up game tile carousel |
| desktop-small | 1024px | Game tile rail → 3-up |
| tablet | 768px | Game tiles → 2-up; nav becomes a hamburger drawer |
| mobile | 480px | Single-column; hero display scales 54px → ~32px |
| mobile-narrow | 320px | Section padding tightens to 32px |

Touch targets meet WCAG AAA (≥44×44px): primary/commerce buttons sit at
48px, text inputs at 48px, the support search bar at 56px, carousel
paddles exactly 48×48. Hero bands stay full-bleed at every breakpoint —
only the internal content column reflows from two-column to stacked. The
support page's 30/70 split promotes its sidebar to a top accordion at
tablet, then fully collapses at mobile. Console renders and key art use
art-directed crops on mobile so the central subject stays centered.

## Known gaps

- Mobile screenshots weren't captured — responsive behavior is synthesized
  from desktop evidence and the documented breakpoint stack.
- Hover states aren't documented, per the source's own policy.
- Sign-in/authentication chrome (login modal, account dashboard, profile)
  isn't in the captured pages.
- PlayStation Store in-store browsing (PDP/cart/checkout) uses a denser
  data-table layout this document doesn't describe.
- Other game pages may carry their own per-title brand colors beyond
  Marathon's yellow, which this document doesn't capture.
- Form validation states beyond the `warning` color token aren't present
  in the captured surfaces.
