# Linear Design System — Full Analysis

Adapted from the Linear marketing-site design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/linear.app/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Linear's marketing canvas is the deepest dark surface in this collection —
`colors.canvas` is `#010102`, essentially pure black with a faint blue tint.
On top sits a four-step surface ladder (`surface-1` through `surface-4`) for
cards, panels, and lifted tiles, with hairline borders running from
`hairline` (`#23252a`) up through `hairline-strong` and `hairline-tertiary`.
Light gray text (`ink` `#f7f8f8`) carries the body and headlines.

The single chromatic accent is Linear lavender-blue (`primary` `#5e6ad2`) —
used on the brand mark, focus rings, and the primary CTA button. A lighter
hover state (`primary-hover` `#828fff`) and a focus-tinted variant
(`primary-focus` `#5e69d1`) extend the same hue. Linear avoids saturated
greens, oranges, reds, etc. on the marketing canvas — the only semantic
color is `semantic-success` (`#27a644`) for status pills.

Display type runs a custom sans (SF Pro Display fallback) at weight
500–700 with negative letter-spacing scaling from -3.0px at 80px down to 0
at body size. The body family is a separate text cut, and a monospace face
is reserved for code snippets in product screenshots.

The page rhythm is dense product screenshots — marketing leads with
high-fidelity captures of the product UI framed in `surface-1` panels with
16px (`rounded.xl`) corners. Chrome stays minimal so the screenshots carry
the page.

**Key characteristics:**
- Dark-canvas marketing system — near-pure-black canvas.
- Lavender-blue brand accent used scarcely: brand mark, focus, primary CTA.
- Four-step surface ladder carries hierarchy without shadow.
- Display tracking pulls aggressively negative (-3.0px at 80px); body holds
  near 0.
- Cards use 12px (`rounded.lg`) corners with 1px hairline borders — rarely
  16px, never pill.
- Product UI screenshots dominate; marketing chrome is a dark frame for the
  app.
- No second chromatic color, no atmospheric gradients, no spotlight cards.

## Colors

### Brand & accent
- **Primary** — signature accent: primary CTA, brand mark, link emphasis.
- **Primary hover / focus** — lighter and focus-ring tints of the same hue.
- **Brand-secure** — muted lavender-gray for "security" surfaces.

### Surface
- **Canvas** — default page background, near-pure black.
- **Surface 1–4** — a four-step lift ladder for cards, panels, hovered/
  featured states, and sub-nav/dropdowns.
- **Hairline / hairline-strong / hairline-tertiary** — 1px border tiers.
- **Inverse canvas/surface** — white surfaces used on a small set of inverse
  CTA pills.

### Text
- **Ink** — headlines and emphasized body.
- **Ink-muted / ink-subtle / ink-tertiary** — descending secondary,
  tertiary, and disabled/footnote tiers.

### Semantic
- **Success** — the only semantic color used on marketing (status pills).
- **Overlay** — pure-black modal scrim.

## Typography

### Families
- **Display** — custom display sans (SF Pro Display fallback); carries
  display-xl through subhead.
- **Text** — a separate text-tuned cut for body sizes, button labels,
  captions.
- **Mono** — reserved for code snippets in product screenshots and status/ID
  tokens.

Open-source substitutes: **Inter** (500/600/700) or **Geist Sans** for
Display/Text; **JetBrains Mono** or **Geist Mono** for Mono.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale (display-xl 80px
down to caption 12px). Principles:
- Aggressive negative tracking on display (-3.0px at 80px).
- One continuous voice from display (weight 600) to body (weight 400) — the
  family change between Display and Text is silent.
- Eyebrow uses positive tracking (+0.4px) as contrast against the
  negative-tracked display type.
- Mono only appears inside product-screenshot contexts, never on marketing
  chrome directly.

## Layout

- Base spacing unit: 4px. Full scale in `design-tokens.yaml → spacing`.
- Card interior padding: 24px (feature/pricing), 32px (testimonial), 48px
  (CTA banners).
- Pill button padding: 8px vertical / 14px horizontal.
- Max content width ~1280px; card grids 3-up desktop → 2-up tablet → 1-up
  mobile.
- The dark canvas *is* the whitespace — sections separate by lifting onto
  surface-1 panels rather than by gaps in white space. 24px gaps within a
  panel, 96px between sections.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 flat | no shadow/border | body type, hero text, footer |
| 1 | surface-1 + 1px hairline | default cards, product panels |
| 2 | surface-2 + 1px hairline-strong | featured pricing card, hover |
| 3 | surface-3 | sub-nav, dropdowns |
| 4 focus | 2px primary-focus outline @ 50% opacity | focused input/button |

Depth comes from the surface ladder plus hairline borders — drop shadows on
dark are avoided almost entirely. Product screenshots are the main
decorative depth; no atmospheric gradients, no spotlight cards. A subtle
white edge highlight on the top of lifted panels gives a faint "pixel
rendered" feel.

## Shapes

| Token | Value | Use |
|---|---|---|
| rounded.xs | 4px | chips, status badges |
| rounded.sm | 6px | inline tags |
| rounded.md | 8px | buttons, form inputs |
| rounded.lg | 12px | pricing/feature/testimonial cards |
| rounded.xl | 16px | product screenshot panels |
| rounded.xxl | 24px | oversized CTA banners (rare) |
| rounded.pill | 9999px | pricing-tab toggles, status pills |
| rounded.full | 9999px | avatar circles |

## Components

Definitions live in `design-tokens.yaml → components`. Summary:
- **Buttons** — primary (lavender fill), secondary (surface-1 + hairline),
  tertiary (plain text), inverse (white-on-dark). Primary has distinct
  hover/pressed states.
- **Pricing tabs** — pill toggle, default vs. selected (surface lift).
- **Cards** — pricing, pricing-featured, feature, product-screenshot (the
  dominant type), testimonial, customer-logo-tile.
- **Inputs** — text-input / text-input-focused, same surface with a
  focus-ring outline rather than a surface change.
- **Status & build** — changelog-row, status-badge.
- **Navigation** — top-nav (56px, canvas background), footer (dense link
  grid, 64px/32px padding).

## Do's and don'ts

**Do**
- Reserve `canvas` (#010102) as the anchor surface — the faint blue tint is
  intentional.
- Use `primary` lavender only for: brand mark, primary CTA, focus ring, link
  emphasis.
- Use the four-step surface ladder for hierarchy; don't skip levels.
- Pair display weight 600 with body weight 400.
- Apply negative letter-spacing aggressively on display sizes.
- Let product UI screenshots be the protagonist of every section.
- Use 8px (`rounded.md`) corners on CTAs.

**Don't**
- Don't ship a light-mode marketing page.
- Don't use lavender as a section background or card fill.
- Don't add a second chromatic accent.
- Don't add atmospheric gradients or spotlight cards.
- Don't pill-round CTAs.
- Don't use true black (`#000000`) as the canvas.
- Don't combine multiple bright accents in product screenshot mockups.

## Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Desktop-XL | 1440px | default layout |
| Desktop | 1280px | 3-up card grid maintained |
| Tablet | 1024px | 3-up → 2-up |
| Mobile-Lg | 768px | pricing comparison becomes accordion; nav → hamburger |
| Mobile | 480px | single column; display-xl scales 80px → ~36px |

Touch targets: CTAs ≥40px tap height, pricing pills ≥36px (≥44px on touch),
form inputs ≥44px on touch. Product screenshots keep aspect ratio and never
crop; customer-logo marquee may collapse 6-up → 3-up below 768px.

## Known gaps

- The surface-ladder values are extracted directly from the site's CSS
  custom properties — treat them as canonical.
- Form-field error/validation styling wasn't visible on the inspected pages.
- Light mode isn't documented — the marketing site doesn't ship one.
- The in-product UI (issue/priority/label colors) uses a richer palette than
  the marketing site; those colors aren't captured here.
- The proprietary display/text/mono faces aren't public — use the
  open-source substitutes listed under Typography.
