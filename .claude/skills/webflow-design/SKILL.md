---
name: webflow-design
description: Webflow's visual-web-development marketing design system — a generous white canvas paired with a deep near-black (#080808) primary CTA color, punctuated by a five-stop chromatic accent system (purple, pink, blue, orange, green) used as full-bleed product-category card fills rather than button colors. Headlines run the proprietary WF Visual Sans Variable at a restrained 500/600 weight ceiling with negative tracking. Use when asked for a "Webflow style", Webflow-inspired UI, or a confident professional SaaS marketing page with color-blocked category cards.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/webflow/DESIGN.md
---

# Webflow Design System

Use this skill for visual-development, no-code, or professional B2B SaaS
marketing surfaces that want Webflow's restrained-black-plus-color-block
system, or for any explicit "Webflow style" request.

## Quick reference

- **Canvas**: `#ffffff` generous white — no dark mode on marketing.
- **Accent**: `#080808` deep near-black is the primary CTA color; a
  five-stop chromatic palette — purple `#7a3dff`, pink `#ed52cb`, blue
  `#3b89ff`, orange `#ff6b00`, green `#00d722` — appears only as full-fill
  product-category card backgrounds, never as button colors.
- **Type**: proprietary `WF Visual Sans Variable`, weight 500/600 ceiling
  (never 700+), with negative tracking at display sizes (-0.8px at 80px).
  Uppercase eyebrows use +1.5px positive tracking.
- **Corners**: tight `4px` on buttons and badges, `8px` on cards — never a
  pill CTA. Only icon containers use a full circle.
- **Layout anchor**: layered multi-stop drop-shadows on featured cards, and
  full-saturation category-color cards mapped to product areas (design,
  CMS, hosting, ecommerce).

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first — the Do's and Don'ts section
   is the fastest way to avoid misusing the chromatic accents as button
   colors, which this brand never does.
2. Pull exact values from `references/design-tokens.yaml` — colors, the
   type scale, spacing, radius scale, and component specs.
3. Reserve the five chromatic accents for full-fill category-card
   backgrounds; keep every CTA in near-black or white-outline.
4. Cap display weight at 600 — the brand never uses 700+ anywhere.
5. Use the tight 4px button radius and 8px card radius consistently;
   never round a CTA into a pill.
6. Layer multi-stop, low-opacity drop-shadows on featured cards rather than
   a single heavy shadow, for the brand's distinctive elevation feel.
