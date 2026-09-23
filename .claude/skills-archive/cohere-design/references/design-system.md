# Cohere Design System — Full Analysis

Adapted from the Cohere design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/cohere/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Cohere's current web presence reads like a sober enterprise-AI command
center with editorial restraint. The homepage opens on a huge typographic
declaration over a white canvas, then leans on photography, dark product
mockups, trust logos, and generous empty space to make AI infrastructure
feel controlled rather than speculative. Product pages invert the tone into
deep-green-black or dark-navy bands, while blog and research pages move
toward a publishing-system clarity — large filters, thin rules, dense
lists, pale technical backgrounds.

What sets the system apart is the pairing of an austere black-and-white UI
shell with bursts of tactile brand imagery. Color rarely appears as
decorative chrome; instead it arrives through photography, abstract 3D
media, coral blog-taxonomy chips, blue research links, and dark product
environments. Cards are rounded but not cute. Type reads large, tight, and
almost monospaced in spirit, giving marketing, product, and editorial
surfaces a shared research-lab cadence.

**Key characteristics:**
- Monumental display headlines with very tight line-height and negative
  tracking.
- White editorial canvases interrupted by deep-green, dark-navy, and
  image-led CTA bands.
- Rounded media and product cards, usually 8px to 22px.
- Pill CTAs in near-black or white; most secondary actions are underlined
  text links instead.
- Trust-logo strips with monochrome partner marks and wide vertical
  spacing.
- Agent-console mockups: dark panels, small status chips, integration
  badges.
- Blog/research surfaces with prominent taxonomy chips, long
  rule-separated lists, and search fields.

## Colors

### Brand & accent
- **Cohere black** — the announcement bar, highest-contrast text, and
  global brand anchor.
- **Near-black primary** — primary CTA buttons, dark footer, deep UI cards.
- **Deep enterprise green** — product hero bands for North/Command-style
  dark sections.
- **Dark navy** — financial-services and security-oriented solution bands.
- **Action blue** — editorial links, pagination, secondary emphasis.
- **Coral / soft coral** — blog category chips, taxonomy outlines, warm
  product markers.

### Surface & background
- **Canvas white** — the dominant page background and form/card surface.
- **Soft stone** — product cards, testimonial placeholders, warm neutral
  blocks.
- **Pale green wash** — the North page's section backdrop behind stacked
  dark capability panels.
- **Pale blue wash** — blog CTA surface behind abstract 3D imagery.
- **Card border** — the softest card containment line.

### Text & rules
- **Ink** — default body text and most link text on light backgrounds.
- **Muted slate / slate** — footer links, dates, metadata, and research
  separators.
- **Hairline / border light** — standard list rules, section dividers, and
  a secondary utility rule.

### Semantic
- **Focus blue** — keyboard focus/ring color.
- **Form focus violet** — text-input focus border.
- **Error red** — extracted ring/shadow color for validation-like states.

### Gradient system
Cohere doesn't use gradients as a generic UI fill — color and gradient
richness are media-led: abstract 3D hero imagery, deep-blue open-science
particle fields, red-orange product video posters, and dark green-to-black
product environments. Keep UI surfaces flat and save gradient work for
large media panels and CTA image bands.

## Typography

### Font family
- **Display**: CohereText, falling back to Space Grotesk, Inter,
  ui-sans-serif, system-ui.
- **Body/UI**: Unica77 Cohere Web, falling back to Inter, Arial,
  ui-sans-serif, system-ui.
- **Technical labels**: CohereMono, falling back to Arial, ui-sans-serif,
  system-ui.
- **Icons**: custom icon fonts and thin-line geometric illustrations.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale — from
`hero-display` (96px/400/-1.92px) down to `micro` (12px/400). All sizes sit
at weight 400; hierarchy is carried by size and tracking, not weight.

### Principles
Use massive type sparingly — most pages have one oversized headline before
settling into restrained 16-24px UI copy. Keep display type tight and
carved rather than airy. Avoid heavy bold weights; size, spacing, and
surface contrast do the hierarchy work instead. Reserve uppercase mono
labels for category/system markers, especially on product and research
pages. Editorial pages can bring in coral chips and blue links, but the
base typography stays black and measured.

### Note on font substitutes
Exact proprietary font files aren't bundled — use the fallback stacks above
when implementing externally.

## Layout

### Spacing system
An 8px base with many one-off alignment values: 2, 6, 8, 10, 12, 16, 20,
22, 24, 28, 32, 36, 40, 56, 60, 64, and 80px. Large sections lean on
dramatic vertical breathing room — the homepage places its trust-logo strip
far below the hero media, and product pages often hold dark panels inside
wide fields of empty white space, transitioning to dense forms or footers
only near the end.

### Grid & container
- Global nav uses a three-zone layout: logo left, menu centered, sign-in/
  CTA right.
- The home hero is centered text above a two-card media composition: a
  wide product-mockup card beside a narrower photography card.
- Feature sections commonly use 3-column cards on desktop.
- Product pages alternate centered hero blocks, trust-logo strips, large
  single-feature bands, and 2- or 3-column card grids.
- Research pages use full-width lists with date and chip columns instead
  of decorative cards.
- Forms use two-column input rows inside a rounded white card set against
  dark or stone section backgrounds.

### Whitespace philosophy
Whitespace functions as a trust signal — large empty intervals separate the
brand claim, customer proof, product proof, and CTA. Density appears only
where the information architecture calls for it: research-paper rows, blog
card grids, and contact-form fields.

## Elevation & depth

Cohere is mostly flat; depth comes from surface alternation, media
contrast, rounded corners, and thin borders rather than drop shadows.

| Level | Treatment | Use |
|---|---|---|
| Flat | No shadow, white or dark field | Hero copy, research lists, editorial surfaces |
| Bordered | 1px hairline / border-light / dark translucent rules | Research rows, forms, pale cards, footer inputs |
| Media lift | Rounded image/video over contrasting section color | Hero photo cards, product videos, CTA imagery |
| Dark product field | Full-width deep-green or navy band | Command, North, financial-services, security sections |

## Shapes

| Token | Value | Role |
|---|---|---|
| `xs` | 4px | Small images, search fields, article thumbnails, utility elements |
| `sm` | 8px | Blog chips, cards, small media, dialogs |
| `md` | 16px | Medium product cards, grouped blocks |
| `lg` | 22px | Signature media-card and soft placeholder radius |
| `xl` | 30px | Research/topic filter pills |
| `pill` | 32px | Primary CTA buttons |
| `full` | 9999px | Round status elements and fully pill-shaped controls |

### Image treatment
Images act as visible-cornered rounded cards — product videos, enterprise
photography, article thumbnails, abstract 3D renders — rather than
decorative full-bleed backdrops, except inside CTA bands. The dominant
radii are 8px and 22px.

## Components

Definitions live in `design-tokens.yaml → components`. Summary:
- **`button-primary`** — near-black or white 32px-radius pill, 12×24
  padding, used for "Request a demo", "Submit", and hero CTAs.
- **`button-secondary`** — text-only underlined/rule-aligned action link
  with no fill; used for "Explore products", "Try the Playground",
  newsletter sign-up.
- **`button-pill-outline`** — 30px-radius outlined pill with transparent
  fill, for research filters and lightweight taxonomy controls.
- **`announcement-bar`** — 36px black strip above the nav with centered
  microcopy, an underlined "Learn more" link, and a close control.
- **`hero-photo-card`** — rounded media card (22px large / 8px small)
  combining photography or abstract imagery with an overlaid dark
  agent-console module.
- **`agent-console-card`** — dark product mockup panel showing agent
  names, status chips, integration badges, prompt fields, and response
  cards.
- **`trust-logo-strip`** — quiet centered copy above a row of monochrome
  logos, no cards or borders, just wide spacing.
- **`capability-card`** — thin-line geometric illustration + 24px heading
  + body + text link; often unboxed on light backgrounds.
- **`dark-feature-band`** — full-width deep-green/navy section for
  capabilities, security claims, and feature breakdowns; text turns white,
  cards get darker translucent surfaces and pale borders.
- **`product-card`** — warm stone card for product/model summaries,
  typically 3-column, 8px radius, with a small pill button and checkmark
  bullet rows.
- **`blog-filter-chip`** — oversized coral taxonomy chip; active chips
  invert to coral fill with dark text, inactive chips use coral outline +
  pale fill.
- **`research-table`** — rule-separated publication list: title left,
  topic pills centered, date right; tall white border-driven rows.
- **`contact-form-card`** — rounded white form panel against dark-green
  or warm-stone sections; rectangular inputs with thin gray borders.
- **`footer-newsletter`** — dark footer subscription block with a coral
  "AI moves fast" label, white headline, muted legal microcopy, and a
  single-line email field.

## Do's and don'ts

**Do**
- Use white canvas as the default surface; introduce dark green or navy as
  full-width product bands.
- Keep primary CTAs pill-shaped and near-black on light surfaces.
- Use 22px radius on major media cards and placeholders.
- Use coral for editorial taxonomy and small warm accents, not as the main
  CTA system.
- Use monochrome trust logos with wide spacing.
- Use thin-line geometric illustrations for research/capability icons.
- Let photography and product mockups carry color while the UI shell stays
  restrained.

**Don't**
- Don't turn coral or blue into broad decorative surface colors.
- Don't add heavy drop shadows to cards.
- Don't make every section card-based — unframed rows, rules, and open
  space are core to the system.
- Don't use rounded cards below 8px for major media.
- Don't replace the display/body type split with one generic sans.
- Don't render undocumented interaction variants.
- Don't use saturated gradients as normal UI backgrounds — keep gradients
  media-led.

## Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Small mobile | < 425px | Single-column cards, compact nav, reduced hero headline scale |
| Mobile | 425–640px | Hero media stacks, card grids go one column, form rows stack |
| Large mobile | 640–768px | Wider one-column layouts with larger media cards |
| Tablet | 768–1024px | Two-column cards begin, nav spacing tightens |
| Desktop | 1024–1440px | Full nav, 3-column card grids, split hero compositions |
| Large desktop | 1440–2560px | Wide containers, large empty vertical intervals |

Primary CTAs and pills meet comfortable touch sizing through 12-24px
padding and pill radii; research and blog filter chips are deliberately
larger than standard tags to stay usable on touch devices. Nav collapses
from full horizontal links to a compact mobile menu; hero media moves from
split cards to stacked cards; product/capability grids collapse 3 → 2 → 1;
form field rows collapse to a single column; research rows keep their
rule-separated structure but stack metadata below titles on smaller
widths.

## Known gaps

- Exact proprietary font files aren't bundled; use the documented fallbacks
  when implementing externally.
- Mobile screenshots weren't regenerated for this update, so mobile
  behavior is documented from the desktop system and existing responsive
  patterns.
- Some live pages lazy-load content blocks late; blank testimonial
  placeholders are documented as skeleton surfaces rather than filled
  testimonial cards.
