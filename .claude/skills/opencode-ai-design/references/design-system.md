# OpenCode Design System — Full Analysis

Adapted from the OpenCode marketing-site design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/opencode.ai/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

OpenCode's whole marketing identity rests on a single typographic decision:
every piece of text on the site — the 38px hero headline, the 14px footer
copyright line, everything in between — is set in **Berkeley Mono**. There
is no sans-serif fallback, no display cut, no italic variant anywhere in the
chrome. The effect is that the page reads less like a SaaS landing page and
more like a `man` page or a README rendered at web resolution, complete
with bracketed `[+]` / `[-]` / `[x]` ASCII markers standing in for icons and
bullets, and a block-pixel ASCII wordmark at the top of the nav instead of a
vector logo.

The chrome itself is spare: a warm cream canvas (`colors.canvas`, `#fdfcfc`,
with a faint blush undertone) paired with nearly-black ink
(`colors.ink`, `#201d1d`) and a four-step neutral gray ladder for body copy,
metadata, and disabled text. Cards don't exist as raised surfaces here —
sections are simply hairline-bordered text blocks (`colors.hairline`, 1px)
sitting directly on the canvas, spaced apart by the system's largest token,
`spacing.section` (96px). The one deliberate visual flourish in the entire
system is a full-bleed dark hero card (`colors.surface-dark`, a near-black
that reuses the same hex as body ink) that mocks up the OpenCode terminal
interface itself — complete with `tab` / `ctrl-p` keybinding hints, a
"Build" command line, and the wordmark rendered as pixel-block ASCII art.

Oddly, the color token set ships the *entire* Apple Human Interface
Guidelines semantic ramp — Apple Blue (`colors.accent`, `#007aff`), red,
orange, and green, each with hover/active deepenings — even though the
marketing pages barely touch them; they mostly show up as syntax-highlight
stand-ins inside that one dark TUI mockup. The wider, brighter palette
belongs to the in-product terminal app, not the marketing chrome, which
stays resolutely monochrome.

**Key characteristics:**
- 100% Berkeley Mono typography across every text role, with no sans-serif
  fallback anywhere in the chrome.
- Warm cream canvas (#fdfcfc) is the only body background — no section
  ever switches to a gray or tinted band.
- A single dark surface (#201d1d) exists exclusively to host the hero TUI
  mockup — it never appears as a general section background.
- Every interactive element gets a uniform 4px radius; every structural
  container (nav, footer, hero card, rows) stays a sharp 0px rectangle.
- ASCII bracket markers (`[+]`, `[-]`, `[x]`) serve as the entire bullet and
  toggle iconography — there are no SVG icons.
- The OpenCode wordmark is always rendered as block-pixel ASCII art, never
  a vector logo, in both the nav and the hero mockup.
- Sections stack at a 96px rhythm with nothing but a 1px hairline rule
  between them — no decorative dividers of any kind.

## Colors

> **Source pages:** `/` (home), `/zen`, `/enterprise`. The chrome palette is
> identical across all three.

### Brand & accent
- **Ink** (`colors.primary` / `colors.ink`, `#201d1d`) doubles as the
  brand's only "color" — it carries headlines, body text, the primary CTA
  fill, nav links, and every solid icon glyph.
- **Ink Deep** (`colors.ink-deep`, `#0f0000`) is the pressed state for the
  primary button, carrying a faint red undertone that echoes the canvas's
  warm cast.
- **Cream** (`colors.canvas`, `#fdfcfc`) is the signature warm white used
  for every page body, every card surface, on-primary text, and the ASCII
  wordmark fill when it sits on the dark hero.

### Surface
- **Canvas Cream** (`#fdfcfc`) — every page body and card.
- **Soft Surface** (`colors.surface-soft`, `#f8f7f7`) — default text-input
  fill, testimonial-row fill, alternating row tint.
- **Surface Card** (`colors.surface-card`, `#f1eeee`) — the install-snippet
  pill, disabled-button fill, slightly-elevated section rows.
- **Surface Dark** (`colors.surface-dark`, `#201d1d`) — the hero TUI mockup
  background and the dark CTA pill on the home page; it's the same hex as
  ink, so the brand uses one near-black for both text and dark surfaces.
- **Surface Dark Elevated** (`colors.surface-dark-elevated`, `#302c2c`) —
  the prompt-row inside the hero TUI mockup, one notch lighter than the
  surrounding dark surface.
- **Hairline** (`rgba(15,0,0,0.12)`) — the 1px section divider, its
  translucent warm tint matching the cream canvas's undertone.
- **Hairline Strong** (`#646262`) — the tab strip's bottom rule and other
  stronger inline dividers.

### Text
- **Ink** (`#201d1d`) — headlines, body text, primary nav links, button
  text on light surfaces.
- **Charcoal** (`#302c2c`) — a subtly softer body tone where pure ink reads
  too heavy.
- **Body** (`#424245`) — default paragraph text and FAQ answers.
- **Mute** (`#646262`) — tab labels at rest, metadata, footer link text.
- **Stone** (`#6e6e73`) — the least-emphasis utility text and breadcrumb
  separators.
- **Ash** (`#9a9898`) — disabled text and secondary annotations inside the
  dark TUI mockup.

### Semantic
The full Apple HIG semantic ramp ships with the system, but on marketing
pages it appears almost exclusively inside the hero TUI mockup as
syntax-highlight stand-ins:
- **Accent** (`#007aff`, Apple Blue) — informational signal and TUI command
  highlight, with `accent-hover` (`#0056b3`) and `accent-active` (`#004085`)
  deepenings.
- **Danger** (`#ff3b30`) — destructive confirmation / error state, with
  `danger-hover` (`#d70015`) and `danger-active` (`#a50011`).
- **Warning** (`#ff9f0a`) — caution callouts, with `warning-hover`
  (`#cc7f08`) and `warning-active` (`#995f06`).
- **Success** (`#30d158`) — positive confirmation and in-TUI success
  indicators.

## Typography

### Font family
**Berkeley Mono** is the proprietary monospaced face used for every text
role, carrying weights 400/500/700 and falling back through a long
monospace stack (IBM Plex Mono → ui-monospace → SFMono-Regular → Menlo →
Monaco → Consolas → Liberation Mono → Courier New). The single-font
decision *is* the brand — there's no display face, no body sans, no italic,
and no proportional-font fallback anywhere, even in the legal copyright
line at 14px. It's the most aggressive typographic restraint in this
collection: OpenCode's identity is "the marketing page is a man page."

### Hierarchy
See `design-tokens.yaml → typography` for the full scale. The 38px/700 hero
headline and the 16px/700 section label share a weight — only size
distinguishes them. Body and inline links share size, weight, and
line-height, differentiated purely by context. Buttons get a deliberately
tall 2.0 line-height so labels feel calmly spaced inside their 4px-radius
rectangles.

### Font substitutes
Berkeley Mono is a paid commercial font. Open-source substitutes that
approximate its metrics within ~3% at body sizes: **JetBrains Mono**
(closest stroke contrast and x-height match), **IBM Plex Mono** (the
documented secondary fallback), and **Geist Mono** (a modern alternative
with similar geometric construction). Preserve `lineHeight: 1.5` for body
and `lineHeight: 2` for buttons when substituting.

## Layout

- **Base unit:** 8px, with finer 1/2/4px steps for tight inline gaps.
- **Universal section rhythm:** every page uses `spacing.section` (96px) —
  the largest token in the system — as the vertical gap between major
  blocks, the dominant layout cue across home, `/zen`, and `/enterprise`.
- **Section internal padding:** content rows sit at 16px vertical with no
  horizontal padding — text starts flush at the section's left edge.
- **Max width:** roughly 960px for body sections; the dark hero TUI mockup
  runs full-bleed within an outer ~1100px content frame.
- **Two-column split:** `/enterprise` pairs a ~360px text block on the left
  with a ~480px form column on the right; the home page stays single-column.
- **Footer:** a 5-up horizontal link row (GitHub / Docs / Changelog /
  Discord / X) that collapses to 2-up at tablet and 1-up at mobile.

Whitespace is structural and generous — 96px between sections with no
decorative dividers, just that single hairline rule. Content stays
left-flush with no indentation; bullets use ASCII bracket prefixes instead
of indent-based nesting. The result feels like a printed code listing
rather than a styled marketing layout.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 — Flat | No border, no shadow | Body sections, list rows, hero text, footer |
| 1 — Hairline rule | 1px `hairline` (translucent warm tint) | Section dividers |
| 2 — Hairline strong | 1px `hairline-strong` | Tab-strip bottom rule, emphasized in-list divider |
| 3 — Inverted dark | `surface-dark` fill | Hero TUI mockup, dark CTA pill |

There are no drop shadows anywhere in the system — nothing lifts, nothing
floats. The only thing that reads as "elevated" is the dark surface used
in the hero mockup, which registers through color contrast rather than
shadow.

Decorative depth comes from typography density and that one dark mockup:
the block-pixel ASCII wordmark, the hero TUI mockup itself (a faux
terminal with a command line and keybinding hints), and three thin-line
ASCII stat charts in the home page's stat block, each captioned in
`typography.caption-md` (e.g. "Fig 1. 150K GitHub Stars").

## Shapes

| Token | Value | Use |
|---|---|---|
| `rounded.none` | 0px | Sections, hero mockup, nav, footer, list rows — every non-button container |
| `rounded.sm` | 4px | Every interactive element — CTAs, inputs, install snippet, badges, prompt rows |
| `rounded.full` | 9999px | Avatar circles in testimonials |

The radius vocabulary is essentially two values: 4px for anything
interactive, 0px for everything else. Avatar circles are the system's only
fully-rounded element.

There's no photography in the system — visual elements are limited to the
ASCII wordmark, inline ASCII charts, small flat-color avatar dots (~32px)
in testimonial rows, and in-product icon glyphs (kbd, A+, ⊕, ↻) rendered as
small monospaced characters rather than bitmaps or SVGs.

## Components

Full specs live in `design-tokens.yaml → components`. Summary:

- **Buttons** — `button-primary` (ink fill, cream text, pressed state
  drops to `ink-deep`), `button-secondary` (outlined on canvas),
  `button-tab` / `button-tab-active` (the install-method tab strip:
  curl/npm/bun/brew/yay), `button-disabled`.
- **Badges** — `badge-news` (small dark chip for "News"/"Beta"/"Live now"
  tags), `badge-section-label` (a bare bolded heading line functioning as a
  section label, no chip background).
- **Inputs** — `text-input` / `text-input-focused` (focus flips border to
  solid ink, no halo), `textarea`, and the signature `install-snippet`
  code block holding the literal `curl -fsSL https://opencode.ai/install |
  bash` command.
- **Cards & containers** — `hero-tui-mockup` (the full-bleed dark TUI
  preview), `tui-prompt-row` (the inset command line inside it), `list-row`
  (feature rows led by ASCII bracket markers), `faq-row` (bracket-toggle
  FAQ entries), `testimonial-row` (avatar + quote), `chart-tile` (the
  sparse-line stat chart).
- **Navigation** — `primary-nav` (56px, ASCII wordmark left, Download CTA
  right) and a mobile hamburger-drawer variant.
- **Footer** — `footer-section` (5-column link grid, copyright + utility
  row beneath).
- **Inline** — `link-inline` (ink-colored, underlined — the brand's only
  link affordance; Apple Blue never appears on marketing links).

## Do's and don'ts

**Do**
- Render every text role in Berkeley Mono — the single-font decision is
  the entire identity.
- Keep the cream canvas as the only body background; never introduce gray
  section bands.
- Use ASCII bracket markers as bullets, toggles, and section glyphs — they
  are the brand's only iconography.
- Anchor the dark hero TUI mockup exactly once per landing page.
- Reserve the semantic accent ramp for in-TUI states; keep marketing chrome
  monochrome.
- Use 4px radius on every interactive element and 0px on every container.
- Stack sections at the 96px rhythm with only a 1px hairline between them.

**Don't**
- Don't introduce a sans-serif body font, a display face, or italics.
- Don't add drop shadows, gradients, or atmospheric backgrounds.
- Don't replace the ASCII bracket markers with SVG icons.
- Don't use the semantic accent ramp on marketing CTAs.
- Don't pad cards with 24px+ internal padding — list rows sit at 8px, FAQ
  rows at 12px.
- Don't render the wordmark as a vector logo — it's always block-pixel
  ASCII.
- Don't fill the hero TUI mockup with photography or illustration.

## Responsive behavior

| Name | Width | Key changes |
|---|---|---|
| desktop-large | 1280px+ | Default — 960px content column, 5-up footer grid |
| desktop | 1024px | Same layout, horizontal nav |
| tablet | 850px | Footer → 2-up; `/enterprise` two-column form stacks |
| tablet-narrow | 768px | Primary nav becomes a hamburger drawer |
| mobile | 640px | Single-column; hero display drops 38px → ~28px |

Touch targets sit comfortably at WCAG AA across the ~36-40px range for
buttons and inputs. The primary nav collapses to a hamburger drawer at
768px while the Download CTA stays visible at every width; the footer
steps 5-up → 2-up → 1-up; section padding tightens from 96px to 64px to
48px down the breakpoint stack. There are no raster images beyond the
favicon/OG share image — wordmarks, charts, and icons are all type or
inline SVG, so nothing needs responsive art-direction crops.

## Known gaps

- Mobile screenshots weren't captured — responsive behavior is synthesized
  from desktop evidence and the documented breakpoint stack.
- Hover states aren't documented, per the source's own policy.
- The full in-product TUI (beyond the marketing hero mockup) isn't
  captured here.
- The `/go` SDK page wasn't extracted — it likely shares this chrome but
  introduces undocumented code-sample components.
- Form validation states (success/error messaging) aren't present in the
  captured surfaces.
