"""Extract Yasmin's copy, verbatim and in order, into content/copy.json.

Run from yasmin/:  python3 tools/extract_copy.py
content/copy.json is the single source for the Round 3 pages and for
COPY-CHECK.md, so the site and the checklist can never drift apart.

Only mechanical clean-up is applied (listed in COPY-INVENTORY.md):
  - the lines of one paragraph or bullet are joined with a single space
    (a URL broken across two lines is joined with no space);
  - bullet glyphs, zero-width spaces and trailing spaces are removed;
  - runs of spaces inside a line become one space (HTML does this anyway).
Words, spelling, punctuation and capitalisation are never changed.
"""
import json, re
import pymupdf, docx

PDF = "source/CASE_STUDY-Yasmin_Bajwa.pdf"
DOCX = "source/Instructions_About_Me.docx"
ZW = "​"


def clean(t):
    return re.sub(r" {2,}", " ", t.replace(ZW, "").replace("●", "")).strip()


# ------------------------------------------------------------ 1. lines + figures, in reading order
lines = []
fig = 0
seen = set()
for pi, page in enumerate(pymupdf.open(PDF)):
    items = []
    for b in page.get_text("dict")["blocks"]:
        if b["type"] != 0:
            continue
        for l in b["lines"]:
            spans = [s for s in l["spans"] if s["text"].replace(ZW, "").strip()]
            if not spans:
                continue
            raw = "".join(s["text"] for s in l["spans"])
            items.append(dict(p=pi + 1, y=round(l["bbox"][1]), x=round(l["bbox"][0]), size=round(spans[0]["size"]),
                              bold=all("Bold" in s["font"] for s in spans),
                              anybold=any("Bold" in s["font"] for s in spans),
                              italic=any("Italic" in s["font"] for s in spans),
                              bullet="●" in raw, t=clean(raw)))
    for info in sorted(page.get_image_info(xrefs=True), key=lambda i: (i["bbox"][1], i["bbox"][0])):
        if info["xref"] and info["xref"] not in seen:
            seen.add(info["xref"]); fig += 1
            items.append(dict(p=pi + 1, y=round(info["bbox"][1]), x=round(info["bbox"][0]), fig=fig))
    lines += sorted(items, key=lambda r: (r["y"], r["x"]))

# ------------------------------------------------------------ 2. group lines into units
BUL_X = {90: 1, 106: 1, 138: 2, 148: 2, 170: 3}
CONT_X = {108, 156, 166}


def style(l):
    if "fig" in l:
        return "fig"
    if l["bullet"]:
        return "li"
    if l["bold"] and l["size"] >= 17:
        return "big"
    if l["bold"] and l["size"] >= 13:
        return "mid"
    if l["bold"]:
        return "b12"
    return "p"


units = []
for l in lines:
    s = style(l)
    u = units[-1] if units else None
    same_page_gap = u and u["p_last"] == l["p"] and 0 < l["y"] - u["y_last"] <= 21
    next_page_top = u and l["p"] == u["p_last"] + 1 and l["y"] <= 75
    if u and s == "li" and False:
        pass
    cont = False
    if u and s != "fig" and u["style"] != "fig":
        if u["style"] == "li" and not l["bullet"] and l["x"] in CONT_X and (same_page_gap or next_page_top):
            cont = True                                   # wrapped bullet line
        elif u["style"] == s and s in ("p", "big") and l["x"] == 72 and u["x"] == 72 and (same_page_gap or (next_page_top and s == "p" and not u["t"].endswith((".", ":", "?", "!", "\u201d")) and not l["t"].startswith("\u201c"))):
            cont = True                                   # wrapped paragraph / 2-line heading
        elif u["style"] == "big" and s == "big" and u["size"] == l["size"] and u["p_last"] == l["p"] and 0 < l["y"] - u["y_last"] <= 36:
            cont = True                                   # 2-3 line heading, title or 24pt note
        elif u["style"] == "p" and s == "b12" and l["x"] == 72 and u["x"] == 72 and same_page_gap and not u["t"].endswith(":"):
            cont = True; u.setdefault("bold_parts", []).append(l["t"])   # bold words inside a paragraph
        elif u["style"] == "b12" and s == "b12" and l["x"] == 72 and same_page_gap and u["t"].lower().startswith("how might we "):
            cont = True                                   # 2-line bold HMW
        elif u["style"] == "mid" and s == "mid" and same_page_gap and u["t"].lower().startswith("how might we "):
            cont = True
        elif u["style"] == "b12" and s == "p" and l["x"] in CONT_X:
            cont = True
    if cont:
        joiner = "" if u["t"].endswith(("usp=dri", "usp=share_lin")) else " "
        if l["bullet"] is False and u["style"] == "li" and u["t"].endswith("used") and l["t"] == "":
            joiner = ""
        u["t"] = (u["t"] + joiner + l["t"]).strip()
        u["p_last"], u["y_last"] = l["p"], l["y"]
        if l.get("italic"):
            u["italic"] = True
        continue
    units.append(dict(style=s, t=l.get("t", ""), fig=l.get("fig"), p=l["p"], y=l["y"], x=l["x"],
                      p_last=l["p"], y_last=l["y"], level=BUL_X.get(l["x"], 1) if s == "li" else None,
                      italic=l.get("italic", False), size=l.get("size")))

# URL lines that start a new unit because the URL is in regular weight
merged = []
for u in units:
    if merged and u["t"].startswith(("https://drive", "ve_link", "k")) and merged[-1]["t"].startswith(("ADD ", "https://drive")) and u["style"] == "p" and len(u["t"]) < 120:
        prev = merged[-1]
        prev["t"] = prev["t"] + ("" if prev["t"].endswith(("usp=dri", "usp=share_lin")) else " ") + u["t"]
        continue
    merged.append(u)
units = merged

# ------------------------------------------------------------ 3. types
NOTE = re.compile(r"^(INSERT |ADD |USE PDF VERSION)")
TITLES = {(1, 73): "room01", (13, 531): "room02", (24, 208): "room03", (30, 437): "room04"}
CHAPTER_LIKE = {"Results & Impact", "Ongoing Evaluation", "Reflection"}
out = {k: [] for k in TITLES.values()}
room = None
for u in units:
    key = (u["p"], u["y"])
    if key in TITLES:
        room = TITLES[key]
        out[room].append(dict(type="title", text=u["t"], src=f"p{u['p']}"))
        continue
    t = u["t"]
    if u["style"] == "fig":
        it = dict(type="figure", doc=u["fig"])
    elif NOTE.match(t):
        it = dict(type="note", text=t)
    elif u["style"] == "li":
        it = dict(type="li", level=u["level"], text=t)
    elif u["style"] == "big" and (u["size"] >= 19 or t in CHAPTER_LIKE):
        it = dict(type="h2", text=t)
    elif u["style"] == "big":
        it = dict(type="h3", text=t)
    elif t in ("Role", "Methods"):
        it = dict(type="label", text=t)
    elif u["style"] == "mid" or (u["style"] == "b12" and t in CHAPTER_LIKE):
        it = dict(type="h2", text=t, promoted=True) if t in CHAPTER_LIKE else dict(type="h3", text=t)
    elif u["style"] == "b12":
        if t.lower().startswith("how might we ") and len(t) > 30:
            it = dict(type="hmw", text=t)
        elif t.startswith("“"):
            it = dict(type="quote", text=t)
        else:
            it = dict(type="h4", text=t)
    else:
        it = dict(type="quote", text=t) if t.startswith("“") else dict(type="p", text=t)
    if u.get("bold_parts"):
        it["bold_parts"] = u["bold_parts"]
    it["src"] = f"p{u['p']}"
    out[room].append(it)

# ------------------------------------------------------------ 4. structural fixes (never wording)
for r in out:
    items, new, i = out[r], [], 0
    while i < len(items):
        it = items[i]
        if it["type"] == "label":               # Role / Methods + value -> one meta row
            new.append(dict(type="meta", label=it["text"], text=items[i + 1]["text"], src=it["src"])); i += 2; continue
        new.append(it); i += 1
    out[r] = new

# Room 01: the visitor-type table on p3 (3 columns in her doc)
r1 = out["room01"]
a = next(i for i, it in enumerate(r1) if it.get("text", "").startswith("Visitor Type"))
b = next(i for i, it in enumerate(r1) if it.get("text", "").startswith("Each simulated visitor"))
out["room01"] = r1[:a] + [dict(type="table", src="p3", head=["Visitor Type", "Characteristics", "Distribution"], rows=[
    ["Strollers", "Browse most exhibits with moderate viewing time", "60%"],
    ["Studiers", "Read interpretation thoroughly and spend longer in each room", "10%"],
    ["Streakers", "Move quickly through the exhibition with minimal stopping", "30%"]])] + r1[b:]

# ------------------------------------------------------------ 5. About (docx)
about = []
for p in docx.Document(DOCX).paragraphs:
    t = re.sub(r" {2,}", " ", p.text).strip()
    if not t:
        continue
    if t == "Portfolio Website Direction":
        about.append(dict(type="brief_h", text=t))
    elif t.startswith(("I want my portfolio", "The landing page should", "For the visual direction")):
        about.append(dict(type="brief", text=t))
    elif t == "About Me":
        about.append(dict(type="h2", text=t))
    elif t.startswith("Highlight these 4 skills"):
        about.append(dict(type="instruction", text=t))
    elif t.startswith(("Hi!", "By blending")):
        about.append(dict(type="p", text=t))
    else:
        about.append(dict(type="skill", text=t))

json.dump(dict(about=about, **out), open("content/copy.json", "w"), indent=1, ensure_ascii=False)
print({k: len(v) for k, v in out.items()}, "about", len(about))
