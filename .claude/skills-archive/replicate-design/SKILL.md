---
name: replicate-design
description: Replicate's marketing-site design system — a warm cream canvas (#f9f7f3, never pure white) that gives an AI developer-tools brand the feel of an indie art zine, paired with a scarce hot-orange accent (#ea2804), oversized 72-128px rb-freigeist-neue display headlines with tight negative tracking, and fully-rounded (9999px) buttons/inputs/badges next to softer 10-16px card corners. Use when asked for a "Replicate style", Replicate-inspired UI, or a cream-and-orange, editorial-meets-developer-tool AI/ML marketing page.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/replicate/DESIGN.md
---

# Replicate Design System

Use this skill for AI/ML developer-tool marketing pages, model-hosting
platforms, or any page that wants Replicate's "print magazine crossed with
lab notebook" feel — warm cream over stark white or dark, with a stamp of
hot orange rather than a themed accent.

## Quick reference

- **Canvas**: warm cream `#f9f7f3` (never pure white) as the default
  background, with `surface-bone` (`#f3f0e8`) for inset card groups and
  pure white reserved only for individual cards and inputs.
- **Accent**: hot orange `#ea2804` — treated as a stamp, used only for the
  primary CTA, the home hero band, and inline links; never decorative.
- **Type**: three-family stack — `rb-freigeist-neue` for display (up to
  128px, `lineHeight: 1.0`, aggressive negative tracking), `basier-square`
  for UI/body, `jetbrains-mono` for all code.
- **Corners**: every interactive element (buttons, inputs, badges, avatars)
  is fully rounded (`rounded.full`, 9999px); content cards step to 10px or
  16px — never sharp corners anywhere.
- **Layout anchor**: dark (`#202020`) code wells sit inside the cream canvas
  like printed pull-quotes; the home hero uses a layered orange-to-pink
  atmospheric mesh gradient.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first — the Do's and Don'ts section
   flags the two easiest mistakes: defaulting to pure white instead of
   cream, and letting orange spread beyond its three sanctioned roles.
2. Pull exact values from `references/design-tokens.yaml` (colors,
   typography scale, spacing, border-radius, component specs) instead of
   guessing hex codes or sizes.
3. Keep orange scarce — if more than one orange element appears per
   viewport, drop one to `surface-dark` or leave it cream.
4. Render every code sample inside a dark (`surface-dark`/`surface-deep`)
   code well with JetBrains Mono — never a light grey inline box.
5. Round every interactive control fully (pill/circle); reserve the 10px
   and 16px radii for model cards, collection tiles, and pricing tiers.
6. For light-mode-only requests this fits directly — Replicate has no dark
   marketing mode, only cream-canvas-with-dark-code-wells.
