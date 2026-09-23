# Zapier Design System — Full Analysis

Adapted from the Zapier design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/zapier/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Zapier is the original "connect your apps" workflow-automation platform,
and its marketing surface today reads as confidently mature. The brand
pairs a warm-cream canvas (`colors.canvas` `#fffefb`) with a deep
coffee-ink text color (`colors.ink` `#201515`) and a single saturated
orange (`colors.primary` `#ff4f00`) CTA. The warmth in the neutrals —
slightly cream rather than pure white — is the brand's defining
temperature signal.

Type carries the second voice. The proprietary Degular Display family
carries hero displays at weight 500. The brand uses Inter for everything
else — sub-displays, body, button, eyebrow. The two-face pairing reads
as "the brand has its own typeface for the loud moments and uses the
workhorse for the rest" — modest and unflashy.

Cards are universally 12px (`rounded.md`). Buttons share the same 12px
radius — not pills, not square. The brand sits between the
friendly-rounded and technical-square camps at a deliberate middle
position.

**Key characteristics:**
- A single primary CTA color (`colors.primary` `#ff4f00`), saturated
  orange — the brand's conversion signature.
- A warm-cream canvas (`colors.canvas` `#fffefb`), not pure white — the
  temperature IS the brand voice.
- Deep coffee ink (`colors.ink` `#201515`), not pure black — warmth
  carries through to text.
- Proprietary Degular Display for hero scale, Inter for everything else
  — a strict two-face system.
- `rounded.md` (12px) for buttons and cards — the brand's
  middle-radius signature.
- A muted cream/coffee neutral ladder — `canvas-soft`, `mute`,
  `body-mid`, `body` — every neutral carries warmth, none are cool gray.

## Colors

### Brand & accent
- **Zapier Orange** — the single brand accent: every primary CTA pill,
  every conversion target. The saturated orange IS the brand.

### Surface
- **Canvas** — warm off-white page background.
- **Canvas Soft** — cream-tinted soft surface for cards and inset
  regions.

### Text
- **Ink** — deep coffee; every heading and primary text.
- **Ink Soft** — near-black with brown warmth.
- **Ink Mid** — mid-emphasis text.
- **Body** — default body text color.
- **Body Mid** — secondary body/metadata text.
- **Mute** — lowest-priority text: fine print, low-emphasis captions.

The brand doesn't surface a separate semantic palette on its marketing
pages — status and validation cues borrow from the ink-plus-orange
hierarchy instead.

## Typography

### Families
Two faces ladder the system: **Degular Display**, a proprietary
geometric display sans used for hero headlines at weight 500 (the
brand's typographic signature), and **Inter**, used for sub-displays,
body, links, buttons, and eyebrows at weights 400/500/600/700.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale (display-xl at
56px down to button-sm at 14.4px). Governing principles:
- **Degular Display 500 for hero, Inter for everything else** — strict
  role separation between the two faces.
- **Positive tracking on the Degular eyebrow** — 1px at 14px is the
  brand's signature label style.
- **Sentence-case headlines** — the brand never uppercases display
  sizes.

Degular Display is proprietary. Open-source substitutes: **Inter** at
weight 500 for hero scale comes closest, with **Mona Sans** at weight
500 as a softer alternative. For sub-display and body, Inter is already
the brand's actual second face.

## Components

Definitions live in `design-tokens.yaml → components`. Summary:
- **Buttons** — `button-primary` (the orange CTA), `button-secondary`
  (dark coffee-ink), `button-tertiary` (white outline), and `button-text`
  (text-only for cards/nav) — all sharing the 12px radius.
- **Cards** — `card-content`/`card-feature-cream` (the default cream
  card), `card-feature-dark` (a polarity-flipped dark coffee card), and
  `pricing-card`/`pricing-card-featured` (a default pricing tier plus
  its polarity-flipped featured counterpart).
- **Inputs** — the canonical text input: white background, ink border,
  a slightly tighter 6px radius.
- **Navigation** — a sticky cream top nav and a dark coffee footer with
  cream-tinted link text.
- **Signature bands** — `hero-band`/`hero-band-dark` (the cream hero and
  its dark counterpart), `content-band-cream`/`content-band-light`
  (the sections that follow), `eyebrow-uppercase` (the small UPPERCASE
  Degular eyebrow above section headlines), and `badge-pill` (an inline
  pill for metadata/tags).

## Layout

- Base spacing unit: 4px, with tokens from `spacing.xxs` (2px) up to
  `spacing.4xl` (64px).
- Section bands use `spacing.4xl` (64px) top/bottom; card interiors sit
  at `spacing.xl` (24px).
- The marketing container runs roughly 1280px wide, centered with
  gutters. The hero splits headline-left/illustration-right at desktop
  and stacks at mobile; the pricing-tier grid runs 3-4 up at desktop.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 — Flat | No shadow, no border | Default for the hero |
| 1 — Hairline | 1px solid ink border | Pricing-tier card chrome, outline buttons |
| 2 — Soft Card | Cream fill against the page canvas | Default content cards — surface contrast carries elevation |

## Shapes

| Token | Value | Use |
|---|---|---|
| rounded.none | 0px | Full-bleed bands |
| rounded.sm | 6px | Inline pills, form inputs |
| rounded.md | 12px | The brand's canonical button + card radius |
| rounded.pill | 9999px | Status pills, badges |
| rounded.full | 9999px | Circular icon containers |

## Do's and don'ts

**Do**
- Reserve `colors.primary` Zapier orange for every primary CTA — the
  saturated orange IS the conversion signature.
- Keep the canvas warm — cream, not pure white; the temperature is the
  brand voice.
- Set hero headlines in Degular Display weight 500, sentence-case, no
  uppercase.
- Pair Degular Display (hero, eyebrow) with Inter (everything else) —
  two faces, two roles.
- Use `rounded.md` (12px) for buttons and cards — the middle radius is
  the brand's signature.
- Pair the orange CTA with ink-dark text on cream backgrounds — that
  three-token rhythm is the brand's whole conversion story.

**Don't**
- Don't replace the cream canvas with pure white; the warmth is the
  brand.
- Don't use pure black ink; the coffee-warmth in `#201515` carries
  through every text color.
- Don't render CTAs as pills; the brand's button is a 12px rounded
  rectangle.
- Don't introduce a second chromatic accent; orange plus cream plus
  coffee is the entire palette.
- Don't substitute Degular Display with a cool geometric sans (e.g. a
  generic Helvetica) — the brand's display face has warm proportions the
  substitute won't capture.

## Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Mobile | <768px | Hero stacks; grids go 1-up; hamburger nav |
| Tablet | 768-1023px | 2-up grids |
| Desktop | ≥1024px | Full grids; hero splits |

Buttons render roughly 48px tall (12px vertical padding plus a 27px
line), meeting WCAG AAA. The brand uses illustrative SVGs of zaps and
workflows plus product screenshots inside `rounded.md`-framed cards;
photography is rare.

## Known gaps

- The token values here are extracted directly from the source analysis
  and should be treated as canonical for this skill.
- The source also carries an "Examples (illustrative)" block of
  auto-derived kit-mirror surfaces (pricing tiers, product selectors,
  data tables, auth cards, and similar) that re-skin these same
  primitives for adjacent product categories; they are preserved in
  `design-tokens.yaml → components` under the `ex-*` keys for reference
  but are not native Zapier marketing components.
