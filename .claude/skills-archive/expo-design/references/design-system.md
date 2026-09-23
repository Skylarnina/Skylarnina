# Expo Design System — Full Analysis

Adapted from the Expo design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/expo/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Expo's marketing site reads like a quietly confident React Native
developer platform. The base canvas is pure white (`colors.canvas` —
`#ffffff`) with a soft sky-blue gradient atmospheric wash behind the hero
band only. Near-black ink (`colors.ink` — `#171717`) carries body and
display alike. The single brand voltage is pure black (`colors.primary` —
`#000000`) for primary CTAs — minimal and editorial-feeling. A small blue
text-link accent (`colors.text-link` — `#0d74ce`) is reserved for inline
body links, never a CTA.

Type runs Inter as the single sans family at modest weights (display 600,
body 400). JetBrains Mono carries every code surface. There's no custom
typeface — the brand trusts Inter's editorial neutrality to do the work.

The brand's strongest visual signature is the device-mockup hero — a
centered MacBook plus iPhone composite showing real Expo dev surfaces
(Expo Studio, the EAS Build dashboard, the Expo Go simulator) — set over a
sky-blue gradient atmospheric wash. That composite is the page's chrome in
place of an illustration.

**Key characteristics:**
- Pure white canvas with a sky-blue gradient atmospheric backdrop confined
  to the hero only.
- A single primary CTA: a pure black pill... actually rectangle, at
  `rounded.md` (8px) — a compact developer-tool dialect, not a pill.
- Text-link blue for inline links only — never on a CTA.
- Inter as the single sans family, with no custom display typeface.
- JetBrains Mono on every code surface.
- A device-mockup hero with real Expo product surfaces functions as the
  brand chrome.
- Hairline-plus-soft-drop depth; no atmospheric brand decoration outside
  the hero.
- A 96px section rhythm.

## Colors

### Brand & accent
- **Black** (`#000000`) — the primary CTA fill, used scarcely.
- **Black Active** (`#1a1a1a`) — the press state.
- **Text Link Blue** (`#0d74ce`) — inline body links inside long-form
  copy, scoped narrowly and never used on CTAs.
- **Legal Link Blue** (`#476cff`) — inline links inside legal/footer copy.
- **Bright Cyan** (`#47c2ff`) — used very sparingly inside docs-widget
  links.

### Surface
- **Canvas** (`#ffffff`) — the pure white page floor.
- **Canvas Soft** (`#fafafa`) — a subtle alternating band.
- **Surface Card** (`#ffffff`) — the pure white card surface.
- **Surface Strong** (`#f0f0f3`) — badges, ecosystem tiles, secondary
  buttons.
- **Surface Dark** (`#171717`) — dark feature cards, code blocks, IDE
  mockups, featured pricing.
- **Surface Dark Elevated** (`#1a1a1a`) — one step lighter inside dark
  cards.

### Atmospheric backdrop
- **Sky Light** (`#cfe7ff`) and **Sky Mid** (`#a8c8e8`) — the soft
  sky-blue gradient wash behind the homepage hero only. This is not a
  brand action color.

### Hairlines
- **Hairline** (`#f0f0f3`) — the default 1px divider.
- **Hairline Soft** (`#f5f5f7`) — a lighter divider.
- **Hairline Strong** (`#dcdee0`) — a stronger panel outline.

### Text
- **Ink** (`#171717`) — display and body emphasis.
- **Body** (`#60646c`) — default running text, a slightly cool gray.
- **Body Strong** (`#171717`) — the same value as ink.
- **Muted** (`#999999`) — sub-titles.
- **Muted Soft** (`#cccccc`) — disabled text.
- **On Primary** (`#ffffff`) — white text on the black CTA.
- **On Dark** (`#ffffff`) — white text on dark cards.
- **On Dark Soft** (`#b0b4ba`) — muted off-white on dark surfaces.

### Semantic
- **Warning** (`#ab6400`) — warning text inside docs callouts.
- **Preview** (`#8145b5`) — the "Preview" tag color.
- **Success** (`#16a34a`) — confirmation states.
- **Error** (`#eb8e90`) — validation errors.

## Typography

### Font family
Inter is the single sans family across every text role; JetBrains Mono
carries every code surface. Fallback: `-apple-system, system-ui,
sans-serif`.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale. Key entries:
`display-mega` (64/600, -1.92px tracking, homepage hero h1), `display-xl`
(48/600, -1.44px, subsidiary heroes), `display-lg` (36/600, -1.08px,
section heads), `display-md` (28/600, -0.84px, sub-section heads),
`display-sm` (22/600, -0.5px, card group titles), `title-md` (18/600,
component titles), `body-md` (16/400, default body), `code` (13/400,
JetBrains Mono), `button` (14/500, CTA labels).

### Principles
Display weight stays fixed at 600 — confident but not bombastic, since
Inter at 600 reads cleaner than 700. Negative letter-spacing runs from
-0.5px up to -1.92px on the largest display sizes. JetBrains Mono is used
on every code surface without exception.

### Font substitutes
Inter and JetBrains Mono are both freely available — the system uses them
directly, with no licensing substitution needed.

## Layout

- **Base unit:** 4px. Full scale: `xxs` 4px, `xs` 8px, `sm` 12px, `base`
  16px, `md` 20px, `lg` 24px, `xl` 32px, `xxl` 48px, `section` 96px.
- **Section padding:** 96px.
- **Max content width:** roughly 1200px.
- **Grid:** a 12-column editorial-body grid; feature card grids run 2-up
  at desktop for hero splits and 3-up for benefit grids; the ecosystem
  tile grid runs 8-up at desktop; the footer runs 5-column at desktop.
- **Whitespace philosophy:** generous editorial pacing. The white canvas
  doesn't compete with the hero's gradient sky wash; cards inside dense
  workflow sections sit close together (16-24px gap).

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| Flat (canvas) | `canvas` (#ffffff) | body bands, footer |
| Card | `surface-card` (#ffffff) | content cards |
| Hairline border | 1px `hairline` | card outlines |
| Soft drop | `0 4px 12px rgba(0,0,0,0.04)` | hovered cards, the system's single shadow tier |
| Atmospheric gradient | sky-blue radial wash | hero backdrop only |
| Dark inversion | `surface-dark` (#171717) | dark feature cards, code blocks, featured pricing |

The sky-blue gradient backdrop appears only in the hero — atmospheric
depth without claiming to be a brand color. The device-mockup composite
(MacBook plus iPhone showing real Expo dev surfaces) functions as page
chrome and is the system's other major decorative-depth element.

## Shapes

| Token | Value | Use |
|---|---|---|
| `rounded.none` | 0px | reserved, effectively unused |
| `rounded.xs` | 4px | inline tags |
| `rounded.sm` | 6px | compact rows |
| `rounded.md` | 8px | CTA buttons, form inputs, ecosystem tiles |
| `rounded.lg` | 12px | feature cards, code blocks, pricing tiers |
| `rounded.xl` | 16px | device-mockup cards |
| `rounded.xxl` | 24px | larger atmospheric cards, rare |
| `rounded.pill` | 9999px | badges only |
| `rounded.full` | 9999px | avatar plates, rare |

The radii are compact and developer-ergonomic — 8px CTAs, 12px cards. Pill
geometry is reserved strictly for badges and never appears on a CTA.

## Components

Definitions live in `design-tokens.yaml → components`. Summary:
- **top-nav** — white 64px bar; Expo wordmark left, a primary menu (Tools
  / Workflows / EAS / Pricing / Docs / Showcase), Sign In plus a "Get
  started" CTA on the right.
- **Buttons** — `button-primary` (pure black, 8px radius, 40px height, a
  press state that darkens to `#1a1a1a`), `button-secondary` (white with a
  1px hairline-strong border), `button-tertiary-text` (inline blue text
  link).
- **Hero & device mockup** — `hero-band` (canvas background with a soft
  sky-blue gradient wash behind a centered `display-mega` headline,
  subhead, and single CTA, with the device mockup below),
  `device-mockup-card` (a layered MacBook plus iPhone composite at 16px
  radius — the MacBook shows the EAS dashboard or Expo Studio, the iPhone
  overlay shows the running app in Expo Go — the page's central chrome).
- **Cards** — `feature-card` (white, 12px radius, 24px padding, hairline-
  strong border), `feature-card-dark` (dark inversion of the same shape),
  `workflow-step-card` (a step row with a 32px square icon plate, step
  number, label, and body), `workflow-step-icon` (32px square plate on
  `surface-strong`), `testimonial-card` (quote card, 24px padding).
- **Code & IDE** — `code-block` (dark background, white JetBrains Mono
  text, 12px radius, 20px padding), `ide-mockup-card` (a stylized
  multi-pane editor plus terminal preview on the dark surface).
- **Pricing** — `pricing-tier-card` (white, hairline-strong border, 32px
  padding), `pricing-tier-featured` (dark inversion, same shape).
- **Ecosystem** — `ecosystem-tile` (a 64px square logo plate for partner
  logos like TypeScript, React, Sentry, with a 1px hairline border).
- **Forms & tags** — `text-input` (white, 8px radius, 44px height, 1px
  hairline-strong border that thickens to 2px ink on focus), `badge-pill`
  (surface-strong fill, uppercase caption type, full pill radius).
- **CTA / footer** — `cta-band` (canvas background, centered `display-lg`
  headline, a single black CTA, 96px padding), `footer-light` (white,
  5-column link list, 64×48px padding), `footer-link` (plain text link in
  the body color).

## Do's and don'ts

**Do**
- Reserve black for primary CTAs.
- Use the text-link blue for inline body links only — never on CTAs or
  buttons.
- Set every CTA at `rounded.md` (8px) — the developer dialect.
- Use Inter at weight 600 for display, 400 for body.
- Render every code surface in JetBrains Mono.
- Pair the hero with the device-mockup composite — it's the page's chrome.

**Don't**
- Don't introduce a saturated brand action color; black is the only CTA
  fill.
- Don't use the text-link blue on a CTA — inline links only.
- Don't drop display below weight 600 or push it above 700.
- Don't use full pills on CTAs — pills are for badges only.
- Don't replicate the sky-blue gradient backdrop outside the hero.
- Don't extract a CTA color from a third-party widget (cookie consent,
  OneTrust) — the brand's CTA color is only what appears on actual page
  CTAs.

## Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Mobile | < 640px | hero h1 scales 64→32px; device mockup collapses to a single iPhone screen; feature grid 1-up; nav becomes a hamburger |
| Tablet | 640–1024px | hero h1 at 48px; device mockup compresses; feature grid 2-up |
| Desktop | 1024–1280px | full hero h1 at 64px; full MacBook plus iPhone composite; feature grid 3-up |
| Wide | > 1280px | content caps at 1200px |

Touch targets: the primary CTA sits at 40px height (WCAG AA, padded toward
AAA); the search input is 44px (AAA). Collapsing strategy: top nav
switches to a hamburger below 768px; the device-mockup composite collapses
from MacBook-plus-iPhone to a single iPhone preview on mobile; the feature
grid steps 3-up → 2-up → 1-up; the ecosystem tile grid steps 8-up → 4-up →
3-up → 2-up.

## Known gaps

- Inter and JetBrains Mono are freely available — no licensing concerns.
- Animation timings (device-mockup parallax, hero entrance) are out of
  scope.
- In-app surfaces (the interactive EAS dashboard, the Expo Go simulator)
  are only partially captured via marketing mockups.
- Form validation states beyond the focus state aren't visible on the
  captured surfaces.
