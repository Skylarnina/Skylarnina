---
name: linear-design
description: Linear's marketing-site design system — near-black canvas (#010102), a single lavender-blue accent (#5e6ad2), a four-step dark surface ladder, negative-tracked display type, and product-screenshot-led layout. Use when building or reviewing UI that should read as a precise, dense, dark developer-tool marketing page, or when asked for a "Linear style", "Linear-inspired", or similar SaaS/dev-tool dark design.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/linear.app/DESIGN.md
---

# Linear Design System

Use this skill when a task calls for Linear's dark, product-led marketing
aesthetic: SaaS landing pages, dev-tool marketing sites, dashboards that
want a "software-craft documentation" feel, or any explicit "Linear style"
request.

## Quick reference

- **Canvas**: `#010102` (near-pure black, faint blue tint) — never true
  black, never light mode.
- **Accent**: `#5e6ad2` lavender-blue — used ONLY on brand mark, primary
  CTA, focus rings, and link emphasis. Never as a background or card fill.
- **Surface ladder**: canvas → surface-1 → surface-2 → surface-3 →
  surface-4, each a small step up in lightness, used for hierarchy instead
  of drop shadows.
- **Type**: two silent-swap sans families (Display for headings, Text for
  body) with aggressive negative letter-spacing on display sizes; free
  substitutes are Inter or Geist Sans, with JetBrains Mono / Geist Mono for
  code.
- **Corners**: 8px on buttons/inputs, 12px on cards, 16px on product
  screenshot panels — never pill-shaped CTAs.
- **Layout anchor**: product UI screenshots are the protagonist of every
  section; marketing chrome stays minimal.

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
3. Treat the lavender accent as scarce — if more than the CTA, brand mark,
   and focus states are lavender, dial it back.
4. Lead sections with a framed product screenshot or realistic UI mock
   rather than illustration or gradient art.
5. For light-mode or non-dark requests, this skill doesn't apply — it only
   documents Linear's dark marketing surface.
