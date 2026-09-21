# Intercom Design System — Full Analysis

Adapted from the Intercom design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/intercom/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Intercom's marketing canvas is a soft cream-white ground
(`colors.canvas` ≈ `#f5f1ec`) — not pure white. That warmth is the brand's
signal: editorial, calm, and product-focused rather than bright SaaS. On
top of the cream canvas sit white floating cards (`surface-1`), thin
hairline dividers (`hairline`), and charcoal type (`ink` — `#111111`).

Display type is Saans, Intercom's proprietary geometric sans, set at
weight 500 with measured negative letter-spacing (-2.0px at 72px display).
Body type uses the same family at weight 400. The single proprietary mono,
SaansMono, is used sparingly for code snippets and product-UI screenshots
embedded in the marketing surface.

The single chromatic accent is Fin Orange (`fin-orange` — `#ff5600`),
Intercom's AI-product brand color. It surfaces on the Fin product CTA, the
Fin badge in pricing, and a few inline emphasis moments — it is not the
system primary. The system primary is charcoal (`ink`). Intercom also
maintains a small "report" palette (blue, green, pink, lime) used inside
in-product analytics surfaces shown in mockups, which is not a marketing-
surface color.

The page rhythm leans heavily on product mockups: every section's payload
is a high-fidelity screenshot of Intercom's product UI, framed in white
cards with 16px corners. Marketing chrome is intentionally quiet so the
product itself is the protagonist.

**Key characteristics:**
- A cream canvas (`#f5f1ec`) is the brand's defining surface — neither
  white nor gray, deliberately warm.
- A product-screenshot-led page rhythm: every section centers a product
  mockup card, with marketing chrome kept minimal.
- Saans, a proprietary sans-serif, carries the entire hierarchy;
  SaansMono is used for code-only contexts.
- Charcoal (`#111111`) is the system primary — buttons, headlines, and
  body type all sit on charcoal.
- Fin Orange (`#ff5600`) is the AI-product color, used on the Fin CTA and
  Fin badge, never decoratively.
- Display tracking pulls aggressively negative (-2.0px at 72px); body
  stays at 0.
- Card corners stay modest at 12px and 16px — never pill-rounded, never
  square.

## Colors

Source pages: intercom.com (home), /pricing, /helpdesk, /customers,
/helpdesk/inbox.

### Brand & accent
- **Charcoal** (`ink`) — the system primary surface: headlines, body type,
  and primary-CTA pill background all render in charcoal.
- **White** (`on-primary`) — text on charcoal CTAs, and the canvas of
  floating cards.
- **Fin Orange** (`fin-orange`) — the AI-product accent, used on the Fin
  CTA, the Fin badge, and a small set of inline emphasis moments.
- **Report Orange** (`report-orange`) — a slightly different orange used
  inside the report/analytics palette for in-product mockups.
- **Brand Blue** (`brand-blue`, `#0007cb`) — a saturated brand blue used
  on a small set of marketing illustrations.

### Surface
- **Canvas** (`#f5f1ec`) — the default page background, a soft cream-
  white.
- **Surface 1** (`#ffffff`) — pure white, used for floating cards
  (pricing, feature, product mockup).
- **Surface 2** (`#ebe7e1`) — a slightly darker cream, used for the
  startup-discount banner and alt-row stripes.
- **Hairline** (`#d3cec6`) — the 1px border tone on cards, a soft warm
  gray.
- **Hairline Soft** (`#ebe7e1`) — even softer dividers between FAQ rows
  and footer columns.
- **Inverse Canvas** (`#000000`) — pure black, used only on the
  testimonial/quote callout strip.
- **Inverse Surface 1** (`#313130`) — one step lighter, used for hovered
  footer items in dark contexts.

### Text
- **Ink** (`#111111`) — all headlines, body type, and button labels.
- **Ink Muted** (`#626260`) — secondary type: meta info, deselected
  pricing tabs.
- **Ink Subtle** (`#7b7b78`) — tertiary type: footer columns, helper text.
- **Ink Tertiary** (`#9c9fa5`) — quaternary type: disabled states,
  footnotes.
- **Inverse Ink** (`#ffffff`) — white on black, used in the quote-strip
  type.
- **Inverse Ink Muted** (`#9c9fa5`) — light gray on black, quote-strip
  meta.

### Semantic & report palette (in-product mockups)
- **Error Red** (`#c41c1c`) — form validation, destructive states.
- **Success Green** (`#0bdf50`) — positive states (shared with
  `report-green`).
- **Report Blue** (`#65b5ff`), **Report Pink** (`#ff2067`), **Report Lime**
  (`#b3e01c`) — analytics chart colors. **Report Cyan** (`#03b2cb`) — the
  phone country-selector accent. These live inside product-UI mockups —
  they are Intercom's in-product chart colors, not marketing-surface
  colors.

## Typography

### Font family
Saans is Intercom's proprietary geometric sans (fallback `Saans Fallback,
ui-sans-serif, system-ui`), carrying display, body, eyebrow, and button
type. SaansMono (fallback `SaansMono Fallback, ui-monospace`) is used
inside code snippets shown in product mockups. The same family carries the
entire hierarchy — hierarchy comes from size, weight, and tracking, not
from a family change.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale. Key entries:
`display-xl` (72/500, -2.0px tracking, the largest hero headline),
`display-lg` (56/500, -1.4px, section-opener headlines), `display-md`
(40/500, -0.8px, sub-section headlines), `headline` (28/500, -0.5px,
pricing-tier titles and CTA banners), `card-title` (22/500, -0.3px, card
titles), `subhead` (20/400, -0.2px, lead body and intro paragraphs),
`body-lg` (18/400, -0.1px, hero subhead and lead paragraphs), `body`
(16/400, default body), `button` (15/500, pill/square button labels),
`eyebrow` (14/500, sentence-case section eyebrows), `mono` (13/400,
SaansMono for code in mockups).

### Principles
Weight 500 carries display — Saans at 500 reads as confident without being
bold. Negative letter-spacing scales with size: roughly -2.0px at 72px
(about 3% of size), tapering to 0 on body. Line-heights tighten on
display (1.05 at display-xl) and relax on body (1.50 at body). SaansMono
never appears on marketing chrome — it lives strictly inside product UI.
Eyebrow text uses sentence case at 14px/500 weight, with no all-caps
tracking.

### Font substitutes
Without Saans, suitable substitutes include Söhne (paid), Inter (free,
weight 500), or Geist Sans (free) — Inter at weight 500 is the closest free
substitute. SaansMono can be approximated with JetBrains Mono at weight
400.

## Layout

- **Base unit:** 8px. Full scale: `xxs` 4px, `xs` 8px, `sm` 12px, `md`
  16px, `lg` 24px, `xl` 32px, `xxl` 48px, `section` 96px.
- **Card interior padding:** `lg` (24px) on pricing/feature cards; `xl`
  (32px) on testimonial/discount cards; `xxl` (48px) on CTA banners.
- **Pill button padding:** 10px vertical, 18px horizontal.
- **Max content width:** roughly 1280px.
- **Grid:** card grids run 3-up at desktop, 2-up at tablet, 1-up at
  mobile; the pricing tier grid is 3-up with a comparison strip below
  showing per-tier checkmarks; product-mockup cards span full content
  width, as the protagonist of every section.
- **Whitespace philosophy:** the cream canvas does the work whitespace
  would do in another brand — sections separate through ample vertical
  breathing room (96px) plus the lift onto white cards.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 (flat) | no shadow, no border | body type, hero text, footer |
| 1 (lift on cream) | white `surface-1` on cream `canvas` | pricing cards, feature cards, product mockups |
| 2 (hairline lift) | `surface-1` + 1px `hairline` border | floating tiles with extra definition |
| 3 (deep accent) | `inverse-canvas` true black | quote/testimonial callout strip |

Intercom resists drop shadows entirely — depth is communicated through the
white-on-cream surface change rather than shadow layers. Product-UI
mockups dominate every section's right column or center band; these are
screenshots, not illustrations. There are no atmospheric gradients, no
spotlight cards, and no pastel section blocks — the cream-plus-white
system is deliberately restrained.

## Shapes

| Token | Value | Use |
|---|---|---|
| `rounded.xs` | 4px | small chips, badges |
| `rounded.sm` | 6px | inline tags |
| `rounded.md` | 8px | all buttons, form inputs |
| `rounded.lg` | 12px | pricing cards, feature cards, FAQ rows |
| `rounded.xl` | 16px | product-mockup cards |
| `rounded.xxl` | 24px | oversized CTA banners |
| `rounded.pill` | 9999px | tab toggles |
| `rounded.full` | 9999px | avatar circles |

Product-UI screenshots dominate the marketing surface and sit in 16px
tiles. Customer-logo tiles render at small sizes (roughly 24-32px logo
height) on the cream canvas with no border. Avatar circles in testimonial
cards use full rounding at 40-48px sizes.

## Components

Definitions live in `design-tokens.yaml → components`. Summary:
- **Buttons** — `button-primary` (charcoal CTA, the default primary
  across all pages, with a pressed state), `button-secondary` (white on
  cream with a hairline border), `button-tertiary` (plain text button on
  cream), `button-fin` (Fin-Orange CTA reserved for Fin AI product CTAs).
- **Pricing tabs** — `pricing-tab-default`/`pricing-tab-selected`, a
  pill toggle on the pricing page; selected state lifts onto white.
- **Cards & containers** — `pricing-card` (white, 24px padding),
  `pricing-card-featured` (inverts to charcoal for the recommended tier),
  `feature-card` (generic feature highlight), `product-mockup-card` (the
  dominant card type, framing a high-fidelity product-UI screenshot at
  16px radius), `testimonial-card` (customer quote with avatar, name, and
  company), `startup-discount-card` ("Startups get 90% off" tinted card
  on `surface-2`), `customer-logo-tile` (small tile in the customer
  marquee, cream background), `cta-banner` (closing CTA panel near the
  page bottom).
- **Inputs** — `text-input`/`text-input-focused` (form fields on contact
  and search overlays, white background, 8px radius).
- **FAQ** — `faq-row` (expandable accordion row in the pricing FAQ, cream
  background, hairline-soft bottom rule).
- **Navigation** — `top-nav` (sticky cream bar, 56px tall, wordmark left,
  nav links centered, log-in/sign-up pair right).
- **Footer** — `footer` (dense link grid on cream, wordmark left, 64×32px
  padding).

## Do's and don'ts

**Do**
- Reserve the cream canvas as the system's anchor surface — never replace
  it with pure white.
- Lift cards from cream onto white (`surface-1`) for hierarchy.
- Use the Fin-Orange button only on Fin AI product CTAs and Fin badges.
- Pair Saans display at weight 500 with body at weight 400.
- Use product-UI screenshots as the protagonist of every section.
- Use 12px radius for cards and 16px radius for product-mockup tiles.
- Apply negative tracking proportionally to display sizes.

**Don't**
- Don't use pure white as the canvas.
- Don't use Fin Orange as a section background or as a generic primary
  CTA.
- Don't add drop shadows to floating cards.
- Don't introduce a second display family.
- Don't pill-round CTAs.
- Don't write all-caps tracked eyebrows.
- Don't promote the report-palette colors to brand-level surfaces.
- Don't combine charcoal CTAs and Fin-Orange CTAs in the same viewport.

## Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Desktop-XL | 1440px | default desktop layout |
| Desktop | 1280px | card grid 3-up maintained |
| Tablet | 1024px | card grid 3-up → 2-up |
| Mobile-Lg | 768px | pricing comparison becomes an accordion; nav becomes a hamburger |
| Mobile | 480px | single column; display-xl scales 72px → ~32px |

Touch targets: CTAs hold ≥40px tap height across viewports; pricing-tab
pills hold ≥40px tap height; form inputs hold ≥44px tap target on touch.
Collapsing strategy: top-nav links collapse to a hamburger below 768px
while the primary CTA stays visible; card grids step 3-up → 2-up at
1024px → 1-up below 768px; the pricing comparison collapses into a
per-tier accordion below 768px; display-xl scales from 72px toward
display-md's 40px on mobile. Image behavior: product-UI screenshots
maintain aspect ratio and never crop; customer logos in the marquee may
collapse from 6-up to 3-up below 768px.

## Known gaps

- The report palette lives in product analytics dashboards rendered
  inside marketing mockups; it's documented for completeness but these are
  not brand surface colors.
- Form-field error and validation styling isn't visible on the inspected
  pages.
- Dark mode isn't documented because the marketing site doesn't ship a
  dark theme.
- The helpdesk/inbox product surfaces show in-product UI states that
  aren't formal marketing chrome.
- Saans and SaansMono are proprietary; an open-source substitute (Inter,
  Söhne, Geist) is acceptable, as documented under Typography.
