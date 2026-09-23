Adapted from the MongoDB design analysis in [voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md) (`design-md/mongodb/DESIGN.md`, MIT License). Token names below refer to `references/design-tokens.yaml` in this skill.

## Overview

MongoDB carries a strong dual-mode visual identity — deep navy-teal hero
bands paired with the unmistakable bright MongoDB green CTA pill, set
against stark white documentation and pricing surfaces. The homepage opens
with "One data platform. Unlimited AI potential." over a deep navy hero,
the green pill sitting at the visual center as the primary CTA. Lower on
the page, embedded terminal-aesthetic code mockup cards sit on the dark
hero band before the page breaks into white feature cards. The pricing
page renders a 3-tier comparison (Free / Flex / Dedicated) with the
featured tier highlighted by a soft mint background and bright green
border. The MongoDB University page presents a course catalog grid where
each tile carries a colored category tag (orange, purple, green, teal) —
these category-encoding accents are the only place, outside the brand
green, where saturated color appears.

The system uses `Euclid Circular A` as its display face — contemporary
geometric, confident but not overly playful — which pairs naturally with
both the developer-tool aesthetic of the database product and the
educational positioning of the learning surfaces. Cards use `rounded.lg`
(12px) corners; buttons use `rounded.full` pills universally. The
brand-teal palette anchors hero bands, footer, code mockups, and dark CTA
banners.

**Key characteristics:**
- Deep navy/teal hero bands with bright MongoDB green CTA pills.
- Stark white pricing/documentation surfaces with colored category tags for
  course tiles (purple, orange, green, teal).
- `Euclid Circular A` across every UI surface.
- Pill-shaped buttons and 12px-rounded cards.
- A 3-tier pricing comparison (Free / Flex / Dedicated) with a featured
  mint-highlighted tier.
- Code mockup cards with a terminal-aesthetic dark canvas.

## Colors

> Source pages: mongodb.com/ (homepage), /products/platform/atlas-database
> (Atlas product), /products/self-managed/community-edition,
> learn.mongodb.com/ (MongoDB University),
> /solutions/use-cases/artificial-intelligence (AI), /pricing (3-tier
> comparison). Token coverage was identical across all six pages.

### Brand & accent
- **MongoDB Green** (`brand-green`) — the brand's most recognizable
  signal, the bright pill-CTA color.
- **Green Dark** (`brand-green-dark`) — the inline link color and
  secondary green.
- **Green Mid** (`brand-green-mid`) — mid-spectrum green for atmospheric
  tints.
- **Green Soft** (`brand-green-soft`) — a pale-mint background tint for
  success badges and the featured pricing tier.
- **Brand Teal Deep** (`brand-teal-deep`) — deep navy-teal for hero bands
  and footer.
- **Brand Teal / Brand Teal Mid** — mid-spectrum teal and a lighter teal
  for hero platform cards.

### Category accent (course tags)
- **Accent Purple** — course tag for "Database & Security."
- **Accent Orange** — course tag for "Search."
- **Accent Pink** — a course tag variant.
- **Accent Blue** — a course tag variant for Atlas/cloud topics.

### Surface
- **Canvas White** — page background and primary card surface.
- **Canvas Dark** — code-block backgrounds, dark mockup canvas.
- **Surface / Surface Soft** — subtle section backgrounds and search-pill
  rest state.
- **Surface Feature** — pale mint background for the featured pricing tier.
- **Hairline / Hairline Soft / Hairline Strong / Hairline Dark** — four
  steps of border weight from primary dividers to dark-surface borders.

### Text
- **Ink** — primary headlines and body text (deep navy-teal).
- **Charcoal / Slate / Steel / Stone / Muted** — a descending
  emphasis-to-disabled text ramp.
- **On Dark / On Dark Muted** — white text and reduced-opacity white on
  dark surfaces.

### Semantic
- **Warning Background / Warning Text** — a pale yellow callout background
  with a matching warning copy color.

## Typography

### Font family
**Euclid Circular A** is MongoDB's geometric sans-serif primary, falling
back to -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif.
**Source Code Pro** handles code mockups, falling back to 'SF Mono',
Menlo, Consolas, monospace.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale (72px hero
display down to 11px eyebrow). Principles:
- Tight hero leading (1.10) on the 72px display.
- Negative letter-spacing on display sizes, from -1.5px down to -0.5px.
- Weight 600 is reserved for buttons and small emphasis moments (FAQ
  headings, badges).
- Generous body leading (1.55) supports technical documentation
  readability.

## Layout

### Spacing system
Base unit 4px with an 8px primary increment, running `spacing.xxs` (4px)
through `spacing.hero` (120px). Marketing pages use `spacing.section-lg`
(96px); pricing tightens to `spacing.section` (64px).

### Grid & container
1280px max-width with 32px gutters. Pricing renders a 3-tier card row
above a dense feature comparison table. The Learn catalog uses a 3-up
course tile grid and a 4-up certification grid. AI use cases open with a
2-column hero paired with atmospheric illustration.

### Whitespace philosophy
Marketing surfaces breathe generously — the 120px hero padding gives deep
teal bands room. Pricing and Learn surfaces tighten dramatically by
comparison.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 (flat) | no shadow; hairline border | default cards, table rows |
| 1 (subtle) | `rgba(0,30,43,0.04) 0px 1px 2px 0px` | hover-elevated tiles |
| 2 (card) | `rgba(0,30,43,0.08) 0px 4px 12px 0px` | feature cards |
| 3 (mockup) | `rgba(0,30,43,0.12) 0px 12px 24px -4px` | code mockup over hero |
| 4 (modal) | `rgba(0,30,43,0.16) 0px 16px 48px -8px` | modals, dropdowns |

Dark teal hero bands carry atmospheric gradient depth. Code mockup cards on
the hero use the canvas-dark surface with a terminal aesthetic. The
pale-mint pricing-feature tier uses a brand-tinted shadow rather than a
neutral one.

## Shapes

| Token | Value | Use |
|---|---|---|
| `rounded.xs` | 4px | course category tags |
| `rounded.sm` | 6px | type badges, code chips |
| `rounded.md` | 8px | inputs, search-pill, code blocks |
| `rounded.lg` | 12px | cards, pricing tiers, course tiles |
| `rounded.xl` | 16px | larger feature panels |
| `rounded.xxl` | 24px | featured product showcases |
| `rounded.full` | 9999px | all buttons, status badges |

Hero illustrations sit on full-bleed dark backgrounds. Course tile
thumbnails use 12px corners, and the customer logo wall presents wordmarks
at a consistent 60–80px height.

## Components

Definitions live in `design-tokens.yaml → components` (default and
pressed/active states only — hover states are not documented):

- **Buttons** — `button-primary` (bright green pill, the dominant CTA,
  pressed → deeper green, disabled → hairline/muted), `button-secondary`
  (outlined pill), `button-on-dark`/`button-secondary-on-dark` (variants
  for dark hero bands), `button-ghost` (quiet rectangular), `button-link`
  (inline green text).
- **Cards** — `card-base`/`card-feature`, `card-product-deploy` (Atlas /
  Community), `card-feature-dark` (dark teal on the hero band),
  `card-course` (University tile with a category tag, title, description,
  and "Get Started →" link), `card-cert`.
- **Pricing** — `pricing-card`, `pricing-card-featured` (mint background +
  green border, the Flex tier).
- **Inputs** — `text-input`/`text-input-focused` (focus flips to
  green-dark), `search-pill` (44px) and `search-pill-large` (56px, atop the
  University catalog).
- **Tabs** — `pill-tab`/`pill-tab-active` ("MongoDB Atlas / Enterprise
  Advanced" at the top of pricing), `segmented-tab`/`segmented-tab-active`.
- **Badges** — `badge-green`, `badge-green-soft`, `badge-purple`,
  `badge-orange`, `badge-popular` ("Most Popular" tier indicator).
- **Code** — `code-block`, `code-mockup-card` (embedded on the hero band
  with terminal-aesthetic content).
- **Tables** — `comparison-table`/`comparison-row` for the pricing feature
  comparison.
- **Documentation-style components** — `service-tile` ("Customize your
  deployment" 6-up grid), `why-card` ("Loved by builders"),
  `customer-testimonial-card`, `logo-wall-item`, `faq-accordion-item`.
- **Signature components** — `hero-band-dark` (with embedded code mockup),
  `hero-platform-card`, `cta-banner-dark`, `footer-region`/`footer-link`
  (dark teal, 6-column).

### Navigation
The sticky white top nav (~64px) carries the MongoDB leaf logo and
"Solutions / Resources / Company / Pricing" links on the left, and a "Sign
In" link plus the bright-green pill "Try Free" CTA on the right.

## Do's and don'ts

**Do**
- Use `brand-green` for primary CTAs everywhere.
- Pair dark-teal hero bands with bright green CTA pills.
- Apply `rounded.full` to every button and status badge.
- Apply `rounded.lg` (12px) to cards consistently.
- Use category accent colors (purple, orange, green, teal) only for course
  tags.
- Keep `Euclid Circular A` consistent across every UI surface.
- Use code mockup cards with terminal-aesthetic content for product
  showcases.

**Don't**
- Don't use the bright green for body text or large surfaces.
- Don't introduce accent colors beyond the brand green and the
  category-encoding palette.
- Don't soften button corners — the pill is a brand signature.
- Don't replace deep teal hero bands with white hero bands.
- Don't apply heavy shadows on flat documentation cards; reserve elevation
  for code mockups.
- Don't use Source Code Pro for prose.

## Responsive behavior

### Breakpoints
| Name | Width | Key changes |
|---|---|---|
| Mobile (small) | <480px | single column; hero 36px; pricing 1-up; course catalog 1-up |
| Mobile (large) | 480–767px | course tiles 2-up; hero 48px |
| Tablet | 768–1023px | 2-column feature grids; hero 56px |
| Desktop | 1024–1279px | 3-tier pricing card row; 3-up course catalog; hero 64px |
| Wide Desktop | ≥1280px | full 72px hero presentation |

### Touch targets
Pill buttons render at 40–44px effective height. Form inputs render at
44px. The large search pill renders at 56px, and pill tabs go from ~32px up
to 44px on mobile.

### Collapsing strategy
The promo banner stays full-width and truncates below 480px. The top nav
collapses to a hamburger below 1024px. The hero's code mockup card moves
below the text on mobile. Pricing tiers go 3-column → 2-column tablet →
1-column mobile. The course catalog goes 3-up → 2-up tablet → 1-up mobile.
Hero type steps 72px → 56px → 48px → 36px, and the footer goes 6-column →
3-column → accordion.

## Known gaps

- Specific dark-mode token values for canvas/surface beyond the hero bands
  are not surfaced.
- Animation/transition timings are not extracted; 150–200ms ease is a
  reasonable default.
- Form-validation success states beyond the default pattern are not
  captured.
- Course-tile category color mappings are observation-based rather than
  formally documented.
