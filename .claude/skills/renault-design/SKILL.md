---
name: renault-design
description: Renault's public marketing-site design system — a stark white catalogue canvas that alternates with true-black storytelling bands, a single Sunlight Yellow (#ffed00) accent used only on primary CTAs and "yeni"/"NEW" badges, and every line of type set in the proprietary NouvelR sans (weight 700 display, 400 body). Corners stay near-square (2px buttons, 0px tiles) and vehicle photography runs full-bleed with copy stacked beneath rather than overlaid. Use when asked for a "Renault style", Renault-inspired UI, or a confident, photography-first, mass-market automotive dealership look.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/renault/DESIGN.md
---

# Renault Design System

Use this skill for automotive dealership or catalogue marketing pages that
want Renault's disciplined black/white/yellow rhythm: vehicle configurators,
model listing grids, campaign landing pages, or any explicit "Renault style"
request.

## Quick reference

- **Canvas**: white (`#ffffff`) for catalogue/browsing surfaces, true black
  (`#000000`) for hero and storytelling bands — the two switch in full-bleed
  bands, never blended.
- **Accent**: Sunlight Yellow `#ffed00`, always paired with black text —
  reserved for the primary CTA, "NEW" badges, and at most one accent tile
  per section.
- **Type**: NouvelR everywhere (no secondary serif), display sizes at weight
  700 with a very tight `lineHeight: 0.95`; body stays at weight 400. Free
  substitutes: Inter Tight, Manrope, or HK Grotesk Semi Condensed.
- **Corners**: near-square — 2px on buttons, 0px on tiles/cards/vehicle
  photography, pill shape reserved only for sub-nav chips and badges.
- **Layout anchor**: vehicle photography is always full-bleed and
  square-cornered, with copy stacked below the image rather than overlaid on
  it.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first — the Do's and Don'ts section is
   the fastest way to avoid generic automotive-site defaults (rounded cards,
   multiple accent colors, soft grey text).
2. Pull exact values from `references/design-tokens.yaml` rather than
   guessing — hex codes, the NouvelR type scale, spacing, and the square
   border-radius scale are all defined there.
3. Treat yellow as scarce: one primary CTA or accent tile per band. Never
   pair yellow with white text, and never use it as body-text color.
4. Alternate full sections between the white catalogue mode and the black
   storytelling mode rather than using mid-grey backgrounds.
5. Keep vehicle and product photography square-cornered and full-bleed
   inside cards; let captions sit beneath the image, not on top of it.
6. Default buttons to `rounded.xs` (2px) and reserve `rounded.pill` strictly
   for sub-nav filter chips and "NEW" badges.
