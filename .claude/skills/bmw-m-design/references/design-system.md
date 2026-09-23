# BMW M Design System — Full Analysis

Adapted from the BMW M design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/bmw-m/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

BMW M's marketing surface sits on a near-pure black `colors.canvas`
(`#000000`) carrying white BMW Type Next Latin headlines set in confident
UPPERCASE. The system has no decorative voltage of its own — all of its
energy comes from full-bleed automotive photography: cars cornering at
speed, carbon-fiber wheel detail, cockpit shots, motorsport pit lanes,
placed as edge-to-edge imagery that fills whole bands. Chrome around that
photography stays deliberately minimal — thin sans-serif copy, 1px hairline
dividers (`colors.hairline`), and all-caps button labels that carry no fill
until interacted with.

The **M tricolor stripe** — light blue `m-blue-light` (`#0066b1`) into dark
blue `m-blue-dark` (`#1c69d4`) into red `m-red` (`#e22718`) — is the one
brand-identity accent. It shows up sparingly on the M wordmark, motorsport
chrome, tech callouts, and model badges. It is never used as a CTA color
and never as a background fill; it exists purely as an identity marker.

The typographic voice runs two cuts of BMW Type Next Latin: a regular cut
for display and nav labels, and a Light cut for body and secondary copy.
Display sizes sit at weight 700 (heavy but tight), while body text drops all
the way to weight 300. That gap between heavy headlines and very light body
copy is the system's defining editorial contrast.

**Key characteristics:**
- Near-pure-black canvas with white type and no light-mode marketing surface.
- UPPERCASE BMW Type Next Latin display headlines at weight 700; sub-heads
  stay sentence-case and lighter.
- The M tricolor appears only as a 4px stripe divider, wordmark accent, or
  motorsport chrome — never as a button or fill.
- Photography fills entire bands edge-to-edge; cars are always the subject
  while UI chrome recedes to small overlaid white labels.
- Flat buttons at `rounded.none` (0px) with uppercase, letterspaced labels —
  the rectangular silhouette is itself a brand signal.
- Radius is almost always zero, with `rounded.full` reserved for circular
  icon buttons (carousel arrows, chatbot launcher) and `rounded.sm` for a
  few small configurator toggle pills.
- Generous, grid-aligned spacing: `spacing.section` (96px) between major
  bands, `spacing.xxl` (64px) inside hero photo bands, `spacing.xl` (40px)
  inside content cards.

## Colors

### Brand & accent
- **Primary** (`#ffffff`) — the system's primary type and CTA color, used
  for headline type, body-on-dark, and primary button labels (buttons
  themselves stay transparent or canvas-colored; the white text plus
  outline is the button).
- **M Blue Light** (`#0066b1`) — first stop of the M tricolor stripe, used on
  M-badge accents and motorsport chrome.
- **M Blue Dark** (`#1c69d4`) — the middle stop, sharing its hex with
  `bmw-blue`, BMW's heritage corporate blue repurposed as the stripe's
  center band.
- **M Red** (`#e22718`) — the third stop, BMW's signature M-power red, used
  in the stripe and on motorsport-pace callouts.
- **Electric Blue** (`#0653b6`) — a separate, colder EV accent used only on
  M xDrive electric model pages, distinct from the heritage blue.

### Surface
- **Canvas** (`#000000`) — the default page floor everywhere.
- **Surface Soft** (`#0d0d0d`) — a barely-there-above-black tone for spec
  table cells and footer-adjacent strips.
- **Surface Card** (`#1a1a1a`) — cards, secondary buttons, icon-button
  backgrounds.
- **Surface Elevated** (`#262626`) — one step lighter, for nested cards
  inside dark bands.
- **Carbon Gray** (`#2b2b2b`) — a carbon-fiber-inspired tone used on
  technical-spec cards.

### Hairlines & borders
- **Hairline** (`#3c3c3c`) — the 1px divider tone on dark surfaces, between
  body sections, table rows, and card outlines.
- **Hairline Strong** (`#262626`) — shares its hex with `surface-elevated`,
  so borders read like one-step elevations rather than drawn ink lines.

### Text
- **Ink / On Dark** (`#ffffff`) — all headline and primary text on the dark
  canvas.
- **Body** (`#bbbbbb`) — default running-text color, slightly cooler than
  pure white, used for paragraphs and secondary metadata.
- **Body Strong** (`#e6e6e6`) — emphasized body and lead paragraphs.
- **Muted** (`#7e7e7e`) — footer links, breadcrumbs, captions.

### Semantic
- **Warning** (`#f4b400`) — used very sparingly on technical-warning
  callouts.
- **Success** (`#0fa336`) — order-confirmation states, rare on marketing
  surfaces.

## Typography

### Font family
BMW Type Next Latin is BMW's licensed display and body face, used in two
cuts (regular and Light) with a fallback stack of
`-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`. The
weight pairing is deliberate: 700 for headlines, nav labels, button text,
and category labels (the "stamped" voice), and 300 for body paragraphs,
descriptive copy, and secondary metadata (the "engineered" voice). That
contrast is BMW's editorial signature — never soften it with a 400 display
or a 500 body.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale (display-xl 80px
down to caption 12px). Key entries: `display-xl` (80/700, hero h1),
`display-lg` (56/700, section heads), `display-md` (40/700, sub-sections and
model names), `display-sm` (32/700, CTA-band heads), `title-lg` (24/700,
grid card titles), `title-md` (20/400, card sub-titles), `label-uppercase`
(14/700, 1.5px tracking, category tabs), `body-md` (16/300 Light, default
body), `button` (14/700, 1.5px tracking).

### Principles
Heavy headlines (700) always sit against very light body (300) — the gap is
non-negotiable. Letter-spacing is meaningful: button and category labels
carry 1.5px tracking for a "machined" feel, while display headlines stay at
0 tracking since BMW Type's cap-height already handles large-size spacing.
UPPERCASE is the default voice for h1/h2; sentence case appears in body and
intro paragraphs but rarely in headlines — the all-caps treatment is a
brand-voice signal, not a stylistic flourish.

### Font substitutes
If BMW Type Next Latin is unavailable, **Inter** (variable) at 700/300 is
the closest open-source stand-in — tighten display tracking to about
-0.5px to match BMW Type's large-size spacing. **Saira Condensed** works as
an alternative headline face for a more compressed feel.

## Layout

- **Base unit:** 4px. Full scale: `xxs` 4px, `xs` 8px, `sm` 12px, `md` 16px,
  `lg` 24px, `xl` 40px, `xxl` 64px, `section` 96px.
- **Section padding (vertical):** `spacing.section` (96px) between major
  editorial bands.
- **Hero photo bands:** `spacing.xxl` (64px) of internal vertical padding
  around the hero headline/subhead pair.
- **Card internal padding:** `spacing.lg` (24px) for content and model
  cards; `spacing.xl` (40px) for spec-cell tables.
- **Gutters:** `spacing.lg` (24px) between cards in 3-up grids; `spacing.md`
  (16px) inside footer columns.
- **Max content width:** roughly 1440px, wider than typical SaaS to give
  photography room to breathe. Photo bands bleed full-width with no max.
- **Grid:** single 12-column grid for editorial body; card grids run 3-up
  desktop, 2-up tablet, 1-up mobile; footer runs 4-column desktop, 2-up
  tablet, 1-up mobile.
- **Whitespace philosophy:** photography does the visual work, so whitespace
  around it stays restrained — cars fill the frame, copy sits tightly
  below or beside. Where whitespace does appear it's always the uniform
  96px section rhythm; there's no atmospheric backdrop or gradient filler.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| Flat | no shadow, no border | body sections, top nav, footer, photo bands |
| Soft hairline | 1px `hairline` border | section dividers, card outlines, table rows |
| Card surface | `surface-card` background, no shadow | feature photo cards, magazine cards, chatbot launcher |
| Photographic depth | full-bleed photography, edge-to-edge crop | hero bands, motorsport features |

No drop shadows and no layered chrome anywhere — depth comes from the
photography itself and from the contrast between black canvas and the
slightly-lighter `surface-card`. The one true decorative element is the
**M stripe divider**, a 4px horizontal bar carrying the M tricolor, used on
motorsport chrome, model-detail headers, and other brand-identity moments —
sparingly, to mark significance. The technical-spec page's `carbon-gray`
cells with a subtle texture overlay are a single-page treatment, not a
system-wide pattern.

## Shapes

| Token | Value | Use |
|---|---|---|
| `rounded.none` | 0px | buttons, cards, photo containers, spec cells, inputs — the dominant radius |
| `rounded.xs` | 2px | almost unused, reserved for legal CTAs |
| `rounded.sm` | 4px | small toggle pills on configurator surfaces |
| `rounded.md` | 6px | rare small dropdown menu items |
| `rounded.full` | 9999px | circular icon buttons, carousel arrows, chatbot launcher |

The radius logic is binary — almost always 0, occasionally circular, with
nothing in between. That's a deliberate choice: sharp rectangles read as
engineered precision, circles read as functional controls. Hero photography
fills full-width with no rounding; photo cards inside grids keep sharp
corners with edge-to-edge images. Carbon-wheel detail and motorsport-pit
shots use 16:9 or 21:9 cinema-aspect ratios; driver portraits in racing-team
grids use 4:5 crops, also sharp-cornered.

## Components

Definitions live in `design-tokens.yaml → components`. Summary:
- **top-nav** — 64px black bar with the BMW M logo (tricolor + roundel + M
  wordmark) at left, a primary menu (Models, Topics, Magazine, Configurator,
  Fastlane), and a right-side cluster for language, search, account.
- **Buttons** — `button-primary` (canvas/transparent fill, white outline,
  0px radius, uppercase 1.5px-tracked label — the rectangular silhouette IS
  the button), `button-primary-outline` (transparent variant for use over
  photography), `button-on-light` (inverted black-on-white for rare light
  contexts), `button-icon`/`carousel-arrow` (48×48 circular, the only
  non-rectangular button shape), `text-link` (uppercase letterspaced inline
  links with a chevron glyph).
- **Cards & containers** — `hero-photo-band` (full-width photo band, 80px
  hero h1, 64px vertical padding), `feature-photo-card` (3-up magazine
  grid, surface-card fill, 24px padding), `model-card` (canvas background,
  40px model name, spec line, text-link), `magazine-article-card`
  (canvas + hairline, thumbnail plus headline), `spec-cell` (surface-soft
  fill, 32px value over an uppercase label), `motorsport-photo-card`
  (edge-to-edge photo with a caption overlay), `chatbot-launcher` (surface
  card with title, prompt, and primary button).
- **Category tabs** — `category-tab`/`category-tab-active`, text-only
  uppercase labels; active state swaps to white text plus a 2px underline,
  no fill or rounding.
- **Inputs** — `text-input` (surface-card fill, 0px radius, 48px height,
  hairline border that thickens to white on focus).
- **Signature** — `m-stripe-divider` (4px tricolor bar, the system's most
  distinctive non-typographic element), `cta-band-photo` (pre-footer "Drive
  an M" band with full-bleed photography and an outline button).
- **Footer** — 4-column black footer with a BMW disclaimer and language
  selector; it never inverts to a light background.
- **cookie-consent-card** — right-side canvas card with a hairline border,
  Light-weight body copy, and stacked outline/text-link buttons.

## Do's and don'ts

**Do**
- Anchor every page with full-bleed automotive photography — the cars are
  the brand voltage, chrome backs off.
- Use UPPERCASE `display-xl` or `display-lg` for headlines; sentence-case
  display reads off-brand.
- Pair heavy display (700) with light body (300) — the weight contrast is
  the editorial signature.
- Reserve the M tricolor for brand-identity moments only — never a button
  fill or surface.
- Default to `rounded.none`; use `rounded.full` only for circular icon
  buttons.
- Letter-space all-caps labels at 1.5px — the "machined" feel is
  non-negotiable.
- Use `spacing.section` (96px) between major editorial bands.

**Don't**
- Don't introduce a brand color outside the M tricolor and heritage
  `bmw-blue`.
- Don't bold body type — it stays at 300 (Light); bumping it up reads as
  marketing-bombastic rather than European-engineered.
- Don't round buttons — the rectangular silhouette is the brand.
- Don't put gradient backdrops behind hero type — the photography is the
  hero, and the floor stays pure black.
- Don't repeat the same surface mode in two consecutive bands (alternate
  photo band, spec table, photo band, magazine grid, photo band).
- Don't use the M stripe as a button fill — it's a divider/accent, never
  an action surface.
- Don't tighten uppercase tracking below 1.5px on button labels.

## Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Mobile | < 768px | hamburger nav; hero h1 scales 80→48px; grids go 1-up; footer 4 cols → 1 |
| Tablet | 768–1024px | top nav tightens but stays horizontal; 2-up card grids; spec tables 2-up |
| Desktop | 1024–1440px | full top-nav; 3-up card grids; spec tables 4-up |
| Wide | > 1440px | same as desktop with more breathing room; max content 1440px |

Touch targets: `button-primary` renders at 48×48px minimum (WCAG AAA);
`button-icon`/`carousel-arrow` are exactly 48×48; `text-input` height is
48px; category tabs use 12px vertical padding with surrounding spacing to
reach 44px effective tap area. Top nav collapses to a full-screen black
hamburger overlay topped by the M-tricolor stripe below 768px; photography
stays full-bleed at every breakpoint; card grids reduce columns rather than
shrinking cards; spec tables collapse from 4-up to 2-up to 1-up while
keeping their display-sm value size; the M-stripe divider stays 4px tall
throughout.

## Known gaps

- The white text was the dominant sampled token; the black canvas itself
  was confirmed from screenshots rather than a top palette entry.
- Exact M tricolor stops come from public BMW brand guidelines — screenshot
  pixel-sampling at this resolution can't reliably separate `#0066b1` from
  `#1c69d4`, so the documented stops should be treated as canonical.
- BMW Type Next Latin's full weight axis beyond Light (300) and 700 isn't
  documented — only the static weights actually observed.
- Animation/transition timing (carousel transitions, hover reveals,
  configurator interactions) is out of scope.
- Form validation states beyond the default `text-input` weren't captured.
- The configurator surface (color/wheel/interior pickers) wasn't in the
  analyzed URL set, so its swatch grid and price-summary card aren't
  documented here.
- A cookie-consent overlay partly obscured the homepage hero in the
  captured screenshot, so secondary hero treatments may include variations
  not captured.
