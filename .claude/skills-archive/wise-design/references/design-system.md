# Wise Design System — Full Analysis

Adapted from the Wise design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/wise/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Wise, the global money-transfer brand, wears its identity in a single
signature pairing: a vivid lime-green primary (`colors.primary`
`#9fe870`) used as the CTA pill and brand accent, set against a pale
sage-tinted canvas (`colors.canvas-soft` `#e8ebe6`) that runs across the
hero band, and a near-black ink (`colors.ink` `#0e0f0c`) carrying a hint
of warmth from the brand's underlying olive cast. The brand reads more
like a calm Scandinavian magazine than a bank — generous whitespace,
large rounded cards, and an unusually heavy display sans set at weight
900 carrying every hero headline.

Display typography is the second decisive voice. The proprietary Wise
Sans family carries hero displays at weight 900 across scales from 64px
up to 126px on the largest hero. The brand pairs Wise Sans 900 with Inter
at weight 600 for sub-displays — the contrast between the chunky
proprietary face and Inter's neutrality creates a clear hierarchy: Wise
Sans for the brand moment, Inter for everything else.

Cards are universally pill-rounded — 24px (`rounded.xl`) is the brand's
signature card radius. Buttons take the same 24px pill-rectangle shape.
The brand never uses sharp corners on UI elements; the visual softness is
part of its friendly-fintech voice.

**Key characteristics:**
- A single lime-green CTA accent (`colors.primary` `#9fe870`) — the
  brand's universal primary action color, with no second accent.
- Two-face display typography — Wise Sans (proprietary, weight 900, hero
  scale) plus Inter (weight 600, sub-display scale). The contrast
  between them is the brand's typographic story.
- `rounded.xl` (24px) as the canonical card and button radius — generous
  and friendly.
- A sage-tinted canvas (`colors.canvas-soft` `#e8ebe6`) as the brand's
  hero surface, with white (`colors.canvas`) reserved for cards within
  the sage band.
- A full semantic palette — positive green, warning yellow, negative red
  families, each documented with content/hover/active variants for
  in-product use.
- A currency-converter card on the hero — the brand's signature
  interactive component, hosting from/to amount inputs.

## Colors

### Brand & accent
- **Wise Green** — the brand's universal CTA color: every primary
  button, every "Send money" pill, the logo accent.
- **Wise Green Hover** — a lighter green for the active state.
- **Wise Green Neutral** — a mid-saturation green used as a neutral
  active fill.
- **Wise Green Pale** — the lightest green for soft surface tints and
  badge backgrounds.

### Surface
- **Canvas** — pure white for card interiors.
- **Canvas Soft** — the sage-tinted page background, the brand's
  defining mood.

### Text
- **Ink** — near-black with a hint of olive warmth, the default text and
  headings color.
- **Ink Deep** — a deep forest-green ink used on positive-state
  surfaces.
- **Body** — secondary body text.
- **Mute** — the lowest-priority text: captions, placeholder, fine
  print.

### Semantic
- **Positive / Positive Deep** — success indicator and its pressed
  state.
- **Warning / Warning Deep / Warning Content** — caution indicator, its
  pressed state, and text-on-warning color.
- **Negative / Negative Deep / Negative Darkest / Negative Bg** —
  destructive/error red, its pressed state, highest-emphasis destructive
  text, and a dark maroon for destructive callout backgrounds.

### Brand accent — tertiary
- **Accent Orange** — bright peach used inside illustrative content and
  pricing cards.
- **Accent Cyan** — bright sky-blue used as a tertiary illustration
  accent.

## Typography

### Families
Two faces ladder the system: **Wise Sans**, a proprietary geometric sans
with an unusually heavy weight 900 used for all hero displays — always
at weight 900, never lighter on the marketing surface — and **Inter**,
used for sub-displays (weight 600), all body copy, and form labels,
loaded with contextual-alternate font features.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale (display-mega
at 126px down to caption at 12px). Governing principles:
- **Weight 900 for hero, weight 600 for everything else** — the brand's
  display ceiling is full-black weight; everything below is semibold.
- **Wise Sans for the brand voice, Inter for utility** — a strict role
  separation between the two faces.

Wise Sans is proprietary; open-source substitutes are **Inter** at
weight 900 or **Manrope** at weight 800/900 for the geometric heaviness,
with **Geist** at weight 800 as a passable second choice. For sub-display
and body, Inter is the brand's actual second face already, so no
substitution is needed there.

## Layout

- Base spacing unit: 4px, with tokens from `spacing.xxs` (2px) up to
  `spacing.3xl` (48px).
- Section padding uses `spacing.3xl` (48px) top/bottom on desktop bands;
  card interiors sit at `spacing.xl` (24px).
- The marketing container centers at roughly 1200px. The hero splits
  into headline-left / currency-converter-card-right at desktop, and
  stacks at mobile. Feature grids run 2-up or 3-up at desktop.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 — Flat | No shadow, no border | Default |
| 1 — Hairline on Dark | 1px solid ink border | Tertiary outline buttons, form inputs |
| 2 — Soft Card | Implicit flat white card on the sage canvas | Cards on the sage hero band |

The brand uses surface contrast — `canvas-soft` background against
`canvas` white cards — as its primary elevation cue rather than shadows.

## Shapes

| Token | Value | Use |
|---|---|---|
| rounded.none | 0px | Full-bleed bands |
| rounded.sm | 8px | Inline pills, small badges |
| rounded.md | 12px | Form inputs, smaller chrome |
| rounded.lg | 16px | Mid-size cards |
| rounded.xl | 24px | The brand's canonical button + card radius |
| rounded.pill | 9999px | Status pills and full-radius accents |
| rounded.full | 9999px | Circular icon containers |

## Components

Definitions live in `design-tokens.yaml → components`. Summary:
- **Buttons** — primary (lime-green pill), secondary (sage-tinted),
  tertiary (white outline), and a circular icon button, all sharing the
  24px shape and button typography/padding.
- **Cards** — the default white card, a sage-tinted feature card, a
  soft-green feature card, and a polarity-flipped dark card with
  lime-green text for promotional moments.
- **Currency-converter card** — the brand's signature interactive
  widget: a white, ink-outlined card hosting from/to amount inputs and
  currency selectors.
- **Inputs** — the canonical text input: white background, ink border,
  12px radius.
- **Navigation** — a sticky white top nav with ink text, plus a dark
  ink footer with sage-tinted text.
- **Signature bands** — a sage-canvas hero band and its polarity-flipped
  dark counterpart (lime-green headline on near-black), a white content
  band following the hero, and positive/negative status-pill badges.

## Do's and don'ts

**Do**
- Reserve `colors.primary` Wise green for every primary CTA — the
  lime-green pill is the brand's conversion signature.
- Set hero headlines in Wise Sans weight 900, never lighter.
- Use `rounded.xl` (24px) for buttons and cards — the generous radius is
  the brand's friendliness signature.
- Cycle page surfaces from the sage canvas to white cards; let surface
  contrast carry elevation.
- Use the full semantic palette (positive/warning/negative) for
  in-product status — never repurpose Wise green as a success indicator
  since it is the brand's CTA color.

**Don't**
- Don't introduce a second brand accent; Wise green is the sole identity
  color.
- Don't render the hero in weight 700 or lighter; the brand's display
  weight is 900.
- Don't render CTAs as sharp rectangles; the 24px pill geometry is
  non-negotiable.
- Don't pair the green CTA with a green background; the brand always
  sits Wise green on neutral surfaces (sage, white, or ink).
- Don't replace Wise Sans with a generic geometric sans for hero
  typography; the proprietary face is a core part of the brand's voice.

## Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Mobile | <768px | Hero stacks; converter card sits full-width below the headline; grids go 1-up |
| Tablet | 768-1023px | Grids go 2-up |
| Desktop | ≥1024px | Hero splits; full grids |

Buttons render roughly 48px tall (12px vertical padding plus a 24px
line), clearing WCAG AAA at all widths. Photography is sparse throughout
— the brand prefers illustrative SVGs and product mockups inside cards,
with small country-flag thumbnails inside currency rows.

## Known gaps

- The token values here are extracted directly from the source analysis
  and should be treated as canonical for this skill.
- The source also carries an "Examples (illustrative)" block of
  auto-derived kit-mirror surfaces (pricing tiers, product selectors,
  data tables, auth cards, and similar) that re-skin these same
  primitives for adjacent product categories; they are preserved in
  `design-tokens.yaml → components` under the `ex-*` keys for reference
  but are not native Wise components.
