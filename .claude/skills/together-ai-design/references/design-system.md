# Together AI Design System — Full Analysis

Adapted from the Together AI marketing-site design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/together.ai/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Together AI is an AI-cloud infrastructure platform — model inference, GPU
clusters, fine-tuning, the plumbing behind an "AI native cloud" — and its web
surface signals exactly that posture: a near-black hero on top, a long ribbon
of white technical content in the middle, and one recurring piece of brand
chrome — a three-color orange-magenta-periwinkle gradient ribbon — doing the
entire job of "we are not just another grey enterprise SaaS." There's no
other illustration system; the gradient carries the whole brand.

Type is the second decisive voice. Two faces carry every page: a custom
geometric display sans (documented here as "The Future") for headlines and
body, set at weight 500 with tight, slightly negative letter-spacing so
64px hero type feels poured rather than typed; and an uppercase monospace
eyebrow ("PP Neue Montreal Mono") that labels every section, button, and
cell header. Headlines stay sentence-case; anything technical goes uppercase
mono — a deliberate tonal contrast: serious enough to use a monospace label,
modern enough to keep the headline out of it.

Surfaces alternate aggressively: `colors.canvas-dark` (`#010120`) for the
hero, research band, and "Grounded in cutting-edge research" section, then
`colors.canvas` (white) for product, pricing, and testimonials, with
`colors.hairline` reserved for table-header rows and toggle backgrounds.
Pastel `colors.accent-mint` tinted stat tiles break up the white middle.
Cards are universally lightly rounded (4px) with hairline borders — never
floating on shadows.

**Key characteristics:**
- A single black `colors.primary` CTA pill carries every conversion target
  across pricing, footer, and sign-in. Mint and white pill variants are
  reserved for hero contexts only.
- A three-color brand gradient (orange → magenta → periwinkle) is the entire
  decorative system, used as the hero ribbon graphic and never reduced to a
  swatch elsewhere.
- All-caps mono eyebrows and button labels appear everywhere — section
  titles, model-row headers, pricing-table labels.
- A near-universal 4px card/button radius, with one off-value (3.25px) inside
  pricing-tab pills and a full pill reserved only for the floating chat-
  launcher orb.
- Dual surface mode — alternating dark and white bands with no in-between
  greys; the single soft surface tone exists only to mark table-header rows.
- A massive `together.ai` wordmark banner at the bottom of every page, tinted
  nearly into the canvas, acting as a "we are here" sign-off that doubles as
  a footer separator.

## Colors

### Brand & accent
- **Ink black** — the single primary CTA color: the black pill carries "Sign
  in," "Contact sales," "Get started now," and every footer CTA.
- **Brand orange / magenta / periwinkle** — the three legs of the brand
  gradient, appearing in the hero ribbon graphic; never used as a standalone
  UI fill.
- **Brand mint** — a pastel cyan outside the gradient, used for hero
  secondary-CTA pills and tinted stat tiles.

### Surface
- **Canvas** — the default product/pricing/docs background, white.
- **Hairline / canvas soft** — the brand's single soft surface tone, used for
  data-table header rows, toggle-pill rails, and 1px dividers.
- **Canvas dark** — the brand's dark hero surface.
- **Hairline on dark** (`surface-dark-soft`) — 1px dividers and badge
  backgrounds on dark surfaces.

### Text
- **Ink** — every heading and body paragraph on light surfaces.
- **Body** — secondary text: captions, table-cell secondary values, footer
  link text.
- **On dark** — all text on canvas-dark surfaces, white.

### Semantic
The brand doesn't maintain a separate error/success palette on its public
surface; validation cues lean on the primary black or the brand gradient
depending on context, with framework defaults adopted where none is
documented.

### Brand gradient
The signature decoration is a three-stop gradient — orange → magenta →
periwinkle — applied as the only piece of decorative chrome (the hero ribbon
graphic). Treat it as one unified object: don't crop it to a single color,
reorder its stops, or add a fourth stop. It's used at large scale, never
miniaturized to icon size.

## Typography

### Families
- **A custom geometric display sans** ("The Future") for every headline,
  lead paragraph, body copy, non-uppercase button label, and inline link.
  Weights 400 and 500 are the working pair — the face never appears bold.
  Tight negative letter-spacing (-1.92px at 64px, -0.16px at 16px body) gives
  it a slightly condensed, poured-on-the-page feel.
- **An uppercase mono caption face** ("PP Neue Montreal Mono") for every
  eyebrow, button label, table-header cell, and pricing-table tab. Weight 500
  at 11–16px, always uppercase, with small positive letter-spacing
  (0.05–0.55px). This carries the brand's technical voice.

Substitute with **Inter** (400/500, `font-feature-settings: "ss01"`, tighten
tracking ~0.6% at display sizes) for the display sans, or **Geist** as a
second option. For the uppercase mono, **JetBrains Mono** or **Geist Mono**
at weight 500 with `text-transform: uppercase` and tracking bumped to
`0.04em` is the closest match.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale (display-xxl 64px
down to mono-caption 10px). Principles:
- The two-face contrast *is* the voice — display sans for narrative,
  uppercase mono for technical labels. Never let mono carry a paragraph;
  never let the display sans carry a button label.
- Negative letter-spacing belongs to the display sans only; the mono face
  uses small positive tracking.
- Headlines stay sentence-case — every uppercase moment belongs to the mono
  face.

## Layout

- Base spacing unit: 4px — nearly every captured value is a multiple of 4,
  aside from two gap-multiplier derivatives (7.2px, 55.2px).
- Marketing bands use 80px top/bottom padding on desktop; pricing tables
  tighten to 48px to keep dense data legible.
- Card interior padding: 24px on research/testimonial cards, 32px on stat
  tiles.
- Inline gaps: 12px between button/nav row siblings, 8px between chip-group
  items.
- Max container width: ~1280px desktop, with 32px horizontal gutters on
  desktop and 16px on mobile.
- Column patterns: research/testimonial grids run 3-up desktop → 1-up mobile;
  article cards run 2-up → 1-up; the hero splits 50/50 (headline left, ribbon
  graphic right) at desktop, stacking with the graphic above type on mobile.
- Surface contrast does most of the separating: a dark band ends, 80px of
  breathing room, the next light band begins. Inside a band, headline and
  lead paragraph hug close (16px) before a wider gap to the supporting visual
  or CTA cluster. Pricing tables keep rows tight (12px vertical) — reading
  more like a sheet than a marketing component.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 — Flat | No shadow, no border | Most cards on light surfaces lean on hairline borders |
| 1 — Hairline | 1px solid hairline on canvas cards | Testimonial cards, article cards, data-table rows |
| 2 — Hairline on dark | 1px solid surface-dark-soft on canvas-dark cards | Research-band cards, on-dark badges |
| 3 — Soft drop | `rgba(1,1,32,0.1) 0 4px 10px` | Floating elements — the chat-launcher orb, sticky-bottom nav |

### Decorative depth
- The hero's three-stop gradient ribbon is the page's only true atmospheric
  effect — layered translucent shapes implying depth without leaving the
  brand palette.
- A dark code-editor mockup inside the otherwise-white product band acts as a
  one-step lift, mirroring the hero's polarity flip.
- The giant `together.ai` wordmark at the bottom sits technically on white
  but is tinted toward the hairline tone, reading as a faint stencil and
  giving the page a final "you have arrived" sign-off.

## Shapes

| Token | Value | Use |
|---|---|---|
| rounded.none | 0px | Hero/research full-bleed bands, footer wordmark banner |
| rounded.xs | 3.25px | The pricing page's slightly tighter sub-tab and outline button |
| rounded.sm | 4px | The brand's canonical radius — buttons, badges, cards, table rows, stat tiles |
| rounded.md | 8px | Feature-tab pills, larger pricing-tab containers |
| rounded.full | 9999px | The floating chat-launcher orb — the only fully-pill shape in the system |

Photography plays a minor role next to the ribbon: customer logos render as
grayscale vector marks at a consistent ~24px height; testimonial portraits
use a hard-edged 1:1 square crop (no avatar pill); article thumbnails run
16:9 with a 4px top-corner radius on the image only, while the card chrome
around it stays square.

## Components

Definitions live in `design-tokens.yaml → components`. Summary:
- **Buttons** — `button-primary` (black pill, canonical CTA), hero-only
  `button-secondary-mint` / `button-secondary-white`, `button-ghost-on-dark`,
  `button-outline`, and `button-icon-circular` (the one full-pill shape, for
  the chat-launcher orb).
- **Cards** — `research-card`, `testimonial-card`, `article-card`,
  `code-editor-mockup`, `stats-card-tinted`.
- **Inputs** — `text-input`, 4px radius, hairline border.
- **Navigation** — `nav-bar` (dark on the hero, switches to white after
  scroll) and `nav-link`.
- **Data/pricing** — `data-table-row`, `data-table-header`,
  `toggle-pill-group`, `pricing-sub-tab`, `feature-tab-pill`.
- **Badges** — `badge-neutral`, `badge-subtle-on-dark`.
- **Signature** — `hero-band-dark`, `research-band-dark`,
  `footer-wordmark-banner`.
- A set of illustrative `ex-*` entries (pricing tiers, auth form, modal,
  toast, etc.) mirror the core primitives for common SaaS surfaces the source
  site doesn't literally have — they're derived, not directly observed.

## Do's and don'ts

**Do**
- Reserve the black primary for every primary CTA — one black pill per
  visible viewport.
- Set every section eyebrow and button label in the uppercase mono face.
- Pair the brand gradient at hero scale only.
- Cycle page surfaces dark → white → dark; let that contrast carry elevation.
- Use the canonical 4px radius across the system; reserve the full pill for
  the one floating chat orb.
- Render the giant `together.ai` wordmark banner at the bottom of long pages,
  tinted toward the hairline tone.

**Don't**
- Don't introduce a fifth accent color — the gradient plus the mint pill is
  the entire decorative palette.
- Don't set body paragraphs in the mono face.
- Don't center-align body paragraphs under a left-aligned display headline.
- Don't drop a soft shadow on light-surface cards — hairlines and surface
  contrast carry elevation instead.
- Don't reduce the brand gradient to a single color, reorder its stops, or
  add a fourth stop.
- Don't switch the primary button to a full pill, and don't set headlines in
  all-caps mono.

## Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Mobile | <479px | Hero stacks; nav collapses to hamburger; multi-col grids drop to 1-up |
| Mobile-Large | 479–767px | Same as Mobile; some tables enable horizontal scroll |
| Tablet | 768–991px | Article grid moves to 2-up; testimonial grid stays 3-up only above ~900px container width |
| Desktop | 992–1279px | Full 3-up research grid, 2-up article grid, hero 50/50 split |
| Desktop-Large | ≥1280px | Container caps at 1280px; bands stay edge-to-edge in color while content centers |

The mono-cap button label sits at ~32px tall by default but is inflated to
≥44px on mobile through extra vertical padding, meeting WCAG AAA; the
circular icon button renders at 44×44px minimum at every viewport. Nav
collapses to a full-overlay hamburger drawer on mobile; the hero stacks
headline above a smaller ribbon graphic (never below); the research band
drops from 4-up to 2-up to 1-up; pricing tables enable horizontal scroll on
tablet and stack model-name above price on mobile. The footer wordmark banner
scales fluidly and always stays edge-to-edge.

## Known gaps

- The custom display sans and mono caption face are proprietary; documented
  Inter/Geist substitutes approximate but don't exactly reproduce their
  metrics.
- The `ex-*` component entries are auto-derived illustrative mirrors for
  surfaces the source site doesn't literally contain (e.g., an e-commerce
  cart) — treat them as a starting point, not observed fact.
- No explicit error/success semantic palette is documented; framework
  defaults are the suggested fallback.
