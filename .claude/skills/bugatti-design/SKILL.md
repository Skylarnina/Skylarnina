---
name: bugatti-design
description: Bugatti's ultra-austere luxury-automotive marketing system — a near-pure black canvas, white uppercase Bugatti Display headlines set with wide letter-spacing (2-6px), a serif Bugatti Text Regular for body copy, and a monospace Bugatti Monospace for buttons and captions. There is no accent color beyond a rare ice-blue link tone, no shadows, no gradients, and the primary CTA is a fully transparent pill with a hairline outline — photography and typography alone carry the brand. Use when asked for a "Bugatti style", "Bugatti-inspired UI", or an extremely minimal, monochrome luxury-automotive marketing page.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/bugatti/DESIGN.md
---

# Bugatti Design System

Use this skill for Bugatti's hyper-minimal, quietly-expensive marketing
aesthetic: hyper-luxury automotive pages, ultra-restrained editorial sites,
or any explicit "Bugatti style" request. It is the most austere brand in the
luxury-automotive set — no accent color, no chrome, only photography and
precisely-tracked type.

## Quick reference

- **Canvas**: `#000000` pure black — no light mode, white type throughout.
- **Accent**: effectively none — the only non-monochrome color is a
  desaturated ice-blue (`#c3d9f3`) reserved for rare inline links.
- **Type**: a strict trinity — Bugatti Display (uppercase, wide-tracked
  2-6px, weight 400 only) for headlines/wordmark, Bugatti Text Regular (a
  serif) for body copy, Bugatti Monospace (uppercase, tracked) for buttons,
  nav, and captions. Never bold, anywhere.
- **Corners**: `0px` on everything except buttons, which are fully
  transparent `9999px` pills with a 1px white outline.
- **Layout anchor**: enormous whitespace (`120px` between sections) framing
  full-bleed automotive photography — less is the entire strategy.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first, especially Do's and Don'ts —
   the biggest risk is over-decorating what should stay austere.
2. Pull exact values from `references/design-tokens.yaml` rather than
   guessing hex codes, tracking, or spacing.
3. Keep the three-typeface split rigid: Display only for headlines/wordmark,
   Text Regular (serif) only for paragraphs, Monospace only for buttons,
   nav, and captions — never mix them.
4. Never introduce bold weight or a second accent color; emphasis comes from
   size, tracking, and generous whitespace, not weight or color.
5. Keep the primary CTA transparent with a hairline outline and pill radius;
   every other shape (cards, photos, inputs) stays sharp at `0px`.
6. Let full-bleed photography and large empty black space carry each
   section — resist the urge to fill space with extra chrome.
