---
name: composio-design
description: Composio's AI-agent tool-integration marketing system — a near-black canvas (#0f0f0f) with a single deep-electric-blue voltage (#0007cd) carrying every CTA, and abcDiatype in one sans family (weight 500 display, no bold) across display and body alike. The brand's defining component is a 2x2 grid of dark terminal/code panes with a radial blue spotlight glow behind it, used as the homepage hero anchor. Use when asked for a "Composio style", "Composio-inspired UI", or a serious, Vercel/Stripe-Docs-adjacent dark developer-infrastructure marketing page.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/composio/DESIGN.md
---

# Composio Design System

Use this skill when a task calls for Composio's dark, technical
developer-infrastructure aesthetic: AI-agent/tool-integration marketing
pages, dense API/toolkit landing sites, or any explicit "Composio style"
request.

## Quick reference

- **Canvas**: near-black `#0f0f0f`, with a pure-black `#000000` recessed
  tone reserved for terminal mockups and code blocks.
- **Accent**: deep electric blue `#0007cd` — the single voltage, carrying
  every primary CTA, the wordmark, and atmospheric radial spotlight glows.
- **Type**: abcDiatype (Inter substitute) across every role at weight 500
  for display — confident but never bombastic; JetBrains Mono for code.
- **Corners**: compact developer-ergonomic radii — 8px CTAs, 12-16px
  cards. No full pills except tiny section-label badges.
- **Layout anchor**: a signature 2x2 grid of dark code/output terminal
  panes with a centered radial blue spotlight glow behind it, anchoring the
  homepage hero.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first — the Do's and Don'ts section
   flags the temptation to round CTAs into full pills or dilute the single
   blue accent.
2. Pull exact values from `references/design-tokens.yaml` rather than
   guessing hex codes, sizes, or paddings.
3. Reserve the electric-blue accent for primary CTAs, the wordmark, and
   spotlight-glow backdrops — cyan and violet are illustrative-only, never
   action colors.
4. Use brightness-step elevation (canvas → surface-card →
   surface-card-elevated) instead of drop shadows for depth.
5. Anchor the homepage hero with the 2x2 terminal-mockup grid and a
   centered radial blue glow rather than an illustration.
6. Keep every CTA at `rounded.md` (8px) — never a full pill; that
   compactness is what signals "developer tool" over "consumer brand."
