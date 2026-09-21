---
name: runwayml-design
description: Runway's marketing-site design system — a cinematic, film-production-grade interface where full-bleed AI-generated photography and video ARE the primary UI elements, set against a near-invisible dark chrome with zero shadows and minimal borders. A single typeface, abcNormal, handles everything from 48px display headlines (line-height 1.0, tracking down to -1.2px) to 11px uppercase micro labels, and cool-toned grays (#767d88, #7d848e) are the only text colors besides black and white. Use when asked for a "Runway style", "Runway-inspired UI", or a cinematic, photography-dominant AI-creative-tool marketing page.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/runwayml/DESIGN.md
---

# Runway Design System

Use this skill when a task calls for Runway's cinematic, film-reel marketing
aesthetic: AI-creative-tool landing pages, portfolio-style visual-content
sites, or any explicit "Runway style" request.

## Quick reference

- **Canvas**: dark-dominant — Runway Black `#000000` and Dark Surface
  `#1a1a1a` for most sections, with occasional light sections in Pure White
  `#ffffff` / Cool Cloud `#e9ecf2`.
- **Accent**: none — there is no decorative brand color; all color and
  gradient comes from the AI-generated photography and video itself.
  Text runs cool-slate grays (`#767d88`, `#7d848e`) rather than warm grays.
- **Type**: a single face, **abcNormal** (Inter or DM Sans as open
  substitutes), for every role — display down to micro tags — with
  line-height 1.0 and negative tracking (-0.9px to -1.2px) at display sizes.
- **Corners**: small and functional only — 4px on buttons, 8px on image
  cards, 16px on rare alert-style containers. Never pill-shaped.
- **Layout anchor**: full-bleed cinematic photography/video fills the role
  whitespace would play elsewhere; mixed-size editorial magazine grids
  pair large hero images with smaller supporting ones.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first — the "interface should be
   invisible, photography carries everything" principle governs every
   other decision in the system.
2. Pull exact values from `references/design-tokens.yaml` instead of
   guessing hex codes, sizes, or spacing.
3. Use abcNormal (or Inter/DM Sans) for every text role — never introduce a
   second typeface, and keep display line-heights at 1.0 with negative
   tracking.
4. Let full-bleed cinematic imagery or video BE the visual content; don't
   fill space with icons, diagrams, or decorative color blocks.
5. Keep the interface itself nearly invisible — zero shadows, only a single
   `1px solid #27272a` border reserved for alert-style containers.
6. Use uppercase labels with positive tracking (0.35px) for structural/nav
   text, and reserve weight 450 for the smallest micro labels as a
   precision detail.
