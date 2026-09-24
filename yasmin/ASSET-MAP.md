# Asset Map

Old → new paths for everything moved out of the loose `yasmin/` root, plus
where each newly-extracted asset came from. All paths below are relative to
`yasmin/`.

## Source documents → `source/`

| Old name | New path |
|---|---|
| `Instructions_About Me.docx` | `source/Instructions_About Me.docx` |
| `CASE STUDY-Yasmin Bajwa_compressed.pdf` | `source/CASE STUDY-Yasmin Bajwa_compressed.pdf` |
| `Little Fuse Wireframes .docx` | `source/Little Fuse Wireframes .docx` |
| `Rhode Island Dept of Health .pdf` | `source/Rhode Island Dept of Health .pdf` |
| `127505- REVISED SHOP DRAWING - Column Surrounds - AV05.pdf` | `source/127505- REVISED SHOP DRAWING - Column Surrounds - AV05.pdf` |

## References → `references/`

| Old name | New path |
|---|---|
| `Ayush Singh - Wall of Portfolios.html` | `references/Ayush Singh - Wall of Portfolios.html` |
| *(new)* | `references/ayushfolio.png` — full-page screenshot of the live site. `ayushfolio.online` isn't reachable from this environment (network policy), so this was captured from the saved HTML file instead, per your fallback instruction. |

## Headshots → `media/headshots/`

| Old name | New path | Note |
|---|---|---|
| `3F0B6633-0122-4280-9E74-19D5BE4363EB.jpeg` | `media/headshots/headshot-01-blue-glasses.jpeg` | Blue mottled backdrop, striped shirt, glasses |
| `6CDAE139-2957-4D43-BF6A-C7A63C35A903.jpeg` | `media/headshots/headshot-02-blue-noglasses.jpeg` | Same session as #1, no glasses |
| `926FB1BC-5BA8-4B56-992A-CBE1E7247FAA.jpeg` | `media/headshots/headshot-03-neutral-blazer.jpeg` | Neutral warm backdrop, blazer — separate, more polished session |
| `IMG_7910.GIF` | `media/headshots/headshot-03-animated.gif` | **Not the simulation** — this is an animated (Cinemagraph-style) version of headshot #3. See ASSET-GAPS.md. |

## Jackson Home → `media/jackson-home/`

Renamed loose files:

| Old name | New path |
|---|---|
| `Arrivals Jackson Home Project 1_.png` | `media/jackson-home/arrivals-01.png` |
| `Arrivals Jackson home Project 1.png` | `media/jackson-home/arrivals-02.png` |
| `Docent Charts- Jackson Home.png` | `media/jackson-home/docent-charts.png` |
| `House flow Jackson Home Project 1_.png` | `media/jackson-home/house-flow.png` |
| `Jackson Home- Map Project 1_.png` | `media/jackson-home/map.png` |
| `Data Set 1.png` | `media/jackson-home/simulation-dashboard.png` |
| `Expected Visit Times.png` | `media/jackson-home/simulation-visit-times.png` |

New, extracted from `source/CASE STUDY-Yasmin Bajwa_compressed.pdf` (not present as loose files — these were embedded only in the PDF):

| New path | Source page |
|---|---|
| `media/jackson-home/simulation-visitor-mix.jpg` | p.3 — expected visitor-type mix table |
| `media/jackson-home/simulation-floorplan-isometric.jpg` | p.5 — isometric floor plan with simulated visitors |
| `media/jackson-home/simulation-annex-flow.jpg` | p.6 — annex/vestibule entrance-exit flow diagram |
| `media/jackson-home/simulation-house-flow-arrows.jpg` | p.7 — house floor plan with visitor flow arrows |
| `media/jackson-home/simulation-random-arrivals.jpg` | p.9 — "Random Arrivals" scenario chart |
| `media/jackson-home/simulation-ontime-arrivals.jpg` | p.10 — "On-Time Arrivals" scenario chart |
| `media/jackson-home/simulation-docent-comparison.jpg` | p.12 — "With/Without Docent" skip-rate comparison |
| `media/jackson-home/simulation-best-scenario.jpg` | p.12 — "Best Scenario: Tickets 20, Walkups 8" chart |

## Power & Energy → `media/power-energy/`

Renamed loose files:

| Old name | New path |
|---|---|
| `PandE_Column_Art_260127.jpg` | `media/power-energy/column-art-01.jpg` |
| `PandE_Column_Art_2601272.jpg` | `media/power-energy/column-art-02.jpg` |
| `PandE_Column_Art_2601273.jpg` | `media/power-energy/column-art-03.jpg` |
| `PandE_Column_CutUpArt_2602184.jpg` … `2602189.jpg` | `media/power-energy/column-cutup-art-01.jpg` … `-06.jpg` |
| `Power-Energy-Portfolio-Final Set Up.mp4` | `media/power-energy/final-setup.mp4` |
| `Power_Energy_Channels_Portfolio.mp4` | `media/power-energy/channels.mp4` |
| `Power_Energy_Columns_High_Resolution.png` | `media/power-energy/columns-high-resolution.png` |
| `column-fabrication-progression-web.mp4` | `media/power-energy/column-fabrication-progression.mp4` |
| `power-energy-user-flow-portfolio.mp4` | `media/power-energy/user-flow.mp4` |
| `ChatGPT Image Aug 18, 2026, 03_11_32 PM.png` | `media/power-energy/kiosk-wireframe-sketch.png` — early whiteboard sketches |
| `ChatGPT Image Aug 18, 2026, 03_24_54 PM.png` | `media/power-energy/kiosk-concept-render.png` — rendered kiosk concept |
| `ITC_Employee_Research_Storyboard_Redesigned_Fixed.png` | `media/power-energy/employee-research-storyboard.png` |

New, extracted from the case study PDF:

| New path | Source page |
|---|---|
| `media/power-energy/kiosk-touchpoint-diagram.jpg` | p.19 — full touchpoint diagram + photo of the installed physical column |
| `media/power-energy/final-interface-userflow-mockup.jpg` | p.20 — "Final Interface & User Flow" phone mockup |

New, rendered from `source/127505- REVISED SHOP DRAWING - Column Surrounds - AV05.pdf` (3 pages, no embedded raster images — this PDF is vector/CAD line art, so pages were rendered to PNG at 2.5x scale):

| New path | Sheet |
|---|---|
| `media/power-energy/shop-drawing-column-overview.png` | Sheet 1 — column plan/section, graphic panel installation, perspective |
| `media/power-energy/shop-drawing-panel-elevations.png` | Sheet 2 — Type D/E panel elevations and sections |
| `media/power-energy/shop-drawing-surround-details.png` | Sheet 3 — typical column surround, kick filler, panel filler details |

## Rhode Island → `media/rhode-island/`

Renamed loose files:

| Old name | New path |
|---|---|
| `RIDOH_Wireframes_Portfolio.mp4` | `media/rhode-island/wireframes.mp4` |
| `Rhode Island COVID vaccine.png` | `media/rhode-island/covid-vaccine-screen.png` |
| `app-store-reviews-portfolio.mp4` | `media/rhode-island/app-store-reviews.mp4` |
| `Mobile Design .png` | `media/rhode-island/mobile-design.png` |

New, extracted from the case study PDF:

| New path | Source page |
|---|---|
| `media/rhode-island/population-health-goals.jpg` | p.27 — "23 Population Health Goals" |
| `media/rhode-island/app-store-reviews-reference.jpg` | p.28 — app store reviews reference screenshot |

New, extracted from `source/Rhode Island Dept of Health .pdf` (a 98-page wireframe/prototype export). That PDF contains ~125 embedded images, but all except the seven below are either the repeated "401Health" logo mark, repeated nav icons, a blank black frame, a Google reCAPTCHA badge, or **two unrelated stock-photo/template images (an Allianz Arena photo and a Rome map-pin mockup) that don't belong to this project** — those were excluded rather than copied in:

| New path | Source page |
|---|---|
| `media/rhode-island/wireframe-daily-activities.png` | p.12 |
| `media/rhode-island/wireframe-schedule-test.png` | p.13 |
| `media/rhode-island/wireframe-insurance-info.png` | p.14 |
| `media/rhode-island/wireframe-select-facility.png` | p.16 |
| `media/rhode-island/wireframe-select-timeslots.png` | p.17 |
| `media/rhode-island/wireframe-select-time.png` | p.18 |
| `media/rhode-island/wireframe-appointment-confirmed.png` | p.19 |

## Littelfuse → `media/littelfuse/`

Renamed loose files:

| Old name | New path |
|---|---|
| `littelfuse_engineering_personas_portfolio.mp4` | `media/littelfuse/engineering-personas.mp4` |
| `littelfuse_user_archetypes_portfolio.png` | `media/littelfuse/user-archetypes.png` |
| `Journey Map.png` | `media/littelfuse/journey-map.png` — this is the Littelfuse "John Doe" product-discovery journey, not Jackson Home; the filename didn't say so, but the content ("Research products on Little Fuse website...") does. |

New, extracted from the case study PDF:

| New path | Source page |
|---|---|
| `media/littelfuse/persona-research-stats.jpg` | p.33 — "From Research to Personas" stats (66%/64%/61%) |
| `media/littelfuse/persona-archetype-cards.jpg` | p.33 — Engineer/Sales/Procurement archetype cards |

**`Little Fuse Wireframes .docx` contained zero embedded images.** It's a
plain list of links to an external Adobe XD prototype
(`xd.adobe.com/view/...`, ~15 separate prototype links covering desktop
product flow, search, "where to buy", and mobile). `xd.adobe.com` isn't
reachable from this environment (network policy), so nothing could be
pulled from it. See ASSET-GAPS.md.
