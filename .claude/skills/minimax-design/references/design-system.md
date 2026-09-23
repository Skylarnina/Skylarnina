# MiniMax Design System — Full Analysis

Adapted from the MiniMax design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/minimax/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

MiniMax presents itself as a Chinese AI infrastructure brand with a
deliberate dual identity. Marketing and platform pages anchor in a stark
white canvas with deep-black typographic emphasis — the brand voice reads
confident, technical, almost editorial. But every model release gets its
own vibrant gradient identity card: M2.7 in volcanic coral-red, Music 2.6
in magenta-pink, Hailuo in deep blue, Speech 2.8 in saturated orange-
purple. Laid out together on the homepage, these tiles read like album
covers, each declaring its own product personality inside a shared
monochrome system.

DM Sans anchors every surface, from an oversized 80px hero display down to
a 12px micro label. Its geometric, slightly humanist character works both
for dense documentation (14px body copy at 1.5 line-height for long-form
reading) and for high-impact marketing displays (-2px letter-spacing at
80px). Buttons are universally pill-shaped, with a sharp two-tier system:
a black-pill primary as the dominant CTA and an outline-pill secondary.
Cards split into two distinct families: vibrant gradient product showcases
at 32px corner softening, and quiet white documentation cards at 16px.

**Key characteristics:**
- A stark monochrome base — black and white — broken open only by
  saturated brand-color gradient cards.
- Distinct product-color encoding: each model line owns its own vibrant
  color (coral M2.7, magenta Music 2.6, blue Hailuo, orange/purple
  Speech 2.8).
- DM Sans across the entire system, with Inter as fallback.
- Pill-shaped buttons and tabs everywhere; rectangular forms only appear
  inside data tables and dense docs.
- Hero typography runs tight 1.10 line-height with -2px letter-spacing for
  impact.
- Documentation uses a 3-column layout: left sidebar nav, center prose
  body, right table-of-contents.
- Black promo banners above the nav mark time-bound brand moments.

## Colors

> Source pages: the MiniMax homepage, the M2.7 model showcase, the
> platform documentation guides, and the token-plan pricing page. Token
> coverage was identical across all four pages.

### Brand & accent
- **Brand coral** — the signature high-impact accent, used on the M2.7
  product card, the Token Plan hero band, promo CTA strips, and "NEW"
  badges; carries the brand's most attention-grabbing energy.
- **Brand magenta** — secondary product-card identity for Music 2.6, used
  for music/audio product encoding.
- **Brand blue** — the Hailuo video product identity and the primary blue
  accent across the system.
- **Brand blue deep** — form-control activation and link emphasis.
- **Brand blue 700** — documentation tag and reference text color.
- **Brand cyan** — an atmospheric blue used in product gradients and
  decorative washes.
- **Brand blue 200** — code badges and info-tag backgrounds.
- **Brand purple** — the Speech 2.8 product identity and a minor
  purple-product accent, gradient mate to magenta.

### Surface
- **Canvas white** — the primary page background and card surface.
- **Surface / surface soft** — subtle section backgrounds and quieter
  section divisions.
- **Hairline / hairline soft** — 1px input border and primary divider,
  with a quieter variant for table-row dividers.

### Text
- **Ink / ink strong** — the brand's near-black anchor for headlines and
  CTA text, with a pure-black variant for promo banners and hero displays.
- **Charcoal** — body text on light surfaces.
- **Slate** — secondary text and metadata.
- **Steel** — tertiary text, table headers, sidebar inactive items.
- **Stone** — muted captions and inactive tab labels.
- **Muted** — footer link text and de-emphasized labels.

### Semantic
- **Success background / success text** — a pale-green wash paired with
  deep-green ink for success badges and confirmations. Error tones derive
  from a dedicated red used only for input border error states, not
  formalized as a top-level token.

## Typography

### Family
DM Sans, a geometric variable sans-serif, is used across every surface and
every role, with Inter/Helvetica Neue/Helvetica/Arial as fallbacks. It was
chosen for its dual fluency: it scales cleanly from an 80px hero display
(where -2px letter-spacing creates magazine-grade tightness) down to a
12px micro label (where slightly humanist counters keep it legible). The
brand's deployment carries no italic variant — emphasis comes entirely
from weight (500/600/700).

### Hierarchy
See `design-tokens.yaml → typography` for the full scale (hero-display at
80px down to micro at 12px). Principles:
- Tight hero leading (1.10) and aggressive negative letter-spacing on
  display sizes create a magazine-quality typographic display unique to
  MiniMax.
- Generous body leading (1.50) keeps long-form documentation comfortable;
  captions push to 1.70 for scientific-paper-grade clarity.
- Weight discipline: 400 for body, 500 for medium emphasis, 600 for
  headings and buttons, 700 for strong inline emphasis — heavier weights
  never appear.
- A single-typeface strategy: DM Sans never mixes with another sans-serif.
  Code samples fall back to a system monospace, but no second typeface
  enters the brand canvas.

## Layout

### Spacing system
- Base unit: 4px, with 8px as the primary increment.
- Section rhythm: marketing pages separate at 96px above the fold, then
  80px below; documentation tightens to 64px; table rows compress to 16px.
- Card internal padding: vibrant product cards use 32px; documentation
  cards use 20-24px; promo strips expand to 64px.

### Grid & container
- Marketing pages use a 1280px max-width with 32px gutters.
- The homepage product matrix renders as a 4-column row of 32px-rounded
  gradient cards, each roughly 280-320px wide, with a 4-column grid of
  16px-rounded white cards below it.
- Documentation uses a 3-column layout: a left sidebar (~220px), a center
  prose column (~720px max-width), and a right table-of-contents (~180px).
  The sidebar persists on desktop and collapses to a drawer below 1024px.
- The pricing page uses 2-column tabs above a 3-column tier card grid.

### Whitespace philosophy
Marketing pages give product photography and color cards generous
breathing room — 96px above the fold creates visual oxygen for the 80px
hero display. Inside documentation, whitespace tightens dramatically:
section gaps drop to 32px, table rows pack down to 16px, and the sidebar
nav uses an 8px vertical rhythm.

## Elevation & depth

The system runs predominantly flat. Elevation is reserved for sticky
panels, dropdowns, and the rare floating CTA.

| Level | Treatment | Use |
|---|---|---|
| 0 (flat) | No shadow; hairline border | Default cards, table rows, form inputs |
| 1 (subtle) | `rgba(0,0,0,0.04) 0px 1px 2px 0px` | Card-recommendation, hover-elevated tiles |
| 2 (card) | `rgba(0,0,0,0.08) 0px 4px 6px 0px` | Standard feature cards, dropdowns |
| 3 (atmospheric) | `rgba(0,0,0,0.08) 0px 0px 22px 0px` | Diffuse glow on featured product cards |
| 4 (modal) | `rgba(36,36,36,0.08) 0px 12px 16px -4px` | Modals, confirmation dialogs, sticky panels |

### Decorative depth
The vibrant gradient product cards carry their own atmospheric depth via
internal radial gradients and silhouette imagery — no shadow is needed;
the color does the work. Brand-tinted shadows appear under purple-themed
cards for subtle ambient lift, and dotted/grain textures occasionally
appear inside product cards as photographic-content decoration, not
formalized system tokens.

## Shapes

### Border radius scale

| Token | Value | Use |
|---|---|---|
| xs | 4px | Code chips, micro-controls |
| sm | 6px | Compact controls, table cells |
| md | 8px | Inputs, secondary buttons, search pill |
| lg | 12px | Documentation cards, recommendation tiles |
| xl | 16px | Standard feature cards, AI product tiles |
| xxl | 20px | Larger feature panels |
| xxxl | 24px | AI product tile feature variants |
| hero | 32px | Vibrant gradient product cards, promo CTA strip |
| full | 9999px | All buttons, all pill tabs, badges |

### Photography geometry
Vibrant product cards use 32px corner softening — distinct from the 16px
used on quiet white cards; the doubled radius is the visual signature of
"this is a featured product moment." Product imagery inside cards is
treated as photographic content (silhouettes, dark portrait studio
lighting) without rounded internal frames. Avatar circles, where they
appear in testimonials, are perfect circles.

## Components

Definitions live in `design-tokens.yaml → components`.

> Per the source's no-hover policy, hover states are not documented — only
> default and pressed/active states.

### Buttons
- **Primary** — black pill, the dominant action across all surfaces, with
  a charcoal pressed state and a muted disabled state.
- **Secondary** — outlined pill, paired with primary in dual-CTA hero
  patterns.
- **Tertiary** — white-fill quieter pill for tertiary nav and
  informational CTAs.
- **Link** — an inline text link styled as a subtle button, underlining on
  activation.
- **Icon circular** — 36×36px circular utility button for carousel
  arrows, share, and copy.

### Vibrant product cards
Coral (M2.7/Token Plan), magenta (Music 2.6), blue (Hailuo Video), purple
(Speech 2.8), and a dark portrait-photo variant — each at 32px rounding
with 32px padding, hosting a product wordmark in massive display type over
a white tagline.

### Cards & containers
- **Base / feature** — standard documentation and feature cards, white or
  light-surface, 16px rounding.
- **Recommendation** — the "Recommended Reading" tile in documentation
  footers.
- **Promo CTA card** — a bright coral promo strip with an embedded white
  "Join Now" pill button.
- **AI product tile** — white cards in the AI Product Matrix grid (Agent,
  Hailuo Video, MiniMax Audio), with an icon/illustration zone, title, and
  description.

### Inputs & forms
Standard text input at 40px height with hairline border, a deep-blue
2px focus border, and a red error border; a documentation top-bar search
pill.

### Tabs
Underline-style segmented tabs (Benchmark / Self-Evaluation / Multi-Agent
Collaboration) and pill-style tabs (Token Plan / Audio Subscription /
Video Package), the active pill filling solid black.

### Badges & status
Success (pale green), new (coral), beta (pale blue), and inline code
badges, plus a black promo banner sitting above the top nav for
time-bound offers like "Invite & Earn."

### Data tables
A bordered table with a light-gray header row and hairline row dividers,
used for the documentation models-comparison table.

### Navigation
Marketing top nav: sticky white bar with the MiniMax wordmark, a
horizontal link list, and black-pill/outlined-pill CTAs on the right.
Documentation/platform nav compresses further, centering a search pill
with account/upgrade CTAs to the right. The sidebar carries inactive/
active link states, and the right rail carries table-of-contents links.

### Signature components
- **Hero band marketing** — a centered hero with the massive 80px display
  and a dual-CTA pair.
- **Product matrix grid** — the 4-column horizontal scroll of vibrant
  gradient product cards, uniform in height, scrolling horizontally on
  mobile.
- **AI product matrix** — the 4-column grid of white product tiles below
  the vibrant matrix.
- **Docs prose block** — the documentation main content area, max-width
  ~720px, with inline code on a light background.
- **Testimonial stat row** — a horizontal row of four stat cells with
  large numbers and labels below.
- **Footer** — a dense black-canvas multi-column footer with the wordmark,
  tagline, social icons, and a four-column link grid.

## Do's and don'ts

**Do**
- Use black as the dominant CTA — it's the brand's most recognizable
  interactive element.
- Reserve product brand colors (coral, magenta, blue, purple) strictly for
  product-identity moments — never for general buttons or text.
- Pair 32px gradient cards with 16px white cards in the same viewport —
  the radius contrast is the visual signature.
- Apply full pill radius to every button, pill tab, and badge.
- Use the 80px hero display with -2px letter-spacing for hero displays —
  never compromise the leading or letter-spacing.
- Treat each model/product line as a distinct color identity — these are
  brand assignments, not free choices.

**Don't**
- Don't use brand-coral or brand-magenta on body text or large surfaces —
  they lose meaning when overused.
- Don't soften button corners below full pill; the pill is a brand
  signature.
- Don't introduce a second display typeface — DM Sans handles every role.
- Don't reduce hero leading below 1.10 — the 80px display needs that
  breathing room.
- Don't apply heavy shadows on white cards; flat-with-borders is the
  documentation default.
- Don't put gradient backgrounds on standard buttons — gradients are
  reserved for product-card identity moments.

## Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Mobile small | < 480px | Single column; hero drops to 40px; pill nav collapses to hamburger; product matrix scrolls horizontally; footer becomes a 1-column accordion |
| Mobile large | 480-767px | Same as small, but the AI product matrix renders 2-up |
| Tablet | 768-1023px | 2-column AI product matrix; pill-tab nav returns; documentation sidebar collapses to a drawer |
| Desktop | 1024-1279px | Full 4-column product matrix; 3-column docs grid |
| Wide desktop | ≥ 1280px | Wider hero gutters, larger product photography, fixed 220px sidebar |

Touch targets stay comfortable: pill buttons render at 38-40px effective
height and bump to 44px on mobile; circular icon buttons step from 36px to
44px; form inputs step from 40px to 44px; sidebar nav items bump from
~32px to 44px in mobile drawers. The promo banner stays full-width,
truncating below 480px; the top nav collapses to hamburger below 1024px;
the documentation grid steps from 3-column to a sidebar drawer to a
single column; the product matrix moves from a 4-column row to a
horizontal-scroll carousel below 1024px; and hero typography steps from
80px down to 56px, 40px, and finally 32px as the viewport narrows.

## Known gaps

- Specific dark-mode token values (canvas, surface, ink, hairline) aren't
  surfaced on these pages — the brand hasn't yet shipped a published
  dark-mode palette.
- Animation/transition timings aren't extracted; 150-200ms ease for
  hover/focus transitions is a reasonable default.
- Form validation success states beyond the default green-border/badge
  pattern weren't explicitly captured.
- The code syntax-highlighting palette inside docs isn't formalized;
  documentation samples appear with system-default monospace and minimal
  coloring.
