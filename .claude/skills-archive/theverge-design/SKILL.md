---
name: theverge-design
description: The Verge's editorial design system — a near-black canvas (#131313) shot through with hazard-tape acid-mint (#3cffd0) and ultraviolet (#5200ff), massive 107px Manuka display headlines, and a vertical "StoryStream" timeline of fully saturated, rounded color-block story tiles (mint, purple, yellow, pink, orange). Depth is entirely flat — 1px hairline borders do what shadows do elsewhere — and every ALL-CAPS label runs in tracked PolySans Mono. Use when asked for a "The Verge style", "Verge-inspired UI", or a loud, dark-canvas tech-media/editorial feed layout.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/theverge/DESIGN.md
---

# The Verge Design System

Use this skill when a task calls for The Verge's loud, dark-canvas
editorial aesthetic: tech-media homepages, story-timeline feeds, or any
explicit "The Verge style" request.

## Quick reference

- **Canvas**: near-black (`#131313`) with no light-mode counterpart — the
  dark canvas is the product on every view.
- **Accent**: acid-mint (`#3cffd0`) and ultraviolet (`#5200ff`) used as
  hazard-tape accents (CTAs, borders, active states, saturated story-tile
  fills), never as a background wash.
- **Type**: heavyweight (900) Manuka display headlines up to 107px paired
  with PolySans for UI/body and uppercase-only PolySans Mono for labels,
  timestamps, and tags.
- **Corners**: eight discrete radii from 2px (typewriter tags) to 40px
  (outlined pills) — every rectangle rounds to one of them, nothing is
  square.
- **Layout anchor**: a vertical "StoryStream" timeline where each post is
  a rounded, often fully-saturated color-block tile stacked along a
  dashed rail, rather than a conventional magazine grid.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first — the "Do's and Don'ts"
   section is the fastest way to avoid a generic dark-mode blog look.
2. Pull exact values from `references/design-tokens.yaml` (colors,
   typography scale, spacing scale, border-radius scale, component specs)
   instead of guessing hex codes or sizes.
3. Build the feed as a StoryStream timeline — pill-cornered rectangles
   stacked on a vertical rail, mixing plain dark tiles with fully
   saturated color-block tiles for emphasis.
4. Use Manuka only at 60px and above for display headlines; never drop it
   into UI, buttons, or body copy.
5. Set every kicker, timestamp, category tag, and button label in
   uppercase PolySans Mono with 1.1-1.9px tracking.
6. Replace shadows with 1px hazard-color hairline borders or saturated
   fills — this system carries elevation through color and outline, never
   box-shadow.
