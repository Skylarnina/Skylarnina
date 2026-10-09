# Chi siamo (v4): Framer handoff

Prototype: `oltresoglia/chi-siamo/index.html` (`?coach=anna` opens on a given coach).
Built on the type system in `../TYPOGRAPHY.md` / `../styles/type.css`: every text layer is one of the 12 Text Styles below,
no detached text. All copy is verbatim from the "ABOUT US WEBSITE" Google Doc; the generator checks every line of Pietro's text is used once.
The site is Italian only. (The preview link has an IT / EN reading switch for review; it is not part of the design.)

**Concept: "Oltre la soglia".** A journey in four numbered steps (01 Da dove vengo · 02 Perché nasce · 03 Come lavoriamo · 04 Il team)
that ends at the threshold: the test. In the hero the arch is a doorway standing on the horizon line.

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

| # | Section | Styles used | Build in Framer |
|---|---|---|---|
| 1 | Hero: "CHI SIAMO" (Display) on the horizon line, Pietro in an arch standing on the same line and covering the last letter; below the line Eyebrow "01 · Da dove vengo" (Saffron) + Lead | Display, Eyebrow, Lead | Stack: wordmark (z 0) → arch-masked image (z 1), both bottom-aligned to a 1px line. Arch x = wordmark x + 5 × Display size. Scroll transform: arch moves up ~8% faster than the word |
| 2 | Founder: portrait + Small caption; H2 "Pietro Vecchi", Lead, Body; timeline 14 / 17 (Numeral + Eyebrow "anni"), Statement "Ho vissuto entrambi gli estremi.", La direzione / Oggi (H3) | H2, Lead, Body, Numeral, Eyebrow, Statement, H3, Small | 2-column Stack; timeline = vertical Stack with a 1px line and saffron-ring dots |
| 3 | Why (Porcelain ground): Eyebrow + Body, H1 "OLTRESOGLIA nasce da qui." with "da qui." on a Saffron marker, H3 + Body | Eyebrow, Body, H1, H3 | Marker = Saffron fill behind the lower 32% of the phrase |
| 4 | How: Eyebrow + Lead; four strips with H3 left and Small index right, profile artwork on the right 62% fading in; H1 "Al centro del percorso ci sei tu, non il programma." ("ci sei tu," Saffron); mission Eyebrow + Body | Eyebrow, Lead, H3, Small, H1, Body | Strip hover zooms the artwork 6% over 1.1s |
| 5 | Team: Eyebrow "04" + H2 "Il team"; depth carousel (card label H3 + Small); name tabs (H3); panel H3 + Small + Lead + Body in two columns | Eyebrow, H2, H3, Small, Lead, Body | Carousel = component with 5 variants, transition 1s cubic-bezier(.76,0,.24,1); tabs and arrows switch variants |
| 6 | Closing line "Per chi pretende…" + Small "Pietro Vecchi · Fondatore" | Statement, Small | Centred |
| 7 | Threshold CTA: Eyebrow "Il primo passo" (Saffron), H1, Button "Fai il test →" | Eyebrow, H1, Button | Same pill as the nav |

Spacing: section padding 160 / 96 / 72 (Desktop / Tablet / Phone); Eyebrow → heading 16; heading → Lead/Body 24 (Phone 16).

## Photos (in `assets/team/`)
- `pietro-hero.jpg` (3:4): hero arch · `pietro.jpg` (4:5): founder section
- `marco.jpg`, `anna.jpg`, `giulio.jpg`, `yuri.jpg`, `devid.jpg` (4:5): coach portraits
- Optional later: `pietro-scontornato.png`, Pietro cut out on a transparent background, to drop the arch in the hero

All photos are shown in grayscale so the set reads as one shoot. Before launch: the coach polos carry other brands' logos ("le 360"),
the backgrounds differ from shot to shot, Yuri's photo is lower resolution, and the Apple logo is visible on Pietro's laptop.

## Pending
- Logo SVG: the header wordmark is set in H3 until the logotype arrives (a logo is an image, not a text style).
- Bounded font files: until they're in `oltresoglia/fonts/`, Archivo stands in. Bounded is wider, so headings will grow in width.
