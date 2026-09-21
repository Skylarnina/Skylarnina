# Claude (Anthropic) Design System — Full Analysis

Adapted from the Claude design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/claude/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Claude.com is the warmest, most editorial interface in the AI-product
category. Its base atmosphere is a tinted cream `colors.canvas`
(`#faf9f5`) — deliberately warm, not the cool gray-white every other AI
brand defaults to. Headlines run a slab-serif display face ("Copernicus" /
Tiempos Headline) at weight 400 with negative letter-spacing, paired with
**StyreneB / Inter** body sans. Together they read like a literary
publication rather than a SaaS marketing page.

Brand voltage comes from the cream-plus-coral pairing: coral
(`colors.primary` — `#cc785c`) is Anthropic's signature accent, used on
every primary CTA, on the brand wordmark, and on full-bleed callout cards.
It's warm and slightly muted, never cyan or blue — a deliberate
counter-position against OpenAI's cool slate, Google's saturated blue, and
Microsoft's corporate cyan.

Three surface modes alternate page-by-page: the cream canvas as the default
body floor, light cream cards (`surface-card`) for feature explanations,
and dark navy product surfaces (`surface-dark`) for code-editor mockups,
model comparison tables, agentic-flow diagrams, pre-footer CTAs, and the
footer itself. That cream-to-dark contrast is the page's core pacing
rhythm.

**Key characteristics:**
- Warm cream canvas (`#faf9f5`) with dark warm-ink text (`#141413`) — the
  brand's defining color choice.
- Coral primary CTA (`#cc785c`), used scarcely on individual buttons and
  generously on full-bleed coral callout cards.
- Slab-serif display headlines (Copernicus / Tiempos Headline) at weight
  400 with negative letter-spacing, paired with humanist sans body for a
  literary editorial voice.
- Dark navy product-mockup cards (`#181715`) carrying code blocks, terminal
  panels, and model-comparison data — real product chrome shown at scale
  rather than abstract marketing illustrations.
- Light cream feature cards (`#efe9de`), one step darker than canvas, used
  for content-driven feature explanations.
- The Anthropic radial-spike mark — a small black four-spoke asterisk-like
  glyph — appears as a wordmark prefix and as a content marker.
- Radius is hierarchical: `8px` buttons/inputs, `12px` content and product
  cards, `16px` the hero illustration container, pill for badges.
- Section rhythm sits at `spacing.section` (96px); internal card padding is
  generous at `spacing.xl` (32px).

## Colors

### Brand & accent
- **Coral / Primary** (`#cc785c`) — the signature Anthropic warm coral,
  used on every primary CTA background, full-bleed coral callout cards, and
  the brand wordmark accent — the most-recognized Anthropic color outside
  the spike-mark logo.
- **Coral Active** (`#a9583e`) — the press/darker variant.
- **Coral Disabled** (`#e6dfd8`) — a desaturated cream-tinted disabled
  state.
- **Accent Teal** (`#5db8a6`) — used sparingly on secondary product
  surfaces (terminal status indicators, "active connection" dots).
- **Accent Amber** (`#e8a55a`) — a small companion warm tone for category
  badges and inline highlights.

### Surface
- **Canvas** (`#faf9f5`) — the default page floor: tinted cream, warm,
  deliberately not pure white.
- **Surface Soft** (`#f5f0e8`) — section dividers and very soft band
  backgrounds.
- **Surface Card** (`#efe9de`) — feature and content cards, one step
  darker than canvas.
- **Surface Cream Strong** (`#e8e0d2`) — the strongest cream variant, used
  on selected category tabs and emphasized section bands.
- **Surface Dark** (`#181715`) — code-editor mockups, model-showcase
  cards, and the footer — the dominant dark surface.
- **Surface Dark Elevated** (`#252320`) — elevated cards inside dark bands
  (settings panels in mockups).
- **Surface Dark Soft** (`#1f1e1b`) — a slightly lighter dark used for code
  block backgrounds inside larger dark cards.
- **Hairline** (`#e6dfd8`) — the 1px border tone on cream surfaces; it
  shares its hex with `primary-disabled`, so borders read like one
  elevation step rather than an ink line.
- **Hairline Soft** (`#ebe6df`) — a barely-visible divider inside the same
  band.

### Text
- **Ink** (`#141413`) — all headlines and primary text: warm dark, slightly
  off pure black.
- **Body Strong** (`#252523`) — emphasized paragraphs, lead text.
- **Body** (`#3d3d3a`) — default running-text color.
- **Muted** (`#6c6a64`) — sub-headings, breadcrumbs, footer-adjacent
  secondary text.
- **Muted Soft** (`#8e8b82`) — captions, fine print, copyright lines.
- **On Primary** (`#ffffff`) — text on coral buttons.
- **On Dark** (`#faf9f5`) — cream-tinted white used on dark surfaces,
  echoing the canvas tone.
- **On Dark Soft** (`#a09d96`) — footer body text and secondary labels in
  dark mockups.

### Semantic
- **Success** (`#5db872`) — green status dots, "available" indicators.
- **Warning** (`#d4a017`) — warning callouts, rare on marketing surfaces.
- **Error** (`#c64545`) — validation errors.

## Typography

### Font family
Copernicus (or Tiempos Headline as substitute) is the slab-serif display
face for headlines, and StyreneB (or Inter as substitute) is the humanist
sans for body, navigation, and UI labels. JetBrains Mono handles code
blocks. Fallback stacks: `Tiempos Headline, Garamond, "Times New Roman",
serif` for display, `Inter, -apple-system, BlinkMacSystemFont, "Segoe UI",
Roboto, sans-serif` for body.

The display/body split is editorial: Copernicus serif (weight 400,
negative tracking) sets h1/h2/h3 and hero display; StyreneB sans (weight
400-500) carries body, navigation, buttons, captions, and labels;
JetBrains Mono carries all code blocks and terminal text.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale. Key entries:
`display-xl` (64/400, -1.5px tracking, homepage h1 in Copernicus),
`display-lg` (48/400, -1px, section heads), `display-md` (36/400, -0.5px,
sub-section heads and model names), `display-sm` (28/400, -0.3px, pricing
tier names and callout headlines), `title-lg` (22/500, pricing plan size
labels — StyreneB), `title-md` (18/500, feature card titles), `body-md`
(16/400, running text), `code` (14/400, JetBrains Mono), `button` (14/500).

### Principles
Display sizes stay at weight 400, never bold. Negative letter-spacing
(-0.3 to -1.5px) is essential — Copernicus without it reads as off-brand.
The serif character is what gives Anthropic its literary, considered
voice; swapping to a sans-serif display would make Claude feel like every
other AI tool. Body type holds weight 400 for paragraphs and weight 500 for
labels and emphasized phrases. The sans body is humanist (StyreneB), never
geometric — Inter is an acceptable substitute for its similar humanist
proportions, while Helvetica or Arial would be too neutral and break the
warm-editorial feel.

### Font substitutes
If Copernicus / Tiempos Headline is unavailable, **Cormorant Garamond** at
weight 500 with -0.02em letter-spacing is the closest open-source
approximation, with **EB Garamond** as a fallback. For StyreneB, **Inter**
is the closest match — both are humanist sans designed for screen reading.
**Söhne** is another close alternative if licensed.

## Layout

- **Base unit:** 4px. Full scale: `xxs` 4px, `xs` 8px, `sm` 12px, `md` 16px,
  `lg` 24px, `xl` 32px, `xxl` 48px, `section` 96px.
- **Section padding:** `spacing.section` (96px), a modern-SaaS rhythm.
- **Card internal padding:** `spacing.xl` (32px) for feature cards, pricing
  tier cards, and model comparison cards; `spacing.lg` (24px) for
  code-window cards and connector tiles.
- **Callout / CTA bands:** `spacing.xxl` (48px) inside coral callout cards;
  64px inside the larger dark CTA band.
- **Max content width:** roughly 1200px centered.
- **Grid:** single 12-column grid for editorial body, with the hero often
  using a 6/6 split (headline left, illustration right); feature card grids
  run 3-up desktop, 2-up tablet, 1-up mobile; connector tile grids run 4-up
  or 6-up desktop, 2-up tablet, 1-up mobile; pricing grids run 3-up desktop
  (Free/Pro/Team/Enterprise), 1-up mobile.
- **Whitespace philosophy:** the cream canvas, serif display, and generous
  internal padding together create an editorial pacing — Claude reads like
  a long-form magazine column rather than a marketing template. Whitespace
  between bands stays uniform at 96px; whitespace inside cards is generous
  at 32px, letting type breathe.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| Flat | no shadow, no border | body sections, top nav, hero bands |
| Soft hairline | 1px `hairline` border | inputs, sub-nav, occasionally on cards |
| Cream card | `surface-card` background, no shadow | feature cards, content cards |
| Dark surface card | `surface-dark` background, no shadow | code-editor mockups, model-showcase cards |
| Subtle drop shadow | faint shadow at low alpha (`0 1px 3px rgba(20,20,19,0.08)`), rarely used | hover-elevated states |

The elevation philosophy is color-block first, shadow rare — most depth
comes from the cream-vs-dark surface contrast rather than drop shadows.
Dark-surface mockups carry their own internal product chrome (code-editor
scrollbars, line numbers, syntax highlighting) that adds detail without
needing external shadows. The Anthropic spike-mark glyph appears as a small
black mark in the wordmark and inline as a content marker; code-editor
mockups carry syntax-highlighted text in muted blues/oranges/grays, line
numbers in `muted-soft`, and status bars in `surface-dark-elevated`. Some
hero illustrations use simple line art with coral and dark-navy strokes on
cream — minimal and hand-drawn-feeling, never photorealistic.

## Shapes

| Token | Value | Use |
|---|---|---|
| `rounded.xs` | 4px | badge accents, tiny dropdowns |
| `rounded.sm` | 6px | small inline buttons, dropdown items |
| `rounded.md` | 8px | standard CTA buttons, text inputs, category tabs |
| `rounded.lg` | 12px | content cards (feature, pricing, code-window, model-comparison) |
| `rounded.xl` | 16px | hero illustration container, larger marquee components |
| `rounded.pill` | 9999px | badge pills, "NEW" tags |
| `rounded.full` | 9999px / 50% | avatar substitutes, icon buttons |

Claude's hero rarely uses photography; instead it relies on simple
line-art illustrations with coral and dark-navy strokes on cream, code
editor mockups (the dominant "hero" treatment on developer-focused pages),
terminal-output mockups, and model-comparison cards (Opus / Sonnet / Haiku)
with abstract geometric thumbnails. When photography does appear (mostly
testimonials), avatars crop to perfect circles at 40px diameter.

## Components

Definitions live in `design-tokens.yaml → components`. Summary:
- **top-nav** — cream 64px bar with the spike-mark and "Claude" wordmark
  at left, a primary menu (Product, Solutions, Use Cases, Pricing,
  Research, Company), and a right cluster with "Sign in" and a coral "Try
  Claude" button.
- **Buttons** — `button-primary` (coral fill, white text, 8px radius,
  darkens on press), `button-secondary` (cream with hairline outline),
  `button-secondary-on-dark` (stays dark over dark cards rather than
  inverting to light), `button-text-link`, `button-icon-circular` (36px),
  `text-link` (coral inline links).
- **Cards & containers** — `hero-band` (6/6 grid hero, 96px padding),
  `hero-illustration-card` (16px-radius card holding either a coral-stroke
  illustration or a dark code-editor mockup), `feature-card` (cream card,
  32px padding), `product-mockup-card-dark` (dark navy card showing real
  Claude product chrome), `code-window-card` (dark card with line numbers
  and syntax-highlighted JetBrains Mono code — the signature visual of
  Claude Code pages), `model-comparison-card` (Opus/Sonnet/Haiku
  comparison with a text-link), `pricing-tier-card` (cream, plan name in
  StyreneB, price in serif Copernicus, checklist, CTA),
  `pricing-tier-card-featured` (flips to dark surface as the signal),
  `callout-card-coral` (full-bleed coral card with an inverted button),
  `connector-tile` (logo + name + description in the integrations grid).
- **Inputs** — `text-input` (cream, 8px radius, hairline border, 40px
  height), `text-input-focused` (border shifts to coral with a 3px
  coral-at-15%-alpha ring), `cookie-consent-card` (bottom-right floating
  dark banner — one of the few places dark appears at small scale on cream
  pages).
- **Tags** — `badge-pill` (gray fill), `badge-coral` (coral fill for
  "NEW"/"BETA" labels, uppercase caption type).
- **Tabs** — `category-tab`/`category-tab-active` in sub-nav rows; active
  state uses `surface-card` background.
- **CTA / footer** — `cta-band-coral` (full-width coral pre-footer band
  with a serif h2 and cream button), `cta-band-dark` (dark alternative on
  developer-focused pages, often paired with a code-window card), `footer`
  (dark navy, 4-column link list, spike-mark wordmark at top, never
  inverts).

## Do's and don'ts

**Do**
- Anchor every page on the cream canvas — pure white reads as "any other
  AI tool," and the warm tint is the brand differentiator.
- Use Copernicus serif for every display headline paired with StyreneB
  sans body; negative letter-spacing on display sizes is non-negotiable.
- Reserve coral for primary CTAs and full-bleed coral callout moments —
  don't paint accent moments coral elsewhere.
- Show actual Claude product chrome (code windows, model-comparison cards)
  instead of illustrating it.
- Alternate cream feature cards with dark navy product-mockup cards — that
  rhythm is the brand's pacing mechanism.
- Use the Anthropic spike-mark glyph as the wordmark prefix; never invert
  it to white-on-dark within the wordmark itself.
- Apply `spacing.section` (96px) between major bands.

**Don't**
- Don't use cool grays or pure white for canvas — cream is the brand.
- Don't bold the serif display weight; Copernicus at 700 reads as
  bombastic, so the system stays at 400.
- Don't use cool blue or saturated cyan as a brand accent — coral is the
  brand voltage.
- Don't put coral everywhere — it's scarce on individual elements and
  generous only on full-bleed coral callout cards.
- Don't use Inter (or any sans) for display headlines — the serif
  character is the brand voice.
- Don't repeat the same surface mode in two consecutive bands; the pacing
  alternates cream → cream-card → dark-mockup → cream → coral-callout →
  dark-footer.
- Don't add hover styling beyond what the system already encodes — primary
  darkens on press, nothing else changes.

## Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Mobile | < 768px | hamburger nav; hero h1 64→32px; hero-illustration-card stacks below content; feature grids 1-up; connector tiles 2-up; pricing 1-up; footer 4 cols → 1 |
| Tablet | 768–1024px | top nav stays horizontal but tightens; feature cards 2-up; connector tiles 3-up; pricing 2-up |
| Desktop | 1024–1440px | full top-nav; 3-up feature cards; 4-up or 6-up connector tiles; 3-up pricing tiers |
| Wide | > 1440px | same as desktop with more outer breathing room; max content caps at 1200px |

Touch targets: `button-primary` is minimum 40×40px; `button-icon-circular`
is exactly 36×36 (under WCAG's 44 but visually centered); `text-input`
height is 40px; connector tiles are entirely tappable, well over 44px.
Top nav collapses to a hamburger sheet below 768px; the hero's 6/6 grid
collapses to single column (headline first, illustration/mockup below);
feature grids reduce columns rather than shrinking cards; pricing tiers
collapse 4→2→1 while the featured dark tier stays visually distinct;
code-window cards retain legibility by allowing horizontal scroll rather
than wrapping code lines; hero illustrations scale proportionally with
line-art strokes thinning slightly on mobile; testimonial avatar photos
crop to circles at every breakpoint.

## Known gaps

- Copernicus and StyreneB are licensed Anthropic typefaces and not
  available as public web fonts; substitutes (Tiempos Headline / Cormorant
  Garamond / EB Garamond for serif, Inter / Söhne for sans) are documented
  under Typography.
- The Anthropic radial-spike-mark is rendered as an inline SVG brand glyph
  and isn't formalized as a system token here — treat it as a logo asset.
- Animation and transition timing (chat message reveal, homepage code-block
  typewriter effect, agentic-flow diagram animation) is out of scope.
- Form validation states beyond the focused text-input weren't extracted —
  error/success states would need a sign-up or feedback flow to confirm.
- The actual Claude product surface (claude.ai chat interface) shares some
  tokens with the marketing site but adds many product-specific components
  (chat bubbles, message tools, file-upload chips, conversation-history
  sidebar) that are out of scope for this marketing-surface document.
- The "agent"/"computer use" demo cards on some pages display animated
  Claude controlling a browser; the static screenshot doesn't fully capture
  that animation chrome.
