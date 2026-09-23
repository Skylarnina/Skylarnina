---
name: elevenlabs-design
description: ElevenLabs' quietly editorial voice-AI marketing system — an off-white canvas (#f5f5f5) with warm near-black ink, where brand voltage is entirely photographic and atmospheric rather than chromatic: soft pastel gradient orbs (mint, peach, lavender, sky, rose) drift behind headlines instead of a saturated accent color. Display type runs a licensed serif, Waldenburg Light, at a deliberately un-bold weight 300, paired with Inter for body and a single near-black pill CTA. Use when asked for an "ElevenLabs style", "ElevenLabs-inspired UI", or a calm, magazine-like AI-product marketing page that avoids neon accents and dark developer-tool canvases.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/elevenlabs/DESIGN.md
---

# ElevenLabs Design System

Use this skill for ElevenLabs' calm, editorial voice-AI marketing
aesthetic: voice/audio-AI product pages, quietly premium SaaS marketing
sites, or any explicit "ElevenLabs style" request. It deliberately avoids
both the neon-accent AI-tool look and the dark developer-tools canvas.

## Quick reference

- **Canvas**: off-white (`#f5f5f5`) with warm near-black ink (`#0c0a09`) —
  no saturated CTA color anywhere in the system.
- **Accent**: none chromatic — the only "color" is five pastel atmospheric
  gradient orbs (mint, peach, lavender, sky, rose) used purely as
  decoration, never as fills or text colors.
- **Type**: licensed serif Waldenburg Light at weight 300 (never bold) for
  every display headline, with Inter at 400/500 and slightly loosened
  tracking (+0.15-0.18px) for body, nav, and captions.
- **Corners**: pill (`9999px`) on every CTA and badge, `16px`/`24px` on
  cards — soft geometry throughout, no sharp `0px` buttons.
- **Layout anchor**: a near-black ink pill primary button plus a
  transparent outline secondary, with soft radial gradient orbs drifting
  behind hero and feature copy for atmosphere rather than illustration.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first, especially Do's and Don'ts —
   the biggest risk is reaching for a saturated brand color where the
   system stays monochrome plus atmosphere.
2. Pull exact values from `references/design-tokens.yaml` rather than
   guessing hex codes, weights, or spacing.
3. Keep every display headline in the serif face at weight 300 — never
   bold it, even for emphasis; size and negative tracking do the work.
4. Use gradient orbs (mint/peach/lavender/sky/rose) only as soft
   atmospheric backdrops behind headlines or inside dedicated orb cards —
   never as a button fill, text color, or card background.
5. Keep the near-black ink pill as the only primary CTA color, paired with
   a transparent-outline secondary button — both fully pill-shaped.
6. Maintain generous, print-magazine-style pacing: 96px between sections,
   soft hairline borders and a single subtle shadow tier for card
   elevation, never heavy shadows.
