# Runway Design System — Full Analysis

Adapted from the Runway design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/runwayml/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Runway's interface behaves like a cinematic reel brought to life as a
website — a dark, editorial, film-production-grade design where full-bleed
photography and video *are* the primary UI elements. This isn't a typical
tech product page; it reads as a visual manifesto for AI-powered
creativity. Every section feels like a frame pulled from a film: dramatic
lighting, sweeping landscapes, and intimate human moments captured in
high-quality imagery that dominates the viewport.

The design language rests on a single typeface — **abcNormal**, a clean,
geometric sans that handles everything from a 48px display headline down
to an 11px uppercase micro label. This single-font commitment creates an
extreme typographic uniformity that lets the visual content speak louder
than the text. Headlines use tight line-heights (1.0) with negative
letter-spacing (-0.9px to -1.2px), producing compressed text blocks that
feel more like film titles than marketing copy.

What makes Runway distinctive is its total commitment to visual content
as design. Rather than illustrating features with icons or diagrams,
Runway shows actual AI-generated and AI-enhanced imagery — cars driving
through cinematic landscapes, artistic portraits, architectural renders.
The interface itself retreats into near-invisibility: minimal borders,
zero shadows, subtle cool-gray text, and a dark palette that puts maximum
focus on the photography.

**Key characteristics:**
- Cinematic full-bleed photography and video as primary UI elements.
- A single-typeface system: abcNormal for everything from display to
  micro labels.
- A dark-dominant palette with cool-toned neutrals (`#767d88`,
  `#7d848e`).
- Zero shadows, minimal borders — the interface is intentionally
  invisible.
- Tight display typography (line-height 1.0) with negative tracking
  (-0.9px to -1.2px).
- Uppercase labels with positive letter-spacing for navigational
  structure.
- Weight 450 — an unusual intermediate weight — for small uppercase text,
  a precision-craft detail.
- Editorial magazine layout with mixed-size image grids.

## Colors

### Primary
- **Runway Black** (`#000000`) is the primary page background and
  maximum-emphasis text color.
- **Deep Black** (`#030303`) is a near-imperceptible variant for layered
  dark surfaces.
- **Dark Surface** (`#1a1a1a`) carries card backgrounds and elevated dark
  containers.
- **Pure White** (`#ffffff`) is the primary text color on dark surfaces
  and the background on light sections.

### Surface & background
- **Near White** (`#fefefe`) is the lightest surface, barely
  distinguishable from pure white.
- **Cool Cloud** (`#e9ecf2`) covers light section backgrounds with a cool
  blue-gray tint.
- **Border Dark** (`#27272a`) is the single dark-mode border color —
  barely visible containment.

### Neutrals & text
- **Charcoal** (`#404040`) is primary body text on light surfaces and
  secondary text elsewhere.
- **Near Charcoal** (`#3f3f3f`) is a slightly lighter variant for dark-
  section secondary text.
- **Cool Slate** (`#767d88`) is secondary body text — a distinctly
  blue-gray cool neutral, used instead of a warm gray.
- **Mid Slate** (`#7d848e`) is tertiary text and metadata description.
- **Muted Gray** (`#a7a7a7`) marks de-emphasized content and timestamps.
- **Cool Silver** (`#c9ccd1`) and **Light Silver** (`#d0d4d4`) are the
  light-mode border and divider tones.
- **Tailwind Gray** (`#6b7280`) is a standard neutral for supplementary
  text.
- **Dark Link** (`#0c0c0c`) is the darkest link text, nearly black.
- **Footer Gray** (`#999999`) covers footer links and deeply muted
  content.

### Gradient system
There is no gradient system in the interface. Visual richness comes
entirely from photographic content — the AI-generated and AI-enhanced
imagery supplies all the color and gradient the design needs; the
interface itself stays intentionally colorless.

## Typography

### Font family
The universal face is **abcNormal**, with `abcNormal Fallback` as the
system fallback. abcNormal is a custom geometric sans-serif; for external
implementations, **Inter** or **DM Sans** serve as close substitutes.

### Hierarchy

| Role | Size | Weight | Line height | Letter spacing | Notes |
|---|---|---|---|---|---|
| Display / Hero | 48px | 400 | 1.00 (tight) | -1.2px | Maximum size, film-title presence |
| Section Heading | 40px | 400 | 1.00-1.10 | -1px to 0px | Feature section titles |
| Sub-heading | 36px | 400 | 1.00 (tight) | -0.9px | Secondary section markers |
| Card Title | 24px | 400 | 1.00 (tight) | normal | Article and card headings |
| Feature Title | 20px | 400 | 1.00 (tight) | normal | Small headings |
| Body / Button | 16px | 400-600 | 1.30-1.50 | -0.16px to normal | Standard body, nav links |
| Caption / Label | 14px | 500-600 | 1.25-1.43 | 0.35px (uppercase) | Metadata, section labels |
| Small | 13px | 400 | 1.30 (tight) | -0.16px to -0.26px | Compact descriptions |
| Micro / Tag | 11px | 450 | 1.30 (tight) | normal | Uppercase tags, tiny labels |

### Principles
One typeface delivers the full range of expression — abcNormal handles
every text role, and variety comes from size, weight, case, and
letter-spacing rather than family switching. Nearly every size uses
line-height 1.0-1.30, even body text, producing a dense, editorial feel.
The weight-450 detail on small uppercase labels — an uncommon intermediate
between regular and medium — is a deliberate micro-craft signal of
typographic sophistication. Even body text carries negative tracking
(-0.16px to -0.26px), keeping everything slightly tighter than a browser
default. Uppercase labels at 14px and 11px use positive letter-spacing
(0.35px) to create navigational signposts that contrast against the
tight lowercase body copy.

## Layout

### Spacing system
- **Base unit:** 8px.
- **Scale:** 4px, 6px, 8px, 12px, 16px, 20px, 24px, 28px, 32px, 48px,
  64px, 78px.
- **Section vertical spacing:** generous, 48-78px.
- **Component gaps:** 16-24px.

### Grid & container
- Max container width runs up to 1600px — a cinema-wide frame.
- The hero is full-viewport, edge to edge.
- Content sections center with generous margins.
- Image grids are asymmetric, magazine-style, with mixed sizes.
- The footer is a full-width dark section.

### Whitespace philosophy
Large vertical gaps between sections create a scrolling experience that
feels like watching scenes change — "cinema-grade breathing." Where other
sites use empty space, Runway fills it with photography instead; the
visual content itself *is* the breathing room. The image grid uses
intentionally varied sizes — a large hero image paired with smaller
supporting images — creating deliberate visual rhythm through editorial
asymmetry.

### Border radius scale
- **Sharp** (4px) — buttons, small interactive elements.
- **Subtle** (6px) — links, small containers.
- **Comfortable** (8px) — standard containers, image cards.
- **Generous** (16px) — alert-style containers, featured elements.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| Flat (0) | No shadow, no border | Everything — the dominant state |
| Bordered (1) | `1px solid #27272a` | Alert containers only |
| Dark Section (2) | Dark background with light text | Hero, features, footer |
| Light Section (3) | White/Cool Cloud background with dark text | Content sections, research |

Runway uses **zero shadows** — a film-production decision. In cinema,
depth comes from lighting, focus, and composition rather than drop
shadows, and the interface mirrors that philosophy: depth is communicated
through dark/light section alternation, photographic depth-of-field, and
overlay transparency, never through CSS box-shadow.

## Components

### Buttons
Text runs 14px abcNormal weight 600, with a background that's typically
transparent or dark and only a minimal border. Radius is small (4px) for
button-like links. The button design is extremely restrained — no heavy
fills or borders were detected — and interactive elements blend into the
editorial flow rather than announcing themselves.

### Cards & containers
Backgrounds are transparent or Dark Surface (`#1a1a1a`); the border is a
barely-visible `1px solid #27272a` in dark mode. Radius runs small
(4-8px) for functional elements and 16px for alert-style containers, with
zero shadow on any element. Cards are primarily photographic — the image
*is* the card.

### Navigation
A minimal horizontal nav sits transparent over hero content, with the
Runway wordmark in white or black and links set in abcNormal at 16px,
weight 400-600. Hover shifts text to white or higher opacity. The nav is
extremely subtle, designed not to compete with visual content.

### Image treatment
Full-bleed cinematic photography and video dominate every relevant
section. AI-generated content is shown at large scale as a primary visual
element, laid out in mixed-size editorial magazine grids. Dark overlays
sit on hero images for text readability, and product screenshots carry
subtle 8px rounded corners.

### Distinctive components
- **Cinematic Hero** — full-viewport image or video with a text overlay;
  the headline runs 48px abcNormal, white on dark imagery; the image is
  always cinematic quality, film-grade composition.
- **Research Article Cards** — photographic thumbnails with article
  titles in a mixed-size grid (one large feature card plus smaller
  supporting cards), with either a clean text overlay or a below-image
  caption style.
- **Trust Bar** — company logos in a clean, monochrome treatment,
  horizontal layout with generous spacing.
- **Mission Statement** — the emotional close of the page: "We are
  building AI to simulate the world through imagination, art and
  aesthetics," on a dark background with white text.

## Do's and don'ts

**Do**
- Use full-bleed cinematic photography as the primary visual element.
- Use abcNormal for all text, maintaining the single-typeface commitment.
- Keep display line-heights at 1.0 with negative letter-spacing for
  film-title density.
- Use the cool-gray neutral palette (`#767d88`, `#7d848e`) for secondary
  text.
- Maintain zero shadows — depth comes from photography and section
  backgrounds.
- Use uppercase with letter-spacing for navigational labels (14px,
  0.35px).
- Apply small border-radius (4-8px) — the design is not pill-shaped.
- Let visual content dominate — the UI should be invisible.
- Use weight 450 for micro labels — the precision matters.

**Don't**
- Don't add decorative colors to the interface — the only color comes
  from photography.
- Don't use heavy borders or shadows — the interface must be nearly
  invisible.
- Don't use pill-shaped radius — Runway's geometry is subtly rounded, not
  circular.
- Don't use bold (700+) weight — 400-600 is the full range, with 450 as
  a precision tool.
- Don't compete with the visual content — text overlays should stay
  minimal and restrained.
- Don't use gradient backgrounds in the interface — gradients exist only
  in photography.
- Don't use more than one typeface.
- Don't use body line-height above 1.50 — the tight, editorial feel is
  core.
- Don't reduce image quality — cinematic photography *is* the design.

## Responsive behavior

| Name | Width | Key changes |
|---|---|---|
| Mobile | <640px | Single column, stacked images, reduced hero text |
| Tablet | 640-768px | Two-column image grids begin |
| Small Desktop | 768-1024px | Standard layout |
| Desktop | 1024-1280px | Full layout, expanded hero |
| Large Desktop | 1280-1600px | Maximum cinema-width container |

Navigation links sit at a comfortable 16px; article cards serve as large
touch targets; buttons run 14px weight 600 with adequate padding.
Navigation collapses to a hamburger on mobile; the hero stays full-bleed
with text scaling down; image grids reflow from multi-column to
two-column to single column; research article cards go from feature-size
to stacked full-width; trust logos switch to horizontal scroll or a
reduced grid. Cinematic images scale proportionally, the full-bleed hero
is maintained across all sizes, image grids reflow to fewer columns, and
video content maintains its aspect ratio throughout.

## Known gaps

The source analysis is a narrative, prose-based document rather than a
token-frontmatter DESIGN.md, so it does not include a "Known Gaps"
section, per-page source attribution, or a component-by-component token
table the way this collection's other analyses do. Values above are
transcribed directly from its color list, typography table, and
prose sections; anything not explicitly stated there (exact component
padding, hover-state colors, focus-ring treatment) isn't documented in
the source and isn't invented here.
