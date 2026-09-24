# Asset map: Yasmin Bajwa, "The Exhibition"

Every image, video and source file in `yasmin/`, with its project, its **Image System type**, and where it goes on the site.

**Types** (from the brief's Image System):
`DRAWING` architectural or technical drawing · `PLAN` 3D top-down floor plan · `DATA` simulation chart or data · `DENSE` dense document (table, persona board, journey map) · `PHOTO` exhibit photo or render · `UI` UI screen or wireframe · `SKETCH` sketch or whiteboard · `FILM` video or GIF · `PORTRAIT` headshot (About)

**Status:** ✅ usable as is · ⚠️ usable, with a caveat · ♻️ duplicate of a better file (don't use) · ⛔ not for the site

> **Files were reorganised in this phase.** The upload was a flat folder with camera or export names. Everything is now in `source/`, `references/` and `media/<room>/` under web-safe names. `git mv` was used, so history is kept. The *Original name* column lets Yasmin find each file on her own drive.

---

## About: `media/about/`

| File | Original name | Type | Size | Use | Status |
|---|---|---|---|---|---|
| `headshot-a_blazer-warm.jpeg` | `926FB1BC-…FAA.jpeg` | PORTRAIT | 1600×2000 (4:5) | **Hero portrait**, hung like an artwork in columns 8–12 with the placard beneath. The warm beige backdrop sits naturally on `#F3F0EA`. Best candidate for the cut-out behind the name. | ✅ |
| `headshot-b_blue.jpeg` | `6CDAE139-…903.jpeg` | PORTRAIT | 1600×2000 | Alternate. The blue backdrop clashes with the gallery-white palette. Spare for LinkedIn or the SEO share image. | ⚠️ |
| `headshot-c_blue-glasses.jpeg` | `3F0B6633-…3EB.jpeg` | PORTRAIT | 1600×2000 | Alternate. Could be one tile in the "Beyond the screen" mosaic if no personal photos arrive. | ⚠️ |
| `headshot-a_animated.gif` | `IMG_7910.GIF` | FILM | 480×600, 58 frames | A living-portrait version of headshot A. **Too small for the hero** (it would upscale about 3×). Could work at small size in the Contact section. Ask for the source video (see GAPS). | ⚠️ |

## Room 01, The Henry Ford Jackson Home: `media/room01-jackson-home/`

| File | Original name | Type | Size | Use | Status |
|---|---|---|---|---|---|
| `r01_plan_house-visitor-paths.png` | `House flow Jackson Home Project 1_.png` | PLAN | 1544×2232 | **Room 01 cover.** Cropped tight to 4:5 (home) and 16:9 (room header), with 2–3 archive-red callouts at the entrance-area congestion points (Vestibule / Pre-1965 / Video Wall, per her docent-control study factor). Also a full plate in "Building the simulation". | ✅ |
| `r01_plan_house.png` | `Jackson Home- Map Project 1_.png` | PLAN | 1024×1536 | Chapter 02 (Space syntax) plate: the plan *before* the paths. Pairs with the cover as a before/after. | ✅ |
| `r01_chart_congestion-queues-visit-delays.png` | `Data Set 1.png` | DATA | 1774×887 | **Data wall** tile (Congestion · Queue sizes · Visit time · Delays), cropped into 2 tiles. Lightbox to the full sheet. | ✅ |
| `r01_chart_arrivals-random.png` | `Arrivals Jackson Home Project 1_.png` | DATA | 1918×820 | Data wall, Scenario testing: "Random arrivals". Pairs with on-time. | ✅ |
| `r01_chart_arrivals-on-time.png` | `Arrivals Jackson home Project 1.png` | DATA | 1815×866 | Data wall: "On-time arrivals". *Not a duplicate* of the file above, despite the similar name. | ✅ |
| `r01_chart_docent-control.png` | `Docent Charts- Jackson Home.png` | DATA | 1554×1012 | Data wall: "Without docent / With docent" skipped-exhibit histograms. The strongest visual proof for the "3–4 presenters" finding. | ✅ |
| `r01_video_discrete-event-simulation.mp4` | `DISCRETE EVENT SIMULATION- Jackson Home Project 1.mp4` (sent in Phase 2) | FILM | 1638×922, 1:10, 60 fps, 22 MB | **Room 01 black-box gallery.** A screen recording: the player's control bar (0:01/01:06, play, volume) is burned into the bottom ~50px. Crop it off, re-encode to 1600px / 30 fps / muted / ≤8 MB, and cut a 20–30 s loop for the background version. | ⚠️ |
| `r01_chart_expected-visit-times.png` | `Expected Visit Times.png` | DATA | 1616×973 | Beside the archetype numerals: Streakers 8–20 min · Strollers 30–45 · Studiers 50–65. Crop out the slide title and bullets and keep only the three box plots. | ✅ |

## Room 02, Power & Energy Interactive: `media/room02-power-energy/`

| File | Original name | Type | Size | Use | Status |
|---|---|---|---|---|---|
| `r02_video_final-setup.mp4` | `Power-Energy-Portfolio-Final Set Up.mp4` | FILM | 1080×1920 vertical, 0:21 | **Black-box gallery**, the "final setup" film. Also the **source for the Room 02 cover still**: frame 0:00 shows the installed column in the gallery (see GAPS: ask for the original photo). | ✅ |
| `r02_video_fabrication-progression.mp4` | `column-fabrication-progression-web.mp4` | FILM | 960×720, 0:14 | Black-box gallery, fabrication progression. Muted loop. | ✅ |
| `r02_video_interface-user-flow.mp4` | `power-energy-user-flow-portfolio.mp4` | FILM / UI | 1600×900, 0:22 | "Final interface & user flow". Fills the doc's p.20 "INSERT VIDEO HERE". Shown on a deeper-wall panel (it's already on a light ground), not in the black box. | ✅ |
| `r02_video_appspace-cms-channels.mp4` | `Power_Energy_Channels_Portfolio.mp4` | FILM / UI | 1920×924, 0:11 | CMS integration chapter. Fills p.20 "INSERT POWER & ENERGY VIDEO HERE". Small, captioned. | ✅ |
| `r02_diagram_column-sides-flow.png` | `Power_Energy_Columns_High_Resolution.png` | DENSE | 5214×5514 | "Five sides, one story" plate: the pentagon diagram with each side's artwork. Detail crop (the pentagon + arrows) and a full plate in the lightbox. | ✅ |
| `r02_board_content-themes-experience-flow.png` | `ChatGPT Image Aug 18, 2026, 03_24_54 PM.png` | PHOTO (render) | 1536×1024 | Content-strategy board (content themes → experience flow → five sides). Dark ground, so it sits well in the black-box section or as a plate. ⚠️ The filename says ChatGPT: confirm with Yasmin what this is (see GAPS). | ⚠️ |
| `r02_sketch_whiteboard-lofi.png` | `ChatGPT Image Aug 18, 2026, 03_11_32 PM.png` | SKETCH | 1672×941 | **"Early sketches"**: split into its two whiteboard halves and pinned at ±1.5°. ⚠️ Same ChatGPT-filename question. | ⚠️ |
| `r02_board_itc-employee-research.png` | `ITC_Employee_Research_Storyboard_Redesigned_Fixed.png` | DENSE | 1920×1250 | "3 employee voices" chapter. Detail crop of the three employee cards, with the full plate in the lightbox. | ✅ |
| `r02_art_PandE_Column_Art_260127.jpg` | same, no prefix | PHOTO (exhibit graphic) | 2160×7680 | Backlit wayfinding graphic ("Power & Energy" title). One of the **tall strips** in the "five sides, unfolded" row. | ✅ |
| `r02_art_PandE_Column_Art_2601272.jpg` | same | PHOTO (exhibit graphic) | 2160×7680 | Artifact-interpretation graphic (Newcomen engine → "Exhibit highlights"). Unfolded row. | ✅ |
| `r02_art_PandE_Column_Art_2601273.jpg` | same | PHOTO (exhibit graphic) | 2160×7680 | Innovation Nation screen. Unfolded row. | ✅ |
| `r02_art_PandE_Column_CutUpArt_2602184.jpg` | same | UI (screen art) | 2160×7680 | Careers screen, landing. ⚠️ **The top photo is an unlicensed Shutterstock comp** ("shutterstock" and "…rey_Popov" watermarks visible). Don't publish it until the licensed file is swapped in (see GAPS). | ⛔ for now |
| `r02_art_PandE_Column_CutUpArt_2602185.jpg` | same | UI | 2160×7680 | Careers: Community Planning (Jeremy Durr Sr.). "3 employee voices" row. | ✅ |
| `r02_art_PandE_Column_CutUpArt_2602186.jpg` | same | UI | 2160×7680 | Careers: Engineering (Madison Ampunan). "3 employee voices" row. | ✅ |
| `r02_art_PandE_Column_CutUpArt_2602187.jpg` | same | UI | 2160×7680 | Careers: Safety & Security (Michael Ciuffoletti). "3 employee voices" row. | ✅ |
| `r02_art_PandE_Column_CutUpArt_2602188.jpg` | same | UI | 2160×7680 | Power map: Michigan view. Unfolded row / interactive-map plate. | ✅ |
| `r02_art_PandE_Column_CutUpArt_2602189.jpg` | same | UI | 2160×7680 | Power map: zoomed detail. Spare. | ✅ |

## Room 03, Rhode Island 401 Health App: `media/room03-rhode-island/`

| File | Original name | Type | Size | Use | Status |
|---|---|---|---|---|---|
| `r03_ui_vaccine-details-pair.png` | `Rhode Island COVID vaccine.png` | UI | 1592×1292 | **Room 03 cover**: the two app screens floating on a `#E9E4DB` panel. The file has phone frames drawn on, and the brief says no device mockups. **Preferred:** rebuild the pair from the frameless 375px pages of `source/Rhode_Island_DOH_Wireframes.pdf` (pp. 43–98). Use this file only as a fallback. | ⚠️ |
| `r03_ui_vaccine-details-annotated.png` | `Mobile Design .png` | UI | 1536×1024 | Feature-prioritisation plate (annotated: imported data, feature add-on, SMART card, dose details). Same phone-frame caveat. | ⚠️ |
| `r03_video_wireframes.mp4` | `RIDOH_Wireframes_Portfolio.mp4` | FILM / UI | 1920×1080, 0:23 | Scroll-through of the desktop wireframes. Fills p.29 "INSERT PDF OR VIDEO OF WIREFRAMES". Deeper-wall panel, muted loop. | ✅ |
| `r03_video_app-store-reviews.mp4` | `app-store-reviews-portfolio.mp4` | FILM | 900×1956 vertical, 0:23, 14 MB | Discovery chapter: the review scroll. Fills p.27. Narrow vertical "screen" beside the pain-point list. Re-encode to ≤5 MB before upload. | ✅ |

## Room 04, Littelfuse Product Discovery: `media/room04-littelfuse/`

| File | Original name | Type | Size | Use | Status |
|---|---|---|---|---|---|
| `r04_doc_journey-map.png` | `Journey Map.png` | DENSE | 1787×880 | **Room 04 cover** (detail crop: the Find → Learn → Get stage icons) plus the "Mapped the journey" chapter: a detail crop of one stage and the full plate in the lightbox. | ✅ |
| `r04_doc_user-archetypes.png` | `littelfuse_user_archetypes_portfolio.png` | DENSE | 3768×1688 | The three archetypes (Engineering & Technical · Sales · Procurement). Detail crop of the Engineering panel with the full plate in the lightbox. Alternate cover crop. | ✅ |
| `r04_video_engineering-personas.mp4` | `littelfuse_engineering_personas_portfolio.mp4` | FILM | 1600×900, 0:20 | Persona walkthrough (OEM Engineer 66% · CM Engineer 44% · Technical Advisor 81%). Deeper-wall panel, muted loop. | ✅ |

---

## Extracted from the case study: `media/doc/`

All 24 images embedded in `source/CASE_STUDY-Yasmin_Bajwa.pdf`, numbered in document order (`doc-NN`), grouped by project, with the page number. The PDF was already compressed by iLovePDF, so **every doc image is 975px wide**. Where a full-resolution original exists in `media/`, use that one; the doc copy is marked ♻️.

**Note:** the brief refers to `CASE_STUDY-Yasmin_Bajwa.docx`. Only the **PDF** was uploaded, and the extraction is from that.

### Room 01, Jackson Home (`media/doc/room01-jackson-home/`)
| File | Page | Content | Type | Use | Status |
|---|---|---|---|---|---|
| `doc-01_room01-01_p03.jpeg` | 3 | Visitor-type table (60/10/30 %) + "Time spent on-site" box plot | DATA | The table becomes the three archetype numerals (no table on site). The box plot is a small plate beside them. **Only copy in existence.** | ⚠️ 975px |
| `doc-02_room01-02_p04.jpeg` | 4 | Congestion / queue / visit time / delays dashboard | DATA | = `r01_chart_congestion-queues-visit-delays.png` | ♻️ |
| `doc-03_room01-03_p05.jpeg` | 5 | House plan, no paths | PLAN | = `r01_plan_house.png` | ♻️ |
| `doc-04_room01-04_p06.jpeg` | 6 | **Annex plan** with entrance/exit arrows (Vestibule, Music Room, site entrance line) | PLAN | Plate in "Building the simulation", beside the house plan. **Only copy in existence.** | ⚠️ 975px |
| `doc-05_room01-05_p07.jpeg` | 7 | House plan with green visitor paths | PLAN | = `r01_plan_house-visitor-paths.png` | ♻️ |
| `doc-06_room01-06_p09.jpeg` | 9 | Random arrivals | DATA | = `r01_chart_arrivals-random.png` | ♻️ |
| `doc-07_room01-07_p10.jpeg` | 10 | On-time arrivals | DATA | = `r01_chart_arrivals-on-time.png` | ♻️ |
| `doc-08_room01-08_p10.jpeg` | 10 | Expected visit times | DATA | = `r01_chart_expected-visit-times.png` | ♻️ |
| `doc-09_room01-09_p12.jpeg` | 12 | Without/with docent charts | DATA | = `r01_chart_docent-control.png` | ♻️ |
| `doc-10_room01-10_p12.jpeg` | 12 | **"Best scenario: tickets 20, walk-ups 8, with docent control"** (4 charts) | DATA | Data wall, **the headline tile** beside the "30 visitors per window" numeral. **Only copy in existence.** | ⚠️ 975px |

### Room 02, Power & Energy (`media/doc/room02-power-energy/`)
| File | Page | Content | Type | Use | Status |
|---|---|---|---|---|---|
| `doc-11_room02-01_p15.jpeg` | 15 | Content themes / experience flow board | PHOTO | = `r02_board_content-themes-experience-flow.png` | ♻️ |
| `doc-12_room02-02_p16.jpeg` | 16 | Whiteboard lo-fi sketches | SKETCH | = `r02_sketch_whiteboard-lofi.png` | ♻️ |
| `doc-13_room02-03_p17.jpeg` | 17 | ITC employee research board | DENSE | = `r02_board_itc-employee-research.png` | ♻️ |
| `doc-14_room02-04_p19.jpeg` | 19 | Column sides + flow diagram | DENSE | = `r02_diagram_column-sides-flow.png` | ♻️ |
| `doc-15_room02-05_p20.jpeg` | 20 | "Final interface & user flow" screen grab | UI | Placeholder only. The doc says the video replaces it: `r02_video_interface-user-flow.mp4` | ♻️ |
| `doc-16_room02-06_p21.jpeg` | 21 | Shop drawing sheet C-2 (plan, section, perspective) | DRAWING | Replaced by the vector PDF, rendered at high resolution (below). | ♻️ |
| `doc-17_room02-07_p22.jpeg` | 22 | Shop drawing sheet 2 (elevations, sections) | DRAWING | Same | ♻️ |
| `doc-18_room02-08_p22.jpeg` | 22 | Shop drawing sheet 3 (plan, elevation, typical surround) | DRAWING | Same | ♻️ |

### Room 03, Rhode Island (`media/doc/room03-rhode-island/`)
| File | Page | Content | Type | Use | Status |
|---|---|---|---|---|---|
| `doc-19_room03-01_p27.jpeg` | 27 | **23 Population Health Goals** table (goals 20–23 highlighted in her text) | DENSE | Detail crop (goals 20–23, "Analyze and communicate data…") plus the full plate in the lightbox. **Only copy, and too low-res for a large crop** (see GAPS). | ⚠️ 975px |
| `doc-20_room03-02_p28.jpeg` | 28 | App Store review screenshot | UI | The doc says "picture is only for reference". Replaced by `r03_video_app-store-reviews.mp4` | ♻️ |
| `doc-21_room03-03_p29.jpeg` | 29 | Vaccine Details annotated screens | UI | = `r03_ui_vaccine-details-annotated.png` | ♻️ |

### Room 04, Littelfuse (`media/doc/room04-littelfuse/`)
| File | Page | Content | Type | Use | Status |
|---|---|---|---|---|---|
| `doc-22_room04-01_p33.jpeg` | 33 | "Designing for the people who drive component decisions": 66% / 64% / 61% stat board | DENSE | The numbers are re-set as live serif numerals; the image itself isn't needed. **Only copy.** (The same board opens the personas video.) | ⚠️ 975px |
| `doc-23_room04-02_p33.jpeg` | 33 | User archetypes | DENSE | = `r04_doc_user-archetypes.png` | ♻️ |
| `doc-24_room04-03_p34.jpeg` | 34 | Journey map | DENSE | = `r04_doc_journey-map.png` | ♻️ |

---

## Source documents: `source/`

| File | Original name | What it is | Use |
|---|---|---|---|
| `Instructions_About_Me.docx` | `Instructions_About Me.docx` | Site direction + About copy + the 4 skills in order | Homepage copy (Hero, Four disciplines, Beyond the screen). |
| `CASE_STUDY-Yasmin_Bajwa.pdf` | `CASE STUDY-Yasmin Bajwa_compressed.pdf` | All 4 case studies, 35 pp. (an identical copy also sits at the repo root) | All room copy; images extracted to `media/doc/`. |
| `PandE_Shop-Drawing_Column-Surrounds_AV05.pdf` | `127505- REVISED SHOP DRAWING - Column Surrounds - AV05.pdf` | 3 sheets, 11×17, **vector** | DRAWING plates for Room 02 (Fig. "Column surround, plan and elevation"). To be rendered as transparent-ground PNGs at 3000px+ in Phase 3, plus a detail crop of the pentagon plan. ⚠️ Dated 11.1.2018: see GAPS. |
| `Rhode_Island_DOH_Wireframes.pdf` | `Rhode Island Dept of Health .pdf` | **98 pp.**, **vector**. pp. 1–42: desktop COVID-19 **test-scheduling portal** (1440 wide). pp. 43–98: the **401Health mobile app** (375 wide: vaccine details, SMART card, household, etc.) | Room 03 UI plates. The mobile pages are clean 375px screens with **no phone frame**, so they are the correct source for the "2–3 screens in a row" treatment and for a frameless Room 03 cover. Desktop: 3 screens in a row (Welcome / Select a testing facility / Select a time). |
| `Littelfuse_Wireframes_XD-links.docx` | `Little Fuse Wireframes .docx` | ~60 **Adobe XD share links** (hi-fi mock-ups: mega menu, L0–L7 product flow, check stock, request sample, where to buy, search, mobile). **No images inside.** | Nothing to place yet. Counts as the Littelfuse wireframes gap. |

## References: `references/`

| File | What it is | Note |
|---|---|---|
| `ayushfolio.png` | Screenshot of ayushfolio.online (sent in Phase 2) | The layout reference: a card with "Hi. I'm *Ayush.*" and a 4-column facts row, a halftone portrait, "Where I've worked" cards, project rows with an image on the right, testimonials, a "What else?" italic paragraph with a photo strip, and a contact footer. |
| `ayush-singh_wallofportfolios-listing.html` | A saved *Wall of Portfolios* listing page **about** Ayush, not his portfolio. Its `_files/` folder wasn't uploaded, so it renders without images. | The reference screenshot was later supplied as `ayushfolio.png` (row above). An identical copy also sits at the repo root. |

## Not Yasmin's: repo root

`day.jpg`, `night.jpg`, `hero.jpg`, `hero 1.jpg`, `hero-foreground.jpg`, `story-*.jpg`, `strip-*.jpg`, `weekend.jpg` are Barcelona night-street photography from a different client project. ⛔ **Not used.** The root copies of `PandE_Column_*.jpg` (5 files) and the case-study PDF are byte-identical to the files in `yasmin/`. They were left untouched.

## Derived web assets: `site/assets/img/` (Phase 2)

| File | Made from | Treatment |
|---|---|---|
| `portrait-4x5.jpg` | `headshot-a_blazer-warm.jpeg` | 1200×1500, untoned |
| `portrait-cutout.png` / `.webp` | same | Transparent cut-out for the depth-layered hero. Mask = soft hair edge from one segmentation model + solid body from a second. The PNG is for Squarespace upload; the WebP is for the prototype. |
| `r01-cover-4x5.jpg` | `r01_plan_house-visitor-paths.png` | 4:5 crop, shared tone, 3 red callouts built into the image (A entry from the Annex · B central hall · C exit). Callout B also covers a stray software tooltip ("Office Online Frame") in her export. |
| `r02-cover-4x5.jpg` | frame 0:00 of `r02_video_final-setup.mp4` | 4:5 crop, shared tone. Interim until the original photo arrives (GAPS C1). |
| `r03-cover-4x5.jpg` | `source/Rhode_Island_DOH_Wireframes.pdf` pp. 57 + 58 | Two frameless vector screens rendered at 3×, floating on `#E9E4DB` with a hairline, shared tone |
| `r04-cover-4x5.jpg` | `r04_doc_journey-map.png` | Detail crop (Learn stage, steps 3–4) mounted like a plate on `#E9E4DB`, shared tone |

**Shared tone** (all four covers): saturation 80%, contrast 97%, then `#F3F0EA` multiplied at 50%.

## Round 2: derived web assets

`tools/build_assets.py` regenerates every file in `site/assets/img/` and `site/assets/video/` from `media/` and `source/`. Its crop boxes are the record of what each web image shows. Main additions this round:
- **Room 01:** 16:9 simulation still (header), itinerary crops (entrance, vestibule, front rooms, kitchen, exit), six simulation stills, and chart tiles cut from the data sheets.
- **Room 02:** column frames from the final-setup and fabrication videos, the five side artworks, the shop drawings rendered from the vector PDF (+ a plan-view detail), the whiteboard split into two sketches, and ITC board and sides-diagram details.
- **Room 03:** ten mobile and three desktop screens rendered from the RIDOH PDF, the goals 20–23 detail, and a 16:9 five-screen header.
- **Room 04:** the Find / Learn / Get journey details and the three archetype panels.
- **Homepage:** four 4:1 discipline strips.
- **Videos:** 8 muted H.264 encodes (≤3.6 MB) with poster frames. The simulation has its burned-in player bar cropped off.
