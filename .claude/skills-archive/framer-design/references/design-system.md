# Framer Design System — Full Analysis

Adapted from the Framer marketing-site design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/framer/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Framer's marketing pages sit on an almost-pure-black artboard —
`{colors.canvas}` is nearly black with a faint warmth — and everything else
is built on top of it. Oversized white display type in **GT Walsheim
Medium** carries the headlines, with letter-spacing pulled to extreme
negative values (-5.5px on the 110px display, -4.25px on the 85px hero).
The effect is closer to a poster than a typical SaaS hero: one assertive
statement per band, with generous air above and below it.

The system's only chromatic accent is `{colors.accent-blue}`, used sparingly
— hyperlinks, selection halos, a subtle blue-tinted ring on focused inputs.
Everything else in the chrome is monochrome: white pill buttons, charcoal
cards, gray secondary text. The real signature move is the rhythm break —
every few sections, a **vibrant gradient atmosphere card** drops in: a
magenta-violet spotlight, a sunset-orange wash, a coral-pink panel. These
aren't section backgrounds; they're individual cards inside a card grid,
each one working like a small living poster demonstrating what Framer can
produce.

Body type runs in **Inter Variable**, and Framer leans hard on Inter's
OpenType character variants (`cv01`, `cv05`, `cv09`, `cv11`, `ss03`, `ss07`,
`dlig`) to give the body voice a custom-tuned feel — single-storey "a,"
straight-leg "l," tabular figures. There's no light mode; dark IS the
brand.

**Key characteristics:**
- Black-canvas marketing system: `{colors.canvas}` covers hero, body,
  pricing, and footer alike — no light interludes.
- Massive negative letter-spacing on display sizes (-5.5px / -4.25px /
  -3.1px) creates poster-grade headline cadence.
- White pill (`{components.button-primary}`) is the only primary CTA
  shape; secondary actions live as charcoal pills or plain text links.
- Oversized gradient spotlight cards act as showcase tiles inside the dark
  grid — individual cards, never section backgrounds.
- Inter Variable with bespoke OpenType character variants everywhere body
  type appears — the typographic voice is unmistakable.
- Border radius runs from 4px utility chips up to 100px pills and full
  circles, with 15–20px the default for cards and 30px for gradient cards.
- A single chromatic accent, `{colors.accent-blue}`, reserved for
  hyperlinks, focus, and selection — never decorative.

## Colors

### Brand & accent
- **Pure white** — the brand primary surface: every primary CTA pill, every
  display headline, every body line on canvas.
- **Sky blue** — the single chromatic accent, limited to hyperlinks,
  focused-input rings, and a few selection states. Never a background or
  brand fill.

### Surface
- **Canvas** — default page background: near-black with a faint warmth,
  covering the footer, pricing, hero, and FAQ alike.
- **Surface 1** — one step above canvas: pricing cards, secondary buttons,
  mockup tiles.
- **Surface 2** — two steps above: featured pricing card, hero pill
  backdrop, selected pricing tab.
- **Hairline / hairline soft** — 1px dividers on input groups, comparison
  tables, FAQ rows, and footer column rules.
- **Inverse canvas** — pure white, used as the surface of light-on-dark
  pill CTAs and a handful of light-mode template thumbnails inside the
  showcase grid.

### Text
- **Ink** — all headline and emphasized body type, pure white.
- **Ink muted** — secondary gray type used for meta info, footer columns,
  comparison-row labels, and deselected pricing tabs. Hierarchy on the
  dark canvas comes from ink → ink-muted contrast, not weight shifts.

### Semantic
- **Success green** — pricing comparison-table checkmarks; a glyph fill,
  not a surface.

### Brand gradient (signature)
- **Gradient magenta / violet / orange / coral** — the four spotlight-card
  variants, with violet the most common. They sit as oversized atmospheric
  tiles inside otherwise monochrome grids — a dark canvas with one or two
  glowing spotlight cards is a recurring page signature.

## Typography

### Family
- **GT Walsheim Framer Medium / GT Walsheim Medium** — Framer's display
  typeface: geometric, slightly humanist, very confident at large sizes
  with extreme negative tracking.
- **Inter Variable** — the system body typeface, used with extensive
  OpenType character variants (`cv01`, `cv05`, `cv09`, `cv11`, stylistic
  sets `ss03`/`ss07`, discretionary ligatures `dlig`, tabular figures for
  numerics). This gives the body voice a bespoke feel without commissioning
  a custom face.
- **Inter** (non-variable) — used selectively for the 22px headline tier,
  where it catches small tracking targets the variable file rounds off.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale (display-xxl
110px down to button 14px). Principles:
- Letter-spacing scales hard with size: display-xxl pulls -5.5px (about 5%
  of size), while body sticks to roughly -1%. Posters at the top,
  comfortable reading at body.
- The OpenType character variants ARE the brand voice — switching off
  `cv11`, `ss03`, etc. visibly changes how the body copy reads.
- Weight stays in a narrow band: display at 500, body at 400, body-sm/
  caption at 500. Hierarchy comes from size and tracking, not a 700/900
  weight ramp.
- Line-heights stay tight everywhere, even body running at 1.30 — denser
  than typical SaaS marketing.

### Font substitutes
Without GT Walsheim Medium, reasonable open substitutes include **Mona
Sans**, **Geist**, or **Inter** at weight 600–700 with manually tightened
tracking. Mona Sans's hairline weights (100–300) are particularly close to
Framer's cleaner section openers. Inter Variable is already open source —
keep it as-is and preserve the documented OpenType variants.

## Layout

- Base spacing unit: 5px — Framer uses non-standard 5/10/15/20/30
  increments rather than the more common 4/8/16/24 scale.
- Card interior padding: 20px on pricing cards, 30px on gradient spotlight
  cards.
- Pill button padding: 10px vertical, 15px horizontal.
- Section padding runs roughly 96px on the home page, tightening to about
  64px on the pricing comparison section.
- Max content width sits near 1199px, with gutters scaling toward 30px on
  desktop.
- Home-page card grids run 2-up at desktop, collapsing to 1-up below
  810px; the pricing tier grid stays 4-up, with the comparison table
  beneath switching to horizontally scrolling columns at narrow widths.
- The dark canvas functions as the whitespace: rather than leaning on
  white air to separate sections, Framer leans on long stretches of black
  with a single oversized statement floating in the middle. Sections
  separate by mode change — charcoal cards, then black with a gradient
  spotlight, then back to charcoal — like cuts in a dark film.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 (flat) | No shadow, no border | Canvas-mounted display type, FAQ rows, footer |
| 1 (charcoal) | `{colors.surface-1}` lift on canvas | Pricing cards, mockup tiles, secondary buttons |
| 2 (light-edge) | White 0.5px top edge + soft black drop shadow | Floating product cards, modal cards |
| 3 (selected) | Translucent blue ring | Focused inputs, selected option |

Four shadow signatures recur across the home page: a subtle 1px drop, a
translucent blue ring, a thick near-black 2px outline marking the active
sub-nav element, and the layered light-edge-plus-drop-shadow used on
floating cards.

Decorative depth otherwise comes from gradient spotlight cards (the
dominant device — color saturation against black substitutes for
shadow-driven elevation), layered product mockups (browser frames holding
live Framer-built sites, shown inside surface-1 cards with the level-2
light-edge treatment), and the subtle blue focus/selection ring, which is
the only chromatic depth signal in the system.

## Shapes

Framer's extracted radius set is unusually granular (1, 4, 5, 6, 8, 10, 12,
15, 20, 30, 40, 100px). The named scale below covers what the marketing
surface actually uses.

| Token | Value | Use |
|---|---|---|
| rounded.xs | 4px | Small chip / utility radius |
| rounded.sm | 6px | Inline tag, badge |
| rounded.md | 10px | Form input, list item |
| rounded.lg | 15px | Template card thumbnails |
| rounded.xl | 20px | Pricing cards, mockup tiles |
| rounded.xxl | 30px | Gradient spotlight cards, oversized panels |
| rounded.pill | 100px | All primary text CTAs |
| rounded.full | 9999px | Circular icon buttons, avatar circles |

Embedded site mockups sit in 20px tiles with 15px interior padding.
Gradient spotlight cards go softer at 30px by design, to feel like
atmospheric panels rather than tight UI. Icon glyphs and sub-nav glyphs
render in full circles at 32–40px.

## Components

Definitions live in `design-tokens.yaml → components`. Summary:
- **Buttons** — button-primary (white pill), button-primary-pressed
  (scale-shrink, not a darker fill), button-secondary (charcoal pill),
  button-translucent (lifted secondary for busy backgrounds),
  button-icon-circular (40px circle).
- **Pricing tabs** — pricing-tab-default / -selected; selected communicates
  "active" through a surface lift, not a color fill.
- **Inputs** — text-input / text-input-focused, focus signaled by the
  level-3 translucent blue ring rather than a surface change.
- **Cards & containers** — pricing-card, pricing-card-featured (one
  surface step up, no chromatic outline), template-card,
  product-mockup-tile.
- **Gradient spotlight cards (signature)** — gradient-spotlight-card
  (violet, most common), -magenta, -orange; coral follows the same shape.
- **Comparison & FAQ** — feature-row, comparison-row, faq-row.
- **Navigation & footer** — top-nav (56px, wordmark left, links centered,
  secondary + primary pill pair right), footer (dense caption-sized link
  grid).

## Do's and don'ts

**Do**
- Treat white and near-black as the system's two anchor surfaces — every
  band of the page picks one or the other.
- Push display-size letter-spacing aggressively negative; that's the brand
  signature, not a stylistic accident.
- Use `{colors.accent-blue}` only for hyperlinks, focus rings, and selected
  indicators — never as a background or button fill.
- Drop in one or two gradient spotlight cards per grid as the brand's
  atmosphere device; don't overdo it.
- Compose every CTA as a pill; secondary actions stay pills too, never
  bordered ghost buttons.
- Keep body type in Inter Variable with the documented character variants
  enabled — the brand voice depends on them.
- Use surface lift (canvas → surface-1 → surface-2) to mark hierarchy on
  dark, not opacity changes on white type.

**Don't**
- Don't ship a light-mode marketing page — Framer's identity is dark.
- Don't introduce mid-tone gray text outside `{colors.ink-muted}` — the
  hierarchy is binary: ink or ink-muted.
- Don't use the sky-blue accent as a brand fill (e.g., a blue CTA pill).
- Don't square off CTAs — pill or full circle is the only vocabulary.
- Don't reduce negative letter-spacing on display sizes "for
  accessibility" — shrink the size instead, but keep the percentage.
- Don't apply gradient backgrounds to whole sections — gradients are
  cards, not section grounds.
- Don't combine more than one chromatic accent — the palette is monochrome
  plus one blue plus the gradient family, not a rainbow.

## Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Desktop | 1199px | Default desktop layout |
| Tablet | 810px | Card grids collapse 4-up → 2-up; nav becomes hamburger |
| Mobile-Lg | 809px | Pricing comparison table becomes a per-tier accordion |
| Mobile-XS | 98px | Smallest documented breakpoint — single-column everything |

Touch targets: pill buttons hold a minimum 44px tap height across
viewports (combining the 14px button type's line-height with 10px vertical
padding); circular icon buttons are 40px on desktop and grow to 44px on
touch; pricing-tab pills hold at least 40px and may switch to horizontal
scroll below 810px. The nav collapses to a hamburger overlay below 810px
while the primary CTA stays visible; card grids go 2-up → 1-up; gradient
spotlight cards keep their 30px corners at every viewport rather than
bleeding to the edge; display type scales down from 110px toward 62px on
tablet and 32px on mobile while preserving the percentage-negative
tracking; product mockups keep aspect ratio and never crop; gradient
spotlight cards keep their gradient orientation across breakpoints, since
the direction is part of the brand spec.

## Known gaps

- The exact gradient stops for the spotlight cards come from screenshot
  pixels rather than CSS variables — the production gradients likely use
  inline `linear-gradient` strings per element, so treat the documented
  hex values as anchors rather than an exact spec.
- Form-field validation/error styling isn't visible on the inspected pages
  because no error states render in the static screenshots.
- Dark mode is the only mode — no light-mode adaptation exists because the
  marketing site doesn't ship one.
- The marketplace template-detail page returned sparser CSS variable data
  than the other pages; its surface tokens were inferred from the matching
  home/gallery treatment rather than extracted directly.
