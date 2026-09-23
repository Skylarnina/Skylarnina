# PostHog Design System — Full Analysis

Adapted from the PostHog marketing-site design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/posthog/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

PostHog's marketing system is built on a deliberate contradiction: a
serious open-source product-analytics platform, rendered as if it were a
friendly engineering sketchbook. The chrome sits on a warm cream canvas
(`colors.canvas`, `#eeefe9`) — never white — and every page carries
hand-drawn hedgehog mascots in lab coats, lounge chairs, terminals, and
reading glasses, scattered across the layout like marginalia in a
textbook. Type runs in IBM Plex Sans Variable, olive-gray (`colors.body`,
`#4d4f46`) for body and deep olive-charcoal (`colors.ink`, `#23251d`) for
headlines, with weights stepped tightly across 400/500/600/700/800 to
build hierarchy without leaning on color. The single saturated
yellow-orange pill (`colors.primary`, `#f7a501`) is the brand's only loud
chromatic moment — everything else stays cream, olive, white card, or an
occasional pastel callout.

The system has a distinctive two-mode body layout. Marketing pages (home,
workflows, pricing) lean on alternating-pastel callout bands and feature
tiles in white cards on cream, while documentation pages add a sticky
240px left sidebar with rounded outline-icon section navigation. Code
samples are full-width dark blocks on `colors.surface-dark` — the same
olive-charcoal that carries body ink, used inverted — nested inside white
doc cards, creating the system's most distinctive visual moment: a
dark-on-dark code island floating inside a white card on a cream canvas,
with a hedgehog doodled in the margin.

Sections stack at `spacing.section` (80px) with cream canvas continuing
uninterrupted between them. The only color bands that break the cream are
pastel tip/warning/success/info banners inside doc articles — soft tinted
boxes carrying "💡 Tip", "✅ Success", "⚠️ Warning", and "📘 Info"
annotations. There are no decorative gradients, no atmospheric mesh
backgrounds, and no full-bleed dark hero chapters; the cream canvas runs
top to bottom and the hedgehogs carry the entire visual identity.

**Key characteristics:**
- A warm cream canvas end-to-end with no surface alternation between
  sections — the page is one continuous sheet.
- A single yellow-orange CTA pill with deep-olive text — the system's only
  saturated color.
- IBM Plex Sans Variable across every role at weights 400/500/600/700/800
  — no other typeface anywhere.
- Hand-drawn hedgehog mascots as the entire decorative system — no
  gradients, no mesh, no atmospheric backgrounds.
- A 4-8px radius card vocabulary, with fully-rounded pills reserved for
  chips.
- Four pastel callout banners (blue/green/red/purple) that break up doc
  article body with soft tinted side rails.
- A sticky 240px doc sidebar with rounded outline-icon section nav and an
  "Ask PostHog AI" CTA at the top.

## Colors

> **Source pages:** home, pricing, a docs article (`/docs/product-
> analytics`), and a product feature page (`/workflows`). The chrome
> palette is identical across all four — doc-specific accents (callout
> pastels, the dark code-block surface) appear only inside the docs
> experience.

### Brand & accent
- **PostHog Yellow** (`#f7a501`) is the universal primary CTA — the sticky
  "Get started — free" pill, hero CTAs, pricing-tier subscribe buttons, and
  the footer signup pill.
- **Yellow Pressed** (`#dd9001`) and **Yellow Active** (`#b17816`) carry
  the pressed and deep-pressed states.

### Surface
- **Canvas** (`#eeefe9`) is the warm cream page background running
  end-to-end — the brand's most distinctive surface choice.
- **Surface Card** (`#ffffff`) is the true-white card/tile background
  sitting on top of cream — the dominant card surface.
- **Surface Doc** (`#fcfcfa`) is a faintly warm white used inside doc
  article body cards, kept slightly softer than pure white to stay
  tonally unified with the cream.
- **Surface Dark** (`#23251d`) is the deep olive-charcoal used inverted as
  code-block background — the same hex as ink, so one olive-near-black
  carries both text and dark code surfaces.

### Text
- **Ink** (`#23251d`) — headlines, button text on light, primary nav
  links.
- **Body** (`#4d4f46`) — the brand's most-used text color: default
  paragraphs, doc article body, inline links before hover.
- **Mute** (`#6c6e63`) — metadata, footer link text.
- **Ash** (`#9b9c92`) — disabled-state text.

### Semantic
Four pastel callout families, each with a saturated accent and a soft
background, appear only inside doc article body:
- **Blue** (`#2c84e0` / `#dceaf6`) — "💡 Tip / Info."
- **Red** (`#cd4239` / `#f7d6d3`) — "⚠️ Warning / Caution."
- **Green** (`#2c8c66` / `#d9eddf`) — "✅ Success / Positive."
- **Purple** (`#7c44a6` / `#e7d8ee`) — "📘 Note / Reference."
Two link colors — **Link Blue** (`#1d4ed8`) and **Link Teal** (`#1078a3`)
— cover general and doc-article inline anchors respectively.

## Typography

### Font family
**IBM Plex Sans Variable** is the system's only face, used at weights
400/500/600/700/800 across every role, falling back through `IBM Plex
Sans` → `-apple-system` → `system-ui`. **ui-monospace** and **Source Code
Pro** carry code samples and inline-code chips. The brand-distinctive
choice is the mixed weight ladder — most chrome lives in the 400-700 band,
with weight 800 reserved exclusively for the largest display headlines on
home and pricing — giving the system its "engineering blog" feel: weight
contrast does more work than size contrast.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale — display-xl at
36px/700 down through display-lg at 24px/800/-0.6px tracking, to
caption-xs and utility-xs at 12px. There's no italic style, no decorative
display variant, no proprietary face. Section eyebrows (`heading-sm` and
`utility-xs`) consistently render uppercase, giving the doc layout its
textbook-chapter feel.

### Font substitutes
IBM Plex Sans Variable is open-source and Google-Fonts-hosted, so no
substitute is generally needed. If one is required, **Inter** is the
closest geometric match at all five weights — pair with -0.5 to -0.6px
tracking on display sizes to approximate Plex's display tracking.
**JetBrains Mono** is a near-perfect substitute for Source Code Pro at
body sizes.

## Layout

- **Base unit:** 8px, with finer 2/4/6px steps for tight inline gaps in
  callouts and pill buttons.
- **Universal section rhythm:** `spacing.section` (80px) between major
  blocks; card grids use `spacing.lg` (16px) gutters; card padding sits at
  24px for product cards and 32px for pricing-tier cards.
- **Max width:** ~1280px at desktop; doc article body sits at ~720px with
  the 240px sidebar pushing the article column right of center.
- **Marketing card grid:** 4-up at desktop, 3-up at 1024px, 2-up at 768px,
  1-up at 480px.
- **Doc layout:** desktop 240px sticky sidebar + ~720px article + optional
  200px right TOC rail (~1160px total).

Whitespace is generous on marketing pages and tight on doc pages — home
and workflows stack feature tiles at 16px gutters with 24px internal
padding, while doc articles tighten to 12px between paragraphs to maximize
density. The cream canvas runs continuously; there are no decorative
dividers, no shaded section bands, only the 1px hairline under section
eyebrows and footer column rules.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 — Flat | No border, no shadow | Canvas-on-canvas blocks, hero text |
| 1 — Hairline border | 1px `hairline` | Marketing cards, pricing cards, doc sidebar items, footer rules |
| 2 — Hairline soft | 1px `hairline-soft` | In-card row divider |
| 3 — Inverted dark code block | `surface-dark` fill | Code samples — the only "elevated" surface uses color, not shadow |

The system has no drop-shadow elevation anywhere in marketing or product
chrome — cards sit flat on cream with thin olive borders. The single
inverted moment is the dark code-block surface inside doc cards.
Decorative depth otherwise comes entirely from illustration: hand-drawn
hedgehog mascots (always flat-color, never photographic), the four pastel
callout banners, and small rounded-square outline product icons marking
each major section in the doc sidebar.

## Shapes

| Token | Value | Use |
|---|---|---|
| `rounded.none` | 0px | Sub-nav strip, footer, doc sidebar, primary nav |
| `rounded.xs` | 2px | Inline `<code>` chips, micro-rule highlights |
| `rounded.sm` | 4px | Inline buttons, form inputs, micro chips |
| `rounded.md` | 6px | Marketing cards, pricing cards, doc cards, code blocks, every standard CTA |
| `rounded.lg` | 8px | Tab top corners, rare large containers |
| `rounded.full` | 9999px | Pill chips, the sticky "Get started — free" nav CTA |

The radius vocabulary clusters around 4-6px for nearly everything; the
only fully-rounded elements are the pill-style sticky nav CTA and inline
pill chips. There's no photography in the system — visual elements are
limited to flat-color hedgehog illustrations (80-240px), 20-24px outline
product icons in the doc sidebar, and inline emoji used as functional
iconography inside callout banners.

## Components

Full specs live in `design-tokens.yaml → components`. Summary:

- **Buttons** — `button-primary` (yellow, universal CTA), `button-
  secondary` (soft cream fill), `button-tertiary` (ghost text), `button-
  disabled`.
- **Tabs & chips** — `product-tab` / `product-tab-active` (major product
  sections, card lift on selection), `pill-tab` / `pill-tab-active`
  (compact filter, fully inverted when active), `badge-uppercase`,
  `badge-promo`.
- **Inputs** — `text-input` / `text-input-focused` (2px blue border +
  translucent focus ring) and `search-input` (doc sidebar / "Ask PostHog
  AI").
- **Cards & containers** — `product-card`, `doc-card`, `feature-tile`,
  `pricing-tier-card`, `hedgehog-mascot-card` (the signature card variant
  with a margin-anchored hedgehog).
- **Callout banners** — `banner-tip-blue` / `-green` / `-red` / `-purple`,
  each prefixed with an emoji icon, appearing only inside doc article body.
- **Code** — `code-block` (dark, muted syntax highlighting) and
  `inline-code` (small cream chip).
- **Navigation** — `primary-nav` (56px, cream, yellow CTA anchored right),
  `sub-nav-strip` (40px secondary bar), `doc-sidebar` (240px sticky,
  search + outline-icon section list).
- **Footer** — `footer-section` (6-column link grid with uppercase
  headers).
- **Inline** — `link-inline` (link-teal, no underline by default).

## Do's and don'ts

**Do**
- Use the cream canvas as the page body — never substitute pure white.
- Reserve the yellow-orange CTA pill for the primary action only.
- Render the wordmark alongside the hedgehog illustration, not as a
  stand-alone wordmark — the hedgehog IS the brand identity.
- Use IBM Plex Sans Variable across every role — body 400, emphasis
  600/700, display 800.
- Stack sections at the 80px rhythm with no decorative dividers; let the
  cream canvas continue uninterrupted.
- Use the four callout-banner colors only inside doc article body, never
  on marketing chrome.
- Pair every code sample with the dark code-block surface; use the cream
  inline-code chip for inline snippets.
- Anchor a hedgehog mascot illustration in feature-tile margins as the
  signature decoration.

**Don't**
- Don't introduce drop shadows on cards — they sit flat with thin olive
  borders only.
- Don't add a second saturated chromatic CTA — yellow-orange is the only
  loud color in the system.
- Don't replace cream with pure white or a full-bleed dark hero band.
- Don't use the callout-banner pastels as marketing-card backgrounds.
- Don't substitute the hedgehog illustration with a generic icon set.
- Don't use uppercase transform outside eyebrows and footer category
  headers.
- Don't pad standard cards beyond 24px — only the pricing-tier card goes
  to 32px.

## Responsive behavior

| Name | Width | Key changes |
|---|---|---|
| desktop-large | 1440px | Default — 4-up feature grid, 240px sticky doc sidebar |
| desktop-small | 1024px | 4-up tiles → 3-up |
| tablet | 768px | 3-up → 2-up; doc sidebar collapses to a top accordion; nav becomes hamburger |
| mobile | 480px | Single-column; hero display scales 36px → ~28px |
| mobile-narrow | 320px | Section padding tightens to 32px |

Touch targets meet WCAG AA (≥40×40px): primary/secondary buttons at 40px,
text inputs at 36px, pill tabs extending to ~44px tappable via inline
padding, doc-sidebar items reaching ~44px through line-height plus
padding. The nav's yellow CTA stays visible at every breakpoint; the doc
sidebar collapses from a persistent 240px column to a top accordion at
tablet and below. Hedgehog illustrations are inline SVG, so they scale
without any responsive art-direction cropping — there's no photography in
the system that would need it.

## Known gaps

- Mobile screenshots weren't captured — responsive behavior is synthesized
  from desktop evidence and the documented breakpoint stack.
- Hover states aren't documented, per the source's own policy.
- The in-product app (dashboard, charts, session-replay player) isn't in
  the captured set — only the marketing site is documented here.
- Authenticated chrome (login modal, account dashboard, billing) isn't in
  the captured pages.
- Form validation states beyond the focused-input treatment aren't
  present.
- The full hedgehog illustration library isn't enumerated — specific
  poses are noted from screenshots but the complete asset set is
  page-specific.
