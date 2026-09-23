# SpaceX Design System — Full Analysis

Adapted from the SpaceX marketing-site design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/spacex/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

SpaceX's design language works by subtraction. The canvas is pure black
(`colors.canvas-night`, `#000000`), display type is white and uppercase with
tight vertical leading, and every band is a single full-bleed photograph or
autoplaying rocket-launch video — there are no decorative shapes, no pricing
tables, and no card grids on the marketing pages. The composition reads closer
to a film title card than a typical SaaS landing page: one huge headline, one
ghost-outlined pill CTA, one photograph filling the frame.

The brand's sense of depth comes entirely from the photography itself — Mars
terrain, exhaust plumes, a booster lit at sunset. Type sits directly on top of
these images at full opacity; there's no gradient overlay or scrim, because the
source photographs are graded dark enough for the type to read cleanly on
their own. When type does need a background (rather than sitting on a photo),
it drops onto `colors.canvas-night-soft`, a barely-lifted near-black, edged
with a 1px `colors.hairline-on-dark` line.

Two cuts of one typeface carry the whole system: **D-DIN-Bold** for every
display size, and regular-weight **D-DIN** for body copy and button labels.
Nothing else appears, not even on the shop site's pricing. The display sizes
compress vertically (line-height 0.95–1.25) while tracking pushes wide and
positive (up to 1.6px at 80px) — the net effect reads as engineered rather
than typeset.

**Key characteristics:**
- One canvas only: pure black for marketing; the shop site is the sole
  exception, switching to white.
- Every display headline is uppercase D-DIN-Bold with positive tracking — the
  brand's clearest typographic signature.
- Full-bleed photography or autoplaying video is the only decorative element;
  type sits straight on the image with no scrim.
- A single ghost-outlined 32px pill CTA per band — never filled, never
  accent-colored.
- Chrome text (eyebrows, button labels) is always uppercase with 0.96–1.17px
  tracking.
- The top nav floats over photography with no opaque background at all.
- Vertical compression (0.95 line-height at 80px) is treated as part of the
  "engineered" aesthetic, not a rendering accident.

## Colors

> Source pages: home (`/`), `/shop`, `/vehicles/starship`,
> `/humanspaceflight/overview`, `/mission`.

### Brand & accent
There is no accent color in this system. Black and white handle every
chromatic need; whatever color appears comes from the photograph itself.

### Surface
- **Canvas night** — the default black marketing surface, no tint at all.
- **Canvas night soft** — a barely-lifted near-black for sections that need
  slight separation from a pure-black hero.
- **Canvas light** — reserved for the shop site's product pages.
- **Canvas cool** — a pale cool-blue-white used as the shop site's secondary
  surface and on certain ghost-button hover states.
- **Hairline on dark / on light** — 1px border tiers for dark and light
  contexts respectively.

### Text
- **On primary** — white, the dominant text color across marketing.
- **On primary mute** — a barely-cooled white for secondary text on dark
  surfaces.
- **Ink / ink mute** — black and mid-grey text, used only on the light shop
  surface.

### Link
- **Link on dark** — white with a persistent underline.
- **Link blue fallback** — the browser-default blue, documented only for
  completeness, not an intentional brand color.

## Typography

### Families
- **D-DIN-Bold** — a condensed industrial sans (DIN 1451-inspired) for every
  display tier, always uppercase. Fallback chain: Arial Narrow → Arial →
  Verdana, prioritizing width compression.
- **D-DIN** regular — body copy, button labels, captions.

Substitute with **Inter** at 700 weight, uppercase, `letter-spacing: 1.6px`,
`line-height: 0.95` for display sizes if D-DIN is unavailable. Avoid default
Helvetica/Arial weights or any serif fallback — the condensed industrial cut is
part of the brand.

### Hierarchy
See `design-tokens.yaml → typography` for exact values (display-xxl 80px down
to caption 13px). Principles:
- Every display tier is uppercase — sentence-case headlines never appear.
- Vertical leading stays unusually tight on display (0.95 at 80px).
- Tracking runs wide and positive (0.96–1.6px on display and caps eyebrows).
- No monospace face exists in this system; code isn't part of the brand.

## Layout

- Base spacing unit: 8px, with 4/12/16/18/24 sub-steps for finer control.
- Marketing sections carry no internal padding at all — the photograph fills
  the section edge to edge. The shop site alone uses 48–64px vertical padding.
- No container constrains marketing bands; they're full-viewport width and
  height. Type sits inside an inner ~1200px column centered over the image.
- Shop product grid: 4-up desktop → 2-up tablet → 1-up mobile.
- "Whitespace" on marketing pages is photographic — the dark sky in a rocket
  shot, the empty stretch of Martian terrain — rather than a UI decision.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 | Flat | Default, and the only level marketing surfaces use |
| 1 | Photographic (full-bleed image/video) | The system's entire depth medium |

There are no drop shadows, blurs, glows, or gradient overlays anywhere.
Depth is achieved by the photograph's own atmosphere — a twilight rocket
launch already has more depth than any CSS shadow could add. When type needs
separation from an image, the image is graded darker rather than scrimmed.

### Decorative depth
Photography and autoplaying video are the only decorative elements. A few
minimal SVG chevrons appear in nav and CTA hover states — nothing else.

## Shapes

| Token | Value | Use |
|---|---|---|
| rounded.xs | 4px | Shop-site form inputs |
| rounded.sm | 8px | Shop product card chrome, video frames |
| rounded.md | 16px | Larger surface chrome |
| rounded.pill | 32px | Ghost-outlined pill CTAs — the brand's signature button |
| rounded.full | 9999px | Circular play-button overlays on video frames |

Photography is always full-viewport-bleed on marketing pages — never inset in
a card. On the shop site, product photography sits in 8px containers with no
shadow, and aspect ratios follow the source image rather than a fixed ratio.

## Components

Definitions live in `design-tokens.yaml → components`. Summary:
- **Buttons** — `button-ghost-on-dark` (the universal marketing CTA: 1px white
  outline, transparent fill, 32px pill), its light-canvas twin
  `button-ghost-on-light`, and a filled `button-filled-cool` reserved for shop
  "Add to cart" actions.
- **Cards** — `card-photo-band` (a full-bleed photographic band with zero
  padding) and `card-shop-product` (8px radius, 16px padding, hairline
  border).
- **Inputs** — `text-input` on the shop site only, 4px radius.
- **Navigation** — `nav-bar-overlay`, a transparent bar floating over hero
  photography with the wordmark left and caps nav items right.
- **Footer** — `footer-dark`, dense uppercase link columns on black.

## Do's and don'ts

**Do**
- Use full-bleed photography or autoplaying video as the dominant decorative
  element on every marketing band.
- Render every display tier in uppercase D-DIN-Bold with positive
  0.96–1.6px tracking.
- Use exactly one `button-ghost-on-dark` per band — never two CTAs side by
  side on marketing surfaces.
- Grade the photograph rather than scrimming the canvas when type needs
  contrast.
- Keep nav overlay-style: transparent, white text over the image.

**Don't**
- Don't introduce any brand accent color — black, white, and photography are
  the entire palette.
- Don't add drop shadows or gradient overlays on the dark canvas.
- Don't set display tiers in sentence-case or title-case.
- Don't put filled buttons on marketing surfaces — ghost pills only.
- Don't reach for serif or humanist sans substitutes.

## Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Wide | ≥1500px | Full hero photograph; type column caps at 1200px |
| Desktop | 1280–1499px | Default desktop layout |
| Laptop | 961–1279px | Type column tightens; photo crop adjusts |
| Tablet | 768–960px | Display drops 80 → 60px; nav compresses |
| Mobile | 600–767px | Display drops to 48px; pill CTA keeps its shape |
| Small mobile | <600px | Display drops to 40px; nav becomes hamburger |

Ghost pill buttons clear ~50×50px from their 18px vertical padding, meeting
WCAG AAA. Form fields hold the 44px minimum. Photography re-crops toward the
focal subject at smaller widths using `srcset` art-direction; the top nav
collapses to a hamburger below 768px while keeping its dark overlay look, and
the shop grid stair-steps 4-up → 2-up → 1-up.

## Known gaps

- No structural gradient or atmospheric-color system exists — this is
  intentional, not an omission.
- Form validation/error styling on the shop site wasn't visible on the
  inspected pages.
- D-DIN is proprietary; the documented Inter substitute approximates but does
  not exactly reproduce its condensed metrics.
