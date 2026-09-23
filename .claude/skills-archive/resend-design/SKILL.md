---
name: resend-design
description: Resend's marketing-site design system — a pure-black canvas (#000000) carrying a 76-96px editorial Domaine Display serif headline as its loudest element, paired with ABC Favorit for prose, Inter for UI, and Geist Mono for code. Depth comes entirely from translucent-white hairline borders (6%/14% opacity) and low-opacity atmospheric glows in six accent hues, never drop shadows, and the primary CTA is a small white pill with black text — the brightest pixel on the page. Use when asked for a "Resend style", Resend-inspired UI, or a black-canvas developer-tool marketing page with editorial serif typography.
metadata:
  author: adapted from voltagent/awesome-design-md (MIT License)
  version: "1.0.0"
  source: https://github.com/voltagent/awesome-design-md/blob/main/design-md/resend/DESIGN.md
---

# Resend Design System

Use this skill for developer-tool or API-product marketing pages that want
Resend's confident, literary black-canvas register: pure black background,
oversized serif headlines, and code-forward proof points rather than
illustration or gradient art.

## Quick reference

- **Canvas**: true black `#000000` on every public page — never near-black,
  never a light mode.
- **Accent**: the brand's real accent is white itself — `button-primary`
  (a white pill, black text) is the single brightest surface per viewport.
  Six low-opacity glow colors (orange, yellow, blue, green, red) exist only
  as atmospheric section washes, never as solid buttons or fills.
- **Type**: a four-family stack — **Domaine Display** serif for 76-96px
  hero headlines (`lineHeight: 1.0`, `ss01/ss04/ss11` features on), **ABC
  Favorit** for marketing prose, **Inter** for UI labels, **Geist Mono** for
  code.
- **Corners**: `rounded.md` (8px) on buttons/inputs, `rounded.lg` (12px) on
  cards/code wells/email mockups, `rounded.full` on pills and avatars.
- **Layout anchor**: no drop-shadow elevation language at all — every
  surface is either a translucent-white hairline border or an atmospheric
  radial glow; code wells and email-mockup insets are the visual anchors of
  each section.

Full color/typography/spacing/component token values:
`references/design-tokens.yaml`

Full written analysis (overview, elevation, shapes, do's/don'ts, responsive
behavior, known gaps): `references/design-system.md`

## How to apply it

1. Read `references/design-system.md` first — the Do's and Don'ts section
   is the fastest way to avoid a generic "near-black SaaS" default instead
   of Resend's true-black, serif-led register.
2. Pull exact values from `references/design-tokens.yaml` rather than
   guessing — hex/rgba codes, the four-family type scale, spacing, and
   component specs are all defined there.
3. Build every surface's depth from translucent-white hairline borders
   (6%/14% opacity tokens) — never add a conventional drop shadow.
4. Reserve the six accent-glow tokens for low-opacity radial washes at the
   top of a section; never render them as a solid button or card fill.
5. Set hero headlines in Domaine Display (or the Söhne/Tiempos Headline
   substitute) at `lineHeight: 1.0` with the stylistic-set features on.
6. Keep `button-primary` (the white pill) to one per viewport — it's meant
   to read as the single brightest pixel on the page.
