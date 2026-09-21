---
name: mintlify-design
description: Mintlify's documentation-infrastructure design system pairs cinematic atmospheric marketing heroes (sky-blue-to-cream gradient with cloud illustrations, dark teal-to-mint gradient with a rocket launch) with dense developer-grade documentation surfaces. Inter carries all UI prose, Geist Mono carries code, black-pill primary buttons dominate marketing, and a scarce Mintlify mint green (#00d4a4) marks accent CTAs and active states only. A 3-column documentation layout (sidebar / prose / TOC) anchors the developer experience. Use when asked for a "Mintlify style", "Mintlify-inspired UI", or a docs-platform marketing page that pairs a cinematic SaaS hero with dense developer documentation.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/mintlify/DESIGN.md
---

# Mintlify Design System

Use this skill when a task calls for Mintlify's dual-mode aesthetic:
documentation-platform marketing pages, docs sites with a 3-column layout,
or any explicit "Mintlify style" request.

## Quick reference

- **Canvas**: `#ffffff` for marketing and docs, with a dark `#0a0a0a` inversion
  reserved for the promo banner and code surfaces.
- **Accent**: Mintlify mint green `#00d4a4` — reserved for the hero "Get
  started" pill, checkmarks, the featured pricing tier border, and active
  docs states. Never a large surface color.
- **Type**: Inter for every UI surface (body, headings, nav, buttons); Geist
  Mono strictly for code blocks, inline code, and type signatures.
- **Corners**: `{rounded.full}` (pill) on every button; `{rounded.lg}` (12px)
  is the dominant card radius — no in-between corner softening.
- **Layout trait**: atmospheric gradient hero bands (sky-blue-to-cream on the
  homepage, dark teal-to-mint on the startups page) give way to a strict
  3-column documentation grid (sidebar ~240px / prose ~720px / TOC ~200px).

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` for the full rationale before writing
   CSS or components — the "Do's and Don'ts" section is the fastest way to
   avoid over-using the mint accent.
2. Pull exact values from `references/design-tokens.yaml` (colors,
   typography scale, spacing scale, border-radius scale, component specs)
   rather than guessing hex codes or sizes.
3. Reserve `colors.brand-green` for one accent CTA or active-state moment
   per viewport — it should never carry a large background.
4. Pair Inter (UI prose) with Geist Mono (code) exclusively — never
   introduce a third typeface or swap the two roles.
5. Use atmospheric gradient heroes only on top-level marketing pages; keep
   deeper documentation surfaces flat and dense at 14–16px body type with
   1.50 line-height.
6. For documentation layouts, hold the 3-column sidebar/prose/TOC structure
   and apply `{rounded.full}` to every button, `{rounded.lg}` to cards.
