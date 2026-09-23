---
name: opencode-ai-design
description: OpenCode's marketing-site design system — a warm cream canvas (#fdfcfc) and nearly-black ink (#201d1d) rendered entirely in Berkeley Mono, so the page reads like a manpage or static-site README rather than a typical SaaS site. The only "visual moment" is a single dark hero card mocking up the OpenCode terminal UI, and bracketed ASCII markers ([+], [-], [x]) stand in for every icon and bullet. Use when asked for an "OpenCode style", "OpenCode-inspired UI", or a terminal-native, monospace-only developer-tool marketing page.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/opencode.ai/DESIGN.md
---

# OpenCode Design System

Use this skill when a task calls for OpenCode's austere, terminal-native
marketing aesthetic: CLI/dev-tool landing pages, README-style product sites,
or any explicit "OpenCode style" request.

## Quick reference

- **Canvas**: `#fdfcfc` warm cream (never pure white, never dark by default)
  with nearly-black ink `#201d1d` for text.
- **Accent**: none on marketing chrome — the brand's only "color" is ink
  itself. A full Apple HIG semantic ramp (blue/red/orange/green) exists but
  is reserved for the in-product TUI, never for marketing CTAs.
- **Type**: **Berkeley Mono** for every single text role, from the 38px hero
  down to 14px footer copy — no sans-serif, no display face, anywhere.
- **Corners**: 4px (`rounded.sm`) on every interactive element; every
  container/section is a sharp 0px rectangle.
- **Layout anchor**: one full-bleed dark hero card mocking up the OpenCode
  TUI itself, plus `[+]`/`[-]`/`[x]` ASCII bracket markers used as bullets
  and toggles everywhere else.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first — the "Do's and Don'ts" section
   is the fastest way to avoid generic SaaS-slop when the whole brand is a
   single monospace typeface.
2. Pull exact values from `references/design-tokens.yaml` rather than
   guessing hex codes, sizes, or component paddings.
3. Set every text role — headline, body, button, caption, even copyright —
   in Berkeley Mono (or the documented open-source substitutes: JetBrains
   Mono, IBM Plex Mono, Geist Mono).
4. Use `[+]`, `[-]`, `[x]` ASCII bracket glyphs as the icon/bullet system
   instead of SVG icons; keep the semantic accent ramp confined to any
   in-product TUI mockup, never on marketing buttons.
5. Anchor exactly one dark (`surface-dark`) hero card per page as the TUI
   mockup centerpiece; keep every other section flat cream with only 1px
   hairline rules as dividers.
6. Stack sections at the 96px `spacing.section` rhythm with no decorative
   dividers, gradients, or shadows anywhere in the system.
