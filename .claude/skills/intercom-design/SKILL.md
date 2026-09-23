---
name: intercom-design
description: Intercom's editorial customer-service marketing system — a soft cream-white canvas (#f5f1ec, deliberately not pure white) holding charcoal Saans type and white floating product-mockup cards with thin hairline borders. Charcoal (#111111) is the system's primary action color; a single confident Fin Orange (#ff5600) is reserved exclusively for the Fin AI product's CTAs and badges. Display headlines run Saans at weight 500 with measured negative tracking, and every section is led by a high-fidelity product screenshot rather than illustration. Use when asked for an "Intercom style", "Intercom-inspired UI", or a calm, product-screenshot-led customer-service/support-software marketing page.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/intercom/DESIGN.md
---

# Intercom Design System

Use this skill for Intercom's calm, editorial customer-service marketing
aesthetic: support/helpdesk SaaS pages, product-led marketing sites, or any
explicit "Intercom style" request.

## Quick reference

- **Canvas**: soft cream-white (`#f5f1ec`) — never pure white or gray —
  with pure white floating cards (`surface-1`) lifted above it for
  hierarchy.
- **Accent**: charcoal (`#111111`) is the system's primary color for
  headlines, body, and default CTAs; Fin Orange (`#ff5600`) is reserved
  strictly for the Fin AI product's CTA and badge, never used decoratively
  or as a general primary.
- **Type**: Saans (proprietary geometric sans) at weight 500 for display
  with measured negative tracking, weight 400 for body — a single family
  carries the entire hierarchy, with SaansMono for code inside product
  mockups only.
- **Corners**: modest and consistent — `8px` buttons/inputs, `12px` cards,
  `16px` product-mockup tiles — never pill-rounded, never square.
- **Layout anchor**: every section centers a high-fidelity product-UI
  screenshot in a white card; marketing chrome stays quiet so the product
  is the protagonist.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first, especially Do's and Don'ts —
   the biggest risk is treating Fin Orange as a general accent instead of
   a scoped product-specific color.
2. Pull exact values from `references/design-tokens.yaml` rather than
   guessing hex codes, weights, or spacing.
3. Anchor the canvas on the cream tone, never pure white; lift cards onto
   white (`surface-1`) rather than adding shadows for hierarchy.
4. Set every display headline in Saans (or Inter 500 as substitute) with
   negative tracking proportional to size; keep body at weight 400 in the
   same family.
5. Reserve Fin Orange exclusively for Fin AI CTAs and badges — default
   CTAs and headlines stay charcoal.
6. Lead every section with a framed product-UI screenshot at `16px`
   radius rather than illustration or gradient art.
