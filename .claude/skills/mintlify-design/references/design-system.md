Adapted from the Mintlify design analysis in [voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md) (`design-md/mintlify/DESIGN.md`, MIT License). Token names below refer to `references/design-tokens.yaml` in this skill.

## Overview

Mintlify sits at the crossroads of polished SaaS marketing and dense
developer documentation. Its home and startups pages open with cinematic
atmospheric heroes — a soft sky-gradient backdrop with cloud illustrations
on the homepage, a dark teal-to-mint gradient with a rocket launch on the
startups page — that feel closer to a consumer SaaS landing page than a
docs tool. Beneath that surface, the deeper pages (pricing comparison, live
documentation) collapse into dense, information-heavy layouts where Inter
body copy runs 14–16px across long-form prose, syntax-highlighted code
blocks, and a 3-column documentation grid.

The brand's mint green (`colors.brand-green`) shows up sparingly but
decisively: on the hero "Get started" pill, the green checkmarks inside
feature lists, the border of the featured pricing tier, and active-state
indicators inside the docs UI. Black-pill primary buttons dominate the
marketing flow, while white-on-dark inversions appear on dark hero bands.
Pairing Inter (body, headings) with Geist Mono (code, inline references,
type signatures) reinforces the developer-tool identity without needing a
third typeface.

**Key characteristics:**
- Atmospheric gradient hero bands (sky-blue to cream on the homepage;
  teal-to-mint on startups) deliver cinematic marketing presentation.
- The signature mint green is reserved for accent CTAs, active states, and
  feature confirmations — never a large surface.
- Black-pill primary buttons (`colors.primary` + `rounded.full`) carry
  marketing CTAs.
- Inter handles all UI prose; Geist Mono is scoped strictly to code blocks,
  inline code, and type/property signatures.
- The 3-column documentation layout (sidebar / prose / TOC) supports dense
  14px body type for long-form developer reading.
- A tightly-controlled radius scale — `rounded.lg` (12px) for marketing,
  `rounded.full` for pills — avoids in-between corner softening.
- A vibrant testimonial card (`colors.testimonial-orange`) deliberately
  breaks the color rhythm for emotional impact.

## Colors

> Source pages: mintlify.com/ (homepage), /startups (program page),
> /pricing (comparison), /docs/components/tabs (live documentation). Token
> coverage was identical across all four pages.

### Brand & accent
- **Mintlify Mint** (`brand-green`) — the signature accent: hero "Get
  started" pill, feature-list checkmarks, featured pricing tier border,
  sidebar active-indicator dots.
- **Deep Mint** (`brand-green-deep`) — the pressed/active variant of the
  mint accent.
- **Soft Mint** (`brand-green-soft`) — a subtle tint for success states and
  confirmation surfaces.
- **Brand Tag** (`brand-tag`) — documentation tag/reference color used in
  `<Tabs>`-style annotations and code-tag chips.
- **Brand Annotate** (`brand-annotate`) — inline code-annotation green from
  the twoslash annotation system.
- **Brand Warn** (`brand-warn`) — code warning highlight (deprecated,
  caution).
- **Brand Error** (`brand-error`) — red used for required-field labels and
  error highlights.
- **Testimonial Orange** (`testimonial-orange`) — warm coral used on the
  Cursor testimonial card and other warm callout surfaces.

### Surface
- **Canvas** — primary page/card background.
- **Canvas Dark** — promo banner, dark inversions, code editor wrapper.
- **Surface / Surface Soft** — subtle and quieter section backgrounds,
  search-pill rest state, code-inline background, sidebar active state,
  FAQ accordion.
- **Surface Code** — dark code-block wrapper background.
- **Hairline / Hairline Soft** — primary 1px borders and quieter table-row
  dividers.

### Hero atmospheric
- **Hero Sky From/To** — atmospheric sky-blue-to-cream gradient on the
  homepage hero.
- **Hero Dark From/To** — dark teal-to-mint gradient on the startups hero.

### Text
- **Ink** — primary headlines and CTA text.
- **Charcoal** — body text, code-inline foreground.
- **Slate** — secondary text and metadata.
- **Steel** — tertiary text, table headers, inactive sidebar items, footer
  links.
- **Stone** — captions, twoslash cursor color, muted labels.
- **Muted** — de-emphasized labels and disabled text.
- **On Dark / On Dark Muted** — white text (and reduced-opacity white) on
  dark surfaces.

### Semantic
Error tones derive from `brand-error` for input borders, required-field
labels, and validation messaging.

## Typography

### Font family
**Inter** carries every UI surface — body, headings, navigation, button
labels, captions — falling back to -apple-system, BlinkMacSystemFont,
'Segoe UI', sans-serif. **Geist Mono** is scoped to code blocks, inline
code references, and type signatures (`string`, `number`, `boolean`) and
property names in API docs, falling back to 'SF Mono', Menlo, Consolas,
'Geist Mono Fallback', monospace. Neither face uses italics — emphasis
comes from weight (500/600), color shift, or background highlighting in
code references.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale (72px hero display
down to 11px uppercase micro labels). Principles:
- Tight hero leading (1.05) gives the 72px hero a magazine-grade feel.
- Negative letter-spacing progresses inversely with size — display sizes
  run -2px to -1.5px; smaller headings relax to 0.
- Documentation-grade body (1.50 line-height at 14–16px) keeps long-form
  docs comfortable to read.
- The Inter/Geist Mono pairing — Inter everywhere else, Geist Mono
  surgically for code — is itself the developer-respect signal.
- Uppercase micro labels with +0.5px tracking carry sidebar section
  headers and "REQUIRED" annotation tags.

## Layout

### Spacing system
Base unit 4px with an 8px primary increment: `spacing.xxs` (4px) through
`spacing.hero` (120px) — see the full ladder in the tokens file. Marketing
pages use `spacing.section-lg` (96px) between major bands; the pricing
comparison tightens to `spacing.section` (64px); documentation surfaces use
`spacing.xxl` (32px) between subsections. Card padding is `spacing.xl`
(24px) for compact cards, `spacing.xxl` (32px) for pricing/feature panels,
and `spacing.section` (64px) for the hero-scale testimonial card.

### Grid & container
Marketing pages hold a 1280px max-width with 32px gutters, often splitting
hero/feature bands into text-left, illustration/mockup-right layouts. The
pricing page renders 3 tier cards (FREE / Lift Off / Custom) above a
detailed feature comparison table. Documentation pages use a strict
3-column grid: ~240px sidebar, ~720px max-width prose, ~200px TOC. Logo
walls run 6-up at 80–100px logo height.

### Whitespace philosophy
Marketing surfaces breathe generously — the 120px hero padding gives
atmospheric gradient backdrops room to read. Documentation tightens
dramatically: section gaps drop to 32px, table rows pack to 16px, and
sidebar nav compresses to 8px vertical rhythm.

## Elevation & depth

The system runs mostly flat with strategic atmospheric depth.

| Level | Treatment | Use |
|---|---|---|
| 0 (flat) | no shadow; hairline border | default cards, table rows, form inputs |
| 1 (subtle) | `rgba(0,0,0,0.04) 0px 1px 2px 0px` | hover-elevated tiles, subtle highlights |
| 2 (card) | `rgba(0,0,0,0.08) 0px 4px 12px 0px` | standard feature cards |
| 3 (mockup) | `rgba(0,0,0,0.12) 0px 24px 48px -8px` | hero product-mockup framing |
| 4 (brand-tinted) | `rgba(0,212,164,0.08) 0px 8px 24px` | featured pricing-tier glow |

The homepage hero leans on an atmospheric photographic backdrop (cloud
illustration on the sky gradient) for depth rather than shadow; the
startups hero uses a similar rocket-launch illustration cutting across the
dark teal gradient. Code blocks get their own internal depth from
syntax-highlighting color hierarchy — no shadow needed there either.

## Shapes

| Token | Value | Use |
|---|---|---|
| `rounded.xs` | 4px | inline code chips, micro tags |
| `rounded.sm` | 6px | sidebar nav items, type badges |
| `rounded.md` | 8px | inputs, search pill, code blocks, secondary cards |
| `rounded.lg` | 12px | standard cards, pricing tiers, hero mockup, FAQ items |
| `rounded.xl` | 16px | larger feature panels |
| `rounded.xxl` | 24px | featured product showcase tiles |
| `rounded.full` | 9999px | all buttons, pill tabs, badges |

The scale is disciplined — the brand never softens a corner between 8px and
12px for the same component family; every button and pill uses the full
radius, and rectangular cards consistently use 12px.

## Components

Definitions live in `design-tokens.yaml → components`. Summary (default and
pressed/active states only — hover states are not documented):

- **Buttons** — `button-primary` (black pill, dominant CTA, pressed →
  charcoal, disabled → hairline/muted), `button-accent-green` (mint pill
  for brand-emphasis CTAs), `button-on-dark` (white pill for dark hero
  bands), `button-secondary` (outlined pill), `button-ghost` (quiet
  rectangular tertiary), `button-link` (inline text), `button-icon-circular`
  (32px circular utility button).
- **Cards** — `card-base`/`card-feature`/`card-help`/`card-startup-perk`
  for general content; `pricing-card` and `pricing-card-featured` (2px mint
  border + brand-tinted shadow) for pricing tiers; `testimonial-card-feature`
  and `founder-quote-card` on the orange surface; `testimonial-card-quote`
  as the quieter white variant.
- **Inputs** — `text-input`/`text-input-focused` (focus ring flips to mint),
  `search-pill` for the docs top-bar search.
- **Tabs** — `segmented-tab`/`segmented-tab-active` (underline style inside
  the docs Tabs component) and `pill-tab`/`pill-tab-active` (top of pricing
  page), plus `toggle-monthly-yearly`.
- **Badges** — `badge-discount` (green), `badge-required` (red), `badge-type`
  (gray type-signature chip), `badge-tag` (blue tag chip).
- **Code** — `code-block`, `code-block-header`, `code-inline`,
  `copy-code-button`.
- **Documentation components** — `property-row`, `feature-comparison-table`/
  `feature-comparison-row`, `sidebar-nav-item`/`-active`,
  `sidebar-section-header`, `doc-toc-item`/`-active`.
- **Signature components** — `hero-band-sky`, `hero-band-dark`,
  `hero-product-mockup` (deep diffuse shadow), `logo-wall-item`,
  `faq-accordion-item`, `footer-region`/`footer-link`.

### Navigation
Marketing top nav is a sticky white bar (~64px) with the Mintlify wordmark,
a horizontal link list (Solutions, Pricing, Customers, Documentation,
Changelog), and right-side "Talk to sales" + black-pill "Get Started".
Documentation top nav compresses to ~56px with a center search-pill and
right-side account/upgrade CTAs.

## Do's and don'ts

**Do**
- Reserve `brand-green` for accent CTAs and active-state indicators only —
  even one accent button per viewport carries weight.
- Use `colors.primary` (black) as the dominant CTA on light backgrounds;
  switch to the white on-dark pill on dark hero bands.
- Apply `rounded.full` to every button and pill; never soften pill corners.
- Pair Inter (UI prose) with Geist Mono (code) — never introduce a third
  typeface.
- Use atmospheric gradient heroes sparingly (homepage and startups page
  only); keep deeper surfaces flat and dense.
- Apply `rounded.lg` (12px) consistently on cards; reserve `rounded.md`
  (8px) for compact UI like search pills and code blocks.
- Keep documentation prose at 16px with 1.50 line-height — never compress.

**Don't**
- Don't use `brand-green` on body text or large surfaces — it loses signal.
- Don't introduce accent colors beyond mint, tag-blue, error-red, and the
  testimonial orange.
- Don't apply heavy shadows on flat documentation cards; reserve elevation
  for the hero product mockup.
- Don't reduce documentation line-height below 1.50.
- Don't combine atmospheric gradients with multiple competing accents in
  the same hero.
- Don't use Inter for code or Geist Mono for prose — the typeface
  assignment IS the brand voice.

## Responsive behavior

### Breakpoints
| Name | Width | Key changes |
|---|---|---|
| Mobile (small) | <480px | single column; hero scales to 36px; pill nav collapses to hamburger; pricing stacks 1-up; footer becomes 1-column accordion |
| Mobile (large) | 480–767px | feature tiles 2-up; hero scales to 44px |
| Tablet | 768–1023px | 2-column feature grids; pill-tab nav returns; docs sidebar collapses to a drawer; hero scales to 56px |
| Desktop | 1024–1279px | full 3-column docs grid; 3-tier pricing row; hero at 72px |
| Wide Desktop | ≥1280px | wider hero gutters, larger product mockup, fixed 240px sidebar |

### Touch targets
Pill buttons render at 36–40px effective height, bumping to 44px on mobile
via padding overrides. Circular icon buttons go from 32×32px desktop to
44×44px mobile. Form inputs render at 40px, bumping to 44px on mobile.

### Collapsing strategy
The promo banner stays full-width and truncates below 480px. The top nav
collapses to a hamburger below 1024px. The 2-column hero collapses to
stacked below 1024px with the mockup moving below the text. The docs grid
goes 3-column → sidebar-drawer (<1024px) → single column (<768px). Pricing
comparison goes 3-column → 1-column stacked (<768px) with the comparison
table becoming horizontal-scroll. The hero display type steps 72px → 56px
→ 44px → 36px across breakpoints, and the footer goes 5-column → 2-column →
accordion.

## Known gaps

- Dark-mode token values for canvas, surface, ink, and hairline are not
  surfaced on the captured pages — no published dark-mode palette exists
  yet.
- Animation/transition timings are not extracted; 150–200ms ease is a
  reasonable default for hover/focus transitions.
- Form-validation success states beyond the default pattern are not
  captured.
- The full code-syntax-highlighting palette inside docs isn't formalized —
  only a handful of annotation tokens (`brand-tag`, `brand-annotate`,
  `brand-warn`) are enumerated.
