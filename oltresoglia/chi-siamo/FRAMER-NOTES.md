# Chi siamo (v3): Framer handoff

Prototype: `oltresoglia/chi-siamo/index.html` (`?coach=anna` opens on a given coach).
Same tokens, nav, buttons and contrast settings as the Contact page (`../contact/FRAMER-NOTES.md`).
All copy is verbatim from the "ABOUT US WEBSITE" Google Doc; the generator checks every line of Pietro's text is used once.

**Concept: "Oltre la soglia".** The page is a journey in four numbered steps (01 Da dove vengo · 02 Perché nasce ·
03 Come lavoriamo · 04 Il team) that ends at the threshold: the test.

| # | Section | Reference move | Build in Framer |
| --- | --- | --- | --- |
| 1 | Hero: "CHI SIAMO" at 15vw behind Pietro's cut-out in an arch frame, over the horizon artwork | Musclefit hero + depth-layered type | Stack: wordmark (z 0) → transparent PNG of Pietro in an arch-masked frame (z 1). Scroll transform: portrait moves up ~8% faster than the word |
| 2 | Founder: portrait + caption left, intro right; then a timeline 14 anni → 17 anni → pull quote "Ho vissuto entrambi gli estremi." → La direzione → Oggi | Prestix "Delivering excellence" + "story in numbers", journey timeline | 2-column Stack; timeline = vertical Stack with a 1px line and saffron-ring dots |
| 3 | Why (light Porcelain ground): problem paragraph, then "OLTRESOGLIA NASCE DA QUI." full width, "da qui." underlined in Saffron | Untitled UI light statement, scale contrast | Text at 10vw; underline = text decoration, Saffron |
| 4 | How: "Partiamo dai tuoi impegni…", then four full-width strips TURNI / RIUNIONI CHE SFORANO / PARTENZE ALL'ULTIMO / SERATE CHE NON DECIDI, then "AL CENTRO DEL PERCORSO CI SEI TU, NON IL PROGRAMMA." + mission | Musclefit marquee band, as stacked photo strips | Each strip: image fill (profile artwork now, photography later) + 50% Charcoal overlay; hover zooms the image 6% over 1.1s |
| 5 | Team: "IL TEAM", depth carousel of the 5 coaches (active card full size with Saffron border, neighbours 80% / 66%, dimmed, peeking off the edges), then name tabs + the active coach's full story in two columns | Untitled UI team carousel + Prestix Buying/Selling/Investing tabs + Musclefit professionals | Carousel = component with 5 variants (one per active coach), transition 1s cubic-bezier(.76,0,.24,1); tabs and arrows switch variants |
| 6 | Closing line: "Per chi pretende dal proprio corpo lo stesso livello che pretende da tutto il resto." | Untitled UI quote | Bounded ExtraLight, 88px |
| 7 | Threshold CTA: test title + "Fai il test" outline pill over the horizon artwork | Musclefit "Transform your body" band | Same pill as the nav |

Type scale: hero word 15vw (max 240) · section headlines 96–168px · timeline numerals 128px · body 17–19px · labels 11px, tracked 0.2em.

## Photos needed (drop into `assets/team/` with these names; the page picks them up)
- `pietro-scontornato.png`: Pietro cut out, transparent background, for the hero arch
- `pietro.jpg`: portrait 4:5 for the founder section
- `marco.jpg`, `anna.jpg`, `giulio.jpg`, `yuri.jpg`, `devid.jpg`: portraits 4:5

All photos are shown in grayscale so the set reads as one shoot.
