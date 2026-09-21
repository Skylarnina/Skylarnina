---
name: shopify-design
description: Shopify's marketing-site design system — two parallel design tracks sharing typographic DNA but diverging in canvas polarity. The cinematic marketing track lives on a pure-black canvas with full-bleed merchant photography and giant thin-weight (330) Neue Haas Grotesk Display headlines; the transactional track (pricing, signup) flips to a cream-and-white canvas with aloe/pistachio mint accents and Inter Variable UI body. Every button on both tracks is a pill — never a rounded rectangle. Use when asked for a "Shopify style", "Shopify-inspired UI", or a cinematic-yet-transactional commerce-platform marketing page.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/shopify/DESIGN.md
---

# Shopify Design System

Use this skill when a task calls for Shopify's two-track commerce-marketing
aesthetic: cinematic merchant-photography hero pages paired with light,
transactional pricing/signup flows, or any explicit "Shopify style" request.

## Quick reference

- **Canvas**: two tracks, never blended — `#000000` pure black for
  cinematic marketing pages, `#ffffff` / `#fbfbf5` cream-white for
  transactional pages (pricing, signup, comparison tables).
- **Accent**: no single brand color — black/white polarity carries the
  cinematic track, while `#c1fbd4` aloe mint and `#d4f9e0` pistachio mint
  mark the "growth"/featured accents on the light track only.
- **Type**: **Neue Haas Grotesk Display** at a thin weight 330 for every
  display/headline (down to 48px minimum), paired with **Inter Variable**
  (420-550) for UI body/buttons/captions; the OpenType `ss03` stylistic set
  is enabled globally on both families.
- **Corners**: pill (9999px) is the ONLY button shape across both tracks —
  rounded rectangles never appear on buttons; cards use 8-20px radii.
- **Layout anchor**: full-bleed, uncropped merchant photography on the
  cinematic track (escaping the container entirely); layered stacked-shadow
  pricing cards with a soft paper-like halo on the light track.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first — the two-canvas-track model
   (cinematic black vs. transactional cream) is the core structural choice
   that governs everything else.
2. Pull exact values from `references/design-tokens.yaml` instead of
   guessing hex codes, sizes, or component paddings.
3. Pick ONE track per page — black canvas with white type and outline
   pills, or light canvas with black type and filled pills — never mix them
   within a single page.
4. Render display type in Neue Haas Grotesk Display (or Helvetica Now
   Display / Inter Display as substitutes) at weight 330, never 400+.
5. Reserve aloe/pistachio mint accents for the light/transactional track
   only; they never appear as fills or text on the cinematic black pages.
6. Keep every button pill-shaped regardless of track; vary fill, border, and
   canvas polarity instead of ever switching to a rounded-rectangle shape.
