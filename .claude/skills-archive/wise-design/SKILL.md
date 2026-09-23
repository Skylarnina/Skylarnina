---
name: wise-design
description: Wise's fintech marketing system — a vivid lime-green CTA accent (#9fe870) set against a sage-tinted canvas (#e8ebe6) and near-black ink, carried by an unusually heavy proprietary display sans (Wise Sans, weight 900 up to 126px) paired with Inter for everything else. Every card and button shares a friendly 24px pill-rectangle radius, and the brand's signature interactive component is a currency-converter card on the hero. Use when asked for a "Wise style", "Wise-inspired UI", or a calm, Scandinavian-magazine-feeling money-transfer/fintech marketing page rather than a typical cold-blue bank interface.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/wise/DESIGN.md
---

# Wise Design System

Use this skill when a task calls for Wise's calm, lime-accented fintech
aesthetic: money-transfer/remittance marketing pages, banking-adjacent
products that want to avoid the typical "cold blue bank" feel, or any
explicit "Wise style" request.

## Quick reference

- **Canvas**: pale sage-tinted (`#e8ebe6`) hero surface with pure-white
  (`#ffffff`) cards floating on top — surface contrast, not shadow,
  carries elevation.
- **Accent**: a single lime-green (`#9fe870`) CTA color — the brand's
  sole identity color, with no second accent.
- **Type**: proprietary Wise Sans at weight 900 for hero display (64-126px)
  paired with Inter at weight 600 for everything smaller — the contrast
  between chunky display and neutral utility type is the brand's
  typographic story.
- **Corners**: 24px is the canonical radius for every button and card —
  generous and friendly, never sharp.
- **Layout anchor**: a currency-converter card on the hero (from/to
  amount inputs plus currency selectors) is the brand's signature
  interactive component.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first — the "Do's and Don'ts"
   section is the fastest way to avoid a generic fintech look.
2. Pull exact values from `references/design-tokens.yaml` (colors,
   typography scale, spacing scale, border-radius scale, component specs)
   instead of guessing hex codes or sizes.
3. Reserve lime green strictly for the primary CTA — never introduce a
   second brand accent color.
4. Set hero headlines in Wise Sans (or Inter/Manrope at weight 900 as a
   substitute) — never render the hero lighter than weight 900.
5. Round every button and card to 24px; cycle page surfaces from the
   sage canvas to white cards to carry elevation through contrast alone.
6. Use the full semantic palette (positive/warning/negative) for
   in-product status states — never repurpose the brand's lime green as a
   success indicator, since it is reserved for the CTA.
