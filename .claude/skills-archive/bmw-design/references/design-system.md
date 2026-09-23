# BMW Design System — Full Analysis

Adapted from the BMW design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/bmw/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

BMW's corporate site is far more measured and settled than its
motorsport-bombastic cousin, BMW M. The atmosphere stays light:
`{colors.canvas}` (#ffffff) is the base surface, `{colors.surface-card}`
(#fafafa) carries soft-grey card plates, and dark navy
`{colors.surface-dark}` (#1a2129) appears only inside hero bands — one per
page, framing the lead model render.

Type runs BMW's licensed BMW Type Next Latin across exactly two weights:
heavy 700 for display, button, and nav copy, and Light 300 for body and
secondary text. That contrast — heavy display next to thin paragraph — is
the editorial signature, channeling a "European-engineered" voice. Weight
500 is deliberately absent; weight 400 shows up only on caption and
neutral-utility nav-link roles.

The brand action color, BMW corporate blue (`{colors.primary}` #1c69d4),
works alone across every primary CTA — buttons are rectangular with 0px
corners and white type. The page rotates a blue-button + dark-navy-hero
combination through its rhythm. The M tricolor stripe (light blue → dark
blue → red) only appears in motorsport contexts and as M-model badges or
dividers — it is never part of the corporate site's main CTA language.

Configuration and reservation flows layer a dealer-side inventory UI (filter
chips, model cards, price tables) on top of the same system — typography
and color stay identical, only density increases.

**Key characteristics:**
- Light canvas is the base surface; dark navy appears only inside hero
  bands, so page rhythm relies on that contrast.
- BMW corporate blue is the single primary action color.
- BMW Type Next Latin: weight 700 display against weight 300 body is the
  signature pairing.
- Buttons are rectangular, 0px radius — a corporate dialect distinct from
  BMW M's sportier radii.
- Model cards run as 4-up or 5-up grids with minimal or no hairline
  border — just white plate, photo, and title.
- Photography sits in its own environment with no shadow — depth comes
  entirely from color-block contrast.
- The M tricolor stripe appears only in M-model contexts, never the
  corporate main language.
- Section rhythm holds at 80px for every major band.

## Colors

### Brand & Accent
- **BMW Blue / Primary** (`{colors.primary}` #1c69d4) — the single brand
  action color: every primary CTA, "Learn More" prefix links, nav-link
  active state. Press shifts to `{colors.primary-active}` (#0653b6).
- **M Blue Light / M Blue Dark / M Red** (`{colors.m-blue-light}` #0066b1,
  `{colors.m-blue-dark}` #1c69d4, `{colors.m-red}` #e22718) — the M
  tricolor stripe, appearing only on M-model pages and the "M" badge; never
  used as CTA colors on the corporate site.

### Surface
- **Canvas** (`{colors.canvas}` #ffffff) — the default page surface.
- **Surface Soft** (`{colors.surface-soft}` #f7f7f7) — footer and sub-nav
  bands.
- **Surface Card** (`{colors.surface-card}` #fafafa) — the light plate
  behind a model card's photo.
- **Surface Strong** (`{colors.surface-strong}` #ebebeb) — a slightly
  heavier grey for section dividers.
- **Surface Dark** (`{colors.surface-dark}` #1a2129) — dark navy for hero
  bands and large dark CTAs, carrying a warm undertone rather than pure
  black.
- **Surface Dark Elevated** (`{colors.surface-dark-elevated}` #262e38) —
  one step lighter, for nested cards on top of the dark hero.

### Hairlines
- **Hairline** (`{colors.hairline}` #e6e6e6) — input outlines,
  configurator card outlines, table separators.
- **Hairline Strong** (`{colors.hairline-strong}` #cccccc) — a more visible
  outline for disabled secondary buttons and emphasized table borders.

### Text
- **Ink** (`{colors.ink}` #262626) — all display and primary text, never
  pure black, so it stays soft against photography.
- **Body** (`{colors.body}` #3c3c3c) — default running text.
- **Body Strong** (`{colors.body-strong}` #1a1a1a) — emphasized paragraphs
  and lead text.
- **Muted / Muted Soft** (`{colors.muted}` #6b6b6b, `{colors.muted-soft}`
  #9a9a9a) — footer links, breadcrumbs, captions, disabled/legal text.
- **On Primary / On Dark** (`{colors.on-primary}` / `{colors.on-dark}`
  #ffffff) — white text on blue buttons and dark hero bands.
- **On Dark Soft** (`{colors.on-dark-soft}` #bbbbbb) — muted white for
  secondary text on dark bands.

### Semantic
- **Success** (`{colors.success}` #22c55e), **Warning**
  (`{colors.warning}` #f59e0b), **Error** (`{colors.error}` #dc2626) —
  confirmation, warning, and validation states.

## Typography

### Font Family
BMW Type Next Latin ships in two cuts: regular (display + UI labels) and
BMW Type Next Latin Light (body + secondary copy). The split is functional:
regular weight 700 handles display headlines, buttons, and nav links; Light
weight 300 handles paragraphs and descriptive copy; regular weight 400
covers caption and neutral nav-link roles. This three-way split mirrors BMW
M's typographic DNA — corporate and the M sub-brand share the same
foundation; only the weight/size ratios differ.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale (display-xl 64px
down to the 12px caption). Notable roles:
- `{typography.display-xl}` (64px/700) is the hero h1 (model name).
- `{typography.label-uppercase}` (13px/700/1.5px tracking) carries "LEARN
  MORE"-style inline links and category tabs.

### Principles
- The 700/300 contrast is the editorial signature; weight 500 is entirely
  absent from the system.
- No negative letter-spacing — BMW Type Next Latin works on a wide body,
  so tracking stays at default. Apple- or Cal.com-style tightening would
  read off-brand here.
- Uppercase inline links ("LEARN MORE") carry 1.5px tracking — the
  "machined precision" voice.
- Weight 400 lives in a narrow lane: only caption and nav-link, both
  neutral utility roles.

### Note on Font Substitutes
BMW Type Next Latin is licensed and not public. **Inter** (variable) is a
close match at weight 700/300, left at 0 letter-spacing. **Saira
Condensed** is an option for a slightly more compressed feel.

## Layout

### Spacing System
- Base unit: 8px.
- Tokens: `{spacing.xxs}` 4px · `{spacing.xs}` 8px · `{spacing.sm}` 12px ·
  `{spacing.md}` 16px · `{spacing.lg}` 24px · `{spacing.xl}` 32px ·
  `{spacing.xxl}` 48px · `{spacing.section}` 80px.
- Section padding: 80px for every major editorial band.
- Card padding: 24px for model and feature cards.

### Grid & Container
- Max content width: ~1440px, center-aligned.
- Editorial body: a single 12-column grid.
- Model card grids: 4-up or 5-up at desktop, 2-up tablet, 1-up mobile.
- Configurator inventory grids: a 3-up filter row plus a 4-up vehicle-card
  grid, deliberately denser.

### Whitespace Philosophy
BMW's whitespace is tighter than BMW M's motorsport-aerated rhythm — the
corporate side is more utility-driven. Section rhythm holds at 80px (not
M's 96px), and card padding stays at 24px (not M's 32px). The page reads
denser and more dealership-functional.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat | No shadow, no border | Body, top nav, footer, hero bands |
| Soft hairline | 1px hairline border | Configurator option tile, table divider |
| Card surface | Surface-card fill, no shadow | Model card photo plate |
| Photographic | Edge-to-edge photography | Hero band, model renders |

The system never uses a drop shadow. Depth comes entirely from color-block
contrast (light canvas vs. dark hero) and the photography itself (subject +
lighting). The one decorative element is the `m-stripe-divider` — a 4px
tricolor horizontal stripe reserved for M-model contexts, motorsport
badges, or an M-related section divider; it stays absent from the main
corporate flow.

## Shapes

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | Every button, card, input, configurator chip — the dominant radius |
| `{rounded.xs}` | 2px | Very small badges, very rare |
| `{rounded.sm}` | 4px | Small inline button (rare) |
| `{rounded.md}` | 8px | Mobile-only collapse cards (rare) |
| `{rounded.lg}` | 12px | Very rare — modal/dialog corners |
| `{rounded.pill}` | 9999px | Filter chips in some contexts (rare) |
| `{rounded.full}` | 9999px / 50% | Avatar, circular icon button |

The radius hierarchy is binary: rectangular for everything, circular only
for icon buttons — a clear departure from softer SaaS-style corners, closer
to a corporate-automotive "engineered precision" voice. Hero photography
runs full-bleed at 16:9 or 21:9; model-card photos sit at 16:10, edge to
edge with 0px corners; configurator vehicle renders float on a white
studio background with the full silhouette visible.

## Components

- **`top-nav`** — white, sticky, 64px tall. BMW circular badge left, a
  primary horizontal menu center (Models, Next Generation, Pre-Owned,
  Dealers, Test Drive), cart/language/profile right.
- **`button-primary`** — BMW Blue fill, white text, 0px radius, 14×32px
  padding, 48px height. Press state shifts to `{colors.primary-active}`.
- **`button-secondary`** — white fill with a hairline outline, same
  rectangular shape.
- **`button-secondary-on-dark`** — transparent fill with a white outline,
  used over a dark hero band.
- **`button-text-link`** — an inline uppercase letter-spaced link
  ("LEARN MORE ›"), no background.
- **`hero-band-dark`** — full-width dark navy hero: model name at 64px/700,
  sub-headline, vehicle render, and a single primary or secondary-on-dark
  CTA.
- **`hero-photo-band`** — a light-canvas showcase band where the vehicle
  render takes the wide area and copy + link CTAs sit alongside.
- **`model-card`** — the 4-up/5-up homepage grid card: photo plate on
  `{colors.surface-card}` at top, model name at 18px/700 below, a tagline
  at 14px/300, and a "LEARN MORE ›" text link.
- **`feature-photo-card`** — a lifestyle card with a 16:9 photo and a
  headline + body excerpt beneath.
- **`spec-cell`** — a technical-spec cell on model detail pages: a value at
  24px/700 above an uppercase label.
- **`inventory-card`** — a dealer inventory listing: vehicle photo, then
  model + variant + price + "View" link.
- **`filter-chip`** / **`filter-chip-active`** — inventory filter chips;
  active state flips to ink fill with white text.
- **`configurator-option-tile`** / **`-selected`** — a color/wheel/
  upholstery selector cell; selected state upgrades the border to 2px
  primary blue.
- **`text-input`** — 0px radius, 48px tall, 14×16px padding, hairline
  border that thickens to ink on focus.
- **`category-tab`** / **`category-tab-active`** — uppercase sub-nav tabs;
  active state adds a 2px ink underline.
- **`cta-band-photo`** — a pre-footer "Discover the New [Model]" band with
  a full-bleed vehicle photo and a single secondary-on-dark CTA.
- **`footer`** — soft-grey, a 4-column link list (Models/Services/
  Dealers/About), copyright line beneath.

## Do's and Don'ts

### Do
- Sit every page on `{colors.canvas}`; reserve `{colors.surface-dark}` for
  hero bands only.
- Pair primary CTAs with BMW Blue, white text, and 0px corners — the
  corporate signature.
- Set display headlines in weight 700 and body in Light 300 — the contrast
  is non-negotiable.
- Use uppercase letter-spaced links like "LEARN MORE" as inline CTAs.
- Place the model-card photo on `{colors.surface-card}` with the title
  beneath — the standard corporate pattern.
- Hold section rhythm at 80px — tighter than BMW M's 96px.
- Reserve the M tricolor stripe for M-model contexts and motorsport
  dividers.

### Don't
- Don't add a brand color other than blue.
- Don't use pill or rounded buttons — 0px rectangular IS the brand button.
- Don't drop display weight to 500 — the system uses 700/400/300 only.
- Don't bold body type — Light 300 is the corporate editorial voice.
- Don't add drop shadows to cards.
- Don't repeat the same surface mode across two consecutive bands — the
  light → dark-hero → light → feature → dark-CTA → light-footer rotation
  is required.
- Don't use the M tricolor stripe as a CTA fill.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 768px | Hamburger nav; hero h1 64→40px; model-card grid 1-up; filter chips 2-up; footer 4 col → 1. |
| Tablet | 768–1024px | Nav narrows, secondary menu hides under "More"; model card 2-up; inventory 2-up. |
| Desktop | 1024–1440px | Full nav; 4-up or 5-up model-card grid; inventory 3-up; full configurator UI. |
| Wide | > 1440px | Same as desktop, content fixed at 1440px. |

### Touch Targets
- Primary CTAs 48×48px minimum — above WCAG AAA.
- Text inputs 48px tall.
- Category tabs carry 12px vertical padding, giving an effective tap area
  above 44px.

### Collapsing Strategy
- Nav collapses to a full-screen hamburger sheet below 768px.
- The hero band's internal layout drops to a single column.
- Model-card grid steps 4-up/5-up → 2-up → 1-up.
- The configurator filter-chip row scrolls horizontally on mobile.
- The M-stripe divider stays at 4px height across every breakpoint.

## Known Gaps

- BMW Type Next Latin is licensed and not published as a public web font;
  Inter at weights 700/300 is documented as the substitute.
- Animation and transition timings (configurator color swap, model-card
  hover-reveal) are out of scope.
- Form validation states beyond input focus weren't extracted — error/
  success states would need a dedicated form page.
- The dealer inventory sub-domain shares typography and color with the
  main site; only UI density rises.
- A cookie-consent overlay can occlude part of the hero — full hero content
  may not always be captured.
- The M tricolor stripe appears infrequently on this corporate site; full
  motorsport context lives on the separate BMW M site.
