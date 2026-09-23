# Lamborghini Design System — Full Analysis

Adapted from the Lamborghini design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/lamborghini/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Lamborghini's site behaves like a digital stage where jet-black surfaces
stretch infinitely and every element seems to emerge from the void under a
spotlight. The canvas is not dark gray or near-black — it is true, flat
`colors.canvas` (`#000000`), and into that abyss only two colors are ever
deployed: white type and Lamborghini Gold (`colors.primary`, `#FFC000`).
The hero is typically a full-viewport (100vh) video — event footage or
vehicle reveals — with the bull logo floating above a navigation that has no
borders, no background fill, and no visible container; it is simply white
marks in darkness. The mood throughout is nocturnal luxury: exclusive,
theatrical, and intentionally intimidating.

Typography carries the brand's voice entirely. `LamboType`, a custom
Neo-Grotesk built by Character Type with design agency Strichpunkt, runs
everything from 120px uppercase hero display down to 10px micro labels. Its
12° angled terminals echo the aerodynamic lines of Lamborghini's cars, and
its underlying hexagonal geometric construction (hexagons, three-armed
stars, circles) resurfaces in UI elements like the hexagonal video-pause
button. Headlines are always uppercase and set at weight 400 (never bold) —
the face itself is distinctive enough that bold emphasis isn't needed —
with dense, tightly-leaded blocks (line-height as low as 0.92 at 120px)
that feel stamped from steel rather than typeset. The technical
infrastructure underneath is a Bootstrap grid with roughly 68 Element
Plus/UI components, but none of that shows through the theatrical surface.

**Key characteristics:**
- True black (`colors.canvas`) dominant surfaces; white and gold are the
  only relief colors.
- LamboType's 12° angled terminals and hexagonal geometric DNA recur across
  typography and UI icons alike.
- Gold is the sole accent — used exclusively on primary CTA buttons, never
  decoratively.
- All display type is uppercase, at extreme scale (120px/80px/54px) with
  tight line-heights.
- Full-viewport cinematic video heroes carry the emotional weight; UI is
  infrastructure, not decoration.
- Zero border-radius on every button and card — sharp, angular rectangles
  echo the vehicles' lines.
- Transparent "ghost" buttons (white border at 50% opacity) are the
  standard secondary CTA on dark backgrounds.

## Colors

### Primary
- **Lamborghini Gold** (`colors.primary`) — the signature accent, a warm
  saturated amber-gold used exclusively for primary action buttons
  ("Discover More", "Tickets", "Start Configuration"). It is the only
  chromatic color in the entire interface.
- **Pure White** (`colors.on-dark`) — primary text on dark surfaces, logo
  rendering, nav elements, and light-mode button fills.

### Secondary & accent
- **Dark Gold** (`colors.primary-hover`) — the hover/pressed state for gold
  buttons, a deep amber that signals interaction.
- **Gold Text** (`colors.primary-text-variant`) — a lighter gold used for
  inline text accents and highlighted labels.
- **Cyan Pulse** (`colors.cyan-pulse`) — an electric blue-cyan informational
  accent and interactive highlight.
- **Link Blue** (`colors.link-blue`) — the universal link-hover color
  across all text colors.

### Surface & background
- **Absolute Black** (`colors.canvas`) — the dominant surface for page
  background, hero, header, footer, and most containers.
- **Charcoal** (`colors.charcoal`) — the primary elevated dark surface for
  cards, panels, and text containers.
- **Dark Iron** (`colors.dark-iron`) — a subtler surface variant, barely
  distinguishable from black, used for footer and deep sections.
- **Overlay Black / Mid / Mist** — semi-transparent overlays for modals,
  video dimming, and hover states at descending opacities.
- **Near White / Mist Surface** — rare light surfaces reserved for
  occasional white-mode content blocks.

### Neutrals & text
A full gray ramp — **Smoke, Graphite, Ash, Steel, Slate, Iron, Shadow
Text** — carries secondary text, muted labels, and body copy on both dark
and light surfaces. All are achromatic; none carry color tint.

### Semantic & accent
- **Cyan Pulse** and **Link Blue** double as informational/interactive
  feedback colors.
- **Teal Action** (`colors.teal-action-hover`) is the hover background for
  transparent/ghost buttons.

### Gradient system
There are no explicit UI gradients. The dark-to-light progression is
achieved purely through surface layering — `#000000` → `#181818` →
`#202020` → `#494949` → `#7D7D7D` — and any atmospheric gradients come
from the video/photography content itself, not CSS.

## Typography

### Family
- **Display & UI**: `LamboType` (Roboto, Helvetica Neue, Arial fallback) —
  Character Type's custom Neo-Grotesk for Lamborghini's 2024 brand
  refresh, spanning Normal to Ultracompressed widths and Light to Black
  weights, with 12° angled terminals, hexagonal construction logic, and
  200+ language support. No italic variants appear anywhere on the
  marketing site — the voice is always upright.
- **Fallback/UI**: `Open Sans`, used as a system fallback in some
  button/form contexts.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale (120px hero
display down to 10px micro labels). Principles:
- **Uppercase is the default voice** — display and feature headings are
  universally uppercase, giving the brand a commanding, shouting tone.
- **Extreme scale range** — a 12:1 ratio from 120px heroes to 10px micro
  text drives dramatic hierarchy.
- **Tight line-heights at scale** — 0.92 to 1.19 on display sizes creates
  dense, compressed, "stamped" type blocks.
- **Weight 400 dominates** — regular weight carries the headlines; the
  typeface's distinctiveness makes bold unnecessary.
- **Negative tracking on captions** (-0.42px at 14px) creates a
  compressed, technical feel.
- **Positive tracking on micro text** (+0.225px at 10px) preserves
  legibility at the smallest sizes.
- A single typeface — LamboType — handles every size, giving the system
  total visual coherence.

## Layout

### Spacing
- **Base unit**: 8px.
- **Full scale**: 2, 4, 5, 8, 10, 12, 15, 16, 20, 24, 32, 40, 48, 56px.
- Button padding: 16px on ghost buttons, 24px on the gold accent CTA.
- Section padding: 48–56px vertical, 40px horizontal.
- Fine spacing (2–5px) handles badge padding and border adjustments.

### Grid & container
- Built on Bootstrap's standard 12-column grid (container + row + col).
- Max content width 1440px at the largest breakpoint.
- Hero sections break out of the grid to fill the viewport edge-to-edge;
  regular content areas center within a 1200px max-width container.

### Whitespace philosophy
Lamborghini uses darkness itself as whitespace. Generous black expanses
between content blocks perform the same role that white space performs in
a light design — they elevate each element to the status of an exhibit. A
model name floating in a black viewport carries the same visual weight as
a gallery piece on a white wall. The absence of color is itself the
design decision.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 (Abyss) | `#000000` flat | page background, deepest layer |
| 1 (Surface) | `#181818` or `#202020` | cards, content panels, elevated sections |
| 2 (Overlay) | `rgba(0,0,0,0.7)` | modal backdrops, video dimming |
| 3 (Fog) | `rgba(0,0,0,0.5)` | lighter overlays, hover states |
| 4 (Mist) | `rgba(0,0,0,0.25)` | subtle depth hints |

### Shadow philosophy
Depth comes from surface-color layering, not drop shadows — on a black
canvas, traditional shadows are effectively invisible. Instead, elevated
elements are literally lighter than their surroundings as the palette steps
from `#000000` → `#181818` → `#202020` → `#494949`, inverting the usual
shadow model: lighter means "closer."

### Decorative depth
Full-bleed video supplies atmospheric depth through cinematic lighting; the
hexagonal pause button floats with a thin white outline stroke; a thin
progress bar at the base of hero sections creates a subtle horizon line.
There are no gradients, glows, or blur effects on UI elements — photography
alone provides visual richness.

## Shapes

| Token | Value | Use |
|---|---|---|
| `rounded.none` | 0px | default for everything — buttons, cards, containers, images |
| `rounded.span` | 1px | subtle inline span elements |
| `rounded.badge` | 2px | badges, close buttons, cookie elements — barely perceptible |
| `rounded.toggle` | 20px | toggle switches only — the sole rounded element in the system |

## Components

Definitions live in `design-tokens.yaml → components`. Summary:
- **Gold Accent CTA** — the primary action button; gold fill, black text,
  24px padding, zero radius, darkens to `primary-hover` on interaction.
- **Transparent Ghost** — the secondary action on dark backgrounds; 1px
  white border at 50% opacity, shifts to teal-tinted fill at 70% opacity
  on hover, with a black-outlined focus state.
- **White Filled / Black Filled / Gray Neutral** — light-mode and inverted
  CTA variants for use on lighter sections.
- **Cards & containers** — charcoal (or black) background, zero radius,
  thin bottom-border dividers instead of card outlines; content is
  full-bleed photography with overlaid white text.
- **Hexagonal pause button** and **progress bar** — the two signature
  decorative components echoing the brand's angled, geometric DNA.
- **Toggle switch** and **badge/tag** are the only two components that
  break the zero-radius rule (20px and 2px respectively).

## Do's and don'ts

**Do**
- Use absolute black as the primary background — never substitute dark
  gray.
- Apply Lamborghini Gold exclusively to primary CTA buttons — never
  decoratively.
- Set all display headings in uppercase LamboType — the brand voice is
  always shouting.
- Use zero border-radius on buttons and cards — sharp angles are
  non-negotiable.
- Maintain tight line-heights (0.92–1.19) on display type for dense,
  architectural text blocks.
- Use the transparent ghost button (white border, 50% opacity) as the
  secondary CTA on dark backgrounds.
- Let full-viewport video/photography carry emotional weight; UI is
  infrastructure, not decoration.
- Reserve hexagonal geometry for UI icons and the video control button.
- Use weight 400 for headlines — the typeface doesn't need bold emphasis.
- Keep the gray palette achromatic — no warm or cool tinting.

**Don't**
- Introduce additional accent colors beyond gold — the monochrome-plus-gold
  system is sacred.
- Apply border-radius to buttons or cards — curves contradict the angular
  vehicle aesthetic.
- Use LamboType in italic or decorative styles — the brand stays upright
  and direct.
- Add gradients to buttons or surfaces — depth comes from surface
  layering, not blending.
- Use light backgrounds as the primary canvas — darkness is default, light
  is the exception.
- Mix lowercase into display headings — uppercase communicates authority.
- Add hover animations with scale or translate — interactions should be
  color-only.
- Use Open Sans for display text — LamboType must handle all visible
  typography.
- Create busy layouts with many small elements — the system favors
  singular, bold statements.
- Apply shadows to elements — on black, shadows are meaningless; use
  surface-color shifts instead.

## Responsive behavior

### Breakpoints
| Name | Width | Key changes |
|---|---|---|
| Mobile Small | <425px | single column, reduced type scale, stacked buttons |
| Mobile | 425–576px | single column, hamburger nav, hero text ~40px |
| Tablet Small | 576–768px | 2-column grid begins, padding adjusts |
| Tablet | 768–1024px | 2-column layout, expanded hero, vehicle cards side-by-side |
| Desktop | 1024–1280px | full navigation, 3+ column grids, display text at 80px |
| Desktop Large | 1280–1440px | full layout, hero at 120px display, max-width containers |
| Wide | >1440px | content centered, margins expand, hero fills viewport |

### Touch targets
Gold CTA buttons: 48px+ minimum height with 24px padding (exceeds WCAG
44×44px). Ghost buttons: 48px+ with 16px padding. The hamburger menu and
hexagonal pause button both sit around a 48px touch target.

### Collapsing strategy
Navigation is always hamburger-based ("MENU" + icon) at every breakpoint —
there is no horizontal nav expansion anywhere. The hero video maintains
full-viewport height across all breakpoints, adjusting `object-fit`.
Display type scales 120px → 80px → 54px/40px from desktop to mobile.
Buttons sit side-by-side on desktop and stack vertically on mobile. Grid
columns progress 3 → 2 → 1, and section spacing reduces from 56px → 40px →
24px vertical padding.

### Image behavior
Hero videos use `object-fit: cover` to preserve cinematic framing at every
size. Vehicle images scale within their containers with maintained aspect
ratios. Event photography crops to viewport width on narrow screens, and
background images darken at their edges to maintain text contrast.

## Known gaps

- Hover animations beyond color/opacity shifts are explicitly avoided by
  design, not merely undocumented.
- Form-field styling is minimal on the marketing site; only switch
  elements and the cookie-banner input are documented.
- Light-mode/white-canvas sections exist but are treated as the rare
  exception rather than a fully specified alternate theme.
- The proprietary LamboType face is not public — use the Roboto / Helvetica
  Neue / Arial fallback stack listed under Typography.
