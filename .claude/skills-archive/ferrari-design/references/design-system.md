# Ferrari Design System — Full Analysis

Adapted from the Ferrari marketing-site design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/ferrari/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Ferrari's marketing pages behave more like a luxury-magazine spread than a
typical car manufacturer's site. Most of the page sits on a near-black
ground (`{colors.canvas}` — #181818); pure-white bands only show up in a
handful of editorial contexts such as preowned-car listings, pricing
tables, and dealer pages. The one splash of color anywhere in the system is
Rosso Corsa (`{colors.primary}` — #da291c), the brand's racing red, and it's
rationed carefully — the Cavallino badge, primary CTA fills, and Formula 1
race-position callouts are the only places it appears.

A single typeface, FerrariSans, handles every text role, and it never goes
past weight 500 even at hero scale — the brand relies on photography to
carry visual weight rather than heavy type. Button and nav copy is the one
place tracking shows up: labels run uppercase with generous letter-spacing
(1.1–1.4px).

What defines the look above everything else is the **full-bleed cinematic
hero photograph** — a top-of-page image (a car detail, a trackside livery
shot) with nothing competing against it. Headlines sit either directly over
the bottom of the photo or in a tight band right beneath it. Underneath
that hero, the page follows an explicit, named 8px spacing ladder: `xxxs`
4 / `xxs` 8 / `xs` 16 / `sm` 24 / `md` 32 / `lg` 48 / `xl` 64 / `xxl` 96 /
`super` 128.

**Key characteristics:**
- One accent color total: `{colors.primary}` Rosso Corsa (#da291c), reserved
  for CTAs, the Cavallino, and F1 position highlights.
- Near-black canvas (#181818), deliberately not pure black; white bands
  only appear inside specific editorial contexts.
- One sans family (FerrariSans) across the whole hierarchy.
- Display weight never exceeds 500 — no bold headlines.
- Button and nav labels are uppercase with 1.4px / 0.65px tracking.
- Every CTA, card, and band uses sharp `rounded.none` (0px) corners —
  precision over softness.
- Depth comes from photography and hairlines, not drop-shadow tiers.
- The 8px spacing scale is named explicitly rather than left implicit.

## Colors

### Brand & accent
- **Rosso Corsa** — the racing red. Primary CTA fill, Cavallino mark, F1
  driver-position highlights. Used sparingly.
- **Rosso Corsa active** — press-state darkening of the primary red.
- **Rosso Corsa hover-darker** — documented for completeness; the site's
  no-hover-states policy means it isn't visible in the live preview.
- **Hypersail yellow / yellow** — sub-brand accents scoped to the Hypersail
  sailing program and the global focus ring; outside the core automotive
  palette.

### Surface
- **Canvas** — the near-black page floor; intentionally warmer than pure
  black.
- **Canvas elevated** — cards and panels lifted off the dark canvas.
- **Canvas light** — the white editorial bands (preowned listings, pricing).
- **Surface card** — same value as canvas-elevated; driver cards and livery
  photo plates.
- **Surface soft/strong light** — alternating light bands and dividers on
  the white editorial pages.

### Hairlines
- **Hairline** — 1px divider color on dark surfaces (shares its hex with
  canvas-elevated).
- **Hairline on light / soft** — dividers used on the white bands.

### Text
- **Ink** — display type and emphasized body on dark.
- **Body / body strong** — default running text and its emphasized twin,
  both white on dark.
- **Body on light** — default text color inside the white bands.
- **Muted / muted soft** — subtitles, captions, and disabled link text on
  dark.
- **On primary** — white text set on the Rosso Corsa fill.

### Semantic
- **Info / success / warning** — used for badges, confirmations, and form
  validation; not part of the decorative palette.

## Typography

### Family
FerrariSans is the single licensed sans used everywhere, falling back to
`-apple-system, system-ui, sans-serif`. There's no separate display/body
pairing — one family covers the entire hierarchy.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale (display-mega 80px
down to caption-uppercase 11px). Principles:
- Display weight sits at 500 across every size, including the 80px hero —
  the photography does the heavy lifting, not bold type.
- CTA labels are uppercase with 1.4px tracking; nav labels uppercase with
  0.65px — a consistent uppercase voice for anything clickable.
- Negative letter-spacing only touches display sizes (-0.36px to -1.6px);
  body stays neutral.

### Font substitutes
FerrariSans is licensed. **Inter** at weight 500 with roughly -1% tracking
is a reasonable open substitute, or **Söhne** for closer humanist
proportions.

## Layout

- Base spacing unit: 4px, expressed as the named ladder in
  `design-tokens.yaml → spacing`.
- Section padding leans on `spacing.xxl` (96px) for major bands, with
  `spacing.super` (128px) reserved for hero depth.
- Max content width on editorial bands is roughly 1280px; hero photography
  goes full-bleed beyond that.
- Editorial body content runs a 12-column grid; feature-card grids flex
  from 2-up (hero splits) to 3-up (benefit grids) to 4-up (preowned
  listings).
- Pacing is generous — cinematic hero photography claims a large share of
  the viewport, while the white editorial bands (preowned, pricing) run
  tighter and denser than the dark cinema sections.

## Elevation & depth

Depth here is photographic and brightness-based rather than shadow-based —
only a single soft, small drop shadow appears anywhere in the extracted
tokens.

| Level | Treatment | Use |
|---|---|---|
| Flat (canvas) | `{colors.canvas}` | Body bands, footer |
| Card | `{colors.canvas-elevated}` | Driver cards, livery plates |
| Light band | `{colors.canvas-light}` | Preowned listings, pricing |
| Hairline border | 1px `{colors.hairline}` / `{colors.hairline-on-light}` | Card outlines, dividers |
| Soft drop | `0 4px 8px rgba(0,0,0,0.1)` | Hovered cards (the one shadow tier) |
| Photographic | Full-bleed cinema imagery | Hero band, livery photography |

Two brand gradients round out the decorative palette: a Rosso Corsa
gradient (`linear-gradient(180deg, #a00c01, #da291c 64%)`) inside accent
bands and CTA hover moments, and a dark-grey gradient
(`linear-gradient(180deg, #3c3c3c, #030303 64%)`) used for atmospheric
darkening at section transitions.

## Shapes

| Token | Value | Use |
|---|---|---|
| rounded.none | 0px | Every CTA, card, band — the dominant radius |
| rounded.xs | 2px | Tight badges (rare) |
| rounded.sm | 4px | Form inputs |
| rounded.md | 6px | Compact cards (rare) |
| rounded.lg | 8px | Mobile-only collapse cards |
| rounded.xl | 12px | Modal/dialog corners (rare) |
| rounded.full | 9999px | Avatar plates, badge pills |

Sharpness is the default; buttons and cards never round beyond that default
except in a handful of documented exceptions. Pill geometry is reserved
strictly for badge labels — never for CTAs.

## Components

Definitions live in `design-tokens.yaml → components`. Summary:
- **Navigation** — top-nav-on-dark / top-nav-on-light, both 64px, Cavallino
  mark left, primary menu center, utilities right, uppercase tracked labels.
- **Buttons** — button-primary (Rosso Corsa fill), button-primary-active
  (press state), button-outline-on-dark/light (transparent, 1px border),
  button-tertiary-text (plain uppercase link). All sharp-cornered.
- **Hero bands** — hero-band-cinema (full-bleed photo, zero padding,
  display-mega headline) and hero-band-light (white editorial variant,
  96px padding).
- **Cards** — feature-card-photo / feature-card-light (image-first tiles),
  driver-card (F1 portrait card on canvas-elevated), preowned-listing-card
  (white-band car listing).
- **Editorial surfaces** — livery-band (full-width Rosso Corsa accent
  panel), spec-cell and race-position-cell (oversized number-display
  callouts, the latter tinted Rosso Corsa), race-calendar-row.
- **Forms & tags** — text-input-on-dark/light (4px radius, 48px height),
  badge-pill (the one pill-shaped surface).
- **Closing surfaces** — newsletter-input-band, cta-band-dark,
  footer-dark, footer-link.

## Do's and don'ts

**Do**
- Keep `{colors.primary}` scarce — CTAs, the Cavallino, F1 position
  highlights only.
- Set every CTA and card at `{rounded.none}` — the brand's signature
  precision.
- Render CTA copy uppercase with 1.4px tracking via `{typography.button}`.
- Pair every hero with a full-bleed cinematic photograph — it supplies the
  depth so shadows don't have to.
- Use the named 8px spacing ladder instead of ad-hoc pixel values.
- Hold display weight at 500 — never bold.

**Don't**
- Don't add a second saturated brand color beyond Rosso Corsa.
- Don't round or pill CTAs — 0px corners are the brand button shape.
- Don't bold display copy; let the photography do the work.
- Don't use Hypersail yellow outside the Hypersail sailing context.
- Don't drop to pure black — the canvas is #181818, slightly warm.
- Don't stack drop-shadow tiers; photography plus brightness steps carry
  elevation.
- Don't pull a CTA color from a third-party widget like a cookie-consent
  modal — the brand red comes from real product CTAs only.

## Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Mobile | < 640px | Hero photo crops vertically; h1 drops 80→32px; feature grid 1-up; hamburger nav; preowned listing 1-up |
| Tablet | 640–1024px | Hero h1 56px; feature grid 2-up; preowned listing 2-up |
| Desktop | 1024–1280px | Full hero h1 80px; feature grid 3-up; preowned listing 4-up |
| Wide | > 1280px | Editorial body caps at 1280px; hero photography stays full-bleed |

Touch targets: the primary CTA sits at 48px height (clears WCAG AAA);
uppercase-tracked nav items get generous padding for an effective 48px tap
area. Top nav collapses to a hamburger below 768px; hero photography
reframes per breakpoint via art direction; feature-card grids step down
4-up → 3-up → 2-up → 1-up; F1 driver cards go 2-up desktop → 1-up mobile.

## Known gaps

- FerrariSans is licensed; Inter at weight 500 is the documented
  open-source substitute.
- Animation timings (hero parallax, livery-band entrance, race-position
  counters) are out of scope for this analysis.
- In-product surfaces (preowned configurator, F1 telemetry overlays) are
  only partially captured through marketing-page surfaces.
- Form validation states beyond focus aren't visible on the captured pages.
- Hypersail yellow tokens are extracted but scoped only to the Hypersail
  sailing program context.
