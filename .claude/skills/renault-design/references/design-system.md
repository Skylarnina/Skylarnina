# Renault Design System — Full Analysis

Adapted from the Renault design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/renault/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Renault's Turkish marketing surfaces lean into hard contrast rather than
soft gradients: browsing pages sit on a white canvas, product storytelling
sits on a black one, and Sunlight Yellow (`{colors.primary}`, `#ffed00`) is
kept in reserve for the handful of moments that matter most. The brand's
2021 flat-line diamond logo is geometric and slightly industrial, and the
rest of the system follows its lead — square corners are the default,
hairline borders are used sparingly, and elevation comes from blocks of
color rather than shadow.

Typography never varies in family: everything is set in **NouvelR**, the
proprietary display face, with display sizes locked to weight 700 and a
tight `lineHeight: 0.95`, dropping to weight 400 for body copy. There's no
secondary serif, no italic, no script — consistency itself is the brand
statement.

The page rhythm cycles through three states: a white "catalogue" mode for
listings and configurators with soft `{colors.hairline}` divider lines, a
black "storytelling" mode for hero imagery and the lower half of campaign
pages, and short yellow accent moments — a promo tile, a "NEW" badge, a shot
of R5 paint — that interrupt the otherwise neutral palette.

**Key characteristics:**
- Full-bleed white-to-black canvas switches instead of gradual shading.
- One brand accent (yellow), used sparingly on CTAs, badges, R5 photography,
  and configurator swatches.
- NouvelR everywhere, with 56px/700/0.95-line-height display headlines that
  stack cleanly across multiple lines.
- Square geometry: 2px buttons, 0px tiles/cards, pill shape kept for sub-nav
  chips and badges only.
- Photography-first vehicle tiles — full-bleed car photos with copy stacked
  underneath, never overlaid.
- Page rhythm: white → black → yellow accent → black, closing on black for
  the footer.

## Colors

### Brand & accent
- **Sunlight Yellow** — the sole accent; primary CTAs, "NEW"/"yeni" badges,
  configurator dot indicators, and full-bleed promo tiles. Never decorative.
- **Sunlight Yellow Pressed** — the darker active/pressed state of yellow
  surfaces.
- **On-Primary** — black label text on yellow; yellow never pairs with
  white text.

### Surface
- **Canvas** — default white page and card background.
- **Surface Soft** — a faint off-white step used for grouped configurator
  rows and inactive fields.
- **Surface Dark** — the black alternate canvas for hero bands, footer, and
  full-bleed storytelling.
- **Surface Deep** — a one-step-up elevation inside dark regions for inset
  cards and form panels.
- **Hairline / Hairline Strong** — the soft divider on white, and the
  full-strength divider plus card/button outlines.
- **Divider Dark** — the translucent-white equivalent divider used inside
  dark sections.

### Text
- **Ink** — primary text on white, also the color of logos, icons, and
  outline borders.
- **Body / Charcoal / Mute / Ash / Stone** — a descending scale from
  secondary paragraph text down to disabled-state foreground.
- **On-Dark / On-Dark Mute** — primary and secondary text on the black
  canvas.

### Semantic
- **Error / Warning / Success / Info** — muted, slightly desaturated
  functional colors used for inline form states.
- **Link** — a fallback unstyled-anchor blue; production links usually
  inherit ink and rely on underline/weight instead of color.

## Typography

### Families
NouvelR is used site-wide across navigation, headlines, body, captions, and
buttons — a slightly geometric, semi-condensed face with tall x-heights and
squared apexes that echoes the diamond logomark. Where it can't be
licensed, **Inter Tight**, **Manrope**, or **HK Grotesk Semi Condensed** are
close substitutes; when substituting, clamp display `lineHeight` to 0.95
rather than letting it relax.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale (display-xl 56px
down to overline 10px). Principles:
- Display sizes are always weight 700 at `lineHeight: 0.95` — the
  tightness reads as confidence rather than corporate polish.
- Body stays at weight 400, never 500 — the 400/700 contrast is
  intentional.
- Button labels carry a barely-visible positive tracking (0.144px on
  button-md) for a touch of mechanical precision.
- No italics, no script, no decorative ligatures anywhere in the system.

## Layout

- Base spacing unit: 4px; full scale in `design-tokens.yaml → spacing`.
- Section-to-section padding: 80px desktop, collapsing to 40px on mobile.
- Promo-tile interior padding: 32px on desktop.
- Configurator rows: 24px vertical padding with a hairline divider between
  rows.
- Max content width ≈ 1440px; the homepage promo grid runs 2-up desktop /
  1-up mobile, vehicle range grids run 3–4-up desktop down to 1-up mobile.
- The configurator splits roughly 60/40 between a fixed visualization pane
  and a scrolling option list on desktop.
- Whitespace is structural rather than decorative — sections separate by
  full color-block switches, not soft padding ramps; density is acceptable
  inside cards since the brand is mass-market, not luxury.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 flat | no shadow/border | default page surface, full-bleed bands |
| 1 outline | 1px hairline or hairline-strong | promo tiles, vehicle cards, configurator panels |
| 2 color-blocked | surface shift (canvas card inside a soft band) | configurator detail cards, related-content rows |
| 3 dark inversion | card flips to black against a white band | commercial-vehicle hero tiles, lifestyle cards |

Shadows exist in the extracted tokens but are rarely visible on marketing
pages; when they do appear they're subtle (~10% opacity, 2–4px blur) on
floating elements like the configurator's sticky summary bar. The one true
atmospheric moment is the R5 hero's purple-to-pink-to-yellow mesh gradient,
and a magenta-to-violet gradient reserved for E-TECH electric powertrain
pages.

## Shapes

| Token | Value | Use |
|---|---|---|
| rounded.none | 0px | tiles, vehicle cards, dividers, banner bands, full-bleed images |
| rounded.xs | 2px | default buttons (primary yellow, secondary black, outline) |
| rounded.sm | 3px | tab panels, small chips |
| rounded.md | 4px | form labels, inline tags |
| rounded.pill | 46px | sub-nav pills, "NEW" badges, decorative carousel chips |
| rounded.full | 9999px | configurator color swatches, avatar dots |

Vehicle photography is always square-cornered, clustering around 16:9 (hero
bands), 1:1 (square promo tiles), and 4:3 (vehicle range cards) aspect
ratios, with occasional 2:1 wide crops for full-bleed lifestyle bands.
Avatars are the one place `rounded.full` circles contrast against the
otherwise square geometry.

## Components

Definitions live in `design-tokens.yaml → components`. Summary:
- **Buttons** — primary (yellow fill), secondary-dark (black fill),
  outline-dark/outline-light (bordered), pill (sub-nav chips only), and a
  square icon button for carousel arrows/share/language.
- **Cards & tiles** — promo-tile in light/dark/yellow variants, a
  borderless vehicle-card with full-bleed photography, and a full-bleed
  hero-banner.
- **Configurator** — a row component for the scrolling option list and a
  circular swatch component for paint-color selection (active state adds a
  hairline-strong ring).
- **Inputs** — a minimal text-input with no side/top border, just a single
  bottom hairline.
- **Navigation & footer** — a 60px nav bar (diamond logo left, top nav
  center, language/login right), pill-style sub-nav chips, and a
  three-column footer on the dark canvas.
- **Signature** — a "NEW"/"yeni" badge anchored on new-vehicle cards.

## Do's and don'ts

**Do**
- Keep yellow exclusive to primary CTAs, "NEW" badges, and at most one
  accent promo tile per band.
- Pair yellow only with black text — never white.
- Set everything in NouvelR; no secondary serif, script, or italic.
- Hold display headlines at weight 700 with `lineHeight: 0.95` so
  multi-line wraps stack tightly.
- Use 2px corners on every standard button.
- Switch full bands between white and black for storytelling rhythm;
  avoid mid-grey section backgrounds.
- Show vehicle photography full-bleed with copy stacked beneath it, never
  overlaid.
- Reserve pill shape for sub-nav and small filter chips only.

**Don't**
- Don't add a second accent color — yellow is the only brand accent;
  semantic colors are functional, not decorative.
- Don't round vehicle cards or promo tiles.
- Don't soften body weights to 500/600 — stick to the 400/700 contrast.
- Don't apply yellow to body text or large surfaces beyond one accent tile
  per band.
- Don't add atmospheric gradients outside the dedicated R5/E-TECH hero
  contexts.
- Don't pair light-grey text on white — step through body/charcoal/mute;
  reserve ash/stone for placeholders and disabled states.
- Don't add drop shadows to vehicle cards or promo tiles.

## Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Desktop XL | ≥1440px | full max-width container, 3–4 column vehicle grid, 2-up promo grid |
| Desktop | 1280–1439px | same layout, container shrinks with side padding |
| Tablet Large | 1024–1279px | vehicle grid drops to 3-up, configurator panes resize to 55/45 |
| Tablet | 768–1023px | promo grid collapses to 2-up, sub-nav pills scroll horizontally |
| Mobile Large | 426–767px | vehicle grid 2-up, configurator stacks (visualization on top), nav collapses to hamburger |
| Mobile | ≤425px | all grids 1-up, hero headline clamps to ~40px, section padding collapses to 40px |

Touch targets: every button ships at minimum 44×44px on mobile; the default
primary button is 48px tall. Sub-nav pills grow from 36px to 40px tall on
mobile. The icon-square button (40px) sits at the WCAG AA minimum and
should grow to 44px when used as a primary navigation control.

Collapsing strategy: nav collapses to hamburger below 1024px; the 2-up
promo grid drops to 1-up below 768px with tile padding shrinking from 32px
to 20px; the configurator flips from side-by-side to stacked below 1024px;
display headlines clamp 56px → 40px → 32px across the ladder; sub-nav pills
convert to a horizontal scroll rail below 768px.

Image behavior: vehicle photography serves at 1.5×/2× DPR and swaps to a
portrait composition below 768px where art direction allows. Hero
atmospheric gradients load lazily and non-blocking. Lifestyle photography in
dark promo tiles keeps its 16:9 framing at every breakpoint, cropping inward
rather than letterboxing.

## Known gaps

- Active/pressed visual states are only reliably documented for the primary
  button; other components don't have a promoted pressed variant.
- Drop-shadow values exist in the extracted tokens but are rarely visible;
  only the configurator's sticky summary bar clearly uses them.
- The logged-in MyRenault application surfaces are out of scope — only the
  public marketing canvas is documented.
- Form-field focus styling isn't visually confirmed on the captured pages;
  it likely uses a thicker ink-colored bottom border.
