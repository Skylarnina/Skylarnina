---
name: zapier-design
description: Zapier's workflow-automation marketing system — a warm-cream canvas (#fffefb, never pure white) with deep coffee ink (#201515) and a single saturated orange CTA accent (#ff4f00), giving the brand a confident-warm rather than cool-tech voice. The proprietary Degular Display face carries hero headlines at weight 500 while Inter handles everything else, and every button/card shares a middle-ground 12px radius rather than pills or sharp squares. Use when asked for a "Zapier style", "Zapier-inspired UI", or a warm, mature workflow-automation/B2B SaaS marketing page.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/zapier/DESIGN.md
---

# Zapier Design System

Use this skill when a task calls for Zapier's warm, confidently-mature
SaaS aesthetic: workflow-automation marketing pages, "connect your apps"
integration platforms, or any explicit "Zapier style" request.

## Quick reference

- **Canvas**: warm-cream (`#fffefb`) page background — never pure
  white — with a cream-tinted soft surface (`#f8f4f0`) for cards.
- **Accent**: a single saturated orange (`#ff4f00`) CTA color — the
  brand's whole conversion signature, with no second chromatic accent.
- **Type**: proprietary Degular Display at weight 500 for hero headlines,
  paired with Inter (weights 400/500/600/700) for everything else —
  sentence-case only, never uppercase display.
- **Corners**: 12px (`rounded.md`) is the canonical radius for every
  button and card — a deliberate middle ground between friendly-rounded
  and technical-square.
- **Layout anchor**: a warm coffee-ink footer/dark-card polarity flip,
  and every neutral in the palette (canvas, mute, body) carries warmth
  rather than cool gray.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first — the "Do's and Don'ts"
   section is the fastest way to avoid a generic cool-gray SaaS look.
2. Pull exact values from `references/design-tokens.yaml` (colors,
   typography scale, spacing scale, border-radius scale, component specs)
   instead of guessing hex codes or sizes.
3. Keep every neutral warm — cream canvas, coffee ink, never pure white
   or pure black — the temperature itself is the brand voice.
4. Set hero headlines in Degular Display weight 500, sentence-case, and
   use Inter for everything smaller.
5. Round every button and card to 12px; resist both pill shapes and
   sharp squares.
6. Reserve orange strictly for the primary CTA; pair it with ink-dark
   text on cream backgrounds as the system's whole conversion rhythm.
