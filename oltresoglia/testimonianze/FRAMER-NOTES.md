# Testimonianze: Framer handoff

Page: `oltresoglia/testimonianze/oltresoglia-testimonianze-pagina.html` (self-contained, fonts inlined).
Order from Bibi (30 Oct): **videos first, then before/after photos, then written testimonials.**
Copy: title and description from Bibi (25 Oct), verbatim. The content (17 videos, 45 photos, 20 written testimonials) came by
WeTransfer; every slot on the page is a numbered placeholder ready to swap.

(`index.html` is the earlier two-row marquee version, kept for reference only.)

## Structure

| # | Section | Content | Build in Framer |
|---|---|---|---|
| — | Header | Same as every page: dark box, nav, "Testimonianze", breadcrumb | Shared component |
| — | Intro | Eyebrow "Storie reali", H2 "Meno grasso. Più atletici…", description. Right: dark box with jump links 17 Video · 45 Foto · 20 Scritte | Links scroll to the three sections |
| 1 | **Video testimonianze** | Dark rounded box (radius 28, 20px inset). Eyebrow, H2 "Raccontato da loro.", counter "01 / 17" + prev/next arrows. **Horizontal carousel, not a grid**: 9:16 cards (230–300px wide, radius 20, gap 20), Saffron play button, name + duration under each card, Saffron progress line | Horizontal Stack, overflow scroll, snap to each card (or the Slideshow component with arrows on, autoplay off). Each card: Video component, poster image, controls on, no autoplay. Cards start aligned with the page content and run off the right edge |
| 2 | **Prima e dopo** | Eyebrow, H2 "I cambiamenti, fotografati.", consent line. Grid of 4:5 cards (radius 18, gap 20; 4 / 3 / 2 / 1 columns by width). First 12 shown, then "Mostra tutte le foto (45)" reveals the rest | Grid, Fill images centred. "Mostra tutte" = variant switch or a second hidden grid |
| 3 | **Testimonianze scritte** | White section. Eyebrow, H2 "Con le loro parole.", line "I messaggi arrivano così come…". 20 cards in a 3-column masonry: quote mark, text, **name underneath** (Bounded Bold) with the Saffron tick | Masonry: 3 vertical Stacks (Framer has no CSS columns); 1 column on phone |
| — | CTA + footer | Unchanged | — |

## Swapping in the content
- Videos: each card's play button has `data-src` (mp4) and `data-poster` (still). Fill them and the card plays inline;
  starting one pauses the others. Compress before upload (1080 × 1920, H.264, ~5–8 MB each); in Framer host on the Video component.
- Photos: put an `<img>` inside `.ba2__img` (it fills the 4:5 frame). 45 is an odd number, so these are treated as one
  combined before/after image each, not pairs; if they are separate files, the card splits into Prima / Dopo halves.
- Written: replace `[Testimonianza scritta NN]` and `[Nome]` with the copy and the name from the document. Card 01 already has
  Marco's message from Bibi's first reference; check whether it is one of the 20.

## To confirm with Bibi
- Section titles "Raccontato da loro." and "Con le loro parole." are proposals (not in Bibi's copy).
- Video captions: name only, or name + role? Duration is optional.
