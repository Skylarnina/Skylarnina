---
name: meta-design
description: Meta's hardware-commerce design system — spanning Quest VR and Ray-Ban Meta AI glasses storefronts — pairs a stark white canvas with full-bleed photographic product cards, Optimistic VF (a confident variable display face with ss01/ss02 stylistic sets), and a dual-CTA hero pattern of black marketing pills alongside a saturated cobalt blue (#0064E0) reserved strictly for buy-now/checkout actions. Pill-shaped 100px-radius buttons and generous 24-32px card rounding carry across the homepage, product detail pages, and buy-now configurators. Use when asked for a "Meta style", Meta-inspired UI, or a confident, photography-first hardware/commerce marketing and product-detail page.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/meta/DESIGN.md
---

# Meta Design System

Use this skill when a task calls for Meta's confident hardware-merchandiser
aesthetic: consumer-electronics storefronts, product-detail/buy-now
configurator flows, or any explicit "Meta style" request.

## Quick reference

- **Canvas**: `#ffffff` stark white — carries full-bleed product photography
  as the dominant visual element.
- **Accent**: two-tier CTA color system — black (`#000000`) for marketing
  pills on homepage/editorial surfaces, cobalt blue (`#0064e0`) reserved
  exclusively for buy-now/checkout CTAs inside commerce flows.
- **Type**: Optimistic VF, a variable display face spanning weight 300
  (editorial subheads) to 700 (emphasis), always with `ss01, ss02`
  stylistic sets switched on together for a humanist, friendly geometry.
- **Corners**: pill-shaped (100px/`rounded.full`) on every button, tab, and
  badge; 32px (`rounded.xxxl`) on photographic feature cards; 16px
  (`rounded.xl`) on icon-feature tiles.
- **Layout anchor**: photography-first hero bands and PDP galleries where
  full-bleed product imagery carries 50-70% of viewport height, with no
  card chrome (no border, no shadow) on photographic showcase tiles.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first — the "Do's and Don'ts" section
   is the fastest way to avoid conflating the two CTA colors.
2. Pull exact values from `references/design-tokens.yaml` rather than
   guessing hex codes or sizes.
3. Keep cobalt (`colors.primary`) strictly inside buy-now/checkout flows —
   marketing-surface primaries always use black (`colors.ink-button`).
4. Apply `rounded.full` to every button, pill tab, and badge — buttons are
   never squared in this system.
5. Switch on `ss01, ss02` together for any Optimistic VF heading; never use
   one stylistic set without the other.
6. Lead sections with full-bleed product photography on `rounded.xxxl`
   cards rather than illustration, gradients, or heavy card chrome.
