---
name: lamborghini-design
description: Lamborghini's marketing system is a cathedral of darkness — true black (#000000) canvas, white type, and Lamborghini Gold (#FFC000) as the sole accent reserved exclusively for primary CTAs. LamboType, a custom Neo-Grotesk with 12° angled terminals, sets every headline in uppercase at extreme scale (up to 120px) with tight line-heights. Use when asked for a "Lamborghini style", "Lamborghini-inspired UI", or a theatrical, all-black luxury-automotive marketing page with zero border-radius and full-viewport cinematic video.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/lamborghini/DESIGN.md
---

# Lamborghini Design System

Use this skill when a task calls for Lamborghini's nocturnal, theatrical
luxury-automotive marketing aesthetic: supercar landing pages, motorsport
event sites, or any explicit "Lamborghini style" request.

## Quick reference

- **Canvas**: `#000000` — true, uncompromising black; never dark gray, never
  light mode.
- **Accent**: Lamborghini Gold `#FFC000` — used ONLY for primary CTA
  buttons ("Discover More", "Tickets"). No other chromatic color appears in
  UI chrome.
- **Type**: `LamboType`, a custom Neo-Grotesk with 12° angled terminals and
  hexagonal geometric DNA — always uppercase at display sizes, weight 400,
  extreme scale range (10px micro to 120px hero) with tight line-heights
  (0.92 at 120px).
- **Corners**: zero border-radius everywhere — buttons, cards, containers.
  The only rounded element in the whole system is the 20px toggle switch.
- **Layout trait**: full-viewport (100vh) cinematic video heroes; depth
  comes from a "darkness gradient" of surface layering (`#000000` →
  `#181818` → `#202020` → `#494949`), never drop shadows.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` for the full rationale before writing
   CSS or components — the "Do's and Don'ts" section is the fastest way to
   avoid drifting into generic dark-mode UI.
2. Pull exact values from `references/design-tokens.yaml` (colors,
   typography scale, spacing scale, border-radius scale, component specs)
   rather than guessing hex codes or sizes.
3. Treat gold as scarce — if anything besides a primary CTA is gold, dial
   it back to white or gray.
4. Set every display heading in uppercase LamboType (or a bold geometric
   sans substitute) at weight 400, never bold — the typeface itself carries
   the aggression.
5. Keep every corner at 0px radius; use surface-color shifts, not shadows,
   for elevation on the black canvas.
6. Lead sections with full-bleed video or high-contrast studio photography
   — UI chrome should recede into the darkness around it.
