# Sanity Design System — Full Analysis

Adapted from the Sanity design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/sanity/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Sanity's website presents a developer-content platform as a nocturnal
command center — dark, precise, and deeply structured. The entire
experience sits on a near-black canvas (`#0b0b0b`) that reads less like a
toggled "dark mode" and more like the natural state of a tool built for
people who live in terminals. Where most CMS marketing pages reach for
friendly pastels and soft illustration, Sanity leans into the gravity of
its own product: structured content deserves a structured stage.

The signature typographic voice is **waldenburgNormal**, a distinctive,
slightly geometric sans with tight negative letter-spacing (-0.32px to
-4.48px at display sizes) that gives headlines a compressed, engineered
quality. At 112px hero scale with -4.48px tracking, the type feels almost
machined — precision-cut steel letterforms. This pairs with **IBM Plex
Mono** for code and technical labels, creating a dual-register voice:
editorial authority meets developer credibility.

What makes Sanity distinctive is the interplay between its monochromatic
dark palette and vivid, saturated accent punctuation. The neutral scale
runs from pure black through a tightly controlled gray ramp (`#0b0b0b` →
`#212121` → `#353535` → `#797979` → `#b9b9b9` → `#ededed` → `#ffffff`)
with no warm or cool bias — just pure, achromatic precision. Against this
disciplined backdrop, a neon green accent (a wide-gamut display-P3 green)
and electric blue (`#0052ef`) land with the impact of signal lights in a
dark control room. An orange-red CTA (`#f36458`) provides the only warm
touch in an otherwise cool system.

**Key characteristics:**
- A near-black canvas (`#0b0b0b`) as the default, natural environment —
  not a dark "mode" but the primary identity.
- waldenburgNormal with extreme negative tracking at display sizes,
  creating a precision-engineered typographic voice.
- A pure achromatic gray scale — no warm or cool undertones anywhere.
- Vivid accent punctuation: neon green, electric blue (`#0052ef`), and
  coral-red (`#f36458`) against the dark field.
- Pill-shaped primary buttons (99999px radius) contrasting with subtle
  rounded rectangles (3-6px) for secondary actions.
- IBM Plex Mono as the technical counterweight to the editorial display
  face.
- Full-bleed dark sections with content held in measured max-width
  containers.
- Hover states that shift to electric blue across all interactive
  elements — a consistent "activation" signal.

## Colors

### Primary brand
- **Sanity Black** (`#0b0b0b`) is the primary canvas and dominant surface
  color — not pure black, but close enough to feel absolute, and the
  foundation of the whole visual identity.
- **Pure Black** (`#000000`) is reserved for maximum-contrast moments,
  deep overlays, and certain border accents.
- **Sanity Red** (`#f36458`) is the primary CTA and brand accent — a warm
  coral-red used for "Get Started" buttons and primary conversion points.

### Accent & interactive
- **Electric Blue** (`#0052ef`) is the universal hover/active state color
  across the entire system — buttons, links, and interactive elements all
  shift to it on hover, and it also serves as the focus-ring color.
- **Light Blue** variants (`#55beff` / `#afe3ff`) cover accent backgrounds,
  badges, and dimmed blue surfaces.
- **Neon Green** (a wide-gamut display-P3 green, falling back to `#19d600`
  in sRGB) marks success states and premium feature highlights.
- **Accent Magenta** (a wide-gamut display-P3 magenta) covers rare
  specialized accent moments.

### Surface & background
- **Near Black** (`#0b0b0b`) is the default page background and primary
  surface.
- **Dark Gray** (`#212121`) is the elevated surface for cards, secondary
  containers, and input backgrounds.
- **Medium Dark** (`#353535`) is a tertiary surface/border color for
  depth between dark layers.
- **Pure White** (`#ffffff`) covers inverted sections and specific button
  surfaces.
- **Light Gray** (`#ededed`) is a light surface for inverted sections and
  subtle background tints.

### Neutrals & text
- **White** (`#ffffff`) is the primary text color on dark surfaces.
- **Silver** (`#b9b9b9`) is secondary text, body copy on dark surfaces,
  muted descriptions, and placeholder text.
- **Medium Gray** (`#797979`) is tertiary text, metadata, and timestamps.
- **Charcoal** (`#212121`) is text on light/inverted surfaces.
- **Near Black Text** (`#0b0b0b`) is primary text on white/light button
  surfaces.

### Semantic & border
- **Error Red** (`#dd0000`) marks destructive actions and validation
  errors — a pure, high-saturation red.
- **GPC Green** (`#37cd84`) is a privacy/compliance indicator green.
- **Focus Ring Blue** (`#0052ef`) matches the interactive blue.
- The border system runs from **Dark Border** (`#0b0b0b`, barely visible)
  through **Subtle Border** (`#212121`, standard on inputs/cards) up to
  **Medium Border** (`#353535`, more visible dividers), with **Light
  Border** (`#ffffff`) on inverted elements and a rare display-P3 **Orange
  Border** for highlighted/featured elements.

## Typography

### Font family
The display, headline, and body/UI tiers all run **waldenburgNormal**,
falling back through `waldenburgNormal Fallback` → `ui-sans-serif` →
`system-ui`. Code and technical content run **IBM Plex Mono**, falling
back through `ibmPlexMono Fallback` → `ui-monospace`. A final CJK
fallback chain runs Helvetica → Arial → Hiragino Sans GB → STXihei →
Microsoft YaHei → WenQuanYi Micro Hei.

waldenburgNormal is a custom typeface; for external implementations,
**Inter** or **Space Grotesk** serve as sans substitutes (geometric,
slightly condensed feel). IBM Plex Mono is available directly on Google
Fonts.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale — a display hero
at 112px/400/-4.48px tracking cascading down through hero-secondary
(72px), section-heading (48px), heading-large/medium/small, subheading,
body tiers, and down to an 11px micro-label tier, plus three IBM Plex Mono
code sizes.

### Principles
Display headings at 72px and above use aggressive negative letter-spacing
(-2.88px to -4.48px), creating a tight, engineered quality that
distinguishes Sanity from looser editorial typography. A single font
carries both editorial display and functional UI text, with a
deliberately narrow weight range (400-425 for most sizes, 500-600 only
for tiny labels) that keeps the voice consistent throughout. Typography
uses deliberate OpenType feature settings — `"cv01", "cv11", "cv12",
"cv13", "ss07"` for display sizes and `"calt" 0` for body text — to
fine-tune character alternates by context. Headings run extremely tight
(1.00-1.24 line-height) while body breathes at 1.50, creating clear
hierarchy through that contrast alone. IBM Plex Mono captions and small
labels frequently render uppercase with tight line-heights, producing a
"system readout" aesthetic for technical metadata.

## Layout

### Spacing system
Base unit: 8px. The scale runs from `space-1` (1px, hairline gaps) through
`space-5` (8px, the base unit for button/input/badge padding) up to
`space-12` (96-120px, hero vertical padding and maximum section spacing).

### Grid & container
Max content width holds around 1440px (inferred from breakpoints), with a
32px page gutter on desktop narrowing to 16px on mobile. Content sections
use full-bleed backgrounds with centered, max-width content; multi-column
layouts run 2-3 columns on desktop, collapsing to single-column on
mobile; card grids use CSS Grid with 16-24px gaps.

### Whitespace philosophy
Sanity uses aggressive vertical spacing between sections (64-120px) to
create breathing room on the dark canvas. Within sections, spacing
tightens (16-32px), producing dense information clusters separated by
generous voids — a rhythm that gives the page a "slides" quality, where
each section feels like its own focused frame.

### Border radius scale
`radius-xs` (3px) covers inputs and textareas; `radius-sm` (4-5px)
secondary buttons and small cards; `radius-md` (6px) standard cards and
containers; `radius-lg` (12px) large cards and feature containers;
`radius-pill` (99999px) primary buttons, badges, and nav pills.

## Elevation & depth

| Level | Value | Usage |
|---|---|---|
| 0 (Flat) | none | Default state for most elements — dark surfaces create depth through color alone |
| 1 (Subtle) | `0px 0px 0px 1px #212121` | Border-like shadow for minimal containment without visible borders |
| 2 (Focus) | `0 0 0 2px var(--color-blue-500)` | Focus ring for inputs and interactive elements |
| 3 (Overlay) | Backdrop blur + semi-transparent dark | Navigation overlay, modal backgrounds |

Sanity's depth system is almost entirely **colorimetric** rather than
shadow-based. Elevation is communicated through surface-color shifts —
`#0b0b0b` (ground) → `#212121` (elevated) → `#353535` (prominent) →
`#ffffff` (inverted/highest) — an approach native to dark interfaces
where traditional drop shadows would be invisible. The few shadows that
exist are ring-based (`0px 0px 0px Npx`) or blur-based rather than offset
shadows, maintaining the flat, precision-engineered aesthetic. Border-
based containment (1px solid `#212121` or `#353535`) is the primary
spatial separator, calibrated to be visible but not dominant — the system
avoids "floating card" aesthetics; everything feels mounted to the
surface rather than hovering above it.

## Components

### Buttons
- **Primary CTA (Pill)** — Sanity Red background, white text, 8px 16px
  padding, 99999px radius, no border, hovering to Electric Blue.
- **Secondary (Dark Pill)** — Near Black background, Silver text, 8px 12px
  padding, 99999px radius, hovering to Electric Blue.
- **Outlined (Light Pill)** — White background, Near Black text, 8px
  padding, 99999px radius, 1px solid Near Black border, hovering to
  Electric Blue.
- **Ghost / Subtle** — Dark Gray background, Silver text, 0px 12px
  padding, 5px radius, 1px solid Dark Gray border, hovering to Electric
  Blue.
- **Uppercase Label Button** — 11px waldenburgNormal weight 600 uppercase,
  transparent or Dark Gray background, Silver text, used for tab-like
  navigation and filter controls.

### Cards
- **Dark Content Card** — `#212121` background, `1px solid #353535` or
  `#212121` border, 6px radius, 24px padding, white titles with Silver
  body text.
- **Feature Card (Full-bleed)** — `#0b0b0b` or a full-bleed image/gradient
  background, no border or `1px solid #212121`, 12px radius, 32-48px
  padding, containing large imagery with overlaid text.

### Inputs
- **Text Input / Textarea** — Near Black background, Silver text, `1px
  solid #212121` border, 8px 12px padding, 3px radius; focus shows a 2px
  blue outline and the background shifts to a deep cyan (`#072227`).
- **Search Input** — Near Black background, Silver text, 0px 12px
  padding, 3px radius, Medium Gray placeholder.

### Navigation
- **Top Navigation** — Near Black background with backdrop blur, a
  left-aligned Sanity wordmark, 16px Silver links hovering to Electric
  Blue, a Sanity Red pill CTA right-aligned, and a `1px solid #212121`
  bottom border.
- **Footer** — Near Black background, a multi-column link layout in
  Silver hovering to blue, with white 13px uppercase IBM Plex Mono
  section headers.

### Badges / pills
- **Neutral Subtle** — white background, Near Black text, 8px padding,
  13px type, pill radius.
- **Neutral Filled** — Near Black background, white text, 8px padding,
  13px type, pill radius.

## Do's and don'ts

**Do**
- Use the achromatic gray scale as the foundation — maintain pure neutral
  discipline with no warm/cool tinting.
- Apply Electric Blue consistently as the universal hover/active state
  across every interactive element.
- Use extreme negative letter-spacing (-2px to -4.48px) on display
  headings 48px and above.
- Keep primary CTAs as full-pill shapes (99999px) in coral-red.
- Use IBM Plex Mono uppercase for technical labels, tags, and system
  metadata.
- Communicate depth through surface color rather than shadows.
- Maintain generous vertical section spacing (64-120px) on the dark
  canvas.
- Use the documented OpenType feature set for display typography.

**Don't**
- Don't introduce warm or cool color tints to the neutral scale.
- Don't use drop shadows for elevation — dark interfaces demand
  colorimetric depth.
- Don't apply a border-radius between 13px and 99998px — the system jumps
  from 12px directly to pill.
- Don't mix the coral-red CTA with the electric-blue interactive color in
  the same element.
- Don't use heavy font weights (700+) — the system maxes out at 600, and
  only for 11px uppercase labels.
- Don't place light text on light surfaces or dark text on dark surfaces
  without checking gray-on-gray contrast.
- Don't use traditional offset box-shadows — ring shadows or border-based
  containment only.
- Don't break the tight heading line-height (1.00-1.24) — never go to
  1.5+ for display text.

## Responsive behavior

| Name | Width | Behavior |
|---|---|---|
| Desktop XL | ≥1640px | Full layout, maximum content width |
| Desktop | ≥1440px | Standard desktop layout |
| Desktop Compact | ≥1200px | Slightly condensed desktop |
| Laptop | ≥1100px | Reduced column widths |
| Tablet Landscape | ≥960px | Two-column layouts begin collapsing |
| Tablet | ≥768px | Transition zone, some elements stack |
| Mobile Large | ≥720px | Near-tablet layout |
| Mobile | ≥480px | Single-column, stacked layout |
| Mobile Small | ≥376px | Minimum supported width |

Navigation collapses to a hamburger menu below 768px; hero typography
scales 112px → 72px → 48px → 38px across breakpoints while maintaining
tight tracking ratios; grid layouts go three-column → two-column at
~960px → single-column below 768px; card grids switch to horizontal
scrolling on mobile rather than wrapping; section vertical padding
reduces by roughly 40% on mobile (120px → 64px → 48px); CTA pills keep
their padding but reduce font size. Full-bleed sections extend edge to
edge with 16px internal gutters on mobile, touch targets hold a 44px
minimum, and heading letter-spacing relaxes slightly at mobile sizes.

## Known gaps

The source analysis is a narrative, prose-based document rather than a
token-frontmatter DESIGN.md, so it doesn't carry a formal "Known Gaps"
section, per-page source attribution, or a component-token table the way
this collection's other analyses do. Values above are transcribed
directly from its color list, typography table, component-styling
prose, and responsive tables; anything not explicitly stated there
(hover states beyond the documented blue shift, exact validation-error
styling) isn't documented in the source and isn't invented here.
