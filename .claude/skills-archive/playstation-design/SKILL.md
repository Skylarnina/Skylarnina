---
name: playstation-design
description: PlayStation's marketing-site design system — a three-canvas chapter structure that alternates pure black, true white, and PlayStation Blue (#0070d1) bands, each holding one editorial moment like a console launch trailer scrolling past the viewer. Display type in PlayStation SST runs an unusually light weight 300 for an airy, premium feel, every CTA is a fully-rounded pill, and console renders or game key art occupy 60-90% of each section. Use when asked for a "PlayStation style", "PlayStation-inspired UI", or a cinematic, chapter-based gaming/hardware marketing page.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/playstation/DESIGN.md
---

# PlayStation Design System

Use this skill when a task calls for PlayStation's cinematic, chapter-based
console-marketing aesthetic: gaming/hardware landing pages, console launch
sites, or any explicit "PlayStation style" request.

## Quick reference

- **Canvas**: three alternating full-bleed bands — `#000000` black,
  `#ffffff` white, and `#0070d1` PlayStation Blue — with the section's
  background color itself acting as the only divider between chapters.
- **Accent**: PlayStation Blue `#0070d1` is the universal primary CTA;
  Commerce Orange `#d53b00` is reserved strictly for buy/pre-order actions
  and never appears on marketing CTAs.
- **Type**: proprietary **PlayStation SST** at a signature **weight 300**
  for every display/heading size (54px down to 22px) — light weight rather
  than bold gives the brand its airy, editorial voice.
- **Corners**: pill (9999px) on every CTA, 8px (`rounded.md`) on product
  cards and game tiles, 4px (`rounded.sm`) on inputs — structural bands stay
  sharp at 0px.
- **Layout anchor**: full-bleed console renders, game key art, and PS Plus
  tier illustrations occupy 60-90% of each band's height; copy is
  compressed into a narrow editorial slot.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first — the "chapter" band structure
   and the light-weight-300 display type are the two choices that make this
   read as PlayStation rather than generic gaming UI.
2. Pull exact values from `references/design-tokens.yaml` instead of
   guessing hex codes, sizes, or component paddings.
3. Alternate full-bleed black / white / blue bands as the section rhythm;
   never add a decorative divider between them — the color change IS the
   divider.
4. Set display headings in PlayStation SST (or Roboto Light / Source Sans
   Pro Light as substitutes) at weight 300, never bolder.
5. Reserve the blue band for at most one high-priority CTA moment per page
   (footer, launch strip); keep commerce orange confined to store actions.
6. Let console photography and game key art dominate 60-90% of each
   section's vertical space — copy stays a small editorial column.
