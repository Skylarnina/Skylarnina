---
name: raycast-design
description: Raycast's marketing-site design system — a pure near-black canvas (#07080a) where the chrome IS the in-product command-palette UI scaled up to marketing size, with hairline borders instead of shadows, a single white CTA pill, and Inter typography with the ss03 stylistic set enabled site-wide. A signature red diagonal-stripe gradient band tops the home-page hero exactly once, while saturated category accents (yellow/red/green/blue) stay confined to extension-tile illustrations. Use when asked for a "Raycast style", "Raycast-inspired UI", or a dark, command-palette-led developer-tools marketing page.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/raycast/DESIGN.md
---

# Raycast Design System

Use this skill when a task calls for Raycast's "the marketing page is the
product" dark aesthetic: command-palette-style dev-tool marketing pages,
launcher/productivity-app sites, or any explicit "Raycast style" request.

## Quick reference

- **Canvas**: pure near-black `#07080a` with a faint four-step surface
  ladder (`canvas` → `surface` → `surface-elevated` → `surface-card`) that
  builds elevation without any drop shadows — the system is dark-only.
- **Accent**: a single white CTA pill (`#ffffff`) is the universal primary
  action; saturated category accents (yellow/red/green/blue) appear only
  inside extension-tile illustrations, never on chrome.
- **Type**: **Inter** with `font-feature-settings: "calt", "kern", "liga",
  "ss03"` enabled site-wide — the ss03 alternate `g` glyph is the brand's
  signature typographic detail.
- **Corners**: a tight 4-16px radius cluster (6px command-rows, 8px
  buttons, 10px feature cards, 16px hero mockup container) — never flat,
  never above 16px except full pills.
- **Layout anchor**: full-fidelity command-palette UI screenshots as the
  hero's load-bearing visual, plus a once-per-page red diagonal-stripe
  gradient band at the very top of the home hero.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first — the surface-ladder elevation
   model and the ss03 typography detail are what separate this from a
   generic dark SaaS theme.
2. Pull exact values from `references/design-tokens.yaml` instead of
   guessing hex codes, sizes, or component paddings.
3. Enable Inter's `ss03` stylistic set on the body element; without it the
   type reads as plain Inter rather than Raycast.
4. Build elevation from the surface-color ladder, never from box-shadows;
   every card gets a 1px hairline border (`#242728`) instead.
5. Anchor a command-palette mockup (real-looking UI, not illustration) as
   the hero's centerpiece, and use the red stripe gradient at most once per
   page, only in that hero band.
6. Keep saturated accent colors inside extension/app-icon illustrations
   only — chrome buttons and text stay white/gray/black.
