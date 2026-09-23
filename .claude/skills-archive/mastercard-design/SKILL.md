---
name: mastercard-design
description: Mastercard's marketing-site design system — a warm putty-cream canvas (#F3F0EE, never white) built entirely around oversized, stadium-and-pill geometry, circular photo portraits linked by hand-drawn-feeling orange orbit lines, and MarkForMC, a geometric sans set at a distinctive half-step weight 450 for body copy. Corners commit to either tiny (under 6px), medium-large (20-40px), or full pill (99px+) — never the 8-12px middle ground. Use when asked for a "Mastercard style", Mastercard-inspired UI, or a warm, editorial, institutional-yet-modern payments/finance marketing page built on circular imagery and pill CTAs.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/mastercard/DESIGN.md
---

# Mastercard Design System

Use this skill when a task calls for Mastercard's warm, editorial payments-
brand aesthetic: fintech/payments marketing pages, institutional-but-modern
brand magazines, or any explicit "Mastercard style" request.

## Quick reference

- **Canvas**: `#F3F0EE` warm putty-cream — never pure white; every surface
  is tinted, never sterile.
- **Accent**: Ink Black (`#141413`) carries primary CTAs and headlines;
  Signal Orange (`#CF4500`) is reserved strictly for cookie-consent/legal
  actions, never marketing CTAs.
- **Type**: MarkForMC, a geometric sans, with headlines at weight 500 and
  tight -2% negative tracking; body copy runs at the unusual weight 450
  (softer than 400, firmer than 500) — this half-step weight is load-bearing.
- **Corners**: extreme and bimodal — 20px on primary buttons, 40px on hero
  media frames, 50%/999px on circular portraits and pill navigation; the
  8-12px "generic" middle ground never appears.
- **Layout anchor**: circular image portraits with an attached white
  satellite micro-CTA and thin orange orbital lines connecting cards across
  the page, implying a constellation of services in motion.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first — the "Do's and Don'ts" section
   is the fastest way to avoid a generic white-canvas fintech look.
2. Pull exact values from `references/design-tokens.yaml` rather than
   guessing hex codes or sizes.
3. Default every background to Canvas Cream (`#F3F0EE`); this single swap
   shifts the whole mood toward Mastercard.
4. Crop feature/service imagery into perfect circles, never rectangles or
   softly-rounded rectangles, and attach a white satellite CTA circle to
   the bottom-right of each portrait.
5. Reach for one of exactly three radii when in doubt: 20px (buttons), 40px
   (hero/stadium frames), or 999px (pills/nav) — skip everything in between.
6. Keep Signal Orange confined to consent/legal moments; use Ink Black pills
   for every marketing CTA.
