# Webflow Design System — Full Analysis

Adapted from the Webflow design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/webflow/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Webflow bills itself as the visual web development platform, and its
marketing surface reads as a confident professional product rather than a
scrappy startup. The default page sits on a generous white
`colors.canvas`, with a deep near-black `colors.primary` (`#080808`)
carrying the brand's primary CTA, typography, and ink. Around that
restrained core, the brand layers a five-stop chromatic accent system —
`colors.accent-purple` (`#7a3dff`), `colors.accent-pink` (`#ed52cb`),
`colors.accent-blue` (`#3b89ff`), `colors.accent-orange` (`#ff6b00`), and
`colors.accent-green` (`#00d722`) — each mapped to a platform product
category (design, CMS, hosting, ecommerce, and so on). These accents show
up as full-card fills inside the product-category grid, never as button
colors; the primary CTA stays near-black throughout.

Typography is the second decisive voice. The proprietary `WF Visual Sans
Variable` family covers every display, body, and label role at weight
500/600 — Webflow never goes heavier than semibold and never lighter than
regular. The hero display sits at 80px, weight 600, -0.8px tracking:
confident without shouting. Uppercase eyebrows at 15px/500 with +1.5px
positive tracking mark every section header.

The shape system stays restrained. Buttons take a tight `rounded.sm` 4px
radius — neither pill nor square — reading as engineered rather than
friendly. Cards step up to `rounded.md` 8px. The full pill (`rounded.full`
9999px) is reserved strictly for circular icon containers. Layered
drop-shadows add modest lift to featured cards without ever feeling
material-heavy.

**Key characteristics:**
- A two-color conversion hierarchy: near-black for every primary CTA,
  white-with-hairline for every secondary. Chromatic accents live only on
  category-card fills, never on buttons.
- The signature move is the five-stop chromatic category palette — purple,
  pink, blue, orange, green — each tied to a product surface and used at
  full saturation.
- Hero typography sits at 80px weight 600 with -0.8px tracking — confident,
  never billboard-loud.
- WF Visual Sans Variable is the single family across the system; there's
  no separate face for body versus display. WFVisualSans-Mono handles only
  rare technical captions.
- Tight 4px button geometry with 8px card corners — the brand never uses
  pill CTAs.
- Layered multi-offset drop-shadows on featured cards are the brand's only
  elevation cue.

## Colors

### Brand & accent
- **Ink black** (`colors.primary`, `#080808`) — the primary conversion
  color: every primary CTA, every heading, every wordmark. Deeper than
  pure black to read as intentionally branded.
- **Accent purple** (`colors.accent-purple`, `#7a3dff`) — one of the five
  chromatic category accents, used for design/build product surfaces.
- **Accent pink** (`colors.accent-pink`, `#ed52cb`) — magenta accent for
  animation/interaction product surfaces.
- **Accent blue** (`colors.accent-blue`, `#3b89ff`) — bright cyan-blue for
  SEO/analytics product surfaces, with `colors.accent-blue-deep`
  (`#006acc`) for emphasis links and `colors.accent-blue-info`
  (`#146ef5`) for info badges.
- **Accent orange** (`colors.accent-orange`, `#ff6b00`) — hosting and
  infrastructure product surfaces.
- **Accent green** (`colors.accent-green`, `#00d722`) — ecommerce and
  status-success surfaces.
- **Accent yellow** (`colors.accent-yellow`, `#ffae13`) — warning and
  collaboration surfaces.
- **Accent red** (`colors.accent-red`, `#ee1d36`) — error and destructive
  states.

### Surface
- **Canvas** (`colors.canvas`, `#ffffff`) — the default page background.
- **Hairline** (`colors.hairline`, `#d8d8d8`) — 1px solid borders on
  inputs, card chrome, and divider lines.

### Text
- **Ink** (`colors.ink`, `#080808`) — default text and headings.
- **Ink strong** (`colors.ink-strong`, `#222222`) — near-black emphasis.
- **Body** (`colors.body`, `#363636`) — default body paragraph color.
- **Body mid** (`colors.body-mid`, `#5a5a5a`) — mid-emphasis secondary
  text — footer lines, captions.
- **Mute** (`colors.mute`, `#898989`) and **mute soft**
  (`colors.mute-soft`, `#ababab`) — lower-priority and placeholder text.

### Semantic
- **Info blue** (`colors.accent-blue-info`, `#146ef5`) for info
  badges/notifications.
- **Success green** (`colors.accent-green`, `#00d722`) for success states.
- **Warning yellow** (`colors.accent-yellow`, `#ffae13`) for caution
  states.
- **Error red** (`colors.accent-red`, `#ee1d36`) for validation/
  destructive states.

## Typography

### Font family
A single proprietary family, `WF Visual Sans Variable` (with `Arial`
system fallback), carries every typographic role at weights 400/500/550/
600 — never 700+. A monospace variant, `WFVisualSans-Mono` (Inconsolata
fallback), handles rare technical caption moments and code-style labels,
with `ss02`, `ss10`, and `zero` OpenType features enabled for a styled
zero glyph.

### Hierarchy
Full scale in `design-tokens.yaml → typography`: `display-xxl` 80px/600
with -0.8px tracking for the hero, down through `display-xl` 56px,
`display-lg` 44.8px, `display-md` 32px/500, `display-sm` 24px,
`display-xs` 20px; uppercase eyebrows sit at 15px/500 (+1.5px) and 12px/
500 (+0.6px); body runs `body-lg` 28.8px through `caption` 12.8px/550 (the
brand's signature semi-bold caption weight); buttons use `button-md`
16px/500.

### Principles
- Weight 600 is the ceiling — nothing on the marketing surface goes
  heavier, keeping the brand confident rather than loud.
- Negative tracking marks display sizes (-0.8px at 80px), tightening the
  kerning as part of the voice.
- Uppercase eyebrows with positive tracking mark every section — 15px/500
  with +1.5px is the signature label style.
- A single family covers the whole system; the variable font's axes do the
  work a second face would otherwise do.

### Font substitutes
WF Visual Sans Variable is proprietary. *Inter* at weights 400/500/600
with `font-feature-settings: "ss01"` is the closest stylistic match for
display and body; for the mono role, *Inconsolata* (the documented
fallback) or *DM Mono* work well.

## Layout

- Base unit: 4px, with frequent 0.4/0.8px sub-multiples for fine padding.
  Full scale in `design-tokens.yaml → spacing`, from `xxs` 2px to `3xl`
  32px.
- Hero and content bands use 32px gutters with generous vertical spacing;
  feature and pricing cards sit at 32px interior padding.
- The marketing container runs wide, effectively edge-to-edge with 32px
  gutters. Category-card grids run 2/3-up at desktop with mixed sizing
  (some feature cards span two columns); pricing tiers run 3-up desktop,
  1-up mobile.

### Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Mobile | <479px | Hero stacks; all grids drop to 1-up. |
| Mobile-large | 479–767px | Same as mobile. |
| Tablet | 768–991px | Grids run 2-up. |
| Desktop | ≥992px | Full multi-up grids. |

Buttons render around 44px tall (12px vertical padding plus 25.6px
line-height), clearing WCAG AAA. Nav shows a full link row at desktop,
collapsing to a hamburger at mobile. Category cards run 2/3/4-up at
desktop, dropping to 1-up on mobile; pricing tiers follow the same
pattern. Category cards are solid color fills with no photography; product
screenshots hold 16:9 inside 8px card chrome, and there's no portrait
imagery anywhere on the marketing surface.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 — flat | none | default bands |
| 1 — hairline | 1px solid `colors.hairline` on `canvas` | default card chrome, input borders |
| 2 — layered drop | 5-stop layered shadow, subtle warm offsets, peaking at `0 3px 7px rgba(0,0,0,.09)` | featured cards needing visible lift |
| 3 — layered drop strong | deeper version of Level 2 at `.12` final opacity | pricing/modal-level emphasis |
| 4 — heavy modal | very heavy multi-stop shadow, `0 24px 24px rgba(0,0,0,.26)` peak | modal/dialog surfaces |

The chromatic category cards themselves supply visual depth through pure
color contrast against the white canvas, while the layered five-stop
shadow recipes (each with very low individual opacity) are the brand's
only true atmospheric effect.

## Shapes

| Token | Value | Use |
|---|---|---|
| `rounded.none` | 0px | full-bleed bands |
| `rounded.xs` | 2px | tight inline pills |
| `rounded.sm` | 4px | canonical button/badge/small-element radius |
| `rounded.md` | 8px | card chrome, feature/category cards |
| `rounded.full` | 9999px | circular icon containers only |

## Components

Full specs in `design-tokens.yaml → components`. Summary:
- **Buttons** — `button-primary` (near-black fill), `button-secondary`
  (white outline), `button-text-arrow` (underlined text-link for
  long-form sections), and `button-icon-circular` for carousel controls.
- **Cards** — `card-feature` and its dark counterpart `card-feature-dark`,
  plus `card-pricing` for pricing tiers.
- **Inputs** — `text-input`, a hairline-bordered field at `rounded.sm`.
- **Navigation** — `nav-bar`, `nav-link`, and `footer`.
- **Signature pieces** — `hero-band` and `hero-band-dark` (the polarity-
  flipped variant used on some campaign pages), `content-band`, the five
  `category-card-*` variants (purple, pink, blue, orange, green — green
  uses ink text for legibility against its lighter fill), and
  `badge-info`/`badge-info-soft` for filled and outline info badges.
- **Example surfaces** (`ex-*`) — auto-derived kit-mirror demonstrations
  (pricing tier, product selector, app-shell row, data-table cell, auth
  card, modal, empty state, toast) re-skinning the brand's primitives onto
  ten common product surfaces.

## Do's and don'ts

**Do**
- Reserve `colors.primary` (`#080808`) for every primary CTA, heading, and
  wordmark — near-black is the conversion color.
- Use the five chromatic accents (purple, pink, blue, orange, green) as
  full-fill category-card backgrounds, never as button colors.
- Set hero headlines in `typography.display-xxl` weight 600 with -0.8px
  tracking.
- Pair the proprietary WF Visual Sans family across every typographic
  role — no second family.
- Use `rounded.sm` 4px for buttons and `rounded.md` 8px for cards; the
  brand never uses pill CTAs.
- Layer multi-stop drop-shadows on featured cards for the brand's
  distinctive elevation recipe.

**Don't**
- Don't push button-medium weight past 600 — the brand's ceiling.
- Don't use chromatic accents as button backgrounds; they're surface fills,
  not actions.
- Don't render CTAs as pills — the button geometry is a tight 4px
  rectangle.
- Don't add a sixth accent color; the five-stop palette is the complete
  system.

## Known gaps

- The `ex-*` example components are auto-derived kit-mirror surfaces, not
  directly observed, and should be treated as reasonable extrapolations.
- Font substitutes are recommendations only — WF Visual Sans Variable is
  proprietary and not publicly distributed.
