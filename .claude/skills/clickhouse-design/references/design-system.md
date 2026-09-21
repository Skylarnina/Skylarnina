# ClickHouse Design System — Full Analysis

Adapted from the ClickHouse design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/clickhouse/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

ClickHouse runs the highest-contrast marketing surface in the database /
data-platform category. The canvas is near-pure black
(`colors.canvas`, `#0a0a0a`) and the single brand voltage is **electric
yellow** (`colors.primary`, `#faff69`) — carrying every primary CTA, every
stat-callout number, every "GET STARTED" badge. The yellow is used sparingly
element by element but generously at the band level via full-bleed yellow
CTA cards.

The black-and-yellow pairing is the brand's fingerprint: where Snowflake
leans on cool blue gradients and Databricks pairs red with slate,
ClickHouse commits to one electric yellow doing all of the color work.
Real SQL, terminal output, and product-UI fragments sit directly in dark
`surface-card` (`#1a1a1a`) panels across the site.

Type is entirely **Inter**, scaled and weighted for hierarchy rather than
mixed with a second family: 700 for display headlines with -1px to -2.5px
tracking, 600 for sub-titles and buttons, 400 for body. JetBrains Mono
handles code.

**Key characteristics:**
- Near-pure black canvas with white type; there is no light-mode marketing
  surface.
- Electric yellow primary reserved for CTAs, large stat numbers ("2.8k+",
  "74k+"), and full-bleed yellow CTA bands.
- Inter 700/600/400 with no serif or second display voice.
- Dark surface cards barely lighter than canvas — a subtle, engineering-grade
  contrast rather than a loud color block.
- Code renders in JetBrains Mono inside `surface-card`, syntax-highlighted
  in muted blue/yellow/gray.
- Huge yellow sans-700 stat numbers carry the credibility moment (star
  counts, contributor counts, benchmark figures).
- Hierarchical radii: 8px buttons, 12px cards, pill reserved for tag
  badges only.
- 96px section rhythm.

## Colors

### Brand & accent
- **Primary (electric yellow)** — the signature color: CTA fills, stat
  numbers, full-bleed yellow bands. This yellow IS the brand.
- **Primary active** — a darker press/hover variant.
- **Primary disabled** — a desaturated dark-yellow tone for disabled
  states on dark canvas.

### Surface
- **Canvas** — the near-black page floor.
- **Surface soft** — section dividers, very soft band tints.
- **Surface card** — feature cards, code windows, product mockups,
  pricing-tier cards.
- **Surface elevated** — nested cards inside larger dark cards.
- **Surface yellow band** — the CTA-card/band fill; same hex as primary.
- **Hairline / hairline strong** — two tiers of 1px card borders and
  emphasis dividers.

### Text
- **On dark (ink)** — all headline and primary text.
- **Body / body strong** — default and emphasized running text.
- **Muted / muted soft** — footer links, captions, and fine print.
- **On primary / on yellow** — near-black text over yellow CTAs and bands;
  this high-contrast pairing IS the action signal.

### Semantic / accent
- **Accent emerald** — success/active status indicators in product UI.
- **Accent rose** — error/"down" indicators.
- **Accent blue** — info states and code-syntax highlighting.

## Typography

### Font family
Inter carries every role — display, body, navigation, buttons, captions —
with JetBrains Mono handling code. The single-family approach is
deliberate: three weights (700/600/400) cover the entire hierarchy without
needing a serif counter-voice, and Inter's geometric humanist character at
confident bold weight reads as precise and engineered, matching the
database's performance-first positioning.

### Hierarchy
See `design-tokens.yaml → typography` for the complete scale — `display-xl`
(72px/700/-2.5px) down through `nav-link` (14px/500). Display weights hold
at 700 across every size; negative letter-spacing (-1px to -2.5px) is what
keeps Inter-700 from reading as wide, generic marketing type — the tighter
tracking is what gives ClickHouse its engineered feel. Body and labels stay
at 400/500/600; hierarchy comes from size and weight rather than family
contrast.

### Note on font substitutes
Inter is open-source and used directly — no substitution needed. Söhne or
Geist are close commercial alternatives if a licensed look is preferred.

## Layout

- Base spacing unit: 4px; full ladder in `design-tokens.yaml → spacing`.
- Section padding: 96px between major bands.
- Card interior padding: 32px for feature cards and pricing tiers, 24px
  for code-window and event cards.
- Max content width ~1280px; hero often splits 7/5 (headline left, code
  mockup right).
- Feature-card grids: 3-up desktop → 2-up tablet → 1-up mobile; pricing
  grids run 3–4-up down to 1-up.
- The pacing reads dense and slightly compressed compared to a typical
  marketing site — generous enough to read editorially, tight enough to
  feel engineering-grade rather than soft.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| Flat | No shadow, no border | Body sections, top nav, hero |
| Soft hairline | 1px `hairline` border | Code-window cards, content cards |
| Surface card | `surface-card` fill, no shadow | Feature cards, pricing tiers, events |
| Yellow band | `primary` fill, no shadow | Full-bleed yellow CTA cards/bands |

There are no drop shadows anywhere. Depth comes from the (subtle) contrast
between black canvas and the barely-lighter `surface-card` tone — closer to
an engineering-grade dim panel than an elevated Material card. Code-window
cards add their own internal chrome (line numbers, syntax highlighting,
status bars) for visual density instead of external shadow, and the
yellow-on-black contrast does most of the elevation work for CTAs.

## Shapes

| Token | Value | Use |
|---|---|---|
| `rounded.xs` | 4px | Reserved for badge accents |
| `rounded.sm` | 6px | Small inline buttons |
| `rounded.md` | 8px | Standard CTA buttons, text inputs |
| `rounded.lg` | 12px | Content cards, code-window cards, pricing tiers |
| `rounded.pill` | 9999px | Badge pills |
| `rounded.full` | 9999px / 50% | Avatars, icon buttons |

## Components

Definitions live in `design-tokens.yaml → components`. Summary:
- **Top nav** — 64px black bar; wordmark left, primary menu, Sign in +
  yellow "Get Started" CTA right.
- **Buttons** — primary (yellow fill, black text — the iconic pairing),
  secondary (dark surface-card fill), text link (yellow underline), and a
  36px circular icon button.
- **Hero band** — black canvas, 7/5 split with a code-window or product
  mockup on the right.
- **Hero stat card** — no card surface at all, just huge yellow
  `stat-display` numbers directly on canvas ("779+", "47k+").
- **Feature card (yellow / dark)** — the yellow variant is full-bleed
  emphasis; the dark variant is the default.
- **Code window card** — dark card with a SQL block in JetBrains Mono,
  often the hero's right-side artifact on developer pages.
- **Product mockup card** — same shape as the dark feature card but with
  embedded product chrome (query editor, monitoring panel).
- **Pricing tier card / featured** — the featured tier flips to yellow
  fill; the color IS the featured signal.
- **Stat callout** — inline yellow numbers, transparent background, used
  as a flat layout block rather than a card.
- **Events card** — dark card with title, uppercase date, location, and
  a Register CTA.
- **Customer logo strip** — horizontal monochrome logos on black canvas.
- **Text input / focused** — dark fill, border thickens to yellow on
  focus.
- **Category tab / active** — dark tab navigation, transparent inactive
  state.
- **Badge pill / badge yellow** — small dark pill vs. yellow "NEW"/"GET
  STARTED" pill.
- **CTA band (yellow)** — pre-footer full-yellow band with a black
  button.
- **Footer** — black, 4-column link list, wordmark at top.

## Do's and don'ts

**Do**
- Anchor every page on the black canvas — the yellow-black pairing is the
  brand voltage.
- Reserve yellow for primary CTAs, stat-callout numbers, and full-bleed
  CTA bands.
- Set every display headline at Inter 700 with -1px to -2.5px tracking.
- Show actual SQL code blocks — ClickHouse is a database; show the query,
  not an illustration of one.
- Use yellow stat-callout numbers to establish credibility.
- Hold the 96px section rhythm.

**Don't**
- Don't introduce a second brand color — ClickHouse is monochrome plus
  yellow.
- Don't push display weight beyond 700 or drop to 500 — the hierarchy is
  built on size, not weight gradation.
- Don't use yellow for body text or casual surface fills.
- Don't use rounded/pill buttons outside small badges — the standard
  button radius is 8px.
- Don't repeat the same surface mode in two consecutive bands.
- Don't replace SQL mockups with abstract illustration.
- Don't invent hover styling beyond what the tokens encode.

## Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Mobile | < 768px | Hamburger nav; hero h1 72→36px; code-window card stacks below; feature/pricing grids collapse to 1-up |
| Tablet | 768–1024px | Nav tightens; feature cards 2-up; pricing 2-up |
| Desktop | 1024–1440px | Full nav; 3-up feature cards; 3–4-up pricing |
| Wide | > 1440px | Same as desktop with more room; content caps at 1280px |

Touch targets: primary CTA at minimum 40×40px; the 36px circular icon
button sits slightly under WCAG 44px but reads as visually centered; text
inputs are 40px tall. Nav collapses to hamburger below 768px; hero grid
drops to single column; code blocks keep their font size and scroll
horizontally on mobile rather than wrapping; pricing tiers collapse
4 → 2 → 1 with the yellow featured tier staying visually distinct;
customer logos wrap on mobile.

## Known gaps

- The exact yellow hex (`#faff69`) was sampled from a screenshot; the
  official brand value may differ slightly.
- Inter weight-axis values beyond 400/500/600/700 aren't formalized — only
  the observed static weights are documented.
- Animation/transition timing (code typewriter effects, stat counters) is
  out of scope.
- Form validation states beyond the focused text input aren't captured.
- The logged-in ClickHouse Cloud product surface (query console,
  dashboards, table browser) shares some tokens but adds many
  product-specific components not covered here.
- The customer logo strip's exact opacity/treatment is approximate.
