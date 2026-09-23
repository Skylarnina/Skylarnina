Adapted from the Ollama design analysis in [voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md) (`design-md/ollama/DESIGN.md`, MIT License). Token names below refer to `references/design-tokens.yaml` in this skill.

## Overview

Ollama's site is the most aggressively under-designed marketing surface in
the AI tooling space, and that is entirely the point. The home page reads
like a Markdown README rendered with care: a 36px center-aligned heading
sits above an inline `curl` install snippet in a soft-gray pill, a single
black "Download" CTA, and a hand-drawn llama mascot as the only ornament.
Everything else — an "automate your work" block, the "Start local. Scale
cloud." pricing pair, a "Your data stays yours" guarantee strip, and the
FAQ wall on `/pricing` — sits on the same paper-white canvas with quiet
`colors.body` neutrals carrying the prose. The system is the
documentation, and the documentation is the system.

The design philosophy is geometric: every interactive element collapses to
`rounded.full` (9999px) — buttons, search pills, install-snippet pills,
text inputs, even the terminal traffic-light dots. There are no decorative
drop shadows, no gradients, no hero illustrations beyond the llama. The
rare card (on `/pricing`) uses a soft `rounded.lg` (12px) with a 1px
hairline. The single inverted moment in the whole system is the dark "Max"
pricing tier — `colors.surface-dark` with white text — the only
attention-grabbing surface in an otherwise studiously flat layout.

Typography pairs `SF Pro Rounded` (display headings, weight 500–600) with
the operating system's default sans (`ui-sans-serif`) for body and
`ui-monospace` for code. The roundness of the heading face is the only
"personality" the chrome carries — it gently echoes the pill-button
geometry without ever becoming decorative.

**Key characteristics:**
- Paper-white canvas end-to-end with no surface alternation — the whole
  page is one continuous sheet.
- A center-aligned hero with a 36px SF Pro Rounded headline, no eyebrow, no
  subhead beyond a small tagline under the llama.
- Pill geometry everywhere — every button and pill input is `rounded.full`;
  cards use `rounded.lg`; nothing else is rounded except section dividers.
- A single-color CTA system — pure black pills carry every action; "Get
  Pro" and "Get Max" inside pricing cards are the only variation.
- An inline `curl` install snippet rendered as a pill with `code-md`
  typography — the site's most signature element, sitting directly under
  the hero headline.
- A terminal-mockup card with macOS traffic-light dots and an inline
  `ollama launch openclaw` example — the home page's only "product preview."
- An inverted dark pricing card for the highest-tier "Max" plan, breaking
  the flat-white rhythm exactly once per page.

## Colors

> Source pages: `/` (home) and `/pricing`. The chrome palette is identical
> across both — only content changes.

### Brand & accent
- **Pure Black** (`primary`) — the brand, full stop. Every primary CTA,
  every black pill, every nav link, every solid icon. There is no other
  "brand color."
- **Ink Deep** (`ink-deep`) — the pressed-state black for the primary
  pill, a single notch below pure black.

### Surface
- **Canvas** — the page itself, used for nearly every surface in the
  system.
- **Soft Surface** — the install-snippet pill background, search pill,
  secondary chip backgrounds, and occasional alternating row fill.
- **Surface Dark** — the dark "Max" pricing card and dark CTA strips; the
  single inverted surface in the system.
- **Hairline / Hairline Strong** — the 1px card border, divider above the
  footer, divider between FAQ rows, with a slightly stronger variant for
  extra separation between unrelated FAQ groups.

### Text
- **Ink** — all headlines, primary nav links, button text on light
  surfaces, prices on pricing cards.
- **Charcoal** — list-item text and disabled-state secondary copy.
- **Body** — the default paragraph color, used for FAQ answers and footer
  link text — the system's most-used text color after pure black.
- **Mute** — caption text, command-line "comment" gray inside terminal
  mockups, the lowest-emphasis utility text.
- **On Dark / On Dark Mute** — primary and secondary text on
  `surface-dark`.

### Semantic
The system has effectively no error/success/warning palette on its public
marketing surfaces — no validation states, no destructive flows, no
banners. The only "semantic" colors are the macOS-style terminal traffic
lights inside the terminal mockup: **Terminal Red** (close-window dot),
**Terminal Yellow** (minimize dot), and **Terminal Green** (zoom dot).
These appear only inside `terminal-card` and have no other use.

### Focus
- **Focus Ring** — a translucent blue browser-default focus ring around
  interactive elements; the only blue anywhere in the system.

## Typography

### Font family
**SF Pro Rounded** (display headings) — Apple's rounded geometric sans,
used at weights 500 and 600 for headlines from `display-xl` (36px) down to
`heading-lg` (24px), falling back to `system-ui` → `-apple-system`.
**ui-sans-serif** (body, links, buttons, captions) — the operating
system's default sans-serif, carrying every non-display text role at
12–20px, falling back through `system-ui` and platform emoji families.
**ui-monospace** (code, install snippet, command tags) — the OS default
monospace, used inside the terminal mockup, the inline `curl` install
pill, and inline `<code>` formatting, falling back to SFMono-Regular →
Menlo → Monaco → Consolas.

The pairing of SF Pro Rounded display + system sans body + system mono
code is intentionally "stock Apple" — the design decision is to not have a
typography decision. A branded display face would compete with the
system's documentation feel.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale (36px hero
headline down to a 12px copyright row). The typography is built for
legibility at small sizes on a flat-white canvas — SF Pro Rounded's
softened terminals on the heading face do almost all of the brand
expression, and everything below 20px collapses into the operating
system's default sans, rendering the way docs.ollama.com and the Ollama
CLI's own help text would appear in a terminal. There is almost no
letter-spacing variation, no display-only weight, no italic, and the
heading-to-body ratio compresses tightly (36 → 30 → 24 → 20 → 16) so the
page reads as a single readable column rather than a marketing pyramid.

### Note on font substitutes
`SF Pro Rounded` is Apple-licensed and ships only on macOS/iOS; elsewhere
it falls back to `system-ui` (Segoe UI / Roboto / DejaVu Sans depending on
platform) — Ollama explicitly accepts that the heading face will look
slightly different off-Apple. The closest open-source substitute is
**Nunito** (rounded geometric sans, weights 500/600). For the body face,
**Inter** is a near-perfect match for `system-ui` rendered metrics. For
code, **JetBrains Mono** or **Fira Code** are the canonical open-source
substitutes for `ui-monospace`.

## Layout

### Spacing system
Base unit 8px, with finer 2/4/6px steps for tight inline gaps:
`spacing.xxs` (2px) · `spacing.xs` (4px) · `spacing.sm` (8px) ·
`spacing.md` (12px) · `spacing.lg` (16px) · `spacing.xl` (24px) ·
`spacing.xxl` (32px) · `spacing.section` (88px). Every page uses
`spacing.section` (88px) — the single largest spacing token in the system —
as the vertical gap between major content blocks (hero → automate → start
local/scale cloud → your data stays yours → get-started footer call).
Pricing cards sit at 32px padding all around; FAQ rows use 16px vertical
padding with no horizontal padding.

### Grid & container
The home page lays out as a single narrow ~720px reading column, with
optional 2-column splits inside specific sections. The pricing grid runs
3-up at desktop within a ~960px max content width, collapsing to 1-up below
768px. The "automate your work" section splits 50/50 (left text, right
terminal mockup) at desktop, stacking vertically with the terminal below
the text on mobile. The FAQ is a single-column stack full-width within the
720px content column, and the footer is a single row of small links,
center-aligned at desktop and wrapping to two rows on narrow screens.

### Whitespace philosophy
Whitespace is the entire layout. Sections are separated by 88px of plain
white air — never by decorative dividers, never by colored bands. Inside a
section, content sits in a tight reading column with no decorative
columns, callout boxes, or lifted cards. The site treats the page as a
long-form Markdown document, and the air between sections functions like a
blank line in Markdown source.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 — Flat | no border, no shadow | hero, automate-your-work, your-data-stays-yours, footer — the dominant treatment |
| 1 — Hairline border | 1px solid hairline | pricing cards, FAQ row dividers, terminal mockup card |
| 2 — Inverted dark | `surface-dark` fill | the dark "Max" pricing card and dark CTA strip — the system's only "elevated" surfaces use color, not shadow |

There is no drop-shadow elevation at all. Nothing lifts, nothing floats,
nothing layers. The only depth cue beyond hairline borders is the single
dark surface used on the highest-tier pricing card to draw attention to
it.

### Decorative depth
The site has effectively zero decorative depth in the traditional sense.
"Depth" comes from two recurring devices: the hand-drawn llama mascot
(appearing once at the top of the hero, once atop each pricing card, and
once beside the lock icon in the "Your data stays yours" section — the
only illustration in the system), and a single line-drawn lock icon,
stroke-only with no fill, in the data-privacy section.

## Shapes

| Token | Value | Use |
|---|---|---|
| `rounded.none` | 0px | nav, footer, FAQ row dividers — flat structural lines |
| `rounded.sm` | 6px | inline code chips, command tags |
| `rounded.md` | 8px | rare medium-radius surfaces (e.g. dropdown panels) |
| `rounded.lg` | 12px | pricing cards, terminal mockup card |
| `rounded.full` | 9999px | every button, every pill input, install-snippet pill, search pill, traffic-light dots |

The dominant shape vocabulary is just two values: pills for everything
interactive and 12px for the few cards in the system. There are no
medium-radius "soft cards" — surfaces are either pills or rectangles with
corners large enough to read as deliberately soft.

### Photography geometry
There is no photography. The only image-like elements are the hand-drawn
llama mascot (~80–120px on the hero, ~32–48px as a pricing-card eyebrow
icon), the stroke-only lock icon in the privacy section, and three 12px
filled circles for the macOS traffic-light dots inside the terminal
mockup.

## Components

Definitions live in `design-tokens.yaml → components` (default and
active/pressed states only — hover states are not documented per system
policy):

- **`button-primary`** — the universal Ollama CTA: black background, white
  text, `button-md` type, 8px/20px padding, 36px height, `rounded.full`.
  Used for "Download" (top nav), "Sign in," "Create account," "Get Pro,"
  "Get Max" — every primary action. Pressed state (`button-primary-active`)
  drops to `ink-deep`.
- **`button-secondary`** — an outline alternative on light canvas (1px
  hairline-strong border), used as a secondary affordance — e.g. "Sign in"
  paired with the black "Download" pill.
- **`button-pill-on-dark`** — a white pill on the dark surface, the "Get
  Max" CTA inside the inverted pricing card; the inversion makes the dark
  card itself the visual anchor while the white pill reads as the CTA.
- **`button-disabled`** — flat soft-gray, `surface-soft` background with
  `mute` text.
- **`search-pill`/`search-pill-focused`** — centered in the primary nav
  with a magnifier icon prefix and "Search models" placeholder; focus
  flips the background to canvas and shows the browser-default focus
  ring.
- **`text-input`/`text-input-focused`** — 1px hairline border by default,
  gaining an ink border plus the browser-default focus ring when active.
- **`install-snippet`** — the signature install pill: soft-gray
  background, `code-md` type, 12px/20px padding, 48px height, containing
  the literal `curl -fsSL https://ollama.com/install.sh | sh` command with
  a small copy icon at the right edge — the page's most prominent "CTA."
- **`command-tag`** — a small inline command chip used for the `ollama
  launch openclaw` example and similar inline-command demos.
- **`terminal-card`** — the home page's only "product preview": a
  1px-hairline card with three traffic-light dots at the top-left and
  terminal output in `code-sm`, comments in `mute`, active commands in
  `ink`.
- **`pricing-card`** — the Free/Pro tiers: a small llama-mascot icon at
  top, tier name in `heading-md`, a one-line description, a large price in
  `display-lg`, a single `button-primary` CTA, a divider, a
  "Everything in Free, plus:" header, and a list of `feature-bullet` rows.
- **`pricing-card-dark`** — identical layout to `pricing-card` but with the
  `surface-dark` background, `on-dark` text, `on-dark-mute` secondary
  text, and `button-pill-on-dark` CTA — the system's single "look here"
  cue.
- **`feature-bullet`** — an inline checkmark plus `body-sm` text in
  `charcoal`, no background or border, stacked with an 8px gap.
- **`faq-row`** — question in `heading-sm`, answer in `body-md`/`body`
  directly below with a small gap; always expanded, no accordion collapse.
- **`cta-strip-dark`** — a rare dark CTA band, used sparingly between
  sections.
- **`link-inline`/`link-mute`** — underlined body-prose anchors, in `ink`
  and `body` respectively.

### Navigation
**`primary-nav`** (56px): a llama icon on the left, followed by
"Models · Docs · Pricing" text links, a centered search pill, and a right
cluster of "Sign in" plus the black `button-primary` "Download." On mobile,
the llama icon sits at left with a hamburger drawer trigger at right; the
search pill expands to full-width when triggered, and the drawer lists
"Models · Docs · Pricing · Sign in · Download" stacked with 16px row gaps.

### Footer
**`footer-section`** — a 1px top border above a single horizontal row of
small links ("Download · Blog · Docs · GitHub · Discord · X · Contact ·
Privacy · Terms") plus a copyright line at the right edge, wrapping to two
rows on narrow screens.

## Do's and don'ts

**Do**
- Treat the page like a Markdown document — a single reading column, 88px
  air between sections, no decorative dividers.
- Use `button-primary` (black pill) for every primary action — there is no
  green, no blue, no brand-tinted CTA.
- Default to `rounded.full` for any interactive element; cards get
  `rounded.lg` (12px), and that is the only exception.
- Use `display-xl` (SF Pro Rounded) for the hero headline and `body-md`
  (system sans) for everything else — avoid intermediate display sizes.
- Reserve `pricing-card-dark` (the inverted dark surface) for exactly one
  "look here" moment per page — never twice.
- Render install commands and CLI examples inside `install-snippet` or
  `terminal-card` with `code-md`/`code-sm` — code is a first-class
  component.
- Keep the llama mascot the only illustration in the system — it is the
  brand.

**Don't**
- Don't introduce gradients, drop shadows, or atmospheric backgrounds —
  the canvas is pure white.
- Don't add brand colors — the system is black on white with gray text,
  full stop.
- Don't soften pills or sharpen cards — pills stay `rounded.full`, cards
  stay `rounded.lg`; don't introduce `rounded.md` for buttons or
  `rounded.full` for cards.
- Don't lift cards with shadows — use a 1px hairline border or invert to
  `surface-dark`, the only two card treatments.
- Don't replace `ui-sans-serif` with a branded display body face — the
  system relies on `system-ui` rendering to feel native.
- Don't fill long-form pages with marketing chrome — FAQ answers stay in
  `body` prose with no decorative containers.

## Responsive behavior

### Breakpoints
| Name | Width | Key changes |
|---|---|---|
| desktop-large | 1280px+ | default desktop — 720px content column, 3-up pricing grid |
| desktop | 1024px | same layout; nav stays horizontal |
| tablet | 850px | pricing collapses from 3-up to 2-up + 1; nav search pill compresses |
| tablet-narrow | 768px | pricing collapses to 1-up stacked; primary nav becomes hamburger |
| mobile | 640px | hero headline drops from 36px to ~28px; install-snippet wraps; section padding tightens |

### Touch targets
All interactive elements meet WCAG AA at the 36–40px height range.
`button-primary` and `button-secondary` sit at 36px height with 20px
horizontal padding, giving an effective tappable area of ~36×80px that
exceeds the 44×44px AAA threshold via inline padding. `text-input` sits at
40px, `search-pill` at 36px with 16px padding. Footer links use 12px type
but receive enough vertical padding for a tappable row of ~32–36px.

### Collapsing strategy
The primary nav goes desktop horizontal → tablet-narrow hamburger drawer
at 768px; the black "Download" CTA stays visible at every width and never
collapses into the menu. The search pill goes from a fixed ~360px desktop
width → ~240px tablet → icon-only mobile with a full-width overlay on tap.
The pricing grid goes 3-up → 2+1 → 1-up stacked at 850, 768, and below,
with the dark "Max" card keeping its inverted treatment at every
breakpoint. The "automate your work" split goes desktop 50/50 → tablet
stacked, text above terminal mockup. The hero headline scales from 36px at
desktop to ~28px at mobile with line-height holding around 1.15, and
section spacing steps 88px desktop → 64px tablet → 48px mobile. The
install-snippet pill wraps the `curl` text to a second line on narrow
screens rather than truncating, with the copy icon staying anchored to the
right edge.

### Image behavior
The only image asset is the llama mascot (a raster PNG at multiple
resolutions: 16/32/48/64/180/192/512px). It renders at fixed pixel sizes on
the hero and pricing cards rather than scaling responsively — the brand
asset is treated like a logo, not a hero image.

## Known gaps

- Mobile screenshots were not captured — the responsive behavior above
  synthesizes Ollama's known mobile pattern (hamburger drawer, 1-up
  pricing stack, install-snippet wrap) from desktop evidence and the
  extracted breakpoint stack.
- Hover states are not documented by system policy.
- Form-field styling beyond search and the install-snippet is not present
  in the captured surfaces — there is no visible long-form form on the
  home or pricing pages.
- Authenticated chrome (account dropdown, billing settings, model
  dashboard) is not in the captured pages.
- The Models/Docs pages are not in the captured set — those surfaces
  likely add a sidebar and a docs typography tier not described here.
