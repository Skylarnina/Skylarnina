---
name: wired-design
description: Wired's technology-magazine design system — a strict editorial black-and-white surface built around a tall, narrow, high-contrast proprietary display serif for headlines, a humanist serif for long-form body copy, and a clean sans for metadata and buttons. Every interactive shape stays perfectly square (0px radius), and the page reads like a printed magazine ported to the web with almost no marketing chrome. Use when asked for a "Wired style", Wired-inspired UI, or an editorial tech-magazine/news layout.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/wired/DESIGN.md
---

# Wired Design System

Use this skill for technology-journalism, magazine, or editorial-content
surfaces that want Wired's strict black-and-white print-to-web voice, or
for any explicit "Wired style" request.

## Quick reference

- **Canvas**: `#ffffff` white — the entire system is a black-and-white
  duet with no dark mode and almost no gray in between.
- **Accent**: `#000000` ink black is the only "accent" — wordmark,
  headlines, CTAs, footer fill. The single chromatic exception is
  `#057dbc` link blue, reserved for inline article links only.
- **Type**: three-face system — `WiredDisplay` (proprietary tall-narrow
  serif) for headlines, `BreveText` (humanist serif) for long-form body
  and bylines, `Apercu` (humanist sans) for nav, buttons, and metadata.
- **Corners**: `0px` on every interactive element — buttons, inputs, and
  cards are perfectly square. Only avatars/social icons use a full circle.
- **Layout anchor**: a magazine story grid — one large feature card, a
  2-up secondary row, then a vertical stack of bylined story rows
  separated by hairline dividers.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first — the Do's and Don'ts section
   is the fastest way to avoid softening the brand's deliberately square,
   print-inspired geometry.
2. Pull exact values from `references/design-tokens.yaml` — colors, the
   full three-face type scale, spacing, and component specs.
3. Keep every button, input, and card corner at `0px` — the brand never
   softens its rectangular geometry.
4. Set display headlines in the tall-narrow serif face; keep long-form body
   in the humanist serif; keep nav, buttons, and metadata in the sans —
   never cross the three roles.
5. Rely on hairline dividers, not shadows, for structure and elevation.
6. Reserve the link-blue accent strictly for inline body links inside
   long-form articles — never on buttons or navigation.
