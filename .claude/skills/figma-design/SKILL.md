---
name: figma-design
description: Figma's marketing-site design system — a strict black-and-white editor frame (pure black CTAs, pure white canvas, figmaSans variable type) that repeatedly drops into oversized pastel color-block panels — lime, lilac, cream, mint, pink, coral, navy — spanning full content width with 24px corners. Every button is a pill, every icon button a circle, and figmaMono handles uppercase eyebrows only. Use when asked for a "Figma style", "Figma-inspired UI", or a confident monochrome SaaS layout punctuated by giant sticky-note-style color panels.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/figma/DESIGN.md
---

# Figma Design System

Use this skill when a task calls for Figma's editorial black-and-white
marketing aesthetic punctuated by oversized pastel storytelling panels:
design-tool marketing pages, creative-software landing pages, or any
explicit "Figma style" request.

## Quick reference

- **Canvas**: pure white (`#ffffff`) with pure black (`#000000`) as the
  system primary — every CTA, headline, and footer link is monochrome.
- **Accent(s)**: no single brand color — instead a rotating family of
  pastel **color-block sections** (lime, lilac, cream, mint, pink, coral,
  navy) that each take over a full-width panel between white bands; a
  single saturated magenta is reserved for one-shot promo CTAs.
- **Type**: `figmaSans` variable sans at unusually fine weight steps (320,
  330, 340, 480, 540, 700) with aggressive negative tracking on display
  sizes; `figmaMono` uppercase for eyebrows/captions only, never body.
- **Corners**: pill (`50px`) on every text CTA, full circle on icon
  buttons — no square buttons anywhere; cards and color-block panels round
  at 24px.
- **Layout anchor**: color-block storytelling sections that span full
  content width and alternate with white canvas — the white return between
  blocks is what makes each one read as deliberate.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` for the full rationale before writing
   CSS or components — the "Do's and Don'ts" section shows how to avoid
   over-coloring the page.
2. Pull exact values from `references/design-tokens.yaml` (colors,
   typography scale, spacing scale, border-radius scale, component specs)
   rather than guessing hex codes or sizes.
3. Keep the chrome (nav, footer, default CTA) strictly black-and-white;
   introduce color only inside a full-width color-block section.
4. When starting a new story section, pick exactly one `block-*` color and
   let it span the full content width with 24px corners and generous
   (48px) interior padding — then return to white canvas before the next
   section.
5. Make every CTA a pill and every icon button a circle; never ship a
   square button.
6. Reserve the magenta accent for a single promotional CTA per page — never
   two in the same viewport.
