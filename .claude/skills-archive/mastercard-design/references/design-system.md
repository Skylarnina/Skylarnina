# Mastercard Design System — Full Analysis

Adapted from the Mastercard design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/mastercard/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Mastercard's site reads like a warm editorial magazine built on stone-toned
paper and signal orange. The canvas is a muted putty-cream
(`colors.canvas-cream`, `#F3F0EE`) — closer to premium annual-report paper
than to a typical white SaaS background — and nearly everything placed on
it is shaped like a stadium, a pill, or a perfect circle. The dominant
gesture is oversized radius: heroes get 40px corners, cards go fully
pill-shaped, service images crop into circular orbits, and buttons complete
either the pill or a snug 20px. Sharp corners are almost entirely absent.

The second gesture is orbit and trajectory. Circular image portraits don't
sit still visually — thin, hand-drawn-feeling orange arcs connect them
across the full viewport width, so the page reads as a constellation of
services rather than a plain list. Each circle carries a small "satellite"
— a white micro-CTA with an arrow icon docked onto its edge like a moon —
which is the system's single most recognizable detail: the circles feel
like they're mid-motion even on a static page.

Typography runs entirely in MarkForMC, Mastercard's proprietary geometric
sans. Headlines sit at a medium weight (500) with tight negative tracking
(-2%), reading confident without shouting. Body copy uses the same family
at an unusually light half-step weight (450) — softer than a plain 400,
chosen deliberately because it reads gentler than "regular" while still
holding its shape. Put together — cream surfaces, pill shapes, circular
portraits, orange orbit lines, black CTAs — the system holds a tension
between institutional (a decades-old payments network) and editorial (a
modern brand magazine), which is exactly the balance Mastercard wants.

**Key characteristics:**
- Warm cream canvas (`#F3F0EE`) in place of white on every surface.
- Extreme border-radius vocabulary: 40px, 99px, and 1000px dominate;
  anything closer to square reads as a third-party widget.
- Circular image portraits with attached white satellite CTAs and traced
  orange orbital connector lines.
- Ghost "watermark" headlines — cream-on-cream text at heading scale —
  layered behind circle portraits.
- Black primary CTAs at 20px radius carry the marketing body; the
  cookie-banner orange stays in consent flows only.
- A floating pill-shaped navigation bar that docks just below the viewport
  top with rounded shoulders.
- Eyebrow labels pairing a tiny accent dot with uppercase bold tracking as
  the section-category signal.
- A dark warm-black footer (`#141413`) with a four-column link layout and a
  large conversational headline.

## Colors

### Brand & accent
- **Logo red / logo yellow** — the two halves of the Mastercard mark;
  brand-asset only, never used as UI color.
- **Ink black** (`#141413`) — the warm near-black used for primary CTAs,
  headline text, and the footer. The slight warmth in the value keeps it
  from reading as jet-black against the cream canvas.

### Secondary & accent
- **Signal orange** (`#CF4500`) — a deep, rust-leaning orange reserved for
  consent actions and eyebrow dots; the page's single aggressive color and
  used sparingly by design.
- **Light signal orange** (`#F37338`) — a lighter carroty orange used for
  carousel indicators and the decorative orbital arcs; always an attention
  cue, never body color.
- **Clay brown** (`#9A3A0A`) — a deep rust used for secondary link-style
  buttons such as cookie-detail links.

### Surface & background
- **Canvas cream** (`#F3F0EE`) — the default page canvas that every
  editorial section sits on.
- **Lifted cream** (`#FCFBFA`) — one step lighter, used for nested "raised"
  sections that want a paper-on-paper feel.
- **White** — reserved for the floating nav pill, modal cards, secondary
  button fills, and the small satellite CTAs attached to portraits.
- **Soft bone** (`#F4F4F4`) — a cooler-gray surface used in a handful of
  component subregions.

### Neutrals & text
- **Ink black** and **charcoal** (`#262627`) — primary and slightly softer
  text alternates.
- **Slate gray** (`#696969`) — muted secondary text, disabled states, and
  privacy-row copy.
- **Granite** (`#555555`) / **graphite** (`#565656`) — deeper grays for
  inline accents and alternate links.
- **Dust taupe** (`#D1CDC7`) — very low-contrast cream-gray used only for
  disabled or "whisper" text.

### Semantic & accent
- **Link blue** (`#3860BE`) — a dusty, deliberately-not-neon blue for
  inline links and informational callouts.

### Gradients
Mastercard uses no programmatic gradients. The gradient impression comes
from two places instead: warm-orange photo subjects fading to the cream
canvas at the edge of circular portraits, and deep soft-halo shadows
(`rgba(0,0,0,0.08) 0px 24px 48px`) beneath pill-shaped media.

## Typography

### Family
MarkForMC is the proprietary geometric sans used for every headline,
paragraph, button, nav link, and footer link. A secondary cut,
MarkOffcForMC, appears in a minority of contexts (legal text, some forms).
The declared fallback stack is Sofia Sans → Arial.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale. Principles:
- Weight 450 is load-bearing for body copy — most brands stop at 400/500/
  700, and replacing 450 with plain 400 flattens the identity.
- Headlines carry tight negative tracking (-2%), which locks words together
  rather than letting them breathe — the source of the system's editorial
  density.
- Uppercase tracking is reserved for the 14px eyebrow scale only; nothing
  else in the system goes uppercase.
- It's a one-font system by design — contrast comes from scale, weight, and
  letter-spacing rather than a second typeface.
- Line-height ratio drops as size grows: roughly 1:1 at the hero size, 1.2
  at card-title size, 1.4 at body size — tight display, comfortable
  reading.

### Note on font substitutes
MarkForMC is proprietary. Sofia Sans (Google Fonts) is the closest open
match and is already in Mastercard's own fallback stack; Inter at weights
450/500/700 works as a generic stand-in (expect a slightly taller x-height);
Neue Haas Grotesk or Geist can approximate the geometric feel. Whatever
substitute is used, keep the -2% headline tracking and the 450 body weight
(use `font-weight: 450` on a variable font, or fall back to 400 and tighten
tracking by roughly -0.5% to compensate).

## Layout

### Spacing system
- Base unit: 8px, confirmed by direct extraction.
- Scale: 8 / 16 / 24 / 32 / 48 / 64 / 96 / 128 (clean powers of 8).
- Section vertical padding: roughly 96-128px between major desktop
  sections, compressing to 48-64px on mobile.
- Card internal padding: 32-40px desktop, ~24px mobile.
- The floating nav pill sits about 24px below the viewport top rather than
  flush against it.

### Grid & container
- Max content width sits around 1200-1280px, with 48-100px horizontal
  gutters.
- A 12-column grid is implied, but practical layouts favor 2-up asymmetric
  splits (headline left, supporting copy right), full-bleed 1-up sections
  for hero/video, or staggered single-portrait placement that creates the
  "constellation" feel.
- The footer runs 4 equal columns on desktop, collapsing to a single-column
  accordion on mobile.

### Whitespace philosophy
Whitespace is treated as structure, not absence. A typical service section
gives a ghost headline the top ~40% of the section (mostly empty cream),
places a single circular portrait asymmetrically around 60% down, and
leaves 300-500px of blank canvas before the next section — a deliberate
"slow down, read one thing at a time" pacing that's the opposite of a dense
dashboard UI.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 | No shadow | ~95% of surfaces sit flat on the cream canvas |
| 1 | `rgba(0,0,0,0.04) 0px 4px 24px 0px` | Floating nav pill — barely-there lift |
| 2 | `rgba(0,0,0,0.08) 0px 24px 48px 0px` | Hero media frames, elevated cards — a soft, wide halo rather than a hard drop |
| 3 | `rgba(0,0,0,0.25) 0px 70px 110px 0px` | Rare dramatic elevation on a feature tile |

Shadows act as atmospheric cushioning rather than directional light — the
level-2 shadow spreads 48px at only 8% opacity, so it barely registers as
dark pixels but gives the sense that a card is "breathing" above the
canvas. Hard-edged, tight shadows almost never appear; functional
delineation (form inputs, footer dividers) prefers a border line instead.

### Decorative depth
Orbital arcs in light signal orange trace connective paths between
sections; ghost watermark headlines in cream-on-cream give sections an
almost-pressed-paper quality; and warm-toned photography dissolving at the
edge of circular portraits implies soft atmospheric depth without any
actual shadow.

## Shapes

| Token | Value | Use |
|---|---|---|
| micro | 3-6px | Tiny decorative elements, cookie-banner micro-chips |
| button | 20px | Primary and secondary body CTAs — the signature button radius |
| consent-pill | 24px | Consent/orange pill buttons, modal inner chips |
| hero | 40px | Hero media frames, large section containers, H2 pill labels |
| circle | 50% | Circular portraits, icon-only buttons, satellite CTAs |
| pill | 999-1000px | Full-pill shapes — nav, carousel cards, footer selector, primary chips |

Unlike a typical 4/8/12/16 scale, Mastercard skips the 8-12px middle ground
entirely and commits to either small (≤6px), medium-large (20-40px), or
full-pill (99px+) — which is exactly why the UI reads as either "precise
utility" or "soft editorial" with nothing in between.

## Components

Definitions live in `design-tokens.yaml → components`. Summary:
- **Buttons** — ink pill primary, outlined-pill secondary, orange consent
  pill (legally-distinct actions only), satellite circular micro-CTA, and
  icon-only circle buttons for carousels/play controls.
- **Hero media frame** — a "stadium" shape at 40px radius spanning near-full
  viewport width, no shadow, sitting directly on canvas.
- **Service/solution portrait card** — a perfect circle or ellipse crop
  (260-340px desktop) with a satellite CTA docked bottom-right and a
  connecting orbital line to the next card.
- **Pill carousel card** — full-pill or stadium-rounded media panel with
  overlaid chip labels and an oversized inline CTA.
- **Ghost watermark text block** — 72-128px cream-on-cream headline layered
  behind foreground content.
- **Search & country selector** — a circular search button that expands
  into a full pill input; a pill-shaped country/language selector in the
  footer.
- **Floating nav pill** — desktop navigation as a translucent-white pill
  floating just below the viewport top, collapsing to logo + hamburger +
  search on mobile.
- **Footer** — ink-black background, a large conversational H2, a 4-column
  link grid, and a bottom row of legal links, the language pill, and social
  icons.

## Do's and don'ts

**Do**
- Use canvas cream (`#F3F0EE`) as the default body background — never pure
  white.
- Mask service/feature imagery as perfect circles, never rectangles or
  rounded rectangles.
- Attach a white satellite CTA to the bottom-right of every circular
  portrait.
- Set headlines in weight 500 with -2% letter-spacing.
- Use weight 450, not 400, for body paragraphs.
- Keep primary CTAs as ink-black pills at 20px radius with cream text.
- Reserve signal orange for consent, legal, or compliance actions only.
- Float the nav as a rounded white pill below the viewport top, not flush
  at the very edge.
- Build page rhythm from three surface tones: canvas cream → lifted cream →
  ink footer.
- Use thin light-signal-orange arcs between service cards to imply
  connection.

**Don't**
- Don't use pure white as a page background — it breaks the warm editorial
  tone.
- Don't round image frames at 8-16px — commit to full-pill, 40px, or
  full-circle; anything in between looks generic.
- Don't use signal orange for marketing CTAs — it reads as cookie-consent
  and dilutes the legal signal.
- Don't mix typefaces — no serif accent, no script, no secondary display
  font.
- Don't crowd the nav with more than six top-level links — the pill is
  meant to feel airy.
- Don't drop hard shadows — elevation should stay at 48px+ spread and ≤10%
  opacity.
- Don't use uppercase for anything larger than the 14px eyebrow label.
- Don't omit the small accent dot before eyebrow labels — it's part of the
  identity.
- Don't place circular portraits on a rigid grid — their effect depends on
  asymmetric placement.

## Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Mobile | ≤ 767px | Nav pill shows logo + menu + search only; primary links hide behind hamburger; portraits stack single-column; hero headline drops from 64px to ~40px; footer collapses to vertical accordion |
| Tablet | 768-1023px | Nav shows 2-3 truncated primary links; portraits arrange 2-up; hero headline ~48px |
| Desktop | ≥ 1024px | Full nav with 5 primary links centered; portraits asymmetrically placed with orbital lines; hero headline 64px |
| Wide | ≥ 1440px | Content max-width caps around 1280px; gutters grow symmetrically; orbital lines extend further |

All interactive elements comfortably exceed 44×44px touch targets: the
satellite CTA runs 50-60px, nav pill buttons about 48px, mobile hamburger
and search 48×48px, and no link or button drops below 40px at any
breakpoint. Navigation keeps its pill shape at every size — full pill on
desktop, compact pill with hamburger on mobile. The service grid collapses
from an asymmetric constellation to 2-up to a single stack, dropping the
orbital arcs on mobile since they depend on asymmetric placement. Section
padding compresses from 128px to 48px, and the two-column hero (headline
left, supporting text right) becomes a stacked layout below desktop.

## Known gaps

- MarkForMC is a proprietary licensed typeface; Sofia Sans is the closest
  open-source substitute and is already in Mastercard's own declared
  fallback stack.
- Tablet-specific layout details (768-1023px) were inferred from desktop
  and mobile captures rather than observed directly.
- The exact "whisper" cream tone used behind ghost-watermark headlines
  reads somewhere between `#E8E2DA` and `#D1CDC7` across different section
  captures; treat it as an approximation.
- The consent orange (`#CF4500`) is Mastercard's documented compliance
  signal and should never be confused with a marketing CTA color.
- The full-color logo mark (red + yellow) is a brand asset, not a UI
  palette entry.
- This skill's token file was reconstructed from the source DESIGN.md's
  prose tables (the source has no machine-readable frontmatter block,
  unlike some of the other brand analyses this skill collection covers),
  so treat the yaml as a faithful transcription rather than an extracted
  CSS dump.
