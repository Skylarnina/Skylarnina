---
name: warp-design
description: Warp's agentic-terminal marketing design system — a single warm near-charcoal canvas (#2b2622, browner than pure black) carrying restrained Inter typography, unusually tight button radii (3-4px, never a pill), and terminal-mockup screenshots as the only decoration. DM Mono handles code and Instrument Serif appears occasionally for editorial italic moments. Use when asked for a "Warp style", Warp-inspired UI, or a quietly confident dark developer-tool marketing page that avoids generous rounding and gradient hype.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/warp/DESIGN.md
---

# Warp Design System

Use this skill for terminal, CLI, or agentic-development marketing surfaces
that want Warp's warm-dark, tightly-cornered restraint, or for any explicit
"Warp style" request.

## Quick reference

- **Canvas**: `#2b2622` warm near-charcoal — the only page surface, with a
  deliberate brown-beige warmth rather than pure black or neutral gray.
- **Accent**: no chromatic brand accent — `#f7f5f0` warm off-white doubles
  as the primary color, default text, and button fill. The off-white-on-
  warm-dark pairing IS the brand's identity.
- **Type**: Inter weight 400 for display (64px hero, -1.6px tracking),
  DM Mono for terminal mockups and code, Instrument Serif for rare
  editorial italic moments.
- **Corners**: extremely tight — `3px` buttons, `4px` cards. Never a
  generous pill; only icon containers use a full circle.
- **Layout anchor**: two terminal screenshots split the hero, followed by
  a partner-logo strip, a single testimonial card, a press list, and
  platform download tiles — no gradients or illustration anywhere.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first — the Do's and Don'ts section
   is the fastest way to avoid defaulting to generous pill CTAs, which
   this brand deliberately avoids.
2. Pull exact values from `references/design-tokens.yaml` — colors, the
   type scale, spacing, radius scale, and component specs.
3. Keep the canvas warm-dark, not neutral gray or pure black — the
   `oklch`-defined warmth is the brand's defining tone.
4. Use tight 3-4px button radii throughout; reserve the full circle for
   icon containers only, never for CTAs.
5. Set the hero headline in Inter weight 400 with aggressive negative
   tracking rather than a bold or heavy weight — restraint is the voice.
6. Anchor sections with terminal-mockup screenshots instead of gradients,
   illustration, or atmospheric backdrops.
