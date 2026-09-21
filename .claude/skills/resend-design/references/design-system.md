# Resend Design System — Full Analysis

Adapted from the Resend design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/resend/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Resend presents as a developer tool with an editorial's typography. Every
page opens on `{colors.canvas}` (`#000000`), and the loudest element on
that canvas isn't a button or a logo mark — it's a 96px Domaine Display
serif headline ("Email for developers") with the `ss01/ss04/ss11`
stylistic alternates switched on. That single typographic choice sets the
brand's tone: confident, considered, slightly literary, and priced on
quality rather than novelty.

The supporting type is technical. Marketing prose runs in **ABC Favorit**,
UI labels run in **Inter**, and code renders in **Geist Mono** inside
`code-window` shells with hairline traffic-light dots. Depth is built
almost entirely from translucent white — 6% hairline borders, 14% strong
borders, 4% dividers — layered over a `surface-deep` tone that sits just
below canvas black. There are no full-band gradients, only soft
**atmospheric glows** (orange, blue, green, red, yellow) anchored at the
top of select sections, all at low opacity.

Page rhythm stays in a single dark register throughout: hero stripe →
atmospheric section → code-window section → email-mockup section →
pricing/feature grid → black footer. The brand never shifts to a light
surface; even the email mockups appear as compact white cards inside the
black canvas, framed like print insets in a black-bordered magazine page.

**Key characteristics:**
- True black canvas on every public page; off-white text carries the
  entire read.
- Serif-led four-family stack: Domaine Display for hero, ABC Favorit for
  body, Inter for UI, Geist Mono for code.
- Six accent glow colors used only as low-opacity atmospheric washes —
  never as buttons or solid surfaces.
- Strict container vocabulary: 12px for feature cards/code wells/email
  mockups, 8px for buttons, full-round for pills and avatars.
- Translucent-white borders replace shadows entirely — no traditional
  drop-shadow elevation language exists.
- The primary button is a small white rectangle with black text — the
  counterintuitive brightest pixel on the page, used as a single visual
  anchor.

## Colors

### Brand & accent
- **Primary White** — the brand's de facto accent; reserved for the
  primary button (white pill on black), the Domaine display headlines, and
  active text. White is the loudest color on this canvas, and that's the
  point.
- **Primary On** — black label text on white pill surfaces.
- **Surface Light** — a subtle blue-tinted off-white used as the
  pressed/active state of the primary button.

### Surface
- **Canvas** — true black, never near-black.
- **Surface Card** — the standard inset card surface, one step lighter
  than canvas.
- **Surface Elevated** — a second elevation step for featured pricing tiers
  and ghost-button surfaces.
- **Surface Deep** — the code-window background, cooler and darker than
  canvas, suggesting depth through temperature rather than lightness.
- **Hairline / Hairline Strong** — the soft and structural translucent-
  white 1px borders used across cards, code wells, and inputs.
- **Divider Soft** — the low-contrast divider between footer columns.

### Text
- **Ink** — primary text, faintly blue-cool so it reads like printed paper
  rather than pure-white glare.
- **Body / Charcoal / Mute / Ash / Stone** — a descending scale from
  long-form body copy down to disabled foreground.
- **On-Light / On-Light Mute** — the label colors used inside the rare
  white email-mockup cards.

### Semantic
- **Accent Orange + Glow** — atmospheric warm wash anchored to
  "reimagined"/customer-story sections; solid orange never appears as a
  button or surface, only as glow.
- **Accent Yellow** — inline highlight strokes and "developer experience"
  callouts.
- **Accent Blue + Glow** — inline link color and the cool atmospheric wash
  on the "integrate this weekend" section.
- **Accent Green + Glow** — success status dots and the "delivery
  confirmed" feature glow.
- **Accent Red + Glow** — inline error red and the "reach humans, not spam
  folders" attention wash.
- **Link** — the same value as accent blue.

## Typography

### Families
- **Domaine Display** — proprietary editorial serif used exclusively for
  hero headlines at 76px+, with `ss01/ss04/ss11` stylistic sets engaged for
  a tighter, print-magazine look.
- **ABC Favorit** — proprietary humanist sans for marketing body copy, hero
  subtitles, and pill labels, carrying `ss01/ss03/ss04` features for
  tabular figures and alternate glyphs.
- **Inter** — open-source sans for UI: button labels, captions, card body
  text, nav links.
- **Geist Mono** — open-source monospace for code wells.

When the proprietary families aren't available, **Söhne** or **Tiempos
Headline** stand in for Domaine Display, and **Geist** or **Inter Tight**
can replace ABC Favorit. Inter and Geist Mono are already open-source.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale (display-xxl 96px
down to code-md 13px). Principles:
- Display sizes always hold `lineHeight: 1.0` with negative letter-spacing
  so the Domaine Display headlines pack into solid typographic blocks
  rather than open prose lines.
- Body weight stays at 400 across both body sizes — the serif/sans family
  change carries hierarchy, not weight bumps.
- ABC Favorit always runs with `ss01/ss04/ss11` engaged; Inter never
  carries OpenType features; code in Geist Mono never carries ligatures.
- Inline links use the ABC Favorit `button-sm` role with positive
  letter-spacing (0.35px) — the small spacing nudge gives interactive prose
  its precision.

### Note on font substitutes
When Domaine Display is unavailable, clamp `lineHeight` to 1.0 explicitly
and apply `font-feature-settings: "ss01", "liga"` on the substitute serif
to mimic the alternate glyphs — Söhne or Tiempos Headline read closest. ABC
Favorit substitutes (Geist, Inter Tight) typically default to looser
tracking, so apply roughly -0.5% letter-spacing on body sizes to
compensate.

## Layout

- Base spacing unit: 4px; full scale in `design-tokens.yaml → spacing`.
- Section padding: 96px vertical between bands, 128px on the hero stripe
  and the closing footer transition.
- Card interior padding: 32px on feature cards, pricing tiers, and code
  windows.
- Max content width ≈ 1200px on body sections.
- Feature grid: 3 columns desktop → 2 tablet → 1 mobile.
- Pricing: 3-tier grid, centered; the featured tier promotes to a
  one-step-elevated surface rather than a colored border.
- Code-story splits: narrative copy left, code window right, collapsing to
  stacked below 1024px.
- The email-mockup band centers a single white card (640px max width) with
  generous vertical padding, reading like a print-magazine inset.
- Whitespace is editorial and generous (96-128px between sections) so
  Domaine Display headlines have room to register at scale; card padding
  holds steady at 32px. Hairline borders carry the role drop shadows would
  play in a brighter system — the dark canvas suppresses traditional
  shadow depth almost entirely.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 flat | no shadow/border | default canvas, full-bleed bands |
| 1 surface card | surface-card + hairline-strong border | feature cards, pricing tiers, form inputs |
| 2 elevated | surface-elevated + hairline-strong border | featured pricing tier, ghost button |
| 3 code well | surface-deep + hairline-strong border | code window, terminal shells |
| 4 atmospheric glow | low-opacity radial gradient anchored at section top | section openers |

There is no traditional drop-shadow language — every surface either gets a
translucent-white hairline border or sits inside an atmospheric glow. The
canvas absorbs shadow naturally; depth registers through temperature and
luminance shifts instead of blur.

**Decorative depth:** six accent colors each pair with a glow token
(orange, yellow, blue, green, red, plus a deep slate variant). Each section
opens with a single radial wash anchored at its top edge, falling off to
black within roughly 600px — never two glows in the same section. The
"beyond experience" email-mockup band lifts a single white card off the
black canvas for the system's only true light-on-dark contrast, with no
shadow — the contrast itself is the elevation. Code-window shells include a
row of three colored traffic-light dots (red/yellow/green) — the only place
all three semantic colors appear together as solid surfaces.

## Shapes

| Token | Value | Use |
|---|---|---|
| rounded.none | 0px | hero stripe, full-bleed bands, footer |
| rounded.xs | 4px | inline tags inside code wells |
| rounded.sm | 6px | code tabs, mid-size chips |
| rounded.md | 8px | buttons, form inputs |
| rounded.lg | 12px | feature cards, pricing tiers, code wells, email mockups |
| rounded.xl | 16px | larger feature panels |
| rounded.full | 9999px | pills, status dots, contributor avatars |

The system uses almost no photography — visual interest comes from
typography, atmospheric glows, code wells, and the white email-card
insets. Where portraits appear (testimonial avatars), they're circular at
32px, inline with body copy. Email mockup cards run at a 4:5 portrait
aspect with `rounded.lg` corners.

## Components

Definitions live in `design-tokens.yaml → components`. Summary:
- **Buttons** — primary (white pill, the brightest pixel), ghost
  (translucent secondary), and outline (tertiary, canvas-colored).
- **Cards** — hero-stripe (full-bleed hero band), feature-card /
  feature-card-bordered, pricing-tier / pricing-tier-featured, code-window
  with a code-tab language switcher, and email-mockup.
- **Inputs** — a single text-input whose focus state thickens the border
  rather than introducing a new ring color.
- **Navigation** — a 64px nav bar (wordmark left, nav center, sign-in +
  primary CTA right) and horizontally-scrolling sub-nav pills.
- **Signature** — badge-pill (neutral inline tags), status-dot (8px green
  indicator), contributor-avatar, and a multi-column footer.

## Do's and don'ts

**Do**
- Use true black as the default page background on every public page.
- Reserve the white primary button as the only solid bright surface — one
  per viewport at most.
- Set hero headlines in Domaine Display at 76-96px with `lineHeight: 1.0`
  and the stylistic-set features engaged.
- Keep ABC Favorit for marketing body, Inter for UI labels, Geist Mono for
  code — strict lanes.
- Build elevation from translucent-white hairlines, not drop shadows.
- Use the accent-glow tokens only as low-opacity radial atmospheric washes.
- Use the white email-mockup inset sparingly — it should feel like a print
  pull-quote, not a recurring pattern.

**Don't**
- Don't use a near-black canvas — the brand sits on true `#000000`.
- Don't apply solid color to atmospheric accent tokens; their glow form is
  for backdrops only.
- Don't add drop shadows to feature cards or code wells.
- Don't bump body weight to 600 for emphasis — use family change instead.
- Don't render code outside the code-window component, even inline.
- Don't loosen Domaine Display `lineHeight` past 1.0.
- Don't introduce a second brand accent — white is the brand on black;
  everything else is atmospheric.
- Don't bring photography front-and-center; the brand reads as type-and-
  code, not photography-led.

## Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Desktop XL | ≥1440px | full 1200 body max-width, 3-up feature grid, side-by-side code-story splits |
| Desktop | 1280-1439px | container shrinks, larger side padding |
| Tablet Large | 1024-1279px | feature grid stays 3-up, code-story stays 2-up |
| Tablet | 768-1023px | feature grid 2-up, code-story stacks, pricing stacks vertically |
| Mobile Large | 426-767px | feature grid 1-up, nav collapses to hamburger, hero clamps to 56px |
| Mobile | ≤425px | all grids 1-up, hero clamps to 44px, section padding collapses to 64px |

Touch targets: buttons ship at a minimum 36px tall on desktop, scaling to
44px on mobile via padding — WCAG AAA on mobile. The text input (40px)
scales to 48px on mobile. Sub-nav pills stay 36px desktop, 40px mobile.

Collapsing strategy: nav collapses to hamburger below 1024px; hero display
clamps 96px → 76px → 56px → 44px across the ladder; the 3-up pricing grid
stacks below 1024px with the featured tier staying centered; code-story
splits switch to stacked below 1024px with the code well always second;
atmospheric glows scale with section width but keep the same opacity.

Image behavior: email-mockup cards reflow to 1:1 aspect on mobile to stay
readable. Atmospheric glows are CSS gradients with no asset cost or
breakpoint variation. Testimonial avatars stay 32px circular at every
breakpoint.

## Known gaps

- Pressed/active states are documented only for the primary button; other
  components rely on the browser's default focus ring for feedback.
- Logged-in dashboard surfaces (API keys, sending logs, audience
  management) are out of scope — only the public marketing canvas is
  documented.
- The email-template editor, a key product feature, isn't extracted since
  it lives behind authentication.
- Atmospheric glow rendering uses CSS radial gradients whose exact stops
  and angles vary per section and aren't standardized as tokens — render
  each per section-specific judgment.
