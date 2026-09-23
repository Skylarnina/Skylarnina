---
name: sentry-design
description: A developer-observability marketing system built on a deep purple-violet midnight canvas (#1f1633), an electric-lime keyword-highlight accent (#c2ef4e), and a chunky proprietary display sans paired with Rubik for UI and Monaco for code. The system flips between two complete canvas polarities — dark for hero/product pages, white for pricing/contact — and layers hand-drawn sticker mascots at section junctions to puncture an otherwise serious observability-tool tone. Use when asked for a "Sentry style" or a subversive, developer-console-flavored observability/monitoring marketing page.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/sentry/DESIGN.md
---

# Sentry Design System

Use this skill for error-monitoring, observability, or logging-tool
marketing pages that want a debugging-console-with-personality feel: dark
midnight hero pages, white transactional pages, and a lime-green keyword
highlight running through the copy itself.

## Quick reference

- **Canvas**: two complete polarities — deep violet midnight
  (`#1f1633`/`#150f23`) for hero and product-feature pages, pure white for
  pricing/contact/dense-reference pages. Never blended on one page.
- **Accent**: electric lime `#c2ef4e` used as a typographic device (a
  highlight chip wrapping single headline keywords), never a button
  background; hot pink `#fa7faa` is a secondary illustration-only accent.
- **Type**: a chunky proprietary display sans (Space Grotesk / Archivo /
  Hubot Sans as open substitutes) for hero and section openers, **Rubik**
  for all UI text, **Monaco** for code. Buttons and eyebrows run uppercase
  with 0.2px tracking.
- **Corners**: `rounded.md` (8px) on buttons and code blocks,
  `rounded.xl` (12px) on pricing/feature cards, `rounded.xxl` (18px) on
  image containers and hero illustrations.
- **Layout anchor**: floating sticker-style mascots (astronauts, monsters,
  traffic cones) overlap section boundaries with no container or shadow —
  they replace drop-shadow depth with illustrated personality.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first — the Do's and Don'ts section
   is the fastest way to avoid over-using the lime accent or adding drop
   shadows where the brand instead uses texture and illustration.
2. Pull exact values from `references/design-tokens.yaml` rather than
   guessing — colors, the Rubik/display type scale, spacing, and component
   specs are all defined there.
3. Pick one canvas polarity (dark or light) per page and commit to it —
   don't blend dark hero sections with light content sections on the same
   band.
4. Wrap at most one keyword per headline in the lime highlight chip; never
   use lime as a button fill or body-text color.
5. Let sticker mascots overlap section boundaries and float without a
   container — constraining them inside a card removes their purpose.
6. Default every filled button's label to uppercase Rubik with 0.2px
   tracking, whichever canvas polarity it sits on.
