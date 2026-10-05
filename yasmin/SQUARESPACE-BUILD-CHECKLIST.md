# Squarespace build checklist · Yasmin Bajwa portfolio

Tick each box as you build. Every block lists its **Fluid Engine columns** (desktop grid of 24, mobile grid of 8), its **Site Styles text style**, and the **exact text to paste** in a grey box (use the box's copy button; the text is her source spelling, so labels are typed in normal case and the Paragraph 3 style uppercases them). Images give the **file to upload** and the **shape to size the block to**.

Generated from the current build (`site/`, the built **mono** palette) and SQUARESPACE-BUILD-NOTES.md by `tools/build_checklist.py`: the text, columns, files and ratios are read from the rendered pages, so they match the prototype exactly. Things Squarespace can't reproduce exactly are flagged **F1…F19** with the nearest native setting, all listed on Page 10. Where this checklist and the build notes differ (the lock-screen font, the CSS numbering), the checklist follows the current build.

**Build order, and why:** Page 0 (Site Styles, header, footer) → **Pages 1–5 the Case studies Portfolio** (its four project URLs are what Projects and Home link to; Room 01 is built first and its sections saved for reuse) → **Page 6 Lock Screen** (password on, tested) → **Page 7 Projects** → **Page 8 Homepage** (links to everything above; built last so no link points at a page that doesn't exist yet) → **Page 9 Custom CSS** (pasted last: two of its rules need block and section IDs from Home and Projects) → Page 10 flags, Page 11 final checks.

**Notation:** `cols 9–20 · mobile 1–8` = the block spans desktop columns 9 to 20 and mobile columns 1 to 8. "A → B" in a text block = several lines in one block, each in its own style. "Line block above" = a 1px Line block directly above, same columns. Spacing is given in px at 1440 (and phone) widths.

**In this checklist:** 317 text pastes, 67 images (including 21 slideshow photos), 8 videos, 34 image captions, 19 lines of CSS, 19 flags.

<div style="page-break-after: always"></div>

## Page 0 · Site Styles, header and footer (set once)

Set these before building any page; every later page assumes them. Values are the built palette (**mono**). If the client picks another palette, change only the colour rows (THEMES.md and the build notes' *Site Styles per theme* list the values).

**Fonts** (*Site Styles → Fonts*)
- [ ] Headings: **Instrument Serif** (Google; **verify** it is in her picker, otherwise add it as a custom font). One weight (400) plus italic: emphasis in headings is italic, never bold.
- [ ] Paragraphs, buttons, navigation, captions: **Inter Tight** 400 (500 for labels and the "About Me" kicker).

**Type scale** (*Site Styles → Fonts → each style*; desktop / mobile)

- [ ] **Heading 1** · Instrument Serif 400 · **140px** desktop / **64px** mobile · line height 0.92 · tracking −0.01em · "Hi, I’m Yasmin."
- [ ] **Heading 2** · Instrument Serif 400 · **80px** desktop / **40px** mobile · line height 1.02 · tracking −0.01em (0 on mobile) · Page and cover titles, "Projects", the contact line
- [ ] **Heading 3** · Instrument Serif 400 · **46px** desktop / **34px** mobile · line height 1.08 · tracking 0 · Chapter titles, "Snippets About My Life"; panel names and row titles (prototype 34 / 32px)
- [ ] **Heading 4** · Instrument Serif 400 · **24px** desktop / **24px** mobile · line height 1.3 · tracking 0 · Her sub-headings, prev/next titles; italic for "How might we…"
- [ ] **Paragraph 1** · Inter Tight 400 · **40px** desktop / **28px** mobile · line height 1.2 · tracking −0.015em · The Snippets statement
- [ ] **Paragraph 2** · Inter Tight 400 · **17px** desktop / **16px** mobile · line height 1.6 · tracking 0 · All her body text
- [ ] **Paragraph 3** · Inter Tight 500, **uppercase** · **11px** desktop / **11px** mobile · line height 1.45 · tracking 0.08em · Labels, captions ("FIG. 03 — …"), "PASSWORD PROTECTED"

**Colours** (*Site Styles → Colours*, mono)
- [ ] Palette: `#FFFFFF` (white) · `#F4F3F0` (stone) · `#111111` (ink). No accent colour.
- [ ] Section theme **White**: background `#FFFFFF`, text `#111111`, links `#111111` underlined.
- [ ] Section theme **Stone**: background `#F4F3F0`, text `#111111` (Snippets, Contact, each Reflection).
- [ ] Section theme **Ink**: background `#111111`, text `#FFFFFF` (the discipline panels, so their names are white without CSS).
- [ ] Paragraph 3 colour: `#6B6B6B` (62% ink; 55% fails contrast at 11px). Image captions get the same through CSS rule 2.

**Buttons** (*Site Styles → Buttons → Primary*)
- [ ] Style **outline**, 1px `#111111`, **square** corners (radius 0), Inter Tight 14px, tracking 0.02em, padding about 14 × 22px. Hover: filled ink, white text.

**Spacing** (*Site Styles → Spacing*; **verify** the names in her account)
- [ ] Page max width **1600px**; site margins **48px** desktop, **20px** mobile (the prototype's margin is 3.4% of the width, between those).
- [ ] Fluid Engine gap between blocks **16px**. The desktop grid is **24 columns**, the mobile grid **8**: every block below gives both.
- [ ] Section spacing target: **144px** top and bottom at 1600px and wider (130px at 1440), **88px** on phones. Fluid Engine has no px field for this (F1).

**Animations, images**
- [ ] *Site Styles → Animations*: **Fade**, speed **Slow**. No parallax, no scroll effects.
- [ ] Image blocks by default: clickthrough **Lightbox**, caption **below**, no border, no shadow, corner radius **0** (CSS rule 6 enforces 0).

**Pages and navigation** (create them empty now; each page below fills one)
- [ ] **Home**: regular page, set as homepage.
- [ ] **Projects**: regular page, URL `/projects`, in the navigation as "Projects".
- [ ] **Case studies**: Portfolio page, URL `/projects-private`, **not linked** (not in the navigation). Its four project pages are built on pages 1–5.
- [ ] Navigation links: **About** → `/#snippets`, **Contact** → `/#contact` (anchor links to Home sections).

**Header** (*Edit Site Header*)
- [ ] Layout: site title left, navigation right. Site title as text: "Yasmin Bajwa", Inter Tight 15px. Navigation 15px, gap about 28px; the current page underlined.
- [ ] Style **Solid**, theme **White**, a 1px rule under it (14% ink): the header border setting if her template has one, else CSS rule 1. Mobile: the menu icon (F2).
- [ ] On the two photo-cover case studies (Rooms 01, 02) the header sits over the photo with white text: *header → transparent over the first section* (**verify** per-page header overlay).

**Footer** (*Edit Footer*, one Fluid Engine section shared by every page)
- [ ] Theme **White**; a **Line** block across the top (1px, 14% ink); 28px above and below the text.
- [ ] **Text** · cols 1–8 · mobile 1–4 · Paragraph 2 (prototype: 13px, 62% ink, F3):
  ```text
  © Yasmin Bajwa
  ```
- [ ] **Text** · cols 17–24, right-aligned · mobile 5–8 · Paragraph 2 (13px) · link → `#` (back to top), underlined:
  ```text
  Back to top ↑
  ```

**Files**: everything to upload is in this repository under `yasmin/site/assets/` (paths below start at `site/`). The zip `yasmin-portfolio-prototype.zip` has the same files.

<div style="page-break-after: always"></div>

## Page 1 · Portfolio collection: Case studies

- [ ] *Pages → +* **Portfolio** · title "Case studies" · URL `/projects-private` · **Not linked** (keep it out of the navigation).
- [ ] Portfolio layout: any (the grid is never shown publicly: the password locks it with the projects, and Home and Projects link straight to each project page).
- [ ] Inside it, four project pages in this order, built on Pages 2–5:
  - [ ] `/projects-private/jackson-home` · "The Henry Ford Jackson Home Visitor Flow Simulation"
  - [ ] `/projects-private/power-energy` · "Designing an Interactive Museum Experience for Power & Energy"
  - [ ] `/projects-private/rhode-island` · "Rhode Island State COVID Vaccine App/401 Health App"
  - [ ] `/projects-private/littelfuse` · "Reimagining How Engineers Discover Littelfuse Products"
- [ ] Password: **not yet**. Set it on Page 6 once all four pages are built (it protects the Portfolio and every project in it with one shared password).
- [ ] Saved sections to create while building Room 01 (heart icon on each, name them like this): *Case · cover*, *Case · meta card*, *Case · chapter index*, *Case · chapter (text)*, *Module · plate pair*, *Module · board 2×2*, *Module · board 1+3*, *Module · strip*, *Module · full plate*, *Module · video panel*, *Case · reflection*, *Case · prev-next*.

<div style="page-break-after: always"></div>

## Page 2 · Room 01 · The Henry Ford Jackson Home Visitor Flow Simulation

- [ ] *Case studies → +* project page · title as below · URL slug `/projects-private/jackson-home` · thumbnail: not needed (the Portfolio grid is never shown).
- [ ] Build this page **completely first**; save the cover, meta card, chapter index, each module, the Reflection and the prev/next section (heart icon → *My saved sections*). Pages 3–5 reuse them.
- [ ] Site Styles used: Heading 2–4, Paragraph 2–3, captions, Line blocks; module images; CSS rules 3–5 (lists) and 6 (corners).

### 2.1 · Cover (photo)
- [ ] **Section:** Blank section · content width **Full** · height **Large** · background image (below) · theme **Ink** text (white)
- [ ] **2.1.1 Section background image** · upload `site/assets/img/r3-cover-r01-16x7.jpg` · section **content width Full**, height **Large** (the photo is 16:7: about 630px tall at 1440) · background **overlay #111111 at 38%** · focal point centre · F4
- [ ] **2.1.2 Text** · cols 2–12 · mobile 1–8 · Heading 2
  ```text
  The Henry Ford Jackson Home Visitor Flow Simulation
  ```

### 2.2 · Meta table on a white card
- [ ] **Section:** **Same section as the cover**, in its bottom rows (F5)
- [ ] **2.2.1 Text** · cols 14–16 · mobile 1–8 · Paragraph 3 → Paragraph 2 (prototype: 15px, F3) (one block, one line per style)
  **Line** block above (1px ink, same columns)
  ```text
  Role
  UX Researcher | Experience Design
  ```
- [ ] **2.2.2 Text** · cols 17–21 · mobile 1–8 · Paragraph 3 → Paragraph 2 (prototype: 15px, F3) (one block, one line per style)
  **Line** block above (1px ink, same columns)
  ```text
  Methods
  Behavioral Observation • Space Syntax Analysis • Behavioral Path Clustering • Visitor Segmentation • Discrete Event Simulation • Predictive Modeling
  ```
- [ ] **2.2.3 Text** · cols 22–24 · mobile 1–8 · Paragraph 3 → Paragraph 2 (prototype: 15px, F3) (one block, one line per style)
  **Line** block above (1px ink, same columns)
  ```text
  Setting
  The Henry Ford, Greenfield Village
  ```

### 2.3 · Chapter index
- [ ] **Section:** Blank section · theme **White** · 1px ink Line blocks above and below the index
- [ ] **2.3.1 Text** · cols 1–24 · mobile 1–8 · Paragraph 2 (prototype: 14px, F3) · one line that wraps; **Line** blocks above and below (1px ink) · numbers in 62% ink, titles in ink
  links: "Project Overview" → `#ch-1` · "The Challenge" → `#ch-2` · "Research Questions" → `#ch-3` · "Research Methodology" → `#ch-4` · "Building the Simulation" → `#ch-5` · "Baseline Assumptions" → `#ch-6` · "Scenario Testing" → `#ch-7` · "Findings" → `#ch-8` · "Impact" → `#ch-9` · "Reflection" → `#ch-10`
  ```text
  01 Project Overview   02 The Challenge   03 Research Questions   04 Research Methodology   05 Building the Simulation   06 Baseline Assumptions   07 Scenario Testing   08 Findings   09 Impact   10 Reflection
  ```

### 2.4 · Chapter · Project Overview
- [ ] **Section:** Blank section · theme **White** · anchor link `ch-1` (*Edit Section → Anchor*) · space above 130px / below 0px at 1440 (mobile 88 / 0) (F1)
- [ ] **2.4.1 Text** · cols 1–6 · mobile 1–8 · Paragraph 3 (prototype: 14px, F3) → Heading 3 (one block, one line per style)
  ```text
  01
  Project Overview
  ```
- [ ] **2.4.2 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  The Dr. Sullivan and Mrs. Richie Jean Sherrod Jackson Home is a nationally significant historic residence associated with the 1965 Selma to Montgomery marches, where civil rights leaders, including Dr. Martin Luther King Jr., gathered to develop strategies that contributed to the passage of the Voting Rights Act. After being relocated to Greenfield Village at The Henry Ford museum, the home was prepared to open to the public as a permanent exhibition in Summer 2026.
  ```
- [ ] **2.4.3 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  As the first building added to Greenfield Village in more than forty years, there was no historical visitor data to guide operational planning. My role was to develop a predictive visitor flow model that would forecast how guests would move through the constrained historic space before opening day.
  ```
- [ ] **2.4.4 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  Using UX research methodologies and behavioral modeling, I created a visitor simulation that allowed stakeholders to evaluate different ticketing strategies, estimate visitor capacity, identify potential congestion points, and determine where presenters should be positioned to create a comfortable and engaging visitor experience.
  ```

### 2.5 · Chapter · The Challenge
- [ ] **Section:** Blank section · theme **White** · anchor link `ch-2` (*Edit Section → Anchor*) · space above 130px / below 0px at 1440 (mobile 88 / 0) (F1)
- [ ] **2.5.1 Text** · cols 1–6 · mobile 1–8 · Paragraph 3 (prototype: 14px, F3) → Heading 3 (one block, one line per style)
  ```text
  02
  The Challenge
  ```
- [ ] **2.5.2 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  No behavioral data existed, planning visitor capacity relied on assumptions rather than evidence. The home's preserved architectural layout introduced additional constraints:
  ```
- [ ] **2.5.3 Text** · cols 9–20 · mobile 1–8 · Bulleted list in Paragraph 2
  ```text
  Narrow circulation paths
  Limited room capacity
  Sequential visitor movement
  Preservation requirements that prevented structural modifications
  ```
- [ ] **2.5.4 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  The challenge became:
  ```
- [ ] **2.5.5 Text** · cols 9–20 · mobile 1–8 · Paragraph 1 (prototype: 28px, F6)
  ```text
  How might we predict visitor behavior and optimize the museum experience before the exhibition opened to the public?
  ```

### 2.6 · Chapter · Research Questions
- [ ] **Section:** Blank section · theme **White** · anchor link `ch-3` (*Edit Section → Anchor*) · space above 130px / below 0px at 1440 (mobile 88 / 0) (F1)
- [ ] **2.6.1 Text** · cols 1–6 · mobile 1–8 · Paragraph 3 (prototype: 14px, F3) → Heading 3 (one block, one line per style)
  ```text
  03
  Research Questions
  ```
- [ ] **2.6.2 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  To support exhibition planning, I focused on answering several key research questions.
  ```
- [ ] **2.6.3 Text** · cols 9–20 · mobile 1–8 · Heading 4
  **Line** block above (1px, 14% ink, same columns)
  ```text
  Visitor Experience
  ```
- [ ] **2.6.4 Text** · cols 9–20 · mobile 1–8 · Bulleted list in Paragraph 2
  ```text
  How long will visitors spend inside the home?
  Where are visitors most likely to stop or experience congestion?
  What will waiting times look like throughout the experience?
  ```
- [ ] **2.6.5 Text** · cols 9–20 · mobile 1–8 · Heading 4
  **Line** block above (1px, 14% ink, same columns)
  ```text
  Capacity Planning
  ```
- [ ] **2.6.6 Text** · cols 9–20 · mobile 1–8 · Bulleted list in Paragraph 2
  ```text
  How many visitors can comfortably occupy both the Jackson Home and Annex (complimentary building with digital interactives) without overcrowding?
  Should visitors enter through 15-minute or 30-minute ticketing windows?
  Can walk-up visitors be accommodated without negatively affecting the experience?
  ```
- [ ] **2.6.7 Text** · cols 9–20 · mobile 1–8 · Heading 4
  **Line** block above (1px, 14% ink, same columns)
  ```text
  Operations
  ```
- [ ] **2.6.8 Text** · cols 9–20 · mobile 1–8 · Bulleted list in Paragraph 2
  ```text
  Where should docents and presenters be positioned to support visitor flow?
  What traffic management strategies should staff use during peak attendance?
  ```

### 2.7 · Chapter · Research Methodology
- [ ] **Section:** Blank section · theme **White** · anchor link `ch-4` (*Edit Section → Anchor*) · space above 130px / below 0px at 1440 (mobile 88 / 0) (F1)
- [ ] Images keep her order; captions are "Fig. nn — …" in Paragraph 3 (the style uppercases them).
- [ ] **2.7.1 Text** · cols 1–6 · mobile 1–8 · Paragraph 3 (prototype: 14px, F3) → Heading 3 (one block, one line per style)
  ```text
  04
  Research Methodology
  ```
- [ ] **2.7.2 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  Because no baseline visitor data existed for the Jackson Home, I combined several UX research methodologies to build a predictive behavioral model.
  ```
- [ ] **2.7.3 Text** · cols 9–20 · mobile 1–8 · Heading 4
  **Line** block above (1px, 14% ink, same columns)
  ```text
  Behavioral Observation
  ```
- [ ] **2.7.4 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  I analyzed visitor movement within comparable historical homes and nearby exhibitions at The Henry Ford to understand common behavioral patterns. These observations focused on:
  ```
- [ ] **2.7.5 Text** · cols 9–20 · mobile 1–8 · Bulleted list in Paragraph 2
  ```text
  visitor arrival behavior
  walking speed
  dwell time
  congestion points
  exhibit engagement
  decision-making at transitions between rooms
  ```
- [ ] **2.7.6 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  These findings established the behavioral assumptions used throughout the simulation.
  ```
- [ ] **2.7.7 Text** · cols 9–20 · mobile 1–8 · Heading 4
  **Line** block above (1px, 14% ink, same columns)
  ```text
  Space Syntax Analysis
  ```
- [ ] **2.7.8 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  In collaboration with our experience design team I evaluated the home's architectural layout to understand how visibility, room connectivity, and circulation paths would naturally influence visitor movement. This helped identify areas likely to become bottlenecks before testing any operational scenarios.
  ```
- [ ] **2.7.9 Text** · cols 9–20 · mobile 1–8 · Heading 4
  **Line** block above (1px, 14% ink, same columns)
  ```text
  Behavioral Path Clustering
  ```
- [ ] **2.7.10 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  Behavioral observations revealed that visitors interact with museum environments differently depending on their engagement level. We simulate this behavior by randomly assigning a visitor type to each person and then reducing the average view time at each exhibit to give the correct %. This results in a very different time profile for each type of visitor to the Jackson Home: To reflect these differences, visitors were grouped into three behavioral archetypes based on existing museum research and validated using historical attendance patterns from The Henry Ford.
  ```
- [ ] **2.7.11 Text** · cols 1–24 · mobile 1–8 · Paragraph 3 → Paragraph 3 → Paragraph 3 (one block, one line per style)
  **Line** block above (1px ink, same columns)
  ```text
  Distribution
  Visitor Type
  Characteristics
  ```
- [ ] **2.7.12 Text** · cols 1–8 · mobile 1–8 · Heading 2 (prototype: 96px Inter Tight, F7) → Heading 4 (prototype: Inter Tight 24px, F6) → Paragraph 2 (prototype: 15px, F3) (one block, one line per style)
  ```text
  60%
  Strollers
  Browse most exhibits with moderate viewing time
  ```
- [ ] **2.7.13 Text** · cols 9–16 · mobile 1–8 · Heading 2 (prototype: 96px Inter Tight, F7) → Heading 4 (prototype: Inter Tight 24px, F6) → Paragraph 2 (prototype: 15px, F3) (one block, one line per style)
  ```text
  10%
  Studiers
  Read interpretation thoroughly and spend longer in each room
  ```
- [ ] **2.7.14 Text** · cols 17–24 · mobile 1–8 · Heading 2 (prototype: 96px Inter Tight, F7) → Heading 4 (prototype: Inter Tight 24px, F6) → Paragraph 2 (prototype: 15px, F3) (one block, one line per style)
  ```text
  30%
  Streakers
  Move quickly through the exhibition with minimal stopping
  ```
- [ ] **2.7.15 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  Each simulated visitor was randomly assigned one of these behavioral profiles, allowing the model to better represent realistic variation in visitor behavior.
  ```
- [ ] **Module · Plate pair**: a wide image (16 cols) beside a tall one (8 cols), tops and bottoms aligned; on mobile stacked in the order listed. Space above: 56px. Build it once, save it (heart icon), reuse it.
- [ ] **2.7.16 Image** · cols 1–8 · mobile 1–8 · upload `site/assets/img/tiles/r01-chart-onsite-box--0_750.jpg` · block shape **3:4** · **Fit**
  the tile already holds the light ground and padding, so nothing is cropped · lightbox on (opens the tile; full-size original: `site/assets/img/r01-chart-onsite-box.jpg`) · alt text: "Time spent on-site by visitor type"
  caption (**Caption: below**, Paragraph 3):
  ```text
  Fig. 01 — Time spent on-site by visitor type
  ```
- [ ] **2.7.17 Image** · cols 9–24 · mobile 1–8 · upload `site/assets/img/tiles/r01-chart-dataset-full--1_500.jpg` · block shape **3:2** · **Fit**
  the tile already holds the light ground and padding, so nothing is cropped · lightbox on (opens the tile; full-size original: `site/assets/img/r01-chart-dataset-full.jpg`) · alt text: "Congestion, queue sizes, visit time and delays"
  caption (**Caption: below**, Paragraph 3):
  ```text
  Fig. 02 — Congestion, queue sizes, visit time and delays
  ```

### 2.8 · Chapter · Building the Simulation
- [ ] **Section:** Blank section · theme **White** · anchor link `ch-5` (*Edit Section → Anchor*) · space above 130px / below 0px at 1440 (mobile 88 / 0) (F1)
- [ ] Images keep her order; captions are "Fig. nn — …" in Paragraph 3 (the style uppercases them).
- [ ] **2.8.1 Text** · cols 1–6 · mobile 1–8 · Paragraph 3 (prototype: 14px, F3) → Heading 3 (one block, one line per style)
  ```text
  05
  Building the Simulation
  ```
- [ ] **2.8.2 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  Using behavioral research, I developed a discrete event simulation that modeled individual visitor movement throughout the exhibition. The simulation followed wayfinding based on the expected paths in the home, displayed below. Each visitor independently navigated the home while interacting with operational constraints including:
  ```
- [ ] **2.8.3 Text** · cols 9–20 · mobile 1–8 · Bulleted list in Paragraph 2
  ```text
  timed ticket arrivals
  room occupancy limits
  queue formation
  walking speed
  exhibit dwell time
  presenter intervention
  alternative routing when spaces reached capacity
  ```
- [ ] **2.8.4 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  Rather than moving visitors as a group, every individual made independent movement decisions based on available space and predefined behavioral rules. This allowed the simulation to realistically forecast congestion and visitor flow under multiple operational scenarios.
  ```
- [ ] **Module · Plate pair**: a wide image (16 cols) beside a tall one (8 cols), tops and bottoms aligned; on mobile stacked in the order listed. Space above: 56px. Build it once, save it (heart icon), reuse it.
- [ ] **2.8.5 Image** · cols 1–8 · mobile 1–8 · upload `site/assets/img/tiles/r01-plan-plain--0_750.jpg` · block shape **3:4** · **Fit**
  the tile already holds the light ground and padding, so nothing is cropped · lightbox on (opens the tile; full-size original: `site/assets/img/r01-plan-plain.jpg`) · alt text: "Jackson Home floor plan"
  caption (**Caption: below**, Paragraph 3):
  ```text
  Fig. 03 — Jackson Home floor plan
  ```
- [ ] **2.8.6 Image** · cols 9–24 · mobile 1–8 · upload `site/assets/img/tiles/r01-plan-annex--1_500.jpg` · block shape **3:2** · **Fit**
  the tile already holds the light ground and padding, so nothing is cropped · lightbox on (opens the tile; full-size original: `site/assets/img/r01-plan-annex.jpg`) · alt text: "The Annex floor plan, with site entrance, entrance line and vestibule"
  caption (**Caption: below**, Paragraph 3):
  ```text
  Fig. 04 — The Annex floor plan, with site entrance, entrance line and vestibule
  ```
- [ ] **Module · Video panel**: the video in cols 1–16, its caption and running time in cols 17–24 under a Line. Space above: 56px. Build it once, save it (heart icon), reuse it.
- [ ] **2.8.7 Video** · cols 1–16 · mobile 1–8 · upload `site/assets/video/r01-simulation.mp4` · thumbnail `site/assets/img/poster-r01-simulation.jpg` · controls on, autoplay off
- [ ] **2.8.8 Text** · cols 17–24 · mobile 1–8 (below the video) · bottom-aligned · **Line** block above (1px ink) · Paragraph 3 → Paragraph 3
  ```text
  Fig. 05 — Discrete event simulation of visitor flow
  Running time 0:48
  ```

### 2.9 · Chapter · Baseline Assumptions
- [ ] **Section:** Blank section · theme **White** · anchor link `ch-6` (*Edit Section → Anchor*) · space above 130px / below 0px at 1440 (mobile 88 / 0) (F1)
- [ ] **2.9.1 Image** · cols 1–11 · mobile 1–8 · upload `site/assets/img/tiles/r01-plan-paths--0_667.jpg` · block shape **2:3** · **Fit**
  the tile already holds the light ground and padding, so nothing is cropped · lightbox on (opens the tile; full-size original: `site/assets/img/r01-plan-paths.jpg`) · alt text: "Jackson Home floor plan with expected visitor paths"
  caption (**Caption: below**, Paragraph 3):
  ```text
  Fig. 06 — Jackson Home floor plan with expected visitor paths
  ```
- [ ] **2.9.2 Text** · cols 14–24 · mobile 1–8 · Paragraph 3 (prototype: 14px, F3) → Heading 3 (one block, one line per style)
  ```text
  06
  Baseline Assumptions
  ```
- [ ] **2.9.3 Text** · cols 14–24 · mobile 1–8 · Paragraph 2
  ```text
  Since the exhibition had not yet opened, several assumptions were established using observations from comparable exhibitions. These assumptions provided a consistent foundation for comparing operational scenarios.
  ```
- [ ] **2.9.4 Text** · cols 14–24 · mobile 1–8 · Paragraph 2
  ```text
  These included:
  ```
- [ ] **2.9.5 Text** · cols 14–24 · mobile 1–8 · Bulleted list in Paragraph 2
  ```text
  Visitors arrive within their assigned ticket window.
  Ticket windows operate in either 15-minute or 30-minute intervals.
  Visitors travel independently while naturally clustering into small social groups.
  Average walking speed is approximately 2.0 mph, representing most museum visitors.
  Each exhibit has a maximum occupancy determined by available floor space.
  When capacity is reached, visitors either wait or continue to another available location.
  Individual viewing times vary according to visitor type and natural behavioral variation.
  ```

### 2.10 · Chapter · Scenario Testing
- [ ] **Section:** Blank section · theme **White** · anchor link `ch-7` (*Edit Section → Anchor*) · space above 130px / below 0px at 1440 (mobile 88 / 0) (F1)
- [ ] Images keep her order; captions are "Fig. nn — …" in Paragraph 3 (the style uppercases them).
- [ ] **2.10.1 Text** · cols 1–6 · mobile 1–8 · Paragraph 3 (prototype: 14px, F3) → Heading 3 (one block, one line per style)
  ```text
  07
  Scenario Testing
  ```
- [ ] **2.10.2 Text** · cols 9–20 · mobile 1–8 · Heading 4
  **Line** block above (1px, 14% ink, same columns)
  ```text
  STUDY FACTORS
  ```
- [ ] **2.10.3 Text** · cols 9–20 · mobile 1–8 · Bulleted list in Paragraph 2
  indented lines are a nested list (Tab)
  ```text
  Ticketing Window:
      30-minute windows
      15-minute windows
  Arrival Pattern:
      Random times within ticketing window
      All arrive at start of ticketing window
  Docent Control:
      No constraint – visitors enter if there is space in the vestibule
      With constraint – docent allows ~8 people at a time into entrance area (Vestibule, Pre 1965 and Video Wall)
  Number of tickets:
      Base: 48 per 30-minutes or 24 per 15-minutes
      Low: 38 per 30-minutes or 20 per 15-minutes
      High: 58 per 30-minutes or 28 per 15-minutes
  Walk-up Visitors:
      A limited number of un-ticketed visitors may be allowed to join the queue if the ticketed visitors have entered the building
  ```
- [ ] **2.10.4 Text** · cols 9–20 · mobile 1–8 · Heading 4
  **Line** block above (1px, 14% ink, same columns)
  ```text
  Ticketing Window & Arrival Patterns
  ```
- [ ] **2.10.5 Text** · cols 9–20 · mobile 1–8 · Bulleted list in Paragraph 2
  indented lines are a nested list (Tab)
  ```text
  The effects of these factors are linked
  If visitor arrivals are spread randomly through the ticketing window
      Congestion and queue sizes are low
      Visitors rarely have to skip exhibits
      Total time spent on-site matches expectations
      There is no significant difference between 30-minute or 15-minute ticketing windows
  ```
- [ ] **2.10.6 Text** · cols 9–20 · mobile 1–8 · Heading 4
  **Line** block above (1px, 14% ink, same columns)
  ```text
  Ticketing Window & Arrival Patterns
  ```
- [ ] **2.10.7 Text** · cols 9–20 · mobile 1–8 · Bulleted list in Paragraph 2
  indented lines are a nested list (Tab)
  ```text
  If most visitors arrive close to the start of the ticketing window
      Congestion and queue sizes are high
      With no docent control at the entrance, skipping behavior balloons
          This could result in many unhappy visitors!
      Average time spent on-site increases by just a few minutes, but the maximum time on-site almost doubles!
      In this case, all indicators are much better if 15-minute ticketing windows are used
  ```
- [ ] **Module · Board 2×2**: four image blocks, cols 1–12 / 13–24, all 1:1 (or a Gallery section → Grid: Simple, 2 columns, 1:1, 24px spacing); one column on mobile. Space above: 56px. Build it once, save it (heart icon), reuse it.
- [ ] **2.10.8 Image** · cols 1–12 · mobile 1–8 · upload `site/assets/img/tiles/r01-chart-arrivals-random--1_000.jpg` · block shape **1:1** · **Fit**
  the tile already holds the light ground and padding, so nothing is cropped · lightbox on (opens the tile; full-size original: `site/assets/img/r01-chart-arrivals-random.jpg`) · alt text: "Arrivals spread randomly through the ticketing window"
  caption (**Caption: below**, Paragraph 3):
  ```text
  Fig. 07 — Arrivals spread randomly through the ticketing window
  ```
- [ ] **2.10.9 Image** · cols 13–24 · mobile 1–8 · upload `site/assets/img/tiles/r01-chart-arrivals-ontime--1_000.jpg` · block shape **1:1** · **Fit**
  the tile already holds the light ground and padding, so nothing is cropped · lightbox on (opens the tile; full-size original: `site/assets/img/r01-chart-arrivals-ontime.jpg`) · alt text: "Arrivals at the start of the ticketing window"
  caption (**Caption: below**, Paragraph 3):
  ```text
  Fig. 08 — Arrivals at the start of the ticketing window
  ```
- [ ] **2.10.10 Image** · cols 1–12 · mobile 1–8 · upload `site/assets/img/tiles/r3-fig-visit-times--1_000.jpg` · block shape **1:1** · **Fit**
  the tile already holds the light ground and padding, so nothing is cropped · lightbox on (opens the tile; full-size original: `site/assets/img/r3-fig-visit-times.jpg`) · alt text: "Expected visit times by visitor type"
  caption (**Caption: below**, Paragraph 3):
  ```text
  Fig. 09 — Expected visit times by visitor type
  ```
- [ ] **2.10.11 Image** · cols 13–24 · mobile 1–8 · upload `site/assets/img/tiles/r01-chart-docent--1_000.jpg` · block shape **1:1** · **Fit**
  the tile already holds the light ground and padding, so nothing is cropped · lightbox on (opens the tile; full-size original: `site/assets/img/r01-chart-docent.jpg`) · alt text: "Skipped exhibits, without and with docent control"
  caption (**Caption: below**, Paragraph 3):
  ```text
  Fig. 10 — Skipped exhibits, without and with docent control
  ```

### 2.11 · Chapter · Findings
- [ ] **Section:** Blank section · theme **White** · anchor link `ch-8` (*Edit Section → Anchor*) · space above 130px / below 0px at 1440 (mobile 88 / 0) (F1)
- [ ] Images keep her order; captions are "Fig. nn — …" in Paragraph 3 (the style uppercases them).
- [ ] **2.11.1 Text** · cols 1–6 · mobile 1–8 · Paragraph 3 (prototype: 14px, F3) → Heading 3 (one block, one line per style)
  ```text
  08
  Findings
  ```
- [ ] **2.11.2 Text** · cols 9–20 · mobile 1–8 · Numbered list in Paragraph 2
  **Line** block above (1px ink, same columns)
  ```text
  Ticketing StrategyVisitors were expected to arrive near the beginning of their assigned ticket windows, particularly during the exhibition's opening months.A 15-minute ticketing schedule distributed arrivals more evenly than 30-minute windows, reducing congestion throughout the home.
  CapacityWhile the home could accommodate a maximum of approximately 32 visitors every 15 minutes, a capacity of 30 visitors per entry window created a noticeably more comfortable visitor experience while maintaining operational efficiency.
  Presenter PlacementSimulation results demonstrated that placing presenters near the first exhibits significantly improved visitor flow.Presenters helped regulate entry into high-demand spaces, reduced skipped exhibits, and minimized bottlenecks during periods of heavy attendance. The recommended staffing model included three to four presenters positioned throughout key zones of the home during opening operations.
  Walk-Up VisitorsAllowing a controlled mix of ticketed and walk-up visitors naturally staggered arrivals, reducing congestion and average waiting times while increasing access for guests unable to reserve tickets in advance.
  ```
- [ ] **Module · Full plate**: one image block across cols 1–24. Space above: 56px. Build it once, save it (heart icon), reuse it.
- [ ] **2.11.3 Image** · cols 1–24 · mobile 1–8 · upload `site/assets/img/tiles/r01-chart-best-full--1_983.jpg` · block shape **2:1** · **Fit**
  the tile already holds the light ground and padding, so nothing is cropped · lightbox on (opens the tile; full-size original: `site/assets/img/r01-chart-best-full.jpg`) · alt text: "Best scenario: 20 tickets, 8 walk-ups, with docent control"
  caption (**Caption: below**, Paragraph 3):
  ```text
  Fig. 11 — Best scenario: 20 tickets, 8 walk-ups, with docent control
  ```

### 2.12 · Chapter · Impact
- [ ] **Section:** Blank section · theme **White** · anchor link `ch-9` (*Edit Section → Anchor*) · space above 130px / below 0px at 1440 (mobile 88 / 0) (F1)
- [ ] **2.12.1 Text** · cols 1–6 · mobile 1–8 · Paragraph 3 (prototype: 14px, F3) → Heading 3 (one block, one line per style)
  ```text
  09
  Impact
  ```
- [ ] **2.12.2 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  The visitor flow simulation provided stakeholders with evidence-based recommendations before the Jackson Home opened to the public. The research directly informed operational planning by helping teams:
  ```
- [ ] **2.12.3 Text** · cols 9–20 · mobile 1–8 · Numbered list in Paragraph 2
  **Line** block above (1px ink, same columns)
  ```text
  establish ticketing schedules for opening operations
  determine comfortable visitor capacity limits
  identify high-congestion areas before opening
  optimize presenter placement throughout the home
  evaluate queue management strategies
  deciding factor for where to place digital interactives in the exhibit
  improve visitor flow while preserving the historic integrity of the building
  ```
- [ ] **2.12.4 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  Rather than relying on assumptions alone, leadership was able to make operational decisions supported by predictive behavioral research and simulation.
  ```

### 2.13 · Reflection
- [ ] **Section:** Blank section · theme **Stone** · anchor link `ch-10` · text centred · space above 130px / below 130px at 1440 (mobile 88 / 88) (F1)
- [ ] **2.13.1 Text** · cols 7–18 · mobile 1–8 · Paragraph 3 · centred
  ```text
  10
  ```
- [ ] **2.13.2 Text** · cols 7–18 · mobile 1–8 · Heading 4 (prototype: 14px, weight 500; nearest Paragraph 3 if 14px isn't possible, F3) · centred
  ```text
  Reflection
  ```
- [ ] **2.13.3 Text** · cols 7–18 · mobile 1–8 · Paragraph 1 italic (prototype: 28px, F6) · centred
  ```text
  This project broadened my understanding of user experience beyond digital products, demonstrating how UX research methodologies can be applied to improve experiences within physical environments. It also deepened my appreciation for how visitors engage with and process complex, emotionally significant stories, particularly those centered on difficult history
  ```
- [ ] **2.13.4 Text** · cols 7–18 · mobile 1–8 · Paragraph 3 · centred
  ```text
  —
  ```

### 2.14 · Previous / all / next
- [ ] **Section:** Blank section · theme **White** · a 1px ink **Line** block across the top · 28px above, 40px below
- [ ] **Line** block · cols 1–24 · 1px ink · at the top of the section
- [ ] **2.14.1 Text** · cols 1–8 · mobile 1–8 · Paragraph 3 → Heading 4 (one block, one line per style)
  link the whole text → `/projects-private/littelfuse`
  ```text
  ← Previous project
  Reimagining How Engineers Discover Littelfuse Products
  ```
- [ ] **2.14.2 Text** · cols 10–15 · mobile 1–8 · Paragraph 3
  link the whole text → `/projects`
  ```text
  All projects
  ```
- [ ] **2.14.3 Text** · cols 17–24 · mobile 1–8 · Paragraph 3 → Heading 4 (one block, one line per style)
  link the whole text → `/projects-private/power-energy`
  ```text
  Next project →
  Designing an Interactive Museum Experience for Power & Energy
  ```

### 2.15 · Footer
- [ ] Nothing to build: the site footer (Page 0).

<div style="page-break-after: always"></div>

## Page 3 · Room 02 · Designing an Interactive Museum Experience for Power & Energy

- [ ] *Case studies → +* project page · title as below · URL slug `/projects-private/power-energy` · thumbnail: not needed (the Portfolio grid is never shown).
- [ ] Start from a **duplicate** of Room 01 (*Pages → ⋯ → Duplicate*, **verify**) or from the saved sections; replace every text and image with the ones below.
- [ ] Site Styles used: Heading 2–4, Paragraph 2–3, captions, Line blocks; module images; CSS rules 3–5 (lists) and 6 (corners).

### 3.1 · Cover (photo)
- [ ] **Section:** Blank section · content width **Full** · height **Large** · background image (below) · theme **Ink** text (white)
- [ ] **3.1.1 Section background image** · upload `site/assets/img/r3-cover-r02-16x7.jpg` · section **content width Full**, height **Large** (the photo is 16:7: about 630px tall at 1440) · background **overlay #111111 at 38%** · focal point centre · F4
- [ ] **3.1.2 Text** · cols 2–12 · mobile 1–8 · Heading 2
  ```text
  Designing an Interactive Museum Experience for Power & Energy
  ```

### 3.2 · Meta table on a white card
- [ ] **Section:** **Same section as the cover**, in its bottom rows (F5)
- [ ] **3.2.1 Text** · cols 14–16 · mobile 1–8 · Paragraph 3 → Paragraph 2 (prototype: 15px, F3) (one block, one line per style)
  **Line** block above (1px ink, same columns)
  ```text
  Role
  UX Designer| Experience Design | Project Management
  ```
- [ ] **3.2.2 Text** · cols 17–21 · mobile 1–8 · Paragraph 3 → Paragraph 2 (prototype: 15px, F3) (one block, one line per style)
  **Line** block above (1px ink, same columns)
  ```text
  Methods
  Information Architecture • User Flows • Wireframing • Content Strategy
  ```
- [ ] **3.2.3 Text** · cols 22–24 · mobile 1–8 · Paragraph 3 → Paragraph 2 (prototype: 15px, F3) (one block, one line per style)
  **Line** block above (1px ink, same columns)
  ```text
  Setting
  The Henry Ford Museum, Power & Energy exhibit
  ```

### 3.3 · Chapter index
- [ ] **Section:** Blank section · theme **White** · 1px ink Line blocks above and below the index
- [ ] **3.3.1 Text** · cols 1–24 · mobile 1–8 · Paragraph 2 (prototype: 14px, F3) · one line that wraps; **Line** blocks above and below (1px ink) · numbers in 62% ink, titles in ink
  links: "Project Overview" → `#ch-1` · "The Challenge" → `#ch-2` · "The Approach/ UX Design" → `#ch-3` · "Discovery & Stakeholder Alignment" → `#ch-4` · "Designing the Interactive Experience" → `#ch-5` · "CMS Integration & Implementation" → `#ch-6` · "Installation & Fabrication" → `#ch-7` · "Results & Impact" → `#ch-8` · "Ongoing Evaluation" → `#ch-9` · "Reflection" → `#ch-10`
  ```text
  01 Project Overview   02 The Challenge   03 The Approach/ UX Design   04 Discovery & Stakeholder Alignment   05 Designing the Interactive Experience   06 CMS Integration & Implementation   07 Installation & Fabrication   08 Results & Impact   09 Ongoing Evaluation   10 Reflection
  ```

### 3.4 · Chapter · Project Overview
- [ ] **Section:** Blank section · theme **White** · anchor link `ch-1` (*Edit Section → Anchor*) · space above 130px / below 0px at 1440 (mobile 88 / 0) (F1)
- [ ] **3.4.1 Text** · cols 1–6 · mobile 1–8 · Paragraph 3 (prototype: 14px, F3) → Heading 3 (one block, one line per style)
  ```text
  01
  Project Overview
  ```
- [ ] **3.4.2 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  The goal of this project was to enhance The Henry Ford Museum’s Power & Energy exhibit through a multi-sided interactive digital column that serves as both a visual entrance marker and a centralized storytelling experience. Furthermore, the column was inspired by an existing column in a nearby exhibit.
  ```
- [ ] **3.4.3 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  The column was designed for student groups, families, and general museum visitors, the column combines video content, interactive content, wayfinding, and artifact highlights to communicate the exhibit’s central themes—including the interconnectedness and tradeoffs involved in energy production, distribution, and use.
  ```
- [ ] **3.4.4 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  The experience also incorporates content from project partner ITC( International Transmission Company) and was built in Appspace, the museum’s institutional content management system, allowing internal teams to maintain and update the experience over time.
  ```

### 3.5 · Chapter · The Challenge
- [ ] **Section:** Blank section · theme **White** · anchor link `ch-2` (*Edit Section → Anchor*) · space above 130px / below 0px at 1440 (mobile 88 / 0) (F1)
- [ ] **3.5.1 Text** · cols 1–6 · mobile 1–8 · Paragraph 3 (prototype: 14px, F3) → Heading 3 (one block, one line per style)
  ```text
  02
  The Challenge
  ```
- [ ] **3.5.2 Text** · cols 9–20 · mobile 1–8 · Heading 4
  **Line** block above (1px, 14% ink, same columns)
  ```text
  Capturing Visitor Attention
  ```
- [ ] **3.5.3 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  In an exhibit filled with large-scale artifacts and live programming, the digital column needed to capture attention without competing with the physical environment.
  ```
- [ ] **3.5.4 Text** · cols 9–20 · mobile 1–8 · Paragraph 1 (prototype: 28px, F6)
  ```text
  How might we create an intuitive digital experience that encourages visitors of all ages to pause, explore, and learn?
  ```
- [ ] **3.5.5 Text** · cols 9–20 · mobile 1–8 · Heading 4
  **Line** block above (1px, 14% ink, same columns)
  ```text
  Balancing Museum and Sponsor Goals
  ```
- [ ] **3.5.6 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  The experience needed to support The Henry Ford’s educational mission while incorporating ITC’s industry, career, and employee stories without feeling overly promotional.
  ```
- [ ] **3.5.7 Text** · cols 9–20 · mobile 1–8 · Paragraph 1 (prototype: 28px, F6)
  ```text
  How might we introduce students to careers in power and energy while balancing visitor, museum, and sponsor needs?
  ```

### 3.6 · Chapter · The Approach/ UX Design
- [ ] **Section:** Blank section · theme **White** · anchor link `ch-3` (*Edit Section → Anchor*) · space above 130px / below 0px at 1440 (mobile 88 / 0) (F1)
- [ ] Images keep her order; captions are "Fig. nn — …" in Paragraph 3 (the style uppercases them).
- [ ] **3.6.1 Text** · cols 1–6 · mobile 1–8 · Paragraph 3 (prototype: 14px, F3) → Heading 3 (one block, one line per style)
  ```text
  03
  The Approach/ UX Design
  ```
- [ ] **3.6.2 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  To address visitor, educational, wayfinding, and sponsor needs, I developed a multi-sided experience that combined passive storytelling with touch-based exploration. Each side of the column served a distinct purpose while contributing to a cohesive visitor journey.
  ```
- [ ] **3.6.3 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  The experience included:
  ```
- [ ] **3.6.4 Text** · cols 9–20 · mobile 1–8 · Bulleted list in Paragraph 2
  ```text
  Exhibit wayfinding: A backlit graphic identifying the Power & Energy exhibit and introducing its central themes.
  Innovation stories: Condensed Innovation Nation episodes highlighting innovation across power and energy. Innovation Nation is an educational television series produced by The Henry Ford that explores inventions, innovators, and technological advancements shaping the world.
  Interactive exploration: A touch-based map visualizing power transmission infrastructure across Michigan and the United States.
  Career discovery: ITC employee interviews introducing students to careers within the power and energy industry.
  Artifact interpretation: A backlit graphic highlighting key artifacts and providing additional historical context based on what was inside the exhibit.
  ```
- [ ] **Module · Strip**: tiles side by side at the tile ratio, captions **above** (F8); two columns on mobile. Space above: 56px. Build it once, save it (heart icon), reuse it.
- [ ] **3.6.5 Image** · cols 1–5 · mobile 1–4 · upload `site/assets/img/tiles/r02-side-wayfinding--0_281.jpg` · block shape **9:32** · **Fit**
  the tile already holds the light ground and padding, so nothing is cropped · lightbox on (opens the tile; full-size original: `site/assets/img/r02-side-wayfinding.jpg`) · alt text: "Column side: Exhibit wayfinding"
  caption (**Caption: below**, Paragraph 3):
  ```text
  Fig. 01 — Column side: Exhibit wayfinding
  ```
- [ ] **3.6.6 Image** · cols 6–10 · mobile 5–8 · upload `site/assets/img/tiles/r02-side-stories--0_281.jpg` · block shape **9:32** · **Fit**
  the tile already holds the light ground and padding, so nothing is cropped · lightbox on (opens the tile; full-size original: `site/assets/img/r02-side-stories.jpg`) · alt text: "Column side: Innovation stories"
  caption (**Caption: below**, Paragraph 3):
  ```text
  Fig. 02 — Column side: Innovation stories
  ```
- [ ] **3.6.7 Image** · cols 11–14 · mobile 1–4 · upload `site/assets/img/tiles/r02-side-map--0_281.jpg` · block shape **9:32** · **Fit**
  the tile already holds the light ground and padding, so nothing is cropped · lightbox on (opens the tile; full-size original: `site/assets/img/r02-side-map.jpg`) · alt text: "Column side: Interactive exploration"
  caption (**Caption: below**, Paragraph 3):
  ```text
  Fig. 03 — Column side: Interactive exploration
  ```
- [ ] **3.6.8 Image** · cols 15–19 · mobile 5–8 · upload `site/assets/img/tiles/r02-side-careers--0_281.jpg` · block shape **9:32** · **Fit**
  the tile already holds the light ground and padding, so nothing is cropped · lightbox on (opens the tile; full-size original: `site/assets/img/r02-side-careers.jpg`) · alt text: "Column side: Career discovery"
  caption (**Caption: below**, Paragraph 3):
  ```text
  Fig. 04 — Column side: Career discovery
  ```
- [ ] **3.6.9 Image** · cols 20–24 · mobile 1–4 · upload `site/assets/img/tiles/r02-side-artifacts--0_281.jpg` · block shape **9:32** · **Fit**
  the tile already holds the light ground and padding, so nothing is cropped · lightbox on (opens the tile; full-size original: `site/assets/img/r02-side-artifacts.jpg`) · alt text: "Column side: Artifact interpretation"
  caption (**Caption: below**, Paragraph 3):
  ```text
  Fig. 05 — Column side: Artifact interpretation
  ```
- [ ] **3.6.10 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  I began to take the existing column we have in the Agriculture column and talk through how the Power & Energy column would look and feel. In addition I began to sketch and create lo- fi wireframes to share with key stakeholders for feedback( See below).
  ```
- [ ] **Module · Plate pair**: a wide image (16 cols) beside a tall one (8 cols), tops and bottoms aligned; on mobile stacked in the order listed. Space above: 56px. Build it once, save it (heart icon), reuse it.
- [ ] **3.6.11 Image** · cols 1–16 · mobile 1–8 · upload `site/assets/img/tiles/r02-concept-board--1_500.jpg` · block shape **3:2** · **Fit**
  the tile already holds the light ground and padding, so nothing is cropped · lightbox on (opens the tile; full-size original: `site/assets/img/r02-concept-board.jpg`) · alt text: "Content themes and experience flow for the column"
  caption (**Caption: below**, Paragraph 3):
  ```text
  Fig. 06 — Content themes and experience flow for the column
  ```
- [ ] **3.6.12 Image** · cols 17–24 · mobile 1–8 · upload `site/assets/img/tiles/r4-whiteboard-stack--0_750.jpg` · block shape **3:4** · **Fit**
  the tile already holds the light ground and padding, so nothing is cropped · lightbox on (opens the tile; full-size original: `site/assets/img/r4-whiteboard-stack.jpg`) · alt text: "Lo-fi sketches and wireframes for the column"
  caption (**Caption: below**, Paragraph 3):
  ```text
  Fig. 07 — Lo-fi sketches and wireframes for the column
  ```

### 3.7 · Chapter · Discovery & Stakeholder Alignment
- [ ] **Section:** Blank section · theme **White** · anchor link `ch-4` (*Edit Section → Anchor*) · space above 130px / below 0px at 1440 (mobile 88 / 0) (F1)
- [ ] Images keep her order; captions are "Fig. nn — …" in Paragraph 3 (the style uppercases them).
- [ ] **3.7.1 Text** · cols 1–6 · mobile 1–8 · Paragraph 3 (prototype: 14px, F3) → Heading 3 (one block, one line per style)
  ```text
  04
  Discovery & Stakeholder Alignment
  ```
- [ ] **3.7.2 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  Once the content strategy for each side of the column was established, I began developing the individual experiences and determining how each could support the broader goals of the Power & Energy exhibit. Visually, the backlit graphics were designed to maintain consistency with the existing exhibit while the interactive content introduced new opportunities for visitor engagement.
  ```
- [ ] **3.7.3 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  For the ITC career experience, the goal was to introduce visitors to the range of careers that support the power and energy industry. Working with ITC stakeholders, I identified three employee volunteers representing different areas of the organization: Safety & Security, Engineering, and Community Planning. I interviewed each employee about their role, responsibilities, career path, and connection to the energy industry. These conversations became the foundation for the career-focused content featured within the interactive. Employee interviews and responses informed the content shown below. Furthermore, below is a summary of highlighted content that was relevant and used in the final wireframes
  ```
- [ ] **Module · Full plate**: one image block across cols 1–24. Space above: 56px. Build it once, save it (heart icon), reuse it.
- [ ] **3.7.4 Image** · cols 1–24 · mobile 1–8 · upload `site/assets/img/tiles/r02-itc-full--1_600.jpg` · block shape **16:10** · **Fit**
  the tile already holds the light ground and padding, so nothing is cropped · lightbox on (opens the tile; full-size original: `site/assets/img/r02-itc-full.jpg`) · alt text: "ITC employee research: three roles"
  caption (**Caption: below**, Paragraph 3):
  ```text
  Fig. 08 — ITC employee research: three roles
  ```
- [ ] **3.7.5 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  In addition to the employee stories, I explored how the experience could connect careers in energy to objects, stories, and experiences visitors could encounter elsewhere in the museum. I developed short prompts for each career area using The Henry Ford’s Model i framework, an educational model that encourages learners to develop the habits and actions of innovators through curiosity, questioning, collaboration, and problem-solving. Because engaging younger visitors was an important project goal, these prompts were intentionally written to encourage exploration beyond the screen—connecting the digital experience back to the physical museum and inviting visitors to continue discovering how innovation, engineering, safety, and community planning shape the world around them.
  ```
- [ ] **3.7.6 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  Excerpts from the UX copy below:
  ```
- [ ] **3.7.7 Text** · cols 9–20 · mobile 1–8 · Paragraph 2 italic (prototype: 20px, F9)
  bold: "“Engineering Together:"
  ```text
  “Engineering Together: Thomas Edison employed dozens of engineers, inventors, and chemists at the Menlo Park Laboratory, where they collectively developed hundreds of technological innovations. Experience Menlo Park Laboratory for yourself in Greenfield Village.”
  ```
- [ ] **3.7.8 Text** · cols 9–20 · mobile 1–8 · Paragraph 2 italic (prototype: 20px, F9)
  bold: "“Safety & Security:"
  ```text
  “Safety & Security: As electric companies built new infrastructure around the country, they hired workers to construct and inspect the new poles and lines. To learn more, visit the Edison Illuminating Company’s Station A in Greenfield Village.”
  ```
- [ ] **3.7.9 Text** · cols 9–20 · mobile 1–8 · Paragraph 2 italic (prototype: 20px, F9)
  bold: "“Community Planning:"
  ```text
  “Community Planning: Thomas Edison tested and gathered feedback on his experimental lighting system with the men and women who lived at the Sarah Jordan Boarding House. Step inside the Boarding House in Greenfield Village.”
  ```

### 3.8 · Chapter · Designing the Interactive Experience
- [ ] **Section:** Blank section · theme **White** · anchor link `ch-5` (*Edit Section → Anchor*) · space above 130px / below 0px at 1440 (mobile 88 / 0) (F1)
- [ ] Images keep her order; captions are "Fig. nn — …" in Paragraph 3 (the style uppercases them).
- [ ] **3.8.1 Text** · cols 1–6 · mobile 1–8 · Paragraph 3 (prototype: 14px, F3) → Heading 3 (one block, one line per style)
  ```text
  05
  Designing the Interactive Experience
  ```
- [ ] **3.8.2 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  I then began finalizing the experience, focusing on the interaction touchpoints, content flow, and visual design. This was an iterative process informed by an existing interactive column within the museum’s Agriculture exhibit.
  ```
- [ ] **3.8.3 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  I began by evaluating the Agriculture column’s existing user flow, including its interaction rules, touchpoints, and the way content was distributed across the different sides of the column. I also reviewed findings from previous guest observations to understand how visitors actually approached, navigated, and engaged with the experience.
  ```
- [ ] **3.8.4 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  These behavioral insights became an important input into the final design. They helped determine how visitors would move through the Power & Energy experience, which types of content were best suited for each side of the column, and how the overall interaction flow should be structured.
  ```
- [ ] **3.8.5 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  The resulting flow and content distribution are illustrated in the diagram below. The final wireframes shown below.
  ```
- [ ] **Module · Full plate**: one image block across cols 1–24. Space above: 56px. Build it once, save it (heart icon), reuse it.
- [ ] **3.8.6 Image** · cols 1–24 · mobile 1–8 · upload `site/assets/img/tiles/r02-sides-full--1_600.jpg` · block shape **16:10** · **Fit**
  the tile already holds the light ground and padding, so nothing is cropped · lightbox on (opens the tile; full-size original: `site/assets/img/r02-sides-full.jpg`) · alt text: "Content distribution across the sides of the column"
  caption (**Caption: below**, Paragraph 3):
  ```text
  Fig. 09 — Content distribution across the sides of the column
  ```
- [ ] **Module · Video panel**: the video in cols 1–16, its caption and running time in cols 17–24 under a Line. Space above: 56px. Build it once, save it (heart icon), reuse it.
- [ ] **3.8.7 Video** · cols 1–16 · mobile 1–8 · upload `site/assets/video/r02-interface.mp4` · thumbnail `site/assets/img/poster-r02-interface.jpg` · controls on, autoplay off
- [ ] **3.8.8 Text** · cols 17–24 · mobile 1–8 (below the video) · bottom-aligned · **Line** block above (1px ink) · Paragraph 3 → Paragraph 3
  ```text
  Fig. 10 — Final interface and user flow
  Running time 0:22
  ```

### 3.9 · Chapter · CMS Integration & Implementation
- [ ] **Section:** Blank section · theme **White** · anchor link `ch-6` (*Edit Section → Anchor*) · space above 130px / below 0px at 1440 (mobile 88 / 0) (F1)
- [ ] **3.9.1 Text** · cols 1–6 · mobile 1–8 · Paragraph 3 (prototype: 14px, F3) → Heading 3 (one block, one line per style)
  ```text
  06
  CMS Integration & Implementation
  ```
- [ ] **3.9.2 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  The museum uses multiple content management systems to publish and maintain digital experiences. For this project, an institutional priority was to host and manage the content within Appspace, a cloud-based platform used to organize, publish, and update digital content across devices.
  ```
- [ ] **3.9.3 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  I collaborated closely with the Appspace team to ensure all final assets met the required dimensions, aspect ratios, and technical specifications. I led conversations with the Appspace partner manager, communicating the experience’s interaction points, user flow, and information architecture to guide the platform setup. Once configured, I built and managed the content channels, programmed the interactive interface, and implemented ongoing updates as the content and experience evolved. Below are the CMS channels within App Space.
  ```
- [ ] **Module · Video panel**: the video in cols 1–16, its caption and running time in cols 17–24 under a Line. Space above: 56px. Build it once, save it (heart icon), reuse it.
- [ ] **3.9.4 Video** · cols 1–16 · mobile 1–8 · upload `site/assets/video/r02-cms.mp4` · thumbnail `site/assets/img/poster-r02-cms.jpg` · controls on, autoplay off
- [ ] **3.9.5 Text** · cols 17–24 · mobile 1–8 (below the video) · bottom-aligned · **Line** block above (1px ink) · Paragraph 3 → Paragraph 3
  ```text
  Fig. 11 — CMS channels in Appspace
  Running time 0:11
  ```

### 3.10 · Chapter · Installation & Fabrication
- [ ] **Section:** Blank section · theme **White** · anchor link `ch-7` (*Edit Section → Anchor*) · space above 130px / below 0px at 1440 (mobile 88 / 0) (F1)
- [ ] Images keep her order; captions are "Fig. nn — …" in Paragraph 3 (the style uppercases them).
- [ ] **3.10.1 Text** · cols 1–6 · mobile 1–8 · Paragraph 3 (prototype: 14px, F3) → Heading 3 (one block, one line per style)
  ```text
  07
  Installation & Fabrication
  ```
- [ ] **3.10.2 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  For the final installation, we partnered with Sleet Custom Cabinets, a fabricator familiar with the museum environment who had previously built the interactive columns and enclosures within the Agriculture exhibit. Building on this existing design helped maintain consistency across the museum while providing a proven framework for the new Power & Energy columns.
  ```
- [ ] **3.10.3 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  I worked closely with the fabricator to provide precise dimensions, specifications, and printing requirements for the backlit graphics. The new columns were designed to match the dimensions and construction of the existing Agriculture columns.
  ```
- [ ] **3.10.4 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  My role during this phase was to coordinate and manage the various teams involved in fabrication and installation, ensuring that the physical build, digital components, graphics, and technical requirements came together successfully and on schedule.
  ```
- [ ] **Module · Board 1+3**: one large image (cols 1–16) as tall as the three small ones stacked in cols 17–24; on mobile stacked, large first. Space above: 56px. Build it once, save it (heart icon), reuse it.
- [ ] **3.10.5 Image** · cols 1–16 · mobile 1–8 · upload `site/assets/img/tiles/r02-shop-1--nat.jpg` · block shape **0.90:1** · **Fit**
  the tile already holds the light ground and padding, so nothing is cropped · lightbox on (opens the tile; full-size original: `site/assets/img/r02-shop-1.jpg`) · alt text: "Shop drawing, column surround: plan, section and perspective"
  caption (**Caption: below**, Paragraph 3):
  ```text
  Fig. 12 — Shop drawing, column surround: plan, section and perspective
  ```
- [ ] **3.10.6 Image** · cols 17–24 · mobile 1–8 · upload `site/assets/img/tiles/r02-shop-2--1_500.jpg` · block shape **3:2** · **Fit**
  the tile already holds the light ground and padding, so nothing is cropped · lightbox on (opens the tile; full-size original: `site/assets/img/r02-shop-2.jpg`) · alt text: "Shop drawing: elevations and sections"
  caption (**Caption: below**, Paragraph 3):
  ```text
  Fig. 13 — Shop drawing: elevations and sections
  ```
- [ ] **3.10.7 Image** · cols 17–24 · mobile 1–8 · upload `site/assets/img/tiles/r02-shop-3--1_500.jpg` · block shape **3:2** · **Fit**
  the tile already holds the light ground and padding, so nothing is cropped · lightbox on (opens the tile; full-size original: `site/assets/img/r02-shop-3.jpg`) · alt text: "Shop drawing: typical column surround and plan"
  caption (**Caption: below**, Paragraph 3):
  ```text
  Fig. 14 — Shop drawing: typical column surround and plan
  ```
- [ ] **3.10.8 Image** · cols 17–24 · mobile 1–8 · upload `site/assets/img/tiles/r02-shop-1-detail--1_500.jpg` · block shape **3:2** · **Fit**
  the tile already holds the light ground and padding, so nothing is cropped · lightbox on (opens the tile; full-size original: `site/assets/img/r02-shop-1-detail.jpg`) · alt text: "Shop drawing, detail: column plan view"
  caption (**Caption: below**, Paragraph 3):
  ```text
  Fig. 15 — Shop drawing, detail: column plan view
  ```
- [ ] **Module · Video panel**: the video in cols 1–16, its caption and running time in cols 17–24 under a Line. Space above: 56px. Build it once, save it (heart icon), reuse it.
- [ ] **3.10.9 Video** · cols 1–16 · mobile 1–8 · upload `site/assets/video/r02-fabrication.mp4` · thumbnail `site/assets/img/poster-r02-fabrication.jpg` · controls on, autoplay off
- [ ] **3.10.10 Text** · cols 17–24 · mobile 1–8 (below the video) · bottom-aligned · **Line** block above (1px ink) · Paragraph 3 → Paragraph 3
  ```text
  Fig. 16 — Column fabrication progression
  Running time 0:14
  ```

### 3.11 · Chapter · Results & Impact
- [ ] **Section:** Blank section · theme **White** · anchor link `ch-8` (*Edit Section → Anchor*) · space above 130px / below 0px at 1440 (mobile 88 / 0) (F1)
- [ ] **3.11.1 Text** · cols 1–6 · mobile 1–8 · Paragraph 3 (prototype: 14px, F3) → Heading 3 (one block, one line per style)
  ```text
  08
  Results & Impact
  ```
- [ ] **3.11.2 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  The Power & Energy interactive column transformed the exhibit entrance into a more intentional visitor touchpoint, creating a clear visual anchor while introducing new opportunities for exploration and learning.
  ```
- [ ] **3.11.3 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  The final experience supported multiple visitor needs through artifact discovery, career exploration, wayfinding, and interactive learning. It also advanced institutional technology goals by integrating the experience into the museum’s CMS ecosystem, creating a more flexible framework for managing and updating digital content.
  ```
- [ ] **3.11.4 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  For project sponsor ITC, the experience provided a meaningful way to connect the Power & Energy story to the people behind the industry by highlighting employee perspectives and diverse career pathways.
  ```
- [ ] **Module · Video panel**: the video in cols 1–16, its caption and running time in cols 17–24 under a Line. Space above: 56px. Build it once, save it (heart icon), reuse it.
- [ ] **3.11.5 Video** · cols 1–16 · mobile 1–8 · upload `site/assets/video/r02-final-setup.mp4` · thumbnail `site/assets/img/poster-r02-final-setup.jpg` · controls on, autoplay off · vertical video (F10)
- [ ] **3.11.6 Text** · cols 17–24 · mobile 1–8 (below the video) · bottom-aligned · **Line** block above (1px ink) · Paragraph 3 → Paragraph 3
  ```text
  Fig. 17 — Final setup: the installed column
  Running time 0:21
  ```

### 3.12 · Chapter · Ongoing Evaluation
- [ ] **Section:** Blank section · theme **White** · anchor link `ch-9` (*Edit Section → Anchor*) · space above 130px / below 0px at 1440 (mobile 88 / 0) (F1)
- [ ] **3.12.1 Text** · cols 1–6 · mobile 1–8 · Paragraph 3 (prototype: 14px, F3) → Heading 3 (one block, one line per style)
  ```text
  09
  Ongoing Evaluation
  ```
- [ ] **3.12.2 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  Because the experience was recently launched, long-term visitor impact has not yet been measured. The next phase of evaluation will focus on understanding how visitors engage with the column in the museum environment.
  ```
- [ ] **3.12.3 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  Planned UX research includes museum volunteer focus groups, testing with The Henry Ford Academy students, and in-gallery visitor observation. Findings will be used to evaluate discoverability, usability, engagement, and opportunities for future content and interaction improvements.
  ```

### 3.13 · Reflection
- [ ] **Section:** Blank section · theme **Stone** · anchor link `ch-10` · text centred · space above 130px / below 130px at 1440 (mobile 88 / 88) (F1)
- [ ] **3.13.1 Text** · cols 7–18 · mobile 1–8 · Paragraph 3 · centred
  ```text
  10
  ```
- [ ] **3.13.2 Text** · cols 7–18 · mobile 1–8 · Heading 4 (prototype: 14px, weight 500; nearest Paragraph 3 if 14px isn't possible, F3) · centred
  ```text
  Reflection
  ```
- [ ] **3.13.3 Text** · cols 7–18 · mobile 1–8 · Paragraph 1 italic (prototype: 28px, F6) · centred
  ```text
  This project expanded my understanding of UX design beyond traditional mobile and desktop interfaces. Designing for a physical museum environment required me to consider not only the interface itself, but also spatial interaction, accessibility, visitor behavior, and the physical context surrounding the experience.
  ```
- [ ] **3.13.4 Text** · cols 7–18 · mobile 1–8 · Paragraph 1 italic (prototype: 28px, F6) · centred
  ```text
  Working across touch displays, backlit graphics, static interpretation, and physical exhibit elements also challenged me to think about information architecture at an environmental scale—determining not only how visitors would navigate content, but where that content should live and how each touchpoint could contribute to a cohesive experience.
  ```
- [ ] **3.13.5 Text** · cols 7–18 · mobile 1–8 · Paragraph 1 italic (prototype: 28px, F6) · centred
  ```text
  Most importantly, the project reinforced that UX does not stop at the screen. Creating an effective museum experience requires balancing digital interaction with physical space, technical constraints, accessibility, storytelling, and the different ways visitors choose to engage.
  ```
- [ ] **3.13.6 Text** · cols 7–18 · mobile 1–8 · Paragraph 3 · centred
  ```text
  —
  ```

### 3.14 · Previous / all / next
- [ ] **Section:** Blank section · theme **White** · a 1px ink **Line** block across the top · 28px above, 40px below
- [ ] **Line** block · cols 1–24 · 1px ink · at the top of the section
- [ ] **3.14.1 Text** · cols 1–8 · mobile 1–8 · Paragraph 3 → Heading 4 (one block, one line per style)
  link the whole text → `/projects-private/jackson-home`
  ```text
  ← Previous project
  The Henry Ford Jackson Home Visitor Flow Simulation
  ```
- [ ] **3.14.2 Text** · cols 10–15 · mobile 1–8 · Paragraph 3
  link the whole text → `/projects`
  ```text
  All projects
  ```
- [ ] **3.14.3 Text** · cols 17–24 · mobile 1–8 · Paragraph 3 → Heading 4 (one block, one line per style)
  link the whole text → `/projects-private/rhode-island`
  ```text
  Next project →
  Rhode Island State COVID Vaccine App/401 Health App
  ```

### 3.15 · Footer
- [ ] Nothing to build: the site footer (Page 0).

<div style="page-break-after: always"></div>

## Page 4 · Room 03 · Rhode Island State COVID Vaccine App/401 Health App

- [ ] *Case studies → +* project page · title as below · URL slug `/projects-private/rhode-island` · thumbnail: not needed (the Portfolio grid is never shown).
- [ ] Start from a **duplicate** of Room 01 (*Pages → ⋯ → Duplicate*, **verify**) or from the saved sections; replace every text and image with the ones below.
- [ ] Site Styles used: Heading 2–4, Paragraph 2–3, captions, Line blocks; module images; CSS rules 3–5 (lists) and 6 (corners).

### 4.1 · Document header (title + meta table)
- [ ] **Section:** Blank section · theme **White** · no background image · space above 101px / below 0px at 1440 (mobile 56 / 0) (F1)
- [ ] **4.1.1 Text** · cols 1–13 · mobile 1–8 · Heading 2
  ```text
  Rhode Island State COVID Vaccine App/401 Health App
  ```
- [ ] **4.1.2 Text** · cols 15–17 · mobile 1–8 · Paragraph 3 → Paragraph 2 (prototype: 15px, F3) (one block, one line per style)
  **Line** block above (1px ink, same columns)
  ```text
  Role
  UX Designer| UX Researcher | UX Consultant
  ```
- [ ] **4.1.3 Text** · cols 18–21 · mobile 1–8 · Paragraph 3 → Paragraph 2 (prototype: 15px, F3) (one block, one line per style)
  **Line** block above (1px ink, same columns)
  ```text
  Methods
  Qualitative Research • Quantitative Analysis • Feedback Synthesis • Competitive/Heuristic Review • Content Strategy • Wireframing
  ```
- [ ] **4.1.4 Text** · cols 22–24 · mobile 1–8 · Paragraph 3 → Paragraph 2 (prototype: 15px, F3) (one block, one line per style)
  **Line** block above (1px ink, same columns)
  ```text
  Setting
  State of Rhode Island Department of Health
  ```

### 4.2 · Chapter index
- [ ] **Section:** Blank section · theme **White** · 1px ink Line blocks above and below the index
- [ ] **4.2.1 Text** · cols 1–24 · mobile 1–8 · Paragraph 2 (prototype: 14px, F3) · one line that wraps; **Line** blocks above and below (1px ink) · numbers in 62% ink, titles in ink
  links: "Project Overview" → `#ch-1` · "The Challenge" → `#ch-2` · "The Approach/ Discovery & Stakeholder Alignment" → `#ch-3` · "UX Design/ Feature Prioritization" → `#ch-4` · "Results & Impact" → `#ch-5` · "Ongoing Evaluation" → `#ch-6` · "Reflection" → `#ch-7`
  ```text
  01 Project Overview   02 The Challenge   03 The Approach/ Discovery & Stakeholder Alignment   04 UX Design/ Feature Prioritization   05 Results & Impact   06 Ongoing Evaluation   07 Reflection
  ```

### 4.3 · FIG. 01 · the cover image, whole
- [ ] **Section:** Same section as the chapter index (below it), or its own White section
- [ ] **Module · Full plate**: one image block across cols 1–24. Space above: 58px. Build it once, save it (heart icon), reuse it.
- [ ] **4.3.1 Image** · cols 1–24 · mobile 1–8 · upload `site/assets/img/tiles/r5-ri-five-screens--nat-p48.jpg` · block shape **2.16:1** · **Fit**
  the tile already holds the light ground and padding, so nothing is cropped · lightbox on (opens the tile; full-size original: `site/assets/img/r5-ri-five-screens.jpg`) · alt text: "401 Health app: five mobile screens"
  caption (**Caption: below**, Paragraph 3):
  ```text
  Fig. 01 — 401 Health app: five mobile screens
  ```

### 4.4 · Chapter · Project Overview
- [ ] **Section:** Blank section · theme **White** · anchor link `ch-1` (*Edit Section → Anchor*) · space above 130px / below 0px at 1440 (mobile 88 / 0) (F1)
- [ ] **4.4.1 Text** · cols 1–6 · mobile 1–8 · Paragraph 3 (prototype: 14px, F3) → Heading 3 (one block, one line per style)
  ```text
  01
  Project Overview
  ```
- [ ] **4.4.2 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  The goal of this project was to improve the State of Rhode Island’s vaccine website and health application, making it easier for residents to report vaccination information and access their vaccination records. The redesigned experience streamlined the reporting process while providing the state with reliable, timely data to support public health decision-making during the COVID-19 pandemic. It also made proof of vaccination easier for residents to access and present when entering large events and other venues requiring verification. Ultimately, the experience aimed to increase vaccination reporting completion rates by 23%, while creating a simpler, more accessible way for residents to manage and use their vaccination information.
  ```

### 4.5 · Chapter · The Challenge
- [ ] **Section:** Blank section · theme **White** · anchor link `ch-2` (*Edit Section → Anchor*) · space above 130px / below 0px at 1440 (mobile 88 / 0) (F1)
- [ ] **4.5.1 Text** · cols 1–6 · mobile 1–8 · Paragraph 3 (prototype: 14px, F3) → Heading 3 (one block, one line per style)
  ```text
  02
  The Challenge
  ```
- [ ] **4.5.2 Text** · cols 9–20 · mobile 1–8 · Heading 4
  **Line** block above (1px, 14% ink, same columns)
  ```text
  Building Trust and Increasing Adoption of Digital Vaccination Records
  ```
- [ ] **4.5.3 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  Research and stakeholder feedback revealed a key barrier to adoption: residents were hesitant to share personal health information and unsure how a digital platform would securely manage their vaccination records. At the same time, residents saw value in having convenient digital access to their vaccination information.
  ```
- [ ] **4.5.4 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  The challenge was to create a sign-up and onboarding experience that reduced friction, established trust, and clearly communicated the value of maintaining a digital vaccination record.
  ```
- [ ] **4.5.5 Text** · cols 9–20 · mobile 1–8 · Heading 4 italic
  **Line** block above (1px, 14% ink, same columns)
  ```text
  How might we...
  ```
- [ ] **4.5.6 Text** · cols 9–20 · mobile 1–8 · Bulleted list in Paragraph 2
  ```text
  Create a seamless sign-up and onboarding experience that encourages residents to complete their vaccination record?
  Build trust by clearly communicating privacy, security, and how personal information is used?
  Demonstrate the value of digital vaccination records for events, travel, and other verification needs?
  ```
- [ ] **4.5.7 Text** · cols 9–20 · mobile 1–8 · Heading 4
  **Line** block above (1px, 14% ink, same columns)
  ```text
  Reducing Friction Through Health Record Integration
  ```
- [ ] **4.5.8 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  A second challenge was eliminating the need for residents to manually re-enter vaccination information already reported to the Rhode Island Child and Adult Immunization Registry (RICAIR). Because healthcare providers and pharmacies were already submitting immunization data to RICAIR, residents expected their existing records to be available within the application.
  ```
- [ ] **4.5.9 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  The challenge was to design a secure, intuitive way for users to authorize access to their existing records while clearly communicating where their information came from and how it would be used.
  ```
- [ ] **4.5.10 Text** · cols 9–20 · mobile 1–8 · Heading 4 italic
  **Line** block above (1px, 14% ink, same columns)
  ```text
  How might we...
  ```
- [ ] **4.5.11 Text** · cols 9–20 · mobile 1–8 · Bulleted list in Paragraph 2
  ```text
  Make it simple for residents to securely authorize access to their existing vaccination records?
  Clearly communicate where vaccination data comes from and how it is being used?
  Reduce unnecessary manual entry while maintaining confidence in the accuracy and privacy of health information?
  ```

### 4.6 · Chapter · The Approach/ Discovery & Stakeholder Alignment
- [ ] **Section:** Blank section · theme **White** · anchor link `ch-3` (*Edit Section → Anchor*) · space above 130px / below 0px at 1440 (mobile 88 / 0) (F1)
- [ ] Images keep her order; captions are "Fig. nn — …" in Paragraph 3 (the style uppercases them).
- [ ] **4.6.1 Text** · cols 1–6 · mobile 1–8 · Paragraph 3 (prototype: 14px, F3) → Heading 3 (one block, one line per style)
  ```text
  03
  The Approach/ Discovery & Stakeholder Alignment
  ```
- [ ] **4.6.2 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  To better understand the existing application experience, Rhode Island state employees shared user feedback and analytics related to website and app usage with my team. I conducted stakeholder interviews with employees across different areas of the program, typically in small groups of no more than two participants to enable focused discussions and gather perspectives from different areas of the program. Through conversations with employees about the existing app and web experience, I began to identify the Rhode Island Department of Health’s broader program goals and priorities. Aligning the design direction with these strategic objectives was essential to gaining leadership support and moving the project forward. The following goals helped guide the design process (Goals 20-23). Several key themes emerged, including frustration with manually re-entering vaccination information and concerns about trusting the system with sensitive health data. I also analyzed Google Play and Apple App Store reviews to identify recurring user pain points, usability issues, and technical challenges within the existing experience. Common themes included difficulties with account setup, barriers to completing key tasks, and uncertainty around how vaccination information was managed. See below.
  ```
- [ ] **4.6.3 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  These insights helped us identify usability opportunities, prioritize design recommendations, and guide the development of a more intuitive, accessible, and trustworthy vaccination management experience.
  ```
- [ ] **Module · Full plate**: one image block across cols 1–24. Space above: 56px. Build it once, save it (heart icon), reuse it.
- [ ] **4.6.4 Image** · cols 1–24 · mobile 1–8 · upload `site/assets/img/tiles/r03-goals-full--1_600.jpg` · block shape **16:10** · **Fit**
  the tile already holds the light ground and padding, so nothing is cropped · lightbox on (opens the tile; full-size original: `site/assets/img/r03-goals-full.jpg`) · alt text: "Rhode Island Department of Health population health goals"
  caption (**Caption: below**, Paragraph 3):
  ```text
  Fig. 02 — Rhode Island Department of Health population health goals
  ```
- [ ] **Module · Video panel**: the video in cols 1–16, its caption and running time in cols 17–24 under a Line. Space above: 56px. Build it once, save it (heart icon), reuse it.
- [ ] **4.6.5 Video** · cols 1–16 · mobile 1–8 · upload `site/assets/video/r03-app-reviews.mp4` · thumbnail `site/assets/img/poster-r03-app-reviews.jpg` · controls on, autoplay off · vertical video (F10)
- [ ] **4.6.6 Text** · cols 17–24 · mobile 1–8 (below the video) · bottom-aligned · **Line** block above (1px ink) · Paragraph 3 → Paragraph 3
  ```text
  Fig. 03 — App Store and Google Play reviews
  Running time 0:23
  ```

### 4.7 · Chapter · UX Design/ Feature Prioritization
- [ ] **Section:** Blank section · theme **White** · anchor link `ch-4` (*Edit Section → Anchor*) · space above 130px / below 0px at 1440 (mobile 88 / 0) (F1)
- [ ] Images keep her order; captions are "Fig. nn — …" in Paragraph 3 (the style uppercases them).
- [ ] **4.7.1 Text** · cols 1–6 · mobile 1–8 · Paragraph 3 (prototype: 14px, F3) → Heading 3 (one block, one line per style)
  ```text
  04
  UX Design/ Feature Prioritization
  ```
- [ ] **4.7.2 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  The solution focused on reducing user effort by creating a streamlined authorization flow that automatically populated vaccination records from an existing health data source. Once authenticated, users could review their vaccination history, add missing information when needed, and manage household members within a single account. This approach reduced duplicate data entry while creating a more intuitive and efficient experience.
  ```
- [ ] **4.7.3 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  Feature prioritization centered on improving usability, accessibility, and access to essential public health services. Key features included:
  ```
- [ ] **4.7.4 Text** · cols 9–20 · mobile 1–8 · Bulleted list in Paragraph 2
  ```text
  Vaccination Status: A clear status card displaying COVID-19 vaccination history, including individual doses.
  Multilingual Support: Terms and Conditions available in multiple languages, including Portuguese, to support Rhode Island’s diverse communities.
  Appointment Scheduling: An integrated calendar that allowed users to find and schedule vaccination appointments.
  Household Management: The ability to add and manage household members and their vaccination records from a single account.
  Symptom Diary: An optional tool for anonymously reporting post-vaccination symptoms, providing the Rhode Island Department of Health with data to support public health monitoring.
  Testing Location Map: An interactive map helping users quickly locate nearby COVID-19 testing services.
  ```
- [ ] **Module · Video panel**: the video in cols 1–16, its caption and running time in cols 17–24 under a Line. Space above: 56px. Build it once, save it (heart icon), reuse it.
- [ ] **4.7.5 Video** · cols 1–16 · mobile 1–8 · upload `site/assets/video/r03-wireframes.mp4` · thumbnail `site/assets/img/poster-r03-wireframes.jpg` · controls on, autoplay off
- [ ] **4.7.6 Text** · cols 17–24 · mobile 1–8 (below the video) · bottom-aligned · **Line** block above (1px ink) · Paragraph 3 → Paragraph 3
  ```text
  Fig. 04 — Desktop wireframes
  Running time 0:23
  ```
- [ ] **Module · Plate pair**: a wide image (16 cols) beside a tall one (8 cols), tops and bottoms aligned; on mobile stacked in the order listed. Space above: 56px. Build it once, save it (heart icon), reuse it.
- [ ] **4.7.7 Image** · cols 1–16 · mobile 1–8 · upload `site/assets/img/tiles/r03-annotated--1_500.jpg` · block shape **3:2** · **Fit**
  the tile already holds the light ground and padding, so nothing is cropped · lightbox on (opens the tile; full-size original: `site/assets/img/r03-annotated.jpg`) · alt text: "Vaccine details: annotated mobile screens"
  caption (**Caption: below**, Paragraph 3):
  ```text
  Fig. 05 — Vaccine details: annotated mobile screens
  ```
- [ ] **4.7.8 Image** · cols 17–24 · mobile 1–8 · upload `site/assets/img/tiles/r4-ri-screens--0_750.jpg` · block shape **3:4** · **Fit**
  the tile already holds the light ground and padding, so nothing is cropped · lightbox on (opens the tile; full-size original: `site/assets/img/r4-ri-screens.jpg`) · alt text: "Mobile wireframes: vaccination record and dose details"
  caption (**Caption: below**, Paragraph 3):
  ```text
  Fig. 06 — Mobile wireframes: vaccination record and dose details
  ```

### 4.8 · Chapter · Results & Impact
- [ ] **Section:** Blank section · theme **White** · anchor link `ch-5` (*Edit Section → Anchor*) · space above 130px / below 0px at 1440 (mobile 88 / 0) (F1)
- [ ] **4.8.1 Text** · cols 1–6 · mobile 1–8 · Paragraph 3 (prototype: 14px, F3) → Heading 3 (one block, one line per style)
  ```text
  05
  Results & Impact
  ```
- [ ] **4.8.2 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  The redesigned experience streamlined how Rhode Island residents accessed and managed their vaccination information by providing a digital alternative to the paper vaccination cards used during the initial COVID-19 vaccine rollout. The multilingual experience also expanded accessibility, helping more residents navigate and manage their health information with confidence.
  ```

### 4.9 · Chapter · Ongoing Evaluation
- [ ] **Section:** Blank section · theme **White** · anchor link `ch-6` (*Edit Section → Anchor*) · space above 130px / below 0px at 1440 (mobile 88 / 0) (F1)
- [ ] **4.9.1 Text** · cols 1–6 · mobile 1–8 · Paragraph 3 (prototype: 14px, F3) → Heading 3 (one block, one line per style)
  ```text
  06
  Ongoing Evaluation
  ```
- [ ] **4.9.2 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  Long-term adoption and engagement metrics were outside the scope of my involvement. However, the design recommendations prioritized reducing friction, strengthening user trust, and simplifying access to critical vaccination information. The experience was also designed with flexibility in mind, allowing the platform to evolve alongside future vaccination programs and changing public health needs.
  ```

### 4.10 · Reflection
- [ ] **Section:** Blank section · theme **Stone** · anchor link `ch-7` · text centred · space above 130px / below 130px at 1440 (mobile 88 / 88) (F1)
- [ ] **4.10.1 Text** · cols 7–18 · mobile 1–8 · Paragraph 3 · centred
  ```text
  07
  ```
- [ ] **4.10.2 Text** · cols 7–18 · mobile 1–8 · Heading 4 (prototype: 14px, weight 500; nearest Paragraph 3 if 14px isn't possible, F3) · centred
  ```text
  Reflection
  ```
- [ ] **4.10.3 Text** · cols 7–18 · mobile 1–8 · Paragraph 1 italic (prototype: 28px, F6) · centred
  ```text
  This project strengthened my understanding of designing digital experiences where privacy, security, accessibility, and trust are fundamental to the user experience. Working with sensitive health information reinforced the importance of reducing unnecessary friction while clearly communicating how personal data is accessed and used—principles I continue to apply in my work today.
  ```
- [ ] **4.10.4 Text** · cols 7–18 · mobile 1–8 · Paragraph 1 italic (prototype: 28px, F6) · centred
  ```text
  The project was also particularly meaningful because of the context in which it was developed. Contributing to a digital health experience during the COVID-19 pandemic gave me a deeper appreciation for the role UX design can play in helping communities navigate essential services during periods of uncertainty.
  ```
- [ ] **4.10.5 Text** · cols 7–18 · mobile 1–8 · Paragraph 3 · centred
  ```text
  —
  ```

### 4.11 · Previous / all / next
- [ ] **Section:** Blank section · theme **White** · a 1px ink **Line** block across the top · 28px above, 40px below
- [ ] **Line** block · cols 1–24 · 1px ink · at the top of the section
- [ ] **4.11.1 Text** · cols 1–8 · mobile 1–8 · Paragraph 3 → Heading 4 (one block, one line per style)
  link the whole text → `/projects-private/power-energy`
  ```text
  ← Previous project
  Designing an Interactive Museum Experience for Power & Energy
  ```
- [ ] **4.11.2 Text** · cols 10–15 · mobile 1–8 · Paragraph 3
  link the whole text → `/projects`
  ```text
  All projects
  ```
- [ ] **4.11.3 Text** · cols 17–24 · mobile 1–8 · Paragraph 3 → Heading 4 (one block, one line per style)
  link the whole text → `/projects-private/littelfuse`
  ```text
  Next project →
  Reimagining How Engineers Discover Littelfuse Products
  ```

### 4.12 · Footer
- [ ] Nothing to build: the site footer (Page 0).

<div style="page-break-after: always"></div>

## Page 5 · Room 04 · Reimagining How Engineers Discover Littelfuse Products

- [ ] *Case studies → +* project page · title as below · URL slug `/projects-private/littelfuse` · thumbnail: not needed (the Portfolio grid is never shown).
- [ ] Start from a **duplicate** of Room 01 (*Pages → ⋯ → Duplicate*, **verify**) or from the saved sections; replace every text and image with the ones below.
- [ ] Site Styles used: Heading 2–4, Paragraph 2–3, captions, Line blocks; module images; CSS rules 3–5 (lists) and 6 (corners).

### 5.1 · Document header (title + meta table)
- [ ] **Section:** Blank section · theme **White** · no background image · space above 101px / below 0px at 1440 (mobile 56 / 0) (F1)
- [ ] **5.1.1 Text** · cols 1–13 · mobile 1–8 · Heading 2
  ```text
  Reimagining How Engineers Discover Littelfuse Products
  ```
- [ ] **5.1.2 Text** · cols 15–17 · mobile 1–8 · Paragraph 3 → Paragraph 2 (prototype: 15px, F3) (one block, one line per style)
  **Line** block above (1px ink, same columns)
  ```text
  Role
  UX Consultant | UX Designer |UX Researcher
  ```
- [ ] **5.1.3 Text** · cols 18–21 · mobile 1–8 · Paragraph 3 → Paragraph 2 (prototype: 15px, F3) (one block, one line per style)
  **Line** block above (1px ink, same columns)
  ```text
  Methods
  Stakeholder Workshop | Data Analysis | Information Architecture | Wireframing | Heuristic Evaluation | Archetypes |Competitive Analysis
  ```
- [ ] **5.1.4 Text** · cols 22–24 · mobile 1–8 · Paragraph 3 → Paragraph 2 (prototype: 15px, F3) (one block, one line per style)
  **Line** block above (1px ink, same columns)
  ```text
  Setting
  Littelfuse
  ```

### 5.2 · Chapter index
- [ ] **Section:** Blank section · theme **White** · 1px ink Line blocks above and below the index
- [ ] **5.2.1 Text** · cols 1–24 · mobile 1–8 · Paragraph 2 (prototype: 14px, F3) · one line that wraps; **Line** blocks above and below (1px ink) · numbers in 62% ink, titles in ink
  links: "Project Overview" → `#ch-1` · "The Challenge" → `#ch-2` · "The Approach" → `#ch-3` · "Results & Impact" → `#ch-4` · "Reflection" → `#ch-5`
  ```text
  01 Project Overview   02 The Challenge   03 The Approach   04 Results & Impact   05 Reflection
  ```

### 5.3 · FIG. 01 · the cover image, whole
- [ ] **Section:** Same section as the chapter index (below it), or its own White section
- [ ] **Module · Full plate**: one image block across cols 1–24. Space above: 58px. Build it once, save it (heart icon), reuse it.
- [ ] **5.3.1 Image** · cols 1–24 · mobile 1–8 · upload `site/assets/img/tiles/r04-journey-full--nat-p48.jpg` · block shape **1.89:1** · **Fit**
  the tile already holds the light ground and padding, so nothing is cropped · lightbox on (opens the tile; full-size original: `site/assets/img/r04-journey-full.jpg`) · alt text: "Product-discovery journey map: overview"
  caption (**Caption: below**, Paragraph 3):
  ```text
  Fig. 01 — Product-discovery journey map: overview
  ```

### 5.4 · Chapter · Project Overview
- [ ] **Section:** Blank section · theme **White** · anchor link `ch-1` (*Edit Section → Anchor*) · space above 130px / below 0px at 1440 (mobile 88 / 0) (F1)
- [ ] **5.4.1 Text** · cols 1–6 · mobile 1–8 · Paragraph 3 (prototype: 14px, F3) → Heading 3 (one block, one line per style)
  ```text
  01
  Project Overview
  ```
- [ ] **5.4.2 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  Littelfuse is a global technology manufacturing company that develops electronic components and solutions used across automotive, industrial, electronics, and other industries.
  ```
- [ ] **5.4.3 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  I worked with Littelfuse to improve its existing digital portal experience, with a focus on creating a more intuitive way for engineers to discover, evaluate, and access products across its extensive portfolio. The project aimed to evolve the portal from an experience largely organized around individual business units into a more customer-centered platform that could better connect users with relevant products and solutions across the broader Littelfuse ecosystem.
  ```
- [ ] **5.4.4 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  From a business perspective, the redesigned experience also created opportunities to increase visibility across product categories and support cross-selling and upselling.
  ```

### 5.5 · Chapter · The Challenge
- [ ] **Section:** Blank section · theme **White** · anchor link `ch-2` (*Edit Section → Anchor*) · space above 130px / below 0px at 1440 (mobile 88 / 0) (F1)
- [ ] **5.5.1 Text** · cols 1–6 · mobile 1–8 · Paragraph 3 (prototype: 14px, F3) → Heading 3 (one block, one line per style)
  ```text
  02
  The Challenge
  ```
- [ ] **5.5.2 Text** · cols 9–20 · mobile 1–8 · Heading 4
  **Line** block above (1px, 14% ink, same columns)
  ```text
  Simplifying Product Discovery Across a Complex Product Catalog
  ```
- [ ] **5.5.3 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  Littelfuse offers an extensive portfolio of highly technical products across a wide range of industries and applications. However, the existing experience placed a significant cognitive burden on users during product discovery. When engineers did not know the exact stock number for a product, they often had to rely on broader search terms and navigate multiple paths to find what they needed.
  ```
- [ ] **5.5.4 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  Preliminary research provided by Littelfuse showed that 73.2% of users searched using an exact stock number, while others relied on broader product categories such as heaters, panels, sensors, and switches. These broader searches often failed to surface relevant results, requiring users to refine their queries or navigate deeper into the product catalog.
  ```
- [ ] **5.5.5 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  When asked about the ease of search, 48% of survey respondents said that while finding products was generally easy, it still took too much time to reach relevant results. Another 12% reported that the search experience was difficult and that they were often unable to find relevant products.
  ```
- [ ] **5.5.6 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  These findings highlighted an opportunity to reduce users’ reliance on exact product knowledge and create a more intuitive discovery experience—one that could help engineers narrow their options, identify the right product, and complete key tasks with less effort.
  ```
- [ ] **5.5.7 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  How Might We…
  ```
- [ ] **5.5.8 Text** · cols 9–20 · mobile 1–8 · Bulleted list in Paragraph 2
  ```text
  How might we help engineers discover the right product without knowing an exact stock number?
  How might we connect engineers with relevant and complementary products across Littelfuse’s broader portfolio?
  How might we streamline key tasks—from comparing products and accessing technical documentation to ordering, requesting samples, and getting support?
  ```

### 5.6 · Chapter · The Approach
- [ ] **Section:** Blank section · theme **White** · anchor link `ch-3` (*Edit Section → Anchor*) · space above 130px / below 0px at 1440 (mobile 88 / 0) (F1)
- [ ] Images keep her order; captions are "Fig. nn — …" in Paragraph 3 (the style uppercases them).
- [ ] **5.6.1 Text** · cols 1–6 · mobile 1–8 · Paragraph 3 (prototype: 14px, F3) → Heading 3 (one block, one line per style)
  ```text
  03
  The Approach
  ```
- [ ] **5.6.2 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  I began by reviewing existing customer research, business goals, and the end-to-end product-discovery experience. I translated those inputs into primary user needs, mapped the engineer’s pre-login journey, and audited the interface against the tasks users needed to complete—searching for a component, comparing options, checking stock, downloading technical information, and requesting samples.
  ```
- [ ] **5.6.3 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  The analysis exposed gaps in navigation, terminology, content pathways, and task continuity. These findings became the foundation for a simpler information architecture and more direct product-discovery flows.
  ```
- [ ] **5.6.4 Text** · cols 9–20 · mobile 1–8 · Heading 4
  **Line** block above (1px, 14% ink, same columns)
  ```text
  Synthesized existing research and business priorities
  ```
- [ ] **5.6.5 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  In reviewing existing research I learned that the Little Fuse customers relied on the platform to complete one of these tasks: find and compare products, access technical documentation, check availability, request samples, and get support. Knowing that these were the common user flows and navigation paths I then began to understand who the primary Little Fuse Customer is.
  ```
- [ ] **5.6.6 Text** · cols 9–20 · mobile 1–8 · Heading 4
  **Line** block above (1px, 14% ink, same columns)
  ```text
  Defined the primary user: a design engineer
  ```
- [ ] **5.6.7 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  Through stakeholder interviews, existing user research, and analysis of customer roles and behaviors, we grouped Littelfuse users into three primary archetypes: Engineering & Technical, Sales, and Procurement. These archetypes reflect the different ways users influence product selection—from engineers evaluating specifications and making design recommendations, to sales partners supporting customers, and procurement professionals managing purchasing and supply. In combination with quantitative survey data with customer interviews, stakeholder research we identify recurring behaviors, pain points and decision drivers that inform the experience strategy. The survey data found that 66% of respondents identified as being in an engineering role, compared with 12% Sales and 5% Procurement.This insight helped us prioritize the experience around engineers’ core tasks—finding the right product quickly, comparing options, accessing technical documentation, and confidently making component decisions—while still supporting the needs of Sales and Procurement users. The analysis of the survey data is what guided our work in completing detailed personas rather than working of static archetypes.
  ```
- [ ] **Module · Board 2×2**: four image blocks, cols 1–12 / 13–24, all 1:1 (or a Gallery section → Grid: Simple, 2 columns, 1:1, 24px spacing); one column on mobile. Space above: 56px. Build it once, save it (heart icon), reuse it.
- [ ] **5.6.8 Image** · cols 1–12 · mobile 1–8 · upload `site/assets/img/tiles/r3-fig-decision-board--1_000.jpg` · block shape **1:1** · **Fit**
  the tile already holds the light ground and padding, so nothing is cropped · lightbox on (opens the tile; full-size original: `site/assets/img/r3-fig-decision-board.jpg`) · alt text: "Survey: who drives component decisions"
  caption (**Caption: below**, Paragraph 3):
  ```text
  Fig. 02 — Survey: who drives component decisions
  ```
- [ ] **5.6.9 Image** · cols 13–24 · mobile 1–8 · upload `site/assets/img/tiles/r04-archetype-engineering--1_000.jpg` · block shape **1:1** · **Fit**
  the tile already holds the light ground and padding, so nothing is cropped · lightbox on (opens the tile; full-size original: `site/assets/img/r04-archetype-engineering.jpg`) · alt text: "User archetype: Engineering & Technical"
  caption (**Caption: below**, Paragraph 3):
  ```text
  Fig. 03 — User archetype: Engineering & Technical
  ```
- [ ] **5.6.10 Image** · cols 1–12 · mobile 1–8 · upload `site/assets/img/tiles/r04-archetype-sales--1_000.jpg` · block shape **1:1** · **Fit**
  the tile already holds the light ground and padding, so nothing is cropped · lightbox on (opens the tile; full-size original: `site/assets/img/r04-archetype-sales.jpg`) · alt text: "User archetype: Sales"
  caption (**Caption: below**, Paragraph 3):
  ```text
  Fig. 04 — User archetype: Sales
  ```
- [ ] **5.6.11 Image** · cols 13–24 · mobile 1–8 · upload `site/assets/img/tiles/r04-archetype-procurement--1_000.jpg` · block shape **1:1** · **Fit**
  the tile already holds the light ground and padding, so nothing is cropped · lightbox on (opens the tile; full-size original: `site/assets/img/r04-archetype-procurement.jpg`) · alt text: "User archetype: Procurement"
  caption (**Caption: below**, Paragraph 3):
  ```text
  Fig. 05 — User archetype: Procurement
  ```
- [ ] **Module · Video panel**: the video in cols 1–16, its caption and running time in cols 17–24 under a Line. Space above: 56px. Build it once, save it (heart icon), reuse it.
- [ ] **5.6.12 Video** · cols 1–16 · mobile 1–8 · upload `site/assets/video/r04-personas.mp4` · thumbnail `site/assets/img/poster-r04-personas.jpg` · controls on, autoplay off
- [ ] **5.6.13 Text** · cols 17–24 · mobile 1–8 (below the video) · bottom-aligned · **Line** block above (1px ink) · Paragraph 3 → Paragraph 3
  ```text
  Fig. 06 — Engineering personas
  Running time 0:20
  ```
- [ ] **5.6.14 Text** · cols 9–20 · mobile 1–8 · Heading 4
  **Line** block above (1px, 14% ink, same columns)
  ```text
  Mapped the product-discovery journey
  ```
- [ ] **5.6.15 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  The user journey was developed during a collaborative workshop at the client’s headquarters, bringing together key stakeholders to map how engineers move from identifying a product need to researching, comparing, testing, and selecting a solution. By documenting both the high-level journey and detailed decision points, we identified key behaviors, information needs, and opportunities to streamline the digital product experience.
  ```
- [ ] **Module · Full plate**: one image block across cols 1–24. Space above: 56px. Build it once, save it (heart icon), reuse it.
- [ ] **5.6.16 Image** · cols 1–24 · mobile 1–8 · upload `site/assets/img/tiles/r04-journey-full--1_929.jpg` · block shape **1.93:1** · **Fit**
  the tile already holds the light ground and padding, so nothing is cropped · lightbox on (opens the tile; full-size original: `site/assets/img/r04-journey-full.jpg`) · alt text: "Product-discovery journey map"
  caption (**Caption: below**, Paragraph 3):
  ```text
  Fig. 07 — Product-discovery journey map
  ```
- [ ] **5.6.17 Text** · cols 1–10 · mobile 1–8 · Heading 4 italic
  **Line** block above (1px, 14% ink, same columns)
  ```text
  Audited critical tasks and interface pathways
  ```
- [ ] **5.6.18 Text** · cols 1–10 · mobile 1–8 · Paragraph 2
  ```text
  Following the journey-mapping workshop, I evaluated the existing Littelfuse website against the needs and behaviors identified in the user journey. The review focused on key paths engineers rely on to discover and evaluate products, revealing gaps in navigation, task flows, content structure, and interaction design.
  ```
- [ ] **5.6.19 Text** · cols 13–24 · mobile 1–8 · Numbered list in Paragraph 2
  **Line** block above (1px ink, same columns)
  ```text
  01 — Navigation & FindabilityCritical product actions—including Cross Reference, Check Stock, Where to Buy, and Request Samples—were inconsistently represented across the experience. We also identified unclear labeling and opportunities to make global search and language selection more intuitive.
  02 — Incomplete Task FlowsMapping core tasks exposed several points where the existing experience did not fully support the user's journey. The Check Stock flow, for example, contained missing screens and unclear paths for users who didn't already know a product or part number.
  03 — Interaction & Content GapsThe audit uncovered smaller usability issues that compounded friction, including inconsistent labels, unclear interface states, missing landing-page templates, misaligned interface elements, and controls without clearly defined behaviors.
  ```
- [ ] **5.6.20 Text** · cols 9–20 · mobile 1–8 · Heading 4
  **Line** block above (1px, 14% ink, same columns)
  ```text
  Translated findings into design principles
  ```
- [ ] **5.6.21 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  Insights from the audit were translated into design principles focused on clarity, consistency, accessibility, and task completion. Existing wireframes were refined to create a more cohesive experience across desktop and mobile, including clearer navigation and labeling, improved menu hierarchy, accessible interaction states, standardized components, and more intuitive search and filtering patterns. These principles were applied consistently across the global header, mega menu, homepage, product pages, and supporting content modules.
  ```
- [ ] **5.6.22 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  The work also addressed gaps where the existing wireframes did not fully support critical user tasks. New and expanded flows were designed for global search, product discovery, Check Stock, Where to Buy, and privacy/GDPR interactions, while missing states, error handling, filters, links, and responsive behaviors were defined to make the experience development-ready. Below are the completed wire frames.
  ```
- [ ] **Module · Full plate**: one image block across cols 1–24. Space above: 56px. Build it once, save it (heart icon), reuse it.
- [ ] **5.6.23 Placeholder: leave out** · cols 1–24 · mobile 1–8 · F11 · F12. The prototype's grey box reads "Littelfuse wireframes — pending export from Adobe XD". Its caption, for when the export arrives:
  ```text
  Fig. 08 — Littelfuse wireframes (placeholder)
  ```

### 5.7 · Chapter · Results & Impact
- [ ] **Section:** Blank section · theme **White** · anchor link `ch-4` (*Edit Section → Anchor*) · space above 130px / below 0px at 1440 (mobile 88 / 0) (F1)
- [ ] **5.7.1 Text** · cols 1–6 · mobile 1–8 · Paragraph 3 (prototype: 14px, F3) → Heading 3 (one block, one line per style)
  ```text
  04
  Results & Impact
  ```
- [ ] **5.7.2 Text** · cols 9–20 · mobile 1–8 · Paragraph 2
  ```text
  The redesigned experience streamlined product discovery and evaluation across desktop and mobile, creating clearer pathways through search, navigation, and key purchasing tasks. Following launch, mobile logins increased by 6%, indicating stronger engagement with the improved mobile experience.
  ```

### 5.8 · Reflection
- [ ] **Section:** Blank section · theme **Stone** · anchor link `ch-5` · text centred · space above 130px / below 130px at 1440 (mobile 88 / 88) (F1)
- [ ] **5.8.1 Text** · cols 7–18 · mobile 1–8 · Paragraph 3 · centred
  ```text
  05
  ```
- [ ] **5.8.2 Text** · cols 7–18 · mobile 1–8 · Heading 4 (prototype: 14px, weight 500; nearest Paragraph 3 if 14px isn't possible, F3) · centred
  ```text
  Reflection
  ```
- [ ] **5.8.3 Text** · cols 7–18 · mobile 1–8 · Paragraph 1 italic (prototype: 28px, F6) · centred
  ```text
  This project introduced me to a highly specialized industry with a unique set of users and technical workflows. To design effectively, I invested additional time in secondary research—studying the competitive landscape, learning industry fundamentals, and understanding how products move from the warehouse into an online product database. That deeper investigation surfaced questions we hadn’t initially considered and ultimately led to additional discovery sessions with stakeholders. In hindsight, that extra effort became a strength of the project: stakeholders appreciated the attention to detail, and it reinforced for me that good UX sometimes means slowing down to fully understand a complex ecosystem before designing for it.
  ```
- [ ] **5.8.4 Text** · cols 7–18 · mobile 1–8 · Paragraph 3 · centred
  ```text
  —
  ```

### 5.9 · Previous / all / next
- [ ] **Section:** Blank section · theme **White** · a 1px ink **Line** block across the top · 28px above, 40px below
- [ ] **Line** block · cols 1–24 · 1px ink · at the top of the section
- [ ] **5.9.1 Text** · cols 1–8 · mobile 1–8 · Paragraph 3 → Heading 4 (one block, one line per style)
  link the whole text → `/projects-private/rhode-island`
  ```text
  ← Previous project
  Rhode Island State COVID Vaccine App/401 Health App
  ```
- [ ] **5.9.2 Text** · cols 10–15 · mobile 1–8 · Paragraph 3
  link the whole text → `/projects`
  ```text
  All projects
  ```
- [ ] **5.9.3 Text** · cols 17–24 · mobile 1–8 · Paragraph 3 → Heading 4 (one block, one line per style)
  link the whole text → `/projects-private/jackson-home`
  ```text
  Next project →
  The Henry Ford Jackson Home Visitor Flow Simulation
  ```

### 5.10 · Footer
- [ ] Nothing to build: the site footer (Page 0).

<div style="page-break-after: always"></div>

## Page 6 · Lock Screen

The lock screen is a settings panel, not a Fluid Engine page: no columns. *Case studies → Page settings → Password*, then *Lock Screen → Customize* (or *Design → Lock Screen*, **verify** which her account has).

- [ ] **Password** on the *Case studies* Portfolio (*Page settings → General → Password*). One password protects all four projects; Squarespace can't give each project its own.
- [ ] Layout **centred**; lock icon **off**; background image **none** (nothing from the case studies may show before the password).
- [ ] Colours: background `#FFFFFF`, text `#111111`. Field rule, button fill and error style come from CSS rules 7–14 (F13).
- [ ] Site title / branding at the top (Inter Tight 15px), 24px from the top edge:
  ```text
  Yasmin Bajwa
  ```
- [ ] Headline (Heading 2 at 56px if the lock screen allows a size, else Heading 2; Instrument Serif 400; italic: "by invitation."):
  ```text
  Projects are shared by invitation.
  ```
- [ ] Description (Paragraph 2, 15px):
  ```text
  Enter the password to continue.
  ```
- [ ] Password field label (Paragraph 3) and the button text:
  ```text
  Password
  Enter
  ```
- [ ] Below the form, a link line (14px) (F14): link "Email Yasmin →" → `mailto:` her address with subject "Portfolio access":
  ```text
  No password? Email Yasmin →
  ```
- [ ] Wrong password: Squarespace's own message (F15). The prototype's text, for reference only:
  ```text
  Incorrect password.
  ```
- [ ] Footer line at the bottom (13px, 62% ink), 24px from the bottom edge:
  ```text
  © Yasmin Bajwa
  ```
- [ ] **Test** in a private window: a project URL shows this screen; the wrong password shows the message without a shake; the right one opens all four projects.

<div style="page-break-after: always"></div>

## Page 7 · Projects

A **regular page** (not the Portfolio grid: that locks with the password). One Blank section, theme **White**.
- [ ] Site Styles used: Heading 2, Heading 4 (26px titles), Paragraph 2–3; logo plates (CSS rules 18–19); one section ID for rule 18 (Page 9).
- [ ] **Section:** Blank · theme White · space above the title 86px (mobile 48), 40px between title and grid, **144px** below the grid at 1600 (F1)
- [ ] **7.1.1 Text** · cols 1–24 · mobile 1–8 · Heading 2
  ```text
  Projects
  ```
- [ ] Then four cards in a 2 × 2 grid (cols 1–12 / 13–24; mobile one column), **56px** between the rows of cards. Each card: the logo plate, then one text block. Link the image and the title to the project page (F16).
- [ ] **7.2.2 Image** · cols 1–12 · mobile 1–8 · upload `site/assets/img/logos/plate-the-henry-ford.png` · block shape **3:2** · **Fit**
  transparent 1200×800 plate, logo already sized inside it; ground and hover come from CSS rules 18–19 · clickthrough link → `/projects-private/jackson-home` (instead of the lightbox) · alt text: "The Henry Ford logo"
- [ ] **7.2.3 Text** · cols 1–12 · mobile 1–8 · Paragraph 3 → Heading 4 (prototype: 26px, F3) → Paragraph 2 (prototype: 15px, F3) (one block, one line per style)
  link the title → `/projects-private/jackson-home`
  ```text
  01 · Password protected
  The Henry Ford Jackson Home Visitor Flow Simulation
  UX Researcher | Experience Design
  ```
- [ ] **7.2.4 Image** · cols 13–24 · mobile 1–8 · upload `site/assets/img/logos/plate-itc.png` · block shape **3:2** · **Fit**
  transparent 1200×800 plate, logo already sized inside it; ground and hover come from CSS rules 18–19 · clickthrough link → `/projects-private/power-energy` (instead of the lightbox) · alt text: "ITC logo"
- [ ] **7.2.5 Text** · cols 13–24 · mobile 1–8 · Paragraph 3 → Heading 4 (prototype: 26px, F3) → Paragraph 2 (prototype: 15px, F3) (one block, one line per style)
  link the title → `/projects-private/power-energy`
  ```text
  02 · Password protected
  Designing an Interactive Museum Experience for Power & Energy
  UX Designer| Experience Design | Project Management
  ```
- [ ] **7.2.6 Image** · cols 1–12 · mobile 1–8 · upload `site/assets/img/logos/plate-rhode-island-doh.png` · block shape **3:2** · **Fit**
  transparent 1200×800 plate, logo already sized inside it; ground and hover come from CSS rules 18–19 · clickthrough link → `/projects-private/rhode-island` (instead of the lightbox) · alt text: "Rhode Island Department of Health logo"
- [ ] **7.2.7 Text** · cols 1–12 · mobile 1–8 · Paragraph 3 → Heading 4 (prototype: 26px, F3) → Paragraph 2 (prototype: 15px, F3) (one block, one line per style)
  link the title → `/projects-private/rhode-island`
  ```text
  03 · Password protected
  Rhode Island State COVID Vaccine App/401 Health App
  UX Designer| UX Researcher | UX Consultant
  ```
- [ ] **7.2.8 Image** · cols 13–24 · mobile 1–8 · upload `site/assets/img/logos/plate-littelfuse.png` · block shape **3:2** · **Fit**
  transparent 1200×800 plate, logo already sized inside it; ground and hover come from CSS rules 18–19 · clickthrough link → `/projects-private/littelfuse` (instead of the lightbox) · alt text: "Littelfuse logo"
- [ ] **7.2.9 Text** · cols 13–24 · mobile 1–8 · Paragraph 3 → Heading 4 (prototype: 26px, F3) → Paragraph 2 (prototype: 15px, F3) (one block, one line per style)
  link the title → `/projects-private/littelfuse`
  ```text
  04 · Password protected
  Reimagining How Engineers Discover Littelfuse Products
  UX Consultant | UX Designer |UX Researcher
  ```

<div style="page-break-after: always"></div>

## Page 8 · Homepage

- [ ] Site Styles used: Heading 1–3, Paragraph 1–3, Primary button, themes White / Stone / Ink; CSS rules 15–16 (panels) and 18–19 (logo tiles). Collect two IDs for Page 9: the four panel image blocks and this page's Projects section.

### 8.1 · Hero
- [ ] **Section:** Blank section · theme **White** · space above 86px / below 86px at 1440 (mobile 48 / 56) (F1)
- [ ] **8.1.1 Text** · cols 1–14 · mobile 1–8 · Heading 1
  italic: "Yasmin."
  ```text
  Hi, I’m Yasmin.
  ```
- [ ] **8.1.2 Text** · cols 1–12 · mobile 1–8 · Paragraph 2 bold (prototype: 19px, F3)
  ```text
  About Me
  ```
- [ ] **8.1.3 Text** · cols 1–12 · mobile 1–8 · Paragraph 2 (prototype: 19px, F3)
  ```text
  Hi! I’m Yasmin, a Digital Exhibit Designer at The Henry Ford Museum with a multidisciplinary background in UX design, user research, and digital marketing. I’m passionate about bringing stories to life through digital experiences—and deeply inspired by history, fashion, and art.
  ```
- [ ] **8.1.4 Button** · cols 1–3 · mobile 1–3 · Primary (outline) · links to `/projects`
  ```text
  View Projects →
  ```
- [ ] **8.1.5 Image** · cols 15–19 · mobile 1–8 · upload `site/assets/img/portrait-4x5.jpg` · block shape **4:5** · **Fill**
  alt text: "Yasmin Bajwa"
  caption (**Caption: below**, Paragraph 3):
  ```text
  Digital Exhibit Designer — The Henry Ford
  ```
- [ ] **8.1.6 Text** · cols 21–24 · mobile 1–8 · Paragraph 3 → Paragraph 2 (prototype: 15px, F3) (one block, one line per style)
  **Line** block below (1px, 14% ink, same columns) · **Line** block above (1px ink, same columns)
  ```text
  Role
  Digital Exhibit Designer, The Henry Ford Museum
  ```
- [ ] **8.1.7 Text** · cols 21–24 · mobile 1–8 · Paragraph 3 → Paragraph 2 (prototype: 15px, F3) (one block, one line per style)
  **Line** block below (1px, 14% ink, same columns)
  ```text
  Based in
  United States
  ```
- [ ] **8.1.8 Text** · cols 21–24 · mobile 1–8 · Paragraph 3 → Paragraph 2 (prototype: 15px, F3) (one block, one line per style)
  **Line** block below (1px, 14% ink, same columns)
  ```text
  Focus
  Interactive Exhibit Design · UX Design · UX Research · Digital Marketing
  ```
- [ ] **8.1.9 Text** · cols 21–24 · mobile 1–8 · Paragraph 3 → Paragraph 2 (prototype: 15px, F3) (one block, one line per style)
  **Line** block below (1px, 14% ink, same columns)
  ```text
  Currently
  Bringing stories to life through digital experiences
  ```
- [ ] **Mobile order** (drag blocks in the mobile view): 8.1.5, 8.1.1, 8.1.2, 8.1.3, 8.1.4, 8.1.6, 8.1.7, 8.1.8, 8.1.9

### 8.2 · Rule under the hero
- [ ] **Line** block · cols 1–24, section content width Full (edge to edge) · 1px, 14% ink · at the top of the next section (or a section divider, if her template has one).

### 8.3 · Snippets About My Life
- [ ] **Section:** Blank section · theme **Stone** · anchor link `snippets` · space above 130px / below 130px at 1440 (mobile 88 / 88) (F1)
- [ ] **8.3.1 Text** · cols 1–10 · mobile 1–8 · Heading 3
  ```text
  Snippets About My Life
  ```
- [ ] **8.3.2 Text** · cols 1–10 · mobile 1–8 · Paragraph 1
  ```text
  By blending design, research, and exhibit development, I bring a fresh, curious perspective to every team. To me, every project is an opportunity to experiment, innovate, and create something people will remember.
  ```
- [ ] **8.3.3 Text** · cols 1–10 · mobile 1–8 · Paragraph 3 (prototype: 12px, tracking 0.24em, F3)
  **Line** block above (1px ink, same columns)
  ```text
  History · Fashion · Art
  ```
- [ ] **8.3.4 Gallery block → Slideshow** · cols 13–24 · mobile 1–8 · aspect ratio **4:5** · autoplay **on, 5 s** · arrows on · dots on if offered · captions off · lightbox off (F17)
  Upload in this order (21 photos; the five landscape ones are already letterboxed to 4:5 so they show whole):
  - [ ] 01 `site/assets/img/snippets/snippet-20.jpg` · alt "The Power & Energy column being installed"
  - [ ] 02 `site/assets/img/snippets/snippet-06.jpg` · alt "Street mural: a portrait with a lightbulb hat"
  - [ ] 03 `site/assets/img/snippets/snippet-09.jpg` · alt "A pastry case of custard tarts"
  - [ ] 04 `site/assets/img/snippets/snippet-11.jpg` · alt "A hat exhibit"
  - [ ] 05 `site/assets/img/snippets/snippet-01.jpg` · alt "Violins of Hope exhibit"
  - [ ] 06 `site/assets/img/snippets/snippet-19.jpg` · alt "Anatomical fashion pieces on mannequins"
  - [ ] 07 `site/assets/img/snippets/snippet-10.jpg` · alt "Yasmin looking at a framed painting"
  - [ ] 08 `site/assets/img/snippets/snippet-13.jpg` · alt "A robotic head sculpture"
  - [ ] 09 `site/assets/img/snippets/snippet-12.jpg` · alt "A blazer hanging outside a vintage shop"
  - [ ] 10 `site/assets/img/snippets/snippet-07.jpg` · alt "An ornate painted ceiling"
  - [ ] 11 `site/assets/img/snippets/snippet-03.jpg` · alt "A gallery mid-install under a skylight"
  - [ ] 12 `site/assets/img/snippets/snippet-14.jpg` · alt "Orangutans playing chess, a diorama"
  - [ ] 13 `site/assets/img/snippets/snippet-05.jpg` · alt "Painting supplies, a painted pumpkin and a charcuterie board"
  - [ ] 14 `site/assets/img/snippets/snippet-15.jpg` · alt "Marble figures installation with digital counters"
  - [ ] 15 `site/assets/img/snippets/snippet-02.jpg` · alt "A gallery mid-install"
  - [ ] 16 `site/assets/img/snippets/snippet-16.jpg` · alt "A carved standing figure"
  - [ ] 17 `site/assets/img/snippets/snippet-08.jpg` · alt "A crown and sceptre on red"
  - [ ] 18 `site/assets/img/snippets/snippet-17.jpg` · alt "Bookshop shelves"
  - [ ] 19 `site/assets/img/snippets/snippet-04.jpg` · alt "An exhibit gallery with panels and cases"
  - [ ] 20 `site/assets/img/snippets/snippet-18.jpg` · alt "Measuring tape against a gallery wall"
  - [ ] 21 `site/assets/img/snippets/snippet-21.jpg` · alt "A The Henry Ford cap on a notebook with a handwritten note" · **publish only once the client confirms it** (F12)
- [ ] **Mobile order** (drag blocks in the mobile view): 8.3.4, 8.3.1, 8.3.2, 8.3.3

### 8.4 · Four disciplines
- [ ] **Section:** Blank section · content width **Full** · theme **Ink** · no space above or below · panels about 60% of the screen tall (540px at 1440; 42% on phones, 2 × 2) (F18)
- [ ] Each panel: an **Image** block filling the panel (Fill), then two **Text** blocks layered on top of it (*Bring forward*): the number in the panel's top rows, the name in its bottom rows. A 1px, 14% white rule between panels (Shape block outline, or none if the gaps show). Mobile: 2 × 2, panels 1–2 in the first row, 3–4 in the second.
- [ ] **8.4.1 Image** · cols 1–6 · mobile 1–4 · upload `site/assets/img/snippets/snippet-15.jpg` · block shape **2:3** · **Fill**
  alt text: "Marble figures installation with digital counters"
- [ ] **8.4.2 Text** · cols 1–6 · mobile 1–4 · Paragraph 3 (prototype: 13px, F3)
  ```text
  01
  ```
- [ ] **8.4.3 Text** · cols 1–6 · mobile 1–4 · Heading 3 (prototype: 34px, F3)
  ```text
  Interactive Exhibit Design
  ```
- [ ] **8.4.4 Image** · cols 7–12 · mobile 5–8 · upload `site/assets/img/snippets/snippet-13.jpg` · block shape **2:3** · **Fill**
  alt text: "Robotic head sculpture in a gallery"
- [ ] **8.4.5 Text** · cols 7–12 · mobile 5–8 · Paragraph 3 (prototype: 13px, F3)
  ```text
  02
  ```
- [ ] **8.4.6 Text** · cols 7–12 · mobile 5–8 · Heading 3 (prototype: 34px, F3)
  ```text
  UX ( User Experience) Design
  ```
- [ ] **8.4.7 Image** · cols 13–18 · mobile 1–4 · upload `site/assets/img/snippets/snippet-18.jpg` · block shape **2:3** · **Fill**
  alt text: "Measuring tape against a gallery wall"
- [ ] **8.4.8 Text** · cols 13–18 · mobile 1–4 · Paragraph 3 (prototype: 13px, F3)
  ```text
  03
  ```
- [ ] **8.4.9 Text** · cols 13–18 · mobile 1–4 · Heading 3 (prototype: 34px, F3)
  ```text
  UX Research
  ```
- [ ] **8.4.10 Image** · cols 19–24 · mobile 5–8 · upload `site/assets/img/snippets/snippet-06.jpg` · block shape **2:3** · **Fill**
  alt text: "Street mural: portrait with a lightbulb hat"
- [ ] **8.4.11 Text** · cols 19–24 · mobile 5–8 · Paragraph 3 (prototype: 13px, F3)
  ```text
  04
  ```
- [ ] **8.4.12 Text** · cols 19–24 · mobile 5–8 · Heading 3 (prototype: 34px, F3)
  ```text
  Digital Marketing
  ```

### 8.5 · Projects
- [ ] **Section:** Blank section · theme **White** · anchor link `projects` · space above 130px / below 130px at 1440 (mobile 88 / 88) (F1)
- [ ] **8.5.1 Text** · cols 1–5 · mobile 1–3 · Heading 2
  ```text
  Projects
  ```
- [ ] **8.5.2 Text** · cols 21–24 · mobile 5–8 · Paragraph 2
  link "All projects →" → `/projects`
  ```text
  All projects →
  ```
- [ ] **Line** block · cols 1–24 · 1px ink · above the first row. Then four rows, each followed by a 1px, 14% ink Line block across cols 1–24; 22px above and below each row's content. Link each title and logo to its project page (F16; F19).
- [ ] **8.5.3 Text** · cols 1–10 · mobile 1–8 · Paragraph 3 → Heading 3 (prototype: 32px, F3) (one block, one line per style)
  link the title → `/projects-private/jackson-home`
  ```text
  01
  The Henry Ford Jackson Home Visitor Flow Simulation
  ```
- [ ] **8.5.4 Text** · cols 12–17 · mobile 1–8 · Paragraph 2 (prototype: 15px, F3) → Paragraph 3 (one block, one line per style)
  ```text
  UX Researcher | Experience Design
  Password protected
  ```
- [ ] **8.5.5 Image** · cols 19–24 · mobile 1–8 · upload `site/assets/img/logos/plate-the-henry-ford.png` · block shape **3:2** · **Fit**
  transparent 1200×800 plate, logo already sized inside it; ground and hover come from CSS rules 18–19 · clickthrough link → `/projects-private/jackson-home` (instead of the lightbox) · alt text: "The Henry Ford logo"
- [ ] **Mobile order** (drag blocks in the mobile view): 8.5.5, 8.5.3, 8.5.4
- [ ] **Line** block · cols 1–24 · 1px, 14% ink
- [ ] **8.5.6 Text** · cols 1–10 · mobile 1–8 · Paragraph 3 → Heading 3 (prototype: 32px, F3) (one block, one line per style)
  link the title → `/projects-private/power-energy`
  ```text
  02
  Designing an Interactive Museum Experience for Power & Energy
  ```
- [ ] **8.5.7 Text** · cols 12–17 · mobile 1–8 · Paragraph 2 (prototype: 15px, F3) → Paragraph 3 (one block, one line per style)
  ```text
  UX Designer| Experience Design | Project Management
  Password protected
  ```
- [ ] **8.5.8 Image** · cols 19–24 · mobile 1–8 · upload `site/assets/img/logos/plate-itc.png` · block shape **3:2** · **Fit**
  transparent 1200×800 plate, logo already sized inside it; ground and hover come from CSS rules 18–19 · clickthrough link → `/projects-private/power-energy` (instead of the lightbox) · alt text: "ITC logo"
- [ ] **Mobile order** (drag blocks in the mobile view): 8.5.8, 8.5.6, 8.5.7
- [ ] **Line** block · cols 1–24 · 1px, 14% ink
- [ ] **8.5.9 Text** · cols 1–10 · mobile 1–8 · Paragraph 3 → Heading 3 (prototype: 32px, F3) (one block, one line per style)
  link the title → `/projects-private/rhode-island`
  ```text
  03
  Rhode Island State COVID Vaccine App/401 Health App
  ```
- [ ] **8.5.10 Text** · cols 12–17 · mobile 1–8 · Paragraph 2 (prototype: 15px, F3) → Paragraph 3 (one block, one line per style)
  ```text
  UX Designer| UX Researcher | UX Consultant
  Password protected
  ```
- [ ] **8.5.11 Image** · cols 19–24 · mobile 1–8 · upload `site/assets/img/logos/plate-rhode-island-doh.png` · block shape **3:2** · **Fit**
  transparent 1200×800 plate, logo already sized inside it; ground and hover come from CSS rules 18–19 · clickthrough link → `/projects-private/rhode-island` (instead of the lightbox) · alt text: "Rhode Island Department of Health logo"
- [ ] **Mobile order** (drag blocks in the mobile view): 8.5.11, 8.5.9, 8.5.10
- [ ] **Line** block · cols 1–24 · 1px, 14% ink
- [ ] **8.5.12 Text** · cols 1–10 · mobile 1–8 · Paragraph 3 → Heading 3 (prototype: 32px, F3) (one block, one line per style)
  link the title → `/projects-private/littelfuse`
  ```text
  04
  Reimagining How Engineers Discover Littelfuse Products
  ```
- [ ] **8.5.13 Text** · cols 12–17 · mobile 1–8 · Paragraph 2 (prototype: 15px, F3) → Paragraph 3 (one block, one line per style)
  ```text
  UX Consultant | UX Designer |UX Researcher
  Password protected
  ```
- [ ] **8.5.14 Image** · cols 19–24 · mobile 1–8 · upload `site/assets/img/logos/plate-littelfuse.png` · block shape **3:2** · **Fit**
  transparent 1200×800 plate, logo already sized inside it; ground and hover come from CSS rules 18–19 · clickthrough link → `/projects-private/littelfuse` (instead of the lightbox) · alt text: "Littelfuse logo"
- [ ] **Mobile order** (drag blocks in the mobile view): 8.5.14, 8.5.12, 8.5.13
- [ ] **Line** block · cols 1–24 · 1px, 14% ink

### 8.6 · Contact
- [ ] **Section:** Blank section · theme **Stone** · anchor link `contact` · space above 130px / below 130px at 1440 (mobile 88 / 88) (F1)
- [ ] **8.6.1 Text** · cols 1–24 · mobile 1–8 · Paragraph 3
  ```text
  Contact
  ```
- [ ] **8.6.2 Text** · cols 1–11 · mobile 1–8 · Heading 2
  ```text
  Let’s create something people will remember.
  ```
- [ ] **8.6.3 Text** · cols 1–10 · mobile 1–8 · Paragraph 3 → Paragraph 2 (one block, one line per style)
  **Line** block below (1px, 14% ink, same columns) · **Line** block above (1px ink, same columns) · link "yasminbajwa248@gmail.com" → mailto:yasminbajwa248@gmail.com
  ```text
  Email
  yasminbajwa248@gmail.com
  ```
- [ ] **8.6.4 Text** · cols 1–10 · mobile 1–8 · Paragraph 3 → Paragraph 2 (one block, one line per style)
  **Line** block below (1px, 14% ink, same columns) · link "(313) 979-2205" → tel:+13139792205
  ```text
  Phone
  (313) 979-2205
  ```
- [ ] **8.6.5 Text** · cols 1–10 · mobile 1–8 · Paragraph 3 → Paragraph 2 (one block, one line per style)
  **Line** block below (1px, 14% ink, same columns) · link "[URL — pending client]" → her LinkedIn profile URL (**pending**: the client hasn't supplied it, F12); until then paste the placeholder and leave it unlinked
  ```text
  LinkedIn
  [URL — pending client]
  ```

### 8.7 · Footer
- [ ] Nothing to build: the site footer (Page 0).

<div style="page-break-after: always"></div>

## Page 9 · Custom CSS (*Website → Pages → Custom code → Custom CSS*)

**19 lines**, one rule per line, each with its comment (budget 30). The rules are the build notes' twenty, renumbered one per line (the notes counted the caption rule as two). Paste it after Home and Projects exist, then replace the placeholders:
- [ ] `.I1`–`.I4`: right-click each **discipline photo** on Home → *Inspect* → copy the wrapper's `fe-block-…` class (rules 15–16).
- [ ] `.T1`–`.T4`, `.N1`–`.N4`: the same for each panel's **name** and **number** text blocks (rule 17).
- [ ] `.L`: the **Projects section on Home** and the **section on the Projects page**: `section[data-section-id="…"]`, both, comma-separated (rules 18–19).
- [ ] Lock-screen rules 7–14: check each class in the inspector on her site (F13).
- [ ] Other palettes: only the hex values change (the build notes list them per palette); cream adds one line, venues three to seven.

```css
.header{border-bottom:1px solid rgba(17,17,17,.14)} /*  1  1px rule under the header, if the template has no header-border setting */
.image-caption,.image-caption p{font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:rgba(17,17,17,.62)} /*  2  image captions in the Paragraph 3 look (11px caps, 62% ink); text blocks already get it from Site Styles */
.sqs-html-content li::marker{color:rgba(17,17,17,.62)} /*  3  her bullet and number markers in 62% ink */
.sqs-html-content ol{padding-left:0;list-style-position:inside;border-top:1px solid #111} /*  4  numbered lists (Findings, Impact, the Littelfuse audit): 1px ink rule above the list */
.sqs-html-content ol>li{padding:14px 0;border-bottom:1px solid rgba(17,17,17,.14)} /*  5  …and a hairline under each item, 14px above and below it */
.sqs-block-button-element,.fluid-image-container,.video-player,.sqs-video-wrapper{border-radius:0!important} /*  6  square corners on buttons, images and videos, whatever the template's default */
.sqs-slide-container input[type="password"]{border:0!important;border-bottom:1px solid #111!important;border-radius:0!important;background:transparent!important;letter-spacing:.12em} /*  7  lock screen: the password field is a single 1px ink line, no box */
.sqs-slide-container input[type="password"]:focus{border-bottom-width:2px!important;box-shadow:none!important} /*  8  lock screen: the line thickens to 2px while typing */
.sqs-slide-container button,.sqs-slide-container input[type="submit"]{border-radius:0!important;background:#111!important;color:#fff!important;border:1px solid #111!important} /*  9  lock screen: the Enter button solid ink, square */
.sqs-slide-container .error,.sqs-slide-container .form-error{color:rgba(17,17,17,.62)!important;font-size:14px!important;animation:none!important} /* 10  lock screen: the wrong-password message as quiet 14px text, no shake */
.sqs-slide-container .sqs-slide-layer-content{max-width:560px;margin:0 auto} /* 11  lock screen: the form column 560px wide, centred */
.sqs-slide-container h1,.sqs-slide-container h2{font-weight:400!important;letter-spacing:-.01em} /* 12  lock screen: the headline in regular weight with the headings' −0.01em tracking (Instrument Serif has no bold) */
.sqs-slide-container a{text-decoration:underline;text-underline-offset:.22em} /* 13  lock screen: links underlined, like the rest of the site */
.sqs-slide-container .sqs-slide-layer{background:#fff} /* 14  lock screen: white ground (no image behind it) */
.I1 img,.I2 img,.I3 img,.I4 img{filter:brightness(.55);transition:filter .3s ease} /* 15  discipline panels: each photo always under a 45% black layer (replace .I1–.I4 with the four image blocks' fe-block classes) */
.I1:hover img,.I2:hover img,.I3:hover img,.I4:hover img{filter:brightness(.7)} /* 16  discipline panels: hover lightens the layer to 30% (300ms) */
.T1,.T2,.T3,.T4,.N1,.N2,.N3,.N4{pointer-events:none} /* 17  discipline panels: the name and number text blocks let the pointer through to the photo (replace with their fe-block classes) */
.L .fluid-image-container{background:#F4F3F0;transition:background-color .3s} /* 18  logo tiles: the light ground behind each transparent plate (replace .L with the Home Projects section and the Projects page section: section[data-section-id="…"], comma-separated) */
.L .fluid-image-container:hover{background:#ECEAE5} /* 19  logo tiles: a shade darker on hover */
```

<div style="page-break-after: always"></div>

## Page 10 · What Squarespace can't reproduce exactly

Each flag is cited next to the blocks it affects. **Nearest native setting** in bold.

- [ ] **F1 · Exact section spacing in px.** Fluid Engine sections have no px padding field: the space above and below comes from the section's **height** setting (Small / Medium / Large / Custom) and the empty grid rows above the first block. **Nearest native:** start at the height named on the section, then add or remove empty rows in the editor until the gap matches the px given (check in Preview at 1440 and on a phone). *Affects: Site Styles, Room 01, Room 02, Room 03, Room 04, Projects, Homepage (40 places).*
- [ ] **F2 · The prototype keeps Projects · About · Contact inline at 390px.** Squarespace headers switch to a menu icon on mobile. **Nearest native:** the mobile menu (*Edit Site Header → Mobile*), with the same three links. *Affects: Header (1 place).*
- [ ] **F3 · Text sizes between Squarespace's seven styles.** Site Styles gives Heading 1–4 and Paragraph 1–3, one size each (plus a mobile size). The prototype uses a few sizes in between (listed with each block as "prototype: Npx"). **Nearest native:** the style named on the block. If her editor offers a size control on selected text (**verify**: it depends on the account's editor version), set the prototype size there; otherwise accept the style's size. *Affects: Footer, Room 01, Room 02, Room 03, Room 04, Projects, Homepage (83 places).*
- [ ] **F4 · On phones the cover title drops below the photo, in ink.** Text placed on a section background stays on it on mobile. **Nearest native:** keep the title on the photo on mobile (white, on the 38% overlay); in the mobile layout move it to the bottom rows. The meta table follows below. *Affects: Room 01, Room 02 (2 places).*
- [ ] **F5 · The case-study meta table overlaps the cover photo's bottom edge (Rooms 01, 02).** A block can't extend outside its section. **Nearest native:** put the white Shape block and the meta text in the **cover section's bottom rows**, so the card sits on the photo, flush with its bottom edge; on mobile, below the title. *Affects: Room 01, Room 02 (2 places).*
- [ ] **F6 · Inter Tight at 24px (stats names, "How might we…" lines at 28px).** Heading 4 is Instrument Serif 24px; Paragraph 1 is Inter Tight 40px. **Nearest native:** Heading 4 for the stats names; Paragraph 1 for the 28px "How might we…" lines and the italic Reflection paragraphs (28px is Paragraph 1's mobile size). *Affects: Room 01, Room 02, Room 03, Room 04 (13 places).*
- [ ] **F7 · The stats numbers ("60%", "10%", "30%") are 96px Inter Tight.** No native style is a 96px sans. **Nearest native:** Heading 2 (80px Instrument Serif). The numbers then read in the heading face; that is the only visible change. *Affects: Room 01 (3 places).*
- [ ] **F8 · Captions above the image (the Strip module) and "Running time" lines.** Image block captions sit below. **Nearest native:** a Paragraph 3 **Text** block above each image in the strip; for videos, the caption and running time go in a Text block beside the video (listed). *Affects: Room 02 (1 place).*
- [ ] **F9 · Her three quoted visitor stories have a 1px rule on the left and 20px italic text.** **Nearest native:** a **Quote** block (Squarespace styles it itself; no left rule) or Paragraph 2 in italic with a **Line** block set vertical (**verify** her editor offers vertical Line blocks). Keep the bold lead-in words bold. *Affects: Room 02 (3 places).*
- [ ] **F10 · Vertical videos are capped at 78% of the screen height and centred in cols 1–16.** **Nearest native:** size the Video block by hand: about cols 5–12 at desktop, centred, so it isn't taller than the screen. *Affects: Room 02, Room 03 (2 places).*
- [ ] **F11 · Littelfuse wireframes: a placeholder until she exports them from Adobe XD.** **Don't publish the grey placeholder.** Leave that figure out until the export arrives (ASSET-GAPS.md); the caption numbering after it stays as listed. *Affects: Room 04 (1 place).*
- [ ] **F12 · Pending content from the client.** LinkedIn URL (Contact), Littelfuse wireframes (Room 04), and confirmation for snippet 21 (the handwritten note, last in the slideshow). Build the rest; fill these when they arrive. *Affects: Room 04, Homepage (3 places).*
- [ ] **F13 · Lock-screen CSS class names.** The lock screen has no settings for the field rule, button fill or error style; CSS rules 7–14 do it, with class names taken from community examples, **not verified**. Check each in the browser inspector on her site; delete any that match nothing. *Affects: Lock Screen, Custom CSS (2 places).*
- [ ] **F14 · The lock screen's "No password? Email Yasmin →" is a link.** Lock-screen text fields may not accept links (**verify**). **Nearest native:** write the line with her address in it: "No password? Email yasminbajwa248@gmail.com". *Affects: Lock Screen (1 place).*
- [ ] **F15 · Wrong password: the prototype says "Incorrect password." under the field.** Squarespace shows its own message and wording. **Nearest native:** its message, restyled by CSS rule 10 (14px, 62% ink, no shake). *Affects: Lock Screen (1 place).*
- [ ] **F16 · Whole project rows are one link in the prototype.** Fluid Engine can't group blocks into one link. **Nearest native:** link the title text and the logo image block to the project page (both listed). *Affects: Projects, Homepage (2 places).*
- [ ] **F17 · The Snippets slideshow sits beside the text (cols 13–24), 4:5, with arrows, dots and a 400ms crossfade.** **Nearest native:** a **Gallery block** set to Slideshow inside the same section (**verify** her plan offers the Gallery block in Fluid Engine). If it doesn't, use a separate **Gallery section → Slideshow: Simple** directly below the text (it can't sit beside it). Transition timing and dots are Squarespace's own (**verify**). *Affects: Homepage (1 place).*
- [ ] **F18 · The discipline panels are four equal full-bleed columns, 60% of the screen tall, with hairlines between.** **Nearest native:** a full-width section (content width **Full**) with four Image blocks at cols 1–6 / 7–12 / 13–18 / 19–24 set to **Fill**. The 45% darkening and the hover use CSS rules 15–16. Fluid Engine's own gaps may leave a thin gap between panels instead of a hairline (**verify**; set block spacing to 0 if offered). *Affects: Homepage (1 place).*
- [ ] **F19 · Row hover: the logo tile darkens when the pointer is anywhere on the row.** No group hover in Fluid Engine. **Nearest native:** CSS rule 19 darkens the tile when the pointer is on the tile itself. *Affects: Homepage (1 place).*

Not carried over at all: the theme switcher, the `?theme=` links, and the five-palette comparison (prototype tools). The prototype's one script stands in for the native slideshow.

<div style="page-break-after: always"></div>

## Page 11 · Final checks

- [ ] Every page in **Preview** at desktop width and in the mobile view; compare with the prototype (`site/*.html`, or the screenshots in `screenshots/`).
- [ ] Every text block against **COPY-CHECK.md**: her copy is verbatim; the captions are the ones listed under *Added captions* (she approves them).
- [ ] Links: header (Projects, About, Contact), "View Projects →", every row and card (title + logo), chapter indexes (each `#ch-n` jumps to its chapter), prev / all / next on each project, Back to top, Email, Phone.
- [ ] Lock screen: test the password in a private window (Page 6).
- [ ] Pending before launch: LinkedIn URL, Littelfuse wireframes, snippet 21 confirmed (F12).
- [ ] Contrast spot-check: captions and labels stay at 62% ink (not lighter). The panel number "04" measures 3.6:1 on its photo in the prototype (THEMES.md, rendered audit): set that number's text to full white, or the darkening to 50% on that panel.
