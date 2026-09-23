# Kraken Design System — Full Analysis

Adapted from the Kraken design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/kraken/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Kraken presents itself as a clean, trustworthy crypto exchange, and its
marketing surface leans entirely on white backgrounds (`colors.canvas`) with
Kraken Purple carrying the brand voice. The primary purple (`colors.primary`,
`#7132f5`) is supported by two deeper variants — `primary-dark` for
outlined-button borders and `primary-deep` as the darkest step in the family
— so the purple never reads as a single flat swatch.

Two proprietary type families divide labor cleanly: `Kraken-Brand` handles
every display heading at a bold weight 700 with negative letter-spacing,
while `Kraken-Product` (falling back to IBM Plex Sans / Helvetica) carries
all UI and body copy. Text sits in near-black `colors.ink` (`#101114`)
against a cool blue-gray neutral scale (`cool-gray`, `silver-blue`) that
keeps the interface calm rather than stark.

**Key characteristics:**
- Kraken Purple as the singular brand accent, expressed across three
  darkness steps plus a 16%-opacity subtle fill.
- Dual-font system: bold Kraken-Brand for display, Kraken-Product for
  everything functional.
- Near-black ink text on a cool blue-gray neutral scale — never warm grays.
- 12px is the hard ceiling for button radius; nothing rounds into a pill.
- Depth comes from whisper-level shadows, not strong elevation.
- A single green accent marks success/positive states exclusively.

## Colors

### Primary
- **Primary** — the commanding purple used for primary CTAs, brand accents,
  and links.
- **Primary Dark / Primary Deep** — darker purple steps used for outlined-
  button borders and deepest brand moments.
- **Primary Subtle** — purple at 16% opacity, used as a soft button fill
  when full-strength purple would be too loud.
- **Ink** — near-black primary text color.

### Neutral
- **Cool Gray** — the primary neutral, also used at 24% opacity for borders.
- **Silver Blue** — secondary text and muted UI elements.
- **Canvas** — white, the sole surface color.
- **Hairline** — the divider/border gray.

### Semantic
- **Success / Success Dark** — green used at 16% opacity for badge
  backgrounds, with the darker step reserved for badge text. This is the
  only chromatic color besides purple in the system.

## Typography

### Families
- **Display** — `Kraken-Brand`, falling back to IBM Plex Sans, Helvetica,
  Arial. Always weight 700 with negative tracking.
- **UI / Body** — `Kraken-Product`, falling back to Helvetica Neue,
  Helvetica, Arial.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale (48px hero display
down to a 7px uppercase micro label). Principles:
- Display sizes (hero, section heading, sub-heading) all run at weight 700
  with consistent negative tracking around -0.5px to -1px.
- Body and UI sizes stay at weight 400–600 with normal tracking.
- The 7px micro label is the system's only uppercase text, used for tiny
  tags.

## Layout

- Spacing runs on a fine-grained scale (1px through 25px) rather than a
  clean power-of-two system — see `design-tokens.yaml → spacing`.
- Border-radius tops out at 12px on buttons (16px on cards); nothing in the
  system uses a pill shape.
- Button padding is consistently tight: 13px vertical / 16px horizontal on
  the primary purple button, 8px on the subtle-purple variant.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| Flat | no shadow | default surfaces, body copy |
| Subtle | `rgba(0,0,0,0.03) 0px 4px 24px` | white buttons, lifted cards |
| Micro | `rgba(16,24,40,0.04) 0px 1px 4px` | fine-grained hover/detail shadows |

Both shadow tokens are deliberately faint — Kraken avoids the heavy,
saturated drop shadows common in fintech UI, favoring a "whisper" level of
elevation that barely separates surfaces from the white canvas.

## Shapes

| Token | Value | Use |
|---|---|---|
| `rounded.xs` | 3px | smallest UI accents |
| `rounded.sm` | 6px | success badges |
| `rounded.md` | 8px | neutral badges |
| `rounded.button-white` | 10px | the white button variant |
| `rounded.button` | 12px | primary/outlined/subtle/secondary buttons — the ceiling for interactive corners |
| `rounded.card` | 16px | card-level containers |
| `rounded.full` / `rounded.circle` | 9999px / 50% | circular elements only (avatars, icons) |

## Components

Definitions live in `design-tokens.yaml → components`. Summary:
- **Buttons** — primary purple (filled), purple-outlined (bordered),
  purple-subtle (16%-opacity fill), white (shadow-lifted), secondary-gray
  (low-emphasis fill). All cap at 12px radius except the white button at
  10px.
- **Badges** — success (green-tinted, 6px radius) and neutral (gray-tinted,
  8px radius), both compact caption-sized labels.

## Do's and don'ts

**Do**
- Use Kraken Purple (`colors.primary`) for CTAs and links.
- Apply 12px radius on all buttons.
- Use Kraken-Brand for headings, Kraken-Product for body.
- Keep shadows at whisper level — `shadow.subtle` or `shadow.micro`.

**Don't**
- Don't use pill buttons — 12px is the maximum radius for any button.
- Don't introduce purples outside the defined three-step scale.
- Don't use the green accent for anything other than success/positive
  signals.

## Responsive behavior

Breakpoints: 375px, 425px, 640px, 768px, 1024px, 1280px, 1536px. The source
analysis does not document per-breakpoint layout changes beyond this scale;
treat it as the canonical set of stops when building responsive layouts.

## Known gaps

- Per-breakpoint layout behavior (column collapse, nav changes) is not
  detailed in the source beyond the breakpoint list itself.
- No dark-mode palette is documented — the marketing site is light-mode
  only.
- Component hover/pressed states are not captured beyond the base
  definitions above.
- The proprietary Kraken-Brand and Kraken-Product faces are not public —
  use the listed fallback stacks (IBM Plex Sans / Helvetica / Arial).
