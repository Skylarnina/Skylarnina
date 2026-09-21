---
name: clay-design
description: Clay.com's GTM data-orchestration marketing system — a cream-tinted white canvas (#fffaf0), dark-navy near-black primary CTAs, a custom rounded "Plain Black" display face at weight 500 with negative tracking, and a six-color rotation of saturated feature cards (hot pink, deep teal, lavender, peach, ochre, cream) that carry product-UI fragments and 3D claymation illustrations. Use when asked for a "Clay style", "Clay.com-inspired UI", or a playful, illustration-forward B2B SaaS look that avoids cool-gray data-platform conventions.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/clay/DESIGN.md
---

# Clay Design System

Use this skill when a task calls for Clay's warm, playful, claymation-illustrated
B2B SaaS aesthetic: GTM/data-orchestration marketing pages, long-scroll product
explainer sites, or any explicit "Clay style" or "Clay.com-inspired" request.

## Quick reference

- **Canvas**: `#fffaf0` cream-tinted white — never cool gray, never a dark
  footer.
- **Accent**: dark navy/near-black `#0a0a0a` for primary CTAs and headline
  ink; the real brand voltage is a rotating six-color feature-card palette
  (hot pink, deep teal, lavender, peach, ochre, cream).
- **Type**: custom rounded display face "Plain Black" at weight 500 only
  (never bolder) with -1 to -2.5px letter-spacing; Inter for everything else.
- **Corners**: generous — 12px on buttons/inputs, 16px on content cards,
  24px on saturated feature cards.
- **Layout anchor**: 3D-rendered claymation illustrations (mountains,
  mascot characters) as full-bleed hero artifacts, plus saturated
  single-color feature cards showing embedded product-UI fragments.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first — the Do's and Don'ts section
   flags the two easiest ways to break the system: cool-gray canvas and a
   dark footer.
2. Pull exact values from `references/design-tokens.yaml` rather than
   guessing hex codes, sizes, or component paddings.
3. Cycle the six feature-card colors (pink → teal → lavender → peach →
   ochre → cream) across a page; never repeat the same color twice in a
   row.
4. Keep Plain Black display type at weight 500 with negative tracking —
   heavier weights read as bombastic and break the brand voice.
5. Embed real product-UI fragments (agent runs, sequencer flows, table
   snippets) inside the colored cards rather than abstract illustration.
6. Close every page on the cream footer (`surface-soft`), never a dark one —
   Clay deliberately avoids the standard dark-footer SaaS template.
