# Airtable Design System — Full Analysis

Adapted from the Airtable design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/airtable/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Airtable's marketing pages read as quietly editorial. The default atmosphere
is white canvas, dark ink type, generous whitespace, and a near-black pill
CTA — nothing competes for attention until a section deliberately calls for
it. Rather than a gradient wash or a single accent color, brand voltage
arrives through **full-bleed signature cards** in `{colors.signature-coral}`,
`{colors.signature-forest}`, and `{colors.surface-dark}` that break up the
page every two or three screens. Between those bands the layout reads like a
print magazine: headline, supporting copy, a small image cluster, then room
to breathe.

Type runs Haas Grotesk at modest weights — 400 for display, 500 for
sub-titles and buttons. Headlines are never bolder than 500; emphasis comes
from size and color contrast instead. Body copy holds at 14px/400
everywhere. The pricing page runs its own dialect entirely: Inter Display at
unusual mid-weights (475/575) paired with pill-shaped buttons that appear
nowhere else — a deliberate signal that this page is about commercial
precision, not editorial storytelling.

**Key characteristics:**
- Primary CTA is `{colors.primary}` (near-black) with white text and a 12px
  corner — confident and final, never decorative.
- Secondary CTA is a white button with hairline outline and ink text; the
  pair forms Airtable's signature button combination.
- The hero sits on plain white canvas — no gradient, mesh, or background
  flourish; type and whitespace alone carry it.
- Brand voltage lives in full-bleed signature cards (coral, forest, dark
  navy) placed every few screens.
- Demo-card grids carry product-UI fragments on warm pastel surfaces
  (peach, mint, cream, and others).
- Section rhythm cycles: white → coral card → white → cream callout → dark
  navy CTA → light gray CTA banner → footer, resetting to canvas between
  every signature surface.
- Radius is hierarchical — 12px for primary CTAs and large signature cards,
  10px for content cards and demo grids, 6px for inputs, full-circle for
  icon buttons; pricing buttons alone jump to pill radius to mark themselves
  as a separate dialect.
- Vertical rhythm holds at 96px between major bands on every page.

## Colors

### Brand & Accent
- **Primary** (`{colors.primary}` #181d26) — the dominant brand color: the
  primary CTA fill, h1/h2 display type, and the dark surface band. Black is
  the primary throughout, not a secondary next to blue.
- **Primary Active** (`{colors.primary-active}` #0d1218) — the press state.

### Surface
- **Canvas** (`{colors.canvas}` #ffffff) — the floor of every editorial body.
- **Surface Soft** (`{colors.surface-soft}` #f8fafc) — tabbed feature cards
  and the featured pricing tier.
- **Surface Strong** (`{colors.surface-strong}` #e0e2e6) — the light-gray
  "Start building" CTA banner near the footer.
- **Surface Dark** (`{colors.surface-dark}` #181d26) — dark navy CTA cards
  mid-page.
- **Surface Dark Elevated** (`{colors.surface-dark-elevated}` #1d1f25) —
  the articles-page hero base behind a rainbow-stripe overlay.
- **Hairline** (`{colors.hairline}` #dddddd) — input outlines, table
  dividers, secondary-button outlines.

### Text
- **Ink** (`{colors.ink}` #181d26) — h1/h2 display type and primary-button
  text-on-light; shares its hex with `{colors.primary}` because it's the
  same role at different layers.
- **Body** (`{colors.body}` #333840) — default running text.
- **Muted** (`{colors.muted}` #41454d) — footer links, breadcrumbs,
  captions.
- **Border Strong** (`{colors.border-strong}` #9297a0) — outline color on
  disabled secondary buttons.
- **On Primary / On Dark** (`{colors.on-primary}` #ffffff) — text on primary
  buttons and dark surfaces.

### Signature Card Surfaces
These carry Airtable's brand voltage — always full-bleed, never a small
accent:
- **Coral** (`{colors.signature-coral}` #aa2d00) — the homepage's largest
  signature card ("Production apps in prototype speed"), full-bleed dark
  coral with white type.
- **Forest** (`{colors.signature-forest}` #0a2e0e) — a deep-green card in
  the homepage demo-grid cluster.
- **Cream** (`{colors.signature-cream}` #f5e9d4) — a soft beige callout band
  holding dark type and product-UI fragments.
- **Peach / Mint / Yellow / Mustard** (`{colors.signature-peach}` #fcab79,
  `{colors.signature-mint}` #a8d8c4, `{colors.signature-yellow}` #f4d35e,
  `{colors.signature-mustard}` #d9a441) — demo-card surfaces carrying small
  product-UI fragments inside the multi-card grid sections.

### Semantic
- **Link** (`{colors.link}` #1b61c9, active #1a3866) — inline body links and
  anchor text only. Despite its CSS-variable name resembling a "primary
  button" token, this color is never the button fill.
- **Info** (`{colors.info}` #254fad) / **Info Border** (`{colors.info-border}`
  #458fff) — inline info badges, focused-input outline.
- **Success** (`{colors.success}` #006400) / **Success Border**
  (`{colors.success-border}` #39bf45) — confirmation states.

## Typography

### Font Family
The system runs **Haas / Haas Groot Disp** — Groot Disp for h1/h2, Haas
Grotesk for everything 24px and below. The pricing surface switches to a
separate **Inter Display** stack at mid-weights (475/575), signaling
commercial precision.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale (display-xl 48px
down to the 13.12px legal size, plus the pricing-only sizes). Notable roles:
- `{typography.display-lg}` (40px/400) is the homepage h1.
- `{typography.legal}` (13.12px/600) is the one place true bold (600)
  appears — reserved for cookie/legal CTAs, not marketing copy.
- `{typography.pricing-display}` (44.8px/475) is the pricing-page h1 in
  Inter Display.

### Principles
Haas prefers weight 400 for display sizes — a 40px h1 is not bold. Emphasis
comes from size, color contrast, and the signature cards rather than
typographic weight. Where weight does step up, it goes to 500 (sub-titles,
buttons, article titles), never 600/700 in the editorial body. The pricing
sub-system's `font-weight: 475` is a custom mid-weight shipped as a variable
font, distinguishing that page from the rest of the site.

### Note on Font Substitutes
If Haas Groot Disp/Haas Grotesk are unavailable, **Inter Display** (variable)
is the closest open-source substitute for both — tighten line-height by
about 5% to match Haas's cap height. Use Inter Display directly for the
pricing sub-system. On Windows, the fallback chain lands on Segoe UI, a
usable but slightly cooler substitute.

## Layout

### Spacing System
- Base unit: 4px, all spacing snaps to 4-multiples.
- Tokens: `{spacing.xxs}` 4px · `{spacing.xs}` 8px · `{spacing.sm}` 12px ·
  `{spacing.md}` 16px · `{spacing.lg}` 24px · `{spacing.xl}` 32px ·
  `{spacing.xxl}` 48px · `{spacing.section}` 96px.
- Section padding: 96px is the universal vertical rhythm — every major
  editorial band on every page uses it top and bottom.
- Card padding: 32px for tabbed feature and pricing cards, 48px inside
  signature coral/forest/dark cards, 24px for cream callouts and demo-grid
  cards.
- Gutters: 24px between cards in 3-up grids, 16px inside denser logo strips
  and footer columns.

### Grid & Container
- Max content width: ~1280px centered, with 48px horizontal breathing room.
- Editorial body: single 8/12-column grid, collapsing to one column on
  mobile.
- Demo-card grids: 3–4 columns at desktop, deliberately uneven card heights
  within a grid to avoid a "spec sheet" feel.
- Logo strip: 6 monochrome partner logos in a row, wrapping to 3-up on
  mobile.

### Whitespace Philosophy
Whitespace is the dominant atmospheric tool. Heroes sit in 96px+ of pure
whitespace above and below the headline pair, with no decoration filling
that space — no gradient, no aurora, no atmospheric mesh. The system trusts
whitespace alone to frame the content.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat | No shadow, no border | Body sections, top nav, footer |
| Soft hairline | 1px hairline border | Inputs, sub-nav rails, comparison-table dividers, secondary buttons |
| Button rest | Faint blue-tinted glow at low alpha | Primary CTA buttons (a holdover tint from the link color) |
| Button focus | 2px blue outer ring at higher alpha | Keyboard focus on primary buttons |
| Card flat | No shadow | Signature and demo-grid cards rely on color contrast, not shadow |

The philosophy is color-block first, shadow second — there is no
soft-glow, atmospheric-shadow, or heavy-elevation language anywhere in the
marketing system. A single-page exception is the articles hero's vertical
rainbow stripe treatment on `{colors.surface-dark-elevated}` — a one-off,
not a system-wide pattern. The demo-card grid instead gets its depth from
real product-UI screenshots inside each card.

## Shapes

| Token | Value | Use |
|---|---|---|
| `{rounded.xs}` | 2px | Cookie-consent and legal CTA buttons |
| `{rounded.sm}` | 6px | Text inputs, small inline buttons |
| `{rounded.md}` | 10px | Secondary content cards, article cards, cream callouts |
| `{rounded.lg}` | 12px | Primary CTA buttons, signature surface cards, tabbed feature cards |
| `{rounded.pill}` | 9999px | Pricing-page CTA buttons only (sub-system signal) |
| `{rounded.full}` | 9999px / 50% | Circular icon buttons, avatars |

Product-UI screenshots inside demo cards keep native aspect ratios (4:3 or
16:10) and crop into 10px-radius containers. Hero illustrations bleed full
width with no rounding. Article-card thumbnails use 16:9 with 10px corners;
testimonial avatars use full circles; pricing comparison images stay
rectangular.

## Components

> No hover states are documented — the source follows a no-hover policy,
> specifying only Default and Active/Pressed states.

- **`top-nav`** — 64px white bar; wordmark left, primary menu center-left,
  "Book Demo" outline + "Sign up for free" primary + "Log In" text-link
  right. The nav never inverts to dark.
- **`button-primary`** — near-black fill, white text, 16×24px padding, 12px
  radius; the "Get started/Sign up for free" CTA, used sparingly (one per
  viewport). Active state darkens to `{colors.primary-active}`.
- **`button-secondary`** — white with hairline outline; the natural pairing
  with primary.
- **`button-secondary-on-dark`** — same white shape used over dark/coral
  signature surfaces; the system never inverts to a translucent style.
- **`button-pricing-pill`** — pill-radius, the only pill in the marketing
  system; part of the pricing sub-system's separate signaling.
- **`button-legal`** — cookie/legal CTA in link-blue, 2px radius, 600
  weight — a "required system surface" cue, not a designed brand moment.
- **`hero-band`** — full-width white hero: headline, sub-headline, primary +
  secondary CTA pair in 96px of whitespace, no card or gradient.
- **`signature-coral-card`** / **`signature-forest-card`** / `hero-card-dark`
  — full-bleed 12px-radius cards in coral, forest, or dark navy, 48px
  padding, carrying an h2, supporting copy, and a light-on-dark button.
- **`feature-card-tabbed`** — light-cream card with a vertical tab rail on
  the left and content pane on the right.
- **`cream-callout-card`** — beige, 10px radius, 24px padding, carrying
  product-UI fragments or stat callouts.
- **`demo-grid-card`** — 10px radius, 16px padding, varying heights,
  framing a single product-UI fragment per card.
- **`logo-strip`** — monochrome partner-logo row on canvas, 32px vertical
  padding.
- **`article-card`** — 16:9 illustrated thumbnail, category tag, title, and
  meta line in the articles grid.
- **`topic-filter-rail`** — 240px-wide left rail with grouped category
  headings and sub-bullets.
- **`text-input`** / **`text-input-focus`** — white, 6px radius, 44px tall,
  hairline border that recolors to the info-border blue on focus.
- **`pricing-tier-card`** / **`pricing-tier-card-featured`** — 10px radius,
  32px padding; the featured tier's only signal is a background shift to
  `{colors.surface-soft}` — no accent border, no badge.
- **`pricing-comparison-row`** — 12px vertical padding, hairline divider
  between rows.
- **`footer`** — light, 6-column link list, 96px padding split between the
  link block and legal row.
- **`cta-band-light`** — light-gray "Start building" strip, 12px radius,
  48px padding, headline plus primary CTA.

## Do's and Don'ts

### Do
- Keep the primary CTA near-black — mixing it up with the link blue turns a
  confident hero into a confused one.
- Reserve the primary CTA for one action per viewport.
- Pair the primary CTA with the white/hairline secondary button — together
  they're Airtable's signature row.
- Trust whitespace as the hero's only atmosphere; no gradient or mesh.
- Use the coral/forest/dark signature cards to break editorial monotony —
  they're the brand's voltage moments.
- Keep demo-grid card heights uneven within a grid.
- Treat the pricing surface as its own dialect — keep Inter Display and the
  pill button together, never mixed with Haas Grotesk button type.
- Anchor every editorial band with 96px vertical padding.

### Don't
- Don't make the link blue (#1b61c9) the primary button color — that's the
  most common misread of Airtable's CSS variables.
- Don't add a gradient backdrop to the hero.
- Don't bold display-weight type — 700 reads as generic marketing template.
- Don't use pill radius outside the pricing surface.
- Don't repeat the same surface mode in two consecutive bands — the pacing
  depends on white → signature → white → cream → dark rotation.
- Don't add hover styling beyond Default and Active/Pressed.
- Don't introduce accent colors beyond the documented signature palette.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 768px | Single column; nav collapses to hamburger; demo-grid 1-up; signature cards stay full-bleed; logo strip wraps to 2 rows; footer collapses to one column. |
| Tablet | 768–1024px | 2-up demo grid; nav tightens but stays horizontal; cream callouts stack 2-up; pricing comparison table becomes horizontally scrollable. |
| Desktop | 1024–1440px | 3–4-up demo grid; full nav; pricing tiers render 4-across. |
| Wide | > 1440px | Same as desktop with more outer breathing room; max content width caps around 1280px. |

### Touch Targets
- Primary CTAs render ≥48×48px — comfortably above WCAG AAA.
- Icon-circular buttons are 40×40px — slightly under the 44px recommendation
  but visually compensated by the centered icon.
- Text inputs are 44px tall.

### Collapsing Strategy
- Nav collapses to a full-screen hamburger sheet below 768px.
- Card grids reduce columns rather than scaling cards down.
- The tabbed feature card re-stacks its tab rail above the content on
  mobile.
- The pricing comparison table becomes horizontally swipeable below
  1024px while headers stay pinned.

## Known Gaps

- Exact hex values for pastel demo-grid surfaces are inferred from
  screenshot pixel sampling and may shift with seasonal launches.
- Hover behavior across components is undocumented (no-hover policy).
- Animation and transition timings are out of scope.
- Form validation states beyond focus are not extracted.
- The pricing comparison table's checkmark glyph and column-divider widths
  are described structurally but not formalized as tokens.
- A CSS variable named `--theme_button-background-primary` maps to
  `{colors.link}` rather than the actual primary button color — a naming
  trap worth remembering if re-deriving tokens from Airtable's own CSS.
