---
name: cal-design
description: Cal.com's friendly modern-SaaS marketing system — a white canvas, near-black (#111111) primary CTAs, and a custom geometric Cal Sans display face set with negative letter-spacing. Brand voltage comes less from color than from showing the real product: light-gray cards embed actual calendar widgets and scheduling UI at small scale, and the only dark surface on the page is a near-black footer that closes every long scroll. Use when asked for a "Cal.com style", "Cal-inspired UI", or a clean, confident scheduling/booking-software marketing page.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/cal/DESIGN.md
---

# Cal.com Design System

Use this skill for Cal.com's clean, product-led scheduling-software
aesthetic: booking/calendar SaaS pages, friendly modern-SaaS marketing
sites, or any explicit "Cal.com style" request.

## Quick reference

- **Canvas**: `#ffffff` white with near-black `#111111` primary CTAs — a
  near-monochrome brand at the action layer.
- **Accent**: essentially none on CTAs; a scarce blue (`#3b82f6`) on inline
  links and a small pastel badge set (orange/pink/violet/emerald) for
  avatar fills and tags only.
- **Type**: custom geometric Cal Sans (weight 600, -0.5 to -2px tracking)
  for every display headline, paired with Inter for body/UI/nav.
- **Corners**: hierarchical — `8px` buttons/inputs, `12px` content cards,
  `16px` the hero app-mockup card, pill/full for badges and avatars.
- **Layout anchor**: real product UI fragments (calendar widgets, schedule
  pickers) shown directly inside marketing cards instead of illustrations,
  closing every page with a dark near-black footer.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first, especially Do's and Don'ts —
   the biggest risk is adding accent color where the system stays
   monochrome.
2. Pull exact values from `references/design-tokens.yaml` rather than
   guessing hex codes, weights, or spacing.
3. Use Cal Sans (or Inter 600 at -0.04em as a substitute) for every display
   headline; keep body copy in Inter 400 and never blur the boundary.
4. Show real product UI (calendar grids, scheduling forms) inside cards
   instead of illustrating the product abstractly.
5. Keep the near-black button (`#111111`) as the only primary CTA color;
   reserve pastel badge colors for avatar fills and tag pills.
6. Alternate surface modes band-to-band (white → light-gray card → white →
   product mockup → dark footer) rather than repeating the same surface
   twice in a row.
