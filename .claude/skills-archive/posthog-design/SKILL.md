---
name: posthog-design
description: PostHog's marketing-site design system — a warm cream canvas (#eeefe9, never white) dotted with hand-drawn hedgehog mascots like marginalia in a sketchbook, rejecting the typical somber dark-tech developer-tools aesthetic. IBM Plex Sans Variable carries every text role with weight contrast (400-800) doing most of the hierarchy work, a single yellow-orange CTA pill (#f7a501) is the only saturated color, and pastel callout banners mark tips/warnings inside documentation. Use when asked for a "PostHog style", "PostHog-inspired UI", or a playful, illustration-led developer-tools/product-analytics marketing page.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/posthog/DESIGN.md
---

# PostHog Design System

Use this skill when a task calls for PostHog's friendly, sketchbook-style
developer-tools aesthetic: product-analytics marketing pages, docs sites
that want a warm engineering-blog feel, or any explicit "PostHog style"
request.

## Quick reference

- **Canvas**: warm cream `#eeefe9` running edge-to-edge with no surface
  alternation between sections — the page is one continuous cream sheet.
- **Accent**: a single yellow-orange CTA pill `#f7a501` with deep-olive text
  — the brand's only saturated chromatic moment; pastel callout banners
  (blue/green/red/purple) exist only inside doc article bodies.
- **Type**: **IBM Plex Sans Variable** everywhere, with hierarchy built from
  weight contrast (400/500/600/700/800) more than from size jumps.
- **Corners**: tight 4-8px radius (`rounded.md` = 6px) on nearly every card
  and CTA; fully-rounded pills only for filter chips and the sticky nav CTA.
- **Layout anchor**: hand-drawn hedgehog mascot illustrations scattered
  across the layout as the entire decorative system — no gradients, no
  atmospheric mesh, no dark hero chapters.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first — it explains the "engineering
   sketchbook" contradiction (serious analytics product, playful chrome)
   that drives every visual choice.
2. Pull exact values from `references/design-tokens.yaml` instead of
   guessing hex codes, sizes, or component paddings.
3. Use `#eeefe9` cream — never pure white — as the page body on every
   section; there is no gray/dark alternation between bands.
4. Build hierarchy from IBM Plex Sans Variable weight steps (400 → 800)
   rather than introducing a second typeface or large size jumps.
5. Anchor hand-drawn hedgehog illustrations in card margins as the brand's
   signature decoration; reserve the yellow CTA pill for primary actions
   only.
6. Confine the four pastel callout colors (blue/green/red/purple) to inline
   tip/warning/note banners inside documentation — never as marketing-card
   backgrounds.
