---
name: ferrari-design
description: Ferrari's marketing-site design system — a near-black cinematic canvas (#181818) lit by full-bleed hero photography, with Rosso Corsa red (#da291c) used scarcely as the single brand accent on CTAs, the Cavallino mark, and F1 race-position highlights. Type is FerrariSans at a restrained weight 500, corners stay sharp at 0px on every button and card, and an explicit 8px spacing ladder governs editorial pacing. Use when asked for a "Ferrari style", luxury-automotive marketing UI, or cinematic dark editorial layouts with a single red accent.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/ferrari/DESIGN.md
---

# Ferrari Design System

Use this skill when a task calls for Ferrari's cinematic-editorial luxury
aesthetic: automotive marketing pages, high-end product launches, or any
explicit "Ferrari style" request.

## Quick reference

- **Canvas**: `#181818` near-black (never pure black) — white-canvas bands
  appear only inside editorial contexts like preowned listings or pricing.
- **Accent**: `#da291c` Rosso Corsa red — used ONLY on primary CTAs, the
  Cavallino mark, and F1 race-position highlights. Never a section
  background or card fill.
- **Type**: single family FerrariSans at weight 500 for display (never
  bold), 400 for body; CTA and nav labels render uppercase with heavy
  positive tracking (1.4px / 0.65px).
- **Corners**: sharp `0px` on every CTA, card, and band — the brand's
  signature precision; pill geometry is reserved for small badges only.
- **Layout anchor**: full-bleed cinematic hero photography (car detail,
  trackside livery) fills the top of every major page; the explicit 8px
  spacing ladder (`xxxs` 4px through `super` 128px) governs editorial pacing.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` for the full rationale before writing
   CSS or components — the "Do's and Don'ts" section is the fastest way to
   avoid generic AI-slop dark themes.
2. Pull exact values from `references/design-tokens.yaml` (colors,
   typography scale, spacing scale, border-radius scale, component specs)
   rather than guessing hex codes or sizes.
3. Treat Rosso Corsa red as scarce — one primary CTA fill and the mark, not
   a decorative section color.
4. Lead every major section with a full-bleed cinematic photograph rather
   than illustration or gradient art; let the photography carry the depth
   instead of drop shadows.
5. Keep every CTA and card at `rounded.none` (0px) — never round or pill
   buttons; reserve pill shape for small badge chips only.
6. Keep display type at weight 500 with uppercase, heavily tracked button
   and nav labels — never bold the headline.
