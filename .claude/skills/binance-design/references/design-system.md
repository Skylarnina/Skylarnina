# Binance Design System — Full Analysis

Adapted from the Binance design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/binance/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Binance reads as a trading platform that wants to feel both authoritative
and energetic at once. The base atmosphere is a deep near-black canvas
(`{colors.canvas-dark}` #0b0e11) holding white type and a single, ubiquitous
accent — Binance Yellow (`{colors.primary}` #FCD535). That yellow does
nearly all of the brand's heavy lifting: every primary CTA, every
brand-claim headline ("FUNDS ARE SAFU"), every "Sign Up" pill, every
featured-tier indicator, and the wordmark itself. There is no second brand
color; the system trusts the yellow voltage to carry the brand and it does.

Type runs Binance's custom BinanceNova (display + body) and BinancePlex
(numerical/financial display). BinanceNova carries headlines, section
titles, and body copy; BinancePlex appears wherever a number needs to feel
"tabular and reliable" — price tickers, transaction volumes, user counts,
prize pools. Both run bolder than typical marketing systems: display sizes
sit at weight 600–700 because a trading platform needs its numbers and
claims to read at a glance against dense data, while body copy stays at
400.

The product is genuinely multi-theme. Marketing surfaces (homepage, smart
money, futures arena) default dark, while transactional surfaces (buy
crypto, deposit, withdraw) flip to a light theme. The same yellow CTAs and
gray-blue hairlines (`{colors.hairline-on-light}` #eaecef) thread through
both modes — only canvas, surface, and text tones flip. Trading green
(`{colors.trading-up}` #0ecb81) and red (`{colors.trading-down}` #f6465d)
signal price direction across both modes, in tables, charts, and tickers.

**Key characteristics:**
- Single accent color (`{colors.primary}` #FCD535) carries all brand
  voltage: primary CTAs, hero headlines, the wordmark, badges — used
  scarcely for emphasis on dark, ubiquitously on transactional dialogs.
- Custom type stack: BinanceNova for editorial content, BinancePlex for
  numbers — big stat numbers always render in BinancePlex for tabular
  consistency.
- Multi-theme: marketing pages default dark, transactional pages flip
  light; yellow CTAs and trading colors are shared across both.
- A light-gray footer closes every page even on dark-canvas pages — a
  deliberate inversion that visually resets the page at the bottom.
- Trading semantics apply as text color (green up / red down), never as
  badge or button background fill.
- Card surfaces are flat color blocks — no gradient surfaces, no
  atmospheric backdrops.
- Radius runs small to medium (6–12px); the pill radius is a deliberate
  exception reserved for top-of-page feature CTAs.
- Editorial bands sit at 80px vertical rhythm — slightly tighter than
  typical marketing-only sites because product pages mix marketing bands
  with dense data tables.

## Colors

### Brand & Accent
- **Binance Yellow** (`{colors.primary}` #FCD535) — the single brand
  color: primary CTA backgrounds, the wordmark, brand-claim headlines,
  trust badges, large stat numbers, inline links.
- **Binance Yellow Active** (`{colors.primary-active}` #f0b90b) — the
  press/hover-darker variant.
- **Binance Yellow Disabled** (`{colors.primary-disabled}` #3a3a1f) — a
  desaturated dark-yellow for disabled CTAs over dark canvas.
- **Accent Turquoise** (`{colors.accent-turquoise}` #2dbdb6) — a small
  secondary accent used sparingly on one product's CTA (Smart Money);
  treat as a single-product experiment, not a system color.

### Surface

**Dark mode (marketing default):**
- **Canvas Dark** (`{colors.canvas-dark}` #0b0e11) — the primary page
  floor; near-black with a slight warm tint, never pure black.
- **Surface Card Dark** (`{colors.surface-card-dark}` #1e2329) — cards, nav
  dropdowns, secondary buttons, the markets table.
- **Surface Elevated Dark** (`{colors.surface-elevated-dark}` #2b3139) —
  one step lighter, for nested cards, hovered nav items, chart panels.

**Light mode (transactional):**
- **Canvas Light** (`{colors.canvas-light}` #ffffff) — the page floor on
  buy crypto, deposit forms, account dialogs.
- **Surface Soft Light** (`{colors.surface-soft-light}` #fafafa) — footer
  surface, disabled states.
- **Surface Strong Light** (`{colors.surface-strong-light}` #f5f5f5) — form
  input backgrounds in muted contexts.

### Hairlines & Borders
- **Hairline on Light** (`{colors.hairline-on-light}` #eaecef) — the most
  frequently used token in the system; Binance leans on hairlines
  liberally.
- **Hairline on Dark** (`{colors.hairline-on-dark}` #2b3139) — shares its
  hex with surface-elevated-dark, so borders feel like surface steps
  rather than ink lines.
- **Border Strong** (`{colors.border-strong}` #cdd1d6) — a heavier tone on
  disabled secondary buttons.

### Text
- **Ink** (`{colors.ink}` #181a20) — the strongest text on light surfaces.
- **Body on Dark** (`{colors.body}` #eaecef) — default running text on
  dark canvas, deliberately not pure white.
- **Body on Light** (`{colors.body-on-light}` #181a20) — reuses the ink
  token.
- **Muted** (`{colors.muted}` #707a8a) / **Muted Strong**
  (`{colors.muted-strong}` #929aa5) — footer links, breadcrumbs, captions,
  table headers; work on both canvas modes.
- **On Primary** (`{colors.on-primary}` #181a20) — black text on yellow
  CTAs.
- **On Dark** (`{colors.on-dark}` #ffffff) — pure white for high-contrast
  headlines on dark canvas.

### Trading Semantics
- **Trading Up** (`{colors.trading-up}` #0ecb81) — price-up green, used as
  text color in tables/charts/tickers, never as a button background.
- **Trading Down** (`{colors.trading-down}` #f6465d) — price-down red,
  same usage rules.

### Info / Focus
- **Info** (`{colors.info}` #3b82f6) — inline info badges and the
  focus-ring base for input focus.

## Typography

### Font Family
BinanceNova carries editorial type (headlines, paragraphs, buttons, nav);
BinancePlex carries numerical/financial type (prices, volumes,
percentages, stat counters, prize pools). The split is functional, not
decorative — BinanceNova on a price ticker would lose the platform's
trading character, and BinancePlex on a paragraph would feel
monospace-cold. Mixing them is not optional.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale (hero-display 64px
down to the 12px caption). Notable roles:
- `{typography.hero-display}` (64px/700) is the homepage h1 ("316,258,026
  USERS TRUST US").
- `{typography.number-display}` (40px/700, BinancePlex) is the big-stat
  role for headline numbers like transaction volumes and prize pools.

### Principles
Display sizes use weight 700 — heavier than most marketing systems,
because a trading platform's numbers need to read at a glance against
chart visualizations and dense tables. Weight never softens to 400 the way
more editorial brands do. `{typography.number-display}` and every smaller
number variant always render in BinancePlex, regardless of surrounding
context — prices, volumes, and stat counters are the system's "trustworthy
number" voice.

### Note on Font Substitutes
If BinanceNova/BinancePlex are unavailable, **Inter** is the closest
open-source substitute for BinanceNova, and **JetBrains Mono** or **IBM
Plex Sans** substitutes for BinancePlex depending on whether tabular
monospace fidelity or humanist proportions matter more. Adjust display
headlines' line-height down about 3% to match BinanceNova's tighter cap
height.

## Layout

### Spacing System
- Base unit: 4px.
- Tokens: `{spacing.xxs}` 4px · `{spacing.xs}` 8px · `{spacing.sm}` 12px ·
  `{spacing.md}` 16px · `{spacing.lg}` 24px · `{spacing.xl}` 32px ·
  `{spacing.xxl}` 48px · `{spacing.section}` 80px.
- Section padding: 80px — slightly tighter than airy marketing sites
  because Binance pages mix marketing bands with dense product surfaces
  (markets tables, FAQ accordions).
- Card padding: 24px for content cards and markets tables, 32px for
  QR-promo cards and CTA bands, 16px for trust badges and table rows.
- Gutters: 24px between cards in 3-up grids, 16px inside footer columns
  and dense FAQ lists.

### Grid & Container
- Max content width: ~1280px on marketing pages, ~1440px on product
  surfaces where horizontal density matters.
- Editorial body: single 12-column grid; product pages often use an 8/4
  split (main panel + side rail).
- Markets table: 5-column header (Pair / Last Price / 24h Change / 24h
  Volume / Action).
- Footer: 6-column link list at desktop, wrapping to 2-up at tablet and
  1-up on mobile.

### Whitespace Philosophy
Binance is denser than typical marketing sites — long-scroll pages mix
hero bands with markets tables, FAQ accordions, and feature grids without
much breathing room between them. The system trusts contrast (yellow vs.
dark canvas, green vs. red price cells) to do the visual separation work
rather than whitespace; where whitespace does appear, it's uniformly
`{spacing.section}` between bands.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat | No shadow, no border | Body sections, top nav, hero bands, footer |
| Soft hairline | 1px hairline on dark or light | Inputs, table dividers, FAQ separators, secondary buttons |
| Card surface | Surface-card fill, no shadow | Elevated cards (markets table, QR-promo, feature-photo, trust badges) |
| Subtle drop shadow | Faint shadow, only over imagery | Sparingly on the buy-crypto amount card |
| Focus ring | 2px info-ring outline at 50% alpha | Input/button keyboard focus |

The elevation philosophy is flat surfaces with color-block separation —
Binance avoids heavy drop shadows or glassmorphism; depth comes from the
contrast between canvas-dark and surface-card-dark (a large lightness jump
that reads as a clear boundary). A single-page exception is the Futures
Arena hero, which uses a yellow-to-dark vertical gradient backdrop —
treat it as a one-off event-hero treatment, not a system-wide signature.
Coin-stack illustrations and trophy icons flanking large stat blocks are
content assets, not design tokens.

## Shapes

| Token | Value | Use |
|---|---|---|
| `{rounded.xs}` | 2px | Almost no use — very small badges only |
| `{rounded.sm}` | 4px | Small inline buttons (subscribe, inline trading actions) |
| `{rounded.md}` | 6px | Standard CTA buttons, primary input fields |
| `{rounded.lg}` | 8px | Search input, content cards, trust badges |
| `{rounded.xl}` | 12px | Elevated card containers (markets table, QR-promo, CTA bands) |
| `{rounded.pill}` | 9999px | Prominent feature CTAs ("Sign Up", "Join Now") |
| `{rounded.full}` | 9999px / 50% | Coin icons, avatars |

Binance's radius hierarchy is tighter than typical marketing systems — most
surfaces sit at 6–12px, with the pill radius a deliberate exception
signaling "this is a top-of-page action." Coin icons render as 24–32px
rounded glyphs, often with a circular outline plus the coin's own brand
color; 3D coin-stack and trophy illustrations carry a slight floor shadow.

## Components

- **`top-nav-dark`** / **`top-nav-light`** — 64px bar carrying the yellow
  wordmark, the primary product menu, and right-side language/theme
  toggle + "Log In" text link + "Sign Up" primary CTA. Light variant swaps
  canvas and text tones for transactional pages.
- **`button-primary`** — yellow fill, black text (the system's iconic
  pairing), 6px radius, 12×24px padding, 40px height. Press state darkens
  to `{colors.primary-active}`; disabled state desaturates.
- **`button-primary-pill`** — a larger pill variant for top-of-page sign-up
  moments and product-launch heroes; used sparingly as a "this is THE
  action" signal.
- **`button-secondary-on-dark`** / **`-on-light`** — surface-card or
  canvas fill with matching text, for less-emphasized actions.
- **`button-trading-up`** / **`button-trading-down`** — solid green/red
  buttons for explicit Buy/Long or Sell/Short actions, 4px radius, tighter
  than the primary CTA to fit dense trading rows.
- **`button-subscribe`** — a compact 28px-tall yellow CTA for subscribing
  to a trader inside a dense table row.
- **`hero-band-dark`** — full-width dark band carrying the homepage h1,
  sub-headline, and dual CTA pair at 80px padding.
- **`stat-callout-card`** — transparent background, yellow BinancePlex
  numbers used as a flat layout block rather than a card with a surface.
- **`trust-badge`** — small dark cards holding "No.1" claims, 8px radius,
  16×20px padding.
- **`markets-table-card`** / **`markets-row`** — the homepage's right-side
  markets table: a tab row plus rows of coin pairs with last price, 24h
  change (colored by direction), and an action chevron.
- **`price-up-cell`** / **`price-down-cell`** — colored text cells always
  paired with a small directional triangle.
- **`feature-photo-card`** — the "Trade on the go" lifestyle photo strip,
  edge-to-edge images with no internal padding.
- **`qr-promo-card`** — a dark card with QR code, app-store badges, and
  short copy, 32px padding.
- **`funds-safu-band`** — the yellow-headlined trust band, anchored by
  three large stat-callout numbers (BTC reserves, users helped, funds
  recovered).
- **`faq-row`** — a transparent accordion row with a hairline divider,
  question in title-sm, answer in body-md when open.
- **`cta-band-dark`** — the pre-footer CTA, elevated one step from canvas,
  12px radius, 48px padding.
- **`buy-crypto-amount-card`** / **`steps-card`** / **`price-chart-card`**
  — light-mode transactional components: an editable BinancePlex amount
  input, a 3-up "How to Buy" step sequence, and a candlestick/line chart
  card with green/red coloring.
- **`search-input-on-dark`** — the homepage's "Search currencies" input,
  8px radius, paired with a yellow pill "Sign Up" CTA.
- **`text-input-on-light`** — standard transactional-page input, 6px
  radius, hairline border, focus-ring on activation.
- **`trader-row`** — Smart Money's top-traders table row: avatar, name,
  badge, ROI/AUM/mint-date columns, and a yellow subscribe CTA.
- **`arena-hero-gradient`** — the Futures Arena product-launch hero, a
  yellow-to-dark vertical gradient with a centered prize-pool headline and
  pill CTA; a signature, single-surface treatment, not a general pattern.
- **`footer-light`** — the light-gray footer closing every page (including
  dark ones), a 6-column link list at 64px vertical padding — one of
  Binance's most distinctive layout choices.

## Do's and Don'ts

### Do
- Reserve `{colors.primary}` for primary actions, brand-claim headlines,
  and the wordmark — its scarcity is what makes it powerful.
- Keep the yellow-with-black-text primary CTA identical across both dark
  and light canvas modes.
- Use green/red trading buttons only for explicit Buy/Sell or Long/Short
  actions — never for a generic confirm/cancel.
- Route every number through BinancePlex; mixing BinanceNova into a
  numeric ticker breaks the trading-platform character.
- Choose canvas mode by surface intent: dark for marketing/product/trading
  dashboards, light for transactional dialogs.
- Anchor every editorial band with 80px vertical rhythm.

### Don't
- Don't introduce a second brand color — the turquoise accent is a
  single-product experiment, not a system token.
- Don't use yellow for body text or large surface fills.
- Don't use trading green/red as card background fills — they're
  price-direction text/badge signals only.
- Don't soften display weight — 700 is intentional; dropping to 400 reads
  as design-portfolio, not trading platform.
- Don't add atmospheric gradients to the canvas outside the one documented
  Futures Arena exception.
- Don't invert the primary button's text color — black-on-yellow is the
  system's signature; white text loses contrast and recognition.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 768px | Nav collapses to hamburger; hero h1 drops from 64px to ~36px; markets table converts to a horizontally-scrollable card list; demo grids 1-up; footer 6 cols → 2. |
| Tablet | 768–1024px | Nav stays horizontal but tightens, secondary items hide behind "More"; markets table 2-up; feature grids 2-up. |
| Desktop | 1024–1440px | Full nav with all primary items; 5-column markets table; trading dashboards in 8/4 split. |
| Wide | > 1440px | Same as desktop with more outer breathing room; max content 1280–1440px depending on surface. |

### Touch Targets
- Primary CTAs render at minimum 40×40px, meeting WCAG AAA with
  surrounding spacing.
- Subscribe/inline action buttons are 28×28px — denser than ideal but
  matches trading-platform norms.
- Coin icons sit at 32×32px, with the entire row tappable for a 44px+
  effective target.

### Collapsing Strategy
- Nav collapses to a full-screen hamburger sheet below 768px, yellow CTAs
  anchored at the bottom.
- Markets table reflows to a horizontally-scrollable single card per coin
  pair on mobile.
- Hero stat numbers shrink proportionally rather than wrapping — the
  biggest claim always reads as one block.
- Trading dashboards switch from chart-plus-side-rail to chart-only with a
  separate "Trade" tab on mobile.
- The light footer stays full-bleed at every breakpoint.

## Known Gaps

- The light-hairline token (`#eaecef`) is the highest-frequency color in
  the extracted source, ahead of the brand-defining yellow — yellow's
  system role was confirmed from screenshots because it's used scarcely as
  an accent.
- BinanceNova/BinancePlex weight-axis values aren't formalized as
  variable-font tokens — only the static weights observed are documented.
- Animation and transition timings (chart redraws, price-change flashes)
  are out of scope.
- Form validation states beyond default inputs weren't extracted.
- The trading dashboard surfaces (Spot/Futures/Margin) weren't in the
  analyzed URL set; their order-book and position-management cards aren't
  documented here.
- The light/dark theme toggle behavior on transactional pages is product
  behavior, not extracted from marketing surfaces.
