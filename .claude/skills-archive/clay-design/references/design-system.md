# Clay Design System — Full Analysis

Adapted from the Clay design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/clay/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Clay.com is the most playful interface in the B2B GTM-data category. Instead
of the cool-gray grids and gradients most data-platform brands lean on, Clay
sits on a **cream-tinted white canvas** (`colors.canvas`, `#fffaf0`) and
turns its brand voltage over to **3D-rendered claymation illustrations** —
mountains, mascot characters, peach/ochre/lavender landscapes.

The display voice is **Plain Black**, a custom rounded typeface (or Inter
500 as a substitute) set very large (72px in the hero) with aggressive
negative tracking. Weight never exceeds 500 — the rounded letterforms
already carry warmth, and going bolder would read as loud rather than
friendly. Body copy runs on Inter at standard weights.

The strongest component signature is a **six-color feature-card rotation**:
hot pink, deep teal, lavender, peach, ochre, and a cream neutral. Each card
carries a fragment of real product UI at small scale — a Claygent agent run,
a sequencer flow, a CRM enrichment result — so the color block itself
becomes the page's primary visual unit on every long-scroll page.

**Key characteristics:**
- Cream canvas (`#fffaf0`), not cool gray — this warmth is what separates
  Clay from its data-platform competitors.
- Dark navy/near-black primary CTAs (`colors.primary`, `#0a0a0a`) at a
  friendly-but-not-pill 12px radius.
- The six-color saturated card palette carries the brand's visual energy.
- 3D claymation illustrations (mountains, characters, abstract landforms)
  as the signature full-bleed hero artifact.
- Plain Black display type at weight 500 only, tracked from -1px to
  -2.5px depending on size.
- A generous radius scale: 12px buttons/inputs, 16px content cards, 24px
  feature cards — scaled to match the rounded display type's character.
- Product UI fragments (agent logs, sequencer flows, enrichment tables)
  embedded inside the colored cards, not abstract art.
- 96px section rhythm between major bands.
- A cream footer, never a dark one — even the closing band of the page
  stays warm and light.

## Colors

### Brand & accent
- **Primary** — near-black ink used for CTAs and h1/h2 headlines.
- **Brand pink / teal / lavender / peach / ochre / mint / coral** — the
  saturated card palette plus two extra illustration accents (mint, coral).
  Teal often marks the featured pricing tier.

### Surface
- **Canvas** — the cream page floor.
- **Surface soft / card / strong** — three ascending cream tones for
  footers, feature-card neutrals, and emphasized bands.
- **Surface dark / dark elevated** — a rare dark-teal-tinted near-black,
  used only occasionally.
- **Hairline** — 1px border on cards and inputs.

### Text
- **Ink** — headlines and primary text.
- **Body strong / body** — lead paragraphs and default running copy.
- **Muted / muted soft** — sub-headings down through fine print.
- **On-primary / on-dark** — white text over dark or primary fills.

### Semantic
Standard success/warning/error greens, ambers, and reds for state feedback.

## Typography

### Font family
**Plain Black** (or Inter 500 with -0.05em tracking as an open-source
stand-in; Söhne Breit or Recoleta are alternate substitutes) carries every
headline. **Inter** covers body, navigation, and UI text. The two never mix
inside a single line — display moments stay in Plain Black, everything else
stays in Inter.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale, from
`display-xl` (72px/500/-2.5px) down to `nav-link` (14px/500). The
governing rule: display type is always weight 500 with negative tracking;
body/UI type stays at 0 tracking.

### Principles
Plain Black at 500 plus negative letter-spacing IS the brand voice —
pushing to 700 reads as bombastic and flattens the typeface's rounded
warmth. Mixing display and body families inside one text block is treated
as a system violation.

## Layout

- Base spacing unit: 4px; full ladder in `design-tokens.yaml → spacing`.
- Section padding: 96px (`spacing.section`) between major editorial bands.
- Card interior padding: 32px for feature/pricing cards, 24px for
  testimonial and product-mockup cards.
- Max content width ~1280px; hero often splits 7/5 (headline left,
  illustration right).
- Feature-card grids: 3-up desktop → 2-up tablet → 1-up mobile; pricing
  grids run 3–4-up down to 1-up.
- Generous whitespace surrounds the big rounded headlines and saturated
  cards — the combination of cream canvas, colored cards, and 3D
  illustration is what gives the page its playful warmth.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| Flat | No shadow, no border | Body sections, top nav, hero |
| Soft hairline | 1px `hairline` border | Inputs, small content cards |
| Saturated card | Brand color fill, no shadow | Feature cards |
| Cream card | `surface-card` fill, no shadow | Testimonial, secondary cards |
| Subtle drop shadow | Faint low-alpha shadow | Rare hover-elevated states |

No heavy shadows anywhere in the system — depth reads from the contrast
between the cream canvas and the bright feature-card fills, not from
elevation tricks. Decorative depth instead comes from the illustrated
assets themselves: the 3D claymation mountains/characters (not tokenized —
they're per-page illustration) and recurring mascot figures inside cards
and CTAs.

## Shapes

| Token | Value | Use |
|---|---|---|
| `rounded.xs` | 6px | Small badges, dropdown items |
| `rounded.sm` | 8px | Small buttons, hairline accents |
| `rounded.md` | 12px | Standard CTA buttons, text inputs |
| `rounded.lg` | 16px | Content cards, testimonial cards, pricing tiers |
| `rounded.xl` | 24px | Saturated feature cards |
| `rounded.pill` | 9999px | Category tabs, badge pills |
| `rounded.full` | 9999px / 50% | Avatars, icon buttons |

## Components

Definitions live in `design-tokens.yaml → components`. Summary:
- **Top nav** — 64px cream bar, logo left, primary menu center, Sign
  in + Try free CTA right.
- **Buttons** — primary (near-black fill), secondary (cream + hairline),
  on-color (white, used atop saturated cards), text-link, and inline
  text-link variants.
- **Hero** — a cream 7/5 split: headline + CTAs left, a 3D claymation
  illustration card right (`hero-illustration-card`).
- **Feature cards** — one entry per brand color (pink, teal, lavender,
  peach, ochre) plus a lower-key cream variant; each carries a title, a
  short description, and a product-UI or mascot fragment. Text flips to
  white on the darker pink/teal cards and stays dark on the lighter ones.
- **Product mockup card** — cream card with hairline border showing real
  Clay product UI (agent runs, sequencer flows, enrichment tables).
- **Testimonial / pricing-tier / pricing-tier-featured** — the featured
  pricing tier flips to the deep-teal brand color as its "featured" signal,
  rather than a colored ribbon.
- **Expert card** — avatar + name + specialization + "Book session" link,
  used on the /experts page.
- **Text input / text-input-focused** — cream fill with hairline border,
  border darkens to ink on focus.
- **Category tab / category tab-active** — pill-shaped sub-nav tabs.
- **Badge pill** — small cream-fill caption-size label.
- **CTA band (illustrated)** — pre-footer band pairing a display headline
  with a primary CTA and a 3D illustration.
- **Footer** — cream-tinted (never dark), 4-column link list, often
  closing with Clay's signature horizon-style mountain illustration.

## Do's and don'ts

**Do**
- Anchor every page on the cream canvas — the warm tint is what
  differentiates Clay from cool-gray data-platform competitors.
- Treat 3D claymation illustrations as hero artifacts; hand-crafted 3D
  characters and mountains ARE the brand.
- Cycle the saturated feature-card colors in sequence rather than
  repeating one back to back.
- Keep every display headline at Plain Black weight 500 with negative
  tracking.
- Show real product-UI fragments inside the saturated cards.
- Close pages on the cream footer, never a dark one.
- Hold the 96px section rhythm.

**Don't**
- Don't switch the canvas to cool gray.
- Don't add a seventh brand-color card — six is already saturated enough.
- Don't push display weight past 500.
- Don't repeat a brand-color card twice in a row.
- Don't replace the claymation illustrations with flat vector art.
- Don't use a dark footer.
- Don't invent hover styling beyond what the tokens already encode.

## Responsive behavior

| Breakpoint | Width | Key changes |
|---|---|---|
| Mobile | < 768px | Hamburger nav; hero h1 72→36px; illustration card stacks below copy; feature/pricing grids collapse to 1-up |
| Tablet | 768–1024px | Nav tightens; feature cards 2-up; pricing 2-up |
| Desktop | 1024–1440px | Full nav; 3-up feature cards; 3-up pricing |
| Wide | > 1440px | Same as desktop with more breathing room; content caps at 1280px |

Touch targets: primary buttons and text inputs sit at a 44×44px minimum
(WCAG AAA). Nav collapses to a hamburger below 768px; the hero's 7/5 grid
goes single-column; feature-card grids reduce columns rather than
shrinking; saturated cards keep their full-strength color fill at every
breakpoint; pricing tiers collapse 4 → 2 → 1.

## Known gaps

- Plain Black is licensed to Clay and unavailable as a public web font —
  Inter at weight 500 with negative tracking is the closest open
  substitute.
- The 3D claymation illustrations are commissioned per-page assets, not
  system tokens.
- The recurring named mascot characters are illustrated assets; their
  exact lineage isn't formalized here.
- Animation/transition timing (illustration parallax, card entrance) is
  out of scope.
- Form validation states beyond focus aren't captured.
- The logged-in Clay product surface (data tables, formula editor, agent
  builder) shares some tokens with marketing but adds many
  product-specific components not covered here.
