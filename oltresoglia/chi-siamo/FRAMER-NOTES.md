# Chi siamo (v5): Framer handoff

Prototype: `oltresoglia/chi-siamo/index.html` (`?coach=anna` opens on a given coach).
Built on the type system in `../TYPOGRAPHY.md` / `../styles/type.css`: every text layer is one of the 12 Text Styles below,
no detached text. All copy is verbatim from the "ABOUT US WEBSITE" Google Doc; the generator checks every line of Pietro's text is used once.
The site is Italian only. (The preview link has an IT / EN reading switch for review; it is not part of the design.)

**Concept: "Oltre la soglia".** A journey in four numbered steps (01 Da dove vengo · 02 Perché nasce · 03 Come lavoriamo · 04 Il team)
that ends at the threshold: the test. v5 is laid out on Sky's three references: KOS Visuals (hero face row), the "About Me"
portfolio (sticky portrait + tags, ruled rows, light page, left-aligned closing) and Sonora (numbered list, expanding team slices).

## Text Styles (create these 12 in Framer)

Fonts: Bounded (Black / Regular / ExtraLight) and Manrope (Light / Regular / Medium / SemiBold). Sizes per breakpoint, in px.

| Style | Font | Case | Desktop 1440 | Tablet 1024 | Phone 390 | Line height | Letter spacing | Colour |
|---|---|---|---|---|---|---|---|---|
| Display | Bounded Black | UPPER | 112 | 84 | 52 | 0.92 | -2% | Porcelain 100% |
| H1 | Bounded Black | UPPER | 64 | 52 | 36 | 1.0 | -1% | Porcelain 100% |
| H2 | Bounded Black | UPPER | 40 | 34 | 28 | 1.05 | 0 | Porcelain 100% |
| H3 | Bounded Regular | Sentence | 24 | 22 | 20 | 1.2 | 0 | Porcelain 100% |
| Statement | Bounded ExtraLight | Sentence | 48 | 40 | 30 | 1.1 | -1% | Porcelain 100% |
| Numeral | Bounded Black | — | 64 | 52 | 40 | 1.0 | -2% | Porcelain 100% |
| Eyebrow | Manrope Medium | UPPER | 11 | 11 | 11 | 1.4 | 14% | Porcelain 40% (Saffron above an H1) |
| Lead | Manrope Light | Sentence | 20 | 19 | 17 | 1.5 | 0 | Porcelain 64% |
| Body | Manrope Regular | Sentence | 16 | 16 | 16 | 1.6 | 0 | Porcelain 64% |
| Small | Manrope Regular | Sentence | 13 | 13 | 13 | 1.5 | 1% | Porcelain 40% |
| Button | Manrope SemiBold | UPPER | 13 | 13 | 13 | 1 | 12% | Saffron |
| Nav | Manrope Regular | Sentence | 14 | 14 | 14 | 1 | 0 | Porcelain 80% |

On the light Porcelain section the same opacities are taken from Dark Charcoal.
Note: the CSS prototype resolves Tablet slightly smaller than this table (see TYPOGRAPHY.md), and Numeral is 36 on Phone in the CSS
(= H1); the table above is the spec as written.

## Sections

| # | Section | Reference | Styles used | Build in Framer |
|---|---|---|---|---|
| 1 | Hero: "CHI SIAMO" (Display) left, Lead right; below, the six faces (Pietro + 5 coaches) in a row, each tilted −3° to +3° and offset up/down | KOS Visuals "Hey, great to meet you" | Display, Lead | Row of 6 frames (4:5, 6px radius), rotation per frame; hover straightens and lifts 16px. Phone: horizontal scroll with snap, 42vw cards |
| 2 | Founder: sticky portrait + tag pills "Biologo Nutrizionista" / "Fondatore" left; right Eyebrow 01 (Saffron), H2 "Pietro Vecchi", Lead, Body, then ruled rows 14 / 17 (Numeral + Eyebrow "anni"), Statement row, La direzione / Oggi (H3) | "About Me" (photo + tags, "My Process" rows) | Eyebrow, H2, Lead, Body, Numeral, Statement, H3, Nav (tags) | 2-column Stack; left column Sticky (top 112). Rows: 1px top border, 180px label column |
| 3 | Why (Porcelain ground): Eyebrow + Body, H1 "OLTRESOGLIA nasce da qui." with "da qui." on a Saffron marker, ruled H3 + Body | "About Me" light page | Eyebrow, Body, H1, H3 | Marker = Saffron fill behind the lower 32% of the phrase |
| 4 | How: sticky Eyebrow 03 (Saffron) + H1 "Al centro del percorso ci sei tu, non il programma." left; Lead, numbered list 01–04 (Small + H3 + artwork thumbnail) and mission right | Sonora "We provide various services" | Eyebrow, H1, Lead, Small, H3, Body | Two equal columns; list rows ruled; thumbnail zooms 12% on hover |
| 5 | Team: Eyebrow 04 + H1 "Il team"; five photo slices in original colour, the selected one 4× wider with Small "01 / 05" + H3 name; below, the bio (H3 + Small + arrows left, Lead + Body in two columns right) | Sonora "Professional team" | Eyebrow, H1, Small, H3, Lead, Body | Slices = component with 5 variants (one open), width transition 0.9s cubic-bezier(.76,0,.24,1) |
| 6 | Closing: Statement "Per chi pretende…" left-aligned on a hairline, Small "Pietro Vecchi · Fondatore" | "About Me" closing line | Statement, Small | — |
| 7 | Threshold CTA: Eyebrow "Il primo passo" (Saffron), H1, Button "Fai il test →" over the horizon artwork | — | Eyebrow, H1, Button | Same pill as the nav |

Header: nav links are pills; the current page has a 1px outline (from the "About Me" reference).

Spacing: section padding 160 / 96 / 72 (Desktop / Tablet / Phone); Eyebrow → heading 16; heading → Lead/Body 24 (Phone 16).

## Photos (in `assets/team/`)
- `pietro-hero.jpg` (3:4): hero arch · `pietro.jpg` (4:5): founder section
- `marco.jpg`, `anna.jpg`, `giulio.jpg`, `yuri.jpg`, `devid.jpg` (4:5): coach portraits
- Optional later: `pietro-scontornato.png`, Pietro cut out on a transparent background, to drop the arch in the hero

Photos are used in their original colours, as supplied (no grayscale, contrast or brightness changes). Before launch: the coach polos carry other brands' logos ("le 360"),
the backgrounds differ from shot to shot, Yuri's photo is lower resolution, and the Apple logo is visible on Pietro's laptop.

## Pending
- Logo SVG: the header wordmark is set in H3 until the logotype arrives (a logo is an image, not a text style).
- Bounded font files: until they're in `oltresoglia/fonts/`, Archivo stands in. Bounded is wider, so headings will grow in width.
