---
name: apple-design
description: Apple's marketing-site design system — a photography-first interface that alternates white, parchment, and near-black product "tiles" (alternating canvases as the section divider itself), SF Pro Display headlines with negative letter-spacing, and a single quiet Action Blue (#0066cc) interactive color. UI chrome recedes almost entirely — there are no shadows on cards, buttons, or text, only one signature drop-shadow reserved for product photography resting on a surface. Use when asked for an "Apple style", "Apple-inspired UI", or a reverent, product-photography-led marketing page.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/apple/DESIGN.md
---

# Apple Design System

Use this skill when a task calls for Apple's museum-gallery product marketing
aesthetic: hardware/product launch pages, premium consumer-tech marketing, or
any explicit "Apple style" request.

## Quick reference

- **Canvas**: alternates white (`#ffffff`), parchment off-white
  (`#f5f5f7`), and near-black tiles (`#272729`–`#252527`) — the color
  change between full-bleed tiles IS the section divider, with no gap or
  border between them.
- **Accent**: a single quiet Action Blue (`#0066cc`) carries every
  interactive element — pill CTAs, text links, focus rings — and nothing
  else. A brighter Sky Link Blue (`#2997ff`) substitutes on dark tiles.
- **Type**: SF Pro Display (headlines) + SF Pro Text (body/UI), with
  negative letter-spacing at every size above 17px for the signature "Apple
  tight" cadence; body runs at 17px/400, never 16px.
- **Corners**: full pill (9999px) on every CTA and search input — the
  signature Apple shape; 18px on utility cards; 0px (no rounding) on
  full-bleed product tiles.
- **Layout anchor**: one soft product-shadow (`rgba(0,0,0,0.22) 3px 5px
  30px`) reserved exclusively for product renders resting on a surface —
  never applied to cards, buttons, or text.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` for the full rationale before writing
   CSS or components — the "Do's and Don'ts" section is the fastest way to
   avoid adding chrome Apple's system deliberately omits.
2. Pull exact values from `references/design-tokens.yaml` (colors,
   typography scale, spacing scale, border-radius scale, component specs)
   rather than guessing hex codes or sizes.
3. Alternate full-bleed light and dark product tiles for section rhythm —
   the color change is the divider, so never add a border or gap between
   tiles.
4. Keep `{colors.primary}` (Action Blue) as the only interactive color; do
   not introduce a second accent, and switch to Sky Link Blue only on dark
   tiles.
5. Reserve the single product drop-shadow for photography resting on a
   surface — never apply shadow to cards, buttons, or text.
6. Set headlines in SF Pro Display with negative tracking (down to
   -0.374px) and body at 17px/400 SF Pro Text — never 16px, never weight
   500 (the system's weight ladder is 300/400/600/700, with 500 absent).
