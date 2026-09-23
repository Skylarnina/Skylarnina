# NVIDIA Design System — Full Analysis

Adapted from the NVIDIA design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/nvidia/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

NVIDIA's marketing system is built like engineering documentation that
learned graphic design — every page is a structured cascade of dense,
factual information on a paper-white grid, framed top and bottom by deep
black hero/footer chapters. There is exactly one accent color in the entire
system, and it does all the work: NVIDIA Green (`colors.primary` — #76b900),
used for every primary CTA, every active tab, every link affordance on dark
surfaces, and the small decorative corner squares that mark card containers.
Nothing else competes for attention.

The system's character comes from extreme typographic restraint and an
almost punishing angular geometry. Every container, button, and image uses
`rounded.sm` (2px) — a value that's barely there but never zero, giving the
system the precise, technical feel of CAD output rather than warm consumer
software. Cards sit on plain white with a hairline border (no shadow, no
elevation), separated by a tight 8px-base spacing rhythm. Long-form pages
stack six to ten of these cards into multi-column technical grids without
ever introducing a decorative break.

The black-canvas hero and footer chapters are the system's "headline
moments" — a single full-bleed photographic or 3D-rendered image with a
white 48px display headline, a single green CTA button, and a small green
corner square as the only ornamentation. Everything else is subordinate.

**Key characteristics:**
- Single-accent system: `colors.primary` carries every CTA, active state,
  and decorative motif — the rest is monochrome black/white/gray.
- Two-mode surface architecture: `colors.surface-dark` for hero/footer
  chapters, `colors.canvas` for body — alternating in a predictable rhythm
  down the page.
- Hyper-angular geometry: `rounded.sm` (2px) on every interactive element.
  There are no pill buttons, no rounded cards, no soft chrome.
- NVIDIA-EMEA proprietary sans-serif at weights 400 and 700, scaled across a
  twelve-tier hierarchy from `typography.utility-xs` (10px) up to
  `typography.display-xl` (48px).
- Card library leans on hairline borders and soft surfaces rather than
  shadows for separation.
- Signature decorative element: the small corner-square component (~12px
  green square) anchored to one corner of resource and feature cards.
- Dense multi-column footer with 4–6 link columns on the dark surface —
  every page closes with the same structured global navigation.

## Colors

> Source pages: `/tr-tr/` (primary homepage), `/en-eu/industries/
> healthcare-life-sciences/`, `/en-eu/solutions/ai/`, `/en-eu/ai/foundry/`.
> The chrome palette is identical across all four — only photography and
> copy vary.

### Brand & accent
- **NVIDIA Green** (`colors.primary` — #76b900): the brand. Every primary
  CTA, every active state, every link affordance on dark surfaces, every
  corner square, and the brand wordmark itself.
- **NVIDIA Green Dark** (`colors.primary-dark` — #5a8d00): pressed state for
  the primary button — one notch deeper than the brand green.
- **Accent Green Pale** (`colors.accent-green-pale` — #bff230): a rare
  highlight tint used in editorial callouts and decorative micro-blocks;
  never on chrome.

### Surface
- **Page Canvas** (`colors.canvas` — #ffffff): the body of every page.
  Cards sit directly on it with hairline rules.
- **Soft Surface** (`colors.surface-soft` — #f7f7f7): breadcrumb strip,
  sub-nav, side-by-side comparison panels, alternating row backgrounds.
- **Black Canvas** (`colors.surface-dark` — #000000): hero chapter, dark CTA
  strips, footer, primary nav — the system's "frame" color.
- **Surface Elevated** (`colors.surface-elevated` — #1a1a1a): nested dark
  panels inside the footer (column dividers, fine-print bar).
- **Hairline** (`colors.hairline` — #cccccc): 1px card border, table rule,
  divider between footer link sections.
- **Hairline Strong** (`colors.hairline-strong` — #5e5e5e): 1px divider on
  dark surfaces (footer column rules, dark-mode card edges).

### Text
- **Ink** (`colors.ink` — #000000): headlines and body text on canvas.
- **Body** (`colors.body` — #1a1a1a): long-form paragraph text where pure
  black is too heavy.
- **Mute** (`colors.mute` — #757575): metadata, breadcrumb separators,
  footer copyright.
- **Stone** (`colors.stone` — #898989): least-emphasis text and disabled
  state.
- **Ash** (`colors.ash` — #a7a7a7): disabled icon color and faint utility
  text.
- **On Dark** (`colors.on-dark` — #ffffff): primary text on the dark
  surface.
- **On Dark Mute** (`colors.on-dark-mute` — rgba(255,255,255,0.7)):
  secondary footer link text and dark-canvas body copy.

### Semantic
- **Error** / **Error Deep**: validation messages, destructive
  confirmation, and its pressed state.
- **Warning** / **Warning Bright**: caution callouts and an inverse variant
  for dark canvas.
- **Success Deep**: positive confirmation where the brand green's
  saturation would clash.
- **Link Blue** (`colors.link-blue` — #0046a4): the only blue in the
  system, reserved for prose-embedded inline hyperlinks on light canvas.

### Editorial accents (used sparingly inside long-form content)
- **Accent Purple** / **Accent Purple Deep** / **Accent Purple Pale**:
  research and scientific-computing editorial accent.
- **Accent Yellow Pale**: documentation tip / soft callout fill.

## Typography

### Font family
**NVIDIA-EMEA** is the proprietary brand sans-serif used across every text
role, carrying weights 400 (regular) and 700 (bold), falling back to Arial
then Helvetica. **Font Awesome 6 Pro/Sharp** handle iconography exclusively
(chevrons, social glyphs, breadcrumb separators, search/menu icons) at
14–22px.

The type system is unusually flat: most chrome and body roles render at the
same line-height (1.25–1.5), with the only meaningful variation coming from
weight (400 vs 700) and size. Weight contrast — not size jumps, not color
tinting — establishes hierarchy, giving marketing copy and technical
documentation an editorial newspaper feel.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale (display-xl 48px
down to utility-xs 10px). The typography is brand-locked: NVIDIA-EMEA at
every level, no serif, no display variant, no monospace, no italic.

### Note on font substitutes
NVIDIA-EMEA is proprietary. **Inter** (weights 400/700) is the closest
open-source pairing — its x-height and stroke contrast match NVIDIA-EMEA's
optical metrics within roughly 2% at body sizes. **Arial** is the official
documented fallback. Avoid Helvetica Now or Helvetica Neue substitutes;
their tighter cap heights drift from the brand's geometry.

## Layout

### Spacing system
- Base unit: 8px.
- Tokens: `spacing.xxs` (2px) through `spacing.section` (64px).
- Every page uses `spacing.section` (64px) as the vertical gap between major
  content blocks. Card grids use 24px gutters; in-card padding runs 24–32px
  depending on density.
- Hero chapter padding: 80px vertical / 48px horizontal — the largest
  spacing in the system, reserved for the dark hero card.

### Grid & container
- Max width ~1280px at desktop, with 24px gutters growing to ~48px at
  ultrawide.
- Card grids: 4-up at desktop, 3-up at 1024px, 2-up at 768px, 1-up at
  480px.
- Long-form text: a 60/40 body-plus-sidebar split at desktop, collapsing to
  single-column below 960px.
- Footer: 6-up link columns at desktop, collapsing to 2-up on tablet, full
  accordion on mobile.

### Whitespace philosophy
Whitespace is structural, not atmospheric. Sections butt against each other
with the 64px section rhythm — there are no decorative dividers, no empty
"breathing room" bands, no gradient transitions between sections. The sense
of air comes from white body sections sandwiched between black chapter
blocks, not from generous padding inside any one component.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 — Flat | No border, no shadow | Canvas-on-canvas blocks, hero chapter content, footer column body |
| 1 — Hairline border | 1px solid hairline | All cards on canvas, table cells, comparison panels |
| 2 — Hairline strong | 1px solid hairline-strong | Dividers on the dark surface (footer column rules, dark-card edges) |
| 3 — Soft shadow | `0 0 5px 0 rgba(0,0,0,0.3)` | Sticky nav bottom edge when scrolled, sticky CTA bar — used very sparingly |

The system has effectively no drop-shadow elevation in card or content
surfaces. The only "shadow" in the extracted tokens is a subtle 5px ambient
on sticky chrome bars. Cards do not lift; they are flat rectangles with
hairline borders.

Depth otherwise comes from photography and 3D-rendered hero imagery rather
than from CSS effects: full-bleed scenes (data-center hardware, neural-net
visualizations, life-sciences microscopy) sit behind hero copy with a dark
gradient overlay for legibility, and the corner-square motif anchors card
containers. Isometric or wireframe 3D renderings appear as illustration
fills inside long-form articles, never as chrome.

## Shapes

| Token | Value | Use |
|---|---|---|
| rounded.none | 0px | Hero chapter, footer, dark CTA strips, primary nav |
| rounded.xs | 1px | Decorative micro-rules and inset accent strips |
| rounded.sm | 2px | Every interactive element — buttons, cards, inputs, pill tabs, badges |
| rounded.full | 9999px / 50% | Avatar circles, social-icon dots, brand wordmark icon |

The system is aggressively angular. Outside of avatar/icon circles, no
element exceeds 2px radius — enough to soften optical aliasing on a sharp
edge, but small enough to read as engineering-grade rather than
consumer-friendly.

## Components

Definitions live in `design-tokens.yaml → components`. Summary:
- **Buttons** — `button-primary` (the universal green CTA, pressed state
  deepens to primary-dark), `button-outline` (green-bordered secondary),
  `button-outline-on-dark` (white-on-black variant), `button-ghost-link`
  (inline arrow link), `button-disabled`.
- **Tabs & chips** — `pill-tab` / `pill-tab-active` (inverts fully on
  selection), `badge-tag` (uppercase document-type label).
- **Inputs & forms** — `text-input` / `text-input-focused` (green border is
  the only focus signal), `search-input`.
- **Cards** — `product-card`, `feature-card`, `resource-card` (all carry the
  corner-square motif), `callout-stat` (massive green numeric stat).
- **Hero & CTA strips** — `hero-card-dark` (anchors the top of every primary
  landing page), `cta-strip-dark` (compressed "Ready to get started?"
  bridge band).
- **Decorative** — `corner-square` (the signature 12×12px green square).
- **Navigation** — `utility-bar` (locale/login row above the main nav),
  `primary-nav`, `breadcrumb-bar`, `sub-nav-strip`.
- **Footer** — `footer-section` (6-column link grid plus legal fine-print
  row).
- **Inline** — `link-inline` (the only blue in the system).

## Do's and don'ts

**Do**
- Reserve NVIDIA Green for primary CTAs, active states, decorative corner
  squares, and the wordmark itself — treat it as a precious resource.
- Stack hero/footer chapters in black and body sections in white,
  alternating in a predictable rhythm down the page.
- Anchor a corner-square component to one corner of every reusable card —
  it is the system's identity tag.
- Use `rounded.sm` (2px) on every interactive element; never go to 0, never
  go past 4.
- Build hierarchy from font weight (400 vs 700) and size, not from color
  tinting; body text stays ink or body regardless of context.
- Stack content sections at `spacing.section` (64px) rhythm with no
  decorative dividers between them.
- Pair the primary button (green fill) with the outline button (green
  border) for primary + secondary action pairs.

**Don't**
- Don't introduce drop shadows on cards or content surfaces. The only
  allowed shadow is the 5px ambient on sticky chrome.
- Don't substitute success-deep, accent-green-pale, or any other green for
  the brand primary in CTAs — the brand green is precise.
- Don't use link-blue outside of inline body-prose links. It is not a
  button color, not a chrome color.
- Don't soften the geometry — no pill buttons, no rounded cards, nothing
  above `rounded.sm` except avatars and social icons.
- Don't pad the dark hero card symmetrically — copy hugs the left third,
  imagery fills the right.
- Don't add a second accent color for variety. The system is intentionally
  one-color.
- Don't place the primary button on a canvas background where green-on-white
  would clash with photo content — use the outline button instead and
  reserve fill for dark surfaces.

## Responsive behavior

| Name | Width | Key changes |
|---|---|---|
| ultrawide | 1920px+ | Content max-width holds at 1280px; outer gutters grow to ~80px |
| desktop-large | 1440px | Default desktop layout — 4-up card grid, 6-col footer |
| desktop | 1280px | Same as large with slightly narrower outer gutters |
| desktop-small | 1024px | 4-up cards collapse to 3-up; sub-nav remains horizontal |
| tablet | 768px | 3-up cards collapse to 2-up; primary nav becomes a hamburger drawer |
| mobile | 480px | Single-column everything; footer columns collapse to accordion |
| mobile-narrow | 320px | Hero display headline scales from 48px down to 32px |

All interactive elements meet WCAG AA (≥ 44×44px). The primary button sits
at 44px height with 24px horizontal padding; the text input at 44px; the
pill tab at ~40px with extended hit-target padding to 44px; the outline
button matches the 44px standard.

Collapsing strategy: primary nav collapses to a hamburger drawer at 768px;
card grids step 4→3→2→1 at 1024/768/480px with gutters dropping from 24px to
16px on mobile; the footer steps 6-up → 2-up → full accordion; hero copy
scales 48→36→32px with line-height holding at 1.25; the sub-nav strip goes
from a horizontal anchor row to horizontal scroll to a select dropdown on
mobile; section padding steps 64→48→32px.

Hero imagery uses art-direction crops (16:9 wide on desktop, 4:5 portrait on
mobile). Card imagery is a fixed aspect (16:9 for resource, 1:1 for product)
that scales rather than re-crops between breakpoints. Non-critical imagery
is lazy-loaded as the user scrolls into the next grid row.

## Known gaps

- Mobile screenshots were not captured — responsive behavior synthesizes
  NVIDIA's known mobile pattern from desktop evidence and the documented
  breakpoint stack.
- Hover states are not documented, per the source analysis's system policy.
- Dialog/modal styling beyond the locale-selector overlay was not visible in
  the captured surfaces.
- Full sign-up/contact form field styling is not present in the captured
  surfaces — only inline search and basic text inputs are documented.
- Login / authenticated chrome is not in the captured pages.
