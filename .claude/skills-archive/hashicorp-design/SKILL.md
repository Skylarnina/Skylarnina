---
name: hashicorp-design
description: HashiCorp's enterprise-infrastructure marketing system — a near-black canvas (#000000) with charcoal card surfaces, held together not by one brand color but by a system of per-product accents (Terraform purple, Vault yellow, Consul red, Waypoint cyan, Vagrant blue, Nomad green, Boundary coral) that act as identity tokens rather than decoration. Display type is hashicorpSans at 600/700 with tight line-heights against relaxed 500-weight body copy, and every CTA sits at a modest 8px radius rather than a pill. Use when asked for a "HashiCorp style", HashiCorp-inspired UI, or a multi-product developer-infrastructure marketing page where each section needs to visually signal which tool it belongs to.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/hashicorp/DESIGN.md
---

# HashiCorp Design System

Use this skill when a task calls for HashiCorp's dark, multi-product
developer-infrastructure aesthetic: DevOps/infra tooling marketing pages,
platform-engineering landing pages, or any explicit "HashiCorp style"
request.

## Quick reference

- **Canvas**: pure black (`#000000`) layered with charcoal `surface-1`
  cards and 1px translucent gray hairlines.
- **Accent(s)**: no single brand color — a **per-product palette** instead:
  Terraform purple (`#7b42bc`), Vault yellow (`#ffcf25`), Consul red
  (`#e62b1e`), Waypoint cyan (`#14c6cb`), Vagrant blue (`#1868f2`), Nomad
  green (`#00ca8e`), Boundary coral (`#f24c53`) — each product section uses
  its own accent consistently, never mixed with another product's.
- **Type**: hashicorpSans everywhere — display at weight 600/700 with tight
  1.17–1.21 line-heights, body at weight 500 with relaxed 1.50–1.71
  line-heights; that contrast is the brand's typographic voice.
- **Corners**: `8px` (`rounded.md`) on every CTA and input — never a pill;
  reads as developer-tool, not consumer-app.
- **Layout anchor**: product-identity cards — each HashiCorp tool gets its
  own colored card variant so a reader can tell which product a section
  covers from the corner of their eye.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` for the full rationale before writing
   CSS or components — the "Do's and Don'ts" section explains the
   per-product color discipline in detail.
2. Pull exact values from `references/design-tokens.yaml` (colors,
   typography scale, spacing scale, border-radius scale, component specs)
   rather than guessing hex codes or sizes.
3. When a section is about a specific HashiCorp-style product, pick that
   product's accent token and use it consistently for the section pill,
   the CTA button, and (where appropriate) the showcase card background —
   never mix two product accents in the same viewport.
4. Keep CTA corners at `rounded.md` (8px) — resist the temptation to round
   further into pill shapes.
5. Pair tight display line-heights (1.17–1.21) with relaxed body
   line-heights (1.50–1.71); the proportional gap is part of the voice.
6. Use surface lift (canvas → surface-1 → surface-2) for hierarchy on dark
   instead of drop shadows, and place an uppercase eyebrow above every
   meaningful section.
