---
name: framer-design
description: Framer's marketing-site design system — a near-pure-black artboard canvas (#090909) carrying oversized white display type in GT Walsheim Medium with extreme negative tracking (down to -5.5px at 110px), broken every few sections by oversized vibrant gradient "spotlight" cards in magenta, violet, orange, and coral. The single chromatic accent, sky blue, is reserved for hyperlinks and focus states only. Use when asked for a "Framer style", Framer-inspired UI, or a confident black-canvas builder/creative-tool marketing page with poster-scale headlines and living gradient showcase tiles.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/framer/DESIGN.md
---

# Framer Design System

Use this skill when a task calls for Framer's dark, poster-scale builder
aesthetic: website/design-tool marketing pages, creative-software landing
pages, or any explicit "Framer style" request.

## Quick reference

- **Canvas**: `#090909` near-pure black with a faint warmth — every band of
  the page (hero, pricing, FAQ, footer) sits on it; there is no light mode.
- **Accent**: `#0099ff` sky blue — used ONLY for hyperlinks, focus rings,
  and selection states, never as a background or button fill.
- **Type**: GT Walsheim Medium for display with extreme negative tracking
  (-5.5px at 110px down to -3.1px at 62px) reading like a poster; Inter
  Variable for body with bespoke OpenType character variants (`cv01/05/09/
  11`, `ss03/07`, `dlig`).
- **Corners**: white pill CTAs (`rounded.pill` 100px) are the only primary
  shape; cards default to 15–20px, gradient spotlight cards go softer at
  30px.
- **Layout anchor**: oversized vibrant gradient "spotlight" cards (violet,
  magenta, orange, coral) drop into otherwise monochrome card grids as
  living showcase tiles — never as full section backgrounds.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` for the full rationale before writing
   CSS or components — the "Do's and Don'ts" section is the fastest way to
   avoid an over-colored or over-shadowed dark theme.
2. Pull exact values from `references/design-tokens.yaml` (colors,
   typography scale, spacing scale, border-radius scale, component specs)
   rather than guessing hex codes or sizes.
3. Push display-size letter-spacing aggressively negative — treat the
   tracking percentage, not the raw px value, as the constant when scaling
   headline size down for smaller viewports.
4. Drop in at most one or two `gradient-spotlight-card` variants per long
   page; three or more in one viewport reads as a moodboard, not a system.
5. Compose every CTA as a pill — primary in white, secondary as a charcoal
   pill — never a bordered ghost button and never a square corner.
6. Use surface lift (canvas → surface-1 → surface-2) to express hierarchy
   on the dark ground instead of opacity changes on white type.
