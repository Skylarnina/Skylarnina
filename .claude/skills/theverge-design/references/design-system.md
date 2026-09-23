# The Verge Design System — Full Analysis

Adapted from The Verge design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/theverge/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

The Verge's 2024 redesign feels like a Condé Nast magazine wired to a
chiptune soundboard. The canvas is almost-black (`canvas-black`
`#131313`), headlines are built from a brutally heavy display face
(Manuka) that runs up to 107px, and the whole page is peppered with
acid-mint (`jelly-mint` `#3cffd0`) and ultraviolet (`verge-ultraviolet`
`#5200ff`) that behave less like brand colors and more like hazard tape.
Story tiles are not quiet gray cards — they're saturated, full-bleed
color blocks (yellow, pink, orange, blue, purple) that read like pasted-
up rave flyers arranged into a timeline. The mood sits somewhere between
a developer console, a club night, and a tech tabloid: serious enough to
cover a congressional hearing, loud enough to review a synthesizer.

What makes the system unmistakable is the **StoryStream** timeline: a
vertical feed where every post is a rounded rectangle, often at 20-40px
radius, filled edge-to-edge with color, framed by a thin border, and
marked by a mono-uppercase timestamp on its left rail. Stories don't
float on a conventional grid; they stack on a dashed vertical rule like
commits in a git log. Above that, a massive "The Verge" wordmark
dominates the masthead in Manuka at hero scale, announcing editorial
territory before any headline even loads.

There is no light mode on the homepage — the dark canvas is the product,
and the palette only inverts when a single story tile takes a mint or
yellow fill. Depth stays almost entirely flat: hairline 1px borders
(white, mint, or purple) do the work that shadows would do on a
Material-flavored site. Every container is either `#131313` with a 1px
outline, a fully saturated accent block, or a slate-gray secondary
surface.

**Key characteristics:**
- Near-black editorial canvas as the default surface — no light mode on
  the homepage.
- Acid-mint plus ultraviolet as hazard-tape accents, never a quiet
  background wash.
- Massive Manuka display headlines up to 107px — the single loudest type
  move in mainstream tech media.
- Rounded pill-card everything: 20/24/30/40px corner radii, never
  square.
- Fully saturated color-block story tiles (mint, purple, yellow, pink,
  orange, electric blue) on a dark page.
- A timeline "StoryStream" feed with mono uppercase timestamps rather
  than a traditional magazine grid.
- Flat depth — 1px borders in white, mint, or purple do the work shadows
  would do elsewhere.

## Colors

### Primary (brand hazards)
- **Jelly Mint** — the signature acid-mint accent: CTA button fill,
  link underlines, active tab borders, high-attention story-tile
  backgrounds. Treat it like neon safety paint, applied sparingly to the
  single most important element on screen.
- **Verge Ultraviolet** — the complementary brand hazard: secondary
  color-block tiles, promotional spans, occasional outlined buttons,
  often at 0.9 alpha to soften its intensity.

### Secondary & accent
- **Console Mint Border** — a darker mint variant used on card outlines
  and button borders where pure mint would over-saturate.
- **Deep Link Blue** — the link *hover* color, the one moment blue
  appears; it replaces mint/white/black on hover across every link
  style.
- **Focus Cyan** — reserved strictly for button focus rings.
- **Purple Rule** — a darker ultraviolet used as the vertical rail
  border on StoryStream items.

### Surface & background
- **Canvas Black** — the default dark surface for the whole homepage;
  almost-but-not-quite pure black, warm enough to feel like a printed
  newsprint negative rather than an OLED void.
- **Surface Slate** — the secondary card background for story tiles that
  don't need a saturated color-block fill.
- **Image Frame** — the 1px border wrapping inline imagery.
- **Hazard White** — story-tile fill, button border, and primary text.
  When white appears as a large block it's an editorial "spotlight"
  decision.
- **Absolute Black** — reserved for text on the mint/yellow/white tiles,
  the only place it appears.

### Neutrals & text
- **Primary Text** — headlines and display text on the canvas.
- **Secondary Text** — bylines, timestamps, photo credits.
- **Muted Text** — button text on dark-slate buttons, slightly
  off-white to reduce glare.
- **Inverted Text** — used only on accent tiles (mint/yellow/white) to
  keep contrast legible.

### Semantic & accent
- **Focus Ring** — keyboard focus only.
- **Overlay Black** (`rgba(0,0,0,0.33)`) — a subtle 1px ring, the
  system's quiet shadow alternative on stacked cards.
- **Dim Gray** — the active/pressed button background.

There are zero decorative gradients. The only gradient-like treatment is
the transition from a saturated tile back to the canvas between rows —
color is applied in solid blocks, not washes, since the hazard-tape
identity would dissolve if anything faded softly.

## Typography

### Families
- **Manuka** (Klim Type Foundry, fallback Impact/Helvetica) — the
  signature display face for the wordmark and feature headlines; a
  heavy-weight (900), industrial, condensed sans that runs 60-107px and
  never smaller.
- **PolySans** (PanGram Pangram) — the UI and secondary-headline
  workhorse, covering weights 300/500/700 from kicker captions to body
  decks.
- **PolySans Mono** — the monospaced sibling, used exclusively for
  ALL-CAPS labels: kickers, timestamps, category tags, button labels.
  This mono-uppercase usage is the second-most identifiable Verge detail
  after Manuka.
- **FK Roman Standard** (Florian Karsten, fallback Georgia) — a serif
  used sparingly for review decks and print-voice excerpts, adding a
  magazine counterpoint to the PolySans stack.
- **Roboto** — a utility font for widgets and legacy modules.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale (hero-wordmark
at 107px down to meta-nano at 10px). Governing principles:
- **Manuka is always the hero, never the UI** — anything below 60px is a
  bug; it exists to shout the brand, not label a button.
- **PolySans is the workhorse, PolySans Mono its uniformed sibling** —
  mono is exclusively UPPERCASE labels, timestamps, tags, and certain
  buttons; lowercase mono doesn't exist in this system.
- **Thin-weight (300) capitalized headlines** are a signature move — the
  19-20px weight-300 with 1.9px tracking creates a "fashion-magazine
  whisper" contrasting with the 107px Manuka shout above it.
- **Letter-spacing has two registers** — positive (0.72-1.9px) for
  ALL-CAPS labels, negative (-0.16px) for the rare serif appearances,
  barely-positive (0.32-1.07px) for massive display. Plain 0
  letter-spacing is rare.
- **FK Roman Standard is the editorial exception**, reserved for
  long-form print-voice moments — reviews, critic pulls, masthead
  essays — never UI.
- **Line heights are tight** (0.80-1.30) for display and labels, relaxed
  (1.60-2.00) only for reading body and mono button labels, giving the
  page a "telegraph ticker" rhythm.

If substituting the proprietary Manuka face with wide-metric open-source
condensed displays (Anton, Oswald, Bebas Neue, Archivo Black), loosen
display line-heights by roughly +0.10 to +0.15 to prevent
ascender/descender collisions. PolySans substitutes (Space Grotesk, DM
Sans, Hanken Grotesk) work at the token values without adjustment.

## Components

Definitions live in `design-tokens.yaml → components`. Summary:
- **Buttons** — a mint-filled pill primary, a dark-slate secondary pill,
  an outlined-mint tertiary, and an outlined-ultraviolet promotional
  variant, plus a non-interactive pill tag at a tighter 20px radius.
- **StoryStream tile** — either a dark tile with a 1px white/mint border
  or a fully saturated fill; hover shifts only the headline text color
  to deep-link-blue, never a lift or scale.
- **Feature card** — the top-story treatment, 24px radius, larger
  padding, image clipped to match the outer radius.
- **StoryStream rail** — a vertical dashed/solid rule marking the
  timeline spine, with mono timestamps on the left and 12-16px gaps
  between pill-cornered entries.
- **Inputs** — dark background, hairline border, a tight 2px radius
  (a deliberately "typewriter form" feel), mint focus border, and
  ultraviolet used as the error/alert accent rather than the usual red.
- **Navigation** — a thin dark bar with the Manuka wordmark left-
  aligned, uppercase mono category links, and a single mint-pill CTA
  pinned right; links transition color-only to deep-link-blue on hover,
  with a mint inset-underline marking the active section.

## Layout

- Base spacing unit: 8px, scaling through 1, 2, 4, 5, 6, 8, 9, 10, 12,
  14, 15, 16, 20, 24, 25px.
- Section padding runs 32-64px vertical between major feed sections;
  StoryStream items themselves are tighter at 12-16px gaps.
- Card padding runs 20-32px, expanding to 40-48px for feature cards.
- Kickers sit ~6-10px above headlines, headlines ~10-14px above decks,
  timestamps ~6-8px below decks.
- Max content width is roughly 1280-1300px, resolving from an
  underlying 12-column grid into a 3-column hero plus a 1-column
  StoryStream rail plus feature panels — the page feels freeform because
  color-block tiles frequently span 2-3 columns.
- Container padding runs 24px mobile / 48px desktop; gutters run
  16-24px between columns, tighter (8-12px) inside StoryStream items.
- Whitespace functions like a club DJ treats silence — a dramatic reset
  between loud moments. Because the canvas is so dark and the accents so
  saturated, even 32px of empty canvas between two tiles acts as a
  palette cleanser; the page is paced rather than airy, with hazard-color
  blocks interrupting stretches of near-black.

## Shapes

The system deliberately uses eight discrete radius values, more than
most sites, so the rhythm between tiny tags, mid-size pill cards, and
large outlined buttons announces each component's hierarchy through its
corners alone:
- **2px** — inputs, small badges (a typewriter-tag feel).
- **3px** — inline images, just enough softening against the canvas.
- **4px** — nested card images and small button variants.
- **20px** — standard pill cards and color-block tiles.
- **24px** — feature-tile radius and the primary button pill.
- **30px** — large promotional buttons.
- **40px** — outlined CTA pills, the loudest pill in the system.
- **50%** — avatar circles, icon buttons, round badges.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 | No border, no shadow | Default canvas text |
| 1 | `rgba(0,0,0,0) 0px 0px 0px 0px inset` | Reset state for interactive elements |
| 2 | `1px solid #ffffff` or `#313131` | Image frames and quiet card outlines |
| 3 | `1px solid #3cffd0` | Active button outlines, focused story tiles |
| 4 | `1px solid #5200ff` | Promotional/alternate state outlines |
| 5 | `rgba(0,0,0,0.33) 0px 0px 0px 1px` | The single "atmospheric" ring on layered cards |
| 6 | `0px -1px 0px 0px inset` (mint/black/white) | Active-tab underline, a signature move |
| 7 | Saturated accent fill | Story-tile elevation via color, not shadow |

The Verge's depth philosophy is color-as-elevation: when something needs
to stand out, it gets a mint fill or a 1px hazard-color border rather
than a shadow. None of the extracted shadow entries are conventional
elevation shadows — they are all inset underlines or near-transparent 1px
rings — and the canvas stays perfectly flat throughout, with saturation
carrying hierarchy instead.

## Do's and don'ts

**Do**
- Use `#131313` as the canvas on every view; there is no light mode.
- Use Jelly Mint and Verge Ultraviolet as hazard accents — buttons,
  borders, active states, saturated tile fills.
- Use Manuka exclusively at 60px+ for hero headlines.
- Round everything: 20px for cards, 24px for feature cards, 30-40px for
  pill buttons.
- Use PolySans Mono for UPPERCASE labels, timestamps, kickers, and
  button text; lowercase mono doesn't exist here.
- Apply 1.5-1.9px letter-spacing to every ALL-CAPS label.
- Use saturated color-block tiles to elevate a story, never a drop
  shadow.
- Use deep-link-blue as the hover color on every link regardless of base
  color.
- Apply the StoryStream timeline rail on feed views.
- Use thin-weight (300) PolySans at 19-20px with 1.9px tracking for
  "fashion-whisper" eyebrows — the contrast with the Manuka shout is the
  whole voice.

**Don't**
- Use a light background — the dark canvas is the product.
- Add box-shadow for elevation; use 1px borders or saturated fills
  instead.
- Use square corners on any interactive or content container.
- Use Manuka for UI, buttons, or body copy — it is strictly display.
- Use lowercase mono; PolySans Mono is always UPPERCASE.
- Let mint and ultraviolet appear as background washes — they are
  hazard accents, not canvas tints.
- Use gradients anywhere; the system is solid color blocks only.
- Introduce accent colors outside the declared mint/purple/yellow/pink/
  orange tile palette.
- Pair Manuka with FK Roman Standard in the same headline cluster.
- Use mint text on the canvas background under 16px — contrast vibrates
  at small sizes.

## Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Small Mobile | <400px | Single column, Manuka hero scales to ~48-54px, StoryStream rail collapses to inline timestamps |
| Mobile | 400-549px | Single column, color-block tiles stack full-width, hamburger nav |
| Large Mobile | 550-767px | Still single column but padding opens up, tile radii stay at 20px |
| Tablet | 768-1023px | 2-column StoryStream with feature card spanning, wordmark shrinks ~50% |
| Small Desktop | 1024-1179px | Full 3-4 column editorial grid, mint pill CTA restored to nav |
| Desktop | 1180-1299px | Max padding, Manuka wordmark at full hero scale |
| Large Desktop | ≥1300px | Container caps at ~1280-1300px, whitespace expands at the margins |

The site tunes its grid at an unusually large number of intermediate
breakpoints — an aggressive responsive strategy overall. Primary pill
buttons clear roughly 44px minimum height; mono uppercase nav links run
smaller (~28-32px) and should be padded to 44px on mobile derivative
work; circle icon buttons run 40-44px. The nav wordmark scales from hero
Manuka down to ~24-32px on mobile, with category links collapsing to a
hamburger drawer below 900px; the grid runs 4 → 3 → 2 → 1 columns;
section padding tightens from 64px → 32px → 20px; Manuka hero type scales
from 107px to ~48-54px; PolySans headlines scale from 34px → 24px; mono
labels stay pinned at 11-12px since they become unreadable if they shrink
further; and color-block story tiles never lose saturation on mobile,
they simply reflow to full width.

## Known gaps

- The token values here are extracted directly from the source analysis
  and should be treated as canonical for this skill.
- The proprietary Manuka, PolySans, and FK Roman Standard faces aren't
  publicly available — use the open-source substitutes noted under
  Typography.
