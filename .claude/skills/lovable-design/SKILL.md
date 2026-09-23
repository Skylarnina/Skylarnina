---
name: lovable-design
description: Lovable's marketing-site design system — a warm parchment-cream canvas (#f7f4ed, never white), near-black charcoal text and dark-button surfaces, and Camera Plain Variable, a humanist display face set with aggressive negative tracking at large sizes. Every gray on the page is derived from a single charcoal hue at different opacities rather than distinct hex values, borders replace shadows for containment, and pill radius (9999px) is reserved for icon/action buttons only. Use when asked for a "Lovable style", Lovable-inspired UI, or a warm, analog-feeling AI-builder marketing page that should read as approachable rather than clinical.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/lovable/DESIGN.md
---

# Lovable Design System

Use this skill when a task calls for Lovable's warm, notebook-like marketing
aesthetic: AI product-builder landing pages, developer-tool sites that want
to feel approachable rather than cold, or any explicit "Lovable style"
request.

## Quick reference

- **Canvas**: `#f7f4ed` warm parchment cream — never pure white; used for
  page background, card surfaces, and even most button surfaces.
- **Accent**: no saturated brand color — depth and hierarchy come from a
  single charcoal (`#1c1c1c`) modulated at different opacities (3%, 4%, 40%,
  82-83%, 100%), not from separate hex values.
- **Type**: Camera Plain Variable, a humanist variable sans with rounded
  terminals; weight 600 with tight negative tracking (-0.9px to -1.5px) at
  display sizes, weight 400 everywhere else — 600 is the maximum weight used.
- **Corners**: 6px standard on buttons/inputs, 12px on cards/images, 16px on
  large containers, full pill (9999px) reserved for icon buttons and action
  pills only.
- **Layout anchor**: a signature multi-layer inset shadow on dark buttons
  gives a tactile "pressed into the surface" feel instead of a floating
  drop-shadow.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first — the "Do's and Don'ts" section
   is the fastest way to avoid a generic white-canvas AI-tool look.
2. Pull exact values from `references/design-tokens.yaml` rather than
   guessing hex codes or sizes — the opacity-derived gray scale is the
   system's signature and should be used exactly as specified.
3. Default every background to cream (`#f7f4ed`), never pure white; use
   `#eceae4` borders instead of shadows for card containment.
4. Reserve full-pill radius for icon buttons, voice/plan-mode toggles, and
   action pills — rectangular CTAs stay at 6px.
5. Apply the signature inset shadow to dark buttons rather than a
   conventional drop shadow — it's the system's most distinctive detail.
6. Keep the weight system narrow: 400 for body/UI/links/buttons, 600 for
   headings — never use bold (700).
