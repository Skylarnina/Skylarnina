---
name: tesla-design
description: Tesla's marketing-site design system — a radically subtracted digital showroom where full-viewport cinematic car photography carries all the emotional weight and the UI is almost invisible. A single Electric Blue (#3E6AE1) marks the only primary CTA, three grays cover the entire text hierarchy, and Universal Sans (Display + Text) runs at just two weights (400/500) with normal — never negative — letter-spacing. Use when asked for a "Tesla style", "Tesla-inspired UI", or an extremely minimal, photography-first automotive/product marketing page with near-zero decoration.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/tesla/DESIGN.md
---

# Tesla Design System

Use this skill when a task calls for Tesla's radically minimal,
photography-first marketing aesthetic: automotive/hardware showroom
pages, product-launch sites that want near-zero decoration, or any
explicit "Tesla style" request.

## Quick reference

- **Canvas**: pure white (`#FFFFFF`) as the dominant surface, punctuated
  by full-viewport (100vh) cinematic car photography — no gradients, no
  patterns, no shadows anywhere.
- **Accent**: a single Electric Blue (`#3E6AE1`) reserved exclusively for
  the primary CTA ("Order Now") and matching promotional text — the only
  chromatic color in the entire interface.
- **Type**: Universal Sans Display (hero titles) plus Universal Sans Text
  (everything else), only weights 400/500, always "normal" letter-
  spacing — never negative tracking, never bold.
- **Corners**: 4px on nearly every button, ~12px on the rare rounded
  category card, 0px everywhere else — sharp edges are the default.
- **Layout anchor**: one full-viewport photograph per section, a floating
  frosted-glass nav with no visible background at rest, and zero
  box-shadows anywhere in the interface.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first — the "Do's and Don'ts"
   section is the fastest way to avoid over-designing what should be an
   almost-invisible UI.
2. Pull exact values from `references/design-tokens.yaml` (colors,
   typography scale, spacing scale, border-radius scale, component specs)
   instead of guessing hex codes or sizes.
3. Let photography carry every section — build full-viewport (100vh)
   hero blocks around cinematic product photography rather than
   decorative UI chrome.
4. Use Electric Blue for one purpose only: the primary CTA. Never apply
   it decoratively or as a background.
5. Keep every border-radius at 4px (buttons) or 0px (nearly everything
   else); never introduce pill buttons or large radii.
6. Never add a box-shadow, gradient, or border for separation — use
   spacing and photography-driven contrast instead.
