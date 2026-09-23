---
name: bmw-design
description: BMW's corporate site design system — a measured, settled automotive-corporate interface, distinct from BMW M's motorsport-bombastic sub-brand. A light cream-tinted white canvas carries BMW corporate blue (#1c69d4) as the single primary CTA color, with dark navy hero bands framing model photography. BMW Type Next Latin sets the entire hierarchy across just two weights — heavy 700 display and Light 300 body — and every button/card stays rectangular at 0px radius. Use when asked for a "BMW style", "BMW-inspired UI", or a dealership-functional, corporate-automotive marketing/configurator page.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/bmw/DESIGN.md
---

# BMW Design System

Use this skill when a task calls for BMW's measured, corporate-automotive
aesthetic: dealership sites, vehicle configurators, model showcase grids, or
any explicit "BMW style" request (as distinct from the sportier BMW M skill).

## Quick reference

- **Canvas**: light — pure white (`#ffffff`) is the base surface, with a
  soft-grey card plate (`#fafafa`) behind model photos; dark navy
  (`#1a2129`) appears only inside hero bands, one per page.
- **Accent**: BMW corporate blue (`#1c69d4`) is the single primary action
  color. The M tricolor stripe (light blue → dark blue → red) only appears
  on M-model pages and badges — never in the main corporate CTA language.
- **Type**: BMW Type Next Latin at two weights only — heavy 700 (display,
  buttons, nav) and Light 300 (body). Weight 500 is deliberately absent.
- **Corners**: rectangular, 0px radius, on every button/card/input — the
  binary radius rule is rectangular-for-everything, circular only for icon
  buttons.
- **Layout anchor**: 4-up or 5-up model-card grids, each card a photo plate
  + title + uppercase "LEARN MORE ›" link — no hairline border needed.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` for the full rationale before writing
   CSS or components — the "Do's and Don'ts" section flags how this skill
   differs from BMW M's sportier corners and darker canvas.
2. Pull exact values from `references/design-tokens.yaml` (colors,
   typography scale, spacing scale, border-radius scale, component specs)
   rather than guessing hex codes or sizes.
3. Keep every button, card, and input at `{rounded.none}` (0px) — reserve
   circular shape exclusively for icon buttons and avatars.
4. Pair heavy 700 display type with Light 300 body copy; never introduce
   weight 500, and keep letter-spacing at 0 on paragraphs (no negative
   tracking, unlike Apple/Cal.com-style systems).
5. Reserve `{colors.surface-dark}` for hero bands only — the page rhythm
   depends on light → dark-hero → light contrast, not on a persistently
   dark canvas.
6. Keep the M tricolor stripe scoped to M-model contexts and motorsport
   dividers — never use it as a CTA fill in the main corporate flow.
