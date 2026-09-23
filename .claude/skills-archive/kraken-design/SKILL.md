---
name: kraken-design
description: Kraken's crypto-exchange marketing system — a clean white canvas carrying Kraken Purple (#7132f5) as the commanding brand color, bold negative-tracked display headlines in the proprietary Kraken-Brand face, and a restrained 12px-radius button system with whisper-level shadows. A single green accent (#149e61) marks success/positive states only. Use when asked for a "Kraken style", "Kraken-inspired UI", or a trustworthy, professional crypto-exchange marketing/product page.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/kraken/DESIGN.md
---

# Kraken Design System

Use this skill when a task calls for Kraken's clean, trustworthy crypto-exchange
marketing aesthetic: fintech/crypto landing pages, exchange dashboards, or any
explicit "Kraken style" request.

## Quick reference

- **Canvas**: `#ffffff` — pure white surface throughout; no dark mode
  documented.
- **Accent**: Kraken Purple `#7132f5`, with darker variants `#5741d8` and
  `#5b1ecf` for borders/depth — reserved for CTAs, brand marks, and links.
- **Type**: dual-font system — `Kraken-Brand` (bold 700, negative tracking)
  for display headings, `Kraken-Product` (IBM Plex Sans fallback) for UI/body.
- **Corners**: 12px is the ceiling for buttons — rounded but never pill;
  cards go up to 16px.
- **Layout trait**: whisper-level shadows (`rgba(0,0,0,0.03) 0px 4px 24px`)
  replace hard elevation; near-black `#101114` text on a cool blue-gray
  neutral scale keeps the interface calm and professional.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` for the full rationale before writing
   CSS or components — the "Do's and Don'ts" section is the fastest way to
   avoid drifting into pill-button or oversaturated-purple territory.
2. Pull exact values from `references/design-tokens.yaml` (colors,
   typography scale, spacing scale, border-radius scale, component specs)
   rather than guessing hex codes or sizes.
3. Cap every button and interactive corner at 12px radius — never round
   further into a pill shape.
4. Use `Kraken-Brand` (or an IBM Plex Sans / Helvetica fallback) for display
   headings with negative letter-spacing; keep body and UI text in
   `Kraken-Product`.
5. Reserve the green accent (`#149e61`) strictly for success/positive
   badges — never as a second brand color.
6. Keep shadows subtle-to-invisible; depth comes from soft borders and the
   whisper shadow tokens, not heavy elevation.
