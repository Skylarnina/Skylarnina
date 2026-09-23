Adapted from the Mistral AI design analysis in [voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md) (`design-md/mistral.ai/DESIGN.md`, MIT License). Token names below refer to `references/design-tokens.yaml` in this skill.

## Overview

Mistral AI carries a singular, almost cinematographic visual signature. The
homepage opens with "Frontier AI. In your hands." rendered in elegant
near-serif display type over photography of a mountain landscape bathed in
mustard-orange sunset light. Below the hero, every page closes with the
same recognizable device: a horizontal "sunset stripe" gradient band
running red → orange → yellow → cream that wraps the foot of the page just
above the footer. This stripe is the brand's single most recognizable
element — it appears without exception on the homepage, the Le Studio
product page, the coding solutions page, news articles, the contact form,
and the services tier page.

The system pairs `PP Editorial Old` (a near-serif, elegant display face)
for hero displays with `Inter` for everything else — body, headings, UI.
Cream-yellow surfaces (`colors.cream`, `colors.surface-cream-soft`) anchor
form panels and feature cards; saturated orange (`colors.primary`) carries
every primary CTA; deep mountain photography on the homepage and dark code
mockups inside Le Studio provide photographic depth. Cards are rectangular
at `rounded.lg` (12px) — distinctly less playful than peers like Miro or
Mintlify, which lean on pills everywhere. Buttons match this restraint at
`rounded.md` (8px), never pills — Mistral's geometry reads as sober and
editorial rather than bubbly.

**Key characteristics:**
- Atmospheric mountain-sunset hero photography (orange-red-yellow gradient
  sky).
- A horizontal "sunset stripe" band at the bottom of every page.
- Cream-yellow surfaces for form panels and feature cards.
- `PP Editorial Old` for hero displays; `Inter` for everything else.
- `rounded.md` (8px) buttons and `rounded.lg` (12px) cards — editorial, not
  playful, geometry.
- Saturated orange primary CTA carrying every action call.

## Colors

> Source pages: mistral.ai/ (homepage), /products/studio (Le Studio
> product), /solutions/coding (coding solution),
> /news/vibe-remote-agents-mistral-medium-3-5 (news), /contact (contact
> form), /services (services tiers). Token coverage was identical across
> all six pages.

### Brand & accent
- **Mistral Orange** (`primary`) — the primary CTA color and brand orange.
- **Orange Deep** (`primary-deep`) — pressed-state and emphasis variant.
- **Sunshine 300/500/700/800/900** — a five-step spectrum of atmospheric
  light-to-saturated sunset orange used in gradient stops.
- **Yellow Saturated** — pure brand yellow used in the sunset stripe
  gradient.
- **Block 5/6/7** — additional spectrum stops (light-yellow → mid-yellow →
  deep-orange) along the same gradient.

### Cream / neutral warm
- **Cream** — warm yellow-cream surface for form panels, feature cards,
  footer.
- **Cream Light** — a lighter cream variant.
- **Cream Deeper** — a more-saturated cream for badge/tag chips.
- **Beige Deep** — the 1px border color on cream surfaces.

### Surface
- **Canvas** — page background and card surface.
- **Surface / Surface Cream** — subtle quieter backgrounds and cream-tinted
  surfaces.
- **Surface Code** — dark code-block / IDE mockup surface.
- **Hairline / Hairline Soft / Hairline Strong** — three steps of border
  weight.

### Text
- **Ink** — primary headlines and body text.
- **Ink Tint** — a slightly softer black for hero overlay text.
- **Charcoal / Slate / Steel / Stone / Muted** — a descending
  emphasis-to-disabled text ramp.
- **On Dark / On Dark Muted** — white text and reduced-opacity white on
  dark surfaces.
- **On Cream** — ink text specifically on cream surfaces.

### Semantic
- **Link** — the inline link color, matching the primary orange.

## Typography

### Font family
**PP Editorial Old** is Mistral's signature near-serif elegant display
typeface, used for hero displays, large numbers, and editorial section
openers. Its slightly classical, intelligent character deliberately
contrasts the contemporary product positioning, falling back to 'Times New
Roman', Georgia, serif. **Inter** carries body, navigation, buttons,
labels, and captions, falling back to ui-sans-serif, system-ui,
-apple-system, sans-serif. **JetBrains Mono** handles code blocks and IDE
mockups, falling back to 'SF Mono', Menlo, Consolas, monospace.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale (84px hero display
down to an 11px eyebrow). Principles:
- The editorial/sans pairing — PP Editorial Old (near-serif, classical)
  anchors hero displays; Inter (geometric sans) carries everything else.
  The contrast between the two IS the brand voice.
- Generous body leading (1.55 on body-md) supports editorial readability
  across long-form pages.
- Tight hero leading (1.05 at 84px) creates a magazine-grade typographic
  display.
- Negative letter-spacing progresses with size — display sizes run -1.5px
  to -0.5px, relaxing to 0 on smaller heads.
- A dedicated `stat-display` token (56px Editorial) carries stat callouts
  like "75% / 80% / 100%".

## Layout

### Spacing system
Base unit 4px with an 8px primary increment: `spacing.xxs` (4px) through
`spacing.hero` (120px). Marketing pages use `spacing.section-lg` (96px);
content pages tighten to `spacing.section` (64px). Card padding is
`spacing.xl` (24px) for compact cards, `spacing.xxl` (32px) for feature and
form panels.

### Grid & container
Marketing pages hold a 1280px max-width with 32px gutters. The hero band
splits 2-column (text left, sunset photography right) on desktop. Le
Studio uses a 3-up feature grid below the hero. The contact page centers a
single-column cream form panel (~520px max-width), and the services page
uses a 4-tier card layout with a cream feature panel as separator.

### Whitespace philosophy
Marketing surfaces breathe generously — the 120px hero padding lets the
mountain-sunset photography fill the frame. Form pages tighten
dramatically: the contact form panel uses 32px internal padding with
fields stacked on a 16px gap.

## Elevation & depth

The system runs mostly flat with strategic atmospheric depth from
photography.

| Level | Treatment | Use |
|---|---|---|
| 0 (flat) | no shadow; hairline-soft border | default cards, table rows, form inputs |
| 1 (subtle) | `rgba(0,0,0,0.04) 0px 1px 2px 0px` | hover-elevated tiles |
| 2 (card) | `rgba(0,0,0,0.04) 0px 4px 12px 0px` | standard feature cards |
| 3 (mockup) | `rgba(0,0,0,0.08) 0px 12px 24px -4px` | IDE mockup, code editor frames |
| 4 (modal) | `rgba(0,0,0,0.12) 0px 16px 48px -8px` | modals, dropdowns |

Atmospheric depth on the hero comes from the photographic mountain-sunset
imagery itself — the natural light gradient does the work. The sunset
stripe closing band carries its own depth via a multi-stop gradient
(red → orange → yellow → cream). IDE/code mockups use dark-canvas
backgrounds with a subtle drop shadow.

## Shapes

| Token | Value | Use |
|---|---|---|
| `rounded.xs` | 4px | small chips, micro-controls |
| `rounded.sm` | 6px | discount badges, compact UI |
| `rounded.md` | 8px | buttons, inputs, search-pill, code blocks |
| `rounded.lg` | 12px | cards, modals, panels — the dominant card radius |
| `rounded.xl` | 16px | larger feature panels |
| `rounded.xxl` | 20px | featured emphasis cards |
| `rounded.full` | 9999px | status badges, pill tabs (used sparingly) |

The radius scale is sober and editorial — Mistral does not use pill
buttons. 8px covers buttons, 12px covers cards, and the full pill radius is
reserved for badges and the rare pill tab.

### Photography geometry
Hero photography is full-bleed atmospheric mountain-sunset imagery with no
internal framing. IDE/code mockups render with 12px corners on a dark
canvas. Customer logos present inline at 60–80px height, and product
imagery (Le Studio mockup, agent UI mockups) sits in 12px panels with a
subtle border.

## Components

Definitions live in `design-tokens.yaml → components` (default and
pressed/active states only — hover states are not documented):

- **Buttons** — `button-primary` (saturated orange, pressed → deeper
  orange, disabled → hairline/muted), `button-cream` (warm secondary),
  `button-dark` (dark primary on cream surfaces), `button-secondary`
  (outlined), `button-on-cream` (white button on cream backgrounds),
  `button-link` (inline orange text).
- **Cards** — `card-base`/`card-feature` (white), `card-cream`/
  `card-cream-soft` (warm surfaces for services tiers and perk callouts),
  `card-feature-product` (subtle elevation), `card-photographic` (dark,
  image-filled).
- **Pricing** — `pricing-card`, `pricing-card-featured` (cream background +
  orange border).
- **Inputs** — `text-input`/`text-input-focused` (focus flips to orange),
  `text-area`, `contact-form-panel` (the cream-tinted container hosting
  the whole contact form).
- **Tabs** — `pill-tab`/`pill-tab-active` (used sparingly on product
  pages), `segmented-tab`/`segmented-tab-active` (underline style).
- **Badges** — `badge-orange`, `badge-cream`, `badge-dark`.
- **Code** — `code-block`, `code-block-header` for IDE-style mockups on Le
  Studio and agent demos.
- **Documentation-style components** — `feature-icon-tile`,
  `industry-tile`, `stat-cell` (stat-display token), `customer-testimonial-card`,
  `logo-wall-item`, `faq-accordion-item`, `app-store-badge`.
- **Signature components** — `hero-band-sunset` (gradient hero), the
  `sunset-stripe-band` (the brand's most recognizable element, spanning
  full width above the footer on every page), `cta-banner-cream`,
  `footer-region`/`footer-link` (5-column cream footer with language
  picker and social icons).

### Navigation
The sticky white top nav (~64px) carries the Mistral M-mark and "MISTRAL
AI_" wordmark plus horizontal links (Products, Solutions, Research, Blog,
Customers, Company) on the left, and a "Contact Sales" link plus a
black-pill "Try Studio" CTA on the right.

## Do's and don'ts

**Do**
- Reserve `colors.primary` (saturated orange) for primary CTAs and active
  states only.
- Use the sunset-stripe band at the foot of every page — it's the brand's
  most recognizable signature.
- Pair `PP Editorial Old` (display) with `Inter` (UI) — never substitute
  either with a generic alternative.
- Apply `rounded.md` (8px) to buttons and `rounded.lg` (12px) to cards
  consistently.
- Use cream-yellow surfaces for form panels, feature cards, and the
  footer.
- Anchor heroes with photographic mountain-sunset imagery, or its
  atmospheric-gradient equivalent.
- Use the `stat-display` token (PP Editorial 56px) for stat callouts to
  keep editorial character.

**Don't**
- Don't use pill-shaped buttons — Mistral's geometry is sober and
  editorial, not playful.
- Don't introduce accent colors beyond the orange/yellow/cream sunset
  palette.
- Don't reduce hero leading below 1.05 — the editorial display needs that
  magazine-grade tightness.
- Don't replace `PP Editorial Old` hero displays with Inter — the
  editorial/sans contrast IS the brand.
- Don't apply heavy shadows on flat documentation-style cards; reserve
  elevation for IDE mockups.
- Don't drop the sunset stripe band from any page bottom — it's the
  brand's continuity element.

## Responsive behavior

### Breakpoints
| Name | Width | Key changes |
|---|---|---|
| Mobile (small) | <480px | single column; hero scales to 40px; pill nav collapses to hamburger; pricing stacks 1-up |
| Mobile (large) | 480–767px | feature tiles 2-up; hero scales to 52px |
| Tablet | 768–1023px | 2-column feature grids; pill-tab nav returns; hero 64px |
| Desktop | 1024–1279px | multi-column layouts; hero 76px; stat row at full width |
| Wide Desktop | ≥1280px | full 84px hero presentation |

### Touch targets
Buttons render at 40–44px effective height (at the WCAG AAA floor with
`10px 20px` padding). Form inputs render at 44px height. Pill tabs render
at ~32px, bumping to 44px on mobile.

### Collapsing strategy
The promo banner stays full-width and truncates below 480px. The top nav
collapses to a hamburger below 1024px. The 2-column hero (text + photography)
collapses to stacked below 1024px. Pricing tiers go 4-column → 2-column
tablet → 1-column mobile. The stat row goes 3-column → stacked below
768px. Hero type steps 84px → 64px → 52px → 40px, and the footer goes
5-column → 3-column → 1-column accordion. The sunset stripe band stays
full-width on every breakpoint.

## Known gaps

- No dark-mode token values are surfaced — the brand has not shipped a
  published dark-mode palette.
- Animation/transition timings are not extracted; 150–200ms ease is a
  reasonable default.
- Form-validation success states beyond the default pattern are not
  captured.
- Sunset-stripe gradient stops are approximations — actual values may vary
  slightly page to page, though the visual rhythm stays consistent.
