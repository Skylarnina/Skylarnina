---
name: ibm-design
description: IBM's Carbon Design System marketing site — white surfaces, charcoal type (#161616), IBM Blue (#0f62fe) as the single confident accent, and a strictly flat-square aesthetic where every button, card, and input sits at 0px radius with thin 1px hairline borders instead of shadows. IBM Plex Sans carries the entire hierarchy, running at a signature light weight 300 for display sizes (42-76px) and 400/600 for body and emphasis. Use when asked for an "IBM style", "Carbon Design System" UI, or an enterprise-serious, flat-square marketing page with restrained light-weight display type.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/ibm/DESIGN.md
---

# IBM Design System

Use this skill when a task calls for IBM's Carbon-faithful enterprise
marketing aesthetic: developer-platform or enterprise-software marketing
pages, cloud/AI product pages, or any explicit "IBM style" or "Carbon"
request.

## Quick reference

- **Canvas**: pure white with light-gray `surface-1` (#f4f4f4) for
  elevation; charcoal `#161616` carries text; the footer is the only dark
  surface above the page break.
- **Accent**: `#0f62fe` IBM Blue — the single brand accent, used for links,
  primary CTAs, the CTA banner, and focus underlines only.
- **Type**: IBM Plex Sans (free, open-source) everywhere; display sizes
  (42–76px) run at a signature light weight **300**, body at 400 with a
  Carbon-precision `letter-spacing: 0.16px`.
- **Corners**: `0px` on absolutely everything — buttons, cards, inputs,
  containers. No rounded pills anywhere on marketing.
- **Layout anchor**: flat-square geometry throughout; depth comes from 1px
  hairlines and surface change (canvas → surface-1), never drop shadows or
  atmospheric gradients.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` for the full rationale before writing
   CSS or components — the "Do's and Don'ts" section is the fastest way to
   avoid drifting into a generic rounded SaaS look.
2. Pull exact values from `references/design-tokens.yaml` (colors,
   typography scale, spacing scale, border-radius scale, component specs)
   rather than guessing hex codes or sizes.
3. Keep every corner at `rounded.none` (0px) — even a 4px rounding breaks
   the Carbon look; this applies to buttons, cards, and inputs alike.
4. Run display headlines at weight 300, not 700 — the light-weight display
   treatment (42–76px) is IBM's signature and reads as quietly
   authoritative rather than commanding.
5. Preserve `letter-spacing: 0.16px` on body sizes when substituting a
   different font — it's a Carbon precision detail that's easy to drop by
   accident.
6. Use surface change (`canvas` → `surface-1`) plus 1px hairlines for card
   hierarchy instead of drop shadows; reserve `{colors.primary}` for
   primary CTAs, links, and the focused-input underline only.
