# Cal.com Design System — Full Analysis

Adapted from the Cal.com design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/cal/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Cal.com's marketing surface reads as a clean, friendly modern-SaaS
interface: white `colors.canvas` (`#ffffff`), near-black primary CTAs
(`colors.primary` — `#111111`), custom **Cal Sans** display type, and light
gray `colors.surface-card` (`#f5f5f5`) cards holding fragments of the actual
product UI. Every band carries clear hierarchy, generous whitespace, and a
single obvious action — the system is confidently engineered without trying
to impress.

Type splits into two clean roles: **Cal Sans** (the custom geometric
display face, used for h1/h2/h3 and hero headlines) and **Inter** (used for
everything else — body, buttons, nav, captions). Cal Sans runs at weight
600 with negative letter-spacing (-0.5px to -2px depending on size), giving
it a modern, slightly condensed, distinctly Cal.com character.

Component voltage comes from **product UI fragments shown directly inside
cards** — calendar widgets, scheduling forms, automation diagrams,
integration tiles. Rather than painting marketing illustrations of the
product, Cal.com shows the actual product chrome at small scale embedded
directly in the marketing flow.

The footer flips to `colors.surface-dark` (`#101010`) — a deep near-black
that visually closes every long-scroll page. It's the only dark surface in
the system; everything above it stays white with light-gray cards.

**Key characteristics:**
- White canvas with a black primary CTA (`#111111`); buttons are `8px`
  radius with confident weight-600 labels — a standard friendly-SaaS
  button.
- Custom Cal Sans display typeface for headlines (Inter weight 600 as a
  substitute). Negative letter-spacing on display sizes gives it a
  geometric, precise, slightly condensed feel.
- Light-gray card surfaces (`#f5f5f5`) for feature cards, testimonials, and
  non-featured pricing tiers; the featured pricing tier flips to the dark
  surface — the only dark card on light pages.
- Product UI fragments embedded directly in cards — real schedule pickers,
  calendar widgets, and integration grids, not illustrations.
- A `nav-pill-group` component wraps grouped nav segments (e.g., a sub-nav
  switcher) in a pill-radius container — one of the system's signature
  interactive components.
- Avatars are perfect circles, 36px diameter, used in testimonial rows and
  team-listing surfaces.
- The footer is dark (`#101010`) with light text (`#a1a1aa`), closing every
  page even though the body above stays white.
- Section rhythm sits at `spacing.section` (96px) — tight enough to feel
  modern-SaaS, generous enough to breathe.
- Radius is hierarchical: `8px` for buttons and inputs, `12px` for content
  cards, `16px` for the hero app-mockup container, pill for the nav-pill-
  group and badges, full circle for avatars and icon buttons.

## Colors

### Brand & accent
- **Primary** (`#111111`) — the dominant action color: all primary CTAs and
  h1/h2 display type. Its press state shifts to `primary-active` (`#242424`).
- **Brand Accent** (`#3b82f6`) — used sparingly on inline links and a small
  "customer story" highlight badge; Cal.com is a near-monochrome brand, so
  this blue appears rarely.
- **Badge Pastels** — a small pastel set for category badges and avatar
  fills: orange (`#fb923c`), pink (`#ec4899`), violet (`#8b5cf6`), emerald
  (`#34d399`). They appear on tag pills and small accent moments inside
  product UI fragments — never on hero CTAs.

### Surface
- **Canvas** (`#ffffff`) — the default page floor.
- **Surface Soft** (`#f8f9fa`) — the nav-pill-group background and very
  soft section dividers.
- **Surface Card** (`#f5f5f5`) — feature cards, testimonial cards, badge
  pills, default avatar fills.
- **Surface Strong** (`#e5e7eb`) — a hairline-border alternative and the
  disabled-button background.
- **Surface Dark** (`#101010`) — the footer background, the only dark
  surface seen on every page; also used for the featured pricing-tier card.
- **Surface Dark Elevated** (`#1a1a1a`) — nested cards inside the dark
  footer or featured pricing card.
- **Hairline** (`#e5e7eb`) — the 1px border tone on light surfaces: input
  borders, table dividers, occasional content-card outlines.
- **Hairline Soft** (`#f3f4f6`) — a barely-visible divider between sections
  that share the white canvas.

### Text
- **Ink** (`#111111`) — all headlines and primary text.
- **Body** (`#374151`) — the default running-text color.
- **Muted** (`#6b7280`) — secondary text: sub-headings, breadcrumbs, footer
  body.
- **Muted Soft** (`#898989`) — tertiary text: captions, fine print,
  copyright lines.
- **On Primary / On Dark** (`#ffffff`) — text on primary buttons and the
  dark footer.
- **On Dark Soft** (`#a1a1aa`) — footer body text, a slightly muted white
  for the link rows.

### Semantic
- **Success** (`#10b981`) — confirmation states and success badges in
  product UI.
- **Warning** (`#f59e0b`) — warning callouts.
- **Error** (`#ef4444`) — validation errors.

## Typography

### Font family
The system runs Cal Sans for display and the brand wordmark, and Inter for
everything else. Cal Sans is Cal.com's custom geometric display typeface —
slightly condensed, weight 600, negative letter-spacing. Inter handles
body, buttons, navigation, captions, and code blocks (paired with JetBrains
Mono). Both fall back to
`-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`.

The split is functional: Cal Sans (display, weight 600, -0.5 to -2px
tracking) sets h1/h2/h3, while Inter (body/UI, weight 400-600, 0 tracking)
handles paragraphs, labels, buttons, and nav.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale. Key entries:
`display-xl` (64/600, -2px tracking, homepage h1), `display-lg` (48/600,
-1.5px, section heads), `display-md` (36/600, -1px, sub-section heads and
card titles), `display-sm` (28/600, -0.5px, CTA-band heads and pricing tier
prices), `title-lg` (22/600, pricing plan names — Inter), `title-md`
(18/600, feature card titles), `body-md` (16/400, running text), `button`
(14/600, standard button labels).

### Principles
Cal Sans is the brand voice — every display headline uses it, and Inter
handles the supporting type. The boundary is strict: body copy never uses
Cal Sans, and display headlines never use Inter. Cal Sans without negative
letter-spacing reads as off-brand — the -0.5px to -2px tracking is part of
the voice. Display weight stays at 600 across all sizes, never 700 or 500 —
that middle weight is what makes Cal Sans feel modern and confident without
tipping into bombastic.

### Font substitutes
If Cal Sans is unavailable, **Inter** at weight 600 with -0.04em
letter-spacing is a usable approximation, though its humanist forms differ
from Cal Sans's geometric character. **Manrope** at weight 700 is another
close alternative.

## Layout

- **Base unit:** 4px. Full scale: `xxs` 4px, `xs` 8px, `sm` 12px, `md` 16px,
  `lg` 24px, `xl` 32px, `xxl` 48px, `section` 96px.
- **Section padding:** `spacing.section` (96px), the universal vertical
  rhythm between editorial bands.
- **Card internal padding:** `spacing.xl` (32px) for feature cards and
  pricing-tier cards; `spacing.lg` (24px) for testimonial and
  product-mockup cards.
- **Gutters:** `spacing.lg` (24px) between cards in 3-up grids; `spacing.md`
  (16px) inside footer columns.
- **Max content width:** roughly 1200px centered.
- **Grid:** single 12-column grid for editorial body, with the hero band
  often using a 7/5 split (h1 left, app mockup right); feature card grids
  run 3-up desktop, 2-up tablet, 1-up mobile; pricing grid runs 4-up
  desktop, 2-up tablet, 1-up mobile; footer runs 4-column desktop, 2-up
  tablet, 1-up mobile.
- **Whitespace philosophy:** generous but not excessive — 96px section
  padding and 32px card padding calibrated for fast scanning. Every band
  carries a single h1 + h2 + supporting cards, never densely packed lists,
  which reads as confident-not-shouting.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| Flat | no shadow, no border | body sections, top nav, hero bands |
| Soft hairline | 1px `hairline` border | inputs, table dividers, occasionally on cards |
| Card surface | `surface-card` background, no shadow | feature cards, testimonials |
| Subtle drop shadow | faint shadow at low alpha (`0 1px 2px rgba(0,0,0,0.05)`, `0 4px 12px rgba(0,0,0,0.08)`) | pricing tier cards, hover-elevated states |
| Featured tier | `surface-dark` background, no shadow needed | the featured pricing tier inverts to dark — color contrast does the elevation work |

The elevation philosophy is soft and modern: small drop shadows on elevated
cards, color-block contrast for emphasis, no heavy shadows, no
neumorphism, no glassmorphism. Calendar widgets and product UI fragments
embedded inside marketing cards carry their own internal shadows from the
product chrome itself — not system tokens. Avatar circles in testimonial
sections sometimes carry pastel fill colors, adding a small chromatic
flourish without breaking the monochrome brand voice.

## Shapes

| Token | Value | Use |
|---|---|---|
| `rounded.xs` | 4px | almost unused, reserved for badge accents |
| `rounded.sm` | 6px | small inline buttons, dropdown items |
| `rounded.md` | 8px | standard CTA buttons, text inputs, category tabs |
| `rounded.lg` | 12px | content cards (feature, testimonial, pricing tier) |
| `rounded.xl` | 16px | the hero app-mockup card — a slightly larger radius for the marquee component |
| `rounded.pill` | 9999px | nav-pill-group, badge pills |
| `rounded.full` | 9999px / 50% | avatars, icon buttons |

Avatar photos use full circles at 36px or 40px. Product UI fragments inside
marketing cards keep their native chrome (which often has its own internal
radii — calendar grid cells, button rows). Hero illustration zones use
16:9 or 4:3 ratios with `rounded.xl` corners.

## Components

Definitions live in `design-tokens.yaml → components`. Summary:
- **top-nav** — white 64px bar with the Cal.com wordmark at left, a
  primary menu (Product, Solutions, Resources, Pricing, Enterprise), and a
  right cluster with "Sign in" text-link and a "Sign up free" primary
  button.
- **nav-pill-group** — a pill-radius wrapper around 2-3 sub-nav segments
  (e.g., Personal / Teams / Enterprise); the active segment renders as a
  white pill with a subtle shadow inside the wrapper — a signature
  interactive treatment.
- **Buttons** — `button-primary` (black fill, white text, 8px radius,
  press state darkens), `button-secondary` (white with hairline outline),
  `button-icon-circular` (36×36 circular, hairline border), `button-text-
  link` (no background, used for "Sign in"), `text-link` (monochrome inline
  links).
- **Cards & containers** — `hero-band` (7/5 grid hero, 96px padding),
  `hero-app-mockup-card` (16px-radius card showing the real Cal.com booking
  widget with calendar grid and time slots), `feature-card` (light gray,
  32px padding, icon + title + description), `feature-icon-card` (white
  variant with hairline border), `product-mockup-card` (real product UI
  fragments), `testimonial-card` (light gray with avatar + quote),
  `pricing-tier-card` (white, plan name + price + checklist + CTA),
  `pricing-tier-card-featured` (flips to the dark surface, no accent
  border or scale shift needed — the dark surface itself is the signal).
- **Inputs** — `text-input` (white, 8px radius, hairline border, 40px
  height), `text-input-focused` (border thickens/shifts to ink).
- **Tags** — `badge-pill` (pill label, gray or pastel fill), `avatar-circle`
  (36px, photo or pastel fill with initials), `rating-stars` (inline stars
  in the orange badge color).
- **Tabs** — `category-tab`/`category-tab-active` inside the nav-pill-group;
  active state adds a white background and subtle shadow.
- **CTA / footer** — `cta-band-light` (light-gray pre-footer card with h2 +
  centered button), `footer` (dark navy, 4-column link list, wordmark at
  top-left in white — the only dark surface on every page).

## Do's and don'ts

**Do**
- Reserve `colors.primary` (`#111111`) for primary CTAs and h1/h2 type —
  Cal.com's button is near-black, not blue.
- Use Cal Sans for every display headline, paired with Inter body — never
  blur the boundary.
- Apply negative letter-spacing on display sizes (-0.5 to -2px); Cal Sans
  without it reads as off-brand.
- Use light-gray feature cards for abstract feature claims and white
  product-mockup cards for "look at the actual product" moments —
  deliberately.
- Embed real product UI fragments inside marketing cards instead of
  painting illustrations of the product.
- Keep avatar circles at 36px, perfect circles, sometimes with pastel
  fills — the only place badge pastels appear.
- Use the nav-pill-group for grouped sub-nav segments.
- End every page with the dark footer — the light-to-dark transition is
  part of the editorial rhythm.

**Don't**
- Don't use accent colors (blue, badge pastels) on primary CTAs — the
  system is monochrome at the action layer.
- Don't bold display weight beyond 600; Cal Sans at 700 reads as
  bombastic.
- Don't use radius beyond `rounded.xl` (16px) on cards — larger radii read
  as consumer-app, not professional booking software.
- Don't place dark surface cards anywhere except the footer and the
  featured pricing tier — it's a deliberate, scarce signal.
- Don't repeat the same surface mode in two consecutive bands; Cal.com's
  pacing alternates white → light-gray → white → product-mockup-card →
  white → dark-footer.
- Don't add hover styling beyond what the system already encodes — primary
  darkens on press, nothing else changes.

## Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Mobile | < 768px | hamburger nav; hero h1 64→32px; hero-app-mockup-card stacks below content; feature/pricing grids 1-up; footer 4 cols → 1 |
| Tablet | 768–1024px | top nav stays horizontal but tightens; nav-pill-group wraps; feature cards 2-up; pricing 2-up |
| Desktop | 1024–1440px | full top-nav; 3-up feature cards; 4-up pricing tiers |
| Wide | > 1440px | same as desktop with more outer breathing room; max content caps at 1200px |

Touch targets: `button-primary` is minimum 40×40px; `button-icon-circular`
is exactly 36×36 (slightly under WCAG's 44×44, compensated by the centered
icon and full-circle silhouette); `text-input` height is 40px; category
tabs inside the nav-pill-group reach 44px+ effective tap area with
surrounding padding. Top nav collapses to a full-screen hamburger sheet
below 768px; the hero's 7/5 grid collapses to single column (headline
first, mockup card below); feature grids reduce columns rather than
shrinking cards; pricing tiers collapse 4 → 2 → 1 while the featured dark
tier stays visually distinct throughout; the nav-pill-group wraps to
multi-row on tablet if segments don't fit; product UI fragments and avatar
photos keep native aspect ratios and circular crops at every breakpoint.

## Known gaps

- The frequency analyzer reported zero button variants because Cal.com
  renders most CTAs as styled `<a>` links rather than `<button>` tags;
  button styles here are documented from screenshot ground-truth plus
  standard Cal Sans/Inter baselines.
- Cal Sans is licensed to Cal.com and not available as a public web font;
  substitutes are documented under Typography.
- The badge pastel set (orange/pink/violet/emerald) is documented from
  observed avatar fill colors; exact hex values may shift seasonally.
- Animation and transition timing (calendar slot picker, schedule
  confirmation, integration grid hover-reveal) is out of scope.
- Form validation states beyond the focused text-input weren't extracted —
  error/success states would need a sign-up or booking flow to confirm.
- The actual booking widget surface (cal.com/{username}) is product, not
  marketing, and is out of scope here.
- Avatar photos in testimonials sometimes carry pastel fills with initials
  instead of photographs; both treatments coexist on the same page.
