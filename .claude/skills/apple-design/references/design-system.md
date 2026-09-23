# Apple Design System — Full Analysis

Adapted from the Apple design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/apple/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Apple's web presence turns product photography into a museum installation
framed by near-invisible UI. Each page stacks edge-to-edge product "tiles" —
alternating light and dark canvases, each centered on a headline, a one-line
tagline, two small blue pill CTAs, and an impossibly crisp product render.
Nothing competes with the product itself: typography stays confident but
quiet, color is either pure white, off-white parchment, or a near-black
tile, and interactive elements come in a single quiet blue.

Density is unusually low even for premium marketing sites — each tile
occupies roughly one viewport, and there's no decorative chrome: no borders,
gradients, decorative frames, or shadows on headlines. Elevation only shows
up when a product image rests on a surface, using a single soft drop-shadow
for visual weight. The overall effect is closer to a gallery wall
disappearing so the artifact can take over.

Store and configurator surfaces keep the same chassis but shift mode: a
tight grid of white utility cards at 18px radius with thin borders, paired
with a persistent thin sub-nav strip. The environment (sustainability) page
leans darker and more editorial. Across every surface the typographic
system, spacing rhythm, and single blue accent stay consistent — it's one
language expressed at different volumes.

**Key characteristics:**
- Photography-first presentation; UI recedes so the product can speak.
- Alternating full-bleed tiles (white/parchment vs. near-black) where the
  color change itself acts as the section divider.
- A single blue accent (`{colors.primary}` #0066cc) carries every
  interactive element — there is no second brand color.
- Two button grammars: tiny blue pill CTAs and compact utility rectangles.
- SF Pro Display + SF Pro Text with negative letter-spacing at display
  sizes for the signature "Apple tight" headline feel.
- Whisper-soft elevation used only when a product image needs to breathe —
  exactly one drop-shadow exists in the entire system.
- A tight two-row nav: a slim global nav plus a product-specific frosted
  sub-nav with a persistent right-aligned primary CTA.
- Predictable section pulse: light hero → dark product tile → light utility
  tile → dark tile → parchment footer.

## Colors

> Source pages analyzed: homepage, environment, store, iPhone 17 Pro buy
> page, accessories index — the color system is identical across all five;
> only the surface-mode mix differs.

### Brand & Accent
- **Action Blue** (`{colors.primary}` #0066cc) — the single brand-level
  interactive color: all text links, blue pill CTAs ("Learn more", "Buy"),
  and the focus-ring root. Press state shifts via a scale transform rather
  than a hex change.
- **Focus Blue** (`{colors.primary-focus}` #0071e3) — a marginally brighter
  sibling reserved for the keyboard focus ring (`outline: 2px solid`).
- **Sky Link Blue** (`{colors.primary-on-dark}` #2997ff) — a brighter blue
  used for in-copy links and callouts on dark surfaces, where Action Blue
  would disappear against the tile background.

### Surface
- **Pure White** (`{colors.canvas}` #ffffff) — the dominant canvas for
  content, utility cards, store tiles, configurator grids.
- **Parchment** (`{colors.canvas-parchment}` #f5f5f7) — the signature
  Apple off-white: alternating light tiles, footer region, default canvas
  in store utility sections. Just different enough from white to create
  rhythm.
- **Pearl Button** (`{colors.surface-pearl}` #fafafc) — a near-white fill
  for secondary "ghost" buttons, lighter than parchment so the button still
  reads against it.
- **Near-Black Tile 1/2/3** (`{colors.surface-tile-1}` #272729,
  `{colors.surface-tile-2}` #2a2a2c, `{colors.surface-tile-3}` #252527) —
  three micro-stepped dark surfaces used to separate adjacent dark tiles and
  embedded video frames.
- **Pure Black** (`{colors.surface-black}` #000000) — reserved for true
  void: video player backgrounds, photographic overlays, the global nav bar.
- **Translucent Chip Gray** (`{colors.surface-chip-translucent}` #d2d2d7) —
  the base hex of the translucent gray chip used at ~64% alpha over
  photography for circular controls.

### Text
- **Near-Black Ink / Body** (`{colors.ink}` / `{colors.body}` #1d1d1f) — the
  voice of every headline, paragraph, and the dark utility button's fill.
  Chosen instead of pure black to keep the page feeling photographic rather
  than printed.
- **Body On Dark** (`{colors.body-on-dark}` #ffffff) — all text on dark
  tiles and the global nav bar.
- **Body Muted** (`{colors.body-muted}` #cccccc) — secondary copy on dark
  tiles where pure white would be too loud.
- **Ink Muted 80** (`{colors.ink-muted-80}` #333333) — body text on the
  Pearl Button surface.
- **Ink Muted 48** (`{colors.ink-muted-48}` #7a7a7a) — disabled button text
  and legal fine-print.

### Hairlines & Borders
- **Divider Soft** (`{colors.divider-soft}` #f0f0f0) — functions as a ring
  shadow rather than a hard line on secondary buttons.
- **Hairline** (`{colors.hairline}` #e0e0e0) — the 1px border on store
  utility cards and configurator chips.

### Brand Gradient
There are no decorative gradients anywhere. Atmospheric depth on product
photography is inherent to the imagery itself, not a CSS overlay — Apple is
the rare premium brand with zero gradient-based design tokens.

## Typography

### Font Family
- **Display**: `SF Pro Display` — Apple's proprietary display face,
  optimized for sizes ≥19px, carrying every headline.
- **Body/UI**: `SF Pro Text` — the text-optimized cut for body copy,
  captions, buttons, and links below 20px.
- `font-variant-numeric: numerator` is enabled on numeric links (pricing,
  spec sheets); display sizes rely on tight tracking rather than
  contextual ligatures.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale (hero-display 56px
down to the 10px micro-legal size). Notable roles:
- `{typography.hero-display}` (56px/600/-0.28px) is the signature "Apple
  tight" hero headline.
- `{typography.lead-airy}` (24px/300) and `{typography.button-large}`
  (18px/300) are the system's rare, deliberate weight-300 moments — an
  airy cue for a handful of large reads.
- `{typography.dense-link}` (17px/2.41 line-height) is the footer/store
  link-list treatment — the unusually relaxed leading is how dense link
  columns stay scannable.

### Principles
- **Negative letter-spacing at display sizes.** Every headline at 17px and
  up carries a slight tighten (-0.12 to -0.374px) — the iconic "Apple
  tight" cadence, never used at 12px or below.
- **Body copy runs at 17px, not 16px** — breaking the typical convention
  gives the page an unmistakable "reading, not scanning" pace.
- **Weight 300 is real and rare**, reserved for a handful of large-size
  reads as a deliberate light-atmosphere cue.
- **Weight 600, not 700, for headlines** — 700 shows up sparingly only on
  the 21px tagline role when a touch more assertion is needed.
- **Weight 500 is deliberately absent** from the ladder (300/400/600/700).
- **Line-height is context-specific**: tight (1.07–1.19) at display sizes,
  1.47 for body, and a relaxed 2.41 for dense footer/store link stacks.

### Note on Font Substitutes
SF Pro is proprietary. Use `system-ui, -apple-system, BlinkMacSystemFont`
first so macOS/iOS/Safari resolve to the real SF Pro. For non-Apple
platforms, **Inter** (variable) at weight 600 with
`font-feature-settings: "ss03"` is the closest open-source approximation of
SF Pro's rounded "a". Nudge letter-spacing down by `-0.01em` on display
sizes and tighten body line-height from 1.47 to about 1.44 — Inter's taller
x-height needs less leading.

## Layout

### Spacing System
- Base unit: 8px, with sub-base values (2/4/5/6/7px) for tight typographic
  adjustments.
- Tokens: `{spacing.xxs}` 4px · `{spacing.xs}` 8px · `{spacing.sm}` 12px ·
  `{spacing.md}` 17px · `{spacing.lg}` 24px · `{spacing.xl}` 32px ·
  `{spacing.xxl}` 48px · `{spacing.section}` 80px.
- Section vertical padding: 80px inside a product tile; tiles stack
  edge-to-edge with 0 gap — the color change alone provides the break.
- Card padding: 24px inside utility grid cards.
- Button padding: 8–11px vertical, 15–22px horizontal.

### Grid & Container
- Max content width: ~980px on text-heavy sections, ~1440px on product
  grids, full-bleed for product tile heroes.
- Column patterns: 3–5 column utility grid on store/accessories, 2-column
  side-by-side occasionally on the homepage, single-column centered stacks
  on product tile heroes.
- Gutters: 20–24px between cards in a utility grid.

### Whitespace Philosophy
Apple's whitespace is the product's pedestal — every tile opens with at
least 64px of air above its headline and 48–64px below, and product renders
sit at least 40px from any surrounding content. The footer is the one
deliberately dense exception, giving the full information architecture at a
glance.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat | No shadow, no border | Full-bleed tiles, global nav, footer, body sections |
| Soft hairline | 1px border at low alpha | Utility cards, sub-nav frosted-glass separator |
| Backdrop blur | `backdrop-filter: blur(N)` on parchment at 80% | Sub-nav and the iPhone buy-page floating sticky bar |
| Product shadow | `rgba(0,0,0,0.22) 3px 5px 30px 0` | Product renders resting on a surface — the only true shadow in the system |

Apple uses exactly one drop-shadow, and it's reserved for photographic
product imagery — never cards, buttons, or text. UI elevation instead comes
from surface-color change (light tile ↔ dark tile) and backdrop-blur on
sticky bars; the single shadow exists to give the product physical weight,
not to signal UI hierarchy. Atmospheric mood on the environment page comes
from photography alone (a mountain vista at dawn), with no gradient tokens
involved; the edge-to-edge tile alternation supplies rhythm without any
border or shadow.

## Shapes

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | Full-bleed product tiles — no corner rounding |
| `{rounded.xs}` | 5px | Inline links styled as subtle chips (rare) |
| `{rounded.sm}` | 8px | Dark utility buttons, inline card imagery |
| `{rounded.md}` | 11px | White Pearl Button capsules |
| `{rounded.lg}` | 18px | Store utility cards, accessories grid cards |
| `{rounded.pill}` | 9999px | Primary blue pill CTAs, sub-nav buy button, configurator chips, search input — the signature Apple pill |
| `{rounded.full}` | 9999px / 50% | Circular control chips floating over photography |

Hero imagery is full-bleed (21:9 or taller on the homepage, 16:9 elsewhere),
photographic-realistic, often shot on a tinted surface that becomes the
tile background. Accessory-grid photos crop to square 1:1 at 18px radius on
light neutral backgrounds. Hero tiles never round their images; rounding
appears only on inline card imagery.

## Components

- **`global-nav`** — persistent 44px-tall black bar, quiet 12px links
  spaced roughly 20px apart, Search/Bag icons always visible right;
  collapses to a hamburger + centered logo around 834px.
- **`sub-nav-frosted`** — 52px sticky bar below the global nav, parchment
  at 80% opacity with backdrop blur; category name in the 21px/600 tagline
  role left, inline links + a persistent primary "Buy" CTA right.
- **`button-primary`** — Action Blue fill, white text, full pill radius,
  11×22px padding — the full-pill shape IS the brand action signal. Active
  state uses `transform: scale(0.95)`; focus adds a 2px Focus Blue outline.
- **`button-secondary-pill`** — transparent "ghost pill": Action Blue text
  and 1px Action Blue border, same pill radius and padding as primary.
- **`button-dark-utility`** — ink-filled, white text, 8px radius, used for
  global-nav actions (Sign In, Bag, language selector).
- **`button-pearl-capsule`** — Pearl-surface secondary button on product
  cards, 3px divider-soft border functioning as a ring, 11px radius.
- **`button-store-hero`** — a larger primary CTA at 18px/300 weight (the
  rare weight-300) with slightly more padding, used sparingly on store
  landing pages.
- **`button-icon-circular`** — 44×44px, translucent chip-gray fill,
  floats over photography for carousel/close controls.
- **`text-link`** / **`text-link-on-dark`** — Action Blue on light
  surfaces, Sky Link Blue on dark tiles where Action Blue would vanish.
- **`product-tile-light`** / **`product-tile-parchment`** / `product-tile-dark`
  (with `-2`/`-3` variants) — full-bleed, 0px-radius, 80px-padded tiles
  alternating white, parchment, and three near-black tones; each stacks a
  product name, one-line tagline, two pill CTAs, and a product render
  carrying the single system shadow.
- **`store-utility-card`** — white, 1px hairline border, 18px radius, 24px
  padding; a 1:1 product photo (8px inner radius) above name + price + a
  text link.
- **`configurator-option-chip`** / **`-selected`** — pill-shaped selectable
  cells with thumbnail + label + price delta; selected state upgrades the
  border to 2px Focus Blue.
- **`environment-quote-card`** — the sustainability page's dark photographic
  hero, centered white headline, small green pictographic logo, single
  primary CTA, 80px padding.
- **`floating-sticky-bar`** — 64px bottom bar on the iPhone buy page,
  parchment at 80% opacity with blur; running price total left, primary
  "Add to Bag" CTA right.
- **`search-input`** — white, pill radius (matching the CTA grammar), 44px
  tall, 12×20px padding, 1px low-alpha border.
- **`footer`** — parchment background, dense link columns in the relaxed
  2.41-leading dense-link role, 14px/600 column headings, fine-print legal
  row at the very bottom.

## Do's and Don'ts

### Do
- Use `{colors.primary}` (Action Blue) for every interactive element and
  nothing else — the single accent is non-negotiable.
- Set headlines in `{typography.hero-display}` or `{typography.display-lg}`
  with negative letter-spacing for the signature tight cadence.
- Run body copy at `{typography.body}` (17px/400/1.47/-0.374px) — never
  16px.
- Alternate light and dark product tiles for section rhythm; the color
  change IS the divider.
- Reserve pill radius for anything that should read as an "action":
  primary CTA, configurator chips, search input, sticky-bar CTA.
- Apply the single product-shadow only to product renders resting on a
  surface.
- Use `transform: scale(0.95)` as the universal active/press
  micro-interaction.
- Keep the global nav true black — it's the only place pure black appears
  on most pages.

### Don't
- Don't introduce a second accent color.
- Don't add shadows to cards, buttons, or text.
- Don't use gradients as decorative backgrounds.
- Don't set body copy at weight 500 — the ladder is 300/400/600/700 with
  500 deliberately absent.
- Don't round full-bleed tiles — they're rectangular and edge-to-edge.
- Don't tighten body line-height below 1.47.
- Don't mix radii grammars outside the documented sm/lg/pill roles.
- Don't use Sky Link Blue on light surfaces — it's the dark-tile-only
  variant.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Small phone | ≤ 419px | Single-column tiles; sub-nav reduces to category name + primary CTA only; hero type drops to 28px. |
| Phone | 420–640px | Single-column stack; product renders scale to 80% of tile width; hero h1 drops to 34px. |
| Large phone | 641–735px | Tighter tile padding (48px vs 80px); fine-print wraps. |
| Tablet portrait | 736–833px | Global nav collapses to hamburger; sub-nav hides category chips, keeps the primary CTA. |
| Tablet landscape | 834–1023px | Global nav fully expands again; 3-column utility grids become 2-column. |
| Small desktop | 1024–1068px | Product tiles use 2/3 width with margin gutters; hero h1 stays at 40px. |
| Desktop | 1069–1440px | Full layout; 4–5 column store grids; 1440px content max. |
| Wide desktop | ≥ 1441px | Content locks at 1440px, margins absorb extra width. |

### Touch Targets
- Minimum 44×44px throughout; primary CTAs land near 44×100px thanks to the
  pill radius's generous hit area.
- Icon-circular buttons are exactly 44×44px.
- Global nav utility links deliberately sit at a tighter ~32×80px target on
  desktop, replaced by the mobile hamburger at ≤833px.

### Collapsing Strategy
- Global nav: full link row → logo + hamburger + bag icon at 834px and
  below.
- Sub-nav: category + links + CTA → category + CTA only on mobile; inline
  links move into a hamburger tray.
- Product tiles: 2-column → 1-column at 834px; vertical padding tightens
  from 80px to 48px at small-phone.
- Utility grids: 5-col → 4-col (1440px) → 3-col (1068px) → 2-col (834px) →
  1-col (640px).
- Hero type: 56px → 40px at 1068px → 34px at 640px → 28px at 419px.

## Known Gaps

- Form validation and error states weren't surfaced on the analyzed pages —
  only the neutral search input is documented.
- The homepage's embedded video player uses pure black; interior player
  controls are a platform widget, not documented here.
- Some component imagery rotates per surface; component specs describe
  structure, not the rotating content.
- Dark-mode counterparts for store/accessories utility cards weren't
  surfaced — the documented system is the default light-dominant variant.
- The exact backdrop-filter blur radius on frosted surfaces is
  platform-dependent (production commonly uses `saturate(180%)
  blur(20px)`) but isn't formalized as a token.
