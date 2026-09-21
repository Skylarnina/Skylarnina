# Raycast Design System — Full Analysis

Adapted from the Raycast marketing-site design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/raycast/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Raycast's marketing site reads like an extended product screenshot. The
chrome *is* the in-product command palette scaled up to marketing size:
pure near-black canvas (`colors.canvas`, `#07080a`), hairline 1px borders
(`colors.hairline`, `#242728`), command-palette-style cards rounded
between 6 and 16px, Inter typography with the **ss03 stylistic set enabled
site-wide** (a single character — the alternate `g` — that gives Raycast's
type its subtle signature distinction), a single white CTA pill anchoring
every primary action, and small splashes of saturated accent reserved for
category illustrations.

The system runs effectively one surface mode — dark — with a faint
four-step ladder (`canvas` → `surface` → `surface-elevated` →
`surface-card`) carrying cards, in-card panels, and key-cap glyph
backgrounds. The signature decorative moment is a **red diagonal-stripe
gradient band** across the very top of the home-page hero, a launch-banner
motif and the only place saturated red appears on chrome. Beyond that
single moment, color is reserved for category accents inside extension
and feature illustrations — Hacker News yellow, Slack red, Linear green,
info blue.

The underlying philosophy is "the marketing page is the product." Section
rhythm is generous (`spacing.section`, 96px), but the page never breaks
tonal continuity — the whole site sits in one continuous dark mode,
full-bleed product screenshots show Raycast's actual command palette /
store / AI chat surfaces, and the typography ligature settings are
inherited directly from the in-product app's text rendering.

**Key characteristics:**
- A single dark surface mode with a four-step ladder: canvas (#07080a) →
  surface (#0d0d0d) → surface-elevated (#101111) → surface-card (#121212).
- A white CTA pill is the universal primary action — everything else stays
  monochrome dark.
- Inter with `font-feature-settings: "calt", "kern", "liga", "ss03"`
  enabled site-wide — the ss03 alternate `g` is part of the brand voice.
- Hairline 1px borders carry every card edge; there are no drop shadows
  anywhere in the system.
- A multi-radius card vocabulary from 6px (keycaps) up to 16px (hero
  mockup containers).
- Saturated category accents appear only inside extension-tile imagery,
  never on chrome.
- A signature red diagonal-stripe gradient band at the top of the hero,
  used once per page maximum.

## Colors

> **Source pages:** home, `/store` (extension marketplace), `/core-
> features/ai`, `/pricing`, and a single extension detail page. The chrome
> palette — dark surface ladder, hairline borders, white CTA, ss03-enabled
> typography — is identical across all five.

### Brand & accent
- **White** (`colors.primary`, `#ffffff`) is the universal primary CTA pill
  background — "Download," "Install Extension," "Get Pro" all carry it,
  with **White Pressed** (`#e8e8e8`) as the dimmer pressed state.
- **On Primary** (`#000000`) is pure black text on the white CTA — the
  only place black appears as text in the system.

### Surface
- **Canvas** (`#07080a`) — the dominant page background.
- **Surface** (`#0d0d0d`) — card and elevated-panel background, one notch
  lighter than canvas.
- **Surface Elevated** (`#101111`) — button-tertiary fill, text-input
  fill, store-search-bar fill, active pill-tab fill.
- **Surface Card** (`#121212`) — app-icon-tile background, keycap fill,
  active command-palette row.
- **Hairline** (`#242728`) is the universal 1px card border across every
  page, with **Hairline Soft** (`rgba(255,255,255,0.08)`) and **Hairline
  Strong** (`rgba(255,255,255,0.16)`) as fainter/stronger variants.

### Text
- **Ink** (`#f4f4f6`) — primary headlines, slightly off-white for tonal
  coherence with the near-black background.
- **Body** (`#cdcdcd`) — default paragraph text and inline-link color.
- **Mute** (`#9c9c9d`) — metadata, footer link text.
- **Ash** (`#6a6b6c`) — disabled-state text.
- **On Dark** (`#ffffff`) — interactive-state primary text (button label,
  focused tab).

### Semantic & gradient
- **Accent Blue** (`#57c1ff`), **Accent Red** (`#ff6161`), **Accent Green**
  (`#59d499`), and **Accent Yellow** (`#ffc533`) — each paired with a
  15%-opacity soft variant — mark info/error/success/warning states and
  double as category accents in extension illustrations (Hacker News
  orange-yellow being the most prominent on the home hero).
- The **Hero Stripe Gradient** — three diagonal red stripes fading from
  `#ff5757` to `#a1131a` — is the system's only chromatic gradient on
  chrome, used once per page maximum.
- The **Keycap Gradient** — a subtle linear blend from `#121212` to
  `#0d0d0d` — gives Raycast's inline keyboard-shortcut glyphs their
  slight 3D-key feel.

## Typography

### Font family
**Inter** is the system's only face, loaded with the `Inter Fallback`
system-fallback variant. Critically, Raycast enables
`font-feature-settings: "calt", "kern", "liga", "ss03"` site-wide — the
**ss03 stylistic set** swaps in Inter's alternate single-story `g`, the
brand's signature typographic detail. The display tier additionally
enables `ss02` and `ss08` and disables standard ligatures to render the
hero wordmark with its distinctive geometric construction. There's no
monospace face used outside inline `<code>` chips in documentation.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale — display-xl at
64px/600 down to caption-sm at 12px/400. The hierarchy works on a
1.6-line-height ladder for body and 1.1-1.4 for display/heading.
Letter-spacing is consistently positive (0.1-0.4px), slightly opening the
type, which gives the dark canvas an airy quality at body sizes. Without
the ss03 feature flag, the typography reads as "Inter default" rather
than "Raycast" — it's the system's most distinctive detail.

### Font substitutes
Inter is open-source and Google-Fonts-hosted — load it directly, but
enable `font-feature-settings: "calt", "kern", "liga", "ss03"` on the body
element to preserve the brand's signature look. The documented fallback is
`Inter Fallback` → `system-ui`. **JetBrains Mono** or **Geist Mono** are
acceptable substitutes for inline code chips.

## Layout

- **Base unit:** 8px, with 2/4/12px steps for tight inline gaps.
- **Universal section rhythm:** `spacing.section` (96px) between major
  blocks; card grids use `spacing.lg` (16px) gutters; feature cards get
  24px internal padding, store extension cards 16px.
- **Max width:** ~1240px at desktop with 24px gutters (~48px at
  ultrawide); hero command-palette mockups run wider (~1080px) with the
  background extending full-bleed.
- **Store extension grid:** 2-up at desktop, collapsing to 1-up at mobile
  — each card a horizontal layout with a large square app icon at the
  left and copy + Install button at the right.
- **Pricing tier grid:** 3-up at desktop (Free / Pro / Pro+Advanced AI),
  collapsing to 1-up stacked at mobile.

Whitespace is generous and the canvas uninterrupted — sections sit 96px
apart with no decorative dividers, the dark canvas continuing edge to
edge. Content stays left-aligned in a tight column with command-palette
mockup imagery occupying the right 50-60% of home-page feature rows. The
red stripe gradient only appears in the very first hero band — from the
second section down, the page is monochrome dark.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 — Flat | No border, no shadow | Canvas-on-canvas blocks, hero text, footer body |
| 1 — Hairline border | 1px `hairline` | Every card on `surface`, store extension card, pricing tier card |
| 2 — Hairline strong | 1px `hairline-strong` | Table-row separator on the comparison table |
| 3 — Surface ladder | canvas → surface → surface-elevated → surface-card | A multi-step background ladder used to create elevation without shadows |

The system has no drop-shadow elevation at all — depth is built entirely
from the surface-color ladder, where each notch lighter reads as one step
closer to the viewer. Decorative depth otherwise comes from the hero
stripe gradient, full-fidelity command-palette mockups (the actual
Spotlight-style overlay with rounded keycaps and accent-color glyphs),
small 48-64px app-icon tiles displaying real app icons, and gradient-
filled keycap glyphs suggesting a physical key surface.

## Shapes

| Token | Value | Use |
|---|---|---|
| `rounded.none` | 0px | Hero band, nav, footer — full-bleed structural surfaces |
| `rounded.xs` | 4px | Keycap glyphs, badge-pro chips, small inline tags |
| `rounded.sm` | 6px | Command-palette row, inline buttons, micro chips |
| `rounded.md` | 8px | Standard buttons, text inputs, store search bar, app-icon tiles |
| `rounded.lg` | 10px | Feature card, command-palette mockup card, pricing tier card |
| `rounded.xl` | 16px | Large hero command-palette mockup container |
| `rounded.full` | 9999px | Pill-tab chips, avatar circles |

The radius vocabulary clusters tightly between 4 and 16px, with most
chrome at 6-10px — the system never goes flat on cards and never above
16px except fully-rounded pills. There's no traditional photography;
visual elements are command-palette mockups (16:9 or 4:3 inside 16px
containers), app-icon tiles (48-64px square at 8px radius), and 32-40px
avatar circles for extension-author attribution.

## Components

Full specs live in `design-tokens.yaml → components`. Summary:

- **Buttons** — `button-primary` (white pill, universal CTA), `button-
  secondary` (transparent text), `button-tertiary` (soft surface fill),
  `button-disabled`, `install-button` (outlined pill on store cards).
- **Filter & tab chips** — `pill-tab` / `pill-tab-active` (store filter
  strip), `badge-pro`, `badge-info-soft`.
- **Inputs** — `text-input` / `text-input-focused` (border brightens
  rather than a colored ring) and `store-search-bar` (44px, magnifier
  icon).
- **Cards & containers** — `command-palette-card` (the home-page hero
  mockup), `command-palette-row` / `-active` (selection state), `feature-
  card-dark` / `-elevated`, `store-extension-card`, `pricing-tier-card` /
  `-featured` (distinguished only by a surface-ladder notch).
- **Decorative** — `app-icon-tile` / `-large`, `keycap` (gradient-filled
  keyboard-shortcut glyph).
- **Navigation** — `primary-nav` (56px, centered link cluster, Download
  CTA pill on the right).
- **Footer** — `footer-section` (6-column link grid with a faint echo of
  the hero stripe at the very top).
- **Inline** — `link-inline` (full white, not a tinted accent — keeps the
  dark canvas tonally pure).

## Do's and don'ts

**Do**
- Render the entire site in one continuous dark mode — there's no light
  variant in the system.
- Use the white pill for every primary CTA — there's no second primary
  color.
- Build elevation from the surface-color ladder, never from drop shadows.
- Enable `font-feature-settings: "calt", "kern", "liga", "ss03"` on the
  body element — the ss03 alternate `g` is part of the brand identity.
- Anchor a command-palette mockup as the hero's load-bearing visual.
- Use keycap glyphs inline for keyboard shortcuts with the subtle key-bg
  gradient.
- Reserve the hero stripe gradient for the hero band exactly once per
  page.
- Use saturated category accents only inside extension/feature
  illustrations, never on chrome buttons or text.

**Don't**
- Don't introduce a light mode.
- Don't add drop shadows on cards.
- Don't replace the white primary CTA with a tinted accent.
- Don't use saturated accent colors on chrome text, buttons, or surfaces.
- Don't repeat the hero stripe gradient outside the top hero band.
- Don't use Inter without the ss03 feature flag enabled.
- Don't pad cards with 32px+ on all sides — the system runs tight at
  16-24px.

## Responsive behavior

| Name | Width | Key changes |
|---|---|---|
| desktop-large | 1440px | Default — 3-up pricing grid, 2-up store extension grid |
| desktop-small | 1024px | 3-up pricing → 2+1 |
| tablet | 768px | Pricing → 1-up stacked; nav becomes a hamburger drawer |
| mobile | 480px | Single-column; hero display scales 64px → ~36px |
| mobile-narrow | 320px | Section padding tightens to 48px |

Touch targets meet WCAG AA at 36px+: primary/tertiary buttons sit at 36px,
text inputs at 36px, the store search bar at 44px, pill tabs at ~24-28px
extending to 36-40px tappable via inline padding. The primary nav
collapses to a hamburger drawer at 768px while the white Download CTA
stays visible at every breakpoint; the store extension grid steps 2-up →
1-up; the pricing comparison table goes from a full 5-column desktop
layout to horizontal scroll at tablet and a vertical card stack at mobile.

## Known gaps

- Mobile screenshots weren't captured — responsive behavior is
  synthesized from desktop evidence and the documented breakpoint stack.
- Hover states aren't documented, per the source's own policy — the
  in-product app has rich hover behavior this document doesn't capture.
- The actual in-product Raycast launcher (full keybindings, panels,
  status bar) is referenced in marketing screenshots but isn't documented
  as its own UI system here.
- Dark mode is the only mode captured — no light variant exists in the
  source pages.
- Form validation states beyond the focused-input border aren't present.
- Authenticated chrome (account dashboard, billing, team management) isn't
  in the captured pages.
