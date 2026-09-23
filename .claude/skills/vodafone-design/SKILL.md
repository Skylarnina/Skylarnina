---
name: vodafone-design
description: Vodafone's telecom marketing design system — a two-band page rhythm alternating near-black hero photography bands with colossal uppercase display headlines and calm white content bands, anchored by the brand's scarlet red (#e60000) as the single accent color. Headlines run the proprietary Vodafone display sans at an impossibly heavy weight 800, and every interactive control is a generously rounded 60px pill. Use when asked for a "Vodafone style", Vodafone-inspired UI, or a bold campaign-poster telecom marketing page.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/vodafone/DESIGN.md
---

# Vodafone Design System

Use this skill for telecom, mobile-carrier, or "big brand campaign poster"
marketing surfaces that want Vodafone's heroic editorial-photography voice,
or for any explicit "Vodafone style" request.

## Quick reference

- **Canvas**: `#ffffff` white for content bands, `#25282b` near-black ink
  for hero and footer bands — a strict two-band rhythm, no in-between grays.
- **Accent**: `#e60000` Vodafone Red is the single brand accent — every
  primary CTA pill and the iconic speechmark logo orb. No second accent.
- **Type**: proprietary `Vodafone` display sans, weight 800 UPPERCASE for
  hero scale (up to 144px), dropping to weight 300 for calmer sub-displays.
  Substitutes: Inter weight 800 (hero) / weight 300 (sub-display).
- **Corners**: `60px` pill on every CTA — the brand has not used a square
  button in years. Cards stay gentler at `6px`.
- **Layout anchor**: full-bleed editorial photography under a colossal
  uppercase headline, followed by calm white story-card content; the red
  speechmark-logo orb acts as the page's visual anchor.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first — the Do's and Don'ts section
   is the quickest way to avoid a generic telecom look that misses the
   brand's uppercase-billboard voice.
2. Pull exact values from `references/design-tokens.yaml` — colors, the
   full type scale, spacing, radius scale, and component specs.
3. Keep the palette to red + near-black + white/grayscale — resist adding
   a second accent even for status callouts.
4. Set hero headlines in weight 800 UPPERCASE with tight negative tracking;
   drop to weight 300 for the calmer sub-display voice that follows.
5. Round every interactive control to the 60px pill; never render a CTA as
   a square rectangle.
6. Pair full-bleed editorial photography with the massive headline overlay
   in the hero, then let the page settle into a calm white content rhythm.
