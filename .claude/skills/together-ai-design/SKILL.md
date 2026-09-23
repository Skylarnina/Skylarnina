---
name: together-ai-design
description: Together AI's marketing-site design system — an AI cloud-infrastructure brand that alternates a near-black (#010120) hero/research band with a bright white product/pricing band, tied together by a single three-color orange-magenta-periwinkle gradient ribbon and an uppercase monospace eyebrow face. Use when asked for a "Together AI style", "Together.ai-inspired UI", or a developer-infrastructure marketing page that pairs a sentence-case display sans with all-caps mono technical labels.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/together.ai/DESIGN.md
---

# Together AI Design System

Use this skill when a task calls for Together AI's dual-surface, gradient-
ribbon developer-infrastructure look: AI/GPU-cloud marketing pages, inference
platform pricing pages, or any explicit "Together AI style" request.

## Quick reference

- **Canvas**: alternates aggressively between `#010120` (near-black hero/
  research bands) and `#ffffff` (white product/pricing bands) — no
  in-between greys except a single hairline tone for table headers.
- **Accent**: a single black (`#000000`) CTA pill carries every conversion
  target; the only decoration is a fixed three-stop gradient (orange →
  magenta → periwinkle) used at hero scale, never as a small swatch.
- **Type**: a custom geometric display sans ("The Future", substitute Inter)
  at weight 500 with negative tracking for headlines/body, paired with an
  uppercase monospace face ("PP Neue Montreal Mono") for every eyebrow,
  button label, and table header.
- **Corners**: a tight, near-universal 4px radius on cards/buttons; the only
  full pill in the system is the floating chat-launcher orb.
- **Layout anchor**: a giant `together.ai` wordmark banner, tinted toward the
  hairline color, closes every long page as a stencil-like sign-off.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first — the two-face typographic
   contrast (sentence-case display vs. all-caps mono) is the brand's
   clearest signal and easy to blur if skipped.
2. Pull exact values from `references/design-tokens.yaml` rather than
   guessing hex codes or sizes.
3. Cycle page surfaces in the dark → white → dark rhythm; use surface
   contrast, not shadows, to carry elevation between sections.
4. Treat the three-stop gradient as one fixed object — never crop it to a
   single color, reorder its stops, or shrink it to icon size.
5. Keep every button and card at the canonical 4px radius; reserve the full
   pill shape for the floating chat-launcher orb only.
6. Set eyebrows, button labels, and table headers in the uppercase mono face;
   keep headlines and body copy in sentence case on the display sans.
