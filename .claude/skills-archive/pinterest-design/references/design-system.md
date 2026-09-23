# Pinterest Design System — Full Analysis

Adapted from the Pinterest marketing-site design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/pinterest/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Pinterest's system is built around a single instructional principle: get
out of the photograph's way. The chrome is a quiet warm-cream neutral
palette (`surface-soft`, `surface-card`, `canvas`) set in Pinterest's
proprietary Pin Sans, with Pinterest Red (`colors.primary`, `#e60023`)
reserved exclusively for the Sign-up CTA, the active-tab indicator, and the
sticky top-nav anchor. Every other surface fades behind the imagery — pin
tiles, category tiles, thumbnails, profile shots — that is the actual
product.

The system runs on two distinct surface modes that alternate down the home
page: a **hero/CTA chrome** (cream surfaces, a large 70px Pin Sans display
headline, alternating left/right photo-illustrated feature cards) and a
**content masonry** (a column-based grid of 16px-radius pin cards on
`surface-card` with zero internal padding — the pin photograph *is* the
card). The search-results page is almost pure masonry: a tight column grid
of mixed-aspect-ratio pin imagery, topped by a small filter-chip strip and
the sticky red Sign-up CTA in the upper right. The `create.pinterest.com`
business surface flips back to a more traditional editorial layout while
still obeying every other system rule — Pin Sans, cream chrome, red CTA,
16px-radius pills.

The system's signature gesture is its shape geometry: 16px radius
(`rounded.md`) covers nearly every surface — buttons, inputs, pin cards,
feature cards — while 32px (`rounded.lg`) is reserved for large pin cards
and modals. There are exactly three radius values in active use: 16px,
32px, and pill (9999px). The system never goes sharp and never lands on a
medium value between 16 and 32 — that jump is deliberate.

**Key characteristics:**
- A single-accent CTA system: Pinterest Red carries every primary action;
  everything else is monochrome.
- Pin Sans typography across every role, from the 70px display tier down
  to 12px captions — no serif, no monospace anywhere.
- A two-radius shape system (16px standard, 32px large/modal) plus pill
  for fully-rounded elements.
- A masonry pin grid as the load-bearing visual element, preserving each
  pin's natural aspect ratio.
- A warm-cream neutral chrome (`#f6f6f3`) that recedes behind imagery
  without competing for attention.
- A sticky top nav with the always-red Sign-up CTA anchored in the upper
  right at every breakpoint.
- A modal overlay (login/signup) using a soft scrim over page content
  rather than a full navigation jump.

## Colors

> **Source pages:** `/` (home), `/search/pins/?q=bold lip` (search
> results), `create.pinterest.com/` (creator marketing), and a creator
> article page. The chrome palette is identical across all four.

### Brand & accent
- **Pinterest Red** (`colors.primary`, `#e60023`) is the brand's only
  highly-saturated color — Sign-up CTAs, the sticky top-nav anchor, the
  active tab-strip state, and the wordmark.
- **Pinterest Red Pressed** (`colors.primary-pressed`, `#cc001f`) is the
  primary button's pressed state, a single notch deeper than brand red.

### Surface
- **Canvas** (`#ffffff`) is true white — the base for the primary nav,
  modals, feature cards, and content body.
- **Soft Surface** (`#fbfbf9`) is a faintly cream-tinted off-white used for
  the home-page hero's body wash.
- **Surface Card** (`#f6f6f3`) is the warm-cream card/tile background,
  carrying category tiles, the default search-bar fill, the default
  secondary-button fill, and pin-card backgrounds — the dominant card
  surface.
- **Secondary BG** (`#e5e5e0`) is a gray-cream fill used for the secondary
  button ("I already have an account"), a notch deeper than surface-card.
- **Surface Dark** (`#262622`) is a warm near-black reserved for the rare
  dark CTA strip on the creator marketing site.
- **Hairline** (`#dadad3`) marks 1px row dividers and footer column rules,
  with **Hairline Soft** (`#e5e5e0`) as a lighter inline variant.

### Text
- **Ink** (`#000000`) — primary headlines, button text, primary nav links.
- **Ink Soft** (`#211922`) — the inline-link color in body prose, a
  near-black with a faint warm cast; the brand's only "color" in chrome
  besides Pinterest Red.
- **Body** (`#33332e`) — default paragraph text on canvas.
- **Mute** (`#62625b`) — metadata, footer links, secondary captions.
- **Ash** (`#91918c`) — disabled button text, placeholder text.
- **Stone** (`#c8c8c1`) — the least-emphasis utility text.

### Semantic
- **Error** (`#9e0a0a`) and **Error Deep** (`#cc001f`) mark validation and
  destructive messaging.
- **Success Deep** (`#103c25`) and **Success Pale** (`#c7f0da`) mark
  in-product success states.
- **Focus Outer** (`#435ee5`) with **Focus Inner** (`#ffffff`) forms the
  system's double-ring focus signal.

### Editorial accents
Used sparingly inside content imagery and category badges: **Accent
Pressed Blue** (`#617bff`), **Accent Purple** (`#7e238b`), and **Accent
Purple Deep** (`#6845ab`) for editorial recommendation badges like
"Pinterest Predicts."

## Typography

### Font family
**Pin Sans** is Pinterest's proprietary geometric sans, used across every
text role at weights 400/500/600/700, falling back through
`-apple-system` → `system-ui` → `Segoe UI` → `Roboto` → `Helvetica Neue` →
`Arial`. Its distinctive trait is tight letter-spacing at display sizes
(-1.2px on the display-xl and heading-xl tiers), which gives 70px
headlines a confident, dense feel rather than the airy spread of a typical
display geometric sans.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale — display-xl at
70px down to caption-sm at 12px. The system has an unusually steep drop
from display (70px) directly to body (16px) on the home hero, with no
intermediate tier between them. The negative tracking on the largest
tiers (-1.2px / -0.8px) tightens headlines into something more confident
than a default geometric sans would produce, while body settles at a
generous 1.4 line-height so multi-line descriptions stay easy to read.

### Font substitutes
Pin Sans is proprietary. **Inter** (weights 400/500/600/700) is the
closest open-source substitute, matching its geometry, x-height, and
metric balance within ~3% at body sizes. **Manrope** is a strong secondary
choice for the display tier. Apply -1.2px tracking at display sizes
regardless of which substitute is used.

## Layout

- **Base unit:** 8px, with finer 4/6/7px steps for tight inline gaps in
  pills and chips.
- **Universal section rhythm:** every page uses `spacing.section` (64px)
  as the vertical gap between major blocks. Pin grids use the tightest
  gutter in the system, `spacing.sm` (8px), so imagery effectively touches
  across columns.
- **Modal padding:** 32px on all sides.
- **Max width:** ~1280px at desktop with 24px gutters (~48px at
  ultrawide).
- **Pin masonry grid:** auto-fitting columns — 5-6 at ultrawide, 4 at
  desktop, 3 at tablet, 2 at mobile-landscape, 1 at mobile — each tile
  preserving its natural aspect ratio (square, 2:3, 3:4, 4:5 — never
  landscape, since pins are vertically oriented).
- **Home hero feature row:** an asymmetric two-column split alternating
  text-left/image-right and image-left/text-right down the page.
- **Footer:** a 4-column link grid at desktop, collapsing to 2-up at
  tablet and 1-up at mobile.

Whitespace is generous on marketing surfaces and tight on discovery
surfaces: the home page sits sections 64px apart with 32px-padded feature
cards, while the search-results page collapses to an 8px-gutter masonry
grid tiling imagery edge to edge. The system effectively behaves like two
tools sharing one chrome — a magazine (hero/feature/CTA/footer) and a
search engine (nav/filter/grid/load-more).

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 — Flat | No border, no shadow | Pin cards, feature cards, footer — the dominant treatment |
| 1 — Hairline border | 1px `hairline` | Inputs, footer dividers, in-list rows |
| 2 — Modal scrim + soft shadow | Dark scrim + 16px ambient shadow | Login/signup modal, image-preview modal |

Pinterest's content surfaces carry effectively no shadow elevation — pin
cards sit flat on canvas. The only "elevation" appears on the modal layer,
where a 16px ambient shadow paired with a 50%-opacity scrim lifts the
modal above the page. Decorative depth otherwise comes entirely from the
photography itself — food photography, fashion close-ups, interior shots —
and from a small `pin-overlay-pill` (e.g. "Cherry red", "Preppy look")
floated over a corner of category-tile imagery.

## Shapes

| Token | Value | Use |
|---|---|---|
| `rounded.none` | 0px | Footer, primary nav, page sections — flat structural surfaces |
| `rounded.sm` | 8px | Rare medium-radius surfaces (editorial tooltips) |
| `rounded.md` | 16px | Buttons, inputs, pin cards, feature cards, category tiles — the dominant radius |
| `rounded.lg` | 32px | Large pin cards, modal cards |
| `rounded.full` | 9999px | Search bar, filter chips, overlay pills, icon buttons, avatars |

The radius vocabulary is essentially three values: 16px for most things,
32px for big cards and modals, and pill for circular/rounded elements.
There are no sharp-cornered buttons or pin cards anywhere in the system.

Pin imagery keeps mixed aspect ratios — square, 3:4, 2:3, 4:5 portrait, and
rare landscape — inside 16px corners on small tiles and 32px on large
feature pins. Category-tile thumbnails stay square at 16px radius, and
avatar circles run 32-48px at full pill radius.

## Components

Full specs live in `design-tokens.yaml → components`. Summary:

- **Buttons** — `button-primary` (red fill, universal CTA), `button-
  secondary` (gray-cream fill, second-tier actions), `button-tertiary`
  (ghost text), `button-icon-circular` (carousel paddles, modal close),
  `button-pill-on-image` (the overlay pill on category-tile photography),
  `button-disabled`.
- **Filter & tab chips** — `filter-chip` / `filter-chip-active`, which
  flips from cream to fully-inverted black-on-white when selected.
- **Inputs** — `text-input` / `text-input-focused` (double-ring focus
  signal) and `search-bar` / `search-bar-focused` (pill-shaped, anchored
  in the nav center).
- **Cards & containers** — `pin-card` (the standard masonry tile, zero
  internal padding), `pin-card-large` (32px-radius feature variant),
  `pin-overlay-pill`, `category-tile`, `feature-card` / `feature-card-
  soft`, `modal-card` (login/signup), `hero-cta-strip` (dark CTA band on
  the creator site).
- **Navigation** — `primary-nav` (64px, centered search bar, always-red
  Sign-up CTA on the right) and a mobile variant that collapses the search
  bar to a magnifier icon.
- **Footer** — `footer-section` (4-column link grid, red wordmark +
  copyright row beneath).
- **Inline** — `link-inline` (ink-soft, no underline by default).

## Do's and don'ts

**Do**
- Reserve Pinterest Red for primary CTAs, the active-tab indicator, and
  the wordmark only — never decorative.
- Use 16px radius on every interactive element and standard card; 32px
  only for large pin cards and modals; pill only for circular elements.
- Stage every pin image inside a card with zero internal padding — the
  photograph *is* the card.
- Stack sections at the 64px rhythm, tightening pin grids to 8px gutters
  so imagery effectively touches.
- Anchor a search-term overlay pill in the corner of category-tile
  photography as the system's signature decorative gesture.
- Build hierarchy from font weight and size, not color tinting — body
  stays the same color regardless of section context.
- Apply -1.2px letter-spacing on the largest display and heading-xl
  tiers.

**Don't**
- Don't use sharp-cornered buttons or cards — nothing in the system sits
  at 0px radius except structural bands.
- Don't introduce drop shadows on cards — the only shadow in the system is
  the modal's 16px ambient shadow.
- Don't pad pin cards internally — metadata sits over the image as an
  overlay pill, never below it.
- Don't substitute a different red for Pinterest Red — it's precisely
  `#e60023`.
- Don't use the ink-soft link tint outside of inline body anchors.
- Don't introduce a third radius value between 16px and 32px — the system
  jumps directly from medium to large with nothing in between.

## Responsive behavior

| Name | Width | Key changes |
|---|---|---|
| ultrawide | 1920px+ | Pin grid expands to 5-6 columns |
| desktop-large | 1440px | Default — 4-column pin grid, full nav |
| desktop-small | 1024px | Pin grid → 3 columns |
| tablet | 768px | Pin grid → 2 columns; nav becomes a hamburger drawer; search bar collapses to icon-only |
| mobile | 480px | Single-column pin grid; hero display scales 70px → ~44px |
| mobile-narrow | 320px | Hero further scales to ~36px |

Touch targets meet WCAG AA (≥44×44px) across primary/secondary buttons
(~40px), search bar (48px), text inputs (44px), and filter chips (extended
to 44px via inline padding). Collapsing follows a consistent pattern: the
nav's search bar shrinks then collapses to an icon; the pin grid steps
5/6→4→3→2→1 columns with gutters tightening from 8px to 6px on mobile; the
home feature row goes from alternating two-column to a stacked single
column with full-bleed imagery; the modal goes from a centered ~480px card
to a full-width bottom sheet.

## Known gaps

- Mobile screenshots weren't captured — responsive behavior is synthesized
  from desktop evidence and Pinterest's known mobile pattern.
- Hover states aren't documented, per the source's own policy.
- The authenticated, logged-in experience (home feed, board pages, profile
  pages) isn't in the captured pages — this document covers the logged-out
  marketing and search experience.
- Pin-detail (single-pin overlay with comments and related pins) isn't
  captured and likely introduces undocumented components.
- The native mobile app isn't documented here — this is web-only chrome.
- Form validation states beyond the focused-input treatment aren't
  present in the captured surfaces.
