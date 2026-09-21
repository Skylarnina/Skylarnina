---
name: slack-design
description: Slack's marketing-site design system — a deep aubergine primary (#4a154b) anchoring every filled CTA, the featured pricing tier, and the footer band, staged against cream-and-lavender hero canvases washed with soft pastel-mesh gradients behind floating product-UI mockups. Type pairs a proprietary humanist display sans (tight negative tracking) with a matching UI sans, and every button is an unusually generous 90px pill. Use when asked for a "Slack style", "Slack-inspired UI", or a warm, workplace-messaging SaaS marketing page built around a single deep-purple brand color.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/slack/DESIGN.md
---

# Slack Design System

Use this skill when a task calls for Slack's warm, aubergine-anchored marketing
aesthetic: workplace-messaging landing pages, SaaS marketing sites that want a
"friendly enterprise" feel, or any explicit "Slack style" request.

## Quick reference

- **Canvas**: white (`#ffffff`) by default, with cream (`#f4ede4`) and pale
  lavender (`#f9f0ff`) hero bands washed in soft pastel-mesh gradients.
- **Accent**: deep aubergine (`#4a154b`) — the brand's only real chromatic
  monotheism, reused on filled CTAs, the featured pricing tier, and the
  footer band. Inline links break the rule with a saturated blue (`#1264a3`).
- **Type**: two proprietary humanist sans families (Avant Garde display,
  Sans body) with tight negative tracking on display sizes; open-source
  substitute is Inter for both tiers.
- **Corners**: buttons are always a 90px full pill with generous 28-30px
  horizontal padding — never a rounded rectangle.
- **Layout anchor**: floating product-UI mockups sit above pastel-mesh
  gradient backdrops (peach/lavender/dusty-green) instead of inside shadowed
  cards — the gradient does the "lifting."

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first — the "Do's and Don'ts" section
   is the fastest way to avoid generic purple-SaaS clichés.
2. Pull exact values from `references/design-tokens.yaml` (colors,
   typography scale, spacing scale, border-radius scale, component specs)
   instead of guessing hex codes or sizes.
3. Treat aubergine as scarce outside of buttons, the footer, and the
   featured pricing tier — never use it as body text color.
4. Build hero sections as a cream-or-lavender canvas with a diffused
   pastel-mesh gradient behind a floating product-UI screenshot, not inside
   a bordered card.
5. Round every button to the full 90px pill with 28px+ horizontal padding —
   resist the urge to shrink it to a standard 8-12px SaaS button.
6. Reserve the saturated link-blue (`#1264a3`) for inline text links only —
   it is the system's one non-aubergine chromatic accent.
