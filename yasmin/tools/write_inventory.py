"""Write COPY-INVENTORY.md from content/copy.json (run from yasmin/)."""
import json

c = json.load(open("content/copy.json"))
site = json.load(open("content/site.json"))

ROOMS = [
    ("room01", "J", "Room 01 — The Henry Ford Jackson Home", "room-01-jackson-home.html"),
    ("room02", "P", "Room 02 — Power & Energy", "room-02-power-energy.html"),
    ("room03", "R", "Room 03 — Rhode Island 401 Health App", "room-03-rhode-island.html"),
    ("room04", "L", "Room 04 — Littelfuse", "room-04-littelfuse.html"),
]

# what each figure / production note becomes on the page
FIG = {
    1: "`doc-01` (p3): the visitor-type table **and** a 'Time Spent On-Site' box plot in one image. Only copy (975px). The table is set as live text (the J-table above), so the figure shows the box-plot half: `r01-chart-onsite-box.jpg`.",
    2: "`doc-02` (p4): Congestion / Queue sizes / Visit time / Delays sheet. Full-res original: `r01_chart_congestion-queues-visit-delays.png`. **A6 board**, lightbox.",
    3: "`doc-03` (p5): house plan without paths. Full-res: `r01_plan_house.png`. Plate.",
    4: "`doc-04` (p6): Annex plan. Only copy (975px). Plate.",
    5: "`doc-05` (p7): house plan **with visitor paths**. Full-res: `r01_plan_house-visitor-paths.png`. **A5/A14 plan-plus-list spread** with Baseline Assumptions (the next chapter), as the brief asks.",
    6: "`doc-06` (p9): Random arrivals chart. Full-res: `r01_chart_arrivals-random.png`. **A6 board**.",
    7: "`doc-07` (p10): On-time arrivals chart. Full-res: `r01_chart_arrivals-on-time.png`. **A6 board**.",
    8: "`doc-08` (p10): Expected Visit Times. Full-res: `r01_chart_expected-visit-times.png`. **A6 board**.",
    9: "`doc-09` (p12): Without / With docent charts. Full-res: `r01_chart_docent-control.png`. **A6 board**.",
    10: "`doc-10` (p12): 'Best scenario: tickets 20, walkups 8, with docent control'. Only copy (975px). **A6 board**.",
    11: "`doc-11` (p15): content themes and experience-flow board. Full-res: `r02_board_content-themes-experience-flow.png`.",
    12: "`doc-12` (p16): whiteboard lo-fi sketches. Full-res: `r02_sketch_whiteboard-lofi.png`.",
    13: "`doc-13` (p17): ITC employee research board. Full-res: `r02_board_itc-employee-research.png`.",
    14: "`doc-14` (p19): the column's sides + interaction flow diagram. Full-res: `r02_diagram_column-sides-flow.png`.",
    15: "`doc-15` (p20): screen grab of the interface. **Replaced by the video** her note just above asks for.",
    16: "`doc-16` (p21): shop drawing sheet 1. **Replaced by the vector PDF** her note asks for: `PandE_Shop-Drawing_Column-Surrounds_AV05.pdf` p1, full-width plate.",
    17: "`doc-17` (p22): shop drawing sheet 2 → vector PDF p2, full-width plate.",
    18: "`doc-18` (p22): shop drawing sheet 3 → vector PDF p3, full-width plate.",
    19: "`doc-19` (p27): the 23 population-health goals table. Only copy (975px). Full plate with caption.",
    20: "`doc-20` (p28): App Store review screenshot, which her note calls 'only for reference'. **Replaced by the video** `r03_video_app-store-reviews.mp4`.",
    21: "`doc-21` (p29): annotated 'Vaccine Details' board (two phone screens with callouts). Full-res: `r03_ui_vaccine-details-annotated.png`. **Kept exactly as she made it** (Q7).",
    22: "`doc-22` (p33): 'Designing for the people who drive component decisions' stat board. Only copy (975px). Plate.",
    23: "`doc-23` (p33): user archetypes board. Full-res: `r04_doc_user-archetypes.png`. Full plate.",
    24: "`doc-24` (p34): journey map. Full-res: `r04_doc_journey-map.png`. Full plate.",
}
NOTE = {
    "INSERT VIDEO HERE - DISCRETE EVENT SIMULATION": "Video block → `r01_video_discrete-event-simulation.mp4` (received in Phase 2; player bar cropped). A5 video with play button.",
    "INSERT VIDEO HERE BELOW IS SCREEN GRAB OF WHAT IT LOOKS LIKE": "Video block → `r02_video_interface-user-flow.mp4`, replacing the screen grab `doc-15`.",
    "INSERT POWER & ENERGY VIDEO HERE": "Video block → `r02_video_appspace-cms-channels.mp4` (the CMS channels she describes in the line above).",
    "USE PDF VERSION HERE OF DRAWINGS": "Three full-width plates rendered from `PandE_Shop-Drawing_Column-Surrounds_AV05.pdf`, replacing `doc-16/17/18`.",
    "INSERT VIDEO OF APP STORE REVIEWS HERE ( PICTURE IS ONLY FOR REFERENCE)": "Video block → `r03_video_app-store-reviews.mp4`, replacing the reference picture `doc-20`.",
    "INSERT PDF OR VIDEO OF DESKTOP & MOBILE WIRE FRAMES HERE": "Video block → `r03_video_wireframes.mp4` (desktop), with the **frameless mobile screens** from `Rhode_Island_DOH_Wireframes.pdf` beside it (Q7). Her own figure `doc-21` follows unchanged.",
    "INSERT WIREFRAMES FROM PDF HERE": "**Labelled placeholder** (Q8): \"Littelfuse wireframes — pending export from Adobe XD\". Logged in ASSET-GAPS.md (B1, Round 3).",
}
PLAN = {
    "room01": {
        "Project Overview": "A2 chapter: number + title left (6 cols), text right (12 cols).",
        "The Challenge": "A2 chapter. Constraints as a real list; the 'How might we' line as a pull sentence.",
        "Research Questions": "A3 label / text rows: each sub-heading (Visitor Experience · Capacity Planning · Operations) is the row label, its bullets the text.",
        "Research Methodology": "A3 rows for the three methods. The visitor-type table becomes an **A4 stats strip** (60% · 10% · 30% with her characteristic text beneath each; default D3).",
        "Building the Simulation": "A2 chapter, then plates in her order.",
        "Baseline Assumptions": "**A5 / A14 spread**: house plan with paths (J-fig 5) beside her 7 assumptions.",
        "Scenario Testing": "Nested lists kept at her three levels; charts as an **A6 board** with captions + lightbox.",
        "Findings": "**A7**: the four findings as a numbered 01–04 list on the right, the docent / best-scenario plates on the left.",
        "Impact": "**A7** numbered list of her 7 bullets.",
        "Reflection": "Centred, 28px italic.",
    },
    "room02": {
        "The Challenge": "Two A3 rows (sub-heading = label) with each 'How might we' as a pull sentence.",
        "The Approach/ UX Design": "A2 chapter. The five 'experience included' bullets sit beside an **A6 board of the five column-art panels** (Q6).",
        "Discovery & Stakeholder Alignment": "A2 chapter; the three UX-copy excerpts as **indented pull quotes**.",
        "CMS Integration & Implementation": "A2 chapter + A5 video.",
        "Installation & Fabrication": "A2 chapter; shop drawings as full-width plates; fabrication video (A5).",
        "Results & Impact": "**A7** numbered list + final-setup video.",
        "Reflection": "Centred, 28px italic.",
    },
    "room03": {
        "The Challenge": "Two A3 rows (sub-heading = label), each with its 'How might we...' list.",
        "The Approach/ Discovery & Stakeholder Alignment": "A2 chapter; goals table as a full plate; App Store video (A5) in place of the picture.",
        "UX Design/ Feature Prioritization": "A2 chapter; the six features as a list; wireframes video; the two mobile screens side by side (**A2 wide + tall**).",
        "Results & Impact": "**A7** layout.",
        "Reflection": "Centred, 28px italic.",
    },
    "room04": {
        "The Challenge": "A3 row; the three How-Might-We bullets as a list.",
        "The Approach": "Sub-headings as A3 row labels. The archetype board and journey map as **full plates**. The audit items 01–03 as an **A7 numbered list**. Wireframes placeholder where her note sits.",
        "Results & Impact": "**A7** layout.",
        "Reflection": "Centred, 28px italic.",
    },
}

L = []
w = L.append
w("# Copy inventory: every word, in her order")
w("")
w("The checklist for Round 3. Every heading, paragraph, bullet, table row, quote and production note from her two source documents, numbered, verbatim and in document order. `COPY-CHECK.md` will tick each ID against the built pages.")
w("")
w("**Sources:** `source/CASE_STUDY-Yasmin_Bajwa.pdf` (the brief's `CASE STUDY-Yasmin Bajwa_compressed.pdf`, renamed in Phase 1) and `source/Instructions_About_Me.docx`.")
w("")
w("**How it was made.** `tools/extract_copy.py` reads the PDF line by line with its fonts and writes `content/copy.json`. The pages will be generated from that file, and the copy check reads it too, so the site and this list can't drift apart. A word-by-word diff against the PDF's own text layer matches all **5,174 words in order**; the only difference is two Google Drive links the PDF wrapped across lines, joined back here. The About document matches paragraph for paragraph.")
w("")
w("**The only clean-up applied** (none of it changes a word):")
w("- lines of one paragraph or bullet are joined with a single space;")
w("- bullet glyphs (●), invisible zero-width spaces and trailing spaces are removed;")
w("- double spaces inside a line become one (e.g. \"team I  evaluated\"). A browser would collapse them anyway.")
w("")
w("Spelling, punctuation and capitalisation are exactly hers, including the likely slips listed in `COPY-NOTES-FOR-CLIENT.md` for her approval. The one exception is the removed duplicate line (P-050), noted there and below.")
w("")
w("**Key to types:** `TITLE` project title · `META` Role / Methods line · `H2` chapter heading (these build the chapter index) · `H3` sub-heading · `H4` bold run-in label · `P` paragraph · `LI` bullet (`LI²`, `LI³` = nested levels) · `HMW` her bold \"How might we\" sentence · `QUOTE` UX-copy excerpt · `TABLE` table · `FIG` figure in her doc · `NOTE` her production note (not shown as text; it becomes the video, drawing or placeholder it asks for).")
w("")

# ---------------- summary
counts = {}
for key, pre, name, _ in ROOMS:
    t = {}
    for it in c[key]:
        t[it["type"]] = t.get(it["type"], 0) + 1
    counts[key] = t
w("## Summary")
w("")
w("| Project | Items | Chapters (H2) | Paragraphs | Bullets | Figures | Notes → media |")
w("|---|---|---|---|---|---|---|")
for key, pre, name, _ in ROOMS:
    t = counts[key]
    w(f"| {name} | {len(c[key])} | {t.get('h2',0)} | {t.get('p',0)} | {t.get('li',0)} | {t.get('figure',0)} | {t.get('note',0)} |")
w(f"| About (docx) | {len(c['about'])} | | | | | |")
w("")

# ---------------- About
w("## About: `Instructions_About_Me.docx`")
w("")
where = {
    "brief_h": "Brief to us. **Not printed** (confirmed, Q1)",
    "brief": "Brief to us. **Not printed** (confirmed, Q1)",
    "h2": "Homepage: section label for the About / statement area",
    "instruction": "Instruction to us. **Not printed** (confirmed, Q1); followed: skills shown in this order",
    "skill": "Homepage §3 **Four disciplines** (A10) panel label",
}
n = 0
for it in c["about"]:
    n += 1
    loc = where.get(it["type"], "")
    if it["type"] == "p":
        loc = "Homepage §1 **Hero**, under 'Hi, I'm Yasmin.'" if it["text"].startswith("Hi!") else "Homepage §2 **Statement** (A9), centred 40px"
    w(f"- **A-{n:02d}** `{it['type'].upper()}`: {it['text']}  \n  → {loc}")
w("")
w("Skill **A-10** is printed exactly as `UX ( User Experience) Design`, space included (default D1). The suggested fix is in COPY-NOTES-FOR-CLIENT.md.")
w("")

# ---------------- rooms
for key, pre, name, page in ROOMS:
    w(f"## {name}")
    w("")
    w(f"Page: `site/{page}`")
    w("")
    chapters = [it["text"] for it in c[key] if it["type"] == "h2"]
    w("**Chapter index (her H2 headings, her order):** " + " · ".join(f"{i+1} {t}" for i, t in enumerate(chapters)))
    w("")
    n = 0
    ch = 0
    for it in c[key]:
        n += 1
        iid = f"{pre}-{n:03d}"
        typ = it["type"]
        if typ == "title":
            w(f"### Header (A1 + A4)")
            w("")
            w(f"- **{iid}** `TITLE` {it['src']}: {it['text']}")
            continue
        if typ == "meta":
            w(f"- **{iid}** `META` {it['src']}: **{it['label']}**: {it['text']}  \n  → header meta panel ({it['label'].upper()})")
            if it["label"] == "Methods":
                sv = site["rooms"][key]
                w(f"- *(supplied, not her copy)* **Setting**: {sv['setting']}  \n  → header meta panel (SETTING, Q9)")
                w(f"- *(supplied, not her copy)* **Year**: {sv['year']}  \n  → header meta panel (YEAR, Q9){' — shown as a visible placeholder' if sv.get('year_pending') else ' (Summer 2026 opening, from her Project Overview)'}")
            continue
        if typ == "h2":
            ch += 1
            w("")
            w(f"### Chapter {ch}: {it['text']}")
            p = PLAN[key].get(it["text"], "A2 / A3 chapter: number + title left, her text right.")
            w(f"*Layout: {p}*")
            w("")
            flag = " (her source sets this at 12–13pt; treated as a chapter like her other projects; default D2)" if it.get("promoted") else ""
            w(f"- **{iid}** `H2` {it['src']}: {it['text']}{flag}")
            continue
        if typ == "figure":
            w(f"- **{iid}** `FIG` {FIG[it['doc']]}")
            if it["doc"] == 23:
                w("- ➕ **ADDED MEDIA** (Q6): **engineering personas video** `r04_video_engineering-personas.mp4`, directly under the archetype board, inside 'Defined the primary user: a design engineer'.")
            continue
        if typ == "note":
            w(f"- **{iid}** `NOTE` {it['src']}: \"{it['text']}\"  \n  → {NOTE.get(it['text'].split(' - https')[0].strip(), 'Video block → her Google Drive video (already in `media/`).') if 'drive.google' not in it['text'] else ('Video block → `r02_video_fabrication-progression.mp4` (the file behind this link).' if 'FABRICATION' in it['text'] else 'Video block → `r02_video_final-setup.mp4` (the file behind this link).')}")
            continue
        if typ == "table":
            w(f"- **{iid}** `TABLE` {it['src']}: {' | '.join(it['head'])}")
            for r in it["rows"]:
                w(f"  - {' | '.join(r)}")
            continue
        label = {"li": "LI" + {1: "", 2: "²", 3: "³"}[it.get("level", 1)], "p": "P", "h3": "H3", "h4": "H4", "hmw": "HMW", "quote": "QUOTE"}[typ]
        extra = ""
        if it.get("bold_parts"):
            extra = f"  \n  *(bold in her doc: \"{' '.join(it['bold_parts'])}\")*"
        if it.get("removed"):
            extra += f"  \n  *(removed on instruction, Q12: the duplicated sentence \"{it['removed']}\" that ended this paragraph in her doc; logged in COPY-NOTES-FOR-CLIENT.md)*"
        indent = "  " * (it.get("level", 1) - 1) if typ == "li" else ""
        w(f"{indent}- **{iid}** `{label}` {it['src']}: {it['text']}{extra}")
        if key == "room02" and typ == "li" and it["text"].startswith("Artifact interpretation:"):
            w("- ➕ **ADDED MEDIA** (Q6): board of the **column-art panels**, one per side of the column (wayfinding, Innovation Nation, interactive map, careers, artifact highlights), right after the list of the five sides. Her files `r02_art_PandE_Column_*.jpg`; the unlicensed Shutterstock careers comp stays out (ASSET-GAPS C2). No words added except captions.")
    w("")

# ---------------- words that are not hers
w("## Words on the pages that are not in her documents")
w("")
w("Rule 3 says no additions. These come from the Round 3 brief itself or are site navigation, and are listed so COPY-CHECK can separate them from her copy.")
w("")
w("| Where | Text | Source |")
w("|---|---|---|")
for row in [
    ("Top bar", "Yasmin Bajwa · Projects · About · Contact", "Brief (navigation)"),
    ("Hero", "Hi, I'm *Yasmin.*", "Brief (her doc says \"Hi! I'm Yasmin,\"; this is the greeting the brief asks for)"),
    ("Hero", "View Projects →", "Brief"),
    ("Hero caption", "DIGITAL EXHIBIT DESIGNER — THE HENRY FORD", "Brief (her words, re-cased)"),
    ("Hero facts", " · ".join(f"{f['label'].upper()}: {f['value']}" for f in site["home"]["facts"]), "Supplied by you (Q9). BASED IN stays a visible placeholder"),
    ("Photo strip", "tiny caption above each photo", "Written by us; listed under Added captions (Q10)"),
    ("Projects", "Projects · Password protected · her project titles · her Role lines", "Brief + her copy"),
    ("Contact heading", site["home"]["contact_heading"], "Your wording from her sentence (Q3). Her statement paragraph A-07 stays whole"),
    ("Contact", "email · LinkedIn · résumé", "Pending her details"),
    ("Every case study", "Chapter numbers, ROLE / METHODS / SETTING / YEAR labels, '← Previous project · Next project → · All projects'", "Brief"),
    ("Every figure", "FIG. n — short factual caption", "Written by us; listed under **Added captions** in COPY-CHECK.md for her approval (Q10)"),
    ("Case study meta", "SETTING and YEAR values", "Supplied by you (Q9); three YEARs are visible placeholders"),
    ("Lock screen", "Projects are shared *by invitation.* · Enter the password to continue. · No password? Email Yasmin →", "Brief"),
]:
    w(f"| {row[0]} | {row[1]} | {row[2]} |")
w("")
w("**Dropped as the brief instructs:** §5 \"About by numbers\". Her copy has no numbers about herself: '4 projects' and '3 institutions' are counts I'd be making up, and the brief says drop the section if fewer than three real numbers exist.")
w("")

# ---------------- questions
w("## Decisions (Round 3 answers)")
w("")
for q, t in [
    ("Q1", "Brief paragraphs A-01…A-04 and the instruction A-08 are **not printed**. Verbatim applies to the two About Me paragraphs and all of the case-study document."),
    ("Q3", f"Contact heading: \"{site['home']['contact_heading']}\". The statement section keeps her paragraph A-07 whole."),
    ("Q6", "Column-art board after the five-sides list in 'The Approach/ UX Design'; personas video directly under the archetype board (both marked ➕ above)."),
    ("Q7", "Her Rhode Island figure is kept as made; frameless mobile screens sit beside the wireframes video."),
    ("Q8", "Littelfuse wireframes: labelled placeholder, logged in ASSET-GAPS.md."),
    ("Q9", "SETTING and YEAR per project and the homepage facts come from `content/site.json`; pending values stay visible."),
    ("Q10", "Short factual captions, listed under 'Added captions' in COPY-CHECK.md."),
    ("Q11–13", "Everything verbatim; suspected slips go to COPY-NOTES-FOR-CLIENT.md. One exception: the second \"Below are the CMS channels within App Space.\" is removed (P-050) and noted there."),
]:
    w(f"- **{q}.** {t}")
w("")
w("## Defaults applied (no answer needed)")
w("")
for d, t in [
    ("D1 (Q2)", "\"UX ( User Experience) Design\" printed exactly as written, space included; fix suggested in COPY-NOTES-FOR-CLIENT.md."),
    ("D2 (Q4)", "Results & Impact, Ongoing Evaluation and Reflection are chapters in every project, although some are set at 12–13pt in her doc."),
    ("D3 (Q5)", "Jackson Home visitor-type table shown as an A4 stats strip: her row order (Strollers, Studiers, Streakers), her column headings as small labels, her characteristic text under each numeral."),
    ("D4 (Q13)", "\"Ticketing Window & Arrival Patterns\" appears twice in Scenario Testing, as in her doc."),
    ("D5", "Figures that are replaced by what her notes ask for (screen grab → video, reference picture → video, JPEG drawings → vector PDF) are not shown twice."),
]:
    w(f"- **{d}:** {t}")
w("")
open("COPY-INVENTORY.md", "w").write("\n".join(L) + "\n")
print("lines", len(L))
