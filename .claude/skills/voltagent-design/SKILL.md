---
name: voltagent-design
description: Voltagent's AI agent engineering platform design system — an unrelenting near-black canvas (#101010, no light mode) broken only by a single electric-green accent (#00d992) and hairline-bordered feature cards with no shadows. Type pairs sentence-case Inter for narrative with SF Mono for inline code, command snippets, and uppercase tracked eyebrows, giving the page a "polished documentation that also sells something" feel. Use when asked for a "Voltagent style", Voltagent-inspired UI, or a calm, hairline-bordered dark developer-tool marketing page.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/voltagent/DESIGN.md
---

# Voltagent Design System

Use this skill for AI-agent, developer-tooling, or documentation-flavored
marketing surfaces that want Voltagent's dark, hairline-bordered restraint,
or for any explicit "Voltagent style" request.

## Quick reference

- **Canvas**: `#101010` near-black — the only page surface, no light mode
  counterpart anywhere on the marketing site.
- **Accent**: `#00d992` electric green is the sole brand color — every
  CTA, status pill, and the lightning-bolt logo glyph. Never used as a body
  fill.
- **Type**: Inter (sentence-case) for display/body/buttons, SF Mono for
  code blocks, command snippets, and uppercase-tracked eyebrow labels
  (`2.52px` tracking at 14px). Hero display sits at a calm weight 400.
- **Corners**: tight `6px` on buttons, `8px` on cards — never a pill except
  for inline status tags (`9999px`).
- **Layout anchor**: hairline-bordered feature cards (1px solid, no fill,
  no shadow) are the primary chrome; a rare dashed divider and green-glow
  border mark section rhythm.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first — the Do's and Don'ts section
   is the fastest way to avoid a generic gradient-heavy dark-AI-startup
   look that isn't actually this restrained.
2. Pull exact values from `references/design-tokens.yaml` — colors, the
   type scale, spacing, radius scale, and component specs.
3. Keep the electric green scarce — CTA, status pill, and logo glyph only;
   never a body-text fill or a large surface color.
4. Build every card from a 1px hairline border on the dark canvas rather
   than a shadow or fill — that's the brand's entire elevation system.
5. Pair sentence-case Inter for narrative with SF Mono for anything
   code-shaped, and set uppercase eyebrows in Inter weight 600 with wide
   positive tracking, not a separate display face.
6. Don't introduce a light-mode counterpart — the brand is dark-canvas
   only.
