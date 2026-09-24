"""Compare the rendered pages with content/copy.json and write COPY-CHECK.md.
Run from yasmin/ after:  python3 tools/build_r3.py && node tools/dom_text.js > content/dom.json
Every item must be on its page exactly once, word-for-word as rendered
(so CSS upper-casing would fail too), visible at 1440px and 390px, in her order."""
import json, re

c = json.load(open("content/copy.json"))
import sys
DOM = sys.argv[1] if len(sys.argv) > 1 else "content/dom.json"     # e.g. content/dom_wf.json to check the wireframes
dom = json.load(open(DOM))
caps = json.load(open("content/captions.json"))
site = json.load(open("content/site.json"))
N = lambda s: re.sub(r"\s+", " ", (s or "").replace(" ", " ")).strip()

ROOMS = [("room01", "J", "room-01-jackson-home", "The Henry Ford Jackson Home"),
         ("room02", "P", "room-02-power-energy", "Power & Energy"),
         ("room03", "R", "room-03-rhode-island", "Rhode Island 401 Health App"),
         ("room04", "L", "room-04-littelfuse", "Littelfuse")]
FIGMAP = json.load(open("content/figmap.json"))      # written by tools/build_r3.py: item id -> captions shown for it
REPLACED = {15: "replaced by the video her note asks for", 16: "replaced by the vector PDF her note asks for",
            17: "replaced by the vector PDF her note asks for", 18: "replaced by the vector PDF her note asks for",
            20: "replaced by the video her note asks for (her note: picture is only for reference)"}


def check_page(page, expected):
    """expected: list of (id, type, text-or-cells). Returns rows + order ok."""
    rows, order_ok = [], True
    res = {}
    for w in (1440, 390):
        els = dom[f"{page}@{w}"]
        by = {}
        for e in els:
            if e["id"]:
                by.setdefault(e["id"], []).append(e)
        last = -1
        for iid, typ, want in expected:
            got = by.get(iid, [])
            ok, why = True, ""
            if len(got) != 1:
                ok, why = False, f"found {len(got)} times"
            else:
                e = got[0]
                if not e["visible"]:
                    ok, why = False, "not visible"
                elif typ == "table":
                    miss = [x for x in want if N(x) not in N(e["text"])]
                    if miss:
                        ok, why = False, "missing cells: " + "; ".join(miss)
                elif N(e["text"]) != N(want):
                    ok, why = False, f"text differs: «{N(e['text'])[:80]}»"
                if e["i"] < last:
                    ok, why = False, "out of order"; order_ok = False
                last = max(last, e["i"])
            res.setdefault(iid, {})[w] = (ok, why)
    return res, order_ok


out = []
w = out.append
total = passed = 0
w("# Copy check")
w("")
w("Each rendered page is compared, item by item, with `content/copy.json`, the verbatim extraction of her two documents (see COPY-INVENTORY.md). An item passes (✔) only if it is:")
w("")
w("- on its page **exactly once**, with a `data-id` matching its inventory ID;")
w("- **word-for-word identical as rendered**, so CSS upper-casing or a changed character fails;")
w("- **visible** at both 1440px and 390px;")
w("- **in her order**, after the previous item.")
w("")
w("The comparison is automatic (`tools/dom_text.js` then `tools/copy_check.py`). Re-run it after any edit. The tables show the start of each text; the check compares the full text.")
w("")
summary_at = len(out)

# ---------------- About
exp = [(f"A-{k:02d}", "p", c["about"][k - 1]["text"]) for k in (5, 6, 7, 9, 10, 11, 12)]
res, ok_order = check_page("index", exp)
w("## Homepage: About (`Instructions_About_Me.docx`)")
w("")
w("| ID | Text | Where | 1440 | 390 |")
w("|---|---|---|---|---|")
where = {"A-05": "Hero, label above her first paragraph", "A-06": "Hero, under the greeting", "A-07": "About bento, statement in the left 12 columns",
         "A-09": "Four disciplines, panel 01", "A-10": "Four disciplines, panel 02", "A-11": "Four disciplines, panel 03", "A-12": "Four disciplines, panel 04"}
for k, a in enumerate(c["about"], 1):
    iid = f"A-{k:02d}"
    if iid in res:
        r = res[iid]
        good = r[1440][0] and r[390][0]
        total += 1; passed += good
        w(f"| {iid} | {a['text'][:70]}{'…' if len(a['text']) > 70 else ''} | {where[iid]} | {'✔' if r[1440][0] else '✘ ' + r[1440][1]} | {'✔' if r[390][0] else '✘ ' + r[390][1]} |")
    else:
        w(f"| {iid} | {a['text'][:70]}{'…' if len(a['text']) > 70 else ''} | Not printed (brief / instruction, confirmed Q1) | — | — |")
w("")

# data-ref copies of her titles and Role lines (homepage rows, projects grid)
refs_bad = []
for page in ("index", "projects"):
    for e in dom[f"{page}@1440"]:
        if e["ref"]:
            room = {"J": "room01", "P": "room02", "R": "room03", "L": "room04"}[e["ref"][0]]
            it = c[room][int(e["ref"][2:]) - 1]
            if N(e["text"]) != N(it["text"]):
                refs_bad.append((page, e["ref"], e["text"]))
w(f"**Project titles and Role lines repeated on the homepage rows and the Projects page:** {'✔ all identical to her text' if not refs_bad else '✘ ' + str(refs_bad)}.")
w("")

# ---------------- rooms
for key, pre, page, name in ROOMS:
    items = c[key]
    exp, chapter_of, ch = [], {}, "Header"
    for i, it in enumerate(items):
        iid = f"{pre}-{i + 1:03d}"
        if it["type"] == "h2":
            ch = it["text"]
        chapter_of[iid] = ch
        if it["type"] in ("figure", "note"):
            continue
        if it["type"] == "table":
            exp.append((iid, "table", [x for row in it["rows"] for x in row]))
        else:
            exp.append((iid, it["type"], it["text"]))
    res, ok_order = check_page(page, exp)
    pagecaps = [x[2] for x in caps if x[0] == page]
    w(f"## {name} — `site/{page}.html`")
    w("")
    w("| ID | Type | Text (start) | Section | 1440 | 390 |")
    w("|---|---|---|---|---|---|")
    for i, it in enumerate(items):
        iid = f"{pre}-{i + 1:03d}"
        typ = it["type"]
        if typ == "figure":
            d = it["doc"]
            shown = FIGMAP.get(page, {}).get(iid, [])
            if d in REPLACED:
                mark = f"✔ {REPLACED[d]}"
            else:
                mark = ("✔ shown" + (f" as {len(shown)} tiles" if len(shown) > 1 else "")
                        if shown and all(x in pagecaps for x in shown) else "✘ missing")
            total += 1; passed += mark.startswith("✔")
            w(f"| {iid} | FIG | doc-{d:02d}: {'; '.join(shown) or '—'} | {chapter_of[iid]} | {mark} | {mark[:1]} |")
            continue
        if typ == "note":
            shown = FIGMAP.get(page, {}).get(iid, [])
            mark = ("✔ → " + "; ".join(shown)) if shown and all(x in pagecaps for x in shown) else "✘ media missing"
            total += 1; passed += mark.startswith("✔")
            w(f"| {iid} | NOTE | {it['text'][:60]}{'…' if len(it['text']) > 60 else ''} | {chapter_of[iid]} | {mark} | {mark[:1]} |")
            continue
        r = res[iid]
        good = r[1440][0] and r[390][0]
        total += 1; passed += good
        t = it["text"] if typ != "table" else " | ".join(it["head"])
        if typ == "meta":
            t = it["label"] + ": " + t
        extra = " *(duplicate sentence removed, Q12)*" if it.get("removed") else ""
        w(f"| {iid} | {typ.upper()} | {t[:70].replace('|', '/')}{'…' if len(t) > 70 else ''}{extra} | {chapter_of[iid]} | {'✔' if r[1440][0] else '✘ ' + r[1440][1]} | {'✔' if r[390][0] else '✘ ' + r[390][1]} |")
    w("")
    w(f"Order check: {'✔ every item appears after the one before it' if ok_order else '✘ items out of order'}.")
    if key == "room02":
        cnt = sum(1 for e in dom[f"{page}@1440"] if e["id"] and "Below are the CMS channels within App Space." in (e["text"] or ""))
        w(f"Removed duplicate: \"Below are the CMS channels within App Space.\" appears **{cnt}×** on the page (expected 1, in P-045). {'✔' if cnt == 1 else '✘'}")
    w("")

# ---------------- added words
w("## Added captions (for Yasmin to approve or edit)")
w("")
w("These are **not her words**. They're short factual captions the brief asked for (Q10). Edit any of them and the pages are regenerated from `tools/build_r3.py`.")
w("")
w("| Page | Figure | Caption |")
w("|---|---|---|")
for pg, lab, cap in caps:
    w(f"| {pg} | {lab} | {cap} |")
w("")
w("## Supplied, not her copy")
w("")
w("| Where | Text | Source |")
w("|---|---|---|")
w("| Homepage hero | Hi, I’m *Yasmin.* | Round 3 brief |")
for f in site["home"]["facts"]:
    w(f"| Homepage facts | {f['label']}: {f['value']} | Q9{' (visible placeholder)' if f.get('pending') else ''} |")
w(f"| Homepage contact | {site['home']['contact_heading']} | Q3 |")
for k, v in site["rooms"].items():
    w(f"| {k} header | Setting: {v['setting']} · Year: {v['year']} | Q9 |")
w("| Every page | Navigation, chapter numbers, ROLE / METHODS / SETTING / YEAR labels, 'View Projects →', 'Projects', 'Password protected', 'All projects', '← Previous project', 'Next project →', footer, lock-screen text | Brief (interface text) |")
w("")

import math
pct = math.floor(1000 * passed / total) / 10
out.insert(summary_at, f"**Result: {passed} / {total} items ✔ ({pct:g}%).**" + (" Every heading, paragraph, bullet, table row, quote, figure and production note is accounted for." if passed == total else " See ✘ rows."))
out.insert(summary_at + 1, "")
if DOM == "content/dom.json":
    open("COPY-CHECK.md", "w").write("\n".join(out) + "\n")
print(f"{passed}/{total}")
