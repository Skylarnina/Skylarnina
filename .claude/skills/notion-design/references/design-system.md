# Notion Design System — Full Analysis

Adapted from the Notion design analysis in
[voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(`design-md/notion/DESIGN.md`, MIT License). Token names below refer to
`references/design-tokens.yaml` in this skill.

## Overview

Notion presents itself as the all-in-one workspace through a confident,
illustration-rich brand voice. The homepage opens with "Meet the night
shift." centered over a deep navy hero band (`colors.brand-navy`), decorated
with scattered brand-colored sticky-note dots and mesh-wire illustrations
around the headline. The signature purple pill primary CTA
(`colors.primary`) "Get Notion free" sits at the visual center, paired with
an outlined "Request a demo" secondary action. Below the buttons, a real
Notion workspace UI mockup card — the "Ramp HQ" kanban board — breaks out of
the hero band with a deep diffuse drop shadow.

Beneath the hero, the page cycles through a distinctive sequence of feature
sections: a dense sticky-note "Keep work moving 24/7" panel carrying
red/blue/green/purple/teal status icons; a bold yellow
(`colors.card-tint-yellow-bold`) "Ask your on-demand assistants" banner
flanked by orange/rose/mint pastel tiles showing assistant UI mockups; and a
"Bring all your work together" three-column grid with brand-colored mockups
(a sky-blue tutorial card, a light Notion calendar, a brown/rust testimonial
slate). The pricing page lays out four tiers — Free, Plus, Business,
Enterprise — horizontally, one tier featured with a purple border, sitting
above a dense feature-comparison table.

The whole system runs on Notion Sans (an Inter-based typeface) across every
surface — humanist-geometric character that pairs naturally with the
colorful illustrations. Buttons round to `rounded.md` (8px) rectangles, NOT
pills, distinguishing Notion's sober rectangular geometry from competitors
that default to pills everywhere. Cards consistently use `rounded.lg`
(12px).

**Key characteristics:**
- Deep navy hero band (`colors.brand-navy`) with scattered sticky-note dot
  and mesh-wire decorative illustrations.
- Signature purple pill (`colors.primary`) primary CTA — Notion's
  recognizable "Get Notion free" button color.
- A real Notion workspace UI mockup card embedded in the hero with a deep
  drop shadow.
- Bold yellow feature banner (`colors.card-tint-yellow-bold`) for
  high-emphasis content sections.
- Pastel feature-card palette (peach, rose, mint, lavender, sky, yellow)
  echoing the live product's database properties.
- Notion Sans (Inter-based) across every UI surface.
- 8px-rounded buttons (never pill), 12px-rounded cards — sober editorial
  geometry.
- Four-tier pricing comparison with a dense feature table.
- Centered hero layout, a departure from the left-aligned norm of most B2B
  SaaS marketing pages.

## Colors

> Source pages: notion.com (homepage), /enterprise, /product/ai,
> /product/agents, /startups, /pricing. Token coverage was identical across
> all six pages.

### Brand & primary
- **Notion Purple** (`colors.primary`): the signature primary-CTA color —
  the unmistakable "Get Notion free" pill. Reserved for the dominant CTA
  only.
- **Purple Pressed** (`colors.primary-pressed`) / **Purple Deep**
  (`colors.primary-deep`): pressed and emphasis variants.
- **Brand Navy** (`colors.brand-navy`): the hero band background.
- **Brand Navy Deep** (`colors.brand-navy-deep`) / **Brand Navy Mid**
  (`colors.brand-navy-mid`): deeper and mid-spectrum navy for the promo
  banner and secondary dark surfaces.
- **Link Blue** (`colors.link-blue`): inline text-link blue — explicitly NOT
  the primary CTA color.
- **Link Blue Pressed** (`colors.link-blue-pressed`): pressed-state link
  blue.

### Brand color spectrum (echoes live product database properties)
- **Brand Pink** / **Brand Pink Deep**, **Brand Orange** / **Brand Orange
  Deep**, **Brand Purple** / **Brand Purple 300** / **Brand Purple 800**,
  **Brand Teal**, **Brand Green**, **Brand Yellow**, **Brand Brown** — the
  wider color spectrum that echoes Notion's own colorful database property
  tags.

### Card tints (pastel feature-card backgrounds)
- **Tint Peach**, **Tint Rose**, **Tint Mint**, **Tint Lavender**, **Tint
  Sky**, **Tint Yellow**, **Tint Yellow Bold** (the bold high-emphasis
  banner tint used for "Ask your on-demand assistants"), **Tint Cream**,
  **Tint Gray** (neutral surface).

### Surface
- **Canvas White** (`colors.canvas`): page background and primary card
  surface.
- **Surface** (`colors.surface`): subtle section backgrounds, search-pill
  rest state, featured pricing tier.
- **Surface Soft** (`colors.surface-soft`): quieter section divisions.
- **Hairline** / **Hairline Soft** / **Hairline Strong**: dividers and
  borders at three strengths.

### Text
- **Ink Deep** (pure black for emphasis), **Ink** (primary headlines and
  body), **Charcoal** (Notion's signature warm-charcoal body emphasis),
  **Slate** (secondary), **Steel** (tertiary/footer links), **Stone**
  (muted labels), **Muted** (disabled/placeholder), **On Dark** / **On Dark
  Muted** (white text and reduced-opacity white on dark surfaces).

### Semantic
- **Success** (confirmation green), **Warning** (mid-priority orange),
  **Error** (validation red).

## Typography

### Font family
**Notion Sans** — Notion's custom Inter-based variable typeface, falling
back to Inter, -apple-system, system-ui, Segoe UI, Helvetica, sans-serif.
Humanist-geometric character used across every UI surface.

### Hierarchy
See `design-tokens.yaml → typography` for the full scale (hero-display 80px
down to button-md 14px). Principles:
- Tight hero leading (1.05) on the 80px display size.
- Negative letter-spacing on display sizes, from -2px down to -0.5px.
- Generous body leading (1.55) for documentation-style readability.
- Weight 600 headlines paired with weight 500 buttons and weight 400 body.

## Layout

### Spacing system
- Base unit: 4px, with 8px as the primary increment.
- Tokens run from `spacing.xxs` (4px) through `spacing.hero` (120px).
- Section rhythm: marketing pages use `spacing.section-lg` (96px); pricing
  tightens to `spacing.section` (64px).

### Grid & container
- 1280px max-width with 32px gutters.
- Pricing: a four-tier card row at desktop with a dense comparison table
  beneath it.
- Homepage: a centered hero with the workspace mockup below the buttons,
  followed by alternating colorful feature-card sections.

### Whitespace philosophy
Marketing surfaces use generous breathing room between feature-card bands.
The hero's workspace mockup card gets full-width treatment with a deep drop
shadow, standing apart from the otherwise flat-bordered card system.

## Elevation & depth

| Level | Treatment | Use |
|---|---|---|
| 0 (flat) | No shadow; hairline border | Default cards, table rows |
| 1 (subtle) | `rgba(15,15,15,0.04) 0px 1px 2px 0px` | Hover-elevated tiles |
| 2 (card) | `rgba(15,15,15,0.08) 0px 4px 12px 0px` | Feature cards |
| 3 (mockup) | `rgba(15,15,15,0.20) 0px 24px 48px -8px` | Hero workspace mockup card |
| 4 (modal) | `rgba(15,15,15,0.16) 0px 16px 48px -8px` | Modals, dropdowns |

The hero workspace mockup card carries the deepest, most diffuse shadow in
the system, giving it visible lift against the navy band. Pastel feature
cards carry their own visual weight through tint backgrounds rather than
shadow. Sticky-note dot illustrations and mesh wires add atmospheric
decoration to the navy hero.

## Shapes

| Token | Value | Use |
|---|---|---|
| rounded.xs | 4px | Tag chips |
| rounded.sm | 6px | Type badges |
| rounded.md | 8px | Buttons, inputs, search-pill |
| rounded.lg | 12px | Cards, pricing tiers, agent tiles, workspace mockup |
| rounded.xl | 16px | Larger feature panels |
| rounded.xxl | 20px | Featured product showcases |
| rounded.xxxl | 24px | Larger feature cards |
| rounded.full | 9999px | Status badges, pill tabs (NOT regular buttons) |

Notion's geometry is sober-editorial — 8px-radius buttons are what
distinguish it from brands that default to pills everywhere.

## Components

Definitions live in `design-tokens.yaml → components`. Summary:
- **Buttons** — `button-primary` (purple, rectangular), `button-dark`
  (black rectangular CTA), `button-secondary` (outlined), `button-on-dark` /
  `button-secondary-on-dark` (for the navy hero), `button-ghost`,
  `button-link` (inline blue text link, distinct from the purple CTA).
- **Cards & containers** — `card-base`, `card-feature` and its seven pastel
  tint variants (peach/rose/mint/sky/lavender/yellow/yellow-bold/cream),
  `card-agent-tile`, `card-template`, `card-startup-perk`, `pricing-card` /
  `pricing-card-featured` (purple-bordered).
- **Inputs & forms** — `text-input` / `text-input-focused` (border switches
  to purple), `search-pill`.
- **Tabs** — `pill-tab` / `pill-tab-active` (fully rounded), `segmented-tab`
  / `segmented-tab-active` (underline style).
- **Badges & status** — `badge-purple`, `badge-pink`, `badge-orange`,
  soft-tint `badge-tag-*` chips, `badge-popular`, `promo-banner`.
- **Tables** — `comparison-table`, `comparison-row`.
- **Documentation & signature components** — `workspace-mockup-card` (the
  embedded product-UI mockup), `testimonial-card`, `logo-wall-item`,
  `faq-accordion-item`, `stat-row`, `cta-banner-light`.
- **Navigation & footer** — sticky white top nav with logo, nav links,
  purple "Get Notion free" button, and a "Log in" link; `hero-band-dark`
  (the signature navy hero with mockup and decorative dots); `footer-region`
  (6-column link grid); `footer-link`.

## Do's and don'ts

**Do**
- Use purple as the dominant CTA across every surface — it's the brand's
  recognizable signal.
- Pair deep navy hero bands with the purple button plus decorative
  sticky-note dots.
- Use pastel feature-card tints (peach, rose, mint, lavender, sky, yellow)
  generously.
- Use the bold-yellow tint for high-emphasis "Ask the assistant"-style
  banner cards.
- Apply 8px radius to buttons consistently — Notion uses rectangles, not
  pills.
- Apply 12px radius to all card families.
- Maintain Notion Sans across every UI surface.
- Use a workspace mockup card on hero bands to show real product UI.

**Don't**
- Don't use purple for body text or large background surfaces.
- Don't use pill-shaped buttons; Notion's geometry is rectangular-sober.
- Don't mix link-blue with primary-purple — they have distinct roles.
- Don't apply heavy shadows to flat documentation cards.
- Don't replace Notion Sans with a generic, unmodified Inter.

## Responsive behavior

| Name | Width | Key changes |
|---|---|---|
| Mobile (small) | < 480px | Single column. Hero 36px. Pricing 1-up. |
| Mobile (large) | 480–767px | Feature cards 2-up. Hero 48px. |
| Tablet | 768–1023px | 2-column feature grids. Hero 56px. |
| Desktop | 1024–1279px | 4-tier pricing card row. Hero 72px. |
| Wide Desktop | ≥ 1280px | Full 80px hero presentation. |

Buttons render at 40–44px effective height; form inputs at 44px; pill tabs
grow from ~32px to 44px on mobile.

Collapsing strategy: the promo banner truncates below 480px; the top nav
collapses to a hamburger below 1024px; the hero's workspace mockup card
moves below the text/buttons on mobile; pricing tiers go 4→2→1 columns;
feature cards go 3→2→1; hero typography steps 80→56→48→36px; the footer
goes 6-column → 3-column → accordion.

## Known gaps

- Specific dark-mode token values weren't surfaced beyond the hero bands.
- Animation/transition timings weren't extracted; 150–200ms ease is a
  reasonable default.
- Form validation success state wasn't explicitly captured.
- The pastel-tint-to-feature mapping (which section uses which tint) is
  observation-based — the actual brand library may include more entries.
