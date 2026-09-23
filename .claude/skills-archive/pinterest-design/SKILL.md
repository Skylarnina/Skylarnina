---
name: pinterest-design
description: Pinterest's photography-first discovery design system — a warm-cream neutral chrome (#f6f6f3) that recedes behind full-bleed pin imagery, with Pinterest Red (#e60023) reserved solely for the sticky "Sign up" CTA and active states. Pin Sans type runs a steep jump from a tight-tracked 70px hero headline down to 16px body, and nearly every surface — buttons, inputs, pin cards — rounds to a fully-rounded pill or a 16px/32px two-step radius system. Use when asked for a "Pinterest style", "Pinterest-inspired UI", or a masonry-grid, photography-led content-discovery interface.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/pinterest/DESIGN.md
---

# Pinterest Design System

Use this skill when a task calls for Pinterest's photography-led discovery
aesthetic: masonry image grids, content-marketplace marketing pages, or any
explicit "Pinterest style" request.

## Quick reference

- **Canvas**: warm-cream neutrals — `#ffffff` canvas, `#f6f6f3`
  surface-card — never a cold pure-gray chrome.
- **Accent**: Pinterest Red `#e60023` used ONLY for the Sign-up CTA, the
  active-tab indicator, and the wordmark. Everything else stays monochrome
  so imagery can carry the color.
- **Type**: proprietary **Pin Sans** (Inter is the closest open substitute)
  with tight negative tracking (-1.2px) on the 70px display tier.
- **Corners**: two-radius system — 16px (`rounded.md`) for nearly
  everything, 32px (`rounded.lg`) for large pin cards and modals, plus pill
  (9999px) for search bars, chips, and avatars. Never sharp, never a
  medium-radius in between.
- **Layout anchor**: a column-based masonry pin grid with 8px gutters where
  each pin's natural aspect ratio is preserved — the pin photograph IS the
  card, with zero internal padding.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` before writing CSS — it explains the
   "get out of the photograph's way" principle that governs every choice.
2. Pull exact values from `references/design-tokens.yaml` (colors,
   typography scale, spacing, radius, component specs) instead of guessing.
3. Treat Pinterest Red as scarce — one Sign-up CTA per fold, never a card
   fill or section background.
4. Build the masonry pin grid with 16px-radius tiles, zero internal padding,
   and 8px gutters; let each image keep its natural aspect ratio.
5. Reserve 32px radius for large feature pins and modals only — the jump
   from 16px straight to 32px (no in-between value) is part of the brand.
6. Apply negative letter-spacing (-1.2px / -0.8px) on the display and
   heading-xl tiers to keep large headlines feeling dense and confident.
