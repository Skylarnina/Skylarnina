---
name: miro-design
description: Miro's visual-workspace marketing system — a stark white canvas anchored by a canary-yellow (#ffd02f) wordmark, black-pill primary CTAs, and a rotation of pastel sticky-note feature cards (rose, teal, coral, yellow) that echo the actual whiteboard product. Roobert PRO, a geometric display sans, carries everything from an 80px hero down to 11px micro labels, and real Miro-board mockups replace stock photography as feature illustrations. Use when asked for a "Miro style", "Miro-inspired UI", or a confident, playful collaboration/whiteboard-software marketing page.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/miro/DESIGN.md
---

# Miro Design System

Use this skill when a task calls for Miro's confident, playful
visual-workspace marketing aesthetic: collaboration/whiteboard SaaS landing
pages, productivity-tool pricing pages, or any explicit "Miro style" request.

## Quick reference

- **Canvas**: `#ffffff` throughout — the wordmark's canary yellow is the
  opening signature, not the background.
- **Accent**: Miro Yellow `#ffd02f` — reserved for the wordmark, top promo
  banner, and "yellow tag" chips; never a primary CTA fill.
- **Type**: Roobert PRO, a geometric, slightly rounded display sans, carries
  every UI surface from an 80px hero to 11px micro labels — weight 400/500/
  600 only, no 700.
- **Corners**: `{rounded.full}` (pill) on every button and pill tab;
  `{rounded.xxxl}` (28px) on the pastel feature cards is the system's most
  distinctive card radius.
- **Layout trait**: pastel feature cards (yellow, rose, coral, teal) that
  echo the live product's sticky-note palette, paired with real Miro-board
  mockup imagery instead of stock photography.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` for the full rationale before writing
   CSS or components — the "Do's and Don'ts" section is the fastest way to
   avoid over-using the yellow brand color.
2. Pull exact values from `references/design-tokens.yaml` (colors,
   typography scale, spacing scale, border-radius scale, component specs)
   rather than guessing hex codes or sizes.
3. Keep `colors.brand-yellow` scoped to the wordmark, promo banner, and
   yellow-tag chips — use `colors.primary` (black) for the actual CTA fill.
4. Pair at least one pastel feature card (yellow/rose/coral/teal) with
   white feature cards in the same viewport for the signature sticky-note
   rhythm.
5. Use real product-board mockups (sticky notes, kanban, mind maps) as
   feature illustrations rather than stock photography or abstract art.
6. Apply `{rounded.full}` to every button, pill tab, and status badge —
   never soften a pill's corners.
