---
name: stripe-design
description: Stripe's marketing-site design system — a deep-navy ink on white canvas, an electric indigo primary (#533afd), and a pastel cream-orange-lavender-indigo-ruby gradient mesh that occupies the upper third of nearly every page. Type is the Sohne family at thin weight 300 with negative letter-spacing, plus tabular figures for money. Use when asked for a "Stripe style", "Stripe-inspired UI", or a financial-infrastructure marketing page with a gradient-mesh hero and dense product/dashboard mockups.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/stripe/DESIGN.md
---

# Stripe Design System

Use this skill when a task calls for Stripe's financial-infrastructure
marketing look: fintech/payments landing pages, developer-platform pricing
pages, or any explicit "Stripe style" request.

## Quick reference

- **Canvas**: white (`#ffffff`), with a pastel gradient mesh (cream → sherbet
  orange → lavender → indigo → ruby) washed across the upper third of nearly
  every marketing page.
- **Accent**: electric indigo (`#533afd`) — one filled pill CTA per band; deep
  navy (`#1c1e54`) fills the featured pricing tier and dashboard chrome.
- **Type**: **Sohne** at weight 300 with negative tracking (-1.4px at 56px
  down to 0 at body) plus the `ss01` stylistic set; money/numeric cells use
  tabular figures (`tnum`). Free substitute: Inter at 300 weight.
- **Corners**: pill-shaped buttons (9999px) everywhere; cards sit at 12px,
  dashboard mockup chrome at 16px.
- **Layout anchor**: composited dashboard/product-UI mockups (IDE panel +
  table + chart) float above the white canvas beneath the gradient hero.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` for the full rationale — especially the
   gradient-mesh and tabular-figure principles, which are easy to miss.
2. Pull exact values from `references/design-tokens.yaml` (colors, typography
   scale, spacing scale, border-radius scale, component specs) instead of
   guessing hex codes or sizes.
3. Apply the gradient mesh to every marketing hero; a bare-canvas hero reads
   off-brand for this system.
4. Render display type at weight 300 with negative tracking — bumping to 400+
   breaks the brand's editorial-thin feel.
5. Use `tnum` (tabular figures) on any cell showing money, transaction counts,
   or other numerics.
6. Keep indigo scarce — one filled pill CTA per band; never use it as body
   text or a section background.
