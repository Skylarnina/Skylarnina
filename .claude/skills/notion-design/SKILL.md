---
name: notion-design
description: Notion's marketing-site design system — a deep navy hero band decorated with brand-colored sticky-note dots, a signature purple pill CTA (#5645d4), and a rich pastel palette of feature-card tints (peach, rose, mint, lavender, sky, yellow) that echo the colorful database properties of the live product. Buttons stay rectangular (8px radius, never pill) while cards round to 12px, all set in the Notion Sans (Inter-based) typeface. Use when asked for a "Notion style", "Notion-inspired UI", or a confident, illustration-rich all-in-one-workspace marketing page.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/notion/DESIGN.md
---

# Notion Design System

Use this skill when a task calls for Notion's confident, illustration-rich
workspace-brand aesthetic: productivity SaaS marketing pages, all-in-one-tool
landing pages, or any explicit "Notion style" / "Notion-inspired" request.

## Quick reference

- **Canvas/background**: pure white (`#ffffff`) body with a deep navy
  (`#0a1530`) hero band reserved for the top-of-page moment.
- **Accent color(s)**: signature purple (`#5645d4`) is the ONLY primary CTA
  color; a wide brand-color spectrum (pink, orange, teal, green, yellow,
  brown) lives inside pastel feature-card tints, never on buttons.
- **Type approach**: Notion Sans (Inter-based) across every UI surface —
  negative tracking on display sizes, weight 600 headlines over weight 400
  body.
- **Corner-radius feel**: buttons/inputs are rectangular at 8px (never
  pill); cards consistently round to 12px; pill shape is reserved for
  status badges and tab chips only.
- **Distinctive layout trait**: a real Notion workspace UI mockup card
  breaks out of the navy hero band with a deep diffuse drop shadow, and
  feature sections cycle through pastel-tinted cards (peach, rose, mint,
  lavender, sky, bold yellow) echoing live product database colors.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` for the full rationale before writing
   CSS or components — the "Do's and Don'ts" section clarifies why buttons
   stay rectangular while cards round more generously.
2. Pull exact values from `references/design-tokens.yaml` (colors,
   typography scale, spacing scale, border-radius scale, component specs)
   rather than guessing hex codes or sizes.
3. Treat purple as scarce — reserve it for the dominant CTA only; use
   link-blue for inline text links and pastel tints for feature-card fills.
4. Anchor hero sections with a navy band plus an embedded product-UI mockup
   card carrying a deep drop shadow, rather than illustration or gradient art.
5. Cycle pastel card tints across feature sections to echo the live
   product's colorful database properties, but keep buttons rectangular.
6. For a non-navy, non-pastel request, this skill doesn't apply cleanly —
   it documents Notion's specific illustration-rich marketing surface.
