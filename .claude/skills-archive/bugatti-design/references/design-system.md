# Bugatti Design System — Full Analysis

Adapted from the Bugatti design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/bugatti/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Bugatti's marketing surface is the most austere interface in luxury
automotive: a near-pure black `colors.canvas` (`#000000`) carrying white
uppercase, letterspaced display type and full-bleed automotive photography.
There is no accent color, no card decoration, no shadow, no gradient, no
chrome of any kind — only photography, typography, and the brand wordmark.
Where peer luxury-auto brands (BMW M, Aston Martin, Lamborghini) lean on
some accent color or signature motif, Bugatti leans on nothing at all. The
empty space, the photograph, and the precisely-tracked headline together
are the brand.

The system runs **three custom Bugatti typefaces**: Bugatti Display (all
display headlines and the "BUGATTI" wordmark, uppercase with wide tracking),
Bugatti Text Regular (body paragraphs, a serif text face), and Bugatti
Monospace (button labels, navigation, captions, dates — anywhere precision
matters). The split is treated as unbreakable: Bugatti Text never appears
in a button, and Bugatti Monospace never appears in a paragraph.

Display sizes are set at weight 400 (regular) — never bold. Emphasis comes
from size and tracking rather than weight: the wordmark tracks at 6px,
display headlines at 2-4px, uppercase labels at 2-2.5px. Tight tracking
would be a brand violation; the wide spacing is what gives the system its
"engineered precision" feel, distinguishing it from other luxury makers.

**Key characteristics:**
- Pure black canvas with white type and no light mode.
- Three custom typefaces: Display (uppercase headlines/wordmark), Text
  Regular (serif body), Monospace (buttons/captions/nav).
- All display headlines are UPPERCASE with 2-4px tracking; body stays
  sentence-case at 0 tracking.
- No accent color at all — the only non-monochrome color anywhere is
  `colors.link` (`#c3d9f3`), a desaturated ice-blue used rarely on inline
  anchor links.
- Buttons are pill-shaped with a fully transparent background and a 1px
  white outline — Bugatti is the only luxury-auto brand with a fully
  transparent primary CTA.
- Photography is the only source of depth. No drop shadows, no gradients,
  no card surfaces beyond `surface-card` (`#141414`), a tone barely
  distinguishable from black.
- Section rhythm is unusually generous — `spacing.section` (120px) between
  major bands, longer than most marketing sites, because Bugatti's pages
  are mostly photography with minimal text density.

## Colors

### Brand & accent
- **Primary** (`#ffffff`) — the single brand color: white type and white CTA
  outlines against black.
- **Link** (`#c3d9f3`) — the only non-monochrome color in the system, a
  desaturated ice-blue used on inline anchor links and, rarely, on focus
  states. Bugatti's brand discipline is tight enough that this one token is
  essentially the whole chromatic vocabulary beyond black and white.

### Surface
- **Canvas** (`#000000`) — the default page floor across every surface.
- **Surface Soft** (`#0d0d0d`) — a barely-above-black tone for spec table
  rows and dense data sections.
- **Surface Card** (`#141414`) — cards (career callout, newsroom article
  container, occasional content cards); even card surfaces stay nearly
  black, with no real contrast jump.
- **Surface Elevated** (`#1f1f1f`) — one step further from black, used for
  nested cards on rare dense pages.
- **Hairline** (`#262626`) — the 1px divider tone: visible but quiet, used
  on table rows, between body sections, and around card outlines.
- **Hairline Strong** (`#3a3a3a`) — a heavier divider used under input
  fields, which otherwise carry no border of their own besides that
  underline.

### Text
- **Ink / On Dark** (`#ffffff`) — all headline and primary text on the dark
  canvas.
- **Body** (`#cccccc`) — default running-text color, slightly cooler than
  pure white, used in body paragraphs.
- **Body Strong** (`#e6e6e6`) — emphasized body and lead paragraphs.
- **Muted** (`#999999`) — footer links, dates, captions, secondary metadata.
- **Muted Soft** (`#666666`) — a second-tier muted for very secondary text
  such as legal disclaimers and the copyright line.

### Semantic
- **Warning** (`#d4a017`) — reserved for technical-warning callouts
  (specifications, recall notices); almost never seen on marketing surfaces.
- **Success** (`#5fa657`) — order-confirmation states, rare on marketing
  pages.

## Typography

### Font family
The system runs three custom Bugatti typefaces as a rigid trinity:
1. **Bugatti Display** — all display headlines, the "BUGATTI" wordmark, and
   model name plates; uppercase, wide-tracked, the default for any visual
   emphasis.
2. **Bugatti Text Regular** — a serif text face used exclusively for
   running body copy, lead paragraphs, and model descriptions, set in
   standard sentence case with no tracking.
3. **Bugatti Monospace** — button labels, navigation, captions, dates, and
   any precision-flavored context; always uppercase with 2-2.5px tracking.

The split is functional and absolute — Bugatti Display in a button would
break the machined-precision voice, Bugatti Monospace in a paragraph would
break the engineered-elegance voice, and Bugatti Text in a button is simply
not done. Fallback stacks: `-apple-system, BlinkMacSystemFont, "Segoe UI",
Roboto, sans-serif` for Display, `Garamond, "Times New Roman", serif` for
Text Regular, and `ui-monospace, "SF Mono", "Cascadia Mono", monospace` for
Monospace.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale. Key entries:
`display-xl` (64/400, 4px tracking, hero h1 like "THE BUGATTI F.K.P.
HOMMAGE"), `display-lg` (48/400, 3px tracking, section heads), `display-md`
(32/400, 2px tracking, model names), `display-sm` (24/400, 1.5px tracking,
card titles), `wordmark` (14/400, 6px tracking — the widest in the
system), `title-md` (20/400, career listing titles), `caption-uppercase`
(11/400, 2px tracking, Monospace — captions and metadata), `body-md`
(16/400, Text Regular serif, sentence case, 0 tracking), `button` (14/400,
2.5px tracking, Monospace).

### Principles
The system never uses bold weight — every typeface stays at 400. Emphasis
instead comes from: size (a 64px hero versus 16px body is a 4x hierarchy),
letter-spacing (6px wordmark versus 0px body), case (uppercase display
versus sentence-case body), and family contrast (Display versus Text
Regular versus Monospace). Introducing weight 700 anywhere would break the
"modest engineering" feel and pull the brand toward a generic luxury
template. The serif Bugatti Text Regular is also what sets Bugatti apart
from the all-sans luxury crowd (BMW, Aston Martin, Lamborghini all run
sans-serif body copy) — its literary, slow-reading feel matches Bugatti's
editorial philosophy.

### Font substitutes
If the three Bugatti faces are unavailable, the closest open-source
stand-ins are **Saira Condensed** (variable, weight 400, +0.05em tracking)
for Bugatti Display, **Cormorant Garamond** or **EB Garamond** for Bugatti
Text Regular, and **JetBrains Mono** or **IBM Plex Mono** (regular weight)
for Bugatti Monospace. Preserving the three-family split matters more than
matching the exact typeface.

## Layout

- **Base unit:** 4px. Full scale: `xxs` 4px, `xs` 8px, `sm` 12px, `md` 16px,
  `lg` 24px, `xl` 40px, `xxl` 64px, `section` 120px.
- **Section padding:** `spacing.section` (120px) — longer than most
  marketing sites because Bugatti's bands are mostly photography with
  minimal text; the empty space frames the cars.
- **Card internal padding:** `spacing.lg` (24px) for newsroom and content
  cards; `spacing.md` (16px) for the career callout card; `spacing.xxl`
  (64px) inside hero photo bands.
- **Gutters:** `spacing.xl` (40px) between cards in 2-up grids — wider than
  typical because Bugatti's grids are sparse.
- **Max content width:** roughly 1280px centered; hero photo bands bleed
  full-width with no max.
- **Grid:** single 12-column grid for editorial body; newsroom runs 2-up
  desktop, 1-up tablet+mobile; career listings run single-column with 80px
  row spacing.
- **Whitespace philosophy:** Bugatti uses whitespace more aggressively than
  any luxury-auto competitor. The homepage hero is mostly photography plus
  huge whitespace plus a single sentence and a single button. The empty
  black space below the photograph is intentional — it lets the car
  breathe. Compressing that whitespace to fit more content would break the
  brand's core contract that less is more.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| Flat | no shadow, no border | body, top nav, footer, photo bands |
| Soft hairline | 1px `hairline` border | section dividers, table rows |
| Card surface | `surface-card` background, no shadow | career callout, newsroom article container |
| Photographic depth | full-bleed photography, edge-to-edge crop | hero bands, model showcases |

The system uses no shadows, no glassmorphism, no gradients — depth comes
entirely from photography (lighting, lens, subject framing) and from the
contrast between black canvas and the minimally-elevated `surface-card`.
There is no decorative depth beyond that: Bugatti is the only luxury-auto
brand without a single decorative motif — no stripe, no badge, no heritage
emblem on the marketing site outside the wordmark itself.

## Shapes

| Token | Value | Use |
|---|---|---|
| `rounded.none` | 0px | all cards, photo containers, inputs, spec cells — the dominant radius |
| `rounded.pill` | 9999px | all buttons — the only rounded element in the system |
| `rounded.full` | 9999px / 50% | circular icon buttons, avatar surfaces |

The radius logic is binary: rectangular for everything except buttons,
which are pills. There's no 4px/8px/12px middle ground — those would feel
"designed" rather than "engineered." Hero photography fills full-width with
no rounding; grid photo cards keep sharp `rounded.none` corners with
edge-to-edge images. Model detail shots use 16:9 or wider cinema-aspect
ratios; newsroom thumbnails use 16:9 at 0px corners. There are no avatars
or rounded photo crops anywhere on the marketing site.

## Components

Definitions live in `design-tokens.yaml → components`. Summary:
- **top-nav** — a 56px transparent bar overlaid on the hero photo, "MENU" at
  left, the centered `wordmark-display` ("BUGATTI" at 14px, 6px tracking),
  and "STORE" plus a bag icon at right, all in Monospace nav-link type.
- **Buttons** — `button-primary` (transparent fill, 1px white outline,
  pill radius, uppercase Monospace label at 2.5px tracking — unique among
  luxury-auto brands for its fully transparent fill), `button-icon`
  (40×40 circular, same outline-only treatment), `text-link` (inline links
  in the ice-blue `colors.link`, underlined, set in the serif body face).
- **Cards & containers** — `hero-photo-band` (full-bleed photo, centered
  display-xl headline, small Monospace caption, single primary button),
  `career-callout-card` (surface-card, 320px wide, floats over the homepage
  hero with a recruiting prompt), `model-photo-card` (canvas background,
  16:9/21:9 hero shot, display-md model name, caption-uppercase specs line,
  text-link), `newsroom-article-card` (canvas + hairline, 16:9 thumbnail,
  date-pill, title-md headline, serif excerpt), `career-listing-row`
  (transparent row with hairline divider, title-md job title, caption-
  uppercase location/department, chevron), `spec-cell` (transparent with
  hairline dividers between cells, title-md value over caption-uppercase
  label).
- **Inputs** — `text-input` (fully transparent background, 1px hairline-
  strong underline only — no other border — serif body type, focus
  thickens the underline to white).
- **Tags & captions** — `caption-overlay` (photo-overlay caption text in
  Monospace uppercase), `category-tag`/`date-pill` (transparent inline
  Monospace labels with no fill or border — the type itself is the tag).
- **CTA / footer** — `cta-band-photo` (pre-footer "Discover Bugatti" band
  with full-bleed photography, centered display-md headline, primary
  button), `footer` (black, 4-column link list covering Bugatti / Models /
  Heritage / Connect, serif copyright line, centered wordmark at the very
  bottom, never inverts to light).

## Do's and don'ts

**Do**
- Anchor every page with full-bleed automotive photography — the cars carry
  the voltage, chrome recedes entirely.
- Keep all display headlines UPPERCASE Bugatti Display with 2-4px tracking;
  give the wordmark 6px.
- Hold the trinity: Display for headlines, Text Regular (serif) for body,
  Monospace for buttons/captions/nav.
- Keep `button-primary` transparent with a 1px white outline — that's the
  brand button.
- Use weight 400 everywhere; the system assigns no role to bold.
- Use `spacing.section` (120px) between major editorial bands — the
  whitespace is part of the brand.
- Reserve `colors.link` (`#c3d9f3`) for inline anchor links only.

**Don't**
- Don't introduce any accent color beyond `colors.link` — total monochrome
  plus photography is the contract.
- Don't bold any type.
- Don't fill primary buttons — transparent plus outline only.
- Don't compress the whitespace between sections.
- Don't round anything besides buttons — cards, photos, and inputs stay at
  0px.
- Don't tighten letter-spacing on display headlines.
- Don't mix the type trinity — Display never appears in a button, Monospace
  never appears in a paragraph.

## Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Mobile | < 768px | hamburger nav; hero h1 64→32px; career callout card hides; photo bands stay full-bleed; footer 4 cols → 1 |
| Tablet | 768–1024px | top nav stays minimal (MENU + wordmark + STORE); 2-up newsroom grid; career rows full-width |
| Desktop | 1024–1440px | full minimal top-nav; 2-up newsroom grid; spec tables 4-up |
| Wide | > 1440px | same as desktop with more breathing room; max content 1280px |

Touch targets: `button-primary` renders at a minimum 44×44px (WCAG AAA);
`button-icon` is exactly 40×40; `text-input` height is 44px; career listing
rows use 24px vertical padding, reaching 44px+ effective tap area with
surrounding spacing. Top nav stays minimal at every breakpoint (labels hide
behind a hamburger on mobile, but the wordmark stays centered); hero
photography stays full-bleed throughout, with crops adjusting from wide at
desktop to vertical on mobile; the homepage's career callout card hides
below 768px since it's a desktop-only floating element; the 2-up newsroom
grid collapses to 1-up below 768px; spec cells reflow 4-up → 2-up → 1-up
while keeping the same display size.

## Known gaps

- The frequency-based palette analyzer captured only three colors at root
  level (`#000000`, `#999999`, `#c3d9f3`); white text and the dark surface
  tones were inferred from screenshots since Bugatti's pages are monochrome
  enough that they didn't surface as distinct palette entries.
- The three Bugatti typefaces are licensed and not available as public web
  fonts; substitutes are documented under Typography.
- Animation and transition timing (photo carousel transitions, menu
  hover-reveal, configurator animations) is out of scope.
- Form validation states beyond the underline-only `text-input` weren't
  extracted from the analyzed surfaces.
- The configurator surface (custom paint/interior pickers) wasn't in the
  analyzed URL set, so its swatch grid and price-summary card aren't
  documented here.
- The German-language newsroom shares the same system as the English site —
  no design-system-level differences beyond localization.
- The Tourbillon model page rendered sparsely in the captured screenshot,
  suggesting lazy-loaded or interactive configurator content; its
  engine-spec layout is documented from general luxury-auto patterns
  informed by the captured spec-cell tokens.
