---
name: airbnb-design
description: Airbnb's consumer marketplace design system — a pure white canvas, deep near-black ink text, and a single voltage of Rausch coral (#ff385c) carrying every primary CTA, the search orb, and the heart save state. Type runs the modest-weight Airbnb Cereal VF (Circular fallback) and every interactive shape is soft: pill search bars, rounded property cards, circular buttons. Use when asked for an "Airbnb style", "Airbnb-inspired UI", or a warm, photography-led consumer marketplace/travel/booking interface.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/airbnb/DESIGN.md
---

# Airbnb Design System

Use this skill when a task calls for Airbnb's warm, generous, photography-first
consumer marketplace aesthetic: travel/booking sites, listing marketplaces,
review-and-rating heavy consumer apps, or any explicit "Airbnb style" request.

## Quick reference

- **Canvas**: pure white (`#ffffff`) with near-black ink (`#222222`) text —
  there is no dark mode on the public marketing surface.
- **Accent**: `#ff385c` ("Rausch") — the single brand color, used scarcely on
  primary CTAs, the search orb, and the heart save state. Sub-brand purples
  (Luxe) and magentas (Plus) exist but never appear in mainline marketing.
- **Type**: Airbnb Cereal VF (Circular fallback) at modest weights (500–700
  display, 400 body) — photography carries visual weight, not bold type.
- **Corners**: soft everywhere — 8px buttons, ~14px property cards, fully
  pill-shaped search bar and CTAs, circular hearts/orbs. No hard corners
  except the body grid.
- **Layout anchor**: photo-first property cards with floating "Guest
  favorite" badges, and a signature pill-shaped, segment-divided global
  search bar terminated by a circular Rausch search orb.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` for the full rationale before writing
   CSS or components — the "Do's and Don'ts" section flags the most common
   ways to drift from Airbnb's restrained, single-accent look.
2. Pull exact values from `references/design-tokens.yaml` (colors,
   typography scale, spacing scale, border-radius scale, component specs)
   rather than guessing hex codes or sizes.
3. Treat Rausch as scarce — one or two coral moments per page (CTA, search
   orb, saved-heart state) against 90% white + ink.
4. Round everything: buttons at 8px, cards at ~14px, search bars and pills
   at full radius. Reserve hard corners for nothing.
5. Lead listing/product cards with photography (1:1 or taller aspect ratio)
   and keep meta text (title, price, rating) minimal beneath the image.
6. For dark-mode or enterprise/SaaS requests, this skill doesn't apply — it
   documents Airbnb's light, consumer-marketplace surface only.
