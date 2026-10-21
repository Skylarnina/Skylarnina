# 3D book mockups (transparent PNG)

One per ebook, 1303 × 1778 px, transparent background with a soft shadow, pages fanned on the right like they are turning
(Bibi's reference, 21 Oct). Covers taken from page 1 of the ebook PDFs Pietro sent.

- `gestire-la-fame-3d-libro.png`
- `allenarsi-con-continuita-3d-libro.png`
- `proteggere-il-sonno-3d-libro.png`
- `migliorare-la-digestione-3d-libro.png`
- `gestire-la-pressione-3d-libro.png`: **temporary**, made from the site's placeholder cover; no PDF yet.

To re-render (e.g. when the Pressione PDF arrives): export page 1 of the PDF to `<slug>.png` (1600 px wide), then
`node tools/book3d.mjs <src-dir> <out-dir> <slug>` (Playwright). The script trims nothing; trim transparent edges after.
