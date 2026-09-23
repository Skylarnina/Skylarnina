# Nintendo.com (2001) Design System — Full Analysis

Adapted from the Nintendo.com (2001) design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/nintendo-2001/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

The 2001-era Nintendo.com treats a web page as if it were a piece of console
hardware. Instead of the grunge textures or corporate gradients common to
that era, the interface is built from brushed-periwinkle metal plates —
every region is a discrete beveled panel with a brighter highlight along its
top edge and a `colors.chrome-indigo` shadow line beneath, as though it were
stamped from injection-molded plastic like a Game Boy shell. The whole page
reads as one machine faceplate: a `colors.canvas` periwinkle body carrying
inset modules, with the largest panels' corners physically chamfered (cut at
45°) rather than rounded, reinforcing the sense of a manufactured object.

Three voices carry the palette. The structural voice is cool
periwinkle-to-indigo chrome (`colors.canvas`, `colors.periwinkle`,
`colors.chrome-indigo`). The authority voice is `colors.carbon` — near-black
slabs used for the top nav, the right-rail action buttons, and the footer,
each printed with a faint halftone dot-matrix texture that reads like a
speaker grille. The energy voice is warm and does exactly one job: pointing
you somewhere. `colors.nav-gold` lights the primary menu words,
`colors.amber` fills utility chips and badges, and `colors.signal` marks
every forward cue — round arrow buttons, headline chevron chips, the Submit
button. In this system, warmth always means action; the cool chrome never
carries it.

Atmosphere comes from the hero fields, which break the periwinkle calm with
full-bleed product photography over textured backdrops — a circuit-board
cyan on Systems, a motion-blurred racetrack red on Games, a soft lavender
wash on Home — each capped with a chunky `typography.display` wordmark
rendered in white with a heavy outline and hard drop shadow, the visual
grammar of game-box cover type. A pixel-eared Mario leans into the masthead
with a "Welcome to Nintendo.com!" speech bubble, tying the whole machine back
to the brand's playful character voice.

**Key characteristics:**
- Every UI region is a beveled metal plate in `colors.canvas` periwinkle,
  edge-lit on top and shadow-lined with `colors.chrome-indigo` below — the
  page is assembled, not laid out.
- Chamfered (cut-corner) geometry on the largest modules; most chrome is
  sharp-edged (`rounded.none`), with roundness reserved for the logo pill,
  radio dots, and circle-arrow badges (`rounded.full`).
- A carbon-navy command layer (`colors.carbon`) with halftone-dot texture
  carries the top nav, right-rail buttons, and footer.
- Warmth is rationed strictly as directional signal: nav gold for menu
  words, amber for utility chips/badges, signal orange for every
  forward/Submit cue.
- Photographic hero fields cycle a page-specific accent tint (lavender on
  home, systems-teal on Systems, games-red on Games) under outlined
  box-art-style display wordmarks.
- A dense modular grid — masthead, dual nav bars, hero, then a two-thirds
  content column beside a one-third right action rail — packed with minimal
  whitespace.
- Character-led: the Mario mascot speech bubble and the ESRB badge frame the
  chrome with brand personality and regulatory trust marks.

## Colors

The palette reads as a cool metallic chassis with rationed warm signal:
periwinkle chrome that everything is built from, carbon command slabs, and
warm wayfinding accents that are the only saturated color in the steady-state
interface.

### Brand & accent
- **Nintendo Red** (`colors.primary` — #e60012): the racetrack logo wordmark
  and the brand's anchor hue, doubling as the validation/alert color. Never a
  surface fill outside the logo plate.
- **Signal Orange** (`colors.signal` — #f68d1f): the "go forward" color —
  every round arrow button, every headline chevron chip, the Submit button,
  the "Play It On" platform badges. If it advances you, it's orange.
- **Amber** (`colors.amber` — #ecab37): utility energy — the Code Bank /
  Game Finder / Go chips, info-box header tabs, sweepstakes stars, and the
  ESRB Privacy-Certified badge. More golden than signal orange, and reserved
  for tools and marks rather than forward motion.
- **Nav Gold** (`colors.nav-gold` — #e48600): the deeper orange-gold used
  exclusively for the primary nav words glowing on the carbon bar.

### Surface
- **Periwinkle Metallic** (`colors.canvas` — #7a8aba): the primary interface
  body that every module is inset into.
- **Light Periwinkle** (`colors.periwinkle` — #8ba1d4): raised mid panels
  (poll panel, system tiles), one step brighter than canvas for elevation.
- **Pale Sky** (`colors.sky` / `colors.canvas-soft` — #9fbee7): the
  secondary-nav strip and light inset panel fills.
- **Pale Lavender** (`colors.lavender` — #acace7): the home hero field and
  side promo cards.
- **Pale Ice** (`colors.ice` — #c0d5e6): the News hero panel field.
- **Chrome Indigo** (`colors.chrome-indigo` — #3d4f97): the beveled
  border/shadow line beneath every plate and the leading angled edge of nav
  tabs.
- **Muted Indigo** (`colors.muted-indigo` — #60619c): inactive tabs and
  recessed chrome.
- **Platinum Gray** (`colors.platinum` — #dedede): list-row and inset
  content surface — news headlines and archive rows sit on this.
- **White** (`colors.surface` — #ffffff): content cards, form fields, the
  logo pill, list-row highlight.

### Text
- **Carbon Navy** (`colors.ink` — #21242e): primary text on light chrome,
  and the fill of the dark command layer.
- **Chrome Indigo** (`colors.ink-soft` — #3d4f97): secondary text and
  small-caps chrome labels.
- **White** (`colors.on-primary` — #ffffff): text on carbon, red, and orange
  chrome.

### Semantic
- **Error/Alert** (`colors.error` — #e60012): validation and destructive
  states reuse the brand red.
- **Systems Teal** (`colors.systems-teal` — #206479): the Systems hero's
  circuit-board cyan field.
- **Games Red** (`colors.games-red` — #a7282b): the Games hero's
  motion-blurred racetrack field.

## Typography

### Font family
The era's web-safe reality is Arial/Helvetica throughout — no webfonts. The
system's character comes from treatment, not typeface: tight uppercase
tracking on every chrome label, and a heavy outlined-and-shadowed display
style for hero wordmarks that mimics console box-art logotype. Body copy is
plain small Arial; links are the same family, bold, in `colors.ink-soft`.

The micro-labels (vertical left-rail tabs, footer fine print) carry the soft
pixelation of small bitmap-rendered Arial from the period — pair Arial with a
pixel face such as Silkscreen or VT323 at 10–11px for a faithful
reproduction.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale. Principles:
- `typography.display` (44px/900) is always white, heavily outlined, with a
  hard offset shadow — the box-art convention, never flat.
- Structural labels (nav words, panel headers, button text) are uppercase
  Arial Bold with a half-pixel of tracking — it reads like silkscreened
  controller legends.
- Body stays small and quiet at 12px so the hierarchy is carried entirely by
  labels and photography, not by body-copy size.

### Note on font substitutes
Arial is freely available and needs no substitute. For period-accurate
bitmap micro-labels, layer a pixel font (Silkscreen, VT323, or Press Start
2P for the chunkiest legends) at 10–11px with anti-aliasing disabled. The
bespoke box-art wordmarks are closest approximated with Archivo Black
(italicized) or Arial Black plus a CSS text-stroke outline and offset
text-shadow.

## Layout

### Spacing system
- Base unit: 8px (`spacing.sm`) — the rhythm between list rows and grid
  cells.
- Tokens: `spacing.xxs` 2px · `spacing.xs` 4px · `spacing.sm` 8px ·
  `spacing.md` 12px · `spacing.lg` 16px · `spacing.xl` 24px · `spacing.xxl`
  32px · `spacing.section` 48px.
- Panels carry 12px interior padding; larger modules use 16px. Inter-module
  gaps run 16–24px. The layout is deliberately dense — whitespace is a
  structural seam between plates, not a luxury.

### Grid & container
- Fixed-width canvas roughly 780–830px, centered — a desktop-era fixed table
  layout sized to a single target window, not a fluid grid.
- Masthead row: Mario mascot + speech bubble at left, search module at
  right, floating above the chrome.
- Dual nav bars: a carbon primary bar (logo, five section words, Code Bank /
  Game Finder chips) stacked over a periwinkle secondary strip (Parents,
  Customer Service, Corporate, Global, Privacy, Store, Contact).
- Body: a full-width hero panel, then a two-column split — roughly
  two-thirds content column of stacked panels beside a one-third right
  action rail (Login/Subscribe/Newsletter/Help buttons, an info box, a side
  promo card).
- Left rail: a thin vertical strip of rotated tabs (Top Ten, Top Rentals,
  Player's Choice, ESRB Ratings) clipped to the chrome edge.

### Whitespace philosophy
Empty space is engineered seam, not breathing room. Modules butt against
each other separated by thin chrome-indigo bevel lines and a few pixels of
canvas, so the eye reads grouped plates. The density is intentional — it
gives the page the feel of a packed control panel where everything is one
click away.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 — Inset | Recessed into canvas; darker chrome-indigo top edge, lighter bottom edge | List rows, form fields, the canvas body itself |
| 1 — Plate | Flush panel; lighter top highlight, chrome-indigo shadow line beneath | Content panels, system tiles, info box |
| 2 — Raised chip | Beveled button with bright top edge + hard bottom shadow | Utility chips, Go/Submit buttons, nav tabs |
| 3 — Command slab | Carbon near-black with halftone texture, sits "above" the chrome | Top nav bar, right-rail buttons, footer |

There is no blurred drop-shadow vocabulary here; depth is physical bevel
simulation. Texture and photography carry additional depth: the halftone
dot-matrix on carbon slabs reads as a recessed speaker grille; hero fields
use motion-blur, circuit-board patterns, and product renders with their own
cast shadows; chamfered corners on outer chrome suggest a machined faceplate
edge. The left-rail rotated tabs appear to tuck behind the main chrome, a
small but effective layering cue.

## Shapes

| Token | Value | Use |
|---|---|---|
| rounded.none | 0px | Default — nav bar, footer, most chrome plates (sharp/chamfered) |
| rounded.xs | 2px | Utility buttons, form fields, badges |
| rounded.sm | 4px | Small panels, featured tiles, list rows |
| rounded.md | 6px | Content panels, hero panel |
| rounded.lg | 10px | Outer section panels, mascot bubble |
| rounded.full | 9999px | Logo racetrack pill, radio dots, circle-arrow badges |

The signature is sharpness with rationed roundness. Chrome is hard-edged and
often chamfered (corners cut at 45° rather than curved) — the
manufactured-faceplate look. Roundness appears only where it signals a
physical control: the fully-pill logo, round radio buttons, and round
signal-orange arrow badges. Resist softening every corner; the tension
between sharp plates and the few pill elements is the whole character.

## Components

Definitions live in `design-tokens.yaml → components`. Summary:
- **Navigation** — `nav-bar` (carbon, gold links), `subnav-strip` (pale-sky,
  utility links), `left-rail-tab` (rotated carbon tabs).
- **Brand & masthead** — `logo-pill` (red racetrack wordmark on white pill),
  `mascot-bubble` (Mario welcome speech bubble).
- **Buttons** — `button-primary` (amber utility chip, pressed state deepens
  to nav-gold), `button-submit` (signal-orange forward/commit),
  `button-secondary` (carbon right-rail action), `button-icon-arrow` /
  `button-arrow-chip` (round or chip forward arrows).
- **Inputs & forms** — `search-field`, `text-input`, `select-dropdown`,
  `field-label`, `radio-option`, `form-panel` (platinum panel capped by a
  section-label-bar), `dotted-divider`.
- **Cards & panels** — `hero-panel` (photographic, page-tinted, outlined
  wordmark), `section-label-bar` (module header), `news-row`,
  `featured-tile`, `poll-panel`, `info-box`, `promo-card`, `system-tile`,
  `link-row-card`, `calendar-widget`.
- **Badges & footer** — `esrb-badge`, `esrb-rating-square`, `footer-bar`.

## Do's and don'ts

**Do**
- Build every region as a beveled plate: a periwinkle body with a brighter
  top edge and a chrome-indigo shadow line beneath — the "assembled machine"
  feel depends on it.
- Reserve warm color for wayfinding only — nav gold for nav words, amber for
  utility/badges, signal for forward/Submit. Cool chrome never carries
  action color.
- Keep structural labels uppercase Arial Bold with 0.5px tracking — the
  silkscreen-legend voice of the whole system.
- Render hero wordmarks as outlined + drop-shadowed display type over
  full-bleed photographic fields tinted per page.
- Use the carbon command layer with halftone texture to separate "system
  controls" from "content."
- Let panels butt together with thin bevel seams; density is the intended
  texture.
- Default corners to sharp/chamfered; spend roundness only on the logo
  pill, radio dots, and circle-arrow badges.

**Don't**
- Don't soften every corner — a uniformly rounded card system erases the
  manufactured-faceplate identity.
- Don't introduce a soft blurred drop-shadow elevation language; depth here
  is hard bevels and pictorial photography, not Material elevation.
- Don't let signal orange and amber bleed into decorative use — warm color
  must always mean "act here."
- Don't add accent colors outside the page-tint heroes; the steady-state
  chrome stays strictly cool periwinkle + carbon.
- Don't widen body copy or whitespace into an airy modern layout; the
  packed, fixed-canvas density is the brand.
- Don't flatten the dual-nav structure (gold primary words over the pale
  secondary strip) into one bar.
- Don't render hero or system wordmarks as flat text; without the outline +
  shadow they lose the box-art reference entirely.

## Responsive behavior

| Name | Width | Key changes |
|---|---|---|
| Desktop (only) | ~780–830px fixed | The native, sole target — a fixed-width application-style layout |
| Narrow window | < 780px | Horizontal scroll (no reflow); the table layout does not collapse |

This is a pre-responsive, fixed-canvas design authored for a single desktop
window size. A faithful modern re-implementation would preserve the fixed
chrome metaphor on desktop and, below roughly 720px, stack the right action
rail beneath the content column and collapse the dual nav bars into a single
carbon bar with a disclosure toggle.

Touch targets were not a consideration originally (mouse-only era; buttons
run 18–28px tall) — a modern port should enlarge `button-primary`,
`button-icon-arrow`, and `radio-option` hit areas to at least 44×44px.

On a modern narrow viewport: dual nav bars collapse to a single carbon bar
with a menu disclosure; the two-column body becomes a single stacked column
with the right rail moving below content; the left rotated-tab strip becomes
a horizontal scroll row or is removed; the fixed hero becomes a fluid
full-bleed hero that keeps its outlined wordmark.

Hero fields are full-bleed photographic plates clipped to the panel's
beveled rectangle; featured-site and game tiles are fixed-pixel thumbnails
(~95×60px) in a tight grid, with no lazy loading (the era predates it).

## Known gaps

- No hover states are documented in the source analysis.
- This is a pre-responsive design; the responsive strategy above is a modern
  extrapolation, not evidence from the original site.
- The examples (`ex-*` component entries) in the token file are illustrative
  kit-mirror demonstration surfaces for re-skinning modern SaaS patterns
  (pricing tiers, data tables, modals) in this brand's chrome — they are not
  literal parts of the 2001 Nintendo.com site.
