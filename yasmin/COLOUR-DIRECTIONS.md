# Colour directions

## Start here: Collection (the colours in her own photographs)

The earlier directions borrowed their colours from outside Yasmin: The Henry Ford's wayfinding colours on her business card, a cream and a wine from the Figma file, a mockup. **Collection** takes every colour from her own pictures instead: her portrait and the 21 photographs in *Snippets About My Life*, sampled with median-cut (`screenshots/her-colours.png` shows each photo next to the colours taken from it; source `brand/her-colours.html`).

What the photographs hold: linen and stone walls and plinths, walnut and espresso wood and frames, brass fittings, and **one strong colour, oxblood**, which recurs in the crown, the textiles, the Violins of Hope case and the diorama. It is very close to the Figma wine, so her instinct for wine was right; the photographs just set its exact shade. The card's orange, olive and light blue barely appear in them at all.

| Role | Colour | Where it comes from | Where it goes |
|---|---|---|---|
| Ground | linen `#F2EDE5` | gallery walls, the portrait backdrop | every section not listed below |
| Ground 2 | sand `#E6DDD0` | plinths, stone, paper labels | Snippets, Reflection, logo tiles |
| Ink | espresso `#2A1C1B` | dark wood, frames, the crown's shadows | all text, rules; 58% layer over the four discipline photos |
| Band | walnut `#3A2924` | the column installation, display cases | Contact only (linen text) |
| Accent | oxblood `#8E3A2F` | the crown, textiles, the violin case | "Yasmin.", links, project numbers, chapter numbers, Enter |
| Detail | brass `#C9A46A` | fittings, gilt frames | link underlines on the walnut band only |

**Share of the page:** linen ~72% · sand ~12% · espresso ~12% · walnut ~3% · oxblood ~1%.
**Never:** a second strong colour; oxblood as a section ground; brass as text on linen (it fails contrast there); recolouring the photographs (the panels keep full colour under the espresso layer).
**Contrast:** every text item passes 4.5:1 on the rendered pages at 1440 and 390 (worst 5.04:1); values in `THEMES.md`.
**See it:** the switcher's first option, **Collection**, or any page with `?theme=collection`.

**In Squarespace** (the cheapest direction to build): palette = the five colours above minus brass (`#F2EDE5` `#E6DDD0` `#2A1C1B` `#3A2924` `#8E3A2F`); three section themes: linen (most sections), sand (Snippets, Reflection), walnut (Contact). Links and the project numbers take oxblood from the palette natively. The base custom CSS keeps its 19 lines with new values: the hairlines and 62% greys become espresso, the lock-screen Enter becomes oxblood, the logo tiles sand; the two panel lines darken with an espresso layer instead of black (same two lines). The brass underline on Contact is optional (+1 line). **19–20 lines**, the only direction with room to spare under the 30-line budget. Full table: SQUARESPACE-BUILD-NOTES.md, *Site Styles per theme*.

**Why I recommend it:** it needs no explanation to Yasmin. She can look at the board and see her own work in the palette, and none of the colours compete with the photographs because they *are* the photographs.

---

## Three earlier directions: cream, wine and The Henry Ford's colours

Three distinct directions for the same site (same layout, copy and photographs), so Yasmin chooses a **mood**, not a swatch. Each gives the same colours different jobs.

| | **Archive** | **Salon** | **Campus** |
|---|---|---|---|
| Idea | The museum label: quiet paper, navy type; the card's colours only tell you which project you're in | Yasmin's own room: wine is her voice and fills the sections that are about her | The business card as a map: soft venue tints section by section, each project on its own tint |
| Lead colour | Navy | Wine | The card (orange, olive, red, light blue, navy) |
| Feels | Calm, scholarly, gallery | Warm, personal, confident | Colourful, optimistic, still premium |
| Best if she wants | The work to carry all the colour | The site to feel like *her* | The site to feel like The Henry Ford's world |

- **See them:** the prototype's theme switcher, top-right (**Collection · Archive · Salon · Campus**; Mono is the uncoloured build; *Earlier* holds the previous rounds). Or open any page with `?theme=heritage` (Archive), `?theme=salon` or `?theme=campus`.
- **Usage guide** (one board, section-by-section colour map for each): `screenshots/colour-directions.png`, also `brand/colour-directions.html`.
- **Values and contrast:** `THEMES.md`. Every piece of text in all three passes 4.5:1, checked on the rendered pages at desktop and phone widths, text on photos included.

---

## Constant in all three (never changes)

| Element | Colour | Rule |
|---|---|---|
| Page ground | paper `#F3F0EA` | The default for every section that isn't listed below |
| "Yasmin." in the hero | wine `#8C2F1E` | Her name is always wine: the one thread through every direction |
| Project colours (wayfinding) | 01 Jackson Home **olive** · 02 Power & Energy **orange** · 03 Rhode Island **light blue** · 04 Littelfuse **red** | Chosen by venue, not taste: Greenfield Village, the Museum, research (Benson Ford), engineering (the Rouge) |
| Project marks | fills `#8A8D4F` `#E9A35B` `#6E94AB` `#B04A44`; text `#63653A` `#8E5412` `#48677A` `#A8443F` | Fills only for 3px bars, tints and the five-colour rule; the text values for project numbers and case-study chapter / FIG. numbers |
| Five-colour rule | orange · olive · red · light blue · navy, 3px | Once, over the project list: the legend for the project colours |
| Photographs | never recoloured | The discipline panels get one flat layer for legibility, nothing else |
| Type | Instrument Serif + Inter Tight | Colour never replaces hierarchy; headings stay the ink colour |

---

## Archive (navy-led)

**Palette:** paper `#F3F0EA` · paper 2 `#E9E4DB` · ink `#1C2635` (navy-black) · navy `#1E3F63` · wine `#8C2F1E`.
**Share of the page:** paper ~74% · ink ~16% · navy band ~7% · wine ~2% · venue colours ~1%.

| Section | Ground | Text | Accents |
|---|---|---|---|
| Header | paper | ink | current page underlined in wine |
| Hero | paper | ink | "Yasmin." wine; button outline ink |
| Snippets About My Life | paper 2 `#E9E4DB` | ink | none |
| Four disciplines | photos under navy-ink `#1C2635` at 60% | white | none |
| Projects | paper | ink | five-colour rule over the list; 3px venue bar beside each row; numbers in the venue text colour; "Password protected" wine |
| Contact | **navy `#1E3F63`** | cream `#F3F0EA` | link underlines orange `#E9A35B` |
| Footer | paper | ink 68% | none |
| Case: cover (01, 02) | photo under navy-ink 60% | cream title | none |
| Case: header (03, 04), meta, chapters | paper | ink | chapter, index and FIG. numbers in the project colour |
| Case: Reflection | paper 2 | ink | none |
| Lock screen | paper | ink | Enter button wine |

**Never:** a second coloured band; venue colours as fills or large text; wine on anything but Yasmin's marks.

## Salon (wine-led)

**Palette:** paper `#F3F0EA` · paper 2 `#E9E4DB` · warm ink `#16140F` · wine `#8C2F1E` · cream on wine `#F3F0EA`.
**Share of the page:** paper ~68% · wine ~17% · warm ink ~14% · venue colours ~1%.

| Section | Ground | Text | Accents |
|---|---|---|---|
| Header | paper | warm ink | |
| Hero | paper | warm ink | "Yasmin." wine |
| Snippets About My Life | **wine `#8C2F1E`** | cream | the slideshow on a 12px cream frame (a picture hung on a wine wall) |
| Four disciplines | photos under warm ink `#16140F` at 60% | white | |
| Projects | paper | warm ink | rule, 3px bars and numbers as Archive |
| Contact | paper 2 `#E9E4DB` | warm ink | wine link underlines |
| Footer | paper | warm ink 64% | |
| Case: cover | photo under warm ink 60% | cream title | |
| Case: chapters | paper | warm ink | project-colour numbers |
| Case: Reflection | **wine** | cream italic | her reflection in her colour |
| Lock screen | **wine** | cream | the form on a paper card; Enter wine |

**Never:** wine on the work itself (case-study chapters, figures, project rows stay paper). Wine and the card red never touch: red is only Littelfuse's 3px bar and number.

## Campus (the card leads, as tints)

**Palette:** paper `#F3F0EA` · orange tint `#F1E4D3` · olive tint `#E2E0D1` · row tints `#E6E4D7` (olive) `#F2E7D9` (orange) `#E3E5E2` (light blue) `#EBDCD6` (red) · ink `#1C2635` · navy `#1E3F63` · wine (her name only).
**Share of the page:** paper ~40% · venue tints ~34% · ink ~14% · navy ~8% · venue colours ~3% · wine ~1%.

| Section | Ground | Text | Accents |
|---|---|---|---|
| Header | paper | ink | |
| Hero | **orange tint `#F1E4D3`** | ink | "Yasmin." wine |
| Snippets About My Life | **olive tint `#E2E0D1`** | ink | |
| Four disciplines | photos (darkened) under **orange · olive · red · light blue at 55%**, one per panel | white | the strongest colour on the page |
| Projects | each row on **its venue tint** (12%), full width | ink | the logo plate on paper; the rule over the list; numbers in the venue text colour |
| Contact | **navy `#1E3F63`** | cream | the card ends navy |
| Footer | paper | ink 68% | |
| Case: cover | photo under navy-ink 60% | cream title | |
| Case: chapter index | paper | ink | a 3px rule in the project's colour on top |
| Case: Reflection | the project's tint | ink | |
| Lock screen | light-blue tint `#DEE1E0` | ink | Enter navy |

**Never:** full-strength venue colours as section grounds (that was the mockup's problem); tints above 16%; more than one tint per section. Navy is the accent here (links, Enter); wine is only her name.

---

## From the ChatGPT mockup

**Kept:** cream paper, navy, olive, a colour per project, the five-colour rule (all three directions use them in different amounts).

**Dropped:**
- The site title "Henry Ford Museum". It is Yasmin's portfolio and stays **Yasmin Bajwa**; naming it after her employer would misrepresent whose site it is.
- Four full-strength bands at once (orange header, olive, navy, red footer) plus swooshes, colour-washed photos, paper texture and a script font.
- The orange "Yasmin." at 2.5:1 on cream, which fails contrast. Her name is wine in every direction (7.3:1).
- Its edits to her copy ("USA", "UI Research", the discipline names, the new "Beyond the work" text, the footer tagline). If that text is new copy from her, it can be added separately.

## In Squarespace

The three directions use the same blocks; only section themes and a few colour values differ. Settings per direction are in SQUARESPACE-BUILD-NOTES.md (*Site Styles per theme*).

| | Archive | Salon | Campus |
|---|---|---|---|
| Palette (5 slots) | `#F3F0EA` `#E9E4DB` `#1C2635` `#1E3F63` `#8C2F1E` | `#F3F0EA` `#E9E4DB` `#16140F` `#8C2F1E` + a free slot | `#F3F0EA` `#1C2635` `#1E3F63` `#8C2F1E` + one tint; the other tints need CSS or section-theme custom colours (**verify**) |
| Coloured section themes | Navy (Contact) | Wine (Snippets, Reflection) | Orange tint (hero), olive tint (Snippets), navy (Contact) |
| Extra CSS beyond the base 19 lines | ~9 (panel layer, row bars, project numbers, link underline) | ~9 (as Archive + slideshow frame, lock ground) | ~15 (panel colours ×4, row tints ×4, project numbers): **over the 30-line budget** unless the row tints are Shape blocks behind each row |

**My recommendation:** **Collection** (above). Of these three: **Archive** if the client wants the work to lead; **Salon** if she wants the site to feel personal. Campus is the most distinctive but the most expensive to build and maintain in Squarespace.
