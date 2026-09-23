---
name: uber-design
description: Uber's transportation-and-delivery marketing design system — a black-and-white duet on a pure white canvas, where black is the only conversion color and every interactive element (buttons, chips, app-download badges) rounds to a 999px pill. Headlines use the custom UberMove display sans at weight 700 in sentence case, paired with editorial 4:3 illustrations of riders and drivers as the sole decorative system. Use when asked for an "Uber style", Uber-inspired UI, or a confident monochrome ride-hailing/delivery marketing layout.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/uber/DESIGN.md
---

# Uber Design System

Use this skill for transportation, delivery, or "super-app" marketing surfaces
that want Uber's disciplined black-and-white restraint, or for any explicit
"Uber style" request.

## Quick reference

- **Canvas**: `#ffffff` pure white, with `#efefef` / `#f3f3f3` soft-gray
  tints for chip and nested-input fills — there is no dark mode.
- **Accent**: `#000000` ink black is the ONLY conversion color — every
  primary CTA pill, the footer fill, and dark promo bands. No second accent.
- **Type**: `UberMove` weight 700 for all display headlines (sentence-case,
  never uppercase, never letter-spaced), `UberMoveText` weight 400/500 for
  body, buttons, and links. Substitutes: Inter (display) + Inter (text).
- **Corners**: `999px` pill on every interactive element (buttons, chips,
  app-download badges); cards and larger surfaces use `16px`.
- **Layout anchor**: a signature alternating band rhythm — white feature
  card, then a black promo band with white text/CTA, repeating down the
  page — plus 4:3 editorial illustrations of riders/drivers as the only
  decoration.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first — the Do's and Don'ts section
   is the fastest way to avoid diluting the black-and-white system with a
   stray accent color.
2. Pull exact hex/px values from `references/design-tokens.yaml` rather than
   guessing — colors, the type scale, spacing, radius scale, and component
   specs are all defined there.
3. Keep the palette to black + white + grayscale; resist adding a second
   brand color even for status or highlight moments.
4. Round every interactive shape to the `999px` pill — this is the single
   geometric signature of the brand. Cards alone break to `16px`.
5. Alternate white and black bands down the page rather than relying on
   shadows or gradients for section separation.
6. Anchor promo sections with a 4:3 editorial illustration instead of stock
   photography or icon art.
