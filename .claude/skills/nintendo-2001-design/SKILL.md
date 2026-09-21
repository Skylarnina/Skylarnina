---
name: nintendo-2001-design
description: Nintendo.com's 2001-era "console chrome" design language — brushed-periwinkle beveled metal panels, a carbon-navy halftone-textured command bar, and warm signal colors (nav gold, amber, signal orange) reserved strictly for wayfinding. Hero fields are photographic, page-tinted, and topped with outlined box-art display type. Use when asked for a "Nintendo 2001 style", a Y2K console-hardware UI, or a retro gaming-brand marketing page that should read like the faceplate of a game system rather than a modern flat website.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/nintendo-2001/DESIGN.md
---

# Nintendo.com (2001) Design System

Use this skill when a task calls for a turn-of-the-millennium console-hardware
aesthetic: retro gaming marketing pages, Y2K nostalgia sites, or any explicit
"Nintendo 2001 style" / "Nintendo.com retro" request.

## Quick reference

- **Canvas**: `#7a8aba` brushed-periwinkle metallic chrome — every region is a
  beveled plate inset into this body, never a flat modern background.
- **Accent(s)**: warmth is rationed as pure wayfinding — `#e48600` nav gold
  for menu words, `#ecab37` amber for utility chips/badges, `#f68d1f` signal
  orange for every forward/Submit cue. Cool chrome never carries action color.
- **Type approach**: web-safe Arial/Arial Black only — uppercase tracked
  labels for chrome, and heavy outlined-and-shadowed display type (box-art
  style) for hero wordmarks.
- **Corner-radius feel**: mostly sharp or chamfered (`0px`), roundness spent
  only on the logo pill, radio dots, and circle-arrow badges (`9999px`).
- **Distinctive layout trait**: every region is a beveled metal plate —
  bright top highlight, `#3d4f97` chrome-indigo shadow line beneath — with a
  carbon-navy halftone-textured command layer (nav, right rail, footer)
  sitting "above" the periwinkle body.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first — the "Do's and Don'ts" section
   is the fastest way to avoid turning this into a generic rounded-card
   modern UI, which erases the entire identity.
2. Pull exact hex/px values from `references/design-tokens.yaml` rather than
   guessing — the bevel colors, warm accents, and chamfered-corner logic are
   load-bearing.
3. Build every panel as a beveled plate (bright highlight top, chrome-indigo
   shadow line beneath) instead of using drop shadows or Material-style
   elevation.
4. Reserve warm color strictly for wayfinding — never let signal orange or
   amber become decorative fill.
5. Cap hero sections with outlined, drop-shadowed display type over
   full-bleed, page-tinted photographic fields.
6. Keep the layout dense and fixed-canvas in spirit — this system predates
   generous modern whitespace and responsive fluidity.
