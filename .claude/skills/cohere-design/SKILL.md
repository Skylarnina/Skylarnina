---
name: cohere-design
description: Cohere's 2026 enterprise-AI marketing system — a white editorial canvas punctuated by full-width deep-green (#003c33) and dark-navy (#071829) product bands, rounded 8-22px media cards, and a type split between a tight near-monospaced display serif (CohereText) and precise Unica77 Cohere Web body text. Use when asked for a "Cohere style", "Cohere-inspired UI", or a restrained, research-lab-cadence enterprise AI marketing page that trades gradients for photography and dark product panels.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/cohere/DESIGN.md
---

# Cohere Design System

Use this skill when a task calls for Cohere's sober, enterprise-AI marketing
aesthetic: command-center-style AI infrastructure pages, dark product/
solution bands, or an editorial research-publishing feel for blog/paper
listings — or any explicit "Cohere style" request.

## Quick reference

- **Canvas**: white, interrupted by full-width deep-green (`#003c33`) or
  dark-navy (`#071829`) product bands — never a mid-tone page background.
- **Accent**: near-black `#17171c` for primary pill CTAs; coral (`#ff7759`)
  for blog taxonomy chips; action blue (`#1863dc`) for editorial links.
  Color arrives through photography and dark bands, not decorative UI fill.
- **Type**: CohereText (near-monospaced display serif, weight 400, tight
  negative tracking) for huge declarative headlines; Unica77 Cohere Web for
  everything else; CohereMono for uppercase technical labels.
- **Corners**: rounded but not cute — 8px on chips/small media, 22px on
  signature media cards and placeholders, 32px pill CTAs.
- **Layout anchor**: monumental tight-tracked headline over a two-card hero
  (wide product mockup + narrower photography card), trust-logo strips with
  generous spacing, and dark agent-console product mockups.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first — its Do's and Don'ts section
   flags the two most common mistakes: turning coral/blue into broad
   decorative fills, and boxing every section into a card.
2. Pull exact values from `references/design-tokens.yaml` rather than
   guessing hex codes, sizes, or component paddings.
3. Start each page or section from a white canvas or a full-width dark
   green/navy band — avoid mid-tone backgrounds unless a specific
   form/CTA section calls for one.
4. Keep the display/body type split intentional: CohereText only for the
   monumental declaration, Unica77 for everything else — don't collapse
   them into one generic sans.
5. Let photography, dark product mockups, and abstract 3D media carry
   color; keep the UI shell itself flat and restrained.
6. Use coral chips and blue links only in editorial/research contexts —
   never as the main CTA system.
