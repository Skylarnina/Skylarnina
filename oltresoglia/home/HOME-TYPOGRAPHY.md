# OLTRESOGLIA Home: text hierarchy across breakpoints

One Text Style per row. Breakpoints match the Framer file: **Desktop ≥ 1280**, **Tablet 810–1279**, **Phone < 810**.
Sizes are fixed per breakpoint (no fluid scaling), so they can be set exactly in Framer. In the prototype they are the
`--t-*` tokens at the top of `home/index.html`; every text on the page uses one of them.

| Style | Font | Weight | Desktop | Tablet | Phone | Line height | Letter spacing (em) | Case | Colour | Used for |
|---|---|---|---|---|---|---|---|---|---|---|
| **Display** | Bounded | Black 900 | 120 | 80 | 38 | 1.0 | -0.03em | UPPER | Outline only (1.5px yellow 55% / #3A3A3A on footer) | OLTRESOGLIA wordmark behind Pietro in the hero; footer wordmark |
| **H1** | Bounded | ExtraBold 800 | 40 | 36 | 30 | 1.1 | -0.015em | Sentence | White; last line yellow | Hero headline (one per page) |
| **H2** | Bounded | ExtraBold 800 | 36 | 30 | 26 | 1.12 | -0.01em | Sentence | Charcoal on light, white on dark | Section titles; the "Il fisico che avevi…" band |
| **Statement** | Bounded | Light 300 | 30 | 26 | 22 | 1.25 | -0.01em | Sentence | Charcoal on yellow | The credo sentence (yellow card) |
| **H3** | Bounded | Bold 700 | 22 | 20 | 19 | 1.25 | 0em | Sentence | Charcoal / white | Card and step titles, phase names, plan titles, kg results (800), "Se ti riconosci…" |
| **H4** | Bounded | Bold 700 | 17 | 16 | 16 | 1.25 | 0em | Sentence | Charcoal / white | Names on cards (team, videos, Pietro), "Vuoi saperne di più?", +500 chip, 01–03 badges (800) |
| **Numeral L** | Bounded | ExtraBold 800 / Black 900 | 56 | 44 | 40 | 1.0 | -0.02em | — | Charcoal; outline on the Come funziona rows | Numbers row (+500, +10 anni, 100%); 01–03 in Come funziona |
| **Numeral XL** | Bounded | Black 900 | 92 | 80 | 64 | 0.82 | -0.04em | — | Charcoal on yellow | 100% in the guarantee card |
| **Logo** | Bounded | ExtraBold 800 Italic | 20 | 18 | 17 | 1.0 | 0.08em | UPPER | White | Wordmark in the nav (17 in the sticky bar and phone menu) until the logo SVG is in |
| **Menu link** | Bounded | Bold 700 | 24 | 24 | 24 | 1.1 | -0.01em | Sentence | White; current page yellow | Links in the phone/tablet menu |
| **Caption caps** | Bounded | ExtraBold 800 | 13 | 13 | 13 | 1.25 | 0em | UPPER | White on video | Title over the video thumbnails |
| **Eyebrow** | Manrope | SemiBold 600 | 13 | 13 | 12 | 1.3 | 0.16em | UPPER | Gold #8A5A00 on light, yellow on dark | Small label above each section title |
| **Lead** | Manrope | Regular 400 | 20 | 18 | 17 | 1.55 | 0em | Sentence | Charcoal 80% / #BDB8AE on dark | Intro paragraphs (hero, credo, team), the four week types |
| **Body L** | Manrope | Bold 700 | 18 | 17 | 16 | 1.5 | 0em | Sentence | White | The bold hero sentence |
| **Body** | Manrope | Regular 400 (bold leads 700) | 16 | 16 | 15 | 1.6 | 0em | Sentence | Charcoal 70% / #BDB8AE on dark | All running text: cards, steps, phases, comparison, lists, guarantee, note |
| **Small** | Manrope | Medium 500 | 13 | 13 | 13 | 1.45 | 0em | Sentence | #8C877E | Stat labels, captions under names, "Test immediato · meno di 2'", footer line |
| **Label** | Manrope | Bold 700 | 12 | 12 | 11 | 1.0 | 0.12em (caps only) | UPPER or Sentence | Gold / grey / charcoal on yellow pill | PRIMA / DOPO, FASE 1:, RIMBORSO, pills ("in 8 mesi"), menu numbers, photo-slot labels |
| **Button** | Manrope | Bold 700 | 15 | 15 | 14 | 1.2 | 0em | Sentence | Charcoal on yellow | Yellow buttons (14 in the nav and sticky bar) |
| **Button caps** | Manrope | Bold 700 | 13 | 13 | 12 | 1.2 | 0.1em | UPPER | Yellow on black | Outline and black buttons |
| **Nav** | Manrope | Medium 500 | 15 | 15 | 15 | 1.0 | 0em | Sentence | #E8E4DC; current yellow + 2px underline | Navbar links (14 in the sticky bar and footer) |

## Rules

- One H1 per page (the hero). Every section title is H2; nothing between H2 and H3.
- Sentence case for all titles (as in the Figma file); UPPERCASE only for Eyebrow, Label, Button caps, Caption caps and the wordmarks.
- Bounded for titles, numbers and names; Manrope for everything you read in sentences, labels and buttons.
- Bold leads inside Body (e.g. "**Solo pesi o solo cardio.** Ti rendono…") stay Body size, weight 700.
- Line length: Lead and Body max ~60 characters per line on desktop.
- Wordmarks are decorative outlines (aria-hidden); the real logo SVG replaces the Logo style when it arrives.

## Framer setup

1. Create the 20 Text Styles above (Assets → Text Styles), each with three breakpoint sizes. Set letter spacing in **em** (in Framer, switch the unit to em), so it scales with the size at every breakpoint.
2. Name them exactly as in the table, so they match this document and the prototype tokens.
3. Colours are separate colour styles (already set up in Framer); apply them per use, not inside the text style.
