---
name: coinbase-design
description: Coinbase's institutional-grade crypto-exchange marketing system — a pure white canvas holding modest-weight CoinbaseDisplay/CoinbaseSans type (display sits at weight 400, never bold), a single scarce accent of Coinbase Blue (#0052ff), and full-bleed near-black editorial heroes carrying layered, angled product-UI mockup cards. Every CTA, badge, and asset glyph rounds to a pill or circle. Use when asked for a "Coinbase style", "Coinbase-inspired UI", or a calm, institutional fintech/crypto marketing page rather than a loud trading-platform look.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/coinbase/DESIGN.md
---

# Coinbase Design System

Use this skill when a task calls for Coinbase's quiet, institutional-finance
marketing aesthetic: crypto/fintech landing pages, editorial financial-
services surfaces, or any explicit "Coinbase style" request that should feel
calm rather than trading-urgent.

## Quick reference

- **Canvas**: pure white, rotating with soft-gray elevation bands and a
  full-bleed near-black (`#0a0b0d`) editorial hero for dashboard mockups.
- **Accent**: Coinbase Blue `#0052ff` — the single brand color, used
  scarcely (primary CTA pill, wordmark, inline brand links only).
- **Type**: CoinbaseDisplay for hero headlines at weight 400 (never
  700+ — the calm, institutional signal), CoinbaseSans for everything
  else, CoinbaseMono on every numeric/tabular value.
- **Corners**: universal pill geometry — every CTA is `rounded.pill`
  (100px), every asset glyph is `rounded.full`, every card is
  `rounded.xl` (24px). No sharp corners anywhere.
- **Layout anchor**: the full-bleed dark hero with 2-3 layered, slightly
  rotated product-UI mockup cards floating above a near-black canvas — the
  brand's single strongest signature.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first — the Do's and Don'ts section
   flags the two most tempting mistakes: bolding display type and adding a
   second brand color.
2. Pull exact values from `references/design-tokens.yaml` rather than
   guessing hex codes, sizes, or paddings.
3. Keep CoinbaseDisplay headlines at weight 400 — bolding shifts the brand
   voice from "calm institutional" to "fintech urgency."
4. Reserve Coinbase Blue for one or two moments per band: the primary CTA
   pill, the wordmark, and inline brand links — never a background or card
   fill.
5. Pair every dark hero with a layered, slightly-angled stack of
   product-UI mockup cards rather than a single flat screenshot.
6. Render every numerical value (prices, percent changes) in CoinbaseMono
   via the `number-display` type token; use trading green/red as text
   color only, never as a button or badge fill.
