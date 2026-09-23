# Shopify Design System — Full Analysis

Adapted from the Shopify design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/shopify/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Shopify runs two parallel design tracks that share typographic DNA and a
single button vocabulary, but diverge sharply in canvas polarity. The
marketing track lives on `colors.canvas-night` (`#000000`) — full-bleed
cinematic photography of merchants, giant `typography.display-xxl`
headlines in Neue Haas Grotesk Display set at weight 330 (a thin, almost
editorial cut), and a single CTA form: a white-stroked black pill (`
button-outline-on-dark`). These pages read like the spread of a high-end
print magazine: lots of black, lots of negative space, photography that
never competes with the type, and one and only one action per band.

The transactional track flips to `colors.canvas-light` and `colors.canvas-
cream` (an off-white barely warmer than pure white). Pricing tiers,
comparison tables, and signup flows sit on this lighter canvas, using the
same pill-button system but in inverse polarity — a solid black pill with
white text, or an aloe-mint pill (`colors.aloe-10`) for the featured
"Start free trial" tier. The mint accents — aloe and pistachio — show up
only on this light track; they never appear on the cinematic dark hero
pages.

Typography splits across three families. **Neue Haas Grotesk Display** at
thin weights (330-500) handles every display, headline, and editorial
moment — the brand's identity is that thin display cut. **Inter Variable**
at 420-550 weights handles every UI body, button label, caption, and form
field — utility text that never competes with the display. **ui-
monospace** appears only in code blocks and rare technical eyebrows.
Across all three families, the OpenType `ss03` stylistic set is enabled —
a character-level signature applied universally, on both tracks alike.

**Key characteristics:**
- A two-canvas system — `canvas-night` for cinematic marketing,
  `canvas-light` / `canvas-cream` for transactional surfaces — never
  blended.
- Pill shape is the only button shape across both tracks; rounded
  rectangles don't exist for buttons.
- Thin-weight (330) display typography is the signature; the 96px
  `display-xxl` tier is the brand's loudest visual.
- Aloe and pistachio greens are reserved for the light track, signaling
  commerce and growth.
- Photography is full-bleed and edge-to-edge, never inset in cards on the
  cinematic track — merchant and storefront imagery does the visual
  lifting that gradients or illustration would do elsewhere.
- The `ss03` OpenType stylistic set is enabled across every text role, a
  character-level unifier tracking across both tracks.
- Tight positive tracking on display sizes (2.4px on the 96px tier) gives
  the thin weight extra optical air.

## Colors

> **Source pages:** home, `/start`, `/website/builder`, `/pricing`.

### Brand & accent
- **Aloe** (`colors.aloe-10`, `#c1fbd4`) is the featured-tier and "growth"
  accent — used as a pill-button background on light surfaces and as a
  feature-card fill in the pricing comparison band.
- **Pistachio** (`colors.pistachio-10`, `#d4f9e0`) is softer than aloe,
  used as a wide section-band fill on the light track to signal a
  different feature category without leaving the green family.
- **Cool Link Tones** (`#9dabad`, `#9797a2`, `#bdbdca`, `#99b3ad`) are
  muted footer/tertiary link colors on dark surfaces, creating a quiet
  hierarchy below the primary white type.

### Surface
- **Canvas Night** (`#000000`) — pure black hero, cinematic feature pages,
  footer.
- **Canvas Night Elevated** (`#0a0a0a`) — cards on cinematic surfaces,
  video frames.
- **Surface Elevated Dark** (`#1e2c31`) — a dark teal-shifted surface on a
  small subset of dark cards, introducing subtle depth without breaking
  the black.
- **Canvas Light** (`#ffffff`) — pricing, signup, comparison tables.
- **Canvas Cream** (`#fbfbf5`) — a slightly warm off-white on the pricing
  page background, invisibly different from pure white but adding
  editorial warmth.
- **Hairline Light** (`#e4e4e7`) and **Hairline Dark** (`#1e2c31`) mark 1px
  borders and table dividers on each track respectively.

### Shade ladder & text
A five-step shade ladder (`#d4d4d8` → `#a1a1aa` → `#71717a` → `#52525b` →
`#3f3f46`) covers tag backgrounds, tertiary/secondary text on both
canvases, and the pressed state of the primary pill button. Text itself is
binary: **Ink** (`#000000`) on light canvas, **On Primary** (`#ffffff`) on
dark canvas and filled-pill labels.

## Typography

### Font family
The display tier is **Neue Haas Grotesk Display** at thin weights
(330-500), falling back to Helvetica at a light weight, then Arial — the
thin-weight cut is the brand, and no substitution should default to
weight 400+. The UI tier is **Inter Variable** at 420-550, a variable font
with sub-weight precision spanning body (420), strong (550), and caption
(500) without jumping to heavier tiers; Inter is open-source via Google
Fonts. The code tier is **ui-monospace**, the system mono, preferred over
a webfont to avoid unnecessary downloads.

The OpenType `ss03` stylistic set is enabled across every role, altering
specific glyph forms (lowercase `a`, `g`, single-story numerals) for a
slightly more geometric character — applied via `font-feature-settings:
"ss03"` on the body element or root.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale — display-xxl at
96px/330/+2.4px down to eyebrow-cap at 12px/400. Display thinness is the
brand: always render display sizes at weight 330, never 400+, since the
thinness is a deliberate editorial choice that makes the giant size feel
quiet. Display type stays in Neue Haas Grotesk Display; body roles never
get pushed up into it, and display roles never get pushed down into
Inter. Tracking lifts specifically at the 96px hero tier (+2.4px positive)
because the thin glyphs need air; at 70px and below, tracking returns to
zero.

### Font substitutes
Open substitutes for Neue Haas Grotesk Display are **Helvetica Now
Display** (proprietary) or **Inter Display** at light weights
(open-source) — avoid Helvetica Neue at default weight, since it's too
heavy for the brand's thin tier. Inter Variable is open-source via Google
Fonts and is the canonical body face, needing no substitute.

## Layout

- **Base unit:** 8px, with denser 2/4px sub-units for fine work.
- **Section padding:** 64-128px on cinematic marketing pages — extreme
  negative space is the point — collapsing to roughly 48px on
  transactional pages where density takes priority.
- **Card internal padding:** 32px on pricing cards, 24px on compact tag
  rows.
- **Grid & container:** cinematic hero pages use a wide max-width
  container (~1440-1600px) with edge-bleeding photography that escapes
  the container; pricing collapses through 4-up → 2-up → 1-up tiers by
  viewport; body content centers in a ~720-840px reading column on
  long-form pages.

The cinematic track treats whitespace as the brand's most valuable asset —
sections often carry 128-192px of vertical air between content blocks,
with photography filling the rest. The transactional track tightens to
roughly 48-64px between bands, because users there are scanning,
comparing, and acting. The contrast between the two whitespace
philosophies is itself part of the brand voice.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 | Flat, no shadow | Default surface |
| 1 | `0 1px 2px rgba(255,255,255,.05), inset 0 1px 0 rgba(255,255,255,.04)` | Subtle inset top-edge sheen on dark cards |
| 2 | `0 0 0 1px rgba(255,255,255,.08), 0 1px 3px rgba(0,0,0,.3), 0 5px 10px rgba(0,0,0,.2)` | Dark elevated cards — hairline + drop-shadow stack |
| 3 | Four stacked tiny shadows (1-8px offset, 10% black) | Pricing cards on light — a soft layered paper halo |
| 4 | `0 25px 50px -12px rgba(0,0,0,.25)` | Modal / floating panel on light |

On the cinematic track, depth comes from photography — full-bleed
merchant imagery layered behind cards, with subtle inset top-edge
highlights suggesting light hitting a glass surface. On the light track,
the layered tiny-shadow stack produces a soft, paper-like halo around
pricing cards — depth without harshness, and the brand's distinctive
light-mode elevation treatment.

## Shapes

| Token | Value | Use |
|---|---|---|
| `rounded.xs` | 4px | Inputs, hairline tags |
| `rounded.sm` | 5px | Small image containers |
| `rounded.md` | 8px | Form inputs, video frames, smaller cards |
| `rounded.lg` | 12px | Pricing cards, feature cards |
| `rounded.xl` | 20px (often top-only) | Hero photo frames, cinematic card chrome |
| `rounded.pill` | 9999px | All buttons, pill tags, mint chips |

Photography is full-bleed with no border — on cinematic pages it escapes
the container entirely, while on transactional pages it sits inside
12px-radius containers with no shadow. Customer-logo strips use simple
greyscale wordmarks at a uniform height (~24-32px) in a single horizontal
strip.

## Components

Full specs live in `design-tokens.yaml → components`. Summary:

- **Buttons** — `button-primary-pill` (the dominant CTA, black fill,
  pressed state lifts to shade-70), `button-outline-on-dark` (the
  cinematic hero CTA, white-stroked transparent pill), `button-outline-on-
  light` (the light-track equivalent), `button-aloe-pill` (the featured
  pricing CTA).
- **Cards & containers** — `card-pricing` / `card-pricing-featured` (mint
  fill distinguishes the featured tier, rather than a colored border),
  `card-feature-cinematic` (dark, often with the top-edge inset sheen),
  `card-pistachio-band` (wide horizontal category band), `card-photo-
  frame` (full-bleed photography container, zero inner padding — the
  photo IS the content).
- **Inputs** — `text-input` (standard light-canvas field).
- **Navigation** — `nav-bar-light` / `nav-bar-dark` (identical structure,
  logo left, nav center, two pill buttons right).
- **Pills, tags, chips** — `pill-tag-mint` / `pill-tag-shade` (small
  feature-category tags on light surfaces).
- **Signature components** — the Cinematic Photography Layer (full-bleed
  merchant photos with no overlay scrim, text living in clean negative
  space instead), and the Stacked Tiny Shadows elevation (four stacked
  tiny drop-shadows producing a soft paper halo on light pricing cards).
- **Inline & footer** — `link-on-dark` (no underline by default; tertiary
  footer links use the cool muted tones with a persistent underline),
  `footer-dark` / `footer-light` (4-5 column muted link groups, social
  icons, a small legal row).

## Do's and don'ts

**Do**
- Reserve aloe and pistachio for the light track only — they never appear
  on cinematic black pages.
- Always use pill radius for buttons; never `rounded.md` or `rounded.lg`.
- Render display tiers at weight 330 — bumping to 400 or 500 breaks the
  brand's thin-display signature.
- Use full-bleed photography on cinematic pages, letting it escape the
  container.
- Apply `font-feature-settings: "ss03"` globally — it's the brand's
  typographic signature.
- Pair black canvas with white type and white-stroked outline pills; pair
  light canvas with black type and filled-black pills.

**Don't**
- Don't introduce a third canvas color — stick to black or light/cream;
  greys, beiges, and blues aren't in the system.
- Don't add drop shadows on cinematic dark cards beyond the subtle inset
  top-highlight — the cinematic track wants flat blackness.
- Don't shrink display tiers below 48px on hero surfaces — below that
  they read as section heads, not display.
- Don't put aloe/pistachio green behind type — they're surface fills, not
  text colors.
- Don't replace the pill shape with a rounded-rectangle button anywhere.

## Responsive behavior

| Name | Width | Key changes |
|---|---|---|
| Wide | ≥1440px | Full cinematic hero with edge-bleeding photography; pricing 4-up |
| Desktop | 1024-1440px | Default content max-width; pricing 4-up tightens |
| Tablet | 768-1023px | Pricing → 2-up; cinematic hero photography crops |
| Mobile | <768px | Pricing → 1-up; hamburger nav; display-xxl drops to ~56-64px |

Pill buttons hit ≥44×44px on mobile via 12px vertical padding times 16px
line-height (WCAG AAA), and form fields hold a 44px minimum height at
every breakpoint. Display sizes scale down through the stair-step 96 → 70
→ 55 → 48 → 36px; cinematic photography crops aggressively at smaller
widths, prioritizing the focal subject over edge-bleed; pricing tiers
stair-step 4-up → 2-up → 1-up while the featured aloe tier stays visually
distinguished at every step; the top nav collapses to a hamburger below
768px, inheriting whichever canvas polarity the page is on. Photography
uses responsive `srcset` with art-direction crops at major breakpoints —
mobile crops favor close subjects, wide crops favor environmental/
storefront context.

## Known gaps

The source analysis is a narrative document built around a YAML token
frontmatter but without a dedicated "Known Gaps" section or per-component
hover-state documentation the way some of this collection's other
analyses provide. Values above are transcribed directly from its
frontmatter tokens and prose sections; anything not explicitly stated
there (hover-state colors beyond what's described, authenticated/logged-
in dashboard chrome, mobile screenshots) isn't documented in the source
and isn't invented here.
