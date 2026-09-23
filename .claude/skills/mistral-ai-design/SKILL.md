---
name: mistral-ai-design
description: Mistral AI's marketing system is anchored by a single cinematographic signature — atmospheric mountain-sunset photography and a horizontal "sunset stripe" gradient band (red to orange to yellow to cream) that closes every page. PP Editorial Old, a near-serif elegant display face, sets hero headlines; Inter carries everything else. Cream-yellow surfaces and a saturated orange CTA (#fa520f) give the system a sober, editorial geometry — 8px buttons and 12px cards, never pills. Use when asked for a "Mistral style", "Mistral AI-inspired UI", or an editorial, sunset-toned frontier-AI marketing page.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/mistral.ai/DESIGN.md
---

# Mistral AI Design System

Use this skill when a task calls for Mistral AI's editorial, sunset-toned
marketing aesthetic: frontier-AI product pages, developer-platform landing
pages, or any explicit "Mistral style" request.

## Quick reference

- **Canvas**: `#ffffff` with warm cream-yellow surfaces (`#fff8e0`) for form
  panels, feature cards, and the footer.
- **Accent**: saturated Mistral orange `#fa520f` carries every primary CTA
  and link; a multi-stop "sunset stripe" gradient (orange → sunshine →
  yellow → cream) is the brand's most recognizable closing element,
  appearing at the foot of every page.
- **Type**: `PP Editorial Old` (near-serif, elegant) for hero displays and
  stat callouts; `Inter` for everything else — body, headings, UI.
- **Corners**: `{rounded.md}` (8px) on buttons, `{rounded.lg}` (12px) on
  cards — sober and editorial, never pill-shaped like most SaaS peers.
- **Layout trait**: atmospheric mountain-sunset hero photography paired
  with the recurring sunset-stripe band at the bottom of every page.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` for the full rationale before writing
   CSS or components — the "Do's and Don'ts" section is the fastest way to
   avoid drifting into pill-button, playful-SaaS territory.
2. Pull exact values from `references/design-tokens.yaml` (colors,
   typography scale, spacing scale, border-radius scale, component specs)
   rather than guessing hex codes or sizes.
3. Always include the sunset-stripe closing band at the foot of any
   full-page mockup — it is Mistral's continuity element across every
   surface.
4. Pair `PP Editorial Old` (display) with `Inter` (UI) — never substitute
   either with a generic system font for hero-scale text.
5. Cap buttons at 8px radius and cards at 12px radius; never introduce a
   pill shape outside of status badges.
6. Anchor heroes with photographic mountain-sunset imagery, or its visual
   equivalent — an atmospheric orange-to-yellow gradient sky.
