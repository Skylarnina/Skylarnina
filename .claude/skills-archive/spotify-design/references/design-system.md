# Spotify Design System — Full Analysis

Adapted from the Spotify design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/spotify/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Spotify's interface wraps listeners in a near-black cocoon — three shades
of charcoal (`near-black` `#121212`, `dark-surface` `#181818`, `mid-dark`
`#1f1f1f`) that let album art and content become the primary source of
color. The governing idea is "content-first darkness": the chrome recedes
into shadow so music, podcasts, and playlists can glow. Every surface in
the system is some shade of charcoal, and the only true color comes from
the iconic Spotify Green (`brand-green` `#1ed760`) and the artwork itself.

Type runs on SpotifyMixUI and SpotifyMixUITitle — a customized cut of
Circular by Lineto — carrying an unusually broad fallback stack (Arabic,
Hebrew, Cyrillic, Greek, Devanagari, CJK) that reflects Spotify's reach
into 180+ markets. The type system is compact and functional: weight 700
for emphasis and navigation, 600 sparingly for secondary emphasis, and
400 for body. Button labels go uppercase with positive letter-spacing
(1.4-2px), giving them a systematic, label-like voice distinct from
regular content text.

What makes the interface unmistakably Spotify is its pill-and-circle
geometry: primary buttons round to 500-9999px, play controls round to a
full 50% circle, and the search input is a 500px pill. That geometry
combines with notably heavy shadows (`rgba(0,0,0,0.5) 0px 8px 24px`) on
elevated elements and a distinctive inset border-shadow pairing on inputs
to produce something that feels like a premium tactile audio device
rather than a flat productivity app.

**Key characteristics:**
- Near-black immersive dark theme (`#121212`-`#1f1f1f`) where the UI all
  but disappears behind the content.
- Spotify Green as the singular brand accent — always functional
  (play controls, active states, CTAs), never decorative.
- SpotifyMixUI/CircularSp family with an extensive global-script fallback
  stack.
- Pill buttons (500-9999px) and circular controls (50%) — rounded and
  touch-optimized throughout.
- Uppercase button labels with wide letter-spacing (1.4-2px).
- Heavy shadows on elevated elements (`rgba(0,0,0,0.5) 0px 8px 24px`).
- A small semantic set — negative red, warning orange, announcement blue —
  layered on top of the achromatic base.
- Album art supplies essentially all of the interface's color; the chrome
  itself stays achromatic by design.

## Colors

### Primary brand
- **Spotify Green** — the primary accent: play buttons, active states,
  CTAs. Never used as a decorative fill.
- **Near Black** — the deepest background surface.
- **Dark Surface** — cards, containers, elevated surfaces.
- **Mid Dark** — button backgrounds, interactive surfaces.

### Text
- **White** — the base text color.
- **Silver** — secondary text, muted labels, inactive nav items.
- **Near White** — a slightly brighter secondary text tone.
- **Light** — a near-pure white reserved for maximum emphasis.

### Semantic
- **Negative Red** — error states.
- **Warning Orange** — warning states.
- **Announcement Blue** — informational states.

### Surface & border
- **Dark Card / Mid Card** — elevated and alternate card surfaces.
- **Border Gray** — button borders on dark surfaces.
- **Light Border** — outlined-button borders and muted links.
- **Separator** — divider lines.
- **Light Surface** — the rare light-mode button surface (cookie consent,
  marketing contexts).
- **Spotify Green Border** — a green accent-border variant.

### Shadows
- **Heavy** (`rgba(0,0,0,0.5) 0px 8px 24px`) — dialogs, menus, elevated
  panels.
- **Medium** (`rgba(0,0,0,0.3) 0px 8px 8px`) — cards, dropdowns.
- **Inset border** (`rgb(18,18,18) 0px 1px 0px, rgb(124,124,124) 0px 0px
  0px 1px inset`) — the input border-shadow combination.

## Typography

### Families
- **Title** — `SpotifyMixUITitle` with the full CircularSp/system fallback
  chain, used for section titles.
- **UI/Body** — `SpotifyMixUI` on the same fallback chain, used for
  everything else.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale (section-title
24px down to micro 10px). Governing principles:
- **Bold/regular binary** — most text sits at either weight 700 or 400,
  with 600 used sparingly, so hierarchy comes primarily from weight
  contrast rather than size variation.
- **Uppercase buttons as system** — button labels are uppercase with wide
  letter-spacing (1.4-2px), creating a systematic "label" voice distinct
  from content type.
- **Compact sizing** — the whole range runs 10-24px, narrower than most
  systems, because Spotify's type exists to be scanned (playlists, track
  lists) rather than read at length.
- **Global script support** — the deep fallback stack (Arabic, Hebrew,
  Cyrillic, Greek, Devanagari, CJK) reflects Spotify's global market
  reach.

## Components

Definitions live in `design-tokens.yaml → components`. Summary:
- **Buttons** — dark pill (nav/secondary), dark large pill (primary app
  navigation), light pill (rare light-mode CTAs), outlined pill (follow/
  secondary actions with asymmetric icon padding), and circular play
  (the core playback control).
- **Cards & containers** — `dark-surface`/`mid-dark` fill, 6-8px radius,
  no visible border on most cards, a subtle background lightening on
  hover, and the medium shadow on elevated cards.
- **Inputs** — the search input is a 500px pill with icon-aware padding
  (`12px 96px 12px 48px`) and a focus state that swaps to a solid black
  border plus a 1px outline.
- **Navigation** — a dark sidebar using SpotifyMixUI at weight 700 for
  active items and 400 for inactive ones, silver for inactive color and
  white for active, circular icon buttons, and the green Spotify logo
  top-left.

## Layout

- Base spacing unit: 8px, with a fine-grained scale (1, 2, 3, 4, 5, 6, 8,
  10, 12, 14, 15, 16, 20px).
- Layout is a fixed sidebar plus a main content area, with grid-based
  album/playlist cards and a full-width now-playing bar pinned to the
  bottom.
- **Dark compression** — Spotify packs content densely; playlist grids,
  track lists, and navigation are all tightly spaced. The dark background
  itself provides visual rest between elements, so large gaps aren't
  needed.
- This is an app, not a marketing site — every pixel is expected to serve
  the listening experience rather than provide editorial breathing room.

## Shapes

- Minimal (2px) — badges, explicit tags.
- Subtle (4px) — inputs, small elements.
- Standard (6px) — album-art containers, cards.
- Comfortable (8px) — sections, dialogs.
- Medium (10-20px) — panels, overlay elements.
- Large (100px) — large pill buttons.
- Pill (500px) — primary buttons, search input.
- Full pill (9999px) — navigation pills, search.
- Circle (50%) — play buttons, avatars, icons.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| Base (0) | `#121212` background | Deepest layer, page background |
| Surface (1) | `#181818` or `#1f1f1f` | Cards, sidebar, containers |
| Elevated (2) | `rgba(0,0,0,0.3) 0px 8px 8px` | Dropdown menus, hover cards |
| Dialog (3) | `rgba(0,0,0,0.5) 0px 8px 24px` | Modals, overlays, menus |
| Inset border | `rgb(18,18,18) 0px 1px 0px, rgb(124,124,124) 0px 0px 0px 1px inset` | Input borders |

Spotify's shadows are notably heavy for a dark-themed product. The 0.5-
opacity shadow at 24px blur gives dialogs and menus a dramatic "floating
in darkness" quality, while the 0.3-opacity 8px-blur shadow gives cards a
subtler lift. The distinctive inset border-shadow combination on inputs
creates a recessed, tactile feel that stands in for a conventional
border.

## Do's and don'ts

**Do**
- Use near-black backgrounds (`#121212`-`#1f1f1f`) and let shade
  variation, not color, carry depth.
- Apply Spotify Green only to play controls, active states, and primary
  CTAs.
- Use pill shapes (500-9999px) for buttons and circles (50%) for play
  controls.
- Set button labels uppercase with wide letter-spacing (1.4-2px).
- Keep typography compact (10-24px) — this is app density, not magazine
  density.
- Use heavy shadows (0.3-0.5 opacity) for elevated elements on the dark
  canvas.
- Let album art carry the color; keep the surrounding UI achromatic.

**Don't**
- Don't use Spotify Green decoratively or as a background fill.
- Don't use light backgrounds for primary surfaces — dark immersion is
  the core of the brand.
- Don't skip the pill/circle geometry on buttons; square buttons break
  the identity.
- Don't use thin, subtle shadows — on a dark background they need to be
  heavy to register at all.
- Don't introduce additional brand colors — green plus achromatic grays
  is the complete palette.
- Don't use relaxed line-heights; Spotify's type is compact and dense by
  design.
- Don't expose raw gray borders where a shadow-based or inset border
  would do the job instead.

## Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Mobile Small | <425px | Compact mobile layout |
| Mobile | 425-576px | Standard mobile |
| Tablet | 576-768px | 2-column grid |
| Tablet Large | 768-896px | Expanded layout |
| Desktop Small | 896-1024px | Sidebar visible |
| Desktop | 1024-1280px | Full desktop layout |
| Large Desktop | >1280px | Expanded grid |

Collapsing strategy: the sidebar goes full → collapsed → hidden; the
album grid runs 5 → 3 → 2 → 1 columns; the now-playing bar is maintained
at every size; the search pill keeps its shape while its width adjusts;
and navigation shifts from a sidebar to a bottom bar on mobile.

## Known gaps

- The token values here are extracted directly from the source analysis
  and should be treated as canonical for this skill.
- The source document does not distinguish a dedicated light-mode palette
  beyond the rare `light-surface` button token — Spotify's product is
  dark-first by design.
