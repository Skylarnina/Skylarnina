Adapted from the Miro design analysis in [voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md) (`design-md/miro/DESIGN.md`, MIT License). Token names below refer to `references/design-tokens.yaml` in this skill.

## Overview

Miro presents itself as the AI-powered visual workspace through a confident,
slightly playful brand voice. The homepage opens on a stark white canvas
anchored by a small canary-yellow Miro wordmark top-left, a black-pill
primary CTA ("Get started free") and a secondary outline pill ("Book a
demo") — then real Miro-board mockup imagery (sticky notes, kanban, mind
maps) carries the visual weight. Deeper surfaces break the white open:
pastel feature cards (rose, teal, coral, yellow) echo the actual
sticky-note palette of the live whiteboard product, and customer-story
cards reuse those same tints to differentiate brand vignettes.

Roobert PRO — Miro's custom display face — anchors every typographic
surface, from the 80px hero display down to 11px micro labels. Its
slightly rounded, geometric character pairs naturally with the playful
product photography and the brand's friendly positioning. Black-pill
primary buttons (`rounded.full`) dominate marketing CTAs; the brand's
signature canary yellow is reserved for the wordmark, top promo banners,
and "yellow tag" feature pills — never a primary CTA. The 4-tier pricing
comparison (Free / Starter / Business / Enterprise) leads into the densest
surface in the system: a feature comparison table roughly 80 rows deep
across several section dividers.

**Key characteristics:**
- A stark white canvas with the Miro wordmark in canary yellow as the
  recognizable opening signature.
- Black-pill primary CTAs (`colors.primary` + `rounded.full`) as the
  dominant interactive element.
- Pastel feature cards (yellow, rose, coral, teal, mint) echoing the actual
  sticky-note palette.
- Roobert PRO across every UI surface, giving a geometric, slightly rounded
  character.
- Real Miro-board mockup imagery used as feature illustrations instead of
  stock photography.
- A 4-tier pricing card grid feeding into a dense feature comparison table.
- A massive dark footer with multi-column links and app-store badges.

## Colors

> Source pages: miro.com/ (homepage), /pricing/ (4-tier comparison),
> /products/ai-workflows/ (AI product), /agile/ (vertical landing),
> /customers/ (story directory). Token coverage was identical across all
> five pages.

### Brand & accent
- **Miro Yellow** (`brand-yellow`) — the brand's recognizable canary
  yellow: wordmark color, top promo banner, "yellow tag" pills.
- **Yellow Deep** (`brand-yellow-deep`) — darker variant for hover states
  and emphasis.
- **Yellow Light** (`yellow-light`) — pale yellow background tint for tag
  chips.
- **Yellow Dark** (`yellow-dark`) — yellow-tag text color (dark olive) for
  chip foreground.
- **Brand Blue / Blue Pressed** — action blue for inline links and the
  featured-pricing-tier border, with a pressed-state variant.
- **Brand Coral / Coral Light / Coral Dark** — coral accent for warm
  callouts, its pale background tint, and its deep-wine tag text color.
- **Brand Rose** — soft rose-pink for feature-card variants.
- **Brand Teal / Teal Light / Moss Dark** — brand teal, its pale
  background tint, and a deep teal-green text color.
- **Brand Pink** — pale pink for soft callouts.
- **Brand Orange Light** — soft orange for feature-card backgrounds.

### Surface
- **Canvas** — page background and primary card surface.
- **Surface / Surface Soft** — subtle section backgrounds and search-pill
  rest state.
- **Surface Yellow** — pale yellow-tinted surface for the tag chip.
- **Surface Pricing Featured** — pale lavender for the featured pricing
  tier.
- **Hairline / Hairline Soft / Hairline Strong** — three steps of 1px
  border, from primary dividers down to strong input borders.

### Text
- **Ink Deep** — headlines on lighter feature cards.
- **Ink** — primary headlines and body text.
- **Charcoal** — body-emphasis text.
- **Slate / Steel / Stone / Muted** — a descending secondary → tertiary →
  caption → disabled text ramp.
- **On Dark / On Dark Muted** — white text (and reduced-opacity white) on
  dark surfaces.

### Semantic
- **Success Accent** — confirmation/success indicator green.
- **Brand Red / Brand Red Dark** — soft and stronger red for error
  backgrounds and borders.

## Typography

### Font family
**Roobert PRO** is Miro's custom geometric sans-serif, used across every
UI surface from oversized 80px hero displays down to 11px micro labels. Its
slightly rounded, friendly character matches the brand's playful product
positioning, falling back to Noto Sans, -apple-system,
BlinkMacSystemFont, sans-serif.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale (80px hero display
down to 11px uppercase micro labels). Principles:
- Tight hero leading (1.05) gives the 80px hero a magazine-grade feel.
- Negative letter-spacing progresses from -2px to -1.5px on display sizes,
  relaxing to 0 on smaller headings.
- A dedicated `stat-display` token (64px/500) carries marketing stat
  callouts like "100M+ users."
- A single weight scale — 400 (body), 500 (medium emphasis and headings),
  600 (badges and uppercase) — Roobert PRO never uses 700 in this system.

## Layout

### Spacing system
Base unit 4px with an 8px primary increment: `spacing.xxs` (4px) through
`spacing.hero` (120px). Marketing pages use `spacing.section-lg` (96px)
between major bands; the pricing comparison tightens to `spacing.section`
(64px); the customer-story stack uses `spacing.xxl` (32px). Card padding
runs `spacing.xl` (24px) for compact cards and `spacing.xxl` (32px) for
feature panels.

### Grid & container
Marketing pages hold a 1280px max-width with 32px gutters. The pricing page
renders a 4-tier card row (Free / Starter / Business / Enterprise) at
desktop. The customer-stories page uses a 2-column grid with filter
dropdowns, and the AI Workflows page opens with a 2-column hero followed by
a 3-up feature grid.

### Whitespace philosophy
Marketing surfaces breathe generously — the 120px hero padding gives the
small wordmark room to stand alone. Pricing surfaces tighten dramatically
by comparison.

## Elevation & depth

The system runs mostly flat with strategic depth reserved for hero
mockups.

| Level | Treatment | Use |
|---|---|---|
| 0 (flat) | no shadow; hairline-soft border | default cards, table rows, form inputs |
| 1 (subtle) | `rgba(5,0,56,0.04) 0px 1px 2px 0px` | subtle hover-elevated tiles |
| 2 (card) | `rgba(5,0,56,0.06) 0px 4px 12px 0px` | standard feature cards |
| 3 (mockup) | `rgba(5,0,56,0.08) 0px 12px 32px -4px` | hero whiteboard-mockup framing |
| 4 (modal) | `rgba(5,0,56,0.12) 0px 16px 48px -8px` | modals, dropdowns |

Atmospheric depth on Miro's hero comes from the live-product-board mockup
illustrations — sticky notes layered at z-offsets, color-block tints behind
whiteboard frames. Pastel feature cards carry their own visual weight
through saturated background color rather than shadow, and customer-story
cards layer dark photographic content with overlay scrims.

## Shapes

| Token | Value | Use |
|---|---|---|
| `rounded.xs` | 4px | small chips, micro-controls |
| `rounded.sm` | 6px | discount badges |
| `rounded.md` | 8px | inputs, search-pill |
| `rounded.lg` | 12px | standard cards, table containers |
| `rounded.xl` | 16px | pricing cards, feature panels |
| `rounded.xxl` | 20px | larger feature cards |
| `rounded.xxxl` | 28px | pastel feature cards (yellow, rose, coral, teal) |
| `rounded.feature` | 32px | hero CTA banner cards |
| `rounded.full` | 9999px | all buttons, pill tabs, badges |

Real Miro board mockups render with 16px corners and a subtle drop shadow;
customer-story cards use 28px corners with full-bleed photography; template
thumbnails use 16px; customer logos present inline at a consistent 100px
height.

## Components

Definitions live in `design-tokens.yaml → components` (default and
pressed/active states only — hover states are not documented):

- **Buttons** — `button-primary` (black pill, "Get started free", pressed →
  charcoal, disabled → hairline/muted), `button-yellow` (brand-emphasis
  pill), `button-blue` (inline action pill), `button-secondary` (outlined
  pill, "Book a demo"), `button-on-dark` (white pill for dark CTA banners),
  `button-ghost` (quiet rectangular), `button-link` (inline blue text),
  `button-icon-circular` (36px utility button).
- **Cards** — `card-base` and `card-feature` (white, 16px/28px), the four
  pastel variants (`card-feature-yellow/coral/teal/rose`), `card-customer-story`
  (image-filled), `card-stat` (64px stat callout).
- **Pricing** — `pricing-card`, `pricing-card-featured` (lavender + blue
  border, the Business tier), `pricing-card-enterprise` (dark-canvas tier).
- **Inputs** — `text-input`/`text-input-focused` (focus flips to brand
  blue), `search-pill`, `filter-dropdown` (pill-shaped, used on
  /customers).
- **Tabs** — `pill-tab`/`pill-tab-active`, `toggle-monthly-yearly`.
- **Badges** — `badge-promo`, `badge-tag-yellow`, `badge-tag-purple`,
  `badge-tag-coral`, `badge-success`, `badge-discount`.
- **Tables** — `comparison-table`/`comparison-row` for the dense pricing
  feature comparison.
- **Documentation-style components** — `whiteboard-mockup` (the signature
  product-illustration component), `template-card`, `industry-tile`,
  `faq-accordion-item`, `logo-wall-item`, `capterra-badge`,
  `app-store-badge`.
- **Signature components** — `hero-band-marketing`, `cta-banner-dark`,
  `footer-region`/`footer-link` (massive 6-column dark footer).

### Navigation
The sticky white top nav (~64px) carries the yellow-square Miro wordmark
plus horizontal links (Product, Solutions, Resources) on the left, and
"Login / Pricing / Contact sales" links plus the black-pill "Get started
free" CTA on the right.

## Do's and don'ts

**Do**
- Reserve `brand-yellow` for the wordmark, top promo banner, and
  "yellow tag" chips.
- Use `colors.primary` (black) as the dominant CTA on all surfaces.
- Pair pastel feature cards (yellow, rose, coral, teal) with white feature
  cards in the same viewport.
- Apply `rounded.full` to every button, pill tab, and status badge.
- Apply `rounded.xxxl` (28px) to pastel feature cards.
- Use real Miro-board mockups as feature illustrations.
- Keep Roobert PRO consistent across every UI surface.

**Don't**
- Don't use `brand-yellow` on standard CTAs or large background surfaces.
- Don't introduce accent colors beyond yellow and the brand pastels.
- Don't soften button corners — the pill is a brand signature.
- Don't reduce hero leading below 1.05.
- Don't apply heavy shadows on flat documentation-style cards; reserve
  elevation for whiteboard mockups.
- Don't use stock photography — always show the live product board UI.

## Responsive behavior

### Breakpoints
| Name | Width | Key changes |
|---|---|---|
| Mobile (small) | <480px | single column; hero scales to 36px; pill nav collapses to hamburger; pricing stacks 1-up |
| Mobile (large) | 480–767px | feature tiles 2-up; hero scales to 48px |
| Tablet | 768–1023px | 2-column feature grids; pill-tab nav returns |
| Desktop | 1024–1279px | 4-tier pricing card row; customer-story grid 2-up; hero at 64px |
| Wide Desktop | ≥1280px | full hero presentation, 80px hero display |

### Touch targets
Pill buttons render at 40–44px effective height, at the WCAG AAA floor.
Circular icon buttons go from 36×36px desktop to 44×44px mobile. Form
inputs render at 44px height. Filter dropdowns render at ~36px, bumping to
44px on mobile.

### Collapsing strategy
The promo banner stays full-width and truncates below 480px. The top nav
collapses to a hamburger below 1024px. The 2-column hero collapses to
stacked below 1024px. Pricing goes 4-column → 2-column tablet → 1-column
mobile with the comparison table becoming horizontal-scroll. The
customer-story grid goes 2-up → 1-up below 768px. Hero type steps 80px →
60px → 48px → 36px, and the footer goes 6-column → 3-column → 2-column →
accordion at the smallest sizes.

## Known gaps

- Dark-mode token values are not surfaced in the source.
- Animation/transition timings are not extracted; 150–200ms ease is a
  reasonable default.
- Form-validation success states beyond the default pattern are not
  captured.
- The sticky-note color tints inside the actual live whiteboard product are
  richer than what marketing surfaces capture here.
