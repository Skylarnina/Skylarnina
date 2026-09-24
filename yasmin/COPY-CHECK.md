# Copy check

Each rendered page is compared, item by item, with `content/copy.json`, the verbatim extraction of her two documents (see COPY-INVENTORY.md). An item passes (✔) only if it is:

- on its page **exactly once**, with a `data-id` matching its inventory ID;
- **word-for-word identical as rendered**, so CSS upper-casing or a changed character fails;
- **visible** at both 1440px and 390px;
- **in her order**, after the previous item.

The comparison is automatic (`tools/dom_text.js` then `tools/copy_check.py`). Re-run it after any edit. The tables show the start of each text; the check compares the full text.

**Result: 293 / 293 items ✔ (100%).** Every heading, paragraph, bullet, table row, quote, figure and production note is accounted for.

## Homepage: About (`Instructions_About_Me.docx`)

| ID | Text | Where | 1440 | 390 |
|---|---|---|---|---|
| A-01 | Portfolio Website Direction | Not printed (brief / instruction, confirmed Q1) | — | — |
| A-02 | I want my portfolio to position me at the intersection of UX Design, U… | Not printed (brief / instruction, confirmed Q1) | — | — |
| A-03 | The landing page should feature a strong photo of me, a short introduc… | Not printed (brief / instruction, confirmed Q1) | — | — |
| A-04 | For the visual direction, I’d like the site to feel editorial, minimal… | Not printed (brief / instruction, confirmed Q1) | — | — |
| A-05 | About Me | Hero, label above her first paragraph | ✔ | ✔ |
| A-06 | Hi! I’m Yasmin, a Digital Exhibit Designer at The Henry Ford Museum wi… | Hero, under the greeting | ✔ | ✔ |
| A-07 | By blending design, research, and exhibit development, I bring a fresh… | Statement (A9), centred | ✔ | ✔ |
| A-08 | Highlight these 4 skills in this order:: | Not printed (brief / instruction, confirmed Q1) | — | — |
| A-09 | Interactive Exhibit Design | Four disciplines, panel 01 | ✔ | ✔ |
| A-10 | UX ( User Experience) Design | Four disciplines, panel 02 | ✔ | ✔ |
| A-11 | UX Research | Four disciplines, panel 03 | ✔ | ✔ |
| A-12 | Digital Marketing | Four disciplines, panel 04 | ✔ | ✔ |

**Project titles and Role lines repeated on the homepage rows and the Projects page:** ✔ all identical to her text.

## The Henry Ford Jackson Home — `site/room-01-jackson-home.html`

| ID | Type | Text (start) | Section | 1440 | 390 |
|---|---|---|---|---|---|
| J-001 | TITLE | The Henry Ford Jackson Home Visitor Flow Simulation | Header | ✔ | ✔ |
| J-002 | META | Role: UX Researcher / Experience Design | Header | ✔ | ✔ |
| J-003 | META | Methods: Behavioral Observation • Space Syntax Analysis • Behavioral P… | Header | ✔ | ✔ |
| J-004 | H2 | Project Overview | Project Overview | ✔ | ✔ |
| J-005 | P | The Dr. Sullivan and Mrs. Richie Jean Sherrod Jackson Home is a nation… | Project Overview | ✔ | ✔ |
| J-006 | P | As the first building added to Greenfield Village in more than forty y… | Project Overview | ✔ | ✔ |
| J-007 | P | Using UX research methodologies and behavioral modeling, I created a v… | Project Overview | ✔ | ✔ |
| J-008 | H2 | The Challenge | The Challenge | ✔ | ✔ |
| J-009 | P | No behavioral data existed, planning visitor capacity relied on assump… | The Challenge | ✔ | ✔ |
| J-010 | LI | Narrow circulation paths | The Challenge | ✔ | ✔ |
| J-011 | LI | Limited room capacity | The Challenge | ✔ | ✔ |
| J-012 | LI | Sequential visitor movement | The Challenge | ✔ | ✔ |
| J-013 | LI | Preservation requirements that prevented structural modifications | The Challenge | ✔ | ✔ |
| J-014 | P | The challenge became: | The Challenge | ✔ | ✔ |
| J-015 | HMW | How might we predict visitor behavior and optimize the museum experien… | The Challenge | ✔ | ✔ |
| J-016 | H2 | Research Questions | Research Questions | ✔ | ✔ |
| J-017 | P | To support exhibition planning, I focused on answering several key res… | Research Questions | ✔ | ✔ |
| J-018 | H3 | Visitor Experience | Research Questions | ✔ | ✔ |
| J-019 | LI | How long will visitors spend inside the home? | Research Questions | ✔ | ✔ |
| J-020 | LI | Where are visitors most likely to stop or experience congestion? | Research Questions | ✔ | ✔ |
| J-021 | LI | What will waiting times look like throughout the experience? | Research Questions | ✔ | ✔ |
| J-022 | H3 | Capacity Planning | Research Questions | ✔ | ✔ |
| J-023 | LI | How many visitors can comfortably occupy both the Jackson Home and Ann… | Research Questions | ✔ | ✔ |
| J-024 | LI | Should visitors enter through 15-minute or 30-minute ticketing windows… | Research Questions | ✔ | ✔ |
| J-025 | LI | Can walk-up visitors be accommodated without negatively affecting the … | Research Questions | ✔ | ✔ |
| J-026 | H3 | Operations | Research Questions | ✔ | ✔ |
| J-027 | LI | Where should docents and presenters be positioned to support visitor f… | Research Questions | ✔ | ✔ |
| J-028 | LI | What traffic management strategies should staff use during peak attend… | Research Questions | ✔ | ✔ |
| J-029 | H2 | Research Methodology | Research Methodology | ✔ | ✔ |
| J-030 | P | Because no baseline visitor data existed for the Jackson Home, I combi… | Research Methodology | ✔ | ✔ |
| J-031 | H3 | Behavioral Observation | Research Methodology | ✔ | ✔ |
| J-032 | P | I analyzed visitor movement within comparable historical homes and nea… | Research Methodology | ✔ | ✔ |
| J-033 | LI | visitor arrival behavior | Research Methodology | ✔ | ✔ |
| J-034 | LI | walking speed | Research Methodology | ✔ | ✔ |
| J-035 | LI | dwell time | Research Methodology | ✔ | ✔ |
| J-036 | LI | congestion points | Research Methodology | ✔ | ✔ |
| J-037 | LI | exhibit engagement | Research Methodology | ✔ | ✔ |
| J-038 | LI | decision-making at transitions between rooms | Research Methodology | ✔ | ✔ |
| J-039 | P | These findings established the behavioral assumptions used throughout … | Research Methodology | ✔ | ✔ |
| J-040 | H3 | Space Syntax Analysis | Research Methodology | ✔ | ✔ |
| J-041 | P | In collaboration with our experience design team I evaluated the home'… | Research Methodology | ✔ | ✔ |
| J-042 | H3 | Behavioral Path Clustering | Research Methodology | ✔ | ✔ |
| J-043 | P | Behavioral observations revealed that visitors interact with museum en… | Research Methodology | ✔ | ✔ |
| J-044 | TABLE | Visitor Type / Characteristics / Distribution | Research Methodology | ✔ | ✔ |
| J-045 | P | Each simulated visitor was randomly assigned one of these behavioral p… | Research Methodology | ✔ | ✔ |
| J-046 | FIG | doc-01: Time spent on-site by visitor type | Research Methodology | ✔ shown | ✔ |
| J-047 | FIG | doc-02: Congestion, queue sizes, visit time and delays | Research Methodology | ✔ shown | ✔ |
| J-048 | H2 | Building the Simulation | Building the Simulation | ✔ | ✔ |
| J-049 | P | Using behavioral research, I developed a discrete event simulation tha… | Building the Simulation | ✔ | ✔ |
| J-050 | LI | timed ticket arrivals | Building the Simulation | ✔ | ✔ |
| J-051 | LI | room occupancy limits | Building the Simulation | ✔ | ✔ |
| J-052 | LI | queue formation | Building the Simulation | ✔ | ✔ |
| J-053 | LI | walking speed | Building the Simulation | ✔ | ✔ |
| J-054 | LI | exhibit dwell time | Building the Simulation | ✔ | ✔ |
| J-055 | LI | presenter intervention | Building the Simulation | ✔ | ✔ |
| J-056 | LI | alternative routing when spaces reached capacity | Building the Simulation | ✔ | ✔ |
| J-057 | P | Rather than moving visitors as a group, every individual made independ… | Building the Simulation | ✔ | ✔ |
| J-058 | FIG | doc-03: Jackson Home floor plan | Building the Simulation | ✔ shown | ✔ |
| J-059 | FIG | doc-04: The Annex floor plan, with site entrance, entrance line and vestibule | Building the Simulation | ✔ shown | ✔ |
| J-060 | FIG | doc-05: Jackson Home floor plan with expected visitor paths | Building the Simulation | ✔ shown | ✔ |
| J-061 | NOTE | INSERT VIDEO HERE - DISCRETE EVENT SIMULATION | Building the Simulation | ✔ → Discrete event simulation of visitor flow (video) | ✔ |
| J-062 | H2 | Baseline Assumptions | Baseline Assumptions | ✔ | ✔ |
| J-063 | P | Since the exhibition had not yet opened, several assumptions were esta… | Baseline Assumptions | ✔ | ✔ |
| J-064 | P | These included: | Baseline Assumptions | ✔ | ✔ |
| J-065 | LI | Visitors arrive within their assigned ticket window. | Baseline Assumptions | ✔ | ✔ |
| J-066 | LI | Ticket windows operate in either 15-minute or 30-minute intervals. | Baseline Assumptions | ✔ | ✔ |
| J-067 | LI | Visitors travel independently while naturally clustering into small so… | Baseline Assumptions | ✔ | ✔ |
| J-068 | LI | Average walking speed is approximately 2.0 mph, representing most muse… | Baseline Assumptions | ✔ | ✔ |
| J-069 | LI | Each exhibit has a maximum occupancy determined by available floor spa… | Baseline Assumptions | ✔ | ✔ |
| J-070 | LI | When capacity is reached, visitors either wait or continue to another … | Baseline Assumptions | ✔ | ✔ |
| J-071 | LI | Individual viewing times vary according to visitor type and natural be… | Baseline Assumptions | ✔ | ✔ |
| J-072 | H2 | Scenario Testing | Scenario Testing | ✔ | ✔ |
| J-073 | H4 | STUDY FACTORS | Scenario Testing | ✔ | ✔ |
| J-074 | LI | Ticketing Window: | Scenario Testing | ✔ | ✔ |
| J-075 | LI | 30-minute windows | Scenario Testing | ✔ | ✔ |
| J-076 | LI | 15-minute windows | Scenario Testing | ✔ | ✔ |
| J-077 | LI | Arrival Pattern: | Scenario Testing | ✔ | ✔ |
| J-078 | LI | Random times within ticketing window | Scenario Testing | ✔ | ✔ |
| J-079 | LI | All arrive at start of ticketing window | Scenario Testing | ✔ | ✔ |
| J-080 | LI | Docent Control: | Scenario Testing | ✔ | ✔ |
| J-081 | LI | No constraint – visitors enter if there is space in the vestibule | Scenario Testing | ✔ | ✔ |
| J-082 | LI | With constraint – docent allows ~8 people at a time into entrance area… | Scenario Testing | ✔ | ✔ |
| J-083 | LI | Number of tickets: | Scenario Testing | ✔ | ✔ |
| J-084 | LI | Base: 48 per 30-minutes or 24 per 15-minutes | Scenario Testing | ✔ | ✔ |
| J-085 | LI | Low: 38 per 30-minutes or 20 per 15-minutes | Scenario Testing | ✔ | ✔ |
| J-086 | LI | High: 58 per 30-minutes or 28 per 15-minutes | Scenario Testing | ✔ | ✔ |
| J-087 | LI | Walk-up Visitors: | Scenario Testing | ✔ | ✔ |
| J-088 | LI | A limited number of un-ticketed visitors may be allowed to join the qu… | Scenario Testing | ✔ | ✔ |
| J-089 | H4 | Ticketing Window & Arrival Patterns | Scenario Testing | ✔ | ✔ |
| J-090 | LI | The effects of these factors are linked | Scenario Testing | ✔ | ✔ |
| J-091 | LI | If visitor arrivals are spread randomly through the ticketing window | Scenario Testing | ✔ | ✔ |
| J-092 | LI | Congestion and queue sizes are low | Scenario Testing | ✔ | ✔ |
| J-093 | LI | Visitors rarely have to skip exhibits | Scenario Testing | ✔ | ✔ |
| J-094 | LI | Total time spent on-site matches expectations | Scenario Testing | ✔ | ✔ |
| J-095 | LI | There is no significant difference between 30-minute or 15-minute tick… | Scenario Testing | ✔ | ✔ |
| J-096 | FIG | doc-06: Arrivals spread randomly through the ticketing window | Scenario Testing | ✔ shown | ✔ |
| J-097 | H4 | Ticketing Window & Arrival Patterns | Scenario Testing | ✔ | ✔ |
| J-098 | LI | If most visitors arrive close to the start of the ticketing window | Scenario Testing | ✔ | ✔ |
| J-099 | LI | Congestion and queue sizes are high | Scenario Testing | ✔ | ✔ |
| J-100 | LI | With no docent control at the entrance, skipping behavior balloons | Scenario Testing | ✔ | ✔ |
| J-101 | LI | This could result in many unhappy visitors! | Scenario Testing | ✔ | ✔ |
| J-102 | LI | Average time spent on-site increases by just a few minutes, but the ma… | Scenario Testing | ✔ | ✔ |
| J-103 | LI | In this case, all indicators are much better if 15-minute ticketing wi… | Scenario Testing | ✔ | ✔ |
| J-104 | FIG | doc-07: Arrivals at the start of the ticketing window | Scenario Testing | ✔ shown | ✔ |
| J-105 | FIG | doc-08: Expected visit times by visitor type | Scenario Testing | ✔ shown | ✔ |
| J-106 | H2 | Findings | Findings | ✔ | ✔ |
| J-107 | H3 | Ticketing Strategy | Findings | ✔ | ✔ |
| J-108 | P | Visitors were expected to arrive near the beginning of their assigned … | Findings | ✔ | ✔ |
| J-109 | P | A 15-minute ticketing schedule distributed arrivals more evenly than 3… | Findings | ✔ | ✔ |
| J-110 | H3 | Capacity | Findings | ✔ | ✔ |
| J-111 | P | While the home could accommodate a maximum of approximately 32 visitor… | Findings | ✔ | ✔ |
| J-112 | H3 | Presenter Placement | Findings | ✔ | ✔ |
| J-113 | P | Simulation results demonstrated that placing presenters near the first… | Findings | ✔ | ✔ |
| J-114 | P | Presenters helped regulate entry into high-demand spaces, reduced skip… | Findings | ✔ | ✔ |
| J-115 | H3 | Walk-Up Visitors | Findings | ✔ | ✔ |
| J-116 | P | Allowing a controlled mix of ticketed and walk-up visitors naturally s… | Findings | ✔ | ✔ |
| J-117 | FIG | doc-09: Skipped exhibits, without and with docent control | Findings | ✔ shown | ✔ |
| J-118 | FIG | doc-10: Best scenario: 20 tickets, 8 walk-ups, with docent control | Findings | ✔ shown | ✔ |
| J-119 | H2 | Impact | Impact | ✔ | ✔ |
| J-120 | P | The visitor flow simulation provided stakeholders with evidence-based … | Impact | ✔ | ✔ |
| J-121 | LI | establish ticketing schedules for opening operations | Impact | ✔ | ✔ |
| J-122 | LI | determine comfortable visitor capacity limits | Impact | ✔ | ✔ |
| J-123 | LI | identify high-congestion areas before opening | Impact | ✔ | ✔ |
| J-124 | LI | optimize presenter placement throughout the home | Impact | ✔ | ✔ |
| J-125 | LI | evaluate queue management strategies | Impact | ✔ | ✔ |
| J-126 | LI | deciding factor for where to place digital interactives in the exhibit | Impact | ✔ | ✔ |
| J-127 | LI | improve visitor flow while preserving the historic integrity of the bu… | Impact | ✔ | ✔ |
| J-128 | P | Rather than relying on assumptions alone, leadership was able to make … | Impact | ✔ | ✔ |
| J-129 | H2 | Reflection | Reflection | ✔ | ✔ |
| J-130 | P | This project broadened my understanding of user experience beyond digi… | Reflection | ✔ | ✔ |

Order check: ✔ every item appears after the one before it.

## Power & Energy — `site/room-02-power-energy.html`

| ID | Type | Text (start) | Section | 1440 | 390 |
|---|---|---|---|---|---|
| P-001 | TITLE | Designing an Interactive Museum Experience for Power & Energy | Header | ✔ | ✔ |
| P-002 | META | Role: UX Designer/ Experience Design / Project Management | Header | ✔ | ✔ |
| P-003 | META | Methods: Information Architecture • User Flows • Wireframing • Content… | Header | ✔ | ✔ |
| P-004 | H2 | Project Overview | Project Overview | ✔ | ✔ |
| P-005 | P | The goal of this project was to enhance The Henry Ford Museum’s Power … | Project Overview | ✔ | ✔ |
| P-006 | P | The column was designed for student groups, families, and general muse… | Project Overview | ✔ | ✔ |
| P-007 | P | The experience also incorporates content from project partner ITC( Int… | Project Overview | ✔ | ✔ |
| P-008 | H2 | The Challenge | The Challenge | ✔ | ✔ |
| P-009 | H3 | Capturing Visitor Attention | The Challenge | ✔ | ✔ |
| P-010 | P | In an exhibit filled with large-scale artifacts and live programming, … | The Challenge | ✔ | ✔ |
| P-011 | HMW | How might we create an intuitive digital experience that encourages vi… | The Challenge | ✔ | ✔ |
| P-012 | H3 | Balancing Museum and Sponsor Goals | The Challenge | ✔ | ✔ |
| P-013 | P | The experience needed to support The Henry Ford’s educational mission … | The Challenge | ✔ | ✔ |
| P-014 | HMW | How might we introduce students to careers in power and energy while b… | The Challenge | ✔ | ✔ |
| P-015 | H2 | The Approach/ UX Design | The Approach/ UX Design | ✔ | ✔ |
| P-016 | P | To address visitor, educational, wayfinding, and sponsor needs, I deve… | The Approach/ UX Design | ✔ | ✔ |
| P-017 | P | The experience included: | The Approach/ UX Design | ✔ | ✔ |
| P-018 | LI | Exhibit wayfinding: A backlit graphic identifying the Power & Energy e… | The Approach/ UX Design | ✔ | ✔ |
| P-019 | LI | Innovation stories: Condensed Innovation Nation episodes highlighting … | The Approach/ UX Design | ✔ | ✔ |
| P-020 | LI | Interactive exploration: A touch-based map visualizing power transmiss… | The Approach/ UX Design | ✔ | ✔ |
| P-021 | LI | Career discovery: ITC employee interviews introducing students to care… | The Approach/ UX Design | ✔ | ✔ |
| P-022 | LI | Artifact interpretation: A backlit graphic highlighting key artifacts … | The Approach/ UX Design | ✔ | ✔ |
| P-023 | P | I began to take the existing column we have in the Agriculture column … | The Approach/ UX Design | ✔ | ✔ |
| P-024 | FIG | doc-11: Content themes and experience flow for the column | The Approach/ UX Design | ✔ shown | ✔ |
| P-025 | FIG | doc-12: Lo-fi sketches and wireframes for the column | The Approach/ UX Design | ✔ shown | ✔ |
| P-026 | H2 | Discovery & Stakeholder Alignment | Discovery & Stakeholder Alignment | ✔ | ✔ |
| P-027 | P | Once the content strategy for each side of the column was established,… | Discovery & Stakeholder Alignment | ✔ | ✔ |
| P-028 | P | For the ITC career experience, the goal was to introduce visitors to t… | Discovery & Stakeholder Alignment | ✔ | ✔ |
| P-029 | FIG | doc-13: ITC employee research: three roles | Discovery & Stakeholder Alignment | ✔ shown | ✔ |
| P-030 | P | In addition to the employee stories, I explored how the experience cou… | Discovery & Stakeholder Alignment | ✔ | ✔ |
| P-031 | P | Excerpts from the UX copy below: | Discovery & Stakeholder Alignment | ✔ | ✔ |
| P-032 | QUOTE | “Engineering Together: Thomas Edison employed dozens of engineers, inv… | Discovery & Stakeholder Alignment | ✔ | ✔ |
| P-033 | QUOTE | “Safety & Security: As electric companies built new infrastructure aro… | Discovery & Stakeholder Alignment | ✔ | ✔ |
| P-034 | QUOTE | “Community Planning: Thomas Edison tested and gathered feedback on his… | Discovery & Stakeholder Alignment | ✔ | ✔ |
| P-035 | H2 | Designing the Interactive Experience | Designing the Interactive Experience | ✔ | ✔ |
| P-036 | P | I then began finalizing the experience, focusing on the interaction to… | Designing the Interactive Experience | ✔ | ✔ |
| P-037 | P | I began by evaluating the Agriculture column’s existing user flow, inc… | Designing the Interactive Experience | ✔ | ✔ |
| P-038 | P | These behavioral insights became an important input into the final des… | Designing the Interactive Experience | ✔ | ✔ |
| P-039 | P | The resulting flow and content distribution are illustrated in the dia… | Designing the Interactive Experience | ✔ | ✔ |
| P-040 | FIG | doc-14: Content distribution across the sides of the column | Designing the Interactive Experience | ✔ shown | ✔ |
| P-041 | NOTE | INSERT VIDEO HERE BELOW IS SCREEN GRAB OF WHAT IT LOOKS LIKE | Designing the Interactive Experience | ✔ → Final interface and user flow (video) | ✔ |
| P-042 | FIG | doc-15: — | Designing the Interactive Experience | ✔ replaced by the video her note asks for | ✔ |
| P-043 | H2 | CMS Integration & Implementation | CMS Integration & Implementation | ✔ | ✔ |
| P-044 | P | The museum uses multiple content management systems to publish and mai… | CMS Integration & Implementation | ✔ | ✔ |
| P-045 | P | I collaborated closely with the Appspace team to ensure all final asse… | CMS Integration & Implementation | ✔ | ✔ |
| P-046 | NOTE | INSERT POWER & ENERGY VIDEO HERE | CMS Integration & Implementation | ✔ → CMS channels in Appspace (video) | ✔ |
| P-047 | H2 | Installation & Fabrication | Installation & Fabrication | ✔ | ✔ |
| P-048 | P | For the final installation, we partnered with Sleet Custom Cabinets, a… | Installation & Fabrication | ✔ | ✔ |
| P-049 | P | I worked closely with the fabricator to provide precise dimensions, sp… | Installation & Fabrication | ✔ | ✔ |
| P-050 | P | My role during this phase was to coordinate and manage the various tea… *(duplicate sentence removed, Q12)* | Installation & Fabrication | ✔ | ✔ |
| P-051 | NOTE | USE PDF VERSION HERE OF DRAWINGS | Installation & Fabrication | ✔ → Shop drawing, column surround: plan, section and perspective | ✔ |
| P-052 | FIG | doc-16: — | Installation & Fabrication | ✔ replaced by the vector PDF her note asks for | ✔ |
| P-053 | FIG | doc-17: — | Installation & Fabrication | ✔ replaced by the vector PDF her note asks for | ✔ |
| P-054 | FIG | doc-18: — | Installation & Fabrication | ✔ replaced by the vector PDF her note asks for | ✔ |
| P-055 | NOTE | ADD COLUMN FABRICATION VIDEO HERE - https://drive.google.com… | Installation & Fabrication | ✔ → Column fabrication progression (video) | ✔ |
| P-056 | H2 | Results & Impact | Results & Impact | ✔ | ✔ |
| P-057 | P | The Power & Energy interactive column transformed the exhibit entrance… | Results & Impact | ✔ | ✔ |
| P-058 | P | The final experience supported multiple visitor needs through artifact… | Results & Impact | ✔ | ✔ |
| P-059 | P | For project sponsor ITC, the experience provided a meaningful way to c… | Results & Impact | ✔ | ✔ |
| P-060 | NOTE | ADD Final Results video here - https://drive.google.com/file… | Results & Impact | ✔ → Final setup: the installed column (video) | ✔ |
| P-061 | H2 | Ongoing Evaluation | Ongoing Evaluation | ✔ | ✔ |
| P-062 | P | Because the experience was recently launched, long-term visitor impact… | Ongoing Evaluation | ✔ | ✔ |
| P-063 | P | Planned UX research includes museum volunteer focus groups, testing wi… | Ongoing Evaluation | ✔ | ✔ |
| P-064 | H2 | Reflection | Reflection | ✔ | ✔ |
| P-065 | P | This project expanded my understanding of UX design beyond traditional… | Reflection | ✔ | ✔ |
| P-066 | P | Working across touch displays, backlit graphics, static interpretation… | Reflection | ✔ | ✔ |
| P-067 | P | Most importantly, the project reinforced that UX does not stop at the … | Reflection | ✔ | ✔ |

Order check: ✔ every item appears after the one before it.
Removed duplicate: "Below are the CMS channels within App Space." appears **1×** on the page (expected 1, in P-045). ✔

## Rhode Island 401 Health App — `site/room-03-rhode-island.html`

| ID | Type | Text (start) | Section | 1440 | 390 |
|---|---|---|---|---|---|
| R-001 | TITLE | Rhode Island State COVID Vaccine App/401 Health App | Header | ✔ | ✔ |
| R-002 | META | Role: UX Designer/ UX Researcher / UX Consultant | Header | ✔ | ✔ |
| R-003 | META | Methods: Qualitative Research • Quantitative Analysis • Feedback Synth… | Header | ✔ | ✔ |
| R-004 | H2 | Project Overview | Project Overview | ✔ | ✔ |
| R-005 | P | The goal of this project was to improve the State of Rhode Island’s va… | Project Overview | ✔ | ✔ |
| R-006 | H2 | The Challenge | The Challenge | ✔ | ✔ |
| R-007 | H4 | Building Trust and Increasing Adoption of Digital Vaccination Records | The Challenge | ✔ | ✔ |
| R-008 | P | Research and stakeholder feedback revealed a key barrier to adoption: … | The Challenge | ✔ | ✔ |
| R-009 | P | The challenge was to create a sign-up and onboarding experience that r… | The Challenge | ✔ | ✔ |
| R-010 | H4 | How might we... | The Challenge | ✔ | ✔ |
| R-011 | LI | Create a seamless sign-up and onboarding experience that encourages re… | The Challenge | ✔ | ✔ |
| R-012 | LI | Build trust by clearly communicating privacy, security, and how person… | The Challenge | ✔ | ✔ |
| R-013 | LI | Demonstrate the value of digital vaccination records for events, trave… | The Challenge | ✔ | ✔ |
| R-014 | H4 | Reducing Friction Through Health Record Integration | The Challenge | ✔ | ✔ |
| R-015 | P | A second challenge was eliminating the need for residents to manually … | The Challenge | ✔ | ✔ |
| R-016 | P | The challenge was to design a secure, intuitive way for users to autho… | The Challenge | ✔ | ✔ |
| R-017 | H4 | How might we... | The Challenge | ✔ | ✔ |
| R-018 | LI | Make it simple for residents to securely authorize access to their exi… | The Challenge | ✔ | ✔ |
| R-019 | LI | Clearly communicate where vaccination data comes from and how it is be… | The Challenge | ✔ | ✔ |
| R-020 | LI | Reduce unnecessary manual entry while maintaining confidence in the ac… | The Challenge | ✔ | ✔ |
| R-021 | H2 | The Approach/ Discovery & Stakeholder Alignment | The Approach/ Discovery & Stakeholder Alignment | ✔ | ✔ |
| R-022 | P | To better understand the existing application experience, Rhode Island… | The Approach/ Discovery & Stakeholder Alignment | ✔ | ✔ |
| R-023 | P | These insights helped us identify usability opportunities, prioritize … | The Approach/ Discovery & Stakeholder Alignment | ✔ | ✔ |
| R-024 | FIG | doc-19: Rhode Island Department of Health population health goals | The Approach/ Discovery & Stakeholder Alignment | ✔ shown | ✔ |
| R-025 | NOTE | INSERT VIDEO OF APP STORE REVIEWS HERE ( PICTURE IS ONLY FOR… | The Approach/ Discovery & Stakeholder Alignment | ✔ → App Store and Google Play reviews (video) | ✔ |
| R-026 | FIG | doc-20: — | The Approach/ Discovery & Stakeholder Alignment | ✔ replaced by the video her note asks for (her note: picture is only for reference) | ✔ |
| R-027 | H2 | UX Design/ Feature Prioritization | UX Design/ Feature Prioritization | ✔ | ✔ |
| R-028 | P | The solution focused on reducing user effort by creating a streamlined… | UX Design/ Feature Prioritization | ✔ | ✔ |
| R-029 | P | Feature prioritization centered on improving usability, accessibility,… | UX Design/ Feature Prioritization | ✔ | ✔ |
| R-030 | LI | Vaccination Status: A clear status card displaying COVID-19 vaccinatio… | UX Design/ Feature Prioritization | ✔ | ✔ |
| R-031 | LI | Multilingual Support: Terms and Conditions available in multiple langu… | UX Design/ Feature Prioritization | ✔ | ✔ |
| R-032 | LI | Appointment Scheduling: An integrated calendar that allowed users to f… | UX Design/ Feature Prioritization | ✔ | ✔ |
| R-033 | LI | Household Management: The ability to add and manage household members … | UX Design/ Feature Prioritization | ✔ | ✔ |
| R-034 | LI | Symptom Diary: An optional tool for anonymously reporting post-vaccina… | UX Design/ Feature Prioritization | ✔ | ✔ |
| R-035 | LI | Testing Location Map: An interactive map helping users quickly locate … | UX Design/ Feature Prioritization | ✔ | ✔ |
| R-036 | NOTE | INSERT PDF OR VIDEO OF DESKTOP & MOBILE WIRE FRAMES HERE | UX Design/ Feature Prioritization | ✔ → Desktop wireframes (video) | ✔ |
| R-037 | FIG | doc-21: Vaccine details: annotated mobile screens | UX Design/ Feature Prioritization | ✔ shown | ✔ |
| R-038 | H2 | Results & Impact | Results & Impact | ✔ | ✔ |
| R-039 | P | The redesigned experience streamlined how Rhode Island residents acces… | Results & Impact | ✔ | ✔ |
| R-040 | H2 | Ongoing Evaluation | Ongoing Evaluation | ✔ | ✔ |
| R-041 | P | Long-term adoption and engagement metrics were outside the scope of my… | Ongoing Evaluation | ✔ | ✔ |
| R-042 | H2 | Reflection | Reflection | ✔ | ✔ |
| R-043 | P | This project strengthened my understanding of designing digital experi… | Reflection | ✔ | ✔ |
| R-044 | P | The project was also particularly meaningful because of the context in… | Reflection | ✔ | ✔ |

Order check: ✔ every item appears after the one before it.

## Littelfuse — `site/room-04-littelfuse.html`

| ID | Type | Text (start) | Section | 1440 | 390 |
|---|---|---|---|---|---|
| L-001 | TITLE | Reimagining How Engineers Discover Littelfuse Products | Header | ✔ | ✔ |
| L-002 | META | Role: UX Consultant / UX Designer /UX Researcher | Header | ✔ | ✔ |
| L-003 | META | Methods: Stakeholder Workshop / Data Analysis / Information Architectu… | Header | ✔ | ✔ |
| L-004 | H2 | Project Overview | Project Overview | ✔ | ✔ |
| L-005 | P | Littelfuse is a global technology manufacturing company that develops … | Project Overview | ✔ | ✔ |
| L-006 | P | I worked with Littelfuse to improve its existing digital portal experi… | Project Overview | ✔ | ✔ |
| L-007 | P | From a business perspective, the redesigned experience also created op… | Project Overview | ✔ | ✔ |
| L-008 | H2 | The Challenge | The Challenge | ✔ | ✔ |
| L-009 | H3 | Simplifying Product Discovery Across a Complex Product Catalog | The Challenge | ✔ | ✔ |
| L-010 | P | Littelfuse offers an extensive portfolio of highly technical products … | The Challenge | ✔ | ✔ |
| L-011 | P | Preliminary research provided by Littelfuse showed that 73.2% of users… | The Challenge | ✔ | ✔ |
| L-012 | P | When asked about the ease of search, 48% of survey respondents said th… | The Challenge | ✔ | ✔ |
| L-013 | P | These findings highlighted an opportunity to reduce users’ reliance on… | The Challenge | ✔ | ✔ |
| L-014 | P | How Might We… | The Challenge | ✔ | ✔ |
| L-015 | LI | How might we help engineers discover the right product without knowing… | The Challenge | ✔ | ✔ |
| L-016 | LI | How might we connect engineers with relevant and complementary product… | The Challenge | ✔ | ✔ |
| L-017 | LI | How might we streamline key tasks—from comparing products and accessin… | The Challenge | ✔ | ✔ |
| L-018 | H2 | The Approach | The Approach | ✔ | ✔ |
| L-019 | P | I began by reviewing existing customer research, business goals, and t… | The Approach | ✔ | ✔ |
| L-020 | P | The analysis exposed gaps in navigation, terminology, content pathways… | The Approach | ✔ | ✔ |
| L-021 | H4 | Synthesized existing research and business priorities | The Approach | ✔ | ✔ |
| L-022 | P | In reviewing existing research I learned that the Little Fuse customer… | The Approach | ✔ | ✔ |
| L-023 | H4 | Defined the primary user: a design engineer | The Approach | ✔ | ✔ |
| L-024 | P | Through stakeholder interviews, existing user research, and analysis o… | The Approach | ✔ | ✔ |
| L-025 | FIG | doc-22: Survey: who drives component decisions | The Approach | ✔ shown | ✔ |
| L-026 | FIG | doc-23: User archetypes: Engineering & Technical, Sales and Procurement | The Approach | ✔ shown | ✔ |
| L-027 | H4 | Mapped the product-discovery journey | The Approach | ✔ | ✔ |
| L-028 | P | The user journey was developed during a collaborative workshop at the … | The Approach | ✔ | ✔ |
| L-029 | FIG | doc-24: Product-discovery journey map | The Approach | ✔ shown | ✔ |
| L-030 | H4 | Audited critical tasks and interface pathways | The Approach | ✔ | ✔ |
| L-031 | P | Following the journey-mapping workshop, I evaluated the existing Litte… | The Approach | ✔ | ✔ |
| L-032 | H4 | 01 — Navigation & Findability | The Approach | ✔ | ✔ |
| L-033 | P | Critical product actions—including Cross Reference, Check Stock, Where… | The Approach | ✔ | ✔ |
| L-034 | H4 | 02 — Incomplete Task Flows | The Approach | ✔ | ✔ |
| L-035 | P | Mapping core tasks exposed several points where the existing experienc… | The Approach | ✔ | ✔ |
| L-036 | H4 | 03 — Interaction & Content Gaps | The Approach | ✔ | ✔ |
| L-037 | P | The audit uncovered smaller usability issues that compounded friction,… | The Approach | ✔ | ✔ |
| L-038 | H4 | Translated findings into design principles | The Approach | ✔ | ✔ |
| L-039 | P | Insights from the audit were translated into design principles focused… | The Approach | ✔ | ✔ |
| L-040 | P | The work also addressed gaps where the existing wireframes did not ful… | The Approach | ✔ | ✔ |
| L-041 | NOTE | INSERT WIREFRAMES FROM PDF HERE | The Approach | ✔ → Littelfuse wireframes (placeholder) | ✔ |
| L-042 | H2 | Results & Impact | Results & Impact | ✔ | ✔ |
| L-043 | P | The redesigned experience streamlined product discovery and evaluation… | Results & Impact | ✔ | ✔ |
| L-044 | H2 | Reflection | Reflection | ✔ | ✔ |
| L-045 | P | This project introduced me to a highly specialized industry with a uni… | Reflection | ✔ | ✔ |

Order check: ✔ every item appears after the one before it.

## Added captions (for Yasmin to approve or edit)

These are **not her words**. They're short factual captions the brief asked for (Q10). Edit any of them and the pages are regenerated from `tools/build_r3.py`.

| Page | Figure | Caption |
|---|---|---|
| index | Photo strip | Power & Energy column |
| index | Photo strip | Jackson Home visitor paths |
| index | Photo strip | 401 Health app |
| index | Photo strip | Column shop drawing |
| index | Photo strip | ITC employee research |
| room-01-jackson-home | Fig. 01 | Time spent on-site by visitor type |
| room-01-jackson-home | Fig. 02 | Congestion, queue sizes, visit time and delays |
| room-01-jackson-home | Fig. 03 | Jackson Home floor plan |
| room-01-jackson-home | Fig. 04 | The Annex floor plan, with site entrance, entrance line and vestibule |
| room-01-jackson-home | Fig. 05 | Discrete event simulation of visitor flow (video) |
| room-01-jackson-home | Fig. 06 | Jackson Home floor plan with expected visitor paths |
| room-01-jackson-home | Fig. 07 | Arrivals spread randomly through the ticketing window |
| room-01-jackson-home | Fig. 08 | Arrivals at the start of the ticketing window |
| room-01-jackson-home | Fig. 09 | Expected visit times by visitor type |
| room-01-jackson-home | Fig. 10 | Skipped exhibits, without and with docent control |
| room-01-jackson-home | Fig. 11 | Best scenario: 20 tickets, 8 walk-ups, with docent control |
| room-02-power-energy | Fig. 01 | Column side: Exhibit wayfinding |
| room-02-power-energy | Fig. 02 | Column side: Innovation stories |
| room-02-power-energy | Fig. 03 | Column side: Interactive exploration |
| room-02-power-energy | Fig. 04 | Column side: Career discovery |
| room-02-power-energy | Fig. 05 | Column side: Artifact interpretation |
| room-02-power-energy | Fig. 06 | Content themes and experience flow for the column |
| room-02-power-energy | Fig. 07 | Lo-fi sketches and wireframes for the column |
| room-02-power-energy | Fig. 08 | ITC employee research: three roles |
| room-02-power-energy | Fig. 09 | Content distribution across the sides of the column |
| room-02-power-energy | Fig. 10 | Final interface and user flow (video) |
| room-02-power-energy | Fig. 11 | CMS channels in Appspace (video) |
| room-02-power-energy | Fig. 12 | Shop drawing, column surround: plan, section and perspective |
| room-02-power-energy | Fig. 13 | Shop drawing: elevations and sections |
| room-02-power-energy | Fig. 14 | Shop drawing: typical column surround and plan |
| room-02-power-energy | Fig. 15 | Column fabrication progression (video) |
| room-02-power-energy | Fig. 16 | Final setup: the installed column (video) |
| room-03-rhode-island | Fig. 01 | Rhode Island Department of Health population health goals |
| room-03-rhode-island | Fig. 02 | App Store and Google Play reviews (video) |
| room-03-rhode-island | Fig. 03 | Desktop wireframes (video) |
| room-03-rhode-island | Fig. 04 | Mobile wireframe: vaccination record |
| room-03-rhode-island | Fig. 05 | Mobile wireframe: dose details |
| room-03-rhode-island | Fig. 06 | Vaccine details: annotated mobile screens |
| room-04-littelfuse | Fig. 01 | Survey: who drives component decisions |
| room-04-littelfuse | Fig. 02 | User archetypes: Engineering & Technical, Sales and Procurement |
| room-04-littelfuse | Fig. 03 | Engineering personas (video) |
| room-04-littelfuse | Fig. 04 | Product-discovery journey map |
| room-04-littelfuse | Fig. 05 | Littelfuse wireframes (placeholder) |

## Supplied, not her copy

| Where | Text | Source |
|---|---|---|
| Homepage hero | Hi, I’m *Yasmin.* | Round 3 brief |
| Homepage facts | Role: Digital Exhibit Designer, The Henry Ford Museum | Q9 |
| Homepage facts | Based in: [pending client] | Q9 (visible placeholder) |
| Homepage facts | Focus: Interactive Exhibit Design · UX Design · UX Research · Digital Marketing | Q9 |
| Homepage facts | Currently: Bringing stories to life through digital experiences | Q9 |
| Homepage contact | Let’s create something people will remember. | Q3 |
| room01 header | Setting: The Henry Ford, Greenfield Village · Year: 2026 | Q9 |
| room02 header | Setting: The Henry Ford Museum, Power & Energy exhibit · Year: [YEAR — pending client] | Q9 |
| room03 header | Setting: State of Rhode Island Department of Health · Year: [YEAR — pending client] | Q9 |
| room04 header | Setting: Littelfuse · Year: [YEAR — pending client] | Q9 |
| Every page | Navigation, chapter numbers, ROLE / METHODS / SETTING / YEAR labels, 'View Projects →', 'Projects', 'Password protected', 'All projects', '← Previous project', 'Next project →', footer, lock-screen text | Brief (interface text) |

