---
name: supabase-design
description: Supabase's marketing-site design system — a white-and-near-black open-source database brand with one chromatic event, emerald green (#3ecf8e), a custom humanist sans display tier (Circular) at negative tracking, and dense composited product-UI screenshots (SQL editor, dashboard tables, log streams) as the only decorative element. Use when asked for a "Supabase style", "Supabase-inspired UI", or a quietly technical, near-monochrome developer-tool/database marketing page.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/supabase/DESIGN.md
---

# Supabase Design System

Use this skill when a task calls for Supabase's clean, technical, near-
monochrome developer-platform look: database/backend marketing pages,
open-source dev-tool landing pages, or any explicit "Supabase style" request.

## Quick reference

- **Canvas**: pure white (`#ffffff`) throughout marketing — no dark-canvas
  track, no atmospheric gradient.
- **Accent**: a single emerald green (`#3ecf8e`) — the only chromatic event
  in the system; everything else is a calibrated grey ladder from `#ededed`
  to `#171717`. Text on the green button is near-black, not white.
- **Type**: **Circular** (or Inter as substitute) at weight 500 for display
  with tight negative tracking (-1.92px at 64px), weight 400 for body.
- **Corners**: tight, square-ish 6px buttons — never pill-shaped; cards at
  12px.
- **Layout anchor**: composited product-UI screenshots (dashboard, SQL
  editor, log stream) dominate every section — never photography, never
  illustration.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first — the "Do's and Don'ts" section
   flags the brand's more counter-intuitive choices (near-black text on the
   green button, square-ish buttons, no gradients).
2. Pull exact values from `references/design-tokens.yaml` rather than
   guessing hex codes or sizes.
3. Treat emerald green as scarce — reserve it for the filled CTA and the
   wordmark accent; don't use it as a background wash.
4. Lead every section with a composited product-UI screenshot (dashboard
   table, SQL editor, or log stream), not photography or illustration.
5. Keep buttons at 6px radius, never pill-shaped — this is a deliberately
   "technical" button shape, distinct from most SaaS marketing sites.
6. For light-mode/white-canvas requests, this skill applies directly; the
   brand doesn't ship a dark marketing track outside of code blocks and the
   inverted pricing tier.
