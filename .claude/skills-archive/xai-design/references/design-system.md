# xAI Design System — Full Analysis

Adapted from the xAI design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/x.ai/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

xAI is Elon Musk's frontier-AI lab, and the website wears that posture
with engineered restraint: a near-black canvas (`colors.canvas`
`#0a0a0a`) edge-to-edge, white outline pills as every interactive
element, and a single proprietary geometric sans, Universal Sans,
carrying every display headline at weight 400. There is no gradient
hero, no atmospheric backdrop, no product screenshot. The brand reads as
confidently sparse — a research lab announcing its work rather than a
SaaS marketing site.

Type is the second decisive voice. Universal Sans carries every display
at weight 400 (regular) with aggressive negative tracking (-2.4px at
96px, scaling down through the display ladder). For technical labels,
eyebrows, and metric counters, the brand pairs Geist Mono (uppercase,
1.4px positive tracking) — every section eyebrow reads more like a code
comment than a marketing label.

Every interactive element is a pill (`rounded.pill`, 9999px) with a 1px
white-translucent border. The button shape never varies — the same
translucent-white pill carries "Try Grok," "Read announcement," "Custom
Voices," "Sign up now," and every "Read" anchor. The pill is the entire
shape system.

**Key characteristics:**
- A single near-black canvas with white outline pills as the entire
  interactive vocabulary.
- Universal Sans weight 400 for display, Geist Mono uppercase tracked
  for labels — the two-face contrast IS the brand voice.
- Every button is a translucent-white pill outline; the brand almost
  never uses filled CTAs, with one exception (the white-filled Sign Up
  pill).
- Cards are tight 8px rectangles in a slightly lighter charcoal fill
  with a hairline border — no shadows.
- A muted accent palette of sunset-orange, dusk-purple, twilight-violet,
  and breeze-blue lives in the design tokens but appears rarely on the
  main marketing surface, reserved for product illustrations and icons.
- Massive negative letter-spacing on display headlines (-2.4px at 96px)
  gives the typography a precise, gathered look.

## Colors

### Brand & accent
- **White** (`colors.primary`) — the brand's primary "color": button
  outline, button-primary fill, all display text. White-on-near-black is
  the signature.
- **Sunset Orange / Sunset Soft** — a warm orange and its lighter
  variant, used inside product illustrations and accent moments.
- **Dusk Purple / Twilight** — deep purple and soft violet, used inside
  product illustrations.
- **Breeze Blue** — a soft blue illustrative accent.
- **Midnight** — a deep blue-black for illustrative backgrounds.

### Surface
- **Canvas** — the default near-black page background, the brand's only
  true surface.
- **Canvas Soft** — a slightly lighter dark fill for hovered nav items
  and tooltips.
- **Canvas Card** — the charcoal card fill used inside product-feature
  cards.
- **Canvas Mid** — a mid-dark used for nested surfaces and code-mockup
  backgrounds.
- **Hairline** — 1px solid dividers on dark surfaces.

### Text
- **Ink** — default text on the canvas, pure white.
- **Ink Hover** — a slightly off-white hover tone.
- **Body** — secondary body text, supporting copy in a lighter weight.
- **Body Mid / Mute** — mid-emphasis body and mute text: captions, fine
  print.

The brand doesn't surface a separate semantic palette on the marketing
site — validation cues use the white-on-canvas hierarchy instead.

## Typography

### Families
Two faces ladder the system: **universalSans**, the proprietary
geometric sans used for every display, body, button, and link role
(weight 400 only on the marketing surface — restraint is part of the
voice, with negative letter-spacing at display sizes as the visual
signature), and **GeistMono**, used for uppercase section eyebrows,
label captions, and metric counters at positive tracking (1.2-1.4px) and
12-14px sizes.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale (display-xl at
96px down to button-md at 14px). Governing principles:
- **Weight 400 for everything** — the brand never bolds; negative
  tracking and size hierarchy carry the emphasis work instead.
- **Tight negative tracking on display sizes** — reverting to neutral
  tracking loses the precision feel that defines the brand.
- **GeistMono uppercase for eyebrows** — tracked positively (1.4px) so
  the mono reads as a code comment.

universalSans is proprietary; the closest open-source substitute is
**Inter** weight 400 with -0.04em to -0.02em letter-spacing at display
sizes, with **Geist** as a second-best option. For mono, **Geist Mono**
is the documented brand companion, with **JetBrains Mono** or **IBM
Plex Mono** as alternates.

## Components

Definitions live in `design-tokens.yaml → components`. Summary:
- **Buttons** — `button-primary`, the rare white-filled pill used on a
  single Sign Up CTA; `button-outline-on-dark`, the canonical
  white-outline pill used for every other CTA; and `button-outline-sm`,
  the same treatment with tighter padding for card-cluster CTAs.
- **Cards** — `card-content` and `card-feature-product` share identical
  chrome: a charcoal fill, hairline border, 8px radius, and generous
  24px interior padding, hosting an SVG illustration plus headline, body,
  and an outline-pill CTA.
- **Inputs** — a standard dark text input with a hairline border and 8px
  radius.
- **Navigation** — a canvas-background sticky top nav, plus a footer
  band using the secondary body text color.
- **Signature components** — `hero-band` (the massive dark hero
  headline), `content-band` (a standard section preceded by an uppercase
  mono eyebrow), `eyebrow-mono` (the signature uppercase tracked label),
  and `divider-hairline` (the 1px line between section bands).

## Layout

- Base spacing unit: 4px, with tokens from `spacing.xxs` (2px) up to
  `spacing.4xl` (64px).
- Hero and content bands use `spacing.4xl` (64px) section padding on
  desktop; card interiors sit at `spacing.xl` (24px).
- Marketing content centers around 1200px; the product/announcement card
  grid runs 2-up at desktop, 1-up at mobile.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 — Flat | No shadow, no border | Default |
| 1 — Hairline | 1px solid hairline border | Card chrome, button outlines (with translucent white) |

The brand uses no shadows at all — hairline borders carry every
elevation cue in the system.

## Shapes

| Token | Value | Use |
|---|---|---|
| rounded.none | 0px | Full-bleed bands |
| rounded.sm | 8px | Card chrome (the brand's `--radius` value) |
| rounded.pill | 9999px | Every button — the brand's universal interactive shape |
| rounded.full | 9999px | Circular icon containers |

## Do's and don'ts

**Do**
- Reserve the near-black canvas as the only page surface — the brand is
  dark-canvas only.
- Set hero headlines in Universal Sans weight 400 with aggressive
  negative tracking; the precision IS the voice.
- Use the full pill (9999px) on every interactive element.
- Pair Universal Sans (sentence-case) with GeistMono UPPERCASE for
  eyebrows, labels, and metric counters.
- Use white-translucent borders for outline buttons — the brand never
  uses solid white borders on its outline pill.

**Don't**
- Don't introduce a light-mode counterpart; xAI is dark-canvas only.
- Don't bold display headlines; weight 400 is the entire scale.
- Don't use filled buttons broadly; outline pills are the norm and the
  white-filled Sign Up pill is the rare exception.
- Don't drop a drop-shadow on cards; hairline borders carry elevation.
- Don't substitute Universal Sans with a generic geometric sans without
  adjusting letter-spacing — the negative tracking is part of the brand.

## Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Mobile | <768px | Hero scales 96px → 48px; grids go 1-up; hamburger nav |
| Desktop | ≥768px | Full hero and 2-up grids |

Buttons render roughly 32-40px tall (8px vertical padding plus a 20px
line); mobile touch areas inflate to meet the WCAG 44×44px minimum. The
brand uses sparse SVG illustrations for product moments (Grok, Voice,
API) — there is no photography on the marketing surface.

## Known gaps

- The token values here are extracted directly from the source analysis
  and should be treated as canonical for this skill.
- The source also carries an "Examples (illustrative)" block of
  auto-derived kit-mirror surfaces (pricing tiers, product selectors,
  data tables, auth cards, and similar) that re-skin these same
  primitives for adjacent product categories; they are preserved in
  `design-tokens.yaml → components` under the `ex-*` keys for reference
  but are not native xAI marketing components.
