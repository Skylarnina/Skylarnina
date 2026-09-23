---
name: hp-design
description: HP's consumer-and-enterprise catalog design system — a pure white canvas with light "cloud"/"fog" gray section bands, HP Electric Blue (#024ad8) as the lone signal color for CTAs and links, and Forma DJR Micro (a single family, weight 500 at every display size, never bold) across the whole hierarchy. Signature angular blue chevron decorations echo the wordmark's slashes, cards round softly at 16px while buttons stay sharp at 4px, and dark-navy slabs close every page in testimonial bands and the footer. Use when asked for an "HP style", HP-inspired UI, or a commercial-clean consumer-electronics catalog page.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/hp/DESIGN.md
---

# HP Design System

Use this skill when a task calls for HP's commercial-clean
consumer-electronics catalog aesthetic: product shop pages, pricing-tier
comparisons, or any explicit "HP style" request.

## Quick reference

- **Canvas**: pure white (`#ffffff`) alternating with light gray "cloud"
  (`#f7f7f7`) and "fog" (`#e8e8e8`) section bands for rhythm.
- **Accent**: `#024ad8` HP Electric Blue — the system's lone signal color,
  reserved for the primary CTA fill and link text; appears at most twice
  per viewport, never as a section background.
- **Type**: Forma DJR Micro, a single family across every role, run at
  weight 500 for ALL display sizes (even the 72px hero) and 400 for body —
  resist the urge to bump weight at hero scale.
- **Corners**: a deliberate two-tier split — buttons and inputs stay sharp
  at `4px`, while cards and photo frames round softly at `16px`.
- **Layout anchor**: angular blue chevron decorations (sharp 0-radius
  slashes derived from the wordmark) flank hero photography; every page
  rhythm closes on a dark-navy ink slab for testimonials, "how can we
  help?", and the footer.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` for the full rationale before writing
   CSS or components — the "Do's and Don'ts" section is the fastest way to
   keep the blue accent scarce.
2. Pull exact values from `references/design-tokens.yaml` (colors,
   typography scale, spacing scale, border-radius scale, component specs)
   rather than guessing hex codes or sizes.
3. Keep the two-tier radius split strict: 4px on every interactive
   control, 16px on every card and photo frame — never blur the two.
4. Set headlines in Forma DJR Micro at weight 500 regardless of size;
   never bold the hero headline.
5. Reserve `{colors.primary}` blue for the primary CTA and link color only
   — use `button-ink` (black) or `button-outline` variants for secondary
   actions so blue never crowds a viewport.
6. Close every page rhythm with a dark-navy `{colors.ink}` slab — the
   "how can we help?" prelude plus the footer — rather than ending flat on
   white.
