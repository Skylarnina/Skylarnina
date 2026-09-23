---
name: binance-design
description: Binance's financial-platform design system — a deep near-black canvas where Binance Yellow (#FCD535) is the single accent carrying every primary CTA, brand-claim headline, and value stat. Type runs the custom BinanceNova (editorial) and BinancePlex (numeric/tabular) stack at bolder-than-usual weights so prices and headlines read at a glance. Marketing/product surfaces default dark; transactional flows (buy crypto, deposit) flip to a shared light theme, with trading green/red threaded through both for price direction. Use when asked for a "Binance style", "Binance-inspired UI", or a confident dark-canvas crypto/trading-platform marketing page.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/binance/DESIGN.md
---

# Binance Design System

Use this skill when a task calls for Binance's confident, data-dense,
dark-canvas trading-platform aesthetic: crypto exchange marketing, fintech
dashboards with trading semantics, or any explicit "Binance style" request.

## Quick reference

- **Canvas**: deep near-black (`#0b0e11`) on marketing/product surfaces;
  transactional flows (buy crypto, deposit, withdraw) flip to a light
  canvas (`#ffffff`) sharing the same yellow CTAs and gray-blue hairlines.
- **Accent**: a single ubiquitous Binance Yellow (`#FCD535`) carries every
  primary CTA, brand-claim headline, and stat number — no second brand
  color exists. Green (`#0ecb81`) and red (`#f6465d`) are reserved
  exclusively for price-direction signals, never CTA fills.
- **Type**: BinanceNova (editorial: headlines, body, nav) paired with
  BinancePlex (numeric: prices, volumes, stat counters) — display sizes run
  weight 600–700, bolder than typical marketing systems, so numbers read at
  a glance against dense data.
- **Corners**: tight — 6px on primary buttons, 8px on inputs/content cards,
  12px on elevated card containers, pill reserved for top-of-page "Sign Up"
  moments only.
- **Layout anchor**: a light-gray footer closes every page even when the
  body above is dark — a deliberate inversion that visually resets the
  page.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` for the full rationale before writing
   CSS or components — the "Do's and Don'ts" section flags Binance's most
   important discipline: never a second brand color.
2. Pull exact values from `references/design-tokens.yaml` (colors,
   typography scale, spacing scale, border-radius scale, component specs)
   rather than guessing hex codes or sizes.
3. Keep Binance Yellow scarce but ubiquitous — primary CTAs, the wordmark,
   and stat/claim headlines, never body text or large surface fills.
4. Choose canvas mode by intent: dark for marketing/product showcase/trading
   dashboards, light for transactional dialogs (buy/deposit/withdraw/forms).
5. Route every number (prices, volumes, percentages, counters) through
   BinancePlex, even inside BinanceNova-set paragraphs — mixing fonts
   breaks the "trustworthy number" voice.
6. Use trading green/red only for explicit Buy/Sell or price-direction
   signals — never as generic confirm/cancel colors, and never as a card
   background fill.
