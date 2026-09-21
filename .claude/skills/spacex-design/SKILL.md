---
name: spacex-design
description: SpaceX's marketing-site design system — pure black canvas, full-bleed photographic and video heroes of rockets and Mars landscapes, uppercase D-DIN-Bold display type with wide positive tracking, and a single ghost-outlined pill CTA per band. There is no brand accent color; black, white, and the photography itself carry the entire system. Use when asked for a "SpaceX style", "SpaceX-inspired UI", or an austere, photography-led aerospace/engineering marketing page.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/spacex/DESIGN.md
---

# SpaceX Design System

Use this skill when a task calls for SpaceX's black-and-white, photography-first
aerospace aesthetic: mission pages, engineering/hardware marketing sites, or any
explicit "SpaceX style" request.

## Quick reference

- **Canvas**: pure `#000000` on marketing pages (`canvas-night`) — no gradients,
  no atmospheric color. The shop site alone switches to `#ffffff`.
- **Accent**: none. Black and white do all the chromatic work; every other hue
  comes from the photograph or video itself.
- **Type**: uppercase **D-DIN-Bold** for every display size, with unusually
  tight vertical leading (0.95–1.25) and wide positive letter-spacing
  (0.96–1.6px) — free substitute: Inter at 700 weight, uppercase, tracked.
- **Corners**: a signature 32px ghost-outlined pill on every CTA; sharper
  4–16px radii elsewhere, never a filled marketing button.
- **Layout anchor**: every band is a full-viewport photograph or autoplaying
  video with type sitting directly on the image — no scrim, no overlay, no
  card grid on marketing pages.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first — the "Do's and Don'ts" section is
   the fastest way to avoid drifting into a generic dark SaaS look.
2. Pull exact values from `references/design-tokens.yaml` rather than guessing
   hex codes, D-DIN sizes, or the pill-CTA padding.
3. Treat photography (or autoplaying video) as the only decorative element —
   no illustrations, no gradients, no drop shadows.
4. Render every display headline in uppercase with positive tracking; never
   sentence-case a hero headline.
5. Use exactly one ghost-outlined pill CTA per band — never pair two buttons
   on a marketing surface.
6. Reserve the light canvas and filled buttons for shop/e-commerce contexts
   only; marketing surfaces stay black with ghost buttons.
