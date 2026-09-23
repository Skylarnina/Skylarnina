---
name: superhuman-design
description: Superhuman's marketing-site design system — a three-canvas rhythm that opens on an indigo-navy (#1b1938) editorial hero with a violet-sky backdrop and a half-bleed portrait subject, flips to a white content body with warm-grey ink, and closes every page on a deep-teal CTA band (#0e3030). Type is a proprietary variable sans at unusual sub-default weights (460/540/600) with tight leading. Use when asked for a "Superhuman style", "Superhuman-inspired UI", or a high-end, editorial-feeling productivity/email SaaS marketing page.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/superhuman/DESIGN.md
---

# Superhuman Design System

Use this skill when a task calls for Superhuman's editorial, high-end
productivity-SaaS look: email/calendar/workflow marketing pages, premium
productivity-tool landing pages, or any explicit "Superhuman style" request.

## Quick reference

- **Canvas**: three-part rhythm — indigo navy (`#1b1938`) hero, white
  (`#ffffff`) body, deep teal (`#0e3030`) closing CTA band on every page.
- **Accent**: pale violet (`#c9b4fa`) for the hero's pill CTA only; indigo
  navy fills the primary rounded-rectangle CTA and the featured pricing tier.
- **Type**: **Super Sans VF**, a variable sans at sub-default weights (460,
  540, 600) with tight 0.96 line-height on display and negative tracking —
  substitute with Inter Variable at the same weight values.
- **Corners**: 8px rounded-rectangle CTAs everywhere in the body; the hero CTA
  alone is a full pill.
- **Layout anchor**: a half-bleed portrait subject (person at twilight,
  looking off-frame) anchors the hero; every page resolves in a deep-teal
  closing band.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first — the three-canvas rhythm and the
   closing-teal-band rule are the two easiest details to miss.
2. Pull exact values from `references/design-tokens.yaml` rather than
   guessing hex codes or sizes.
3. Use sub-default type weights (460/540/600), never plain 400/500/700 — this
   subtle warmth is the brand's typographic signature.
4. Reserve pill-shaped buttons for the hero only; every other CTA in the body
   is an 8px rounded rectangle.
5. Close every marketing page with a deep-teal CTA band — omitting it breaks
   the brand's resolving rhythm.
6. Keep body text in warm dark grey (`#292827`), never pure black.
