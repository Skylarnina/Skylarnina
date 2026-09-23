# Coinbase Design System — Full Analysis

Adapted from the Coinbase design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/coinbase/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Coinbase reads like an institutional financial brand that happens to trade
crypto — quiet, white-canvas, editorially spaced, and almost monochromatic.
The single brand voltage is **Coinbase Blue** (`colors.primary`, `#0052ff`),
used scarcely: every primary CTA pill, the brand wordmark, and inline
emphasis links. Beyond that one blue the system is white canvas + ink +
soft-gray elevation bands + a deep near-black editorial canvas
(`colors.surface-dark`, `#0a0b0d`) for full-bleed product-mockup heroes.

Type pairs **CoinbaseDisplay** for hero headlines with **CoinbaseSans** for
body, captions, and navigation. Display sits at **weight 400** — not the
700+ typical of trading platforms — a deliberate choice that signals
editorial calm and institutional trust rather than fintech urgency.

The page rhythm rotates three modes: bright white editorial sections,
soft-gray elevation bands, and **full-bleed dark editorial heroes** carrying
layered product-UI mockup cards. The dark hero with floating dashboard
mockups is the single most distinctive component in the system.

**Key characteristics:**
- Single accent color — Coinbase Blue carries every primary CTA, wordmark,
  and inline brand link, used scarcely.
- Modest display weights — CoinbaseDisplay at weight 400, never 700+.
- Universal pill/circle geometry: every CTA is `rounded.pill` (100px),
  every asset glyph is `rounded.full`, every card is `rounded.xl` (24px).
  Sharp corners are absent.
- Full-bleed dark heroes with floating product-UI cards is the brand's
  strongest signature pattern.
- Trading semantics (`semantic-up`/`semantic-down`) apply as text color
  only, never as background fills.
- 96px section rhythm — generous editorial pacing.

## Colors

### Brand & accent
- **Coinbase Blue** — the single brand color: every primary CTA pill, the
  Coinbase wordmark, and inline brand links.
- **Coinbase Blue active** — press-state darken.
- **Coinbase Blue disabled** — faded-blue tint for disabled CTAs.
- **Accent yellow** — a small sub-brand accent used very sparingly inside
  Bitcoin/asset glyph illustrations; illustrative-only, not an action
  color.

### Surface
- **Canvas** — the default page floor.
- **Surface soft** — subtle alternating band surface.
- **Surface strong** — light-gray fill behind secondary buttons, search
  pills, asset-icon plates.
- **Surface dark** — deep near-black canvas for full-bleed dark heroes and
  CTA bands (shares its hex with `ink`).
- **Surface dark elevated** — one step lighter, used for the floating
  product-UI mockup cards inside dark heroes.

### Hairlines
- **Hairline** — default 1px divider on white surfaces.
- **Hairline soft** — a lighter divider (shares its hex with
  `surface-strong`).

### Text
- **Ink** — display headings, primary nav, body emphasis.
- **Body** — default running text, a slightly cool gray.
- **Body strong** — same value as ink, used for stronger emphasis.
- **Muted / muted soft** — sub-titles/breadcrumbs/footer secondary down to
  disabled link text.
- **On primary / on dark / on dark soft** — white and muted-white text used
  over blue CTAs and dark heroes.

### Trading semantics
- **Semantic up** — "price up" green, text color only.
- **Semantic down** — "price down" red, text color only.

## Typography

### Font family
The system runs **CoinbaseDisplay** (display headlines), **CoinbaseSans**
(body, navigation, captions, buttons), **CoinbaseIcons** (icon font), and
**CoinbaseMono** for tabular numerical data. Fallback stack:
`-apple-system, system-ui, "Segoe UI", Roboto, Helvetica, Arial, sans-serif`.
The display/body split is functional — CoinbaseDisplay carries hero
headlines only, and CoinbaseSans carries everything else.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale — `display-mega`
(80px/400/-2px) down through `nav-link` (14px/500).

### Principles
- **Display weight stays at 400** — the single most distinctive
  typographic choice, signaling calm institutional trust rather than
  trading-platform urgency.
- **Negative letter-spacing on display only** (-1px to -2px); body stays
  at 0.
- **CoinbaseMono on every number** — asset prices, percent changes, and
  anything tabular renders in CoinbaseMono.

### Note on font substitutes
CoinbaseDisplay, CoinbaseSans, and CoinbaseMono are licensed Coinbase
typefaces. Substitutes: **Inter** at weight 400 with -1.5% letter-spacing
for CoinbaseDisplay; **Inter** at weight 400/600 for CoinbaseSans;
**JetBrains Mono** or **Geist Mono** at weight 500 for CoinbaseMono.

## Layout

- Base spacing unit: 4px; full ladder in `design-tokens.yaml → spacing`.
- Section padding: 96px for every major editorial band.
- Card interior padding: 32px for feature cards and product-UI mockups.
- Max content width ~1200px, centered; hero photography runs full-bleed.
- Editorial body: single 12-column grid; feature-card grids run 2-up for
  hero splits, 3-up for benefit grids; footer uses a 6-column link list.
- Whitespace is generous and editorial — closer to a financial-news outlet
  than a trading dashboard. 96px between bands, 24px between cards inside
  a band. Density lives behind the login wall, not on marketing.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| Flat | No shadow, no border | 80% of surfaces |
| Hairline border | 1px `hairline` | Feature-card outlines on white |
| Soft drop | `0 4px 12px rgba(0,0,0,0.04)` | Single shadow tier — hovered cards |
| Photographic | Full-bleed product-UI mockups | Hero depth |

The most distinctive decorative pattern is **layered product-UI cards
inside dark heroes** — a `product-ui-card-dark` floats above a darker base
canvas, often with a second smaller card overlapping at a slight angle.
Geometric brand illustrations carry illustrative depth where shadows would
otherwise be used.

## Shapes

| Token | Value | Use |
|---|---|---|
| `rounded.none` | 0px | Reserved (essentially unused) |
| `rounded.xs` | 4px | Inline tags |
| `rounded.sm` | 8px | Compact rows |
| `rounded.md` | 12px | Form inputs |
| `rounded.lg` | 16px | Mid-size cards |
| `rounded.xl` | 24px | Feature cards, product-UI mockups, pricing tiers |
| `rounded.pill` | 100px | All CTA buttons, search pills, badges |
| `rounded.full` | 9999px | Asset icon circles, avatars |

Pill for anything interactive, 24px card-radius for containers, full
circle for icons — sharp corners are absent from the system.

## Components

Definitions live in `design-tokens.yaml → components`. Summary:
- **Top nav (light / on-dark)** — 64px bar; wordmark left, primary menu
  (Cryptocurrencies / Individuals / Businesses / Institutions / Developers
  / Company) center, search + globe + Sign In + Sign Up right.
- **Buttons** — `button-primary` (the signature Coinbase Blue pill, 44px),
  active/disabled variants, `button-secondary-light/dark`,
  `button-outline-on-dark`, `button-tertiary-text`, and a larger 56px
  `button-pill-cta` for hero-level actions.
- **Hero bands** — `hero-band-dark` (the signature full-bleed dark hero
  with layered mockups) and `hero-band-light` (used on Wealth/Explore).
- **Product-UI cards (dark / light)** — floating dashboard mockups, often
  shown as 2-3 stacked cards at a slight rotation.
- **Feature card** — used in 2-up and 3-up grids.
- **Trading surfaces** — `asset-row` (icon + name/ticker + price +
  change), `price-up-cell`/`price-down-cell` (color-only, no fill),
  `asset-icon-circular` (32px circular plate).
- **Pricing** — `pricing-tier-card` (light, hairline border) and
  `pricing-tier-featured` (inverts to the dark surface — the inversion
  itself IS the "highlighted choice" signal, no colored ribbon).
- **Forms** — `text-input` (48px, hairline border, 2px blue border on
  focus) and `search-input-pill` (44px pill).
- **`badge-pill`** — uppercase section-label pill ("INSTITUTIONAL",
  "REGULATED").
- **CTA / footer** — `cta-band-dark` pre-footer band, `footer-light`
  6-column link list, `legal-band` bottom strip.

## Do's and don'ts

**Do**
- Reserve Coinbase Blue for primary CTAs, wordmark, brand-glyph
  illustrations, and inline accent links.
- Set every CTA to `rounded.pill` (100px); every asset glyph to
  `rounded.full`.
- Keep CoinbaseDisplay headlines at weight 400.
- Use the dark/light band rotation as page rhythm.
- Render every numerical value in CoinbaseMono.
- Pair every dark hero with a layered product-UI mockup card stack.

**Don't**
- Don't introduce a secondary brand color — Coinbase Blue is the only
  action color; trading green/red are semantic-only.
- Don't bold display copy — bolding shifts the brand voice away from the
  calm weight-400 signature.
- Don't add extra shadow tiers beyond the single soft-drop tier.
- Don't use sharp `rounded.none` (0px) on CTAs.
- Don't mix CoinbaseDisplay and CoinbaseSans inside the same headline.
- Don't use trading green/red as a button background.
- Don't extract a CTA color from a third-party widget (cookie consent,
  OneTrust) — the brand's CTA color is what appears on actual product
  CTAs.

## Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Mobile | < 640px | Hero h1 80→40px; feature grid 1-up; asset rows stack; nav collapses to hamburger; layered product-UI cards collapse to a single card |
| Tablet | 640–1024px | Hero h1 64px; feature grid 2-up; asset rows stay horizontal but compress columns |
| Desktop | 1024–1280px | Full hero h1 80px; feature grid 3-up; full asset-row layout |
| Wide | > 1280px | Content caps at 1200px; hero photography full-bleed |

Touch targets: the primary CTA pill sits at 44px height (WCAG AAA); the
larger hero pill at 56px is well above AAA; the 32px asset-icon circle is
borderline but an 8px padded row creates an effective 48px tap zone; the
search pill sits at 44px (AAA). Nav switches to a hamburger sheet below
768px while the Sign Up CTA stays visible; the hero h1 steps down
80→64→52→44→36px on the smallest screens; layered product-UI mockups
collapse from 2-3 stacked cards to one on mobile; pricing rows collapse
3 → 2 → 1; asset rows stack a ticker line above a price/change line on
mobile.

## Known gaps

- CoinbaseDisplay, CoinbaseSans, and CoinbaseMono are licensed; Inter and
  JetBrains Mono are the documented open substitutes.
- In-product trading surfaces (order book, charts, order forms) sit behind
  login walls — this document covers marketing only.
- Animation timings are out of scope.
- Form validation states beyond focus aren't visible on captured surfaces.
- Accent yellow appears only inside Bitcoin asset-glyph illustrations;
  documented as illustrative-only.
