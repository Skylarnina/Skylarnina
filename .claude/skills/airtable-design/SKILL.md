---
name: airtable-design
description: Airtable's editorial workflow-software design system — white canvas, dark-ink type, generous whitespace, and a near-black pill-cornered primary CTA, with brand voltage delivered through full-bleed "signature" cards in coral, dark green, and dark navy that punctuate long-scroll pages every few screens. Type runs Haas Grotesk at modest, never-bold weights, with a separate Inter Display pricing sub-system. Use when asked for an "Airtable style", "Airtable-inspired UI", or a quietly editorial, whitespace-led B2B SaaS marketing page.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/airtable/DESIGN.md
---

# Airtable Design System

Use this skill when a task calls for Airtable's calm, editorial, print-like
workflow-software marketing aesthetic: B2B SaaS landing pages, productivity
tool marketing, or any explicit "Airtable style" request.

## Quick reference

- **Canvas**: pure white (`#ffffff`) with dark ink text (`#181d26`) — no
  gradients, no mesh, no atmospheric hero backdrop.
- **Accent**: no single accent color — brand voltage instead comes from
  full-bleed **signature surface cards**: coral (`#aa2d00`), forest green
  (`#0a2e0e`), and dark navy (`#181d26`), plus a warm-pastel demo-grid
  palette (peach, mint, yellow, mustard).
- **Type**: Haas Grotesk / Haas Groot Disp at weight 400–500 — display
  headlines never go bolder than 500. A separate Inter Display pricing
  sub-system at unusual mid-weight (475) marks the pricing page as a
  distinct dialect.
- **Corners**: hierarchical — 12px on primary CTAs and signature cards, 10px
  on content cards, 6px on inputs, pill-shaped only on the pricing page's
  buttons (a deliberate sub-system signal).
- **Layout anchor**: rhythm alternates white canvas, signature card, white,
  cream callout, dark CTA, light CTA banner, footer — the canvas resets
  between every signature surface.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first — the "Do's and Don'ts" section
   flags the most common mistake: mistaking the link-blue CSS variable name
   for the primary button color, when the real primary is near-black.
2. Pull exact values from `references/design-tokens.yaml` rather than
   guessing hex codes, sizes, or radii.
3. Keep the primary CTA near-black (`{colors.primary}`) with a 12px radius —
   never blue, never pill-shaped outside the pricing sub-system.
4. Break editorial monotony with full-bleed signature cards (coral, forest,
   dark navy) every 2–3 screens; never stack two consecutive white bands.
5. Keep the hero pure whitespace — no gradient, no mesh, no atmospheric
   backdrop behind the headline.
6. If building a pricing surface, switch fully into the Inter Display +
   pill-button sub-system rather than mixing it with the main Haas dialect.
