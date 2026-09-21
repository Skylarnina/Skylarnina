---
name: starbucks-design
description: Starbucks' retail-flagship design system — a warm cream-and-ceramic canvas (#f2f0eb / #edebe9) built on a four-tier green brand system (Starbucks, Accent, House, Uplift) with gold reserved exclusively for Rewards-status ceremony. The proprietary SoDoSans face carries almost every surface at tight negative tracking, full-pill 50px buttons with a signature scale(0.95) press, and a floating circular "Frap" order CTA anchor the interaction language. Use when asked for a "Starbucks style", "Starbucks-inspired UI", or a warm, confident retail/food-and-beverage marketing and ordering experience.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/starbucks/DESIGN.md
---

# Starbucks Design System

Use this skill when a task calls for Starbucks' warm retail-flagship
aesthetic: coffee/QSR ordering flows, loyalty/rewards experiences, or any
explicit "Starbucks style" request.

## Quick reference

- **Canvas**: warm neutral cream (`#f2f0eb`) and ceramic off-white
  (`#edebe9`) — never pure white — referencing real café materials.
- **Accent**: a four-tier green system (Starbucks Green for headings,
  Green Accent for CTAs, House Green for deep feature/footer bands,
  Uplift for decorative touches) with gold (`#cba258`) reserved strictly
  for Rewards-status ceremony.
- **Type**: proprietary SoDoSans at tight `-0.01em`/`-0.16px` tracking
  for nearly everything, with a context-specific serif (Rewards) and
  script (Careers) swapped in only in their own contexts.
- **Corners**: every button is a 50px full pill; cards round to 12px with
  whisper-soft layered shadows rather than one heavy drop shadow.
- **Layout anchor**: a floating 56px circular "Frap" order button with a
  layered shadow stack, plus a color-block page rhythm alternating cream,
  white, and dark-green (`#1E3932`) bands.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first — the "Do's and Don'ts"
   section is the fastest way to avoid flattening the brand into "one
   generic green."
2. Pull exact values from `references/design-tokens.yaml` (colors,
   typography scale, spacing scale, border-radius scale, component specs)
   instead of guessing hex codes or sizes.
3. Map each green to its intended role — Starbucks Green for headings,
   Green Accent for CTAs, House Green for deep bands/footer, Uplift for
   decorative accents — never collapse them into a single brand green.
4. Use the warm cream/ceramic canvas instead of pure white, and keep
   SoDoSans tracking tight (`-0.01em`) across the whole system.
5. Round every button to the full 50px pill and apply `scale(0.95)` as
   the universal active-press state.
6. Reserve gold strictly for Rewards-status moments; never use it as a
   general-purpose accent.
