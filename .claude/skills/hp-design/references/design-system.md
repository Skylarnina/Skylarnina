# HP Design System — Full Analysis

Adapted from the HP marketing-site design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/hp/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

HP's marketing pages read like a long-running consumer-electronics catalog
crossed with an enterprise-software product page. The whole system rests
on pure white (`{colors.canvas}`) with thin gray "cloud"/"fog" panels for
alternating section bands. There's exactly one chromatic action color —
HP Electric Blue (`{colors.primary}` — #024ad8) — and one ink color
(`{colors.ink}` — #1a1a1a); together they carry roughly ninety percent of
the visual work. Type is a single family across every surface — **Forma
DJR Micro**, HP's bespoke geometric grotesque — set at weight 500 for
headlines and 400 for body: clean, neutral, slightly mechanical.

The signature gesture is a pair of **angular blue chevrons** — sharp
0-radius slashes lifted from the HP wordmark's own parallel slashes — that
anchor the homepage hero, the laptop-hub hero, and the printer pricing
page. They frame the primary banner card, layered behind product
photography, on the left and right edges. Outside those decorative
chevrons, every other surface is rectilinear, with soft 8–16px corners on
cards and a tight 4px corner on buttons.

The system runs three distinct voice modes: a **white commercial body**
for product browsing (cards, category icons, pricing tiers); a **dark
navy slab** (near-black `{colors.ink}`) for testimonial bands, the closing
"How can we help?" prelude, and the footer; and a **light fog band**
(`{colors.cloud}` / `{colors.fog}`) for utility sections like comparison
strips and FAQ accordions. Blue only ever shows up on filled CTAs, link
text, the chevron decorations, and the active price stamp on a featured
pricing tier — it never becomes a section background.

**Key characteristics:**
- Pure white canvas with deep ink running every body surface; light fog
  bands alternate for section rhythm.
- HP Electric Blue is the lone CTA fill and link color — it shows up at
  most twice per viewport.
- Bespoke Forma DJR Micro carries every surface (display, body, button,
  caption) at weights 400/500/600/700.
- Cards round at 16px for product/pricing tiles; buttons sit at 4px with
  uppercase labels.
- Geometric blue chevrons (rectangles cut at 45°) frame hero photography
  and echo the wordmark.
- Dark-navy slabs close every page rhythm — testimonial bands, the "how
  can we help?" prelude, and the footer.
- Typical section rhythm: utility strip → top nav → white body →
  cloud-band → ink slab → cloud-band → ink footer.

## Colors

### Brand & accent
- **HP Electric Blue** — the system's lone signal color: primary CTA fill,
  link color, chevron-decoration fill, active sub-nav indicator. Reserved.
- **Bright blue** — a slightly lighter variant used inside dark slabs
  (testimonial-card buttons, dark-band CTA links) where the deeper blue
  would muddy.
- **Deep navy** — the pressed state for the primary CTA and the
  visited-link color.
- **Soft blue** — a pale-blue surface used inside customer-story cards and
  selection chips.

### Surface
- **Canvas / paper** — the universal white page background; paper is the
  same white used for card surfaces, with hairlines or shadows providing
  the lift.
- **Cloud** — the lightest gray section band, used for alternating-row
  backgrounds and product-feature card groups.
- **Fog** — a slightly darker gray band, used for FAQ outer panels and
  header strips.
- **Steel** — a hairline border with stronger emphasis (focus states,
  active filter).
- **Bloom coral / rose** — the "Get 25% off" sale-tag chip plus a soft pink
  lifestyle accent on sale heroes.
- **Storm mist / sea / deep** — teal-storm tones reserved for the
  printer-plan illustration backdrop and supporting infographic accents.

### Text
- **Ink** — universal text color on white surfaces — headlines, body,
  button labels, navigation.
- **Ink deep** — pure black, used for the wordmark and 1px hairline
  strokes around badge outlines.
- **Ink soft** — an alternate near-black used inside dark-navy slabs as a
  subtle textural shift.
- **On ink** — pure white text on every dark-navy slab.
- **Charcoal / graphite** — muted body colors on white surfaces: secondary
  descriptions, fine-print disclaimers, legal lines, and timestamps.

### Semantic
- **Bloom deep / bloom wine** — error and discount-emphasis colors; the
  deep brick reads as "sale" or "destructive" depending on placement.
- **Storm deep** — a neutral status accent (e.g., the printer-plan
  "Versatile" tier color).

## Typography

### Family
The voice is single-family: **Forma DJR Micro** (HP's bespoke geometric
grotesque, Arial fallback) across every surface — display, body, button,
caption. It's a wide, slightly rounded grotesque designed at small optical
sizes to stay legible at UI-chrome scale. HP runs it at weight 400 for
body, 500 for display headlines, and 600/700 for emphasis and button
labels.

The 16/14/12px caption tier carries catalog metadata — model numbers, spec
rows, fine print — at weight 400 with a 1.4–1.5 line-height. Button labels
lift to weight 600/700 with positive 0.5–1.1px letter-spacing and
uppercase transform — the only place the system tracks letters.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale (display-xxl 72px
down to price-md 24px). The typographic decision worth flagging: HP runs
**weight 500 for every display size**, including the largest 72px hero.
Most editorial systems jump to 600/700 at hero scale; HP doesn't. The
result feels open and approachable rather than commanding — appropriate
for a brand selling across consumer, SMB, and enterprise audiences in the
same catalog. Forma DJR Micro's rounded-grotesque shapes do most of the
warmth themselves; there's no italic anywhere except legal disclaimers,
and emphasis is carried entirely by weight (500 → body-emphasis, 700 →
caption-bold).

### Font substitutes
Forma DJR Micro is proprietary. Closest open substitutes: **Inter** at
400/500/600/700 (slightly narrower — bump font-size ~3% to compensate),
**Manrope** at 400/500/600/700 (closer proportions, gentler curves, no
adjustment needed), or **Roboto** at 400/500/700 as a flatter last resort.
When swapping, set body line-height to 1.4 and display line-height to 1.0
explicitly, since most substitutes default looser than Forma DJR Micro's
tight numbers.

## Layout

- Base spacing unit: 8px, with a smaller 4px half-step. The scale is
  gentle — most card padding lands at 16px or 24px, with an 80px section
  gap.
- Full scale in `design-tokens.yaml → spacing`; the 80px section gap is
  the universal rhythm constant, holding across every homepage band and
  between the hero and comparison table on the printer-plan page.
- Card interior padding: 24px on product cards, 32px on promo strips and
  feature cards, 16px on compact article tiles.
- Desktop max-width sits at 1366px, with full-bleed section backgrounds
  beyond the content container.
- Hero sections are single full-width photo cards with the headline
  overlay positioned upper-left or upper-right. Product family grids run
  4 columns above 1200px, 3 at 1024–1199px, 2 at 768–1023px, 1 below.
  Pricing tiers run 4 columns above 1024px, collapsing to a 2×2 grid then
  a single-column accordion.
- Whitespace is commercial-clean: generous around hero photography, tight
  around catalog spec rows. Product cards leave at least 32px above and
  below the photo so it reads as a hero shot rather than a thumbnail.
  Fine-print regions tighten line-height to 1.3 and shrink type to
  11–12px to keep legal copy compact.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 — Flat | No border, no shadow | Section bands (white, cloud, fog), full-bleed photo heroes |
| 1 — Hairline | 1px `{colors.hairline}` border, no shadow | Outlined buttons, comparison-table cells, FAQ accordion outers |
| 2 — Soft lift | Soft drop shadow | Product cards, pricing-tier columns, customer-story tiles |
| 3 — Floating modal | Stronger drop shadow | Add-to-cart drawer, mobile-nav sheet, image zoom modal |

The system stays mostly flat — depth communicates through color contrast
(a cloud band next to a white card on the same band) rather than shadow
elevation. Soft Lift is the workhorse: every product tile and pricing
column gets it, and nothing else does. The floating-modal level is rare,
reserved for transient overlays.

The most distinctive depth gesture is the **HP blue chevron pair** —
two angular slashes (no radius, no shadow) flanking the homepage and
laptop-shop hero cards. They're not generic geometric flourishes; they're
a literal echo of the HP wordmark's two parallel slashes, scaled up to
architectural size. Hero and laptop-shop photography sits inside 16px
containers with a soft 1px hairline, while lifestyle photography
(testimonials, "How HP works for X") goes full-bleed inside dark-navy
slabs without rounding.

## Shapes

| Token | Value | Use |
|---|---|---|
| rounded.none | 0px | Hero chevron decorations, full-bleed photo heroes, marquee strips |
| rounded.xs | 2px | Secondary chip backgrounds, sale-tag pills |
| rounded.sm | 3px | Default secondary CTA radius (small touch zones) |
| rounded.md | 4px | Primary buttons, secondary buttons, text inputs |
| rounded.lg | 8px | Badge pills, category-icon cards, FAQ row containers |
| rounded.xl | 16px | Product cards, pricing tiers, customer-story tiles, photo frames |
| rounded.pill | 9999px | Category sub-nav tabs, search-pill input, filter chips |

The system holds a clear two-tier philosophy: buttons stay sharp (4px,
almost rectilinear) while cards and photo frames stay soft (16px). That
split IS the visual signature — sharp interactive elements against softer
container surfaces. Hero photography sits in 16px frames with no border;
product-family thumbnails are square on a white background, padded so the
device fills about 70% of the frame; customer-story photography uses 16:9
inside the same 16px frame. There are no full-bleed circular avatars —
testimonial avatars are 4px-rounded squares.

## Components

Definitions live in `design-tokens.yaml → components`. No hover states are
documented — only default and active/pressed states — so every component
below varies through separate front-matter entries rather than an implied
hover rule.

- **Buttons** — button-primary (the lone blue CTA, with pressed and
  disabled variants), button-ink (black filled CTA for photo overlays),
  button-outline / button-outline-ink (blue-text and black-text outlined
  secondaries), button-text-link (inline underlined link).
- **Cards** — card-product (the workhorse product tile), card-product-
  feature (full-row feature card with photo + copy), card-pricing-tier /
  -featured (featured tier gets a thin blue top border, never an inverted
  dark card), card-customer-story, card-article-tile, card-category-icon
  (the small icon-and-label tile in "Our Products").
- **Hero & promo** — hero-promo-card (flanked by chevron-decoration blue
  slashes outside its bounding box), promo-strip-dark (inline dark navy
  promo block).
- **Forms** — text-input / text-input-focused (steel border default,
  ink border on focus, no halo), text-input-search (pill search in the
  top nav).
- **Badges** — badge-pill-ink / badge-pill-outline (inline "New"/featured
  tags), badge-sale-coral (the sale price-stamp).
- **Navigation** — utility-strip (36px top bar), nav-bar-top (64px desktop
  nav with a 1px hairline bottom border), nav-link (active page gets a 2px
  blue underline), category-tab / category-tab-active (pill sub-nav for
  filtering).
- **Signature** — chevron-decoration (the geometric blue slash motif, a
  sharp parallelogram sized to the hero card it flanks — hero-only, never
  inline noise), faq-row (accordion row with a hairline divider),
  help-band-dark (the closing "How can we help?" prelude), footer-dark
  (5-column link grid).

## Do's and don'ts

**Do**
- Reserve `{colors.primary}` for the primary CTA, link color, and the
  chevron-decoration motif — at most twice per viewport.
- Set every headline in Forma DJR Micro at weight 500 with line-height
  1.0 — resist bumping weight at hero scale.
- Use `{rounded.xl}` (16px) for cards and photo frames; `{rounded.md}`
  (4px) for buttons and inputs — keep the two-tier split sharp.
- Pair white body bands with cloud-gray alternating bands; let the gray
  do the breathing.
- Close every page rhythm with a dark-navy ink slab — the "how can we
  help?" prelude plus the footer.
- Set button labels uppercase with the documented 0.7px tracking — the
  only place the system tracks letters.
- Use Soft Lift shadow exclusively for product cards and pricing tiers;
  leave section bands flat.
- Frame product photography inside `{rounded.xl}` containers; never use a
  full-bleed circular mask.

**Don't**
- Don't introduce secondary saturated colors outside the primary blue
  family plus the bloom-coral sale tag and storm printer-plan accents.
- Don't apply heavy material shadows — depth comes from color contrast and
  the single Soft Lift tier only.
- Don't round buttons above `{rounded.md}` (4px); an 8px+ button reads as
  a different brand.
- Don't run Forma DJR Micro below 12px — 11px caption is the floor.
- Don't use the chevron decoration as inline noise — it's a hero-only
  architectural element tied to the wordmark.
- Don't lower ink text opacity to create hierarchy — switch surface or
  shift to charcoal/graphite instead.
- Don't replace the HP wordmark with a generic sans lockup — it's a
  custom mark with its own proportions.

## Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Mobile | < 480px | Single-column stack; hamburger nav; section padding drops to ~48px; hero scales to ~36px |
| Mobile-Large | 480–767px | Same column count; hero scales to ~44px; pricing tiers stack vertically |
| Tablet | 768–1023px | 2-column product grid; pricing 2×2; nav still full text labels |
| Desktop | 1024–1279px | 3-column product grid; 4-column pricing; full nav |
| Desktop-Large | ≥ 1280px | 4-column product grid; 1366px content max-width with full-bleed bands |

Touch targets: every interactive element clears 44×44px on mobile —
`button-primary` at 44px height plus 24px horizontal padding clears WCAG
AAA. Nav-link tap areas extend invisibly beyond the text to the full 44px
row height. The utility strip stays visible at every breakpoint, with
dropdowns collapsing to an "Account" icon below 768px; the top nav's
middle category list collapses into a hamburger drawer below 1024px while
search, sign-in, and cart stay visible; the hero stays single-column at
every size, with chevron decorations shrinking to about 60% on tablet and
disappearing entirely on mobile; the product family grid steps 4 → 3 → 2 →
1 column; the footer's 5-column link grid collapses to 2 columns on
tablet, then to a single-column accordion on mobile. There are no art-
direction crop swaps between desktop and mobile — the same image is used
at every size, cropped horizontally rather than letterboxed.

## Known gaps

- Forma DJR Micro is proprietary (Commercial Type / Mark Caneso); Inter,
  Manrope, or Roboto are the documented substitutes.
- Hover colors are not documented — every component spec covers only
  Default and Active/Pressed states.
- Form-field error/validation styling beyond focus isn't visible on the
  inspected pages.
- The HP wordmark itself is a custom mark and shouldn't be approximated
  with a generic sans lockup.
