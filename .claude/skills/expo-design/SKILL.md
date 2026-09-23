---
name: expo-design
description: Expo's React Native developer-platform marketing system — a pure white canvas with a soft sky-blue gradient atmosphere behind the hero only, near-black ink body/display text, and pure black (#000000) as the single primary-CTA color. A small blue (#0d74ce) is reserved strictly for inline text links, never CTAs. Inter carries every text role at modest weights (display 600, body 400) with JetBrains Mono on all code surfaces, and the page's signature visual is a centered MacBook-plus-iPhone device-mockup hero showing real Expo product UI. Use when asked for an "Expo style", "Expo-inspired UI", or a quietly confident developer-platform marketing page.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/expo/DESIGN.md
---

# Expo Design System

Use this skill for Expo's quietly confident React Native developer-platform
aesthetic: dev-tool landing pages, CLI/SDK marketing sites, or any explicit
"Expo style" request. It is minimal and editorial rather than loud —
brand voltage comes from real product screenshots, not color.

## Quick reference

- **Canvas**: pure white, with a soft sky-blue gradient wash reserved for
  the hero band only — never repeated elsewhere on the page.
- **Accent**: pure black (`#000000`) is the only primary-CTA color; a
  scarce blue (`#0d74ce`) marks inline body links only, never buttons.
- **Type**: Inter as the single sans family (display weight 600, body 400,
  negative tracking on display), paired with JetBrains Mono for every code
  surface.
- **Corners**: compact developer-ergonomic radii — `8px` CTAs and inputs,
  `12px` cards, `16px` the device-mockup card; pill radius is reserved for
  badges only, never buttons.
- **Layout anchor**: a centered MacBook + iPhone device-mockup composite
  showing real Expo product surfaces (EAS dashboard, Expo Go) is the
  page's defining chrome.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first, especially Do's and Don'ts —
   the biggest risk is drifting toward a saturated brand color or pill
   CTAs.
2. Pull exact values from `references/design-tokens.yaml` rather than
   guessing hex codes, weights, or spacing.
3. Keep black as the only CTA fill; use the blue text-link color solely
   for inline links inside body copy.
4. Anchor the hero with a device-mockup composite (or equivalent framed
   product screenshot) rather than illustration — it's the brand's central
   visual signature.
5. Render every code block or IDE mockup in JetBrains Mono on the dark
   surface color (`#171717`), never on the white canvas.
6. Keep the sky-blue gradient atmosphere confined to the hero; every other
   section stays flat white or flips fully to the dark surface for
   contrast (feature-card-dark, code blocks, featured pricing).
