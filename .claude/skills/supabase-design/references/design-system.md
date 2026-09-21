# Supabase Design System — Full Analysis

Adapted from the Supabase marketing-site design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/supabase/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Supabase's design language is engineered for clarity above everything else.
Marketing surfaces sit on `colors.canvas` (pure white), with text rendered in
`colors.ink` (`#171717` — near-black, never pure black). Across the whole
system the only consistent chromatic event is the **emerald green primary**
(`colors.primary`, `#3ecf8e`), used as the filled CTA, an occasional accent
dot, and the wordmark's signature highlight. Everything else is a calibrated
grey ladder from `#ededed` (hairline-cool) to `#171717` (ink), with thin
black-on-white typography carrying most of the visual work.

Typography runs **Circular** at weight 500 for display and 400 for body. The
display tier uses tight negative letter-spacing (-1.92px at 64px) to pull the
rounded humanist letterforms into editorial density. There's no atmospheric
gradient, no full-bleed photography, and no dark-canvas marketing track — the
brand commits fully to white.

The product itself shows up as composited UI screenshots on every page:
dashboard tables, SQL editors, query builders, log streams. These screenshots
*are* the brand's argument. They sit inside 12px containers with subtle 1px
hairlines, often arranged 2-up or as a floating "stacked panes" composition
above the hero band.

**Key characteristics:**
- A single emerald primary (`#3ecf8e`) is the only chromatic event; everything
  else is monochrome.
- A white canvas marketing track with a greyscale hierarchy running from
  hairline-cool to ink.
- A custom humanist sans display tier at weight 500 with negative letter-
  spacing of -1.92px to -0.42px.
- Composited product-UI screenshots (dashboard, SQL editor, log stream) are
  the dominant decorative element — never photography, never illustration.
- Tight 6px/8px button radii — square-ish, technical, never pill-shaped.
- Code blocks render in deep `colors.canvas-night` (`#1c1c1c`) with monospace
  inline code — the brand's developer DNA is visible in every snippet.
- Pricing tiers use a dark inverted `colors.canvas-night` featured tier, not a
  green one — green is reserved for buttons and dot accents.

## Colors

> Source pages: home (`/`), `/database`, `/partners/integrations`,
> `/partners/integrations/powersync`, `/solutions/ai-builders`, `/pricing`.

### Brand & accent
- **Emerald** — the signature CTA color: filled-button background, brand
  wordmark accent, dot indicator.
- **Emerald deep** — the pressed-state lift of the primary.
- **Emerald soft** — a lighter emerald used in chart accents and product UI.
- **Accent purple / violet / yellow / pink / crimson / indigo / tomato** —
  rare accents reserved for integration logos and chart highlights; never
  system colors, never buttons.

### Surface
- **Canvas** — the default page background, white.
- **Canvas soft** — a barely-tinted off-white for alternating section bands.
- **Canvas night** — a deep near-black used in code blocks, dashboard
  mockups, and the featured pricing tier.
- **Canvas night soft** — a slightly lifted dark tone for nested dark chrome.
- **Hairline / hairline strong / hairline cool (1–3)** — the brand's grey
  ladder for borders and fine chrome work.

### Text
- **Ink** — default body text, near-black, never pure.
- **Ink secondary** — a slightly cooler near-black for body emphasis.
- **Ink mute / ink mute 2 / ink faint** — descending secondary, tertiary, and
  disabled/placeholder tiers.
- **On primary** — near-black (`#171717`), not white — the text color used on
  the emerald button. The button reads as a "lit" surface with dark type
  rather than a colored chip.
- **On dark** — white text used on canvas-night surfaces.

## Typography

### Families
- **Circular** — a proprietary geometric humanist sans by Lineto. Fallback
  chain: 'Helvetica Neue', Helvetica, Arial.
- **System mono** (`ui-monospace`, Menlo/Monaco/Consolas fallbacks) for code
  blocks.

Substitute with **Inter** at weight 500, `letter-spacing: -1.92px` at 64px,
when Circular isn't licensed — it's the closest open-source analogue.
**Geist Sans** is a viable second choice.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale (display-xxl 64px
down to caption/micro at 12-13px). Principles:
- Weight 500 across display reads as engineered rather than decorative.
- Negative tracking on display scales from -1.92px at 64px proportionally
  down — tightening the rounded humanist letterforms into editorial density.
- Code blocks always use system mono families; there's no proprietary mono
  webfont in this system.

## Layout

- Base spacing unit: 8px, with 2/4/12px sub-tokens for fine work.
- Section padding runs 64–96px on marketing surfaces.
- Card interior padding: 32px on feature/pricing cards.
- Marketing pages center in a ~1280px container with no edge-bleed — the
  brand keeps content inside the box, unlike full-bleed competitors.
- Pricing collapses 4-up → 2-up → 1-up at 1024/768px; product-UI mockups
  stack 2-up or overlap as panes within the same container.
- The brand relies on generous 64–96px section padding without atmospheric
  gradients — the white canvas itself is the design, and composited product
  mockups break up sections without needing decoration.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 | Flat, 1px hairline | Default cards |
| 1 | `0 1px 3px rgba(0,0,0,0.06)` | Subtle card lift |
| 2 | `0 8px 24px rgba(0,0,0,0.08)` | Floating composited UI mockups |
| 3 | `0 16px 48px rgba(0,0,0,0.12)` | Modal overlays, deep elevation |

### Decorative depth
Depth here is **product-UI mockups**, not gradients. Stacked dashboard/SQL-
editor/log panes composite together with subtle Level-2 shadows to suggest
spatial hierarchy.

## Shapes

| Token | Value | Use |
|---|---|---|
| rounded.xs | 4px | Form inputs, hairline tags |
| rounded.sm | 6px | Buttons (the brand's signature button radius), code blocks |
| rounded.md | 8px | Compact cards, alerts |
| rounded.lg | 12px | Pricing cards, feature cards, product mockups |
| rounded.xl | 16px | Modal dialogs, large container chrome |
| rounded.full | 9999px | Pill tags, avatars |

Photography is minimal. Customer-logo strips display wordmarks at a uniform
~24–32px height in greyscale; rare case-study cards use 4:3 photos inset in
12px containers.

## Components

Definitions live in `design-tokens.yaml → components`. Summary:
- **Buttons** — `button-primary-green` (dark text on green, pressed variant
  to `primary-deep`), `button-secondary-outline`, `button-on-dark`,
  `button-link` (plain text, underline on hover).
- **Cards** — `card-feature-light`, `card-pricing` and its inverted
  `card-pricing-featured` (canvas-night), `card-feature-dark`, `code-block`.
- **Inputs** — `text-input`, 6px radius, hairline border.
- **Navigation** — `nav-bar-light`, logo left, nav center, sign-in + filled
  CTA right.
- **Tags** — `pill-tag-green`, `pill-tag-soft`.
- **Footer** — `footer-light`, 4–5 link columns.

## Do's and don'ts

**Do**
- Reserve emerald for filled CTAs and the wordmark accent — it should appear
  sparingly.
- Render display tiers at weight 500 with negative letter-spacing.
- Use 6px radius for buttons — square-ish, never pill-shaped.
- Composite product-UI mockups inside 12px containers with subtle Level-2
  shadows.
- Use near-black text on the emerald button, not white — the brand's
  idiosyncratic choice.
- Apply system mono for every code block.

**Don't**
- Don't introduce additional accent colors as system colors — purples,
  yellows, and pinks belong inside chart points and integration logos only.
- Don't bump display weight above 500.
- Don't use pill-shaped buttons.
- Don't use white text on the emerald button.
- Don't add atmospheric gradients to hero bands.

## Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Wide | ≥1440px | Full container width; product mockups at full scale |
| Desktop | 1024–1440px | Default max-width; pricing 4-up |
| Tablet | 768–1023px | Pricing 2-up; mockups simplify to a single panel |
| Mobile | <768px | Pricing 1-up; hamburger nav; display drops 64 → 36px |

Buttons hit ≥36×36px on mobile with padding scaling up to meet WCAG AA; form
fields stay at a 36px minimum. Display tiers stair-step 64 → 48 → 36 → 28 →
22px, product-UI mockups simplify to a single primary panel on mobile, and
pricing tiers stair-step 4-up → 2-up → 1-up with the dark featured tier always
distinguished. Product mockups use `srcset` with mobile crops focused on the
most actionable inner panel.

## Known gaps

- Circular is proprietary; the documented Inter/Geist Sans substitutes
  approximate but don't exactly match its geometric-humanist metrics.
- Chart-accent colors (purple, violet, yellow, pink, crimson, indigo, tomato)
  are documented as rare accents but their exact usage rules beyond
  "integration logos and chart points" aren't fully specified in the source.
