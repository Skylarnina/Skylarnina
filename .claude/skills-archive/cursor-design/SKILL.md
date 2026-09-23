---
name: cursor-design
description: Cursor's AI-code-editor marketing system — a warm-cream editorial canvas (#f7f7f4, not IDE-dark, not pure white) with warm near-black ink, a single scarce accent of Cursor Orange (#f54e00), and CursorGothic display type at weight 400 (never bold) for a magazine-editorial voice. Its signature is a five-color pastel "AI timeline" pill palette (peach/mint/blue/lavender/gold) marking agent action stages inside in-product mockups only. Use when asked for a "Cursor style", "Cursor-inspired UI", or a quietly-confident, cream-canvas developer-tool marketing page that avoids the typical dark-IDE aesthetic.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/cursor/DESIGN.md
---

# Cursor Design System

Use this skill when a task calls for Cursor's editorial, warm-cream
developer-tool aesthetic: AI code-editor marketing pages, IDE-mockup-led
landing sites, or any explicit "Cursor style" request that should feel
calm and magazine-like rather than dark-IDE dramatic.

## Quick reference

- **Canvas**: warm cream `#f7f7f4` — never pure white, never dark. Ink is
  warm near-black `#26251e`, not pure black.
- **Accent**: Cursor Orange `#f54e00`, reserved for primary CTAs and the
  wordmark — used scarcely.
- **Type**: CursorGothic at weight 400 for both display and body — a
  magazine voice, never bold; JetBrains Mono on every code surface (code
  is roughly half the page).
- **Corners**: compact — 8px CTAs, 12px cards. Pill radius reserved for
  the AI-timeline pills and small badges, not CTAs.
- **Layout anchor**: a centered IDE-mockup card (multi-pane editor + chat
  + terminal) below the hero copy, plus the signature five-color pastel
  timeline-pill palette marking AI agent stages (Thinking / Grepping /
  Reading / Editing / Done) inside in-product visualizations only.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first — the Do's and Don'ts section
   flags the two easiest mistakes: bolding display type and scattering the
   timeline pastels onto non-timeline UI.
2. Pull exact values from `references/design-tokens.yaml` rather than
   guessing hex codes, sizes, or paddings.
3. Keep display type at CursorGothic weight 400 — bolding breaks the
   editorial, magazine-calm voice the brand depends on.
4. Use hairlines plus the white-card-on-cream contrast for depth; never
   add drop shadows.
5. Reserve the five timeline pastel pills for in-product agent-action
   visualizations only — never as general system action colors.
6. Render every code surface (inline, blocks, IDE panes) in JetBrains
   Mono, and keep Cursor Orange as the only CTA action color.
