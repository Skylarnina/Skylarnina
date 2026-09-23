# Dell 1996 Design System — Full Analysis

Adapted from the Dell 1996 design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/dell-1996/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Dell's December 1996 home page is a perfectly preserved fossil of
catalog-era enterprise web design — the moment a Fortune-100 brand decided
the web was important enough to invest in, but two years before CSS saw
wide adoption and three years before anyone used the phrase "design
system." Every visual choice is a downstream consequence of that
constraint: layout via HTML tables, type via the browser's built-in font
stack (Arial Black / Helvetica / Times Roman), color via 8-bit-safe flat
fills, and decoration via hand-cut GIF "stickers" — the NEW! burst, the
round PC Magazine Readers' Choice seal, the beveled yellow "BUY a DELL"
tab. The page is literally bordered — a 1-cell-wide black HTML table frame
— and inside it, every product line gets a "ribbon card": a white title bar
with a sharp black underline, a tinted body block in one of eight catalog
colors (sage, salmon, peach, lime, sky, steel, periwinkle, olive), and a
beveled product photograph notched into the card's right edge.

The brand voice carries through two anchors: a vivid Dell-red CTA panel on
the homepage's left side (cream-yellow Times Roman copy on the red fill,
sitting inside the black frame) and a screaming red phone number —
1-800-213-DELL — pinned to the top-right of every page, because in 1996 the
website was a brochure that ended in a phone call. The footer is a row of
four hand-drawn icon labels (FIND / HOME / ONLINE STORE / SERVICE &
SUPPORT) linked by a thin green rule, plus a single classic-Mosaic-blue
underlined "Copyright" link above Times Roman legal small print.

**Key characteristics:**
- A literal page frame: every page sits inside an ~8px black outer border —
  the browser window is treated as a printed picture frame.
- Flat color-block "ribbon cards" tint each product family with a
  dedicated catalog color (sage for Latitude, salmon for OptiPlex GX,
  periwinkle for PowerEdge, sky for Dellware, etc.) — no gradients, no
  shadows, no opacity.
- Chunky display typography: Arial Black 36/900 for section title blocks,
  Helvetica Bold 16 for product-row titles, Times Roman 14 for everything
  else.
- Hand-cut GIF stickers overlay the layout: the yellow "BUY a DELL" tab top
  right, angled "NEW!" bursts on new product rows, round red PC Magazine
  seals.
- Dell red is reserved for exactly two things — the homepage CTA panel and
  the top-right phone number — never decorative.
- Footer icon-nav with classic-blue (`#0000ee`) anchor underlines, the
  unmistakable Netscape 3.x link color.

## Colors

### Brand & accent
- **Dell Red** (`#e91d2a`) — the brand's signature red, reserved for the
  homepage CTA panel and the top-right phone number, plus the PC Magazine
  award-seal ring. Never used as a card body fill.
- **Dell Yellow** (`#fcc20f`) — sticker yellow: the "BUY a DELL" tab in the
  top banner, and the angled "NEW!" bursts overlapping new product rows.
- **Dell Purple** (`#6a26a4`) — the accent stripe behind the lowercase
  ".com"/"DELL" wordmark text, appearing only inside the "BUY a DELL"
  sticker chrome.

### Surface
- **Frame Ink** (`#000000`) — pure black: the page frame, the top-banner
  background, button fills, and every 1px ribbon-card hairline.
- **Canvas** (`#ffffff`) — true white inside the frame: the page surface,
  the ribbon-card title-bar fill, and the icon-label nav backdrop.

### Text
- **Ink** (`#000000`) — body text, headings, pre-visit link copy: pure
  black, with no warm near-black softening (that wasn't a thing in 1996).
- **Link** (`#0000ee`) — classic Mosaic/Netscape 3.x default link blue,
  underlined on inline anchors ("Copyright", "(Terms of Use)", inline body
  links).

### Ribbon-card tint family
Eight catalog colors, one per product line — the page's chromatic
personality: olive (`#8e8a25`, "DIMENSION DESKTOPS" eyebrow), sage
(`#b3bd95`, Latitude Notebooks), salmon (`#d77a7a`, "OPTIPLEX DESKTOP
SYSTEMS" eyebrow + GX Series), peach (`#e6915d`, Dimension + OptiPlex Gs),
lime (`#c0d4a7`, OptiPlex G Series), sky (`#9ab6c8`, Dellware), steel
(`#a5b8c0`, Dimension XPS Pro), and periwinkle (`#8c9ae0`, PowerEdge). The
tints are saturated but not vivid — they sit just below true neutral
chroma, the signature of GIF-era web-safe-palette quantization.

## Typography

### Font family
Three system-stack families, no webfonts (webfonts didn't exist yet):
- **Arial Black** (fallback Helvetica, system-ui sans) — display headings
  only. The chunky stenciled section eyebrows ("DIMENSION DESKTOPS",
  "OPTIPLEX DESKTOP SYSTEMS") are Arial Black at weight 900, all-caps,
  normal tracking.
- **Helvetica** (fallback Arial, system-ui sans) — product-row titles,
  button labels, and the top banner's "BUILD YOUR OWN COMPUTER. ONLINE."
  headline; always bold (700), always all-caps.
- **Times New Roman** (fallback Times, serif) — body copy. Every
  paragraph, caption, and inline anchor sits in default-rendered Times
  Roman, instantly dating the design — body text on the modern web is
  almost never serif.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale. Key entries:
`display` (36/900, section eyebrow titles), `heading-1` (24/900, sub-page
heroes), `heading-2` (16/700, top-banner copy and product-line h1),
`heading-3` (14/700, ribbon-card title bars), `body` (14/400, default
paragraph copy), `body-sm` (12/400, browser-compatibility fine print),
`caption` (11/400, footer copyright), `button`/`ui-label` (12/700, button
and nav labels).

### Principles
Sans for UI, serif for body — the inverse of the modern convention, and a
dead giveaway of mid-90s typography. Display weights are extreme (900,
Black) and never softer; the "Dimension"/"OptiPlex" eyebrow blocks lean on
the heaviest weight the font ships. There's no letter-spacing tracking
adjustment anywhere — pixel-fonts in 1996 didn't reward it, so everything
sits at the browser's default kern. Line-height stays tight on display
(1.0) and conventional on body (1.4), a holdover from print-magazine
catalog layout.

### Font substitutes
All three families were operating-system defaults on every consumer OS
shipped in 1996 (Windows 95: Arial/Times New Roman; Mac OS 7.5+:
Helvetica/Times) — the brand had no fallback strategy because none was
needed. Modern reproductions can stay on this exact stack (Arial Black /
Helvetica / Times New Roman) for authenticity.

## Layout

- **Base unit:** 4px (with 2/6/10 intermediates) — 1996 page layout was
  driven by HTML table cell padding rather than a designed scale.
- **Tokens:** `xxs` 2px, `xs` 4px, `s` 6px, `sm` 8px, `m` 10px, `md` 12px,
  `lg` 16px, `xl` 20px, `xxl` 24px, `section-sm` 32px, `section` 40px,
  `section-lg` 48px.
- **Card interior padding:** `md` (12px) vertical / `lg` (16px) horizontal
  on ribbon-card bodies.
- **Section vertical rhythm:** `section` (40px) between product-ribbon
  stacks; `section-sm` (32px) between the eyebrow color block and its
  first ribbon card.
- **Grid & container:** a fixed-width table layout pinned around 760px
  wide — the de facto 1996 standard targeting 800×600 monitors with a
  small scrollbar gutter. A two-column outer structure runs a ~28% left
  rail (icon-link grid + red CTA panel) against a ~72% right column
  (product ribbon stack). There's no grid system in the modern sense —
  every section is its own `<table>` with hard-coded column widths.
- **Whitespace philosophy:** tight by modern standards — catalog density
  wins over editorial breath, with every pixel inside the black frame
  doing work. Compensating decompression happens inside each ribbon card:
  the white title bar, tinted body block, and product-photo notch create
  internal breathing room without enlarging the overall page.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 — Flush | no shadow, no border | body text, copyright row, footer band background |
| 1 — Hairline | 1px solid frame-ink | ribbon-card outer edge, table-cell dividers |
| 2 — Frame | 8px solid frame-ink | the page-frame border around the entire viewport |
| 3 — Bevel | hard-edge 1px highlight + 1px shadow on GIF stickers/photos | "BUY a DELL" yellow sticker, NEW! bursts, award seals, product photographs |

There are no soft shadows anywhere — every depth cue is either a hard 1px
border or a hand-painted bevel baked into a GIF. Modern reproductions that
want to stay period-accurate must resist the urge to add Material-style
elevation or atmospheric drop shadows. Bevels and frames carry the entire
depth vocabulary: the page frame is the strongest cue, telling the viewer
"this is a contained document, not a continuous canvas"; bevels on
stickers push them forward as if pinned on with thumbtacks; product
photographs carry their own hand-painted bevel and drop shadow baked
into the image itself.

## Shapes

| Token | Value | Use |
|---|---|---|
| `rounded.none` | 0px | universal default — buttons, cards, inputs, banners, page frame, ribbon-card bodies, eyebrow blocks |
| `rounded.full` | 9999px | circular award seals (PC Magazine Readers' Choice), the round "h" sticker on the HOME icon |

The 1996 design has effectively two radius modes: square (everything) and
round (decorative seal stickers) — there is no 4/8/12px subtle radius
tier, since that vocabulary belongs to the post-Bootstrap web. Product
photos are rectangular GIFs with their own internal beveled "monitor"
framing, sitting at native pixel dimensions and never scaled. Aspect
ratios cluster around 4:3, the era's standard CRT shape. There are no
avatars — staff photography was reserved for "About Dell" pages not
captured in this analysis.

## Components

Definitions live in `design-tokens.yaml → components`. No hover states are
documented anywhere — every component below is Default state only.

- **page-frame** — the literal black border around the entire viewport;
  the page sits inside it. Treat it as non-negotiable container chrome;
  collapsing it on mobile to ~4px is acceptable, but removing it entirely
  loses the brand.
- **top-banner** — pure-black strip across the top carrying the white
  "BUILD YOUR OWN COMPUTER. ONLINE." headline plus sub-tagline, the yellow
  "BUY a DELL" sticker pinned at right, and the red phone number.
- **section-eyebrow-olive / section-eyebrow-salmon** — large tinted color
  blocks holding a chunky stenciled section title (Arial Black 36/900).
- **Ribbon cards** — the brand's signature component, built from three
  pieces: `ribbon-card-title` (white bar, Helvetica Bold all-caps product
  name, 1px bottom border), `ribbon-card-body-<tint>` (one of eight flat
  tints holding the Times Roman marketing pitch), and a photo notch (the
  product GIF hanging in the rightmost ~25% of the row, above and below
  the body bar like a card pinned to a corkboard). Pick the tint variant
  matching the product family: sage for Latitude, salmon for OptiPlex GX,
  peach for Dimension/OptiPlex Gs, lime for OptiPlex G Series, sky for
  Dellware, steel for Dimension XPS Pro, periwinkle for PowerEdge. All
  seven share identical chrome — a 1px black border, 12×16px padding,
  sharp corners, Times Roman 14 body — only the fill color changes.
- **cta-block-red** — the homepage's vivid Dell-red panel; white Times
  Roman copy, a 1px frame-ink border, 16px padding. One per page maximum —
  the brand's most aggressive attention-grab, never used for anything but
  a top-tier sales message.
- **phone-callout** — the top-right phone number, red on the black banner,
  Helvetica Bold 16, pinned to every page's top banner.
- **Stickers** — `buy-a-dell-sticker` (yellow rectangle, Helvetica Bold
  "BUY a DELL" with a purple-striped "a", 1px black border, pinned
  top-right of every page), `new-burst-sticker` (angled yellow burst,
  Helvetica Bold black "NEW!", ~15° rotation for a pinned-on-with-tape
  feel), `cert-seal` (round red award seal reading "PC MAGAZINE" ringed by
  "SERVICE · RELIABILITY · READERS' CHOICE," 64px, full rounding).
- **icon-label-nav** — the bottom-of-page navigation row: four hand-drawn
  icons (FIND/HOME/ONLINE STORE/SERVICE & SUPPORT) connected by a thin
  green rule baked into the GIF art, each with an uppercase Helvetica
  label beneath.
- **Inputs & buttons** — `text-input` (white fill, 1px black border, Times
  Roman 14), `button-primary` (black fill, white Helvetica Bold uppercase
  label), `button-secondary` (white fill, inverted colors, same chrome),
  `button-text-link` (bare underlined classic-Mosaic-blue anchor, Times
  Roman 14).
- **footer-band** — the bottom of every page: icon-label nav row,
  classic-blue Copyright link, "(Terms of Use)" parenthetical,
  browser-compatibility fine print, and period browser/OS logo banners.

### Examples (illustrative)

The source document also lists auto-derived "kit-mirror" example surfaces
(`ex-pricing-tier`, `ex-pricing-tier-featured`, `ex-product-selector`,
`ex-cart-drawer`, `ex-app-shell-row`, `ex-data-table-cell`,
`ex-auth-form-card`, `ex-modal-card`, `ex-empty-state-card`, `ex-toast`)
that re-skin modern SaaS/B2B surfaces (pricing tiers, app shells, data
tables, auth forms) using the same brand-native primitives — white/canvas
surfaces, `rounded.none`, and the frame-ink border/divider color — so a
downstream product built in this style stays visually consistent even
when it needs UI patterns 1996 Dell never had.

## Do's and don'ts

**Do**
- Keep the literal black page-frame border on every page — the brand's
  single most identifiable container chrome.
- Reserve Dell red for the CTA panel and the phone callout only; every
  other use dilutes the urgency signal.
- Use the eight ribbon-card tints as a family — pick one per product line
  and stay with it across that line's marketing surfaces.
- Set every display headline in Arial Black 36/900 — the typographic
  register depends on extreme weight against flat color.
- Keep body copy in Times Roman 14; substituting a modern sans loses the
  catalog feel entirely.
- Render every CTA/button at `rounded.none` (0px); modern soft-radius
  buttons betray the era.
- Use hand-painted bevels/hard-edge GIF shadows on stickers and product
  photos — never a soft CSS shadow.

**Don't**
- Don't introduce a chromatic accent outside the eight catalog tints plus
  Dell red, Dell yellow, and classic link blue — the palette is closed by
  design.
- Don't soften any corner; `rounded.none` is universal, only award seals
  get `rounded.full`.
- Don't replace Times Roman body with Arial/Helvetica/Inter/a webfont —
  the serif body is the era's signature.
- Don't add soft drop shadows or atmospheric gradients; the brand runs on
  hard borders and flat fills.
- Don't crop or "tuck" product photos with border-radius or clip-path —
  the notch into the ribbon-card edge is the framing, and the photo itself
  stays a hard rectangle.
- Don't pair two red CTA panels on the same page — the red fill is meant
  to be the singular attention pole.
- Don't strip the phone callout from the top banner — in 1996 the website
  existed to drive phone-call orders, so the phone number IS the
  navigation.

## Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Period default | 800×600 | fixed 760px layout, designed for the era's standard monitor |
| Modern desktop | 1280+px | layout sits centered with generous side gutters, like a magazine spread mid-screen |
| Tablet | 768px | black frame compresses to 4px; ribbon cards stack full-width |
| Mobile | < 480px | black frame to 2px; two-column structure collapses to single column, left-rail icon grid stacking above the product stack |

Touch targets: 1996 had no notion of touch (mouse-only assumptions), so
modern reproductions need to widen the icon-label nav targets to a 44×44px
minimum at mobile — the original icons sat around 24×24 with an 8px label
below, well under modern guidelines. Collapsing strategy: at ≤768px the
homepage's left-rail icon-link grid collapses from a 2×4 grid to a single
column; the ribbon-card photo notch becomes a top-aligned full-width image
at mobile; the top banner's tagline shrinks one type tier and the phone
number wraps below the sticker; the footer icon-label nav stays 4-up at
every width since the icons are small enough to survive. Image behavior:
product photos were authored as bitmap GIFs at fixed pixel widths
(typically 80-120px) with hand-applied bevel shadows via table-cell
negative spacing for the notch effect; modern reproductions should keep
the bevel-shadow effect but use SVG drop-shadow or CSS
`filter: drop-shadow(2px 2px 0 #000)` to recreate it crisply at high-DPI.

## Known gaps

- The Dell purple stripe (`#6a26a4`) only appears inside the "BUY a DELL"
  sticker chrome and wasn't confirmed as a broader system color.
- Animation and transition timing has no meaning here — the original
  pages predate any web animation techniques.
- Form input validation states weren't visible on the captured pages; the
  text-input spec is inferred from period-standard HTML 3.2 form widgets.
- The configurator / order-flow surfaces ("Configure & Buy") weren't in
  the analyzed URL set, so their layout isn't documented here.
- Some `ex-*` illustrative examples carry `TO_FILL` markers in the source
  for properties not directly observed on the captured Dell pages —
  treat those as reasonable extrapolations from the brand-native
  primitives, not literal 1996 artifacts.
