# Vercel Design System — Full Analysis

Adapted from the Vercel design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/vercel/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Vercel is a developer platform, and its marketing surface reads like the
public face of a deployment dashboard, aimed at people who already speak
the product's language. The look is one of the cleanest "stark" systems
around: a near-white `colors.canvas-soft` body (`#fafafa`), ink-near-black
`colors.ink` text (`#171717`), and a full 200-step gray scale that gives
every divider, border, and disabled state its own deliberate step. Color
only shows up at marketing scale in the multi-stop mesh gradient — running
`colors.gradient-develop-start` through `colors.gradient-preview-end` into
`colors.gradient-ship-start` and out to cyan, magenta, and amber — which
appears as a full atmospheric backdrop, never shrunk to a swatch. That
gradient is effectively the brand's entire decorative vocabulary.

Type is the second load-bearing choice. Vercel's own geometric sans
(`Geist`) covers display, body, and buttons all at once — weight 600 for
display, 500 for buttons, 400 for body. A companion mono face (`Geist
Mono`) handles anything technical: terminal mockups, code blocks,
occasional filename captions. Headlines sit in sentence case with
aggressively negative tracking (-2.4px at the 48px hero) — the brand never
tracks positively at display sizes and never shouts in all caps outside of
mono labels.

Surfaces step through four levels: `colors.canvas` pure white for cards,
`colors.canvas-soft` (98%) for the page body, `colors.canvas-soft-2` (95%)
for occasional insets, and `colors.primary` deep ink for the polarity-
flipped dark band. Shadows stay exceptionally quiet — elevated cards use a
stacked recipe (`0px 1px 1px #00000005` plus `0px 2px 2px #0000000a`) with
an inset border, rather than a single heavy drop. Cards never float on
theatrical shadow; they sit held by hairline and soft glow.

**Key characteristics:**
- A single black-ink primary CTA carries every conversion target, paired
  with a white-on-white `button-secondary`. Marketing CTAs use a 100px
  pill; in-app nav buttons use a tight 6px square instead.
- The multi-stop mesh gradient is the only decorative chrome — hero scale
  and inside feature-band atmospheric backdrops. It is, functionally, the
  brand.
- Section eyebrows and small labels run in the monospace face
  (`typography.caption-mono` or `typography.code`); everything else stays
  in the geometric sans.
- Elevation is built from three stacked, low-opacity offsets rather than
  one heavy shadow.
- A full 100–1000 gray/blue/red/amber/green/teal/purple/pink scale exists
  as system tokens, but the marketing surface only touches the `100`,
  `700`, and `1000` steps — the rest live in in-product surfaces.
- Pricing follows a 3-up rhythm on `/pricing`, with the middle
  `pricing-card-featured` tier flipped to `colors.primary` against
  white-card siblings.

## Colors

### Brand & accent
- **Ink** (`colors.primary`, `#171717`) — the single primary CTA color;
  black-near-pure ink that also carries body text on light surfaces.
  Resolved from the design system's `--ds-gray-1000`.
- **Cyan** (`colors.cyan`, `#50e3c2`) — the signature mint-cyan visible in
  the hero gradient's stops.
- **Highlight pink** (`colors.highlight-pink`, `#ff0080`) — the high-
  saturation stop in the preview-gradient pair.
- **Violet** (`colors.violet`, `#7928ca`) — the deep purple opening the
  preview-gradient and appearing in developer-console highlights.
- **Link blue** (`colors.link`, `#0070f3`) — the primary link color and
  legacy success semantic.

### Surface
- **Canvas** (`colors.canvas`, `#ffffff`) — pure-white card/dialog/modal
  surface.
- **Canvas soft** (`colors.canvas-soft`, `#fafafa`) — 98% white, the
  default page background for nearly every section.
- **Canvas soft 2** (`colors.canvas-soft-2`, `#f5f5f5`) — a slightly
  deeper inset used for code-editor inner backgrounds, hovered template
  cards, and dropdown menus.
- **Hairline** (`colors.hairline`, `#ebebeb`) — 1px dividers on table
  rows, card borders, input borders.
- **Hairline strong** (`colors.hairline-strong`, `#a1a1a1`) — a stronger
  500-level gray for slightly-heavier dividers and de-emphasized text.

### Text
- **Ink** (`colors.ink`, `#171717`) — headings and body on light surfaces.
- **Body** (`colors.body`, `#4d4d4d`) — sub-headings, captions, inactive
  nav-link text.
- **Mute** (`colors.mute`, `#888888`) — placeholder and low-key labels.
- **On primary** (`colors.on-primary`, `#ffffff`) — text on
  `colors.primary` surfaces.

### Semantic
- **Success/link** (`colors.success`, `#0070f3`) — doubles as the primary
  link color, underlined on hover.
- **Link deep** (`colors.link-deep`, `#0761d1`) — pressed/visited state.
- **Link bg soft** (`colors.link-bg-soft`, `#d3e5ff`) — soft pastel fill
  for informational pill banners.
- **Error** (`colors.error`, `#ee0000`) with soft (`#f7d4d6`) and deep
  (`#c50000`) variants for destructive states.
- **Warning** (`colors.warning`, `#f5a623`) with soft (`#ffefcf`) and deep
  (`#ab570a`) variants for caution/pending status.

### Brand gradient
Three color pairs collapse into a single mesh gradient at hero scale:
**Develop** (blue `#007cf0` → teal `#00dfd8`), **Preview** (violet
`#7928ca` → pink `#ff0080`), and **Ship** (coral `#ff4d4d` → amber
`#f9cb28`). Treat all three as one unified object: never crop to a single
color, never reorder the stops, never shrink it below hero scale.

## Typography

### Font family
Two custom faces cover the system: **Geist**, the geometric sans, carries
every display/body/button/link/label role at weights 400/500/600 (never
heavier); **Geist Mono** covers terminal mockups, code blocks, and small
mono-caption labels at weight 400, sized 12–13px. A condensed display face
(`Space Grotesk`) loads for rare editorial moments but doesn't appear as a
primary face anywhere captured.

### Hierarchy
Full scale in `design-tokens.yaml → typography`: `display-xl` 48px/600
with -2.4px tracking for the hero, down through `display-lg` 32px,
`display-md` 24px, `display-sm` 20px; body runs `body-lg` 18px through
`caption` 12px; `code` and `caption-mono` at 12–13px carry the technical
voice; buttons use `button-md`/`button-lg`.

### Principles
- Negative tracking is part of the voice — reverting to default tracking
  at display sizes breaks the brand.
- Headlines are sentence-case, often period-terminated ("Build and deploy
  on the AI Cloud.") — that punctuation is deliberate.
- Mono is for the technical layer only — eyebrows, code blocks, terminal
  mockups — never body paragraphs.
- Weight 600 is the display ceiling; the sans never appears at 700+.

### Font substitutes
Both faces are proprietary. *Inter* (400/500/600) with
`font-feature-settings: "ss01", "ss02"` is the closest open match for the
geometric sans; *Satoshi* is a passable second choice. For mono, *JetBrains
Mono* (400) at 12–13px is closest; *IBM Plex Mono* is the runner-up.

## Layout

- Base unit: 4px (the brand's `--geist-space` token). Full scale in
  `design-tokens.yaml → spacing`, from `xxs` 4px to `section` 192px.
- Marketing bands use 64–96px top/bottom padding; hero bands stretch to
  192px to give the mesh gradient room.
- Marketing cards sit at 24–32px interior padding; template-grid cards stay
  tighter at 16px for denser grids.
- Button/nav/chip rows use 12–16px gaps; the brand's `--geist-gap` token is
  exactly 24px.
- Container maxes around 1400px (legacy pages still use 1200px), with 24px
  desktop gutters / 16px mobile.
- Grid patterns: 3-up feature rows dropping to 1-up mobile, a 5-up tab pill
  row, a 5-up template grid scaling to 1-up, and a 3-up pricing grid with
  the middle tier flipped.
- The gradient does most of the decorative work, so whitespace mainly
  separates bands (64–96px between sections); inside a card the
  headline/paragraph stack stays tight at 8px before a wider gap to the CTA
  cluster.

### Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Mobile | <600px | Hero stacks; hamburger nav; 3-up grids drop to 1-up; tab row scrolls. |
| Tablet | 600–959px | 3-up grids drop to 2-up. |
| Desktop | 960–1199px | Full 3-up grids; pricing 3-up. |
| Wide | 1200–1399px | Container caps at 1400px. |
| Ultra-wide | ≥1400px | Content stays centered at 1400px; bands stretch edge-to-edge in color only. |

`button-primary` renders ~32px in nav and ~48px in marketing contexts —
marketing CTAs comfortably clear WCAG AAA; nav buttons gain touch padding
on mobile to hit the 44×44px floor. Nav collapses to a hamburger overlay;
the hero never splits into two columns at any breakpoint (headline and body
always stack). Template thumbnails hold 16:9 aspect at every size; the mesh
gradient scales fluidly and never tiles or crops.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 — flat | none | full-bleed hero and dark polarity-flipped sections |
| 1 — inset hairline | `0 0 0 1px #00000014` inset | default card chrome |
| 2 — subtle drop | `0 1px 1px #00000005, 0 2px 2px #0000000a` + inset | template-grid, marketing cards |
| 3 — soft stack | `0 2px 2px #0000000a, 0 8px 8px -8px #0000000a` + inset | feature-grid cards |
| 4 — float stack | `0 2px 2px #0000000a, 0 8px 16px -4px #0000000a` + inset | pricing cards, callouts |
| 5 — modal | `0 1px 1px #00000005, 0 8px 16px -4px #0000000a, 0 24px 32px -8px #0000000f` + inset | modals, dropdowns |

Shadows are always stacked — several small offsets layered to simulate
natural light — never a single generic 8px blur, and an inset hairline
ring keeps every card edge crisp. The mesh gradient supplies whatever
atmospheric depth the page has, applied flat rather than as 3D
illustration; switching a section from `canvas-soft` to `primary` is the
brand's chief depth cue between bands.

## Shapes

| Token | Value | Use |
|---|---|---|
| `rounded.none` | 0px | full-bleed hero/footer bands |
| `rounded.xs` | 4px | tightest inline pill |
| `rounded.sm` | 6px | the brand's base UI radius — in-app buttons, inputs, dropdowns |
| `rounded.md` | 8px | the marketing radius — feature and template cards |
| `rounded.lg` | 12px | larger pricing-card variants |
| `rounded.xl` | 16px | largest card chrome, when hosting a hero image cap |
| `rounded.pill-sm` | 64px | tab-ghost pills in the category row |
| `rounded.pill` | 100px | marketing CTA pill — `button-primary`, `button-secondary` |
| `rounded.full` | 9999px | circular icon buttons, ghost nav links |

The mesh gradient is treated as full-bleed 2D wallpaper, never cropped to a
frame; customer logos render as consistent-height monochrome SVGs; the
code-editor mockup is a dark 16:10 rectangle at `rounded.md`; template
thumbnails hold 16:9 inside `rounded.md`.

## Components

Full specs in `design-tokens.yaml → components`. Summary:
- **Buttons** — `button-primary`/`button-secondary` at marketing scale
  (100px pill), `button-primary-sm`/`button-secondary-sm` at nav scale, and
  a `tab-ghost` pill for the category row. Nav CTAs (`nav-cta-signup`,
  `nav-cta-login`, `nav-cta-ask-ai`) use the tight 6px radius instead.
- **Cards** — `card-marketing`/`card-marketing-large` for feature callouts,
  `card-soft` for cluster sub-regions, `template-card` for the deploy-
  template grid, `code-editor-mockup` for dark code previews, and
  `pricing-card`/`pricing-card-featured` for the 3-up pricing grid.
- **Inputs** — `form-input`/`form-input-sm`/`form-input-lg`, all sharing
  the 6px radius at 32/40/48px heights.
- **Navigation** — `nav-bar` (64px sticky header), `nav-link`, and a
  4-column `footer` with mono-caps eyebrow labels.
- **Signature pieces** — `hero-band` (mesh-gradient backdrop),
  `feature-mesh-band`, `showcase-band-light`/`showcase-band-dark`,
  `logo-strip`, `badge-secondary`, `banner-marketing`, and `link-inline`.
- **Example surfaces** (`ex-*`) — auto-derived kit-mirror demonstrations
  (pricing tier, product selector, app-shell row, data-table cell, auth
  card, modal, empty state, toast) re-skinning the brand's primitives onto
  ten common product surfaces.

## Do's and don'ts

**Do**
- Reserve `colors.primary` (`#171717`) for primary CTAs — black ink IS the
  conversion target.
- Use the 100px pill for marketing-scale CTAs and the 6px radius for
  nav-scale buttons; let the two scales coexist deliberately.
- Set headlines in `typography.display-*` weight 600, sentence-case, often
  period-terminated, with aggressive negative tracking.
- Use the mesh gradient as atmospheric decoration at hero scale only —
  never as an icon, never as a single flat color.
- Layer stacked shadows with inset hairline rings rather than single heavy
  drops.
- Cycle surfaces through `canvas-soft` → `canvas` → `primary` polarity-
  flipped bands as the page's depth cue.
- Set code blocks and technical eyebrows in `typography.code` /
  `typography.caption-mono` — mono is the platform's voice.

**Don't**
- Don't add a sixth accent color; ink + gray + the four-pair gradient is
  the whole system.
- Don't render headlines in all caps — sentence-case with negative
  tracking is non-negotiable.
- Don't drop a single heavy shadow on cards — always stack small offsets
  with an inset hairline.
- Don't shrink the brand gradient to icon scale or a single flat color —
  it lives at hero scale only.
- Don't push the geometric sans to weight 700; the display ceiling is 600.
- Don't mix the 100px marketing pill with the 6px nav radius on one
  screen — pick a scale and hold it.
- Don't set body paragraphs in the mono face — that's reserved for code
  and technical labels.

## Known gaps

- The `ex-*` example components are auto-derived kit-mirror surfaces, not
  directly observed, and should be treated as reasonable extrapolations.
- Font substitutes are recommendations only — Geist and Geist Mono are
  proprietary (though Vercel does distribute Geist as open-source in some
  contexts; treat the documented fallback stack as the safe default).
- The full 100–1000 in-product color scale isn't fully captured here since
  the marketing surface only exercises a few of its steps.
