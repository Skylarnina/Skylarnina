# Copy inventory: every word, in her order

The checklist for Round 3. Every heading, paragraph, bullet, table row, quote and production note from her two source documents, numbered, verbatim and in document order. `COPY-CHECK.md` will tick each ID against the built pages.

**Sources:** `source/CASE_STUDY-Yasmin_Bajwa.pdf` (the brief's `CASE STUDY-Yasmin Bajwa_compressed.pdf`, renamed in Phase 1) and `source/Instructions_About_Me.docx`.

**How it was made.** `tools/extract_copy.py` reads the PDF line by line with its fonts and writes `content/copy.json`. The pages will be generated from that file, and the copy check reads it too, so the site and this list can't drift apart. A word-by-word diff against the PDF's own text layer matches all **5,174 words in order**; the only difference is two Google Drive links the PDF wrapped across lines, joined back here. The About document matches paragraph for paragraph.

**The only clean-up applied** (none of it changes a word):
- lines of one paragraph or bullet are joined with a single space;
- bullet glyphs (●), invisible zero-width spaces and trailing spaces are removed;
- double spaces inside a line become one (e.g. "team I  evaluated"). A browser would collapse them anyway.

Spelling, punctuation and capitalisation are exactly hers, including the likely slips listed under **Questions**. Nothing is corrected unless she says so.

**Key to types:** `TITLE` project title · `META` Role / Methods line · `H2` chapter heading (these build the chapter index) · `H3` sub-heading · `H4` bold run-in label · `P` paragraph · `LI` bullet (`LI²`, `LI³` = nested levels) · `HMW` her bold "How might we" sentence · `QUOTE` UX-copy excerpt · `TABLE` table · `FIG` figure in her doc · `NOTE` her production note (not shown as text; it becomes the video, drawing or placeholder it asks for).

## Summary

| Project | Items | Chapters (H2) | Paragraphs | Bullets | Figures | Notes → media |
|---|---|---|---|---|---|---|
| Room 01 — The Henry Ford Jackson Home | 130 | 10 | 25 | 66 | 10 | 1 |
| Room 02 — Power & Energy | 67 | 10 | 29 | 5 | 8 | 5 |
| Room 03 — Rhode Island 401 Health App | 44 | 7 | 13 | 12 | 3 | 2 |
| Room 04 — Littelfuse | 45 | 5 | 21 | 3 | 3 | 1 |
| About (docx) | 12 | | | | | |

## About: `Instructions_About_Me.docx`

- **A-01** `BRIEF_H`: Portfolio Website Direction  
  → Brief to the designer, **not site copy** (Q1)
- **A-02** `BRIEF`: I want my portfolio to position me at the intersection of UX Design, UX Research, and Museum/Digital Experience Design. The overall site should feel modern, polished, and design-forward while still reflecting my background creating digital experiences within the museum world. I don’t want it to read as a traditional museum portfolio or a generic product-design portfolio—the museum/exhibition experience should be the element that makes my UX background distinctive.  
  → Brief to the designer, **not site copy** (Q1)
- **A-03** `BRIEF`: The landing page should feature a strong photo of me, a short introduction to who I am and what I do, and a clear CTA to View Projects. I’m open to incorporating the About Me content directly into the landing page or having a separate About page depending on what creates the cleanest experience. The developer can recommend the best structure.  
  → Brief to the designer, **not site copy** (Q1)
- **A-04** `BRIEF`: For the visual direction, I’d like the site to feel editorial, minimal, sophisticated, and highly visual, with thoughtful motion and interaction where appropriate. Case studies should be easy to scan but immersive enough to showcase research, workshops, user journeys, wireframes, prototypes, fabrication, and final experiences. I have a mixture of static imagery, diagrams, GIFs/video, and project documentation that should feel integrated rather than simply placed on the page. Please also include password protection.  
  → Brief to the designer, **not site copy** (Q1)
- **A-05** `H2`: About Me  
  → Homepage: section label for the About / statement area
- **A-06** `P`: Hi! I’m Yasmin, a Digital Exhibit Designer at The Henry Ford Museum with a multidisciplinary background in UX design, user research, and digital marketing. I’m passionate about bringing stories to life through digital experiences—and deeply inspired by history, fashion, and art.  
  → Homepage §1 **Hero**, under 'Hi, I'm Yasmin.'
- **A-07** `P`: By blending design, research, and exhibit development, I bring a fresh, curious perspective to every team. To me, every project is an opportunity to experiment, innovate, and create something people will remember.  
  → Homepage §2 **Statement** (A9), centred 40px
- **A-08** `INSTRUCTION`: Highlight these 4 skills in this order::  
  → Instruction to the designer, **not site copy**; followed exactly (skills shown in this order)
- **A-09** `SKILL`: Interactive Exhibit Design  
  → Homepage §3 **Four disciplines** (A10) panel label
- **A-10** `SKILL`: UX ( User Experience) Design  
  → Homepage §3 **Four disciplines** (A10) panel label
- **A-11** `SKILL`: UX Research  
  → Homepage §3 **Four disciplines** (A10) panel label
- **A-12** `SKILL`: Digital Marketing  
  → Homepage §3 **Four disciplines** (A10) panel label

Skill **A-10** reads `UX ( User Experience) Design` in her file, with a space after the bracket. See Q2.

## Room 01 — The Henry Ford Jackson Home

Page: `site/room-01-jackson-home.html`

**Chapter index (her H2 headings, her order):** 1 Project Overview · 2 The Challenge · 3 Research Questions · 4 Research Methodology · 5 Building the Simulation · 6 Baseline Assumptions · 7 Scenario Testing · 8 Findings · 9 Impact · 10 Reflection

### Header (A1 + A4)

- **J-001** `TITLE` p1: The Henry Ford Jackson Home Visitor Flow Simulation
- **J-002** `META` p1: **Role**: UX Researcher | Experience Design  
  → header meta panel (ROLE)
- **J-003** `META` p1: **Methods**: Behavioral Observation • Space Syntax Analysis • Behavioral Path Clustering • Visitor Segmentation • Discrete Event Simulation • Predictive Modeling  
  → header meta panel (METHODS)

### Chapter 1: Project Overview
*Layout: A2 chapter: number + title left (6 cols), text right (12 cols).*

- **J-004** `H2` p1: Project Overview
- **J-005** `P` p1: The Dr. Sullivan and Mrs. Richie Jean Sherrod Jackson Home is a nationally significant historic residence associated with the 1965 Selma to Montgomery marches, where civil rights leaders, including Dr. Martin Luther King Jr., gathered to develop strategies that contributed to the passage of the Voting Rights Act. After being relocated to Greenfield Village at The Henry Ford museum, the home was prepared to open to the public as a permanent exhibition in Summer 2026.
- **J-006** `P` p1: As the first building added to Greenfield Village in more than forty years, there was no historical visitor data to guide operational planning. My role was to develop a predictive visitor flow model that would forecast how guests would move through the constrained historic space before opening day.
- **J-007** `P` p1: Using UX research methodologies and behavioral modeling, I created a visitor simulation that allowed stakeholders to evaluate different ticketing strategies, estimate visitor capacity, identify potential congestion points, and determine where presenters should be positioned to create a comfortable and engaging visitor experience.

### Chapter 2: The Challenge
*Layout: A2 chapter. Constraints as a real list; the 'How might we' line as a pull sentence.*

- **J-008** `H2` p1: The Challenge
- **J-009** `P` p1: No behavioral data existed, planning visitor capacity relied on assumptions rather than evidence. The home's preserved architectural layout introduced additional constraints:
- **J-010** `LI` p1: Narrow circulation paths
- **J-011** `LI` p1: Limited room capacity
- **J-012** `LI` p1: Sequential visitor movement
- **J-013** `LI` p1: Preservation requirements that prevented structural modifications
- **J-014** `P` p2: The challenge became:
- **J-015** `HMW` p2: How might we predict visitor behavior and optimize the museum experience before the exhibition opened to the public?

### Chapter 3: Research Questions
*Layout: A3 label / text rows: each sub-heading (Visitor Experience · Capacity Planning · Operations) is the row label, its bullets the text.*

- **J-016** `H2` p2: Research Questions
- **J-017** `P` p2: To support exhibition planning, I focused on answering several key research questions.
- **J-018** `H3` p2: Visitor Experience
- **J-019** `LI` p2: How long will visitors spend inside the home?
- **J-020** `LI` p2: Where are visitors most likely to stop or experience congestion?
- **J-021** `LI` p2: What will waiting times look like throughout the experience?
- **J-022** `H3` p2: Capacity Planning
- **J-023** `LI` p2: How many visitors can comfortably occupy both the Jackson Home and Annex (complimentary building with digital interactives) without overcrowding?
- **J-024** `LI` p2: Should visitors enter through 15-minute or 30-minute ticketing windows?
- **J-025** `LI` p2: Can walk-up visitors be accommodated without negatively affecting the experience?
- **J-026** `H3` p2: Operations
- **J-027** `LI` p2: Where should docents and presenters be positioned to support visitor flow?
- **J-028** `LI` p2: What traffic management strategies should staff use during peak attendance?

### Chapter 4: Research Methodology
*Layout: A3 rows for the three methods. The visitor-type table becomes an **A4 stats strip** (60% · 10% · 30% with her characteristic text beneath each; see Q5).*

- **J-029** `H2` p2: Research Methodology
- **J-030** `P` p2: Because no baseline visitor data existed for the Jackson Home, I combined several UX research methodologies to build a predictive behavioral model.
- **J-031** `H3` p2: Behavioral Observation
- **J-032** `P` p2: I analyzed visitor movement within comparable historical homes and nearby exhibitions at The Henry Ford to understand common behavioral patterns. These observations focused on:
- **J-033** `LI` p2: visitor arrival behavior
- **J-034** `LI` p2: walking speed
- **J-035** `LI` p2: dwell time
- **J-036** `LI` p2: congestion points
- **J-037** `LI` p2: exhibit engagement
- **J-038** `LI` p2: decision-making at transitions between rooms
- **J-039** `P` p2: These findings established the behavioral assumptions used throughout the simulation.
- **J-040** `H3` p3: Space Syntax Analysis
- **J-041** `P` p3: In collaboration with our experience design team I evaluated the home's architectural layout to understand how visibility, room connectivity, and circulation paths would naturally influence visitor movement. This helped identify areas likely to become bottlenecks before testing any operational scenarios.
- **J-042** `H3` p3: Behavioral Path Clustering
- **J-043** `P` p3: Behavioral observations revealed that visitors interact with museum environments differently depending on their engagement level. We simulate this behavior by randomly assigning a visitor type to each person and then reducing the average view time at each exhibit to give the correct %. This results in a very different time profile for each type of visitor to the Jackson Home: To reflect these differences, visitors were grouped into three behavioral archetypes based on existing museum research and validated using historical attendance patterns from The Henry Ford.
- **J-044** `TABLE` p3: Visitor Type | Characteristics | Distribution
  - Strollers | Browse most exhibits with moderate viewing time | 60%
  - Studiers | Read interpretation thoroughly and spend longer in each room | 10%
  - Streakers | Move quickly through the exhibition with minimal stopping | 30%
- **J-045** `P` p3: Each simulated visitor was randomly assigned one of these behavioral profiles, allowing the model to better represent realistic variation in visitor behavior.
- **J-046** `FIG` `doc-01` (p3): the visitor-type table **and** a 'Time Spent On-Site' box plot in one image. Only copy (975px). The table is set as live text (the J-table above), so the figure shows the box-plot half: `r01-chart-onsite-box.jpg`.
- **J-047** `FIG` `doc-02` (p4): Congestion / Queue sizes / Visit time / Delays sheet. Full-res original: `r01_chart_congestion-queues-visit-delays.png`. **A6 board**, lightbox.

### Chapter 5: Building the Simulation
*Layout: A2 chapter, then plates in her order.*

- **J-048** `H2` p4: Building the Simulation
- **J-049** `P` p4: Using behavioral research, I developed a discrete event simulation that modeled individual visitor movement throughout the exhibition. The simulation followed wayfinding based on the expected paths in the home, displayed below. Each visitor independently navigated the home while interacting with operational constraints including:
- **J-050** `LI` p4: timed ticket arrivals
- **J-051** `LI` p4: room occupancy limits
- **J-052** `LI` p4: queue formation
- **J-053** `LI` p4: walking speed
- **J-054** `LI` p4: exhibit dwell time
- **J-055** `LI` p4: presenter intervention
- **J-056** `LI` p4: alternative routing when spaces reached capacity
- **J-057** `P` p4: Rather than moving visitors as a group, every individual made independent movement decisions based on available space and predefined behavioral rules. This allowed the simulation to realistically forecast congestion and visitor flow under multiple operational scenarios.
- **J-058** `FIG` `doc-03` (p5): house plan without paths. Full-res: `r01_plan_house.png`. Plate.
- **J-059** `FIG` `doc-04` (p6): Annex plan. Only copy (975px). Plate.
- **J-060** `FIG` `doc-05` (p7): house plan **with visitor paths**. Full-res: `r01_plan_house-visitor-paths.png`. **A5/A14 plan-plus-list spread** with Baseline Assumptions (the next chapter), as the brief asks.
- **J-061** `NOTE` p8: "INSERT VIDEO HERE - DISCRETE EVENT SIMULATION"  
  → Video block → `r01_video_discrete-event-simulation.mp4` (received in Phase 2; player bar cropped). A5 video with play button.

### Chapter 6: Baseline Assumptions
*Layout: **A5 / A14 spread**: house plan with paths (J-fig 5) beside her 7 assumptions.*

- **J-062** `H2` p8: Baseline Assumptions
- **J-063** `P` p8: Since the exhibition had not yet opened, several assumptions were established using observations from comparable exhibitions. These assumptions provided a consistent foundation for comparing operational scenarios.
- **J-064** `P` p8: These included:
- **J-065** `LI` p8: Visitors arrive within their assigned ticket window.
- **J-066** `LI` p8: Ticket windows operate in either 15-minute or 30-minute intervals.
- **J-067** `LI` p8: Visitors travel independently while naturally clustering into small social groups.
- **J-068** `LI` p8: Average walking speed is approximately 2.0 mph, representing most museum visitors.
- **J-069** `LI` p8: Each exhibit has a maximum occupancy determined by available floor space.
- **J-070** `LI` p8: When capacity is reached, visitors either wait or continue to another available location.
- **J-071** `LI` p8: Individual viewing times vary according to visitor type and natural behavioral variation.

### Chapter 7: Scenario Testing
*Layout: Nested lists kept at her three levels; charts as an **A6 board** with captions + lightbox.*

- **J-072** `H2` p8: Scenario Testing
- **J-073** `H4` p8: STUDY FACTORS
- **J-074** `LI` p8: Ticketing Window:
  - **J-075** `LI²` p8: 30-minute windows
  - **J-076** `LI²` p8: 15-minute windows
- **J-077** `LI` p8: Arrival Pattern:
  - **J-078** `LI²` p8: Random times within ticketing window
  - **J-079** `LI²` p8: All arrive at start of ticketing window
- **J-080** `LI` p8: Docent Control:
  - **J-081** `LI²` p8: No constraint – visitors enter if there is space in the vestibule
  - **J-082** `LI²` p8: With constraint – docent allows ~8 people at a time into entrance area (Vestibule, Pre 1965 and Video Wall)
- **J-083** `LI` p8: Number of tickets:
  - **J-084** `LI²` p8: Base: 48 per 30-minutes or 24 per 15-minutes
  - **J-085** `LI²` p8: Low: 38 per 30-minutes or 20 per 15-minutes
  - **J-086** `LI²` p8: High: 58 per 30-minutes or 28 per 15-minutes
- **J-087** `LI` p8: Walk-up Visitors:
  - **J-088** `LI²` p8: A limited number of un-ticketed visitors may be allowed to join the queue if the ticketed visitors have entered the building
- **J-089** `H4` p9: Ticketing Window & Arrival Patterns
- **J-090** `LI` p9: The effects of these factors are linked
- **J-091** `LI` p9: If visitor arrivals are spread randomly through the ticketing window
  - **J-092** `LI²` p9: Congestion and queue sizes are low
  - **J-093** `LI²` p9: Visitors rarely have to skip exhibits
  - **J-094** `LI²` p9: Total time spent on-site matches expectations
  - **J-095** `LI²` p9: There is no significant difference between 30-minute or 15-minute ticketing windows
- **J-096** `FIG` `doc-06` (p9): Random arrivals chart. Full-res: `r01_chart_arrivals-random.png`. **A6 board**.
- **J-097** `H4` p9: Ticketing Window & Arrival Patterns
- **J-098** `LI` p9: If most visitors arrive close to the start of the ticketing window
  - **J-099** `LI²` p9: Congestion and queue sizes are high
  - **J-100** `LI²` p9: With no docent control at the entrance, skipping behavior balloons
    - **J-101** `LI³` p9: This could result in many unhappy visitors!
  - **J-102** `LI²` p9: Average time spent on-site increases by just a few minutes, but the maximum time on-site almost doubles!
  - **J-103** `LI²` p9: In this case, all indicators are much better if 15-minute ticketing windows are used
- **J-104** `FIG` `doc-07` (p10): On-time arrivals chart. Full-res: `r01_chart_arrivals-on-time.png`. **A6 board**.
- **J-105** `FIG` `doc-08` (p10): Expected Visit Times. Full-res: `r01_chart_expected-visit-times.png`. **A6 board**.

### Chapter 8: Findings
*Layout: **A7**: the four findings as a numbered 01–04 list on the right, the docent / best-scenario plates on the left.*

- **J-106** `H2` p10: Findings
- **J-107** `H3` p10: Ticketing Strategy
- **J-108** `P` p10: Visitors were expected to arrive near the beginning of their assigned ticket windows, particularly during the exhibition's opening months.
- **J-109** `P` p11: A 15-minute ticketing schedule distributed arrivals more evenly than 30-minute windows, reducing congestion throughout the home.
- **J-110** `H3` p11: Capacity
- **J-111** `P` p11: While the home could accommodate a maximum of approximately 32 visitors every 15 minutes, a capacity of 30 visitors per entry window created a noticeably more comfortable visitor experience while maintaining operational efficiency.
- **J-112** `H3` p11: Presenter Placement
- **J-113** `P` p11: Simulation results demonstrated that placing presenters near the first exhibits significantly improved visitor flow.
- **J-114** `P` p11: Presenters helped regulate entry into high-demand spaces, reduced skipped exhibits, and minimized bottlenecks during periods of heavy attendance. The recommended staffing model included three to four presenters positioned throughout key zones of the home during opening operations.
- **J-115** `H3` p11: Walk-Up Visitors
- **J-116** `P` p11: Allowing a controlled mix of ticketed and walk-up visitors naturally staggered arrivals, reducing congestion and average waiting times while increasing access for guests unable to reserve tickets in advance.
- **J-117** `FIG` `doc-09` (p12): Without / With docent charts. Full-res: `r01_chart_docent-control.png`. **A6 board**.
- **J-118** `FIG` `doc-10` (p12): 'Best scenario: tickets 20, walkups 8, with docent control'. Only copy (975px). **A6 board**.

### Chapter 9: Impact
*Layout: **A7** numbered list of her 7 bullets.*

- **J-119** `H2` p13: Impact
- **J-120** `P` p13: The visitor flow simulation provided stakeholders with evidence-based recommendations before the Jackson Home opened to the public. The research directly informed operational planning by helping teams:
- **J-121** `LI` p13: establish ticketing schedules for opening operations
- **J-122** `LI` p13: determine comfortable visitor capacity limits
- **J-123** `LI` p13: identify high-congestion areas before opening
- **J-124** `LI` p13: optimize presenter placement throughout the home
- **J-125** `LI` p13: evaluate queue management strategies
- **J-126** `LI` p13: deciding factor for where to place digital interactives in the exhibit
- **J-127** `LI` p13: improve visitor flow while preserving the historic integrity of the building
- **J-128** `P` p13: Rather than relying on assumptions alone, leadership was able to make operational decisions supported by predictive behavioral research and simulation.

### Chapter 10: Reflection
*Layout: Centred, 28px italic.*

- **J-129** `H2` p13: Reflection
- **J-130** `P` p13: This project broadened my understanding of user experience beyond digital products, demonstrating how UX research methodologies can be applied to improve experiences within physical environments. It also deepened my appreciation for how visitors engage with and process complex, emotionally significant stories, particularly those centered on difficult history

## Room 02 — Power & Energy

Page: `site/room-02-power-energy.html`

**Chapter index (her H2 headings, her order):** 1 Project Overview · 2 The Challenge · 3 The Approach/ UX Design · 4 Discovery & Stakeholder Alignment · 5 Designing the Interactive Experience · 6 CMS Integration & Implementation · 7 Installation & Fabrication · 8 Results & Impact · 9 Ongoing Evaluation · 10 Reflection

### Header (A1 + A4)

- **P-001** `TITLE` p13: Designing an Interactive Museum Experience for Power & Energy
- **P-002** `META` p13: **Role**: UX Designer| Experience Design | Project Management  
  → header meta panel (ROLE)
- **P-003** `META` p13: **Methods**: Information Architecture • User Flows • Wireframing • Content Strategy  
  → header meta panel (METHODS)

### Chapter 1: Project Overview
*Layout: A2 / A3 chapter: number + title left, her text right.*

- **P-004** `H2` p14: Project Overview
- **P-005** `P` p14: The goal of this project was to enhance The Henry Ford Museum’s Power & Energy exhibit through a multi-sided interactive digital column that serves as both a visual entrance marker and a centralized storytelling experience. Furthermore, the column was inspired by an existing column in a nearby exhibit.
- **P-006** `P` p14: The column was designed for student groups, families, and general museum visitors, the column combines video content, interactive content, wayfinding, and artifact highlights to communicate the exhibit’s central themes—including the interconnectedness and tradeoffs involved in energy production, distribution, and use.
- **P-007** `P` p14: The experience also incorporates content from project partner ITC( International Transmission Company) and was built in Appspace, the museum’s institutional content management system, allowing internal teams to maintain and update the experience over time.

### Chapter 2: The Challenge
*Layout: Two A3 rows (sub-heading = label) with each 'How might we' as a pull sentence.*

- **P-008** `H2` p14: The Challenge
- **P-009** `H3` p14: Capturing Visitor Attention
- **P-010** `P` p14: In an exhibit filled with large-scale artifacts and live programming, the digital column needed to capture attention without competing with the physical environment.
- **P-011** `HMW` p14: How might we create an intuitive digital experience that encourages visitors of all ages to pause, explore, and learn?
- **P-012** `H3` p14: Balancing Museum and Sponsor Goals
- **P-013** `P` p14: The experience needed to support The Henry Ford’s educational mission while incorporating ITC’s industry, career, and employee stories without feeling overly promotional.
- **P-014** `HMW` p14: How might we introduce students to careers in power and energy while balancing visitor, museum, and sponsor needs?

### Chapter 3: The Approach/ UX Design
*Layout: A2 chapter. The five 'experience included' bullets sit beside an **A6 board of the five column-art panels** (see Q6).*

- **P-015** `H2` p14: The Approach/ UX Design
- **P-016** `P` p14: To address visitor, educational, wayfinding, and sponsor needs, I developed a multi-sided experience that combined passive storytelling with touch-based exploration. Each side of the column served a distinct purpose while contributing to a cohesive visitor journey.
- **P-017** `P` p15: The experience included:
- **P-018** `LI` p15: Exhibit wayfinding: A backlit graphic identifying the Power & Energy exhibit and introducing its central themes.
- **P-019** `LI` p15: Innovation stories: Condensed Innovation Nation episodes highlighting innovation across power and energy. Innovation Nation is an educational television series produced by The Henry Ford that explores inventions, innovators, and technological advancements shaping the world.
- **P-020** `LI` p15: Interactive exploration: A touch-based map visualizing power transmission infrastructure across Michigan and the United States.
- **P-021** `LI` p15: Career discovery: ITC employee interviews introducing students to careers within the power and energy industry.
- **P-022** `LI` p15: Artifact interpretation: A backlit graphic highlighting key artifacts and providing additional historical context based on what was inside the exhibit.
- **P-023** `P` p15: I began to take the existing column we have in the Agriculture column and talk through how the Power & Energy column would look and feel. In addition I began to sketch and create lo- fi wireframes to share with key stakeholders for feedback( See below).
- **P-024** `FIG` `doc-11` (p15): content themes and experience-flow board. Full-res: `r02_board_content-themes-experience-flow.png`.
- **P-025** `FIG` `doc-12` (p16): whiteboard lo-fi sketches. Full-res: `r02_sketch_whiteboard-lofi.png`.

### Chapter 4: Discovery & Stakeholder Alignment
*Layout: A2 chapter; the three UX-copy excerpts as **indented pull quotes**.*

- **P-026** `H2` p16: Discovery & Stakeholder Alignment
- **P-027** `P` p16: Once the content strategy for each side of the column was established, I began developing the individual experiences and determining how each could support the broader goals of the Power & Energy exhibit. Visually, the backlit graphics were designed to maintain consistency with the existing exhibit while the interactive content introduced new opportunities for visitor engagement.
- **P-028** `P` p16: For the ITC career experience, the goal was to introduce visitors to the range of careers that support the power and energy industry. Working with ITC stakeholders, I identified three employee volunteers representing different areas of the organization: Safety & Security, Engineering, and Community Planning. I interviewed each employee about their role, responsibilities, career path, and connection to the energy industry. These conversations became the foundation for the career-focused content featured within the interactive. Employee interviews and responses informed the content shown below. Furthermore, below is a summary of highlighted content that was relevant and used in the final wireframes
- **P-029** `FIG` `doc-13` (p17): ITC employee research board. Full-res: `r02_board_itc-employee-research.png`.
- **P-030** `P` p17: In addition to the employee stories, I explored how the experience could connect careers in energy to objects, stories, and experiences visitors could encounter elsewhere in the museum. I developed short prompts for each career area using The Henry Ford’s Model i framework, an educational model that encourages learners to develop the habits and actions of innovators through curiosity, questioning, collaboration, and problem-solving. Because engaging younger visitors was an important project goal, these prompts were intentionally written to encourage exploration beyond the screen—connecting the digital experience back to the physical museum and inviting visitors to continue discovering how innovation, engineering, safety, and community planning shape the world around them.
- **P-031** `P` p17: Excerpts from the UX copy below:
- **P-032** `QUOTE` p17: “Engineering Together: Thomas Edison employed dozens of engineers, inventors, and chemists at the Menlo Park Laboratory, where they collectively developed hundreds of technological innovations. Experience Menlo Park Laboratory for yourself in Greenfield Village.”
- **P-033** `QUOTE` p18: “Safety & Security: As electric companies built new infrastructure around the country, they hired workers to construct and inspect the new poles and lines. To learn more, visit the Edison Illuminating Company’s Station A in Greenfield Village.”
- **P-034** `QUOTE` p18: “Community Planning: Thomas Edison tested and gathered feedback on his experimental lighting system with the men and women who lived at the Sarah Jordan Boarding House. Step inside the Boarding House in Greenfield Village.”

### Chapter 5: Designing the Interactive Experience
*Layout: A2 / A3 chapter: number + title left, her text right.*

- **P-035** `H2` p18: Designing the Interactive Experience
- **P-036** `P` p18: I then began finalizing the experience, focusing on the interaction touchpoints, content flow, and visual design. This was an iterative process informed by an existing interactive column within the museum’s Agriculture exhibit.
- **P-037** `P` p18: I began by evaluating the Agriculture column’s existing user flow, including its interaction rules, touchpoints, and the way content was distributed across the different sides of the column. I also reviewed findings from previous guest observations to understand how visitors actually approached, navigated, and engaged with the experience.
- **P-038** `P` p18: These behavioral insights became an important input into the final design. They helped determine how visitors would move through the Power & Energy experience, which types of content were best suited for each side of the column, and how the overall interaction flow should be structured.
- **P-039** `P` p18: The resulting flow and content distribution are illustrated in the diagram below. The final wireframes shown below.
- **P-040** `FIG` `doc-14` (p19): the column's sides + interaction flow diagram. Full-res: `r02_diagram_column-sides-flow.png`.
- **P-041** `NOTE` p20: "INSERT VIDEO HERE BELOW IS SCREEN GRAB OF WHAT IT LOOKS LIKE"  
  → Video block → `r02_video_interface-user-flow.mp4`, replacing the screen grab `doc-15`.
- **P-042** `FIG` `doc-15` (p20): screen grab of the interface. **Replaced by the video** her note just above asks for.

### Chapter 6: CMS Integration & Implementation
*Layout: A2 chapter + A5 video.*

- **P-043** `H2` p20: CMS Integration & Implementation
- **P-044** `P` p20: The museum uses multiple content management systems to publish and maintain digital experiences. For this project, an institutional priority was to host and manage the content within Appspace, a cloud-based platform used to organize, publish, and update digital content across devices.
- **P-045** `P` p20: I collaborated closely with the Appspace team to ensure all final assets met the required dimensions, aspect ratios, and technical specifications. I led conversations with the Appspace partner manager, communicating the experience’s interaction points, user flow, and information architecture to guide the platform setup. Once configured, I built and managed the content channels, programmed the interactive interface, and implemented ongoing updates as the content and experience evolved. Below are the CMS channels within App Space.
- **P-046** `NOTE` p20: "INSERT POWER & ENERGY VIDEO HERE"  
  → Video block → `r02_video_appspace-cms-channels.mp4` (the CMS channels she describes in the line above).

### Chapter 7: Installation & Fabrication
*Layout: A2 chapter; shop drawings as full-width plates; fabrication video (A5).*

- **P-047** `H2` p21: Installation & Fabrication
- **P-048** `P` p21: For the final installation, we partnered with Sleet Custom Cabinets, a fabricator familiar with the museum environment who had previously built the interactive columns and enclosures within the Agriculture exhibit. Building on this existing design helped maintain consistency across the museum while providing a proven framework for the new Power & Energy columns.
- **P-049** `P` p21: I worked closely with the fabricator to provide precise dimensions, specifications, and printing requirements for the backlit graphics. The new columns were designed to match the dimensions and construction of the existing Agriculture columns.
- **P-050** `P` p21: My role during this phase was to coordinate and manage the various teams involved in fabrication and installation, ensuring that the physical build, digital components, graphics, and technical requirements came together successfully and on schedule. Below are the CMS channels within App Space.
- **P-051** `NOTE` p21: "USE PDF VERSION HERE OF DRAWINGS"  
  → Three full-width plates rendered from `PandE_Shop-Drawing_Column-Surrounds_AV05.pdf`, replacing `doc-16/17/18`.
- **P-052** `FIG` `doc-16` (p21): shop drawing sheet 1. **Replaced by the vector PDF** her note asks for: `PandE_Shop-Drawing_Column-Surrounds_AV05.pdf` p1, full-width plate.
- **P-053** `FIG` `doc-17` (p22): shop drawing sheet 2 → vector PDF p2, full-width plate.
- **P-054** `FIG` `doc-18` (p22): shop drawing sheet 3 → vector PDF p3, full-width plate.
- **P-055** `NOTE` p23: "ADD COLUMN FABRICATION VIDEO HERE - https://drive.google.com/file/d/1cKmaAiyAW03hFPZ2O-OOlia55EY6v4pV/view?usp=drive_link"  
  → Video block → `r02_video_fabrication-progression.mp4` (the file behind this link).

### Chapter 8: Results & Impact
*Layout: **A7** numbered list + final-setup video.*

- **P-056** `H2` p23: Results & Impact
- **P-057** `P` p23: The Power & Energy interactive column transformed the exhibit entrance into a more intentional visitor touchpoint, creating a clear visual anchor while introducing new opportunities for exploration and learning.
- **P-058** `P` p23: The final experience supported multiple visitor needs through artifact discovery, career exploration, wayfinding, and interactive learning. It also advanced institutional technology goals by integrating the experience into the museum’s CMS ecosystem, creating a more flexible framework for managing and updating digital content.
- **P-059** `P` p23: For project sponsor ITC, the experience provided a meaningful way to connect the Power & Energy story to the people behind the industry by highlighting employee perspectives and diverse career pathways.
- **P-060** `NOTE` p23: "ADD Final Results video here - https://drive.google.com/file/d/1OW2QVKf-GOFc-GanrBi_6sppCcU5P3JF/view?usp=share_link"  
  → Video block → `r02_video_final-setup.mp4` (the file behind this link).

### Chapter 9: Ongoing Evaluation
*Layout: A2 / A3 chapter: number + title left, her text right.*

- **P-061** `H2` p23: Ongoing Evaluation (her source sets this at 12–13pt; treated as a chapter like her other projects; Q4)
- **P-062** `P` p23: Because the experience was recently launched, long-term visitor impact has not yet been measured. The next phase of evaluation will focus on understanding how visitors engage with the column in the museum environment.
- **P-063** `P` p23: Planned UX research includes museum volunteer focus groups, testing with The Henry Ford Academy students, and in-gallery visitor observation. Findings will be used to evaluate discoverability, usability, engagement, and opportunities for future content and interaction improvements.

### Chapter 10: Reflection
*Layout: Centred, 28px italic.*

- **P-064** `H2` p23: Reflection
- **P-065** `P` p23: This project expanded my understanding of UX design beyond traditional mobile and desktop interfaces. Designing for a physical museum environment required me to consider not only the interface itself, but also spatial interaction, accessibility, visitor behavior, and the physical context surrounding the experience.
- **P-066** `P` p24: Working across touch displays, backlit graphics, static interpretation, and physical exhibit elements also challenged me to think about information architecture at an environmental scale—determining not only how visitors would navigate content, but where that content should live and how each touchpoint could contribute to a cohesive experience.
- **P-067** `P` p24: Most importantly, the project reinforced that UX does not stop at the screen. Creating an effective museum experience requires balancing digital interaction with physical space, technical constraints, accessibility, storytelling, and the different ways visitors choose to engage.

## Room 03 — Rhode Island 401 Health App

Page: `site/room-03-rhode-island.html`

**Chapter index (her H2 headings, her order):** 1 Project Overview · 2 The Challenge · 3 The Approach/ Discovery & Stakeholder Alignment · 4 UX Design/ Feature Prioritization · 5 Results & Impact · 6 Ongoing Evaluation · 7 Reflection

### Header (A1 + A4)

- **R-001** `TITLE` p24: Rhode Island State COVID Vaccine App/401 Health App
- **R-002** `META` p24: **Role**: UX Designer| UX Researcher | UX Consultant  
  → header meta panel (ROLE)
- **R-003** `META` p24: **Methods**: Qualitative Research • Quantitative Analysis • Feedback Synthesis • Competitive/Heuristic Review • Content Strategy • Wireframing  
  → header meta panel (METHODS)

### Chapter 1: Project Overview
*Layout: A2 / A3 chapter: number + title left, her text right.*

- **R-004** `H2` p24: Project Overview
- **R-005** `P` p24: The goal of this project was to improve the State of Rhode Island’s vaccine website and health application, making it easier for residents to report vaccination information and access their vaccination records. The redesigned experience streamlined the reporting process while providing the state with reliable, timely data to support public health decision-making during the COVID-19 pandemic. It also made proof of vaccination easier for residents to access and present when entering large events and other venues requiring verification. Ultimately, the experience aimed to increase vaccination reporting completion rates by 23%, while creating a simpler, more accessible way for residents to manage and use their vaccination information.

### Chapter 2: The Challenge
*Layout: Two A3 rows (sub-heading = label), each with its 'How might we...' list.*

- **R-006** `H2` p24: The Challenge
- **R-007** `H4` p24: Building Trust and Increasing Adoption of Digital Vaccination Records
- **R-008** `P` p25: Research and stakeholder feedback revealed a key barrier to adoption: residents were hesitant to share personal health information and unsure how a digital platform would securely manage their vaccination records. At the same time, residents saw value in having convenient digital access to their vaccination information.
- **R-009** `P` p25: The challenge was to create a sign-up and onboarding experience that reduced friction, established trust, and clearly communicated the value of maintaining a digital vaccination record.
- **R-010** `H4` p25: How might we...
- **R-011** `LI` p25: Create a seamless sign-up and onboarding experience that encourages residents to complete their vaccination record?
- **R-012** `LI` p25: Build trust by clearly communicating privacy, security, and how personal information is used?
- **R-013** `LI` p25: Demonstrate the value of digital vaccination records for events, travel, and other verification needs?
- **R-014** `H4` p25: Reducing Friction Through Health Record Integration
- **R-015** `P` p25: A second challenge was eliminating the need for residents to manually re-enter vaccination information already reported to the Rhode Island Child and Adult Immunization Registry (RICAIR). Because healthcare providers and pharmacies were already submitting immunization data to RICAIR, residents expected their existing records to be available within the application.
- **R-016** `P` p25: The challenge was to design a secure, intuitive way for users to authorize access to their existing records while clearly communicating where their information came from and how it would be used.
- **R-017** `H4` p25: How might we...
- **R-018** `LI` p25: Make it simple for residents to securely authorize access to their existing vaccination records?
- **R-019** `LI` p25: Clearly communicate where vaccination data comes from and how it is being used?
- **R-020** `LI` p25: Reduce unnecessary manual entry while maintaining confidence in the accuracy and privacy of health information?

### Chapter 3: The Approach/ Discovery & Stakeholder Alignment
*Layout: A2 chapter; goals table as a full plate; App Store video (A5) in place of the picture.*

- **R-021** `H2` p25: The Approach/ Discovery & Stakeholder Alignment
- **R-022** `P` p26: To better understand the existing application experience, Rhode Island state employees shared user feedback and analytics related to website and app usage with my team. I conducted stakeholder interviews with employees across different areas of the program, typically in small groups of no more than two participants to enable focused discussions and gather perspectives from different areas of the program. Through conversations with employees about the existing app and web experience, I began to identify the Rhode Island Department of Health’s broader program goals and priorities. Aligning the design direction with these strategic objectives was essential to gaining leadership support and moving the project forward. The following goals helped guide the design process (Goals 20-23). Several key themes emerged, including frustration with manually re-entering vaccination information and concerns about trusting the system with sensitive health data. I also analyzed Google Play and Apple App Store reviews to identify recurring user pain points, usability issues, and technical challenges within the existing experience. Common themes included difficulties with account setup, barriers to completing key tasks, and uncertainty around how vaccination information was managed. See below.
- **R-023** `P` p26: These insights helped us identify usability opportunities, prioritize design recommendations, and guide the development of a more intuitive, accessible, and trustworthy vaccination management experience.
- **R-024** `FIG` `doc-19` (p27): the 23 population-health goals table. Only copy (975px). Full plate with caption.
- **R-025** `NOTE` p27: "INSERT VIDEO OF APP STORE REVIEWS HERE ( PICTURE IS ONLY FOR REFERENCE)"  
  → Video block → `r03_video_app-store-reviews.mp4`, replacing the reference picture `doc-20`.
- **R-026** `FIG` `doc-20` (p28): App Store review screenshot, which her note calls 'only for reference'. **Replaced by the video** `r03_video_app-store-reviews.mp4`.

### Chapter 4: UX Design/ Feature Prioritization
*Layout: A2 chapter; the six features as a list; wireframes video; the two mobile screens side by side (**A2 wide + tall**).*

- **R-027** `H2` p28: UX Design/ Feature Prioritization
- **R-028** `P` p28: The solution focused on reducing user effort by creating a streamlined authorization flow that automatically populated vaccination records from an existing health data source. Once authenticated, users could review their vaccination history, add missing information when needed, and manage household members within a single account. This approach reduced duplicate data entry while creating a more intuitive and efficient experience.
- **R-029** `P` p28: Feature prioritization centered on improving usability, accessibility, and access to essential public health services. Key features included:
- **R-030** `LI` p28: Vaccination Status: A clear status card displaying COVID-19 vaccination history, including individual doses.
- **R-031** `LI` p29: Multilingual Support: Terms and Conditions available in multiple languages, including Portuguese, to support Rhode Island’s diverse communities.
- **R-032** `LI` p29: Appointment Scheduling: An integrated calendar that allowed users to find and schedule vaccination appointments.
- **R-033** `LI` p29: Household Management: The ability to add and manage household members and their vaccination records from a single account.
- **R-034** `LI` p29: Symptom Diary: An optional tool for anonymously reporting post-vaccination symptoms, providing the Rhode Island Department of Health with data to support public health monitoring.
- **R-035** `LI` p29: Testing Location Map: An interactive map helping users quickly locate nearby COVID-19 testing services.
- **R-036** `NOTE` p29: "INSERT PDF OR VIDEO OF DESKTOP & MOBILE WIRE FRAMES HERE"  
  → Video block → `r03_video_wireframes.mp4` (desktop). Mobile screens from `Rhode_Island_DOH_Wireframes.pdf` can sit beside it; see Q7.
- **R-037** `FIG` `doc-21` (p29): annotated 'Vaccine Details' board (two phone screens with callouts). Full-res: `r03_ui_vaccine-details-annotated.png`. See question Q7 (device frames).

### Chapter 5: Results & Impact
*Layout: **A7** layout.*

- **R-038** `H2` p29: Results & Impact (her source sets this at 12–13pt; treated as a chapter like her other projects; Q4)
- **R-039** `P` p29: The redesigned experience streamlined how Rhode Island residents accessed and managed their vaccination information by providing a digital alternative to the paper vaccination cards used during the initial COVID-19 vaccine rollout. The multilingual experience also expanded accessibility, helping more residents navigate and manage their health information with confidence.

### Chapter 6: Ongoing Evaluation
*Layout: A2 / A3 chapter: number + title left, her text right.*

- **R-040** `H2` p30: Ongoing Evaluation (her source sets this at 12–13pt; treated as a chapter like her other projects; Q4)
- **R-041** `P` p30: Long-term adoption and engagement metrics were outside the scope of my involvement. However, the design recommendations prioritized reducing friction, strengthening user trust, and simplifying access to critical vaccination information. The experience was also designed with flexibility in mind, allowing the platform to evolve alongside future vaccination programs and changing public health needs.

### Chapter 7: Reflection
*Layout: Centred, 28px italic.*

- **R-042** `H2` p30: Reflection (her source sets this at 12–13pt; treated as a chapter like her other projects; Q4)
- **R-043** `P` p30: This project strengthened my understanding of designing digital experiences where privacy, security, accessibility, and trust are fundamental to the user experience. Working with sensitive health information reinforced the importance of reducing unnecessary friction while clearly communicating how personal data is accessed and used—principles I continue to apply in my work today.
- **R-044** `P` p30: The project was also particularly meaningful because of the context in which it was developed. Contributing to a digital health experience during the COVID-19 pandemic gave me a deeper appreciation for the role UX design can play in helping communities navigate essential services during periods of uncertainty.

## Room 04 — Littelfuse

Page: `site/room-04-littelfuse.html`

**Chapter index (her H2 headings, her order):** 1 Project Overview · 2 The Challenge · 3 The Approach · 4 Results & Impact · 5 Reflection

### Header (A1 + A4)

- **L-001** `TITLE` p30: Reimagining How Engineers Discover Littelfuse Products
- **L-002** `META` p30: **Role**: UX Consultant | UX Designer |UX Researcher  
  → header meta panel (ROLE)
- **L-003** `META` p30: **Methods**: Stakeholder Workshop | Data Analysis | Information Architecture | Wireframing | Heuristic Evaluation | Archetypes |Competitive Analysis  
  → header meta panel (METHODS)

### Chapter 1: Project Overview
*Layout: A2 / A3 chapter: number + title left, her text right.*

- **L-004** `H2` p30: Project Overview
- **L-005** `P` p30: Littelfuse is a global technology manufacturing company that develops electronic components and solutions used across automotive, industrial, electronics, and other industries.
- **L-006** `P` p31: I worked with Littelfuse to improve its existing digital portal experience, with a focus on creating a more intuitive way for engineers to discover, evaluate, and access products across its extensive portfolio. The project aimed to evolve the portal from an experience largely organized around individual business units into a more customer-centered platform that could better connect users with relevant products and solutions across the broader Littelfuse ecosystem.
- **L-007** `P` p31: From a business perspective, the redesigned experience also created opportunities to increase visibility across product categories and support cross-selling and upselling.

### Chapter 2: The Challenge
*Layout: A3 row; the three How-Might-We bullets as a list.*

- **L-008** `H2` p31: The Challenge
- **L-009** `H3` p31: Simplifying Product Discovery Across a Complex Product Catalog
- **L-010** `P` p31: Littelfuse offers an extensive portfolio of highly technical products across a wide range of industries and applications. However, the existing experience placed a significant cognitive burden on users during product discovery. When engineers did not know the exact stock number for a product, they often had to rely on broader search terms and navigate multiple paths to find what they needed.
- **L-011** `P` p31: Preliminary research provided by Littelfuse showed that 73.2% of users searched using an exact stock number, while others relied on broader product categories such as heaters, panels, sensors, and switches. These broader searches often failed to surface relevant results, requiring users to refine their queries or navigate deeper into the product catalog.
- **L-012** `P` p31: When asked about the ease of search, 48% of survey respondents said that while finding products was generally easy, it still took too much time to reach relevant results. Another 12% reported that the search experience was difficult and that they were often unable to find relevant products.
- **L-013** `P` p31: These findings highlighted an opportunity to reduce users’ reliance on exact product knowledge and create a more intuitive discovery experience—one that could help engineers narrow their options, identify the right product, and complete key tasks with less effort.
- **L-014** `P` p31: How Might We…
- **L-015** `LI` p31: How might we help engineers discover the right product without knowing an exact stock number?
- **L-016** `LI` p31: How might we connect engineers with relevant and complementary products across Littelfuse’s broader portfolio?
- **L-017** `LI` p31: How might we streamline key tasks—from comparing products and accessing technical documentation to ordering, requesting samples, and getting support?

### Chapter 3: The Approach
*Layout: Sub-headings as A3 row labels. The archetype board and journey map as **full plates**. The audit items 01–03 as an **A7 numbered list**. Wireframes placeholder where her note sits.*

- **L-018** `H2` p32: The Approach
- **L-019** `P` p32: I began by reviewing existing customer research, business goals, and the end-to-end product-discovery experience. I translated those inputs into primary user needs, mapped the engineer’s pre-login journey, and audited the interface against the tasks users needed to complete—searching for a component, comparing options, checking stock, downloading technical information, and requesting samples.
- **L-020** `P` p32: The analysis exposed gaps in navigation, terminology, content pathways, and task continuity. These findings became the foundation for a simpler information architecture and more direct product-discovery flows.
- **L-021** `H4` p32: Synthesized existing research and business priorities
- **L-022** `P` p32: In reviewing existing research I learned that the Little Fuse customers relied on the platform to complete one of these tasks: find and compare products, access technical documentation, check availability, request samples, and get support. Knowing that these were the common user flows and navigation paths I then began to understand who the primary Little Fuse Customer is.
- **L-023** `H4` p32: Defined the primary user: a design engineer
- **L-024** `P` p32: Through stakeholder interviews, existing user research, and analysis of customer roles and behaviors, we grouped Littelfuse users into three primary archetypes: Engineering & Technical, Sales, and Procurement. These archetypes reflect the different ways users influence product selection—from engineers evaluating specifications and making design recommendations, to sales partners supporting customers, and procurement professionals managing purchasing and supply. In combination with quantitative survey data with customer interviews, stakeholder research we identify recurring behaviors, pain points and decision drivers that inform the experience strategy. The survey data found that 66% of respondents identified as being in an engineering role, compared with 12% Sales and 5% Procurement.This insight helped us prioritize the experience around engineers’ core tasks—finding the right product quickly, comparing options, accessing technical documentation, and confidently making component decisions—while still supporting the needs of Sales and Procurement users. The analysis of the survey data is what guided our work in completing detailed personas rather than working of static archetypes.
- **L-025** `FIG` `doc-22` (p33): 'Designing for the people who drive component decisions' stat board. Only copy (975px). Plate.
- **L-026** `FIG` `doc-23` (p33): user archetypes board. Full-res: `r04_doc_user-archetypes.png`. Full plate.
- **L-027** `H4` p33: Mapped the product-discovery journey
- **L-028** `P` p33: The user journey was developed during a collaborative workshop at the client’s headquarters, bringing together key stakeholders to map how engineers move from identifying a product need to researching, comparing, testing, and selecting a solution. By documenting both the high-level journey and detailed decision points, we identified key behaviors, information needs, and opportunities to streamline the digital product experience.
- **L-029** `FIG` `doc-24` (p34): journey map. Full-res: `r04_doc_journey-map.png`. Full plate.
- **L-030** `H4` p34: Audited critical tasks and interface pathways
- **L-031** `P` p34: Following the journey-mapping workshop, I evaluated the existing Littelfuse website against the needs and behaviors identified in the user journey. The review focused on key paths engineers rely on to discover and evaluate products, revealing gaps in navigation, task flows, content structure, and interaction design.
- **L-032** `H4` p34: 01 — Navigation & Findability
- **L-033** `P` p34: Critical product actions—including Cross Reference, Check Stock, Where to Buy, and Request Samples—were inconsistently represented across the experience. We also identified unclear labeling and opportunities to make global search and language selection more intuitive.
- **L-034** `H4` p34: 02 — Incomplete Task Flows
- **L-035** `P` p34: Mapping core tasks exposed several points where the existing experience did not fully support the user's journey. The Check Stock flow, for example, contained missing screens and unclear paths for users who didn't already know a product or part number.
- **L-036** `H4` p34: 03 — Interaction & Content Gaps
- **L-037** `P` p34: The audit uncovered smaller usability issues that compounded friction, including inconsistent labels, unclear interface states, missing landing-page templates, misaligned interface elements, and controls without clearly defined behaviors.
- **L-038** `H4` p35: Translated findings into design principles
- **L-039** `P` p35: Insights from the audit were translated into design principles focused on clarity, consistency, accessibility, and task completion. Existing wireframes were refined to create a more cohesive experience across desktop and mobile, including clearer navigation and labeling, improved menu hierarchy, accessible interaction states, standardized components, and more intuitive search and filtering patterns. These principles were applied consistently across the global header, mega menu, homepage, product pages, and supporting content modules.
- **L-040** `P` p35: The work also addressed gaps where the existing wireframes did not fully support critical user tasks. New and expanded flows were designed for global search, product discovery, Check Stock, Where to Buy, and privacy/GDPR interactions, while missing states, error handling, filters, links, and responsive behaviors were defined to make the experience development-ready. Below are the completed wire frames.
- **L-041** `NOTE` p35: "INSERT WIREFRAMES FROM PDF HERE"  
  → **Missing.** Only Adobe XD links exist (`Littelfuse_Wireframes_XD-links.docx`). A labelled placeholder until exports arrive (ASSET-GAPS B1). See Q8.

### Chapter 4: Results & Impact
*Layout: **A7** layout.*

- **L-042** `H2` p35: Results & Impact (her source sets this at 12–13pt; treated as a chapter like her other projects; Q4)
- **L-043** `P` p35: The redesigned experience streamlined product discovery and evaluation across desktop and mobile, creating clearer pathways through search, navigation, and key purchasing tasks. Following launch, mobile logins increased by 6%, indicating stronger engagement with the improved mobile experience.

### Chapter 5: Reflection
*Layout: Centred, 28px italic.*

- **L-044** `H2` p35: Reflection (her source sets this at 12–13pt; treated as a chapter like her other projects; Q4)
- **L-045** `P` p35: This project introduced me to a highly specialized industry with a unique set of users and technical workflows. To design effectively, I invested additional time in secondary research—studying the competitive landscape, learning industry fundamentals, and understanding how products move from the warehouse into an online product database. That deeper investigation surfaced questions we hadn’t initially considered and ultimately led to additional discovery sessions with stakeholders. In hindsight, that extra effort became a strength of the project: stakeholders appreciated the attention to detail, and it reinforced for me that good UX sometimes means slowing down to fully understand a complex ecosystem before designing for it.

## Words on the pages that are not in her documents

Rule 3 says no additions. These come from the Round 3 brief itself or are site navigation, and are listed so COPY-CHECK can separate them from her copy.

| Where | Text | Source |
|---|---|---|
| Top bar | Yasmin Bajwa · Projects · About · Contact | Brief (navigation) |
| Hero | Hi, I'm *Yasmin.* | Brief (her doc says "Hi! I'm Yasmin,"; this is the greeting the brief asks for) |
| Hero | View Projects → | Brief |
| Hero caption | DIGITAL EXHIBIT DESIGNER — THE HENRY FORD | Brief (her words, re-cased) |
| Hero facts | ROLE / BASED IN / FOCUS / CURRENTLY + values | Brief. **Values not in her copy** (Q9) |
| Photo strip | tiny caption above each photo | Brief (A8). Caption text needs approval (Q10) |
| Projects | Projects · Password protected · her project titles · her Role lines | Brief + her copy |
| Contact | Let's make something *people remember.* | Brief. Her line is "create something people will remember" (Q3) |
| Contact | email · LinkedIn · résumé | Pending her details |
| Every case study | Chapter numbers, 'FIG. n — caption', ROLE / METHODS labels, '← Previous project · Next project → · All projects' | Brief. Captions need approval (Q10) |
| Case study meta | SETTING / YEAR | Brief. **Not in her copy** (Q9) |
| Lock screen | Projects are shared *by invitation.* · Enter the password to continue. · No password? Email Yasmin → | Brief |

**Dropped as the brief instructs:** §5 "About by numbers". Her copy has no numbers about herself: '4 projects' and '3 institutions' are counts I'd be making up, and the brief says drop the section if fewer than three real numbers exist.

## Questions before building

- **Q1.** The four **'Portfolio Website Direction'** paragraphs (A-01…A-04) and **'Highlight these 4 skills in this order::'** (A-08) are instructions to the designer ("The developer can recommend the best structure", "Please also include password protection"). I plan to follow them, **not print them** on the site. Confirm.
- **Q2.** **'UX ( User Experience) Design'**: verbatim has a space inside the bracket. Print exactly, or may it read **'UX (User Experience) Design'**?
- **Q3.** **Contact headline:** the brief's "Let's make something people remember." isn't a sentence in her docs (hers: "…create something people will remember."). Use the brief's line, or her sentence verbatim?
- **Q4.** **Heading levels:** in Rhode Island and Littelfuse she set Results & Impact / Ongoing Evaluation / Reflection at 12–13pt, and in Power & Energy 'Ongoing Evaluation' at 12pt, while the same headings are chapters elsewhere. I'm treating them all as chapters so the chapter index is consistent. Words unchanged.
- **Q5.** **Jackson Home visitor-type table** (J-table): the A4 stats strip shows 60% · 10% · 30% with her characteristic text beneath. It keeps her row order (Strollers, Studiers, Streakers) and her column headings as small labels. OK?
- **Q6.** **Additions of images** the brief asks for that her doc doesn't place: the **Power & Energy column-art panels** (A6 board beside 'The experience included:') and optionally the **Littelfuse personas video** (after 'Defined the primary user'). Both are her files; no words added. Confirm placement.
- **Q7.** **Rhode Island screens:** her figure `doc-21` has phone frames drawn round the screens, and the brief says no device mockups. Keep her figure as is (it's her own board), and show the 'two mobile screens side by side' from the frameless vector PDF next to the wireframes video?
- **Q8.** **Littelfuse 'INSERT WIREFRAMES FROM PDF HERE':** there is no Littelfuse wireframes PDF or video in the repo. The only video is the personas one. It stays a labelled placeholder until she exports screens from the XD links.
- **Q9.** **Values I don't have:** homepage facts (BASED IN, FOCUS, CURRENTLY) and case-study SETTING / YEAR. I'll show only ROLE and METHODS in the case-study header (her words) and leave the others as marked placeholders, unless you supply them.
- **Q10.** **Figure captions** are required by the brief but aren't her words. I'll write short, factual ones (e.g. "FIG. 05 — House plan with expected visitor paths") and list them in COPY-CHECK as captions, separate from her copy.
- **Q11.** **Likely slips in her text, kept verbatim unless she approves a fix:** "Annex (complimentary building…)" (complementary?) · "ITC( International" · "lo- fi" · "feedback( See below)" · "Little Fuse" ×2 beside "Littelfuse" · "Procurement.This" (missing space) · "rather than working of static archetypes" · "In combination with … we identify" · "particularly those centered on difficult history" (no full stop) · "App Space" beside "Appspace" · "wire frames" beside "wireframes" · "The final wireframes shown below." · "Pre 1965" · "deciding factor for where to place digital interactives" (bullet grammar) · spacing in "UX Designer| Experience Design", "|UX Researcher", "The Approach/ UX Design".
- **Q12.** **Duplicated line:** "Below are the CMS channels within App Space." ends both the CMS chapter (P-045) and an Installation & Fabrication paragraph (P-050), where no CMS image follows. Verbatim means it appears twice. Keep both, or drop the second?
- **Q13.** **Duplicated heading:** "Ticketing Window & Arrival Patterns" appears twice in Scenario Testing (J-089, J-097), once for random arrivals and once for arrivals at the start of the window. Kept twice, as in her doc.

