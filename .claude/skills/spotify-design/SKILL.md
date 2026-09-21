---
name: spotify-design
description: Spotify's app-interface design system — a near-black immersive canvas (#121212-#1f1f1f) where the UI recedes so album art can carry all the color, punctuated only by the singular functional accent of Spotify Green (#1ed760) on play controls and CTAs. Type runs the compact SpotifyMixUI/CircularSp family across a narrow 10-24px range, with uppercase wide-tracked button labels and pill-and-circle geometry everywhere. Use when asked for a "Spotify style", "Spotify-inspired UI", or a dark, content-first music/media-streaming app interface.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/spotify/DESIGN.md
---

# Spotify Design System

Use this skill when a task calls for Spotify's dark, content-first app
aesthetic: music/audio streaming interfaces, media-library dashboards, or
any explicit "Spotify style" request.

## Quick reference

- **Canvas**: near-black immersive dark theme, three shades of charcoal
  (`#121212` deepest → `#181818`/`#1f1f1f` surfaces) — never light mode.
- **Accent**: Spotify Green (`#1ed760`) used strictly functionally — play
  controls, active states, primary CTAs — never decoratively or as a
  background wash.
- **Type**: SpotifyMixUI/CircularSp, compact and functional across a
  10-24px range; button labels are uppercase with wide letter-spacing
  (1.4-2px).
- **Corners**: pill (500px-9999px) for buttons and search inputs, circle
  (50%) for play/icon controls — square buttons break the identity.
- **Layout anchor**: album art and content are the only color source; the
  UI itself stays achromatic and densely packed, with heavy shadows
  (0.3-0.5 opacity) doing the elevation work on dark surfaces.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first for the full rationale — the
   "Do's and Don'ts" section is the fastest way to avoid generic
   dark-mode clichés.
2. Pull exact values from `references/design-tokens.yaml` (colors,
   typography scale, spacing scale, border-radius scale, component specs)
   instead of guessing hex codes or sizes.
3. Treat Spotify Green as scarce and functional — if it appears anywhere
   other than a play control, active state, or primary CTA, remove it.
4. Round every button to a pill and every icon/play control to a full
   circle; there is no square-button variant in this system.
5. Keep type compact (10-24px) and dense — this is an app to scan, not a
   marketing page to read, so avoid relaxed line-heights.
6. Let album art or content imagery supply the only real color in the
   frame; the chrome around it should stay achromatic gray.
