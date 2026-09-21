---
name: ollama-design
description: Ollama's marketing site is the most aggressively under-designed surface in AI tooling — a paper-white canvas, a 36px center-aligned SF Pro Rounded headline, a single black pill CTA, an inline `curl` install snippet, and a hand-drawn llama mascot as the only ornament. There is no gradient, no hero photography, no color beyond black/white/gray, and every interactive element collapses into a `{rounded.full}` pill. Use when asked for an "Ollama style", "Ollama-inspired UI", or a Markdown-README-like, radically minimal developer-tool marketing page.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/ollama/DESIGN.md
---

# Ollama Design System

Use this skill when a task calls for Ollama's radically minimal,
documentation-first marketing aesthetic: open-source developer-tool landing
pages, CLI-product pricing pages, or any explicit "Ollama style" request.

## Quick reference

- **Canvas**: `#ffffff` end-to-end with no surface alternation — the whole
  page is one continuous white sheet.
- **Accent**: none — pure black `#000000` is the entire brand color,
  carrying every CTA pill; there is no green, blue, or brand-tinted CTA
  anywhere in the system.
- **Type**: `SF Pro Rounded` (weight 500/600) for headings, the operating
  system's default `ui-sans-serif` for body, and `ui-monospace` for code —
  an intentionally "stock" typographic decision.
- **Corners**: `{rounded.full}` (pill) on every button, input, and pill
  chip; `{rounded.lg}` (12px) is the only other radius, reserved for the
  rare card. Nothing else rounds.
- **Layout trait**: the page reads like a rendered Markdown README — a
  single ~720px reading column, 88px section rhythm, and one inverted dark
  "Max" pricing card as the system's single "look here" moment.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` for the full rationale before writing
   CSS or components — the "Do's and Don'ts" section is the fastest way to
   avoid over-designing what should stay minimal.
2. Pull exact values from `references/design-tokens.yaml` (colors,
   typography scale, spacing scale, border-radius scale, component specs)
   rather than guessing hex codes or sizes.
3. Keep `colors.primary` (black) scarce per viewport — at most one black
   pill per fold across nav, hero CTA, and pricing-card CTA combined.
4. Default to `{rounded.full}` for every interactive element; reserve
   `{rounded.lg}` (12px) for the rare card and nothing else.
5. Render install commands and CLI examples inside the install-snippet or
   terminal-card components with `ui-monospace` — code is a first-class
   component here, not an afterthought.
6. Reserve the inverted dark surface (`colors.surface-dark`) for exactly
   one "look here" moment per page — never twice.
