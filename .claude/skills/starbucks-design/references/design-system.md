# Starbucks Design System — Full Analysis

Adapted from the Starbucks design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/starbucks/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Starbucks reads as a warm, confident retail flagship wearing the green of
its storefront apron across every surface. The canvas alternates between
a neutral-warm cream (`neutral-warm` `#f2f0eb`) and a slightly darker
ceramic off-white (`ceramic` `#edebe9`) — colors chosen to reference real
store materials: paper napkins, café walls, wood finishes. Signature
Starbucks Green (`starbucks-green` `#006241`) anchors the brand moment on
hero bands, CTAs, and the Rewards experience. The greens actually arrive
in four calibrated shades (Starbucks, Accent, House, Uplift), each mapped
to a specific surface role, while gold (`gold` `#cba258`) is reserved
strictly for Rewards-status ceremony rather than acting as a general
accent.

Typography carries most of the brand voice. The proprietary SoDoSans
typeface sits across nearly every surface at a tight `-0.16px` letter-
spacing, reading confident and friendly rather than fashion-magazine
severe. Two deliberate exceptions exist: the Rewards page switches to a
warm serif (`"Lander Tall", "Iowan Old Style", Georgia`) for specific
headline moments, echoing a coffeehouse chalkboard, and the Careers pages
use a handwritten script (`"Kalam", "Comic Sans MS", cursive`) for
personal cup-name touches. Three typefaces, three contexts — the system
never mixes them within a single surface.

Surfaces breathe through rounded geometry. Every button is a 50px full
pill. Cards take a 12px rounded rectangle. The "Frap" floating CTA — a
56px circular order button in Green Accent — is the product's signature
depth move: it floats bottom-right with a layered shadow stack (a 6px
base halo plus an 8px/12px ambient shadow) and compresses via
`scale(0.95)` on press. Elevation elsewhere stays restrained — card
shadows sit at a whispered 0.14/0.24 alpha, and the global nav uses a
quiet three-layer shadow stack. The whole system reads like clean café
signage: legible, warm, never shouting.

**Key characteristics:**
- Four-tier green brand system (Starbucks / Accent / House / Uplift),
  each mapped to a distinct surface role — not one flat "brand green."
- Gold reserved for Rewards-status moments only; never a general-purpose
  accent.
- Warm-neutral canvas (`#f2f0eb` / `#edebe9`) instead of cold white,
  referencing café materials.
- Custom proprietary SoDoSans typeface with tight `-0.16px` letter-
  spacing as the universal voice.
- Context-specific type switches: serif for Rewards, script for Careers
  cup-names.
- Full-pill buttons (50px radius) with a `scale(0.95)` active press as
  the signature micro-interaction.
- Floating circular "Frap" CTA (56px, Green Accent, layered shadow
  stack) — the product's signature elevation element.
- Gift-card surfaces designed as photographed physical products — each
  card is a distinct illustrated photograph, not a generated graphic.
- 12px card radius plus whisper-soft shadows keep content cards flat-
  plus-hint-of-lift.
- Rem-based spacing anchored at 1.6rem (~16px), stepping to 6.4rem
  (~64px).
- Color-block page rhythm: cream hero → white content → dark-green
  feature band → cream utility zone → dark-green footer, an espresso-
  dark bookend around a bright body.

## Colors

### Primary
- **Starbucks Green** — the historic brand green; h1 headings, primary
  section headers, and the main brand signal wherever a single dominant
  color is needed.
- **Green Accent** — a brighter, more luminous green; the primary
  filled-CTA color and the fill of the floating Frap button.
- **House Green** — the deep near-black brand green; footer surface,
  feature-band backgrounds, reward-status dark surfaces, and the Rewards
  hero band.
- **Green Uplift** — a secondary mid-dark green for decorative accents
  and dark-gradient moments.
- **Green Light** — a pale mint wash for form-valid-state tints and
  light utility surfaces.

### Secondary & accent
- **Gold** — Rewards-status ceremony, tier callouts, partnership badges,
  premium accents; never a general-purpose brand color.
- **Gold Light** — softer gold for background washes on gold-tier
  sections.
- **Gold Lightest** — cream-gold page wash under partnership sections.

### Surface & background
- **White** — primary card/modal surface, also gift-card tile fill.
- **Neutral Cool** — subtle cool-gray for dropdown menus and quiet
  utility containers.
- **Neutral Warm** — the warm-cream primary page canvas.
- **Ceramic** — a slightly warmer/darker cream for zone separators and
  soft section washes.
- **Black** — reserved for the dark top-of-page CTA strip and
  high-contrast sign-in buttons.

### Neutrals & text
- **Text Black** (`rgba(0,0,0,0.87)`) — primary heading/body text; not
  pure black, reads warmer.
- **Text Black Soft** (`rgba(0,0,0,0.58)`) — secondary/metadata text.
- **Text White** — primary heading/body text on dark-green surfaces.
- **Text White Soft** (`rgba(255,255,255,0.70)`) — secondary text on
  dark-green surfaces.
- **Rewards Green** — a dedicated muted slate-green used only on
  Rewards-page text blocks, dustier than Text Black, signaling "reward
  surface" without full Starbucks Green.

### Semantic
- **Red** — error/destructive states.
- **Yellow** — warning state, a legacy brand touch.
- Two translucent alpha ladders (black and white, 10% steps) handle
  overlays and secondary text on both light and dark surfaces.

There is no structural gradient system — surface hierarchy is
solid-color-block throughout, relying on the five-tier cream/green
palette rather than gradients.

## Typography

### Families
- **Primary** — SoDoSans (proprietary, licensed from House Industries),
  used across nearly every surface.
- **Rewards serif** — `"Lander Tall", "Iowan Old Style", Georgia` for
  specific Rewards headline moments.
- **Careers script** — `"Kalam", "Comic Sans MS", cursive`, exclusive to
  Careers "cup name" decorative touches.

Open-source substitutes for SoDoSans: **Inter** or **Manrope** (similar
humanist geometric proportions and confident feel) or **Nunito Sans**
(warmer, café-brand fit). If substituting, verify the tight `-0.01em`/
`-0.16px` tracking still reads well — some open fonts need `-0.005em`
instead. Lander Tall substitutes: Iowan Old Style, Lora, or Source Serif
Pro. Kalam is already free on Google Fonts.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale (display-10 at
80px down to micro-1 at ~13px). Governing principles:
- Tight negative tracking (`-0.01em`) is nearly universal — the product
  reads slightly compressed, giving SoDoSans a confident presence without
  feeling squeezed.
- Weight shifts carry hierarchy more than size shifts: h1 and h2 share
  the same 24px/36px size, separated only by weight (600 vs 400) and
  color (Starbucks-Green vs Text Black).
- The size scale is rem-based and anchored at `1rem = 10px` via a
  62.5%-root trick, so it's semantic (text-1 through text-10) rather than
  arbitrary pixel values.
- Context-specific typeface swaps (serif on Rewards, script on Careers)
  are deliberate and localized — never mixed with the primary sans on
  the same surface.
- Body text never goes pure black; it sits at `rgba(0,0,0,0.87)` to match
  the warm-neutral canvas temperature.

## Components

Definitions live in `design-tokens.yaml → components`. Summary:
- **Buttons** — primary filled, primary outlined, black filled ("Join
  now"), dark outlined ("Sign in"), green-on-green inverted (white
  button on a dark-green band), outlined-on-dark, and a consent-agree
  variant — all sharing the 50px pill and `scale(0.95)` active press.
- **Frap** — the floating circular order button, the system's signature
  elevation element, plus a top-rounded full-width feedback tab.
- **Cards** — the default content card (12px radius, whisper-soft dual
  shadow), photographed gift-card tiles, three-column Rewards status
  cards on House Green, and cream-gold partnership cards.
- **Forms** — floating-label inputs with animated label size/position,
  valid/invalid tint states, and a springy checked-input transition.
- **Navigation** — a fixed global nav that grows progressively across
  breakpoints (64 → 72 → 83 → 99px) with a soft three-layer shadow.
- **PDP cluster** — a repeating product-detail component set: a size
  selector with a green ring on the active cup icon, add-in/milk select
  fields, a numeric stepper, a "Customize" pill with a gold sparkle icon,
  an "Add to Order" pill, a gold-outlined Rewards cost pill, a dark-green
  product-description band, and a two-column nutrition table.

## Layout

- Rem-based spacing scale anchored at `1rem = 10px`, from `space-1`
  (4px) up to `space-9` (64px); `1.6rem`/16px is the single most
  frequent spacing unit across the whole system.
- Outer gutters scale from 16px (mobile) to 24px (tablet) to 40px
  (desktop).
- Column-width scale: small (343px), medium (500px), large (720px),
  xlarge (1440px).
- Gift-card grid: 3-5 up responsive grid of ~343px tiles; Rewards status
  panels are 3-up at `lg+` breakpoints; the hero splits 40% image / 60%
  content.
- Whitespace carries the feeling of "plenty of space in the café" —
  generous 40-64px section padding, content blocks separated by
  whitespace rather than dividers, with the cream canvas itself acting as
  a visual breath between white cards and green feature bands.

## Shapes

| Value | Use |
|---|---|
| 12px | Cards, modals, menu-item tiles |
| 12px 12px 0 0 | Top-rounded-only feedback tab |
| 50px | All buttons — the universal full-pill radius |
| 50% | Circular icons, the Frap button, avatar thumbnails |
| 3.3333%/5.298% | Elliptical radius for Starbucks-Visa-Card mockups |

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| Card | `0 0 0.5px rgba(0,0,0,0.14), 0 1px 1px rgba(0,0,0,0.24)` | Default content cards — a whisper-soft dual shadow |
| Global nav | Triple-layer soft shadow | Fixed top bar |
| Frap base | `0 0 6px rgba(0,0,0,0.24)` | Base halo around the floating CTA |
| Frap ambient | `0 8px 12px rgba(0,0,0,0.14)` | Stacked directional ambient shadow |
| Gift card | Light drop shadow around illustrated photography | Physical-card feel |
| Starbucks Card (SVC) | Stacked SVG drop-shadow filters | Starbucks Card visuals |

The shadow philosophy is whisper-soft and layered over solid: the system
never reaches for one heavy drop shadow, instead stacking 2-3 low-alpha
shadows at different offsets to simulate ambient plus direct lighting.
The Frap button is the single most elevated element on any page. There is
no gradient system anywhere — color-block banding (dark-green bands
reading as "recessed" zones between cream/white sections) is what carries
perceived depth instead.

## Do's and don'ts

**Do**
- Use the warm cream or ceramic canvas instead of pure white — it is the
  brand's signature temperature.
- Map each green to its intended role rather than using one flat brand
  green everywhere.
- Keep SoDoSans tracking tight (`-0.01em`/`-0.16px`) across the system.
- Use the 50px full-pill radius on every button, without exception, and
  the `scale(0.95)` active press as the universal micro-interaction.
- Reserve gold strictly for Rewards-status ceremony.
- Use SoDoSans for nearly everything; switch to the serif only for
  Rewards editorial headlines and the script only for Careers cup-name
  moments.
- Layer 2-3 low-alpha shadows rather than one heavier drop shadow.
- Let the cream canvas breathe between cards through whitespace, not
  dividers.

**Don't**
- Don't use pure white as the page canvas.
- Don't collapse the four-green system into a single `#006241` everywhere
  — it flattens the brand.
- Don't use gold as a general-purpose accent.
- Don't square the corners on buttons; the 50px pill is universal.
- Don't introduce gradient fills; the system is color-block throughout.
- Don't distinguish h1 from h2 by size; the hierarchy comes from weight
  and color.
- Don't use pure black for body text.
- Don't skip the `scale(0.95)` active-press feedback on buttons.
- Don't stack a single heavy shadow where 2-3 low-alpha layers belong.
- Don't introduce serifs or scripts into the main shopping flow — they
  belong to Rewards and Careers respectively.

## Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| xs | <480px | Nav at 64px; hamburger menu; single column; full-width pills |
| Mobile | 480-767px | Nav at 72px; gift-card grid 2-up; card padding tightens |
| Tablet | 768-1023px | Nav at 83px; gift-card grid 3-up; hero split begins |
| Desktop | 1024-1439px | Nav at 99px; gift-card grid 4-up; full 40/60 hero |
| XLarge | 1440px+ | Content caps at max column width; gift-card grid 5-up |

Pill buttons at `7px 16px` padding measure roughly 32px tall — below the
44px WCAG AAA touch minimum, so mobile padding should expand to reach the
minimum. The Frap button, at 56px, clears the minimum comfortably and
extends its tap area with a small negative touch offset. Floating-label
form inputs grow their label size on mobile for easier reading and
tapping at arm's length. Across breakpoints, the global nav height scales
progressively rather than jumping; the hero splits from asymmetric 40/60
to stacked; the gift-card grid steps 5 → 1 columns; feature bands stay
full-width but stack their text and imagery vertically; and Rewards'
3-column status panels collapse to a single column on mobile.

## Known gaps

- SoDoSans is proprietary and not on Google Fonts — use Inter or Manrope
  and document the swap when implementing publicly.
- Lander Tall (the Rewards serif) is also custom; substitute with Iowan
  Old Style, Lora, or Source Serif Pro.
- Per-component animation timings beyond the few documented values
  (`0.4s` general duration, `0.2s` icon transition, `300ms` expander) are
  not captured for every interactive surface.
- Form error-state styling (border weight, icon placement) is only
  partially documented via the tint tokens.
- Careers-page-specific components (the cup-name card, the search radio
  grid) are referenced by token names but not fully specified.
- Starbucks Visa Card / Starbucks-Card mockup specs are only hinted at by
  the elliptical-radius and SVG-shadow-filter tokens.
