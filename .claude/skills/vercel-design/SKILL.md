---
name: vercel-design
description: Vercel's developer-platform marketing design system — a stark near-white canvas paired with near-black ink, where the only decoration is a multi-stop mesh gradient (blue-cyan / violet-pink / coral-amber) reserved for hero-scale atmospheric backdrops. Headlines use the custom Geist sans at weight 600 with aggressive negative tracking, paired with Geist Mono for technical labels and terminal/code mockups. Use when asked for a "Vercel style", Vercel-inspired UI, or a precise, engineered developer-platform marketing page.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/vercel/DESIGN.md
---

# Vercel Design System

Use this skill for developer-platform, cloud-infrastructure, or dev-tool
marketing surfaces that want Vercel's calm, engineered stark-white system,
or for any explicit "Vercel style" request.

## Quick reference

- **Canvas**: `#fafafa` (98% white) for the page body, `#ffffff` for cards,
  `#f5f5f5` for occasional inset regions — no dark mode on marketing.
- **Accent**: `#171717` near-black ink is the only conversion color; the
  brand's signature decoration is a multi-stop mesh gradient (develop
  blue→teal, preview violet→pink, ship coral→amber) used ONLY at hero scale.
- **Type**: `Geist` weight 600 for display with aggressive negative
  tracking (-2.4px at 48px), weight 400/500 for body/buttons; `Geist Mono`
  for code, terminal mockups, and eyebrow labels. Substitutes: Inter + JetBrains Mono.
- **Corners**: `100px` pill for marketing-scale CTAs, tight `6px` for
  nav-scale buttons, `8-16px` for cards.
- **Layout anchor**: subtle stacked shadows (never a single heavy drop),
  polarity-flipped dark bands between light sections, and the mesh gradient
  as the sole atmospheric effect.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first, especially Do's and Don'ts —
   it's the fastest way to avoid a generic dark-SaaS or gradient-overload
   look that isn't actually Vercel's restrained voice.
2. Pull exact values from `references/design-tokens.yaml` — colors, the
   type scale, spacing, radius scale, and full component specs.
3. Treat the mesh gradient as scarce: hero backdrop only, never
   miniaturized to an icon or reduced to a single color swatch.
4. Use stacked, low-opacity shadows (multiple small offsets) rather than a
   single heavy drop-shadow for card elevation.
5. Keep the geometric sans at weight 600 maximum for display — the brand
   never goes to 700+.
6. Reserve Geist Mono strictly for code, terminal mockups, and section
   eyebrows; never set body paragraphs in mono.
