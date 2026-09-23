---
name: revolut-design
description: Revolut's marketing-site design system — a two-mode canvas that switches full-bleed between true black storytelling bands and white catalogue bands, giant Aeonik Pro display headlines (20-136px, weight 500, tight negative tracking), and a "white pill on black" primary CTA rather than the brand's own cobalt-violet (#494fdf), which is reserved for featured plan cards. A wide secondary palette (teal, pink, light-green, warning orange) lives only inside product mockups, never on buttons. Use when asked for a "Revolut style", Revolut-inspired UI, or a fintech-meets-product-brochure marketing page.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/revolut/DESIGN.md
---

# Revolut Design System

Use this skill for consumer fintech marketing pages, banking/payments
product sites, or any page that wants Revolut's oversized-headline,
black-and-white-with-a-cobalt-stamp brochure feel.

## Quick reference

- **Canvas**: true black (`#000000`) for storytelling/hero bands, white
  (`#ffffff`) for catalogue bands (FAQ, comparisons, downloads) — the two
  switch in full-bleed bands, never blended.
- **Accent**: cobalt violet `#494fdf` is scarce — reserved for the featured
  plan card, the wordmark, and secondary CTAs on white. The actual primary
  CTA is a **white pill with black text** sitting on the dark canvas.
- **Type**: Aeonik Pro (weight 500) for every display size 20-136px with
  tight `lineHeight: 1.0` and heavy negative tracking on the largest sizes;
  Inter for all body/button/caption text with slight positive tracking.
- **Corners**: every button and pill uses `rounded.full`; content cards use
  `rounded.lg` (20px); inputs and small chips use `rounded.md` (12px).
- **Layout anchor**: full-bleed product mockups (phone, card, terminal) are
  shown edge-to-edge inside dark sections with no caption overlay — the
  asset IS the section.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first — the Do's and Don'ts section
   flags the two most common mistakes: turning the eight-color secondary
   palette into button colors, and using cobalt violet as a broad theme
   instead of a scarce stamp.
2. Pull exact values from `references/design-tokens.yaml` rather than
   guessing hex codes or sizes.
3. Default the primary CTA to a white pill on the black canvas, not the
   cobalt accent — cobalt is reserved for the featured plan card and
   secondary CTAs on white bands.
4. Keep the eight saturated accent colors (teal, pink, light-green, warning
   orange, etc.) inside product illustrations and mockups only — never as
   button surfaces.
5. Switch entire sections between black and white; avoid mid-grey
   backgrounds or gradual tonal transitions.
6. Render hero and product photography full-bleed with no surrounding
   chrome or overlay text.
