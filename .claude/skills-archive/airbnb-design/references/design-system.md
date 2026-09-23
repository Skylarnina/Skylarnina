# Airbnb Design System — Full Analysis

Adapted from the Airbnb design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/airbnb/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Airbnb is the textbook case of a warm, photography-driven consumer
marketplace. The page floor is plain white (`{colors.canvas}` #ffffff) with
near-black ink (`{colors.ink}` #222222) carrying headlines and body copy, and
exactly one brand voltage — Rausch (`{colors.primary}` #ff385c) — which shows
up on primary buttons, the search orb, the wishlist heart, and inline brand
links. There is no second color in the main marketing experience; the Luxe
purple (`{colors.luxe}` #460479) and Plus magenta (`{colors.plus}` #92174d)
tokens only surface inside those sub-brands' own pages.

Type runs on Airbnb's custom variable font, Cereal VF, with Circular kept as
the historic fallback. Display sizes stay modest — 22–28px at weight
500–600 — rather than the heavier 700+ weights common on SaaS or fintech
sites. Even the homepage's h1 sits at a restrained 28px/700; the page leans on
photography (a city collage, listing cards) to carry visual weight instead of
big type.

Shape language is uniformly soft: 8px buttons, ~14px property cards, and a
fully pill-shaped search bar, hearts, and search orb. Category-strip corners
run out to 32px. Virtually nothing on the page has a hard corner outside the
underlying grid.

**Key characteristics:**
- One accent color only — Rausch carries every CTA, the search orb, the
  saved-heart state, and the wordmark; most screens stay 90% white/ink with
  just one or two coral moments.
- Custom variable type (Cereal VF) at modest weights; the system trusts
  photography, not bold type, for visual heft.
- Three-product top nav (Homes / Experiences / Services), each with a
  hand-illustrated icon; the two newer products carry small "NEW" badges,
  and the active tab gets an underline rule.
- A pill-shaped global search bar divided into Where/When/Who segments by
  hairlines, ending in a circular Rausch search orb.
- Photo-first property cards: rounded image with carousel dots, a floating
  "Guest favorite" badge top-left, a heart top-right, then compact meta text.
- Dropdown menus (footer, language picker) stay flat text over white — no
  card surface, no shadow.
- Elevation is capped at a single shadow tier, used on hover-floated cards
  and dropdowns.
- An 8px base spacing system with major sections at 64px — generous, but
  tighter than editorial-magazine spacing since the marketplace wants card
  density.

## Colors

### Brand & Accent
- **Rausch** (`{colors.primary}` #ff385c) — the sole brand color: primary CTA
  fills (Reserve, Continue), the search orb, the saved-heart state, and
  inline brand links.
- **Rausch Active** (`{colors.primary-active}` #e00b41) — the press/pointer-
  down variant, slightly more saturated.
- **Rausch Disabled** (`{colors.primary-disabled}` #ffd1da) — a pale tint for
  disabled CTAs.
- **Luxe Purple** (`{colors.luxe}` #460479) and **Plus Magenta**
  (`{colors.plus}` #92174d) — sub-brand accents confined to their own
  Luxe/Plus surfaces, never mainline marketing.

### Surface
- **Canvas** (`{colors.canvas}` #ffffff) — the default floor of every public
  page; there is no public dark mode.
- **Surface Soft** (`{colors.surface-soft}` #f7f7f7) — disabled fields,
  sub-nav hover states, the inline search-filter band.
- **Surface Strong** (`{colors.surface-strong}` #f2f2f2) — circular
  icon-button fills (breadcrumb back-arrow, listing toolbar).

### Hairlines & Borders
- **Hairline** (`{colors.hairline}` #dddddd) — search-bar dividers, table
  separators, footer column splits, card borders.
- **Hairline Soft** (`{colors.hairline-soft}` #ebebeb) — lighter dividers on
  long editorial body copy.
- **Border Strong** (`{colors.border-strong}` #c1c1c1) — disabled outline
  buttons, form outlines after focus.

### Text
- **Ink** (`{colors.ink}` #222222) — the dominant text color; headlines, body,
  nav links, most inline links. Never pure black.
- **Body** (`{colors.body}` #3f3f3f) — secondary running text where ink would
  read too heavy (reviews, amenity copy).
- **Muted** (`{colors.muted}` #6a6a6a) — city-block sub-titles, inactive
  product tabs, footer sub-labels, "View all" links.
- **Muted Soft** (`{colors.muted-soft}` #929292) — disabled link text, used
  sparingly.
- **Star Rating** (`{colors.star-rating}` #222222) — same ink token; ratings
  render in ink rather than gold/yellow, a deliberate choice against a
  "cheap" travel-site feel.
- **On Primary** (`{colors.on-primary}` #ffffff) — white text on Rausch.

### Semantic
- **Error** (`{colors.primary-error-text}` #c13515) and its hover
  (`{colors.primary-error-text-hover}` #b32505) — inline form-validation
  text, distinct from Rausch.
- **Legal Link Blue** (`{colors.legal-link}` #428bff) — links inside legal
  copy only (Privacy, Terms).

### Scrim
- **Scrim** (`{colors.scrim}` #000000 at 50% opacity) — the global modal
  backdrop for date pickers, login, and language dialogs.

## Typography

### Font Family
Everything — display, body, nav, captions — runs Airbnb Cereal VF, falling
back to `Circular, -apple-system, system-ui, Roboto, "Helvetica Neue",
sans-serif`. There is no separate display family; one variable font covers
the whole scale.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale (rating-display 64px
down to the 8px uppercase-tag). Notable roles:
- `{typography.rating-display}` (64px/700) is the loudest type in the
  system — reserved for the listing-detail rating number.
- `{typography.display-xl}` (28px/700) is the homepage h1, deliberately
  small so it tucks under the search bar.
- `{typography.display-lg}` (22px/500) is the even-quieter listing h1.

### Principles
Display weight stays modest throughout — the homepage h1 at 28px/700 is
intentionally small, letting photography and the city-link grid do the
hierarchy work. The rating display is the single place the system trusts
type alone to carry weight, because a trust signal deserves the loudest
treatment available.

### Note on Font Substitutes
If Cereal VF/Circular are unavailable, **Inter** is the closest open-source
match; tighten line-height by about 2% on display sizes to approximate
Cereal's slightly tighter cap height.

## Layout

### Spacing System
- Base unit: 4px, with a 2px micro-step.
- Tokens: `{spacing.xxs}` 2px · `{spacing.xs}` 4px · `{spacing.sm}` 8px ·
  `{spacing.md}` 12px · `{spacing.base}` 16px · `{spacing.lg}` 24px ·
  `{spacing.xl}` 32px · `{spacing.xxl}` 48px · `{spacing.section}` 64px.
- Section padding: 64px vertical — tighter than typical SaaS (80–96px)
  because the marketplace needs card density per scroll.
- Card padding: 24px for host/reservation cards, 16px for property-card
  meta, 8px for caption/date-row gutters.
- Gutters: 16px between homepage grid cards, 24px in footer columns, 4px on
  dense category-strip dividers.

### Grid & Container
- Max content width: ~1280px on homepage/editorial; listing detail caps
  closer to 1080px.
- City-link grid: 6 columns at desktop, each cell a title + muted sub-label.
- Listing detail: ~64%/32% split between photo/amenity body and a sticky
  reservation card.
- Footer: 3 columns at desktop, 1 on mobile.

### Whitespace Philosophy
Editorial bands get 64px of vertical air, but card grids compress to 16px
gaps — an intentional "open hero, dense marketplace below" contrast that
signals marketplace density without overwhelming the fold.

## Elevation

Essentially one shadow tier plus flat.

- **Flat** — body, hero, footer, editorial bands (95% of the page).
- **Card hover float** — `rgba(0,0,0,0.02) 0 0 0 1px, rgba(0,0,0,0.04) 0 2px
  6px 0, rgba(0,0,0,0.1) 0 4px 8px 0`, applied on property-card hover, the
  resting search bar, and dropdown menus. This is the system's only shadow
  definition.
- **Modal scrim** — `{colors.scrim}` at 50% opacity behind date pickers,
  login, and language dialogs.

There are no progressive elevation tiers — depth comes from photography,
white-on-white separation, and rounded clipping rather than layered shadow.

## Components

### Buttons
- **`button-primary`** — Rausch fill, white text, 8px radius, 14×24px
  padding, 48px height, weight 500. The default CTA (Reserve, Continue,
  Search, account flows).
- **`button-primary-active`** — press state; background flips to
  `{colors.primary-active}`, no transform or shadow change.
- **`button-primary-disabled`** — pale Rausch tint (#ffd1da) with white text.
- **`button-secondary`** — white fill, ink text, 1px ink outline, 8px
  radius — "Save", "Cancel", inverse CTAs over Rausch.
- **`button-tertiary-text`** — plain ink text, no surface/border, underline
  on hover — "Show more" links, modal close.
- **`button-pill-rausch`** — pill-shaped Rausch CTA on featured cells
  ("Become a host").

### Search Surface
- **`search-bar-pill`** — the signature global search bar: white, 9999px
  radius, 64px tall, 1px hairline border, divided into Where/When/Who
  `{component.search-field-segment}` cells with uppercase labels above
  placeholder text.
- **`search-orb`** — 48×48px circular Rausch button terminating the search
  bar — the single hottest color moment on the homepage.

### Top Navigation
- **`top-nav`** — white, 80px tall, 1px bottom hairline. Wordmark left,
  three product tabs centered, account utilities right.
- **`product-tab-active`** — ink label, 32px illustrated icon, 2px ink
  underline.
- **`product-tab-inactive`** — muted label, no underline.
- **`new-tag`** — tiny rounded-pill "NEW" badge anchored top-right of an
  icon, uppercase 8px/700 with 0.32px tracking.

### Listing Cards
- **`property-card`** — photo-first, ~1:1 image with rounded clipping,
  carousel dots, floating "Guest favorite" badge top-left, heart top-right;
  meta beneath (title, dates/distance muted, price right-aligned).
- **`experience-card`** — taller 4:5 aspect variant with a "NEW" badge
  instead of "Guest favorite".
- **`guest-favorite-badge`** — white pill at 11px/600, the system's one
  shadow tier applied for lift.

### Listing Detail
- **`rating-display-card`** — the loudest moment: a 64px/700 rating number
  flanked by small laurel-wreath ornaments, with a "Guest favorite" tagline
  and ink stat columns beneath.
- **`amenity-row`** — a single-column icon+label list, 12px row padding,
  hairline dividers above/below the section.
- **`reviews-card`** — 2-column review excerpts, each with an author row and
  a 3-line excerpt plus "Show more".
- **`host-card`** — white, rounded, 24px padding: avatar, name, "Superhost"
  badge, response rate, "Contact host" secondary button.
- **`reservation-card`** — sticky right-rail card: nightly price, date
  selector, guest stepper, full-width "Reserve" CTA, fee breakdown.

### Date Picker
- **`date-picker-day`** — 40×40px circular cell, transparent default, ink
  text.
- **`date-picker-day-selected`** — ink fill, white text, full circle; range
  states connect with a soft-surface lozenge.

### Forms
- **`text-input`** — white surface, 1px hairline outline, 8px radius, 56px
  tall, 14×12px padding, stacked muted caption label above. On focus, border
  thickens to 2px ink — no glow or ring.

### Footer
- **`footer-light`** — white (matches canvas — no contrast footer), 48×80px
  padding, 3 link columns (Support/Hosting/Airbnb) with 24px gutters.
- **`legal-band`** — bottom strip with copyright, language/currency pickers,
  and social icons, all muted at caption-sm size.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to logo + hamburger; product tabs hide in a sheet; search bar becomes a single tappable pill; property cards 1-up; city grid 1-column; reservation card becomes a sticky bottom bar. |
| Tablet | 744–1128px | Product tabs stay but search bar narrows; property cards 2-up; city grid 2–3 columns. |
| Desktop | 1128–1440px | Full nav with 3 centered product tabs; full-width search bar with all segments; property cards 4-up; city grid 6-column; 2-column listing detail. |
| Wide | > 1440px | Content caps at 1440px (listing/search) or ~1280px (editorial); gutters absorb the rest. |

### Touch Targets
- Primary CTAs ≥48×48px.
- Search orb 48×48px circular — the most-tapped element.
- Heart save button 32×32px, compensated by generous card padding.
- Date-picker day cells 40×40px circular.

### Collapsing Strategy
- Top product tabs collapse into a hamburger sheet below 744px.
- Search bar's 3 segments collapse into one tap target opening a full-screen
  overlay on mobile.
- Card grids reduce column count at each breakpoint — never reflow rows.
- Reservation card switches from sticky rail to sticky bottom bar on mobile.

## Known Gaps

- **Hover states** are intentionally undocumented per the source's no-hover
  policy — property-card hover is known to be a subtle elevation lift, but
  precise values weren't reliably extractable.
- **Loading/skeleton states** were not visible on the analyzed surfaces.
- **Map view styling** (search-results map) uses Mapbox-tinted tiles with
  custom Rausch markers — not captured here.
- **Form input error states**: error text color is documented, but the full
  outline + helper-text combination on validation failure wasn't visible.
- **Sub-brand palettes** (Luxe, Plus) are documented as tokens only — their
  full typography/surface sub-systems live on separate sub-domains and
  aren't captured here.
