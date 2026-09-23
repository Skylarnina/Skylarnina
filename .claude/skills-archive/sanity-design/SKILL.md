---
name: sanity-design
description: Sanity's marketing-site design system — a near-black canvas (#0b0b0b) treated as the tool's natural habitat rather than a "dark mode," with waldenburgNormal display type set at extreme negative tracking (down to -4.48px at 112px) for a precision-engineered, machined feel. A pure achromatic gray ladder carries structure while a coral-red CTA (#f36458) and electric-blue hover state (#0052ef) punctuate the dark field like signal lights, and every primary button is a full 99999px pill. Use when asked for a "Sanity style", "Sanity-inspired UI", or a nocturnal, precision-typography-led developer-content-platform marketing page.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/sanity/DESIGN.md
---

# Sanity Design System

Use this skill when a task calls for Sanity's nocturnal, precision-engineered
developer-content-platform aesthetic: structured-content/CMS marketing pages,
dark technical-brand sites, or any explicit "Sanity style" request.

## Quick reference

- **Canvas**: near-black `#0b0b0b` as the primary, default surface — not a
  toggled dark mode — with a pure achromatic gray ladder (`#0b0b0b` →
  `#212121` → `#353535` → `#797979` → `#b9b9b9` → `#ededed` → `#ffffff`)
  and no warm/cool tint anywhere in the neutrals.
- **Accent**: coral-red `#f36458` for the primary CTA, electric blue
  `#0052ef` as the universal hover/active signal across every interactive
  element, plus rare wide-gamut neon green and magenta for specialized
  premium/success moments.
- **Type**: proprietary **waldenburgNormal** with extreme negative tracking
  at display sizes (-4.48px at 112px), paired with **IBM Plex Mono** for
  code and technical labels.
- **Corners**: pill (99999px) for every primary/secondary button, 3-6px
  for inputs and secondary containers, 12px for large feature cards — the
  system jumps straight from 12px to full pill with nothing in between.
- **Layout anchor**: full-bleed dark sections with content held in measured
  max-width containers; depth comes from surface-color shifts, never from
  drop shadows.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first — the achromatic-gray-plus-
   signal-color philosophy and the extreme display tracking are what make
   this read as Sanity rather than generic dark-mode SaaS.
2. Pull exact values from `references/design-tokens.yaml` instead of
   guessing hex codes, sizes, or component paddings.
3. Keep the neutral scale pure achromatic — never introduce a warm or cool
   tint to the grays.
4. Apply extreme negative letter-spacing (-2px to -4.48px) on display
   headings 48px and above, using Inter or Space Grotesk as an open
   substitute for waldenburgNormal.
5. Build elevation from surface-color steps (`#0b0b0b` → `#212121` →
   `#353535` → `#ffffff`) rather than shadows; use hairline borders for
   containment instead of floating cards.
6. Keep every primary/secondary button a full 99999px pill in coral-red or
   near-black, and shift every interactive element to electric blue
   (`#0052ef`) on hover/active.
