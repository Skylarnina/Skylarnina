# Lovable Design System — Full Analysis

Adapted from the Lovable design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/lovable/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Lovable's site trades the cold-white convention of most developer tools for
a warm, paper-like parchment tone (`colors.cream`, `#f7f4ed`). Near-black
charcoal text (`colors.charcoal`, `#1c1c1c`) sits on that cream at a contrast
that stays sharp without feeling sterile. The custom Camera Plain Variable
typeface carries the brand's personality: its rounded terminals and organic
curves read as humanist rather than geometric, and its variable-weight axis
lets the system use in-between weights like 480 for special display
moments.

The system's most unusual trait is that it has almost no distinct gray
hex values — every "shade" on the page is really the same charcoal color at
a different opacity (3%, 4%, 40%, 82%, 83%, 100%). That single-hue-many-
opacities approach gives the whole page a tonal coherence that's hard to get
by picking grays independently. Borders (`colors.light-cream`, `#eceae4`)
do the job shadows would normally do; the one shadow the system leans on is
a multi-layer inset applied to dark buttons, giving them a tactile,
pressed-into-the-surface look rather than a hovering one.

**Key characteristics:**
- Warm parchment canvas (`#f7f4ed`) instead of white — deliberately chosen,
  not a default.
- Camera Plain Variable with humanist warmth; display sizes get aggressive
  negative tracking (-0.9px to -1.5px).
- Every neutral gray is the same charcoal hue at varying opacity — never an
  arbitrary independent hex value.
- Signature multi-layer inset shadow on dark buttons for tactile depth.
- Borders (`#eceae4`) instead of drop shadows for card containment.
- Full-pill radius (9999px) reserved for icon buttons and action toggles,
  never for rectangular CTAs.
- Built on shadcn/ui + Radix primitives with Tailwind utility styling.

## Colors

### Primary
- **Cream** — page background, card surfaces, and most button surfaces; the
  foundation of the whole palette.
- **Charcoal** — primary text, headings, dark button backgrounds.
- **Off-white** — button text on dark backgrounds; almost indistinguishable
  from pure white but intentionally warmer.

### Neutral scale (opacity-based)
The system has no separate neutral-gray palette. Instead `colors.charcoal`
is reused at descending opacities: 100% for primary text, 83%/82% for
strong secondary text and body copy, 40% for interactive borders, and 3-4%
for barely-visible hover tints and overlays. A distinct `muted-gray` hex
(`#5f5f5d`) covers secondary text and captions where the opacity approach
isn't used.

### Surface & border
- **Light cream** (`#eceae4`) — the warm divider line used for card
  borders, dividers, and image outlines.
- **Cream surface** — identical to the page background, so cards blend
  seamlessly into the page rather than standing apart.

### Interactive
- **Ring blue** — the Tailwind focus-ring color, used sparingly for
  keyboard accessibility rather than as a brand accent.
- The dark-button inset shadow (a white highlight line at the top, a dark
  ring, and a soft drop beneath) is the system's signature depth technique.

## Typography

### Family
Camera Plain Variable is the only typeface in the system, with
`ui-sans-serif, system-ui` as fallbacks. It runs on a continuous variable
weight axis, which lets the system dial in nuanced stops like 480 (a
display weight lighter than semibold but stronger than regular) alongside
the two fixed stops actually used elsewhere: 400 for body/UI and 600 for
headings.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale (display-hero at
60px down to caption at 14px). Principles:
- Headline tracking compresses aggressively as size grows: -1.5px at 60px
  down to normal at 16px body text.
- Two weights only — 400 for everything except headings, 600 for headings.
  700 (bold) never appears.
- Weight 480 is reserved for a single special "lighter than semibold"
  display variant, used sparingly.

## Layout

- Base spacing unit: 8px, with the scale widening generously at the top end
  (8px up through 208px) to give editorial sections room to breathe.
- Max content width sits around 1200px, centered.
- Hero sections use single-column centered layout with very generous
  vertical padding (96px or more).
- Feature sections run 2-3 column grids; the footer uses a full-width
  multi-column link layout.
- Tight internal card padding (12-24px) deliberately contrasts with wide
  section gaps (80-208px), giving the page an alternating rhythm of focused
  content and visual rest.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| Flat | No shadow, cream background | Page surface, most content |
| Bordered | `1px solid #eceae4` | Cards, images, dividers |
| Inset | multi-layer inset shadow (white highlight + dark ring + soft drop) | Dark primary buttons |
| Focus | `rgba(0,0,0,0.1) 0px 4px 12px` diffused shadow | Active/focus states |
| Ring | `rgba(59,130,246,0.5)` 2px ring | Keyboard focus on inputs |

The system's depth is intentionally shallow — no dramatic drop-shadowed
floating cards. The inset-shadow technique on dark buttons is the only
notable shadow pattern; everything else relies on the `#eceae4` border for
containment. The warm, diffused focus shadow deliberately reads as a soft
glow rather than a sharp outline.

### Decorative depth
The hero and footer carry a soft, barely-visible multi-color gradient wash
(pinks, oranges, blues) behind the content — atmospheric rather than
graphic. There are no harsh section dividers; spacing and the cream
background's warmth handle the transitions between sections.

## Shapes

| Token | Value | Use |
|---|---|---|
| micro | 4px | small buttons, interactive elements |
| standard | 6px | buttons, inputs, nav menu |
| comfortable | 8px | compact cards, divs |
| card | 12px | standard cards, image containers, templates |
| container | 16px | large containers, footer sections |
| full | 9999px | action pills, icon buttons, toggles only |

## Components

Definitions live in `design-tokens.yaml → components`. Summary:
- **Buttons** — primary dark (with the signature inset shadow), ghost/
  outline, cream-surface tertiary, and pill icon buttons for secondary
  actions like voice recording or plan-mode toggles.
- **Cards** — standard cards use cream backgrounds with `#eceae4` borders
  and no box-shadow; image cards keep a consistent 12px radius.
- **Inputs** — cream background, `#eceae4` border, ring-blue focus outline.
- **Distinctive components** — a large AI chat input with soft borders and
  pill-shaped voice/plan-mode toggles; a template gallery of image+title
  cards; a stats bar with large 48px+ numbers over muted descriptive text.

## Do's and don'ts

**Do**
- Use the warm cream background as the page foundation.
- Set display type in Camera Plain Variable with negative tracking (-0.9px
  to -1.5px).
- Derive every gray from charcoal at varying opacity, not independent hex
  values.
- Use the inset-shadow technique on dark buttons.
- Use `#eceae4` borders instead of shadows for card containment.
- Keep the weight system narrow: 400 for body/UI, 600 for headings.
- Reserve full-pill radius (9999px) for icon/action buttons only.
- Apply 0.8 opacity on active/pressed states for tactile feedback.

**Don't**
- Don't use pure white (`#ffffff`) as a page background.
- Don't use heavy box-shadows for cards — borders are the containment
  mechanism.
- Don't introduce saturated accent colors — the palette is warm-neutral.
- Don't use weight 700 (bold) — 600 is the system's maximum.
- Don't apply 9999px radius to rectangular buttons.
- Don't use sharp, hard-edged focus outlines — use soft shadow-based focus.
- Don't mix border styles inconsistently — `#eceae4` for passive borders,
  40%-opacity charcoal for interactive ones.
- Don't loosen letter-spacing on headings — Camera Plain is designed to run
  tight at scale.

## Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Mobile small | < 600px | Tight single column, reduced padding |
| Mobile | 600-640px | Standard mobile layout |
| Tablet small | 640-700px | 2-column grids begin |
| Tablet | 700-768px | Card grids expand |
| Desktop small | 768-1024px | Multi-column layouts |
| Desktop | 1024-1280px | Full feature layout |
| Large desktop | 1280-1536px | Maximum content width, generous margins |

Touch targets stay comfortable throughout: 8px/16px button padding, pill
buttons with generous 9999px radius for large tap targets, adequately
spaced nav items. Hero headline scales 60px → 48px → 36px with proportional
tracking reductions; feature card grids step 3-up → 2-up → single column;
section spacing compresses from 128px+ down to 64px on mobile. Template
screenshots keep their `#eceae4` border and 12px radius at every size.

## Known gaps

- Camera Plain Variable is proprietary; the fallback stack (`ui-sans-serif,
  system-ui`) is what the live site itself declares, so no dedicated
  open-source substitute has been verified.
- The exact opacity boundary between "muted gray" text and charcoal-at-82%
  isn't fully disambiguated in the source captures — treat `#5f5f5d` as the
  practical stand-in for secondary text.
- Dark-mode token values are not documented — the marketing site does not
  appear to ship one.
- This skill's token file was reconstructed from the source DESIGN.md's
  prose tables (the source has no machine-readable frontmatter block, unlike
  some of the other brand analyses this skill collection covers), so treat
  the yaml as a faithful transcription rather than an extracted CSS dump.
