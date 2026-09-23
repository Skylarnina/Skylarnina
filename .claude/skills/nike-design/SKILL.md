---
name: nike-design
description: Nike's commerce system is built on extreme typographic contrast — towering uppercase Futura display lockups (up to 96px, line-height 0.9) burned directly into full-bleed campaign photography, over a near-monochrome retail chrome of pill-shaped black CTAs, soft-gray "#f5f5f5" product staging, and zero-radius product cards. There is no decorative color: chromatic energy is reserved for photography and the rare sale-price red. Use when asked for a "Nike style", "Nike-inspired UI", or a photography-first athletic e-commerce/PLP-PDP marketing page.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/nike/DESIGN.md
---

# Nike Design System

Use this skill when a task calls for Nike's photography-first commerce
aesthetic: athletic e-commerce PLP/PDP pages, campaign hero editorial, or
any explicit "Nike style" request.

## Quick reference

- **Canvas**: pure white `#ffffff`, with `soft-cloud` (`#f5f5f5`) as the
  universal "stage" gray behind every product photograph — the system's
  most-used non-white surface.
- **Accent**: none, by design — pure black (`#111111`) and white carry
  ~95% of the chrome; `sale` red (`#d30005`) is the only non-neutral color
  in retail chrome, reserved strictly for discounted price text.
- **Type**: `display-campaign` — Nike Futura ND at 96px, uppercase, weight
  500, line-height 0.9 — burned into hero photography; everything else runs
  Helvetica Now Display/Text at 12–32px.
- **Corners**: zero radius on every card, campaign tile, and container;
  every CTA, filter chip, and badge is a `{rounded.lg}` (30px) pill instead.
- **Layout trait**: product photography is full-bleed and unpadded, staged
  on `soft-cloud`; the only "shadow" in the system is a 1px inset hairline
  on sticky bars.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` for the full rationale before writing
   CSS or components — the "Do's and Don'ts" section is the fastest way to
   avoid introducing decorative color or shadows.
2. Pull exact values from `references/design-tokens.yaml` (colors,
   typography scale, spacing scale, border-radius scale, component specs)
   rather than guessing hex codes or sizes.
3. Reserve `typography.display-campaign` (96px uppercase Futura) strictly
   for editorial campaign hero lockups — never for section headers or
   product titles.
4. Stage every product photograph on `colors.soft-cloud` — never on white
   or a colored background.
5. Keep every CTA pill-shaped at `rounded.lg` (30px); never introduce a
   square or sharp-cornered button.
6. Use `colors.sale` only on price-row text — never as a badge background
   or decorative chrome.
