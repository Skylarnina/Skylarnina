---
name: minimax-design
description: MiniMax's AI-infrastructure design system pairs a stark black-and-white marketing/documentation base — black-pill primary CTAs on white canvas, DM Sans across every size from an 80px hero down to 12px micro labels — with saturated per-product gradient cards (coral, magenta, blue, purple) that turn each model release into its own visual identity, like album covers laid across the homepage. A 3-column documentation layout (sidebar / prose / TOC) carries the developer surfaces. Use when asked for a "MiniMax style", MiniMax-inspired UI, or a monochrome AI marketing page punctuated by vivid per-product color cards.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/minimax/DESIGN.md
---

# MiniMax Design System

Use this skill when a task calls for MiniMax's confident dual-identity AI
brand look: AI model showcase pages, developer documentation, or any
explicit "MiniMax style" request.

## Quick reference

- **Canvas**: `#ffffff` stark white for marketing and docs surfaces; a
  black (`#0a0a0a`) footer closes every page.
- **Accent**: no single brand color — instead each model/product line owns
  a saturated identity color (coral M2.7, magenta Music 2.6, blue Hailuo,
  purple Speech 2.8), confined strictly to that product's showcase card.
- **Type**: DM Sans throughout, from an 80px hero at -2px tracking and 1.10
  line-height down to 12px micro labels; weight discipline of 400/500/600/
  700 only.
- **Corners**: pill (9999px) on every button and tab; 32px on vibrant
  gradient product cards versus 16px on quiet white documentation cards —
  the doubled radius signals "featured product moment."
- **Layout anchor**: a 4-column horizontal row of vibrant gradient product
  cards reading like album covers, sitting above a quieter white
  AI-product-tile grid and a 3-column docs layout (sidebar / prose / TOC).

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first — the "Do's and Don'ts" section
   is the fastest way to avoid diluting the product-color-encoding system.
2. Pull exact values from `references/design-tokens.yaml` rather than
   guessing hex codes or sizes.
3. Keep brand colors (coral, magenta, blue, purple) confined to
   product-card identity moments — never use them on standard buttons or
   generic surfaces.
4. Pair `rounded.hero` (32px) gradient cards with `rounded.xl` (16px) white
   cards in the same viewport — the radius contrast is the visual
   signature.
5. Apply `rounded.full` to every button, pill tab, and badge.
6. Use `typography.hero-display` (80px, -2px tracking, 1.10 line-height)
   for hero displays without compromising the tight leading.
