---
name: claude-ai-design
description: Anthropic's Claude.com marketing system — a warm tinted-cream canvas (#faf9f5, never pure white), a slab-serif display face (Copernicus/Tiempos Headline) set at weight 400 with negative tracking, and warm coral (#cc785c) as the single primary-action color. Dark navy product surfaces (code-editor mockups, model-comparison cards) alternate with cream feature cards to create an editorial, literary-magazine pacing rather than a typical cool-toned AI-SaaS look. Use when asked for a "Claude style", "Claude.ai-inspired UI", "Anthropic style", or a warm, editorial AI-product marketing page.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/claude/DESIGN.md
---

# Claude (Anthropic) Design System

Use this skill for Claude.com's warm, editorial AI-product marketing
aesthetic: AI-tool landing pages, developer-platform marketing sites, or
any explicit "Claude style" / "Anthropic style" request. It deliberately
counter-positions against the cool blue/slate look most AI brands use.

## Quick reference

- **Canvas**: `#faf9f5` tinted cream — warm and deliberately not pure white
  or cool gray; dark navy (`#181715`) surfaces appear for product mockups,
  callouts, and the footer.
- **Accent**: coral (`#cc785c`) as the single primary-action color — scarce
  on individual buttons, generous on full-bleed coral callout cards.
- **Type**: slab-serif Copernicus/Tiempos Headline (weight 400, negative
  tracking) for every display headline, paired with humanist StyreneB/Inter
  for body, UI, and code in JetBrains Mono.
- **Corners**: hierarchical — `8px` buttons/inputs, `12px` content cards,
  `16px` the hero illustration container, pill for badges.
- **Layout anchor**: real product chrome (code-editor mockups, terminal
  panels, model-comparison cards) on dark navy cards alternating with cream
  feature cards for editorial pacing.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first, especially Do's and Don'ts —
   the biggest risk is defaulting to pure white or cool blue instead of the
   warm cream/coral pairing.
2. Pull exact values from `references/design-tokens.yaml` rather than
   guessing hex codes, weights, or spacing.
3. Set every display headline in the serif face at weight 400 with negative
   letter-spacing; keep body copy in the humanist sans — never swap the
   serif into body text or vice versa.
4. Reserve coral for primary CTAs and full-bleed coral callout cards; don't
   scatter it as a general accent elsewhere.
5. Show real product chrome (code windows, model-comparison cards) on dark
   navy cards rather than abstract illustrations.
6. Alternate surface modes band-to-band (cream → cream-card → dark-mockup →
   cream → coral-callout → dark-footer) instead of repeating one surface.
