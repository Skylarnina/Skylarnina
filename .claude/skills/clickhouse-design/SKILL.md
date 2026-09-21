---
name: clickhouse-design
description: ClickHouse's database marketing system — a near-pure-black canvas (#0a0a0a) with electric yellow (#faff69) as the single brand voltage, white Inter type at confident weight 700 with aggressive negative tracking, and SQL code blocks rendered directly in dark cards. Corners are compact (8-12px), no pill buttons, no second accent color. Use when asked for a "ClickHouse style", "ClickHouse-inspired UI", or a high-contrast black-and-electric-yellow developer/database marketing look.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/clickhouse/DESIGN.md
---

# ClickHouse Design System

Use this skill when a task calls for ClickHouse's stark, high-contrast
black-and-yellow developer aesthetic: database/data-infrastructure marketing
pages, engineering-grade dark dev-tool sites, or any explicit "ClickHouse
style" request.

## Quick reference

- **Canvas**: `#0a0a0a` near-pure black — the system has no light mode.
- **Accent**: electric yellow `#faff69`, used only on primary CTAs, large
  stat-callout numbers ("779+", "47k+"), and full-bleed yellow CTA bands —
  never as body-text color or a casual surface fill.
- **Type**: Inter everywhere — weight 700 for display (with -1 to -2.5px
  tracking), 600 for sub-titles/buttons, 400 for body; JetBrains Mono for
  code. No serif or second display family.
- **Corners**: compact — 8px on buttons/inputs, 12px on content and code
  cards, pill only on small tag badges.
- **Layout anchor**: real SQL code blocks and terminal output embedded
  directly in dark `surface-card` panels — the code IS the marketing
  voltage, not an illustration of it.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` before writing CSS — the Do's and
   Don'ts section is the fastest way to avoid diluting the yellow accent.
2. Pull exact values from `references/design-tokens.yaml` rather than
   guessing hex codes, sizes, or paddings.
3. Reserve yellow for CTAs, stat numbers, and full-bleed CTA bands — if
   more than that turns yellow, dial it back.
4. Show actual SQL/code in `code-window-card`, not abstract illustrations
   of a database.
5. Rotate surface modes band-to-band (black canvas → dark feature card →
   yellow CTA card → black canvas → code window) rather than repeating the
   same surface twice in a row.
6. Keep display type at Inter weight 700 with negative tracking; never
   soften to 500 or round CTAs into pills.
