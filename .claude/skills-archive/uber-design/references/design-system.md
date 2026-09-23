# Uber Design System — Full Analysis

Adapted from the Uber design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/uber/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Uber operates a sprawling transportation-and-delivery super-app, and its
marketing pages signal that scale through restraint rather than spectacle.
There's no secondary color, no competing illustration style, nothing
fighting the headline for attention. The page is essentially a black-and-white
duet: `colors.primary` black is the conversion anchor — every CTA pill,
the nav login button, the footer fill — while `colors.canvas` white carries
everything else. The one recurring piece of decoration is a set of editorial
4:3 illustrations (riders, drivers, parking lots, highway traffic) that
ground the marketing copy without leaking any accent color into the system.

Typography does the rest of the work. Two proprietary faces cover every
role: `UberMove` at weight 700 for headlines, ranging from 20px up to 52px
with tight 1.22–1.25 line-height, and `UberMoveText` at weights 400/500 for
body copy, buttons, and links. Neither face is ever italicized or
letter-spaced. Headlines stay in sentence case throughout — uppercase is
reserved for the rare section eyebrow like "WHY BECOME."

The pill is the brand's one shape signature. Every interactive control —
primary and secondary CTAs, subtle gray chips, floating white buttons,
category pills, app-download badges — rounds all the way to `rounded.pill`
(999px). Cards and larger surfaces step down to `rounded.xl` (16px); the
oversized annual-showcase card uses that same 16px radius at scale. The one
outlier is the ride-request form's tab toggle, which uses a tighter
36px radius rather than the canonical pill.

**Key characteristics:**
- A two-tier CTA hierarchy: black pill for primary conversion, white pill
  (sometimes shadowed) for secondary, soft-gray pill for tertiary/chips.
- The pill (999px) is the single interactive shape everywhere except the
  tab-toggle (36px) and larger cards (16px).
- Every headline sits in sentence-case weight-700 display type; there's no
  all-caps display anywhere.
- 4:3 editorial illustrations are the only consistent decorative device —
  no gradients, no atmospheric backdrops, no ornamental shadows.
- A repeating white-card/black-band rhythm runs down the page, not just in
  the hero — black bands also appear as mid-page promo callouts.
- A signature hero ride-request card: pickup + destination inputs, a
  date/time chip, and a black "See prices" pill, stacked inside a shadowed
  16px card.

## Colors

### Brand & accent
- **Ink black** (`colors.primary`, `#000000`) — the system's only
  conversion color: primary CTAs, footer fill, dark promo bands, nav login
  buttons. There is no secondary accent anywhere on the marketing site.
- **Surface pressed** (`colors.surface-pressed`, `#e2e2e2`) — the pressed
  state for white pills; grey appears only in active states.
- **Black elevated** (`colors.black-elevated`, `#282828`) — a near-black
  hover tone reserved for the translucent white tab-toggle.

### Surface
- **Canvas** (`colors.canvas`, `#ffffff`) — the default page background.
- **Canvas soft** (`colors.canvas-soft`, `#efefef`) — category chips,
  ride-request input rows, subtle pill fills.
- **Canvas softer** (`colors.canvas-softer`, `#f3f3f3`) — a slightly
  lighter gray for nested inputs on white cards.

### Text
- **Ink** (`colors.ink`, `#000000`) — every heading and body paragraph on
  light surfaces.
- **Body** (`colors.body`, `#5e5e5e`) — captions and supporting copy.
- **Hairline mid** (`colors.hairline-mid`, `#4b4b4b`) — muted links inside
  footer columns and breadcrumb-style nav.
- **Mute** (`colors.mute`, `#afafaf`) — placeholder text and low-priority
  metadata.
- **On dark** (`colors.on-dark`, `#ffffff`) — all text set on `colors.ink`
  surfaces.

### Semantic
Uber doesn't run a dedicated error/success/warning palette on its public
marketing surface — validation reads through black or the illustration
system instead. The one chromatic color anywhere in the system is
`colors.link` (`#0000ee`), the plain browser-default link blue used only for
inline links buried in legal and footer text.

## Typography

### Font family
Two custom faces carry the entire system:
1. A custom geometric display sans (captured as `UberMove`), weight 700
   only, sizes 20–52px, with line-heights tightening to 1.22–1.25 at
   display scale for a "poured onto the page" feel.
2. A custom text sans (`UberMoveText`) at weights 400/500 for body, button,
   link, and small headings, used from 12px up to 24px on ride-request form
   labels. Tracking stays neutral throughout.

The two faces share a family DNA but never trade roles — display never
carries a paragraph, text never carries a hero headline.

### Hierarchy
See `design-tokens.yaml → typography` for the complete scale. Highlights:
`display-xxl` 52px/700 for the hero, stepping down through `display-xl`
36px, `display-lg` 32px, `display-md` 24px, `display-sm` 20px; body runs
`body-lg` 18px/500 down to `caption` 12px/400; buttons use `button-large`
18px/500 and `button-md` 16px/500.

### Principles
- Sentence-case is the voice — no all-caps headlines outside rare eyebrows.
- Weight 700 belongs to headlines; weight 500 belongs to buttons and
  emphasis — never promote a button label to 700.
- No tracking flourish — the display face is never letter-spaced.
- Two faces, two strict roles: UberMove for display, UberMoveText for
  everything else.

### Font substitutes
Both faces are proprietary. *Inter* at weight 700 with
`font-feature-settings: "ss01"` is the closest open-source match for
display; *Geist* weight 700 is a fallback. For the text face, *Inter*
weights 400/500 match the geometric width and x-height well; *Plus Jakarta
Sans* offers a softer alternative.

## Layout

- Base unit: 4px, with a few 6px sub-multiples inside button padding.
  Full scale: `spacing.xxs` 4px through `spacing.3xl` 32px.
- Marketing bands sit at 32px top/bottom padding; promo cards inset 24px.
- Content cards use 24px interior padding; the ride-request form tightens
  to 16px to stay compact.
- Button rows, chip rows, and app-store badge rows use 12px gaps between
  siblings.
- Container maxes out around 1200px with 32px desktop gutters (16px on
  mobile). Promo cards run 2-up desktop / 1-up mobile; app-download pills
  run 2-up desktop / 1-up mobile.
- Card-to-card spacing (roughly a full 32px gutter) carries the page rhythm;
  inside a card the headline/paragraph/CTA stack stays tight at 8px. Black
  bands and the footer skip internal hairlines entirely — content sits flat
  on ink with white text.

### Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Mobile | <600px | Hamburger nav; promo cards stack; request form goes full-width. |
| Mobile-large | 600–767px | Same as mobile; chip rows scroll horizontally. |
| Tablet | 768–1119px | 2-up promo grid; nav stays horizontal until ≥1120px. |
| Desktop | 1120–1135px | Full nav row; 2-up promo cards. |
| Desktop-large | ≥1136px | Container caps ~1200px; bands stay edge-to-edge. |

`button-primary` renders roughly 44px tall (meeting WCAG AAA); the larger
`button-large-rounded` reaches ~56px. Category chips grow to ≥44px on touch
viewports. Nav collapses to a full-screen hamburger overlay below desktop;
the ride-request card goes edge-to-edge at mobile; the annual-showcase card
scales from a 2:3 desktop frame to 4:3 on mobile. Editorial illustrations
and photography stay hard-edged and uncropped at all sizes; the logo bar
renders as consistent-height monochrome SVGs.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 — flat | none | most cards and surfaces |
| 1 — subtle drop | `rgba(0,0,0,.12) 0 4px 16px` | card-elevated on light bands |
| 2 — card drop | `rgba(0,0,0,.16) 0 4px 16px` | ride-request form card, large content cards |
| 3 — pill float | `rgba(0,0,0,.16) 0 2px 8px` | the floating white pill over photography |

Rather than lean on shadow, the brand gets its depth from two other moves:
flipping mid-page sections to solid black (the polarity shift itself reads
as depth), and letting each promo card's 4:3 illustration carry visual
weight. Nested pill buttons at varying heights also create a subtle stacked
hierarchy.

## Shapes

| Token | Value | Use |
|---|---|---|
| `rounded.none` | 0px | full-bleed hero bands, footer, raw images |
| `rounded.md` | 8px | ride-request form inputs |
| `rounded.lg` | 12px | smaller secondary card chrome |
| `rounded.xl` | 16px | the canonical card radius — promo, content, request-form, showcase cards, large buttons |
| `rounded.pill` | 999px | every pill button, chip, app-download badge |
| `rounded.pill-tab` | 36px | the Ride/Drive tab-toggle on the hero |
| `rounded.full` | 9999px | circular icon containers |

Editorial illustrations run 4:3 in promo cards and 16:9 for full-width
showcases; driver/rider portraits crop to 4:5 inside 16px card frames; the
annual-showcase image scales 2:3 desktop to 4:3 mobile with the headline
overlaying the bottom edge.

## Components

Full specs live in `design-tokens.yaml → components`. Summary:
- **Buttons** — `button-primary` (black pill), `button-secondary` (white
  pill), `button-subtle` (gray pill), `button-floating` (shadowed white
  pill over photography), `button-large-rounded` (the one CTA that breaks
  the pill rule, at 16px radius, used inside the ride-request flow), and
  `button-tab-translucent` (the 36px tab toggle).
- **Cards** — `card-content`/`card-elevated` (default), `card-soft-tinted`
  (gray-tinted callout), `promo-card-illustrated` and its dark counterpart
  `promo-card-on-dark`, `request-form-card` (the hero ride-request chrome),
  and `showcase-image-card` (the oversized annual showcase).
- **Inputs** — `text-input` and `text-input-on-soft`, both flat-cornered
  (`rounded.none`) rows inside the request-form card.
- **Navigation** — `nav-bar` (light by default, flips to dark on rare
  pages like Eats), `nav-link`, and a black `footer`.
- **Signature pieces** — `hero-band-light`/`hero-band-dark`,
  `category-button` (horizontal-scroll chip row), `faq-row` (hairline
  accordion, no card chrome), `app-download-pill`, and
  `icon-button-circular`.
- **Links** — `link-blue` (legal fine print only), `link-on-dark`,
  `link-mute`, `link-mute-soft`.
- **Example surfaces** (`ex-*`) — auto-derived kit-mirror demonstrations
  (pricing tier, product selector, app-shell row, data-table cell, auth
  card, modal, empty state, toast) that re-skin the brand's primitives onto
  ten common SaaS/product surfaces for consistency across generated kits.

## Do's and don'ts

**Do**
- Reserve `colors.primary` black for every primary CTA pill — one black
  pill per viewport is the brand's entire conversion story.
- Round every interactive element to `rounded.pill` (999px) — it's the
  brand's one geometric signature.
- Keep cards at `rounded.xl` (16px) across promo, content, request-form,
  and showcase surfaces.
- Set every headline in sentence-case weight-700 display type.
- Flip to a black promo band mid-page to break up white-on-white rhythm —
  the polarity shift is the depth cue.
- Anchor every promo card with a 4:3 editorial illustration rather than
  stock photography.

**Don't**
- Don't add a second brand accent — the system is black, white, and
  grayscale only.
- Don't render the primary CTA as a `rounded.xl` rectangle outside the
  documented `button-large-rounded` exception.
- Don't use all-caps display headlines; sentence-case is non-negotiable.
- Don't default every card to a shadow — flat is the default state; shadow
  is reserved for the floating pill and the request-form card.
- Don't lean on illustration alone — the pill geometry and black/white
  duet carry the brand even without imagery.
- Don't adjust the display face's letter-spacing; default tracking is part
  of the voice.
- Don't use `rounded.full` (9999px) on cards — that radius is for circular
  elements only; cards stay at 16px.

## Known gaps

- The `ex-*` example components are auto-derived kit-mirror surfaces, not
  directly observed on the live site — treat them as reasonable
  extrapolations, not verified specs.
- No dedicated error/success/warning palette is documented for the public
  marketing surface.
- Font substitutes are recommendations, not exact matches — UberMove and
  UberMoveText are proprietary and not publicly distributed.
