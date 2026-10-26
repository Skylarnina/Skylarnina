# 3D book mockups (transparent PNG)

One per ebook (about 1300–1370 × 1780–1810 px, same scale), transparent background with a soft shadow, pages fanned on the right like they are turning
(Bibi's reference, 21 Oct). Covers taken from page 1 of the ebook PDFs Pietro sent.

- `gestire-la-fame-3d-libro.png`
- `allenarsi-con-continuita-3d-libro.png`
- `proteggere-il-sonno-3d-libro.png`
- `migliorare-la-digestione-3d-libro.png`
- `gestire-la-pressione-3d-libro.png` (cover from the PDF sent on 26 Oct)

To re-render (e.g. when a cover changes): export page 1 of the PDF to `<slug>.png` (1600 px wide), then
`node tools/book3d.mjs <src-dir> <out-dir> <slug>` (Playwright). The script trims nothing; trim transparent edges after.
