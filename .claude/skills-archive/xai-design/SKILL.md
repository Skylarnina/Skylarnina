---
name: xai-design
description: xAI's frontier-AI marketing system — a strict near-black canvas (#0a0a0a) broken only by white translucent-outline pills, a custom geometric sans (Universal Sans, weight 400 only) carrying every headline at aggressive negative tracking, and an uppercase tracked Geist Mono for eyebrows and labels. A muted sunset/dusk/twilight accent palette lives in the tokens but appears only inside product illustrations, never on the main marketing surface. Use when asked for an "xAI style", "Grok-inspired UI", or an engineered, unmarketed, research-lab-cadence dark AI marketing page.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/x.ai/DESIGN.md
---

# xAI Design System

Use this skill when a task calls for xAI's engineered, unmarketed dark
aesthetic: frontier-AI/research-lab marketing pages, product-announcement
sites that want to avoid typical SaaS gloss, or any explicit "xAI style"
request.

## Quick reference

- **Canvas**: near-black (`#0a0a0a`) as the only true page surface — no
  light-mode counterpart, no gradient hero, no atmospheric backdrop.
- **Accent**: white is the brand's real "color" — every button outline,
  every headline, is white-on-near-black; a muted sunset-orange/dusk-
  purple/twilight-violet/breeze-blue set exists only for product
  illustrations.
- **Type**: Universal Sans at weight 400 only, with aggressive negative
  tracking (down to -2.4px at 96px) for display, paired with uppercase
  tracked Geist Mono for eyebrows, labels, and metric counters.
- **Corners**: every interactive element is a full pill (9999px) with a
  1px translucent-white border; cards are tight 8px rectangles — the
  pill is the entire shape system.
- **Layout anchor**: no shadows anywhere — hairline borders carry every
  elevation cue, and product moments use sparse SVG illustration rather
  than photography.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first — the "Do's and Don'ts"
   section is the fastest way to avoid over-decorating what should be a
   sparse, research-lab-toned page.
2. Pull exact values from `references/design-tokens.yaml` (colors,
   typography scale, spacing scale, border-radius scale, component specs)
   instead of guessing hex codes or sizes.
3. Keep the canvas dark-only at `#0a0a0a` — never introduce a light-mode
   counterpart.
4. Set every interactive element as a translucent-white-outline pill;
   reserve the rare white-filled pill for a single primary Sign Up CTA.
5. Set display headlines in Universal Sans weight 400 with aggressive
   negative tracking, and pair them with uppercase, positively-tracked
   Geist Mono eyebrows above every section headline.
6. Never add a box-shadow; use 1px hairline borders for all card and
   button elevation instead.
