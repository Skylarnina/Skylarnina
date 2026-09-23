---
name: mongodb-design
description: MongoDB's marketing system carries a dual-mode identity — deep navy-teal hero bands (#001e2b) with the unmistakable bright MongoDB green (#00ed64) CTA pill, paired with stark white documentation and pricing surfaces. Euclid Circular A is the display face across every UI surface; buttons are always pill-shaped, cards round to 12px, and colored category tags (purple, orange, pink, blue) mark course tiles on MongoDB University. Use when asked for a "MongoDB style", "MongoDB-inspired UI", or a database/developer-platform marketing page pairing a dark hero with a bright signal-green CTA.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/mongodb/DESIGN.md
---

# MongoDB Design System

Use this skill when a task calls for MongoDB's dual-mode dark-hero /
white-documentation marketing aesthetic: database or developer-platform
landing pages, pricing comparisons, or any explicit "MongoDB style" request.

## Quick reference

- **Canvas**: stark white (`#ffffff`) for documentation and pricing
  surfaces, deep navy-teal (`#001e2b`) for hero bands, footer, and CTA
  banners.
- **Accent**: bright MongoDB green `#00ed64` — the brand's most
  recognizable signal, carrying every primary CTA pill against both light
  and dark surfaces.
- **Type**: `Euclid Circular A` across every UI surface — contemporary
  geometric, confident but not playful.
- **Corners**: `{rounded.full}` (pill) on every button and status badge;
  `{rounded.lg}` (12px) on cards, pricing tiers, and course tiles.
- **Layout trait**: dark hero bands with embedded terminal-aesthetic code
  mockups, feeding into a 3-tier pricing comparison (Free / Flex /
  Dedicated) and a course-catalog grid where each tile carries a colored
  category tag (purple/orange/pink/blue) — the only saturated color outside
  the brand green.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` for the full rationale before writing
   CSS or components — the "Do's and Don'ts" section is the fastest way to
   avoid diluting the brand green.
2. Pull exact values from `references/design-tokens.yaml` (colors,
   typography scale, spacing scale, border-radius scale, component specs)
   rather than guessing hex codes or sizes.
3. Pair dark-teal hero bands with bright green CTA pills — never put the
   green pill on a mid-tone surface.
4. Reserve the category accent colors (purple, orange, pink, blue) strictly
   for course/content tags — never for primary chrome.
5. Apply `{rounded.full}` to every button and status badge, and
   `{rounded.lg}` (12px) consistently to cards.
6. Use terminal-aesthetic code mockup cards on dark canvas for product
   showcases, echoing MongoDB's developer-tool identity.
