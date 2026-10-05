# Chi siamo: Framer handoff

Prototype: `oltresoglia/chi-siamo/index.html` (add `?bio=aperte` to open every bio).
Uses the same styles as the Contact page after client feedback round 1. Colour, text, radius and button
styles are listed in `../contact/FRAMER-NOTES.md`; only what is new here is below.

## Layout (client reference: two-column grid of coach cards)

1. **Header**: same as Contact. Nav adds **Chi siamo** (between Programma and Guide), marked as the
   current page with a 2px Saffron underline.
2. **Intro**: eyebrow "Chi siamo" (Saffron) → headline "Le persone" (Bounded ExtraLight) /
   "dietro OLTRESOGLIA." (Bounded Black), 56px, mobile 40px → intro line placeholder (text pending from Pietro).
3. **Team**: a 2-column grid, gap 32, cards in a row share their height. With an odd number of coaches the
   last card is centred at half width. Below 840px: one column, gap 24.
4. **Footer**: pending homepage.

## Coach card (make it a Framer component; CMS-ready)

| Part | Spec |
| --- | --- |
| Card | fill Banner Grey `#232526`, 1px border Porcelain 14%, radius 16, padding 40 / 40 / 32 (mobile 32 / 24 / 24) |
| Photo | circle, 240px (max 72% of card width), centred; image fill, cover. Placeholder: Porcelain 10% on Charcoal with initials |
| Name plate | overlaps the photo by 28px; fill Porcelain `#EBF0F2`, text Dark Charcoal, Bounded Black, 21px (mobile 17), UPPER, 0.06em, radius 12, padding 14 × 20, max width 340 |
| Bio | Manrope 400, 16 / 26, Porcelain 85%; paragraph gap 14; margin-top 28 |
| "Leggi tutta la storia" | Manrope 600 15px, Saffron, underlined, chevron 16px; toggles to "Riduci". Shows the first 2 paragraphs, the rest expands in place |

Suggested CMS collection "Team" (fits Basic's 2-collection limit together with Guide):
`nome` (text), `foto` (image), `anteprima` (formatted text: first 2 paragraphs), `storia` (formatted text: the rest), `ordine` (number).

Coach order (as in `chi_siamo.pdf`): Marco Saponaro, Devid Cresta, Yuri, Anna, Giulio.

## Pending
Five portraits (square, ideally on a plain light background like the reference) · intro text · headline approval ·
copy review points listed in the handoff message (banned words, typos).
