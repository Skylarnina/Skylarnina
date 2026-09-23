---
name: dell-1996-design
description: A reconstruction of Dell.com's December 1996 catalog-era web design — a literal thick black frame around the whole page, flat 8-bit-safe "ribbon card" color blocks (sage, salmon, peach, lime, sky, steel, periwinkle, olive) tinting each product line, chunky Arial Black display titles over Times New Roman serif body copy, and hand-cut GIF-sticker decoration (a yellow "BUY a DELL" tab, angled "NEW!" bursts, a round PC Magazine award seal). Use when asked for a "Dell 1996 style", a pre-CSS/catalog-era retro web look, or a deliberately anachronistic table-layout enterprise homepage.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/dell-1996/DESIGN.md
---

# Dell 1996 Design System

Use this skill when the task explicitly wants a period-accurate,
pre-CSS "catalog web" pastiche: retro tech-nostalgia landing pages, a
deliberately anachronistic enterprise homepage, or any explicit "Dell 1996
style" / "Y2K catalog web" request. This is not a modern design system —
it's a faithful reconstruction of table-layout, GIF-sticker, web-safe-color
web design.

## Quick reference

- **Canvas**: white, contained inside a literal ~8px solid black
  `page-frame` border around the entire viewport — the browser window is
  treated as a printed frame.
- **Accent**: Dell red (`#e91d2a`) reserved for exactly two things (the CTA
  panel and the phone number); eight flat "ribbon-card" tints (sage, salmon,
  peach, lime, sky, steel, periwinkle, olive) color each product line.
- **Type**: sans for UI (Arial Black 900 display, Helvetica Bold labels),
  serif Times New Roman for all body copy — the inverse of the modern
  convention.
- **Corners**: `0px` everywhere except circular award-seal stickers
  (`9999px`) — no soft-radius vocabulary at all.
- **Layout anchor**: flat color-block "ribbon cards" (white title bar + a
  tinted body block) with a beveled product-photo GIF notched into the
  right edge, plus hand-cut sticker decoration pinned over the layout.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first — the Do's and Don'ts section
   is the fastest way to keep the pastiche period-accurate rather than
   accidentally modern.
2. Pull exact values from `references/design-tokens.yaml` rather than
   guessing hex codes, weights, or spacing.
3. Keep the black `page-frame` border around the whole page and the black
   `top-banner` strip with the tagline, the yellow "BUY a DELL" sticker,
   and the red phone number.
4. Build product sections as ribbon cards: a white title bar in Helvetica
   Bold, then a flat-tinted body block (pick one of the eight catalog
   tints per product line) with Times New Roman copy.
5. Reserve Dell red for the CTA panel and phone number only; never use it
   as a decorative fill or a third element on the same page.
6. Keep every corner sharp (`0px`); only circular award-seal stickers get
   full rounding, and never add soft drop shadows or gradients — depth
   comes from hard 1px borders and hand-painted GIF bevels only.
