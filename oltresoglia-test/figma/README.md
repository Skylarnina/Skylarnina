# Test Oltresoglia: screens for Figma

This folder has **17 screen states × 2 sizes** (mobile 390 px, desktop 1440 px). Each is a static HTML page, so each imports into Figma as one clean frame with no clicking through the test.

Open **`index.html`** in this folder to see the list of states.

| # | File | State |
|---|---|---|
| 01 | `01-ingresso` | Entry |
| 02 | `02-ingresso-riprendi` | Entry, returning user ("Riprendi dalla domanda 4") |
| 03–10 | `03-domanda-1` … `10-domanda-8` | Questions 1–8, no answer yet |
| 11 | `11-domanda-1-selezionata` | Answer just selected (Saffron card, others dimmed) |
| 12 | `12-domanda-8-rivisitata` | Answered question after going back ("Continua" button) |
| 13 | `13-email` | Email, empty |
| 14 | `14-email-errore` | Email, error state |
| 15 | `15-email-suggerimento` | Email, "Intendevi mario@gmail.com?" |
| 16 | `16-analisi` | "Stiamo analizzando…", step 1 done, step 2 in progress |
| 17 | `17-risultato` | Result preview (ORBITA, points per profile) |

Add `-desktop` to a file name for the 1440 px version.

## Importing with html.to.design

1. Download the `oltresoglia-test` folder. Keep `figma/` and `assets/` side by side, because the pages load the photo from `../assets/`.
2. In Chrome, install the **html.to.design** extension. In its extension settings, turn on **Allow access to file URLs**.
3. Open a page (e.g. `03-domanda-1.html`). For mobile pages, open DevTools → device toolbar and set the width to **390**. For `-desktop` pages, use a window at least 1440 px wide.
4. Capture with the extension, then paste into Figma with the html.to.design plugin. Repeat for each state.

**To import by URL instead:** the pages need to be public, for example on GitHub Pages or Netlify. Then paste each page's link into the plugin.

## After importing, check

- **Photo:** the page shows it in black and white with a CSS filter, which may not come across. If it imports in colour, set the image to 0% saturation in Figma.
- **Progress segments:** they are slanted with `skewX(-10deg)`. If they import straight, skew them 10° in Figma.
- **Font:** Manrope must be installed or available in Figma. It's free on Google Fonts.
- **Keep the static pages in sync:** these pages are snapshots. After changing `../index.html`, rebuild them with `node build-states.js` (requires Playwright).
