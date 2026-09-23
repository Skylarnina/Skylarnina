# Replicate Design System — Full Analysis

Adapted from the Replicate design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/replicate/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Replicate is a developer-tools platform styled like an art zine. Its public
marketing pages sit on a warm cream canvas (`{colors.canvas}`, `#f9f7f3`)
instead of the white-or-near-black default most AI infrastructure sites
reach for, and that one decision reshapes everything downstream: product
photography reads as editorial, code wells read like printed pull-quotes,
and the brand's orange (`{colors.primary}`, `#ea2804`) lands like a stamp
rather than a UI theme.

Typography is doing decorative work here, not just labeling content.
**rb-freigeist-neue** — a heavy, slightly condensed grotesque — appears up
to 128px in hero bands with a tight `lineHeight: 1.0` and negative tracking
that lets multi-line headlines pack into dense geometric blocks. Its
companion, **basier-square**, handles body text, button labels, and
metadata at 14–18px. **JetBrains Mono** carries every code sample and
command. Each of the three families has exactly one job.

Page rhythm moves between the default cream canvas, a full-bleed orange
hero, and a `{colors.surface-dark}` (`#202020`) band that hosts the "how it
works" code walkthrough. Curves are deliberately soft everywhere: buttons,
inputs, tags, and avatars all use `rounded.full`, while content cards and
code wells step up to `rounded.md` or `rounded.lg`. Nothing in the system
has a sharp corner.

**Key characteristics:**
- Warm cream canvas (never pure white) paired with a slightly deeper cream
  (`surface-bone`) for inset card groups.
- Hot orange reserved for the primary CTA, the hero band, and inline links
  only — never decorative.
- Massive display headlines (128px hero, 72px section openers) with tight
  leading and negative tracking.
- Strict three-family lane system: display / UI / code, never mixed.
- Every interactive element is fully rounded; content cards step to a
  moderate 10-16px radius instead.
- Dark code wells sit inside the cream canvas like printed pull-quotes.
- Section rhythm: cream → orange hero → cream → dark code-story band →
  cream → black footer.

## Colors

### Brand & accent
- **Replicate Orange** — the brand accent; primary CTA, hero band
  background, and inline link color. Treated as a stamp — at most one
  orange element per viewport.
- **Orange Pressed** — the active/pressed state of orange elements.
- **Hero Glow / Hero Pink** — the lighter orange and warm pink stops that
  make up the radial mesh gradient behind the home hero, softening its
  bottom edge into cream.
- **On-Primary** — white label text on orange surfaces.

### Surface
- **Canvas** — default warm-cream background, never pure white.
- **Surface Bone** — a half-step deeper cream for inset card groups and
  feature bands.
- **Surface Card** — pure white, reserved for individual model cards,
  search inputs, and pricing tiers — the only place white appears.
- **Surface Dark / Surface Deep** — code wells, the featured pricing tier,
  the "how it works" band, and the footer.
- **Hairline / Hairline Strong** — low-contrast dividers on cream, and
  structural button outlines/focused inputs.

### Text
- **Ink** — primary text, notably warmer than pure black to match the
  cream canvas.
- **Body / Charcoal / Mute / Ash / Stone** — a descending scale from
  long-form body copy down to disabled/placeholder text.
- **On-Dark / On-Dark Mute** — primary and secondary text on dark surfaces.

### Semantic
- **Success (badge-success)** — inline "running"/"deployed" status pills on
  model cards.
- **Link** — same value as the brand orange, intentionally pulling links
  into the accent color.
- **Focus Ring** — the default interactive-element focus ring.
- **GitHub Dark** — the GitHub-branded button surface, deliberately kept
  off-brand to match GitHub's own tokens.

## Typography

### Families
- **rb-freigeist-neue** — proprietary heavy grotesque for all display sizes
  (30px+); carries the editorial-magazine personality via tight leading and
  negative tracking.
- **basier-square** — proprietary humanist sans for body, button labels,
  captions, and metadata.
- **jetbrains-mono** — open-source monospace for every code well and inline
  command.

Substitutes when the proprietary faces aren't licensed: **Bricolage
Grotesque** or **Migra** for rb-freigeist-neue; **Geist** or **Inter** for
basier-square. JetBrains Mono is open-source and should be used directly.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale. Principles:
- Display sizes hold `lineHeight: 1.0` (or 0.83 on `heading-lg`) so
  multi-line stacks read as single typographic blocks.
- Negative letter-spacing scales with size — larger type tightens more
  (-3px at 128px down to -0.3px at 20px); body stays at 0.
- Body weight sits at 400 throughout — emphasis comes from switching
  family (basier-square → rb-freigeist-neue), never from bumping weight.
- Code is never set in basier-square, even at small sizes; JetBrains Mono
  carries every literal command, model slug, and API call.

### Note on font substitutes
When substituting, clamp display `lineHeight` to 1.0 explicitly and apply a
roughly -3% letter-spacing on the largest display sizes — open-source
substitutes typically ship with looser default tracking than the originals.

## Layout

- Base spacing unit: 4px; full scale in `design-tokens.yaml → spacing`.
- Section padding: 96px vertical between full-width bands, stretching to
  160px on bands that need extra editorial breathing room (the hero, the
  closing CTA stripe).
- Card interior padding: 16px on model cards, 32px on pricing tiers.
- Max content width ≈ 1280px on body sections, 1440px on full-bleed hero
  bands.
- Model grid: 4 columns desktop → 3 tablet-large → 2 tablet → 1 mobile.
- Pricing: 3-tier grid, stacking below 1024px; the center tier flips to the
  dark "featured" treatment.
- Code-story sections split 2-up (copy left, code well right), collapsing
  to stacked below 1024px.
- Whitespace on cream is generous and editorial (96-160px between
  sections); inside cards it tightens to 16-32px for a compact
  list-of-cards rhythm. Hairline dividers replace shadow on cream; the
  translucent dark-divider token carries the same role on dark surfaces.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 flat | no shadow/border | default cream canvas, full-bleed bands |
| 1 outline | 1px hairline | model cards, pricing tiers, collection tiles |
| 2 bone inset | shift to surface-bone inside a cream band | feature groups, "how it works" walkthrough |
| 3 dark inversion | card flips to surface-dark against cream | code wells, featured pricing tier |
| 4 soft drop | subtle shadow (~8% opacity) | hover-anchored model thumbnails |

Shadows exist in the token set but are used sparingly, mainly to lift
photography thumbnails one step off the cream canvas — the dominant
elevation language is color-blocking, not shadow stacking.

**Decorative depth:** the home hero's atmospheric mesh layers the brand
orange core through the lighter hero-glow into an outer hero-pink wash. The
"how it works" band runs full-bleed dark with a single hairline divider
between narrative copy and code well. A horizontally-scrolling contributor
avatar mosaic sits over a textured cream canvas — the only place avatars
appear at the brand level.

## Shapes

| Token | Value | Use |
|---|---|---|
| rounded.none | 0px | hero bands, full-bleed sections, footer |
| rounded.xs | 4px | code tabs, inline tags inside code wells |
| rounded.sm | 6px | mid-radius callouts, small inset chips |
| rounded.md | 10px | model cards, collection tiles, code wells |
| rounded.lg | 16px | pricing tiers, larger feature cards |
| rounded.full | 9999px | buttons, inputs, badges, avatars, pills |

Model thumbnails are square (1:1) at `rounded.md` corners, full-bleed to
the card edge. Hero example outputs run 4:3 or 16:9 at `rounded.md`.
Contributor avatars are circular at 40px (32px in metadata contexts). The
hero band uses a stylized black-ink illustration rather than photography,
kept inside the orange band rather than laid over cream.

## Components

Definitions live in `design-tokens.yaml → components`. Summary:
- **Buttons** — primary (orange fill), dark (equal-weight alternative),
  outline, ghost (inline sub-actions), and a circular icon button — all
  fully rounded.
- **Cards** — model-card (thumbnail + name + status pill), collection-tile,
  pricing-tier / pricing-tier-featured (dark inversion for the recommended
  plan), code-block with a tab strip for switching languages, and the
  orange hero-band.
- **Inputs** — a pill-shaped text-input with a 3px focus ring.
- **Navigation** — a 60px nav bar (wordmark left, nav center, GitHub icon +
  sign-in + primary CTA right) that collapses to hamburger on mobile, plus
  horizontally-scrolling sub-nav filter pills.
- **Signature** — badge-status (green "running" pill), badge-tag (neutral
  capability tags), contributor-avatar, and a dense multi-column footer.

## Do's and don'ts

**Do**
- Use cream as the default page background; reserve white for individual
  cards, inputs, and the hero illustration backdrop.
- Keep orange to three roles: primary CTA, home hero band, inline links.
- Fully round every interactive element; step content cards to 10px/16px.
- Open hero bands with the largest display sizes at `lineHeight: 1.0` and
  negative tracking.
- Keep the three type families in their strict lanes.
- Render code in a dark code-block, never an inline light-grey box.

**Don't**
- Don't replace cream with pure white at the page level.
- Don't introduce a second brand color — the green success and blue focus
  tokens are functional, not decorative.
- Don't loosen display `lineHeight` past 1.0.
- Don't bump body weight to 500 for emphasis — change family instead.
- Don't apply full rounding to content cards; that breaks the rhythm.
- Don't put code in a light grey box, and don't add drop shadows on cream
  surfaces beyond the sparing hover-lift on thumbnails.

## Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Desktop XL | ≥1440px | full 1280 body max-width, hero runs full-bleed, 4-up model grid |
| Desktop | 1280-1439px | container shrinks with 24px side padding |
| Tablet Large | 1024-1279px | model grid 3-up, code-story splits stay 2-up |
| Tablet | 768-1023px | model grid 2-up, code-story stacks, pricing stacks vertically |
| Mobile Large | 426-767px | model grid 1-up, nav collapses to hamburger, hero clamps to 64px |
| Mobile | ≤425px | all grids 1-up, hero clamps to 48px, section padding collapses to 64px |

Touch targets: all buttons ship at a minimum 44px tall on mobile — the
default primary button is already 44px, clearing WCAG AAA. The icon button
(36px) grows to 44px on mobile via padding; sub-nav pills grow from 36px to
40px.

Collapsing strategy: nav collapses to hamburger below 1024px; hero display
clamps 128px → 96px → 64px → 48px across the ladder; the 3-up pricing grid
stacks below 1024px with the featured tier staying centered; code-story
splits switch to stacked below 1024px with the code well always second;
sub-nav pills convert to a horizontal scroll rail below 768px.

Image behavior: model thumbnails serve at 1.5×/2× DPR, swapping to a
smaller export below 768px. The hero mesh is a CSS gradient with no asset
cost or breakpoint variation. Code blocks wrap softly below 1024px instead
of scrolling horizontally, with long lines breaking at a continuation
marker.

## Known gaps

- Pressed/active states are only documented for the primary button; other
  components rely on the focus ring for interactive feedback, which isn't
  broken out as a per-component variant.
- The logged-in model playground and dashboard/billing surfaces are out of
  scope — only the public marketing canvas is documented.
- The home hero illustration ("the tinkerer at the workbench") is bespoke
  artwork, not a reusable token — replicating it requires custom
  illustration rather than the token set.
