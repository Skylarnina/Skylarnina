---
name: nvidia-design
description: NVIDIA's engineering-grade marketing system — a two-mode canvas that alternates deep black hero/footer chapters with flat paper-white body sections, connected by a single almost-violently-saturated NVIDIA Green (#76b900) accent that carries every CTA, active tab, and decorative corner square. Everything is unapologetically angular (2px radius everywhere) in a tight bold NVIDIA-EMEA sans, with no gradients, no drop shadows, and no second accent color. Use when asked for an "NVIDIA style", "NVIDIA-inspired UI", or a technical, engineering-documentation-flavored marketing page for hardware/AI-infrastructure brands.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/nvidia/DESIGN.md
---

# NVIDIA Design System

Use this skill when a task calls for NVIDIA's engineering-documentation
marketing aesthetic: hardware/AI-infrastructure landing pages, enterprise
tech marketing, or any explicit "NVIDIA style" / "NVIDIA-inspired" request.

## Quick reference

- **Canvas/background**: alternates black (`#000000`) hero/footer chapters
  with a plain white (`#ffffff`) body canvas in predictable rhythm down the
  page — never both at once in the same section.
- **Accent color(s)**: exactly one — NVIDIA Green (`#76b900`) — carrying
  every primary CTA, active tab, dark-surface link, and the small decorative
  corner squares. Nothing else competes for attention.
- **Type approach**: proprietary NVIDIA-EMEA sans at weights 400/700 only —
  hierarchy built almost entirely from weight and size, never color tinting.
- **Corner-radius feel**: aggressively angular — `2px` (`rounded.sm`) on
  every interactive element and card; nothing exceeds it except avatar/icon
  circles.
- **Distinctive layout trait**: a small ~12px solid-green square anchored to
  one corner of resource and feature cards — the system's signature
  ornamental device, replacing decoration everywhere else.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` for the full rationale before writing
   CSS or components — the "Do's and Don'ts" section explains why the green
   must stay scarce and the geometry must stay sharp.
2. Pull exact values from `references/design-tokens.yaml` (colors,
   typography scale, spacing scale, border-radius scale, component specs)
   rather than guessing hex codes or sizes.
3. Alternate black chapter sections (hero, footer, CTA strips) with white
   body sections at a predictable `spacing.section` (64px) rhythm — the
   background swap IS the section divider, not a decorative rule.
4. Treat NVIDIA Green as precious: reserve it for the primary CTA, active
   states, and the corner-square motif; never introduce a second accent
   color for variety.
5. Keep every button, card, and input at `rounded.sm` (2px) — resist the
   urge to soften corners into pills or larger radii.
6. Build hierarchy from font weight (400 vs 700) and size only; body text
   stays a consistent ink/body color regardless of section context.
