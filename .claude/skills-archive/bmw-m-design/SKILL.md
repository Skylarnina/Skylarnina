---
name: bmw-m-design
description: BMW M's motorsport marketing system — a near-pure black canvas carrying white BMW Type Next Latin headlines in confident UPPERCASE, with full-bleed automotive photography (track shots, cockpit detail, carbon fiber) supplying all the visual energy. The only brand color is the M tricolor stripe (light blue #0066b1, dark blue #1c69d4, red #e22718), used sparingly as a divider and never as a fill. Corners are almost always sharp (0px), body copy runs light-weight (300) against bold display (700), and buttons stay flat and rectangular. Use when asked for a "BMW M style", "BMW M-inspired UI", or a European-engineered, photography-led motorsport marketing page.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/bmw-m/DESIGN.md
---

# BMW M Design System

Use this skill for BMW M's motorsport-engineering marketing aesthetic: dark
automotive landing pages, performance-brand sites, or any explicit "BMW M
style" request. Distinct from BMW's own corporate site — BMW M is louder,
darker, and photography-led rather than corporate-calm.

## Quick reference

- **Canvas**: `#000000` near-pure black — no light mode, white type throughout.
- **Accent**: the M tricolor stripe (`#0066b1` → `#1c69d4` → `#e22718`) used
  only as a 4px divider/brand marker — never a button fill or background.
- **Type**: BMW Type Next Latin, UPPERCASE display at weight 700 paired with
  Light (300) body copy — the heavy/light contrast is the editorial signature.
- **Corners**: almost always `0px` (rectangular buttons and cards); the only
  exception is `9999px` full-circle icon buttons.
- **Layout anchor**: full-bleed automotive photography fills entire bands;
  chrome (nav, buttons, dividers) stays minimal and gets out of the way.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first — the Do's and Don'ts section is
   the fastest way to avoid a generic dark-automotive template.
2. Pull exact values from `references/design-tokens.yaml` rather than
   guessing hex codes, weights, or spacing.
3. Lead every section with full-bleed photography (cars, cockpit, carbon
   detail) — chrome should never compete with the image for attention.
4. Set display headlines UPPERCASE at weight 700; keep body copy sentence-case
   at weight 300 (Light) — never blur that weight contrast.
5. Reserve the M tricolor stripe for brand-identity moments only (dividers,
   badges, motorsport chrome) — never as a CTA or surface color.
6. Keep buttons and cards at `0px` radius; use `9999px` only for circular
   icon buttons like carousel arrows.
