# Revolut Design System — Full Analysis

Adapted from the Revolut design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/revolut/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Revolut's marketing canvas runs a high-contrast two-mode system: a
near-black storytelling canvas (`{colors.canvas-dark}`, `#000000`) that
hosts hero bands, product mockups, and the planning section, alternating
with white catalogue bands (`{colors.canvas-light}`) that host comparison
tables, FAQs, and download tiles. The two modes switch in full-bleed bands
rather than gradual transitions — sections slam against each other, which
is where the brand's magazine-spread rhythm comes from.

Display type is **Aeonik Pro at weight 500**, used from 20px all the way up
to 136px. The flagship hero ("Banking & Beyond") sits at 80-136px with
`lineHeight: 1.0` and tight negative tracking. Body copy runs in
open-source **Inter** at weight 400, paired with slight positive tracking
(0.24px) on UI labels for a touch of mechanical precision.

The brand accent, cobalt violet (`{colors.primary}`, `#494fdf`), appears
scarcely. The real primary CTA on the hero is a white pill on black
("Choose your subscription"); cobalt is reserved for the featured plan
card, secondary CTAs on white sections, and the brand glyph itself. A wide
secondary palette — deep teal, light-blue, deep-pink, light-green, warning
orange, yellow — lives inside product mockups and feature illustrations
only, never as a button surface.

**Key characteristics:**
- Two-mode canvas: true black for storytelling, white for browsing,
  switched in full-bleed bands.
- Aeonik Pro 500 across 20-136px with `lineHeight: 1.0` and large negative
  tracking on display sizes.
- The real primary CTA is a white pill with black text on the dark canvas
  — cobalt violet is reserved for the featured plan card and secondary
  CTAs.
- Eight saturated accent colors live inside product mockups and
  illustrations only, never as button surfaces.
- All buttons are pill-shaped; content cards use `rounded.lg` (20px);
  inputs and small chips use `rounded.md` (12px).
- Photography is product-led — phone, card, and terminal mockups shown
  full-bleed inside dark sections with no caption overlay.

## Colors

### Brand & accent
- **Cobalt Violet** — the brand accent; reserved for the featured plan
  card, the wordmark icon, and secondary CTAs in white-canvas regions.
- **Cobalt Bright** — a one-step-brighter variant used for inline link
  color and accent-photo headers.
- **Cobalt Deep** — the active/pressed state of cobalt elements.
- **On-Primary** — white label text on cobalt surfaces.

### Surface
- **Canvas Light** — the white catalogue mode for FAQ, downloads, and
  comparison tables.
- **Canvas Dark** — the storytelling canvas; true black, never near-black.
- **Surface Soft** — a subtle off-white for download tiles, soft buttons,
  and inset groups inside white bands.
- **Surface Card** — pure white card surface for feature cards on white.
- **Surface Deep** — a one-step-up dark surface for inset cards inside
  black-canvas regions.
- **Surface Elevated** — the planning-section card background, slightly
  luminous, used to lift plan cards off the black canvas.
- **Hairline Light / Hairline Dark / Hairline Strong** — 1px dividers on
  white bands, their low-contrast equivalent in dark regions, and the
  structural full-strength divider.

### Text
- **Ink** — primary text, warmer than pure black, paired with the white
  canvas.
- **Body / Charcoal / Mute / Ash / Stone / Faint** — a descending scale
  from long-form body copy down to disabled foreground/hairline
  replacement.
- **On-Dark / On-Dark Mute** — primary and secondary text on the dark
  canvas.

### Semantic
- **Accent Teal / Light Blue / Blue Link / Light Green / Green Text /
  Yellow / Warning / Pink / Danger / Deep Red / Brown** — a wide palette
  used inside product mockup illustrations, inline link colors, and
  destructive/positive states. None of these appear as button surfaces —
  see Do's and Don'ts.
- **Link** — same value as accent-blue-link, the default inline link
  color on white surfaces.

## Typography

### Families
- **Aeonik Pro** — proprietary humanist sans for all display sizes (20px+)
  at weight 500, carrying the brand's editorial confidence and tightening
  dramatically with negative tracking at large sizes.
- **Inter** — open-source workhorse for body, button labels, captions, and
  metadata, always at weight 400 or 600, with positive tracking (0.16-
  0.24px) on UI labels.

When Aeonik Pro can't be licensed, **Inter Display**, **General Sans**, or
**Söhne** are credible substitutes — apply roughly -1% letter-spacing on
display sizes to match the original tightness.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale (display-xxl
136px down to caption 13px). Principles:
- Display sizes always run at weight 500 with `lineHeight: 1.0` (1.19-1.21
  below 48px); negative tracking scales with size — bigger types tighten
  more.
- Body Inter sits at weight 400 with positive tracking (0.24px) — the
  small nudge gives UI labels a slightly mechanical, fintech-precise feel.
- Hero CTAs use the Aeonik Pro `button-lg` variant; everything below the
  hero uses the Inter `button-md`.
- Inline links inside dark photo regions step up to weight 700
  (`link-emph`) so they hold contrast without leaning on the cobalt accent.

### Note on font substitutes
Clamp display `lineHeight` to 1.0 explicitly and apply -1% letter-spacing
on display sizes when substituting for Aeonik Pro. Inter is open-source and
should be used directly for body.

## Layout

- Base spacing unit: 4px; full scale in `design-tokens.yaml → spacing`.
- Section padding: 88px vertical between bands, 120px on the hero band and
  the closing planning section.
- Card interior padding: 32px on feature and plan cards.
- Max content width ≈ 1200px on body sections; hero bands run full-bleed.
- Plan grid: 4-up on the home page, stacking 2-up tablet, 1-up small
  mobile.
- Feature grid: 3-up desktop → 2-up tablet → 1-up mobile.
- Product mockup bands: a single full-width hero photo of a phone or card
  mockup, with no surrounding chrome — the asset itself is the section.
- Whitespace is generous and editorial (88-120px between sections) so
  display headlines have room to register at 80-136px. Card padding holds
  at 32px. Hairline dividers replace shadow on white surfaces; their dark
  equivalent carries the same role in dark regions.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 flat | no shadow/border | default canvas bands, full-bleed hero |
| 1 surface card | white card on a soft off-white band | feature cards inside light bands |
| 2 surface elevated dark | luminous dark surface on black | plan cards inside the planning section |
| 3 featured surface | cobalt violet on black | featured plan card (cobalt inversion) |
| 4 product mockup | full-bleed photo asset | hero phone/card/terminal mockup bands |

There's no traditional drop-shadow language — depth registers through
color-blocking (light-to-dark band switches) and surface-luminance shifts.
Photography mockups carry their own depth from the asset itself.

**Decorative depth:** the home page's phone-mockup hero band sits full-
bleed against black with the device's own glow as the only atmospheric
depth — no additional gradients, no shadows. The cobalt-violet featured
plan card sits inside the otherwise dark planning grid as a single
saturated color block, marking the recommended tier visually. The metals
card tier uses a warm brown accent and deep gradient to signal premium
without resorting to a gold-on-black metallic effect.

## Shapes

| Token | Value | Use |
|---|---|---|
| rounded.none | 0px | hero bands, full-bleed sections, footer |
| rounded.sm | 8px | inline tags, small chips |
| rounded.md | 12px | form inputs, download tiles |
| rounded.lg | 20px | feature cards, plan cards |
| rounded.xl | 28px | product mockup containers |
| rounded.full | 9999px | buttons, pills, badges, tabs |

Phone mockups run at a 9:19.5 vertical aspect with `rounded.xl` corners on
the device chrome. Card mockups run at the credit-card ratio (1.586:1)
with `rounded.lg` corners. Terminal/POS mockups run 4:3 with `rounded.xl`
corners and substantial surrounding padding. Rare lifestyle photography
runs 16:9 with `rounded.lg` corners.

## Components

Definitions live in `design-tokens.yaml → components`. Summary:
- **Buttons** — primary (white pill on dark, the real primary CTA), dark
  (reverse-canvas equivalent), soft (tertiary on white), outline-light /
  outline-dark, and a small pill for sub-nav chips.
- **Cards** — hero-band-dark / hero-band-photo, feature-card-light /
  feature-card-dark, plan-card / plan-card-featured (cobalt inversion), a
  full-bleed product-mockup container, and an app-store download-tile.
- **Inputs** — a generously tall (56px) text-input for fintech-grade
  accessibility.
- **Navigation** — a 64px nav bar (wordmark left, nav center, login +
  primary CTA right) and horizontal sub-nav pill chips.
- **Signature** — badge-tag (neutral) and badge-feature (cobalt "New"/
  "Most popular" pill), plus a multi-column dark footer with regulatory
  disclosure text.

## Do's and don'ts

**Do**
- Switch full bands between black (storytelling) and white (catalogue) —
  the two-mode rhythm is core to the brand.
- Use the white pill on dark as the primary CTA on every dark hero band.
- Reserve cobalt violet for the featured plan card and the wordmark —
  treat it as a deliberate stamp, not a color theme.
- Set hero headlines in Aeonik Pro 500 at 80-136px with `lineHeight: 1.0`
  and large negative tracking.
- Use Inter for body, buttons, and captions — never substitute Aeonik Pro
  for body type.
- Apply `rounded.full` to every button and pill; `rounded.lg` (20px) to
  feature/plan cards; `rounded.md` (12px) to inputs.
- Show product mockups full-bleed inside dark sections.
- Use the wide accent palette inside product illustrations and iconography
  only.

**Don't**
- Don't use accent colors (teal, pink, etc.) as button surfaces — they
  live inside illustrations only.
- Don't use a near-black canvas — the brand is `#000000`, not `#0a0a0a`.
- Don't pair white text with cobalt violet in large body content — cobalt
  is for the featured plan card surface, not prose.
- Don't add drop shadows on cards — elevation is canvas + surface-
  luminance shifts.
- Don't introduce a second brand color — cobalt violet is the only brand
  stamp.
- Don't loosen Aeonik Pro `lineHeight` past 1.0 on display sizes.
- Don't bump body Inter to weight 500 — use 400 (default) or 600
  (emphatic) only.
- Don't pair the dark canvas with a third dark surface beyond
  surface-elevated; the dark surface ladder has only two steps.

## Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Desktop XL | ≥1440px | 4-up plan grid, full-bleed product mockup bands, max content 1200 |
| Desktop | 1280-1439px | container shrinks with larger side padding |
| Tablet Large | 1024-1279px | plan grid 4-up; feature grid 3-up |
| Tablet | 768-1023px | plan grid 2-up; feature grid 2-up |
| Mobile Large | 426-767px | plan grid 1-up; feature grid 1-up; nav collapses to hamburger; hero clamps to 64px |
| Mobile | ≤425px | all grids 1-up; hero clamps to 48px; section padding collapses to 64px |

Touch targets: all buttons ship at minimum 48px tall — comfortably clears
WCAG AAA. The text input is 56px tall for fintech-grade accessibility. The
small pill chip (36px) grows to 44px on mobile via padding.

Collapsing strategy: nav collapses to hamburger below 1024px; hero display
clamps 136px → 80px → 64px → 48px across the ladder; the plan grid steps
4-up → 2-up → 1-up; product mockup bands stay full-bleed at every
breakpoint, cropping inward rather than letterboxing; sub-nav pills convert
to a horizontal scroll rail below 768px.

Image behavior: phone and card mockups serve at 1.5×/2× DPR, swapping to a
smaller hero crop below 768px. Product photography retains its own
atmospheric lighting at every breakpoint with no responsive variant assets.

## Known gaps

- Pressed/active states are documented for the primary button only; other
  components rely on the browser's default focus ring.
- Logged-in app surfaces (transactions, transfers, account settings) are
  out of scope — only the public marketing canvas is documented.
- The wide accent palette is captured from the extracted token set, but
  exact usage inside product illustrations varies per market and product
  line — document per-illustration rather than as system buttons.
- Mobile-app screenshot art direction (phone bezels, status bars) is
  product-photography territory and isn't standardized as design tokens.
