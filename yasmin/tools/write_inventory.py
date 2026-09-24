"""Write COPY-INVENTORY.md from content/copy.json (run from yasmin/)."""
import json

c = json.load(open("content/copy.json"))

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
    21: "`doc-21` (p29): annotated 'Vaccine Details' board (two phone screens with callouts). Full-res: `r03_ui_vaccine-details-annotated.png`. See question Q7 (device frames).",
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
    "INSERT PDF OR VIDEO OF DESKTOP & MOBILE WIRE FRAMES HERE": "Video block → `r03_video_wireframes.mp4` (desktop). Mobile screens from `Rhode_Island_DOH_Wireframes.pdf` can sit beside it; see Q7.",
    "INSERT WIREFRAMES FROM PDF HERE": "**Missing.** Only Adobe XD links exist (`Littelfuse_Wireframes_XD-links.docx`). A labelled placeholder until exports arrive (ASSET-GAPS B1). See Q8.",
}
PLAN = {
    "room01": {
        "Project Overview": "A2 chapter: number + title left (6 cols), text right (12 cols).",
        "The Challenge": "A2 chapter. Constraints as a real list; the 'How might we' line as a pull sentence.",
        "Research Questions": "A3 label / text rows: each sub-heading (Visitor Experience · Capacity Planning · Operations) is the row label, its bullets the text.",
        "Research Methodology": "A3 rows for the three methods. The visitor-type table becomes an **A4 stats strip** (60% · 10% · 30% with her characteristic text beneath each; see Q5).",
        "Building the Simulation": "A2 chapter, then plates in her order.",
        "Baseline Assumptions": "**A5 / A14 spread**: house plan with paths (J-fig 5) beside her 7 assumptions.",
        "Scenario Testing": "Nested lists kept at her three levels; charts as an **A6 board** with captions + lightbox.",
        "Findings": "**A7**: the four findings as a numbered 01–04 list on the right, the docent / best-scenario plates on the left.",
        "Impact": "**A7** numbered list of her 7 bullets.",
        "Reflection": "Centred, 28px italic.",
    },
    "room02": {
        "The Challenge": "Two A3 rows (sub-heading = label) with each 'How might we' as a pull sentence.",
        "The Approach/ UX Design": "A2 chapter. The five 'experience included' bullets sit beside an **A6 board of the five column-art panels** (see Q6).",
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
w("Spelling, punctuation and capitalisation are exactly hers, including the likely slips listed under **Questions**. Nothing is corrected unless she says so.")
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
    "brief_h": "Brief to the designer, **not site copy** (Q1)",
    "brief": "Brief to the designer, **not site copy** (Q1)",
    "h2": "Homepage: section label for the About / statement area",
    "instruction": "Instruction to the designer, **not site copy**; followed exactly (skills shown in this order)",
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
w("Skill **A-10** reads `UX ( User Experience) Design` in her file, with a space after the bracket. See Q2.")
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
            continue
        if typ == "h2":
            ch += 1
            w("")
            w(f"### Chapter {ch}: {it['text']}")
            p = PLAN[key].get(it["text"], "A2 / A3 chapter: number + title left, her text right.")
            w(f"*Layout: {p}*")
            w("")
            flag = " (her source sets this at 12–13pt; treated as a chapter like her other projects; Q4)" if it.get("promoted") else ""
            w(f"- **{iid}** `H2` {it['src']}: {it['text']}{flag}")
            continue
        if typ == "figure":
            w(f"- **{iid}** `FIG` {FIG[it['doc']]}")
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
        indent = "  " * (it.get("level", 1) - 1) if typ == "li" else ""
        w(f"{indent}- **{iid}** `{label}` {it['src']}: {it['text']}{extra}")
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
    ("Hero facts", "ROLE / BASED IN / FOCUS / CURRENTLY + values", "Brief. **Values not in her copy** (Q9)"),
    ("Photo strip", "tiny caption above each photo", "Brief (A8). Caption text needs approval (Q10)"),
    ("Projects", "Projects · Password protected · her project titles · her Role lines", "Brief + her copy"),
    ("Contact", "Let's make something *people remember.*", "Brief. Her line is \"create something people will remember\" (Q3)"),
    ("Contact", "email · LinkedIn · résumé", "Pending her details"),
    ("Every case study", "Chapter numbers, 'FIG. n — caption', ROLE / METHODS labels, '← Previous project · Next project → · All projects'", "Brief. Captions need approval (Q10)"),
    ("Case study meta", "SETTING / YEAR", "Brief. **Not in her copy** (Q9)"),
    ("Lock screen", "Projects are shared *by invitation.* · Enter the password to continue. · No password? Email Yasmin →", "Brief"),
]:
    w(f"| {row[0]} | {row[1]} | {row[2]} |")
w("")
w("**Dropped as the brief instructs:** §5 \"About by numbers\". Her copy has no numbers about herself: '4 projects' and '3 institutions' are counts I'd be making up, and the brief says drop the section if fewer than three real numbers exist.")
w("")

# ---------------- questions
w("## Questions before building")
w("")
def ids_with(room, pre, needle, typ=None):
    return [f"{pre}-{i+1:03d}" for i, it in enumerate(c[room]) if needle in it.get("text", "") and (typ is None or it["type"] == typ)]
dup = ids_with("room02", "P", "Below are the CMS channels within App Space.")
tw = ids_with("room01", "J", "Ticketing Window & Arrival Patterns", "h4")
Q = [
    ("Q1", "The four **'Portfolio Website Direction'** paragraphs (A-01…A-04) and **'Highlight these 4 skills in this order::'** (A-08) are instructions to the designer (\"The developer can recommend the best structure\", \"Please also include password protection\"). I plan to follow them, **not print them** on the site. Confirm."),
    ("Q2", "**'UX ( User Experience) Design'**: verbatim has a space inside the bracket. Print exactly, or may it read **'UX (User Experience) Design'**?"),
    ("Q3", "**Contact headline:** the brief's \"Let's make something people remember.\" isn't a sentence in her docs (hers: \"…create something people will remember.\"). Use the brief's line, or her sentence verbatim?"),
    ("Q4", "**Heading levels:** in Rhode Island and Littelfuse she set Results & Impact / Ongoing Evaluation / Reflection at 12–13pt, and in Power & Energy 'Ongoing Evaluation' at 12pt, while the same headings are chapters elsewhere. I'm treating them all as chapters so the chapter index is consistent. Words unchanged."),
    ("Q5", "**Jackson Home visitor-type table** (J-table): the A4 stats strip shows 60% · 10% · 30% with her characteristic text beneath. It keeps her row order (Strollers, Studiers, Streakers) and her column headings as small labels. OK?"),
    ("Q6", "**Additions of images** the brief asks for that her doc doesn't place: the **Power & Energy column-art panels** (A6 board beside 'The experience included:') and optionally the **Littelfuse personas video** (after 'Defined the primary user'). Both are her files; no words added. Confirm placement."),
    ("Q7", "**Rhode Island screens:** her figure `doc-21` has phone frames drawn round the screens, and the brief says no device mockups. Keep her figure as is (it's her own board), and show the 'two mobile screens side by side' from the frameless vector PDF next to the wireframes video?"),
    ("Q8", "**Littelfuse 'INSERT WIREFRAMES FROM PDF HERE':** there is no Littelfuse wireframes PDF or video in the repo. The only video is the personas one. It stays a labelled placeholder until she exports screens from the XD links."),
    ("Q9", "**Values I don't have:** homepage facts (BASED IN, FOCUS, CURRENTLY) and case-study SETTING / YEAR. I'll show only ROLE and METHODS in the case-study header (her words) and leave the others as marked placeholders, unless you supply them."),
    ("Q10", "**Figure captions** are required by the brief but aren't her words. I'll write short, factual ones (e.g. \"FIG. 05 — House plan with expected visitor paths\") and list them in COPY-CHECK as captions, separate from her copy."),
    ("Q11", "**Likely slips in her text, kept verbatim unless she approves a fix:** \"Annex (complimentary building…)\" (complementary?) · \"ITC( International\" · \"lo- fi\" · \"feedback( See below)\" · \"Little Fuse\" ×2 beside \"Littelfuse\" · \"Procurement.This\" (missing space) · \"rather than working of static archetypes\" · \"In combination with … we identify\" · \"particularly those centered on difficult history\" (no full stop) · \"App Space\" beside \"Appspace\" · \"wire frames\" beside \"wireframes\" · \"The final wireframes shown below.\" · \"Pre 1965\" · \"deciding factor for where to place digital interactives\" (bullet grammar) · spacing in \"UX Designer| Experience Design\", \"|UX Researcher\", \"The Approach/ UX Design\"."),
    ("Q12", f"**Duplicated line:** \"Below are the CMS channels within App Space.\" ends both the CMS chapter ({dup[0]}) and an Installation & Fabrication paragraph ({dup[1]}), where no CMS image follows. Verbatim means it appears twice. Keep both, or drop the second?"),
    ("Q13", f"**Duplicated heading:** \"Ticketing Window & Arrival Patterns\" appears twice in Scenario Testing ({tw[0]}, {tw[1]}), once for random arrivals and once for arrivals at the start of the window. Kept twice, as in her doc."),
]
for q, t in Q:
    w(f"- **{q}.** {t}")
w("")
open("COPY-INVENTORY.md", "w").write("\n".join(L) + "\n")
print("lines", len(L))
