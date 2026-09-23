# Tesla Design System — Full Analysis

Adapted from the Tesla design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/tesla/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Tesla's website is an exercise in radical subtraction — a digital
showroom where the product is everything and the interface is almost
nothing. The homepage opens with a full-viewport hero filling the entire
screen with cinematic car photography: vehicles arranged on polished
concrete against a hazy cityscape sky, with a single model name floating
above in translucent white type. There are no decorative borders, no
gradients, no patterns, and no shadows. The chrome exists only to provide
just enough navigational structure to get out of the way; every pixel
that isn't product imagery is whitespace, and that restraint is the
system's most powerful statement.

The color philosophy is almost ascetic: a single blue (`electric-blue`
`#3E6AE1`) for primary calls to action, three shades of dark gray for
text hierarchy, and white for everything else. The entire emotional
weight is carried by photography — sprawling landscape shots, studio-lit
vehicle profiles, and atmospheric environmental compositions stretching
edge-to-edge across each viewport-height section. The nav bar floats
above the hero with no visible background, border, or shadow — the
wordmark and navigation labels simply exist in the space, trusting the
imagery beneath to provide contrast.

Typography recently transitioned from Gotham to Universal Sans — a
custom family split into "Display" for headlines and "Text" for body/UI
— unifying the website, mobile app, and in-car software into a single
typographic voice. The Display variant renders hero titles at 40px
weight 500; the Text variant handles everything from navigation
(14px/500) to body copy (14px/400). The font carries geometric precision
with slightly humanist terminals — engineered rather than designed,
matching a brand identity that doesn't need to announce itself. There are
no text shadows, no text gradients, no decorative type treatments; every
letterform earns its place through clarity alone.

**Key characteristics:**
- Full-viewport (100vh) hero sections dominated by cinematic car
  photography with minimal overlay UI.
- Near-zero UI decoration — no shadows, no gradients, no borders, no
  patterns anywhere on the page.
- A single accent color, Electric Blue, used exclusively for primary CTA
  buttons.
- Universal Sans (Display + Text) unifying web, app, and in-car
  interfaces.
- Photography-first presentation where product imagery carries all
  emotional weight.
- A frosted-glass nav concept that floats transparent/white over hero
  content.
- 0.33s cubic-bezier transitions as the universal timing for interactive
  state changes.
- A carousel-driven hero with dot indicators and edge-arrow navigation
  for multiple vehicle showcases.
- A persistent "Ask a Question" chatbot bar anchored to the viewport
  bottom.

## Colors

### Primary
- **Electric Blue** — the only chromatic color in the interface; used
  exclusively for "Order Now" and similar primary action buttons.
- **Pure White** — the dominant background for all surfaces, panels,
  navigation, and secondary button fills, letting photography breathe.

### Secondary & accent
- **Promo Blue** — the same electric blue reused for promotional text
  ("0% APR Available") over hero imagery, visually linking incentive
  messaging to action. No other secondary accents exist — color variety
  is deliberately avoided.

### Surface & background
- **White Canvas** — page background, nav panel, dropdowns, and surface
  containers.
- **Light Ash** — a barely perceptible alternate surface for section
  differentiation.
- **Carbon Dark** — a warm near-black with a blue undertone, used for
  hero text overlays and potential dark-mode contexts.
- **Frosted Glass** (`rgba(255,255,255,0.75)`) — semi-transparent white
  for the nav backdrop-filter effect on scroll.

### Neutrals & text
- **Carbon Dark** — primary heading and navigation text, the darkest
  text value, used for model names, nav labels, and hero titles on light
  backgrounds.
- **Graphite** — body text and secondary content, the default paragraph
  color.
- **Pewter** — tertiary text for sub-links like "Learn" and "Order."
- **Silver Fog** — placeholder text and disabled states.
- **Cloud Gray / Pale Silver** — light borders, divider lines, and
  subtle UI delineation.

### Semantic
- The marketing site avoids semantic color coding entirely (no green/
  red/yellow status indicators); form states fall back to standard
  browser defaults. Electric Blue is the sole interactive color signal.

There are no gradients anywhere in the interface. Depth comes entirely
from photography, whitespace, and the binary contrast between full-bleed
imagery and clean white surfaces; even the nav achieves layering through
opacity (frosted glass) rather than gradient or shadow.

## Typography

### Families
- **Display** — `Universal Sans Display` (fallback: -apple-system,
  Arial, sans-serif) for hero titles and large model names; a geometric
  sans with precisely engineered proportions, recently replacing Gotham
  to unify Tesla's digital ecosystem.
- **Text/UI** — `Universal Sans Text` on the same fallback stack, used
  for navigation, body copy, buttons, and all UI text, optimized for
  legibility at smaller sizes.

No OpenType features, no italic variants, and no text transforms (no
uppercase) appear anywhere on the marketing site.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale (hero-title at
40px down to category-label at 16px). Governing principles:
- **"Normal" letter-spacing everywhere** — unlike most modern tech
  brands, Tesla never applies negative tracking to headlines; the
  typeface is meant to speak for itself unmanipulated.
- **Weight restraint** — only two weights appear, 500 (medium) for
  headings/UI and 400 (regular) for body. No bold, no light.
- **Unified sizing** — most UI text clusters at 14px, with only hero
  titles (40px) and promo text (22px) breaking away, creating a sense of
  engineered consistency.
- **Display vs Text split** — the two-variant system creates subtle
  optical correction without visible stylistic difference; they read as
  the same typeface at different sizes.
- **No text transforms** — no uppercase anywhere in nav or CTAs; the
  lowercase approach reinforces an understated confidence.

## Components

Definitions live in `design-tokens.yaml → components`. Summary:
- **Buttons** — all buttons use barely-rounded rectangles (4px radius).
  The primary CTA is filled Electric Blue with white text; the secondary
  CTA is white with graphite text; nav buttons are transparent with
  carbon-dark text; text links use pewter with an underline-on-hover
  response. Every button shares the same 0.33s transition timing.
- **Cards** — the vehicle card (in the nav dropdown) is fully
  transparent with no border or shadow, just an image, model name, and
  two text links in a 3-column grid. The category card is the one
  exception with visible rounding (~12px), filled edge-to-edge with
  landscape photography and a white text label in the top-left corner —
  no shadow, no border, no overlay gradient.
- **Inputs** — transparent background, carbon-dark text, silver-fog
  placeholder, minimal browser-default border.
- **Navigation** — a centered horizontal desktop nav with the wordmark
  left, five category buttons centered, and icon buttons right; it
  transitions from transparent over the hero to opaque white on scroll,
  with a full-width dropdown panel (3-column vehicle grid, no shadow, no
  border) and a hamburger collapse on mobile.
- **Persistent chat bar** — anchored to the viewport bottom with a chat
  icon, "Ask a Question" placeholder, send icon, and a secondary CTA with
  a teal icon accent.

## Layout

- Base spacing unit: 8px, with common values at 8px, 16px, and 21.44px.
- Button padding stays minimal (4px outer, content-centered via
  flexbox); nav items use `4px 16px`.
- Sections are full-viewport with content centered vertically; card
  gaps run roughly 16px.
- Max content width is roughly 1383px, though the hero itself is fully
  edge-to-edge at 100vh.
- The nav dropdown panel splits roughly 70/30 into a 3-column vehicle
  grid plus a text sidebar; category cards run 2-up (a large card beside
  a smaller one).
- Whitespace functions as a luxury signal: because each section is a
  full viewport height, only one "message" is visible at a time — one
  car, one model name, one CTA pair — producing a gallery-like browsing
  experience where every scroll is a deliberate transition rather than a
  continuous feed.

## Shapes

| Value | Context |
|---|---|
| 0px | Most elements — sharp edges are the default |
| 4px | Buttons (primary, secondary, nav items) — barely perceptible rounding |
| ~12px | Category cards — noticeable but restrained rounding on larger surfaces |
| 50% | Carousel dot indicators — perfect circles |

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| Level 0 (Flat) | No shadow, no border | Default state for all elements at rest |
| Level 1 (Frost) | `rgba(255,255,255,0.75)` backdrop | Navigation bar on scroll — frosted glass |
| Level 2 (Overlay) | `rgba(128,128,128,0.65)` | Modal overlays and region/cookie popups |
| Level 3 (Subtle) | `rgba(0,0,0,0.05)` | Minimal shadow hints on rare hover states |

Tesla's approach to elevation is essentially "none." Depth is
communicated through three alternative strategies instead of shadow: (1)
z-index layering, where the sticky nav sits above hero content through
positioning rather than shadow; (2) opacity-based transparency, where the
frosted-glass nav and overlay modals rely on background opacity; and (3)
photography-as-depth, where full-bleed images create their own visual
depth through perspective and lighting, making UI shadows redundant. No
gradients, glows, or atmospheric effects appear on UI elements at all —
carousel arrows float over the hero using only a semi-transparent white
background.

## Do's and don'ts

**Do**
- Let photography dominate every screen — the product IS the design.
- Use Electric Blue exclusively for primary CTAs, never decoratively.
- Maintain viewport-height sections for major content blocks — one
  message per screen.
- Keep typography at weight 400-500 only, no bold, no light.
- Use 4px border-radius for interactive elements — precision over
  playfulness.
- Trust whitespace as a luxury signal; never fill available space just
  because it's empty.
- Keep all transitions at 0.33s for consistency in motion.
- Use transparent PNG vehicle imagery on white backgrounds for product
  showcases.
- Center CTAs below model names in a model → subtitle → buttons rhythm.
- Maintain the Display/Text font split — Display for hero-scale only.

**Don't**
- Add shadows to any element — elevation through shadow contradicts the
  flat, gallery aesthetic.
- Use more than one chromatic color besides the blue CTA.
- Apply gradients, patterns, or decorative backgrounds to surfaces.
- Use text larger than 40px on the web.
- Add borders to cards or containers — use spacing for separation
  instead.
- Use uppercase text transforms.
- Introduce pill buttons or large border-radii.
- Override Universal Sans with other typefaces.
- Add hover animations with scale/translate transforms — interactions
  stay color-only.
- Clutter the viewport with more than two CTAs per screen.

## Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Mobile | <768px | Single-column layout, hamburger nav, hero text scales to ~28px, CTAs stack vertically, category cards go full-width |
| Tablet | 768-1024px | 2-column nav panel, hero stays full-viewport, CTAs remain side-by-side, reduced horizontal padding |
| Desktop | 1024-1440px | Full horizontal nav, 3-column vehicle grid, hero at 40px, side-by-side CTAs at 200px/160px width |
| Large Desktop | >1440px | Content stays centered, hero photography scales to fill wider viewports |

Primary CTA buttons measure 200×40px minimum (well above the 44×44px
WCAG requirement); nav buttons hold a 32px minimum height with `4px
16px` padding; carousel arrows are ~44px square semi-transparent
buttons. On collapse, horizontal category buttons become a hamburger
drawer, side-by-side hero CTAs stack vertically, 2-up category cards go
single-column full-width, and the 3-column vehicle grid steps down to 2
then 1 column — while section vertical padding stays generous
(viewport-height sections) even as horizontal padding shrinks. Hero
images use `object-fit: cover` to preserve cinematic composition at every
width, and vehicle/category images scale proportionally without
stretching.

## Known gaps

- The token values here are extracted directly from the source analysis
  and should be treated as canonical for this skill.
- Exact spacing for lazy-loaded below-fold sections (which render blank
  white until scrolled into view) is not fully documented beyond the
  general lazy-loading note.
