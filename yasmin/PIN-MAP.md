# Pin map: where every layout comes from

Each section takes the **composition** of one pin from `design-references/`: placement, scale, layering and cropping. It never takes the pin's colours, fonts or subject matter. Every section also names its pin in an HTML comment (`<!-- P6 (itinerary …) -->`), so the source is visible in the code.

| # | Pin file | Short name |
|---|---|---|
| P1 | `0cfc662a1adcb1220185755eddb90b9e.png` | "Booked": a card floating over a soft scene |
| P2 | `10fd2117bcb25f2e5d635d4a4cbb8761.png` | Travel Hub: tall pill windows over one background |
| P3 | `47642dd926565b4780a6f457c22e44e9.png` | "Fillory": dark 3D carousel, framed active card |
| P4 | `4e61e93ef13c61eaa1702fcd92ac87f3.png` | EAT / HIKE / CAMP: stacked photo strips |
| P5 | `507072b563ee36384addcbe4c7bd18fa.png` | "ADVENTURE": giant word behind the subject, 01–04 index |
| P6 | `64dd18ab2fc338bdba99765ade163764.png` | "JAPAN": tall mini-cards, itinerary with photos on a line |
| P7 | `80a4eac65812643926da3f9278cbd504.png` | "Choose a Destination": pill switcher, centre card, peeking sides |
| P8 | `92d6f77ccb7aa414d42b799a109d3f31.png` | "NÔR": wide-tracked serif, spaced caps, short hairline |
| P9 | `a29587d37b16c5733ada37612b10280c.png` | "Country Harmony": overlapping thin circles, numbered 01–04 |
| P10 | `c0e1501be1035a59719f1c48bbed9e11.png` | "One Last Flight": stacked headline, one word in accent, meta line |
| P11 | `ce9fa9655cb5abbc7e40dbea6e275931.png` | Nexetrip: cards floating over a full-bleed landscape |
| P12 | `f5049d576c1c03cc1ce79fe8ff835b37.png` | "Visit Tokyo": big caps left, 01–05 index right, dark video section |

## Homepage: `site/index.html`

| Section | Pin(s) | What was taken | What changed for Yasmin |
|---|---|---|---|
| 1. Hero | **P5 + P8** | P5: one giant word across the full width, with the subject standing in front of its lower half, and a thin 01–04 index at the edge. P8: spaced caps, a short hairline and a small paragraph beneath. | The word is YASMIN (Instrument Serif, 22vw, tracked 0.12em) on the black box, with her cut-out headshot in front. The index lists the four rooms and links to them. CTA pill: "View Projects →". |
| 2. Four disciplines | **P4** | Full-width strips stacked with no gaps, one word each in wide-tracked caps, centred. | The strips are cropped from her own work: installed column, 401Health screens, Jackson Home plan, ITC career photo. 55% black-box overlay, lifting to 35% on hover. A small red numeral and one line of context sit at the strip edges. |
| 3. The rooms | **P3** (+ P10 meta line) | A dark ground, the active card large and framed, neighbours rotated back in perspective and dimmed. | The four room covers at 4:5. The active one gets a 1px archive-red frame; neighbours sit at 70% scale and 50% opacity. Beneath: `ROOM 01 \| UX RESEARCH \| THE HENRY FORD \| 2026`, the title, "Enter room →" and the lock. |
| 4. Beyond the screen | **P9** | Three overlapping thin circles, one holding a photo, labels inside; a numbered 01–04 list beside. | HISTORY · FASHION · ART, with the personal photo circle as a labelled placeholder. Her About text in 30px serif, and 01–04: stories brought to life · research-led design · exhibit development · a curious, experimental eye. |
| 5. Contact | **P8** | Wide-tracked serif centred over a dark, sculptural photo; tiny caps; short hairline. | "Let's make something *people remember.*" over the installed column at 32% opacity on the black box. |

## Room template, used by all four rooms: `site/room-0N-*.html`

| Section | Pin(s) | What was taken |
|---|---|---|
| Fixed room index | **P12** | Vertical 01–04 at the right edge, the current room larger with a line and in accent. Hovering a number reveals the room name. |
| 1. Room header | **P10 + P12** | P10: a three-line stacked headline with one word in the accent colour, a meta line split by `\|`, and PLAY / TRAILER-style buttons ("▶ Watch the simulation" / "The visitor's route"). P12: big caps at the left over a darkened scene, index at the right. The full-bleed cover sits at 45% opacity and zooms slowly on scroll. |
| 2. Wall label | **P6** | A row of tall mini-cards ("3 cities / 10 days"): photo crops with a caption. Here they carry Role / Methods / Setting / Year / Key number. Heights are staggered so it isn't an equal card grid. |
| 3. Overview · 4. Challenge | Round-1 system | Two-column editorial with a 40px pull sentence; numbered plaque list; full-width 56px italic "How might we…" lines. |
| 5. Signature | One per room, below | |
| 6. Plates and data walls | Round-1 Image System | Drawings multiplied onto the deeper wall; data walls of small charts with one huge numeral; detail crop plus "view full plate" lightbox. Figures are numbered through each room. |
| 7. Black-box gallery | **P12** | The dark video section with round play marks over the thumbnails. One main screen, with smaller screens in a row. |
| 8. Findings / Impact | Round-1 system | Exhibit numerals in a hairline grid; hairline rows with an accent tick. |
| 9. Reflection | Round-1 system | Centred serif italic, the closing text panel. |
| 10. Next room | **P11** | The next room's cover full bleed, with cards floating over it: the next room large with an accent frame, and the other two smaller at either side. |

### Room signatures

| Room | Pin | Section |
|---|---|---|
| 01 Jackson Home | **P6** itinerary + **P9** circles | "The visitor's route": a vertical line with seven stops (Entrance line → Vestibule → Pre-1965 → Video wall → the rooms → Annex → Exit). Plan crops and simulation stills overlap beside each stop, as in P6. Congestion stops are red, with numbers from her model. Then the archetypes as overlapping circles sized by share (60 / 30 / 10). |
| 02 Power & Energy | **P2** arch windows | "The column": five tall pill windows, one per side of the column, each showing that side's artwork, over the installed column softened full bleed. The middle window is taller and framed. |
| 03 Rhode Island | **P1 + P7** | "The app": 401Health screens as cards over the faded desktop portal, with a P7 pill switcher (Vaccination status · Multilingual · Scheduling · Household · Symptom diary · Testing map). The centre card is sharp and the neighbours peek. "+23%" is always labelled as a target. |
| 04 Littelfuse | **P7** centre card | "Three kinds of user": the archetypes as a centre-card carousel with a pill switcher. Engineering (66%) opens active. |

## Private view: `site/private-view.html`

| Section | Pin(s) | What was taken |
|---|---|---|
| Lock screen | **P8 + P1** | P1: one panel floating centred over a full-bleed scene, here solid `#141311` at 85%, a thin border, square corners and no blur. P8: spaced caps, wide-tracked serif title, short hairline. |

## Pins used, and where

P1 (room 03, private view) · P2 (room 02) · P3 (home) · P4 (home) · P5 (home) · P6 (every room's wall label, room 01) · P7 (rooms 03, 04) · P8 (home ×2, private view) · P9 (home, room 01) · P10 (home meta line, every room header) · P11 (every room's exit) · P12 (every room's index, header and black box).
