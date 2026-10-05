"""SQUARESPACE-BUILD-CHECKLIST.md: the build as tick-boxes, generated from the rendered prototype.

Run from yasmin/:
    node tools/checklist_extract.js > content/checklist-blocks.json
    python3 tools/build_checklist.py
The text to paste is read from the built pages (textContent, so her source spelling, not the uppercased display),
the Fluid Engine column spans from the rendered layout (24 columns at 1440, 8 at 390), image files and box ratios
from the DOM. Section settings, Site Styles and the custom CSS follow SQUARESPACE-BUILD-NOTES.md, corrected to
the current build. Palette: mono (the built one); THEMES.md and the notes give the values for the other four.
"""
import collections, json, os, re

D = json.load(open("content/checklist-blocks.json"))
INK, HAIR = "rgb(17, 17, 17)", "rgba(17, 17, 17, 0.14)"
OUT = []
w = OUT.append
STATS = collections.Counter()

# ---------------------------------------------------------------- URLs (Squarespace)
SLUG = {"room-01-jackson-home": "/projects-private/jackson-home", "room-02-power-energy": "/projects-private/power-energy",
        "room-03-rhode-island": "/projects-private/rhode-island", "room-04-littelfuse": "/projects-private/littelfuse"}


def url(h):
    if not h:
        return h
    h = re.sub(r"\?theme=[\w-]+", "", h)   # the prototype's switcher adds this at run time
    if h.startswith(("mailto:", "tel:", "http")):
        return h
    if h == "#linkedin":
        return f"her LinkedIn profile URL (**pending**: the client hasn't supplied it, {fl('pending', 'Homepage')}); until then paste the placeholder and leave it unlinked"
    if h == "#top":
        return "`#` (back to top)"
    m = re.match(r"^(index|projects|room-0\d-[\w-]+)\.html(#.*)?$", h)
    if m:
        base = {"index": "/", "projects": "/projects"}.get(m.group(1)) or SLUG[m.group(1)]
        return f"`{base}{m.group(2) or ''}`"
    if h.startswith("#"):
        return f"`{h}` (anchor on this page)"
    return f"`{h}`"


# ---------------------------------------------------------------- flags (Squarespace can't do it exactly)
FLAGS = collections.OrderedDict()


NUM = {"next": 1}


def F(key, title, native):
    FLAGS[key] = {"title": title, "native": native, "where": [], "n": None}


F("size", "Text sizes between Squarespace's seven styles",
  "Site Styles gives Heading 1–4 and Paragraph 1–3, one size each (plus a mobile size). The prototype uses a few sizes in between "
  "(listed with each block as \"prototype: Npx\"). **Nearest native:** the style named on the block. If her editor offers a size control "
  "on selected text (**verify**: it depends on the account's editor version), set the prototype size there; otherwise accept the style's size.")
F("statsnum", "The stats numbers (\"60%\", \"10%\", \"30%\") are 96px Inter Tight",
  "No native style is a 96px sans. **Nearest native:** Heading 2 (80px Instrument Serif). The numbers then read in the heading face; that is the only visible change.")
F("sansname", "Inter Tight at 24px (stats names, \"How might we…\" lines at 28px)",
  "Heading 4 is Instrument Serif 24px; Paragraph 1 is Inter Tight 40px. **Nearest native:** Heading 4 for the stats names; Paragraph 1 for the 28px "
  "\"How might we…\" lines and the italic Reflection paragraphs (28px is Paragraph 1's mobile size).")
F("quote", "Her three quoted visitor stories have a 1px rule on the left and 20px italic text",
  "**Nearest native:** a **Quote** block (Squarespace styles it itself; no left rule) or Paragraph 2 in italic with a **Line** block set vertical (**verify** "
  "her editor offers vertical Line blocks). Keep the bold lead-in words bold.")
F("padding", "Exact section spacing in px",
  "Fluid Engine sections have no px padding field: the space above and below comes from the section's **height** setting (Small / Medium / Large / Custom) and the "
  "empty grid rows above the first block. **Nearest native:** start at the height named on the section, then add or remove empty rows in the editor until the gap "
  "matches the px given (check in Preview at 1440 and on a phone).")
F("rowlink", "Whole project rows are one link in the prototype",
  "Fluid Engine can't group blocks into one link. **Nearest native:** link the title text and the logo image block to the project page (both listed).")
F("rowhover", "Row hover: the logo tile darkens when the pointer is anywhere on the row",
  "No group hover in Fluid Engine. **Nearest native:** CSS rule 19 darkens the tile when the pointer is on the tile itself.")
F("overlap", "The case-study meta table overlaps the cover photo's bottom edge (Rooms 01, 02)",
  "A block can't extend outside its section. **Nearest native:** put the white Shape block and the meta text in the **cover section's bottom rows**, so the card sits on "
  "the photo, flush with its bottom edge; on mobile, below the title.")
F("covermobile", "On phones the cover title drops below the photo, in ink",
  "Text placed on a section background stays on it on mobile. **Nearest native:** keep the title on the photo on mobile (white, on the 38% overlay); in the mobile "
  "layout move it to the bottom rows. The meta table follows below.")
F("mobilemenu", "The prototype keeps Projects · About · Contact inline at 390px",
  "Squarespace headers switch to a menu icon on mobile. **Nearest native:** the mobile menu (*Edit Site Header → Mobile*), with the same three links.")
F("slideshow", "The Snippets slideshow sits beside the text (cols 13–24), 4:5, with arrows, dots and a 400ms crossfade",
  "**Nearest native:** a **Gallery block** set to Slideshow inside the same section (**verify** her plan offers the Gallery block in Fluid Engine). If it doesn't, "
  "use a separate **Gallery section → Slideshow: Simple** directly below the text (it can't sit beside it). Transition timing and dots are Squarespace's own (**verify**).")
F("panelsfull", "The discipline panels are four equal full-bleed columns, 60% of the screen tall, with hairlines between",
  "**Nearest native:** a full-width section (content width **Full**) with four Image blocks at cols 1–6 / 7–12 / 13–18 / 19–24 set to **Fill**. The 45% darkening and "
  "the hover use CSS rules 15–16. Fluid Engine's own gaps may leave a thin gap between panels instead of a hairline (**verify**; set block spacing to 0 if offered).")
F("lockwrong", "Wrong password: the prototype says \"Incorrect password.\" under the field",
  "Squarespace shows its own message and wording. **Nearest native:** its message, restyled by CSS rule 10 (14px, 62% ink, no shake).")
F("locklink", "The lock screen's \"No password? Email Yasmin →\" is a link",
  "Lock-screen text fields may not accept links (**verify**). **Nearest native:** write the line with her address in it: \"No password? Email yasminbajwa248@gmail.com\".")
F("lockcss", "Lock-screen CSS class names",
  "The lock screen has no settings for the field rule, button fill or error style; CSS rules 7–14 do it, with class names taken from community examples, "
  "**not verified**. Check each in the browser inspector on her site; delete any that match nothing.")
F("placeholder", "Littelfuse wireframes: a placeholder until she exports them from Adobe XD",
  "**Don't publish the grey placeholder.** Leave that figure out until the export arrives (ASSET-GAPS.md); the caption numbering after it stays as listed.")
F("pending", "Pending content from the client",
  "LinkedIn URL (Contact), Littelfuse wireframes (Room 04), and confirmation for snippet 21 (the handwritten note, last in the slideshow). Build the rest; fill these when they arrive.")
F("caption", "Captions above the image (the Strip module) and \"Running time\" lines",
  "Image block captions sit below. **Nearest native:** a Paragraph 3 **Text** block above each image in the strip; for videos, the caption and running time go in a Text block beside the video (listed).")
F("vertical", "Vertical videos are capped at 78% of the screen height and centred in cols 1–16",
  "**Nearest native:** size the Video block by hand: about cols 5–12 at desktop, centred, so it isn't taller than the screen.")


def fl(key, where):
    f = FLAGS[key]
    if f["n"] is None:
        f["n"] = NUM["next"]; NUM["next"] += 1
    f["where"].append(where)
    return f"F{f['n']}"


# ---------------------------------------------------------------- styles
DESIGN = {77.8: 80, 30.2: 32, 54.7: 56, 86.4: 96}


def style_of(L, where):
    st = L["style"]
    size = DESIGN.get(st["size"], st["size"])
    size = int(size) if float(size).is_integer() else size
    it = " italic" if st["italic"] else ""
    t = (L.get("text") or "").strip()
    if st["serif"]:
        if size >= 120: return "Heading 1" + it
        if size >= 70: return "Heading 2" + it
        if size >= 40: return "Heading 3" + it
        if size >= 29: return f"Heading 3{it} (prototype: {size}px, {fl('size', where)})"
        if size >= 25: return f"Heading 4{it} (prototype: {size}px, {fl('size', where)})"
        if size >= 22: return "Heading 4" + it
        return f"Heading 4{it} (prototype: {size}px, weight 500; nearest Paragraph 3 if 14px isn't possible, {fl('size', where)})"
    if st["upper"] and size <= 12.5:
        return "Paragraph 3" + ("" if size == 11 else f" (prototype: {size}px, tracking 0.24em, {fl('size', where)})")
    if size >= 80: return f"Heading 2 (prototype: {size}px Inter Tight, {fl('statsnum', where)})"
    if 38 <= size <= 42: return "Paragraph 1" + it
    if 26 <= size <= 30: return f"Paragraph 1{it} (prototype: {size}px, {fl('sansname', where)})"
    if 23 <= size <= 25: return f"Heading 4 (prototype: Inter Tight {size}px, {fl('sansname', where)})"
    if 19 <= size <= 21 and st["italic"]: return f"Paragraph 2 italic (prototype: {size}px, {fl('quote', where)})"
    if 19 <= size <= 21: return f"Paragraph 2{' bold' if st['weight'] >= 500 else ''} (prototype: {size}px, {fl('size', where)})"
    if 16.5 <= size <= 17.5: return "Paragraph 2" + it
    if re.fullmatch(r"\d\d", t): return f"Paragraph 3 (prototype: {size}px, {fl('size', where)})"
    return f"Paragraph 2 (prototype: {size}px, {fl('size', where)})"


def cols(b, m):
    mc = m["cols"]
    if b.get("kind") == "text" and mc[1] - mc[0] >= 5 and mc[0] <= 2:   # a stacked text block on a phone: the full width
        mc = [1, 8]
    m = dict(m, cols=mc)
    bc = b["cols"]
    if b.get("kind") == "text" and bc[1] - bc[0] < 2:   # a very short line (a link, a number): give the block room
        bc = [21, 24] if bc[1] == 24 else [bc[0], bc[0] + 3]
        if m["cols"][1] - m["cols"][0] < 2:
            m = dict(m, cols=[5, 8] if m["cols"][1] == 8 else [m["cols"][0], m["cols"][0] + 3])
    b = dict(b, cols=bc)
    a = f"cols {b['cols'][0]}–{b['cols'][1]}" if b["cols"][0] != b["cols"][1] else f"col {b['cols'][0]}"
    z = f"{m['cols'][0]}–{m['cols'][1]}" if m["cols"][0] != m["cols"][1] else f"{m['cols'][0]}"
    return f"{a} · mobile {z}"


RATIOS = [(1, 1), (4, 5), (5, 4), (3, 4), (4, 3), (2, 3), (3, 2), (16, 9), (9, 16), (16, 10), (16, 7), (9, 32), (21, 9), (2, 1), (1, 2)]


def ratio(r):
    best = min(RATIOS, key=lambda q: abs(q[0] / q[1] - r) / r)
    if abs(best[0] / best[1] - r) / r < 0.02:
        return f"{best[0]}:{best[1]}"
    return f"{r:.2f}:1"


def fence(lines, indent="  "):
    out = [indent + "```text"]
    out += [indent + x for x in lines]
    out.append(indent + "```")
    return out


def list_lines(items, depth=0):
    out = []
    for it in items:
        out.append("    " * depth + it["text"])
        if it.get("sub"):
            out += list_lines(it["sub"], depth + 1)
    return out


def rule_note(b):
    notes = []
    for r in b.get("rules", []):
        kind = "1px ink" if r["color"] == INK else ("1px, 14% ink" if r["color"] == HAIR else r["color"])
        notes.append(f"**Line** block {'above' if r['side'] == 'top' else 'below'} ({kind}, same columns)")
    return notes


def asset(src):
    return "site/" + src if src and not src.startswith("site/") else src


def plate(src):
    stem = os.path.splitext(os.path.basename(src))[0]
    return f"site/assets/img/logos/plate-{stem}.png"


REF = {"n": 0}


def ref(prefix):
    REF["n"] += 1
    return f"{prefix}.{REF['n']}"


def text_block(prefix, b, m, where, extra=""):
    if b.get("index"):
        STATS["text"] += 1
        head = (f"- [ ] **{ref(prefix)} Text** · {cols(b, m)} · Paragraph 2 (prototype: 14px, {fl('size', where)}) · one line that wraps; "
                "**Line** blocks above and below (1px ink) · numbers in 62% ink, titles in ink")
        notes = "  links: " + " · ".join(f"\"{x['title']}\" → `{x['href']}`" for x in b["index"])
        return [head, notes] + fence(["   ".join(f"{x['no']} {x['title']}" for x in b["index"])])
    ls = b["lines"]
    styles = []
    body = []
    links, ital, bold = [], [], []
    for L in ls:
        if L.get("items") is not None:
            styles.append(("Numbered list" if L["ordered"] else "Bulleted list") + " in " + style_of(L, where))
            body += list_lines(L["items"])
            STATS["text"] += 1
        else:
            if not L["text"]:
                continue
            styles.append(style_of(L, where))
            body.append(L["text"])
            STATS["text"] += 1
        links += L.get("links", []) or []
        ital += L.get("italic_parts", []) or []
        bold += L.get("bold_parts", []) or []
    if not body:
        return []
    head = f"- [ ] **{ref(prefix)} Text** · {cols(b, m)} · " + (" → ".join(styles) if len(styles) > 1 else styles[0])
    if len(styles) > 1:
        head += " (one block, one line per style)"
    if b.get("centred"):
        head += " · centred"
    if extra:
        head += " · " + extra
    notes = rule_note(b)
    if ital:
        notes.append("italic: " + ", ".join(f"\"{x}\"" for x in ital))
    if bold:
        notes.append("bold: " + ", ".join(f"\"{x}\"" for x in bold))
    for t, h in links:
        if h:
            notes.append(f"link \"{t}\" → {url(h)}")
    if b.get("href") and not links and b.get("pn"):
        notes.append(f"link the whole text → {url(b['href'])}")
    elif b.get("href") and not links and any(L["tag"] in ("h2", "h3") for L in ls):
        notes.append(f"link the title → {url(b['href'])}")
    if any(L.get("items") is not None and any(i.get("sub") for i in L["items"]) for L in ls):
        notes.append("indented lines are a nested list (Tab)")
    out = [head]
    if notes:
        out.append("  " + " · ".join(notes))
    return out + fence(body)


def image_block(prefix, b, m, where, logo=False, fit=None, href=None):
    src = b["src"]
    STATS["image"] += 1
    up = plate(src) if logo else asset(src)
    if fit is None:
        fit = "Fit" if ("/tiles/" in src or logo) else "Fill"
    r = ratio(b["ratio"])
    head = f"- [ ] **{ref(prefix)} Image** · {cols(b, m)} · upload `{up}` · block shape **{r}** · **{fit}**"
    notes = []
    if logo:
        notes.append("transparent 1200×800 plate, logo already sized inside it; ground and hover come from CSS rules 18–19")
    if "/tiles/" in src:
        notes.append("the tile already holds the light ground and padding, so nothing is cropped")
    if b.get("full"):
        notes.append(f"lightbox on (opens the tile; full-size original: `{asset(b['full'])}`)")
    if href:
        notes.append(f"clickthrough link → {url(href)} (instead of the lightbox)")
    notes.append(f"alt text: \"{b['alt']}\"" if b.get("alt") else "alt text: none (decorative)")
    out = [head, "  " + " · ".join(notes)]
    if b.get("caption"):
        cap_style = "Paragraph 3"
        out.append(f"  caption (**Caption: below**, {cap_style}):")
        out += fence([b["caption"]], "  ")
        STATS["caption"] += 1
    return out


def video_block(prefix, b, m, where):
    STATS["video"] += 1
    head = f"- [ ] **{ref(prefix)} Video** · cols {b['video_cols'][0]}–{b['video_cols'][1]} · mobile {m['cols'][0]}–{m['cols'][1]} · upload `{asset(b['src'])}` · thumbnail `{asset(b['poster'])}` · controls on, autoplay off"
    if b.get("vertical"):
        head += f" · vertical video ({fl('vertical', where)})"
    cap = f"- [ ] **{ref(prefix)} Text** · cols {b['caption_cols'][0]}–{b['caption_cols'][1]} · mobile 1–8 (below the video) · bottom-aligned · **Line** block above (1px ink) · Paragraph 3 → Paragraph 3"
    return [head, cap] + fence([b["caption"], b["runtime"]])


MODS = {"pair": "Plate pair: a wide image (16 cols) beside a tall one (8 cols), tops and bottoms aligned; on mobile stacked in the order listed.",
        "board": "Board 2×2: four image blocks, cols 1–12 / 13–24, all 1:1 (or a Gallery section → Grid: Simple, 2 columns, 1:1, 24px spacing); one column on mobile.",
        "one3": "Board 1+3: one large image (cols 1–16) as tall as the three small ones stacked in cols 17–24; on mobile stacked, large first.",
        "strip": "Strip: tiles side by side at the tile ratio, captions **above** (F); two columns on mobile.",
        "full": "Full plate: one image block across cols 1–24.",
        "video": "Video panel: the video in cols 1–16, its caption and running time in cols 17–24 under a Line."}


def blocks_md(prefix, sec, msec, where):
    out = []
    bs, ms = sec["blocks"], msec["blocks"]
    assert len(bs) == len(ms), (where, len(bs), len(ms))
    refs = []
    for i, (b, m) in enumerate(zip(bs, ms)):
        refs.append(f"{prefix}.{REF['n'] + 1}")
        if b["kind"] == "video" and not b.get("module_start"):
            b = dict(b, module_start={"mod": "video", "mt": b.get("mt", 0)})
        if b.get("module_start"):
            mod = b["module_start"]["mod"]
            desc = MODS[mod]
            if mod == "strip":
                desc = desc.replace("(F)", f"({fl('caption', where)})")
            out.append(f"- [ ] **Module · {desc.split(':')[0]}**: {desc.split(':', 1)[1].strip()} Space above: {b['module_start']['mt']}px. "
                       "Build it once, save it (heart icon), reuse it.")
        k = b["kind"]
        if k == "text":
            out += text_block(prefix, b, m, where)
        elif k == "button":
            STATS["button"] += 1
            out.append(f"- [ ] **{ref(prefix)} Button** · {cols(b, m)} · Primary (outline) · links to {url(b.get('href'))}")
            out += fence([b["lines"][0]["text"]])
        elif k == "image":
            out += image_block(prefix, b, m, where, logo=b.get("role") == "logo", href=b.get("href") or sec.get("href"))
        elif k == "video":
            out += video_block(prefix, b, m, where)
        elif k == "placeholder":
            out.append(f"- [ ] **{ref(prefix)} Placeholder: leave out** · {cols(b, m)} · {fl('placeholder', where)} · {fl('pending', where)}. "
                       f"The prototype's grey box reads \"{b['label']}\". Its caption, for when the export arrives:")
            out += fence([b["caption"]])
        elif k == "slideshow":
            out += slideshow(prefix, b, m, where)
        elif k == "cover":
            out += cover(prefix, b, m, where)
        else:
            out.append(f"- [ ] {k} (unmapped)")
    # mobile order, when it differs
    order = sorted(range(len(ms)), key=lambda j: (round(ms[j]["box"]["y"]), ms[j]["box"]["x"]))
    layered = any(b.get("panel") for b in bs)
    if order != list(range(len(ms))) and len(ms) > 1 and not layered:
        out.append(f"- [ ] **Mobile order** (drag blocks in the mobile view): " + ", ".join(refs[j] for j in order))
    return out


def slideshow(prefix, b, m, where):
    STATS["image"] += len(b["slides"])
    out = [f"- [ ] **{ref(prefix)} Gallery block → Slideshow** · {cols(b, m)} · aspect ratio **4:5** · autoplay **on, 5 s** · arrows on · dots on if offered · captions off · lightbox off ({fl('slideshow', where)})",
           f"  Upload in this order ({len(b['slides'])} photos; the five landscape ones are already letterboxed to 4:5 so they show whole):"]
    for i, s in enumerate(b["slides"], 1):
        last = " · **publish only once the client confirms it** (" + fl("pending", where) + ")" if s["src"].endswith("snippet-21.jpg") else ""
        out.append(f"  - [ ] {i:02d} `{asset(s['src'])}` · alt \"{s['alt']}\"{last}")
    return out


def cover(prefix, b, m, where):
    return [f"- [ ] **{ref(prefix)} Section background image** · upload `{asset(b['src'])}` · section **content width Full**, height **Large** (the photo is 16:7: about 630px tall at 1440) · "
            f"background **overlay #111111 at 38%** · focal point centre · {fl('covermobile', where)}"]


def spacing(sec, msec):
    return f"space above {sec['pt']}px / below {sec['pb']}px at 1440 (mobile {msec['pt']} / {msec['pb']})"


# ---------------------------------------------------------------- page 0: Site Styles, header, footer (once)
def site_styles():
    w("## Page 0 · Site Styles, header and footer (set once)")
    w("")
    w("Set these before building any page; every later page assumes them. Values are the built palette (**mono**). If the client picks another palette, change only the colour rows (THEMES.md and the build notes' *Site Styles per theme* list the values).")
    w("")
    w("**Fonts** (*Site Styles → Fonts*)")
    w("- [ ] Headings: **Instrument Serif** (Google; **verify** it is in her picker, otherwise add it as a custom font). One weight (400) plus italic: emphasis in headings is italic, never bold.")
    w("- [ ] Paragraphs, buttons, navigation, captions: **Inter Tight** 400 (500 for labels and the \"About Me\" kicker).")
    w("")
    w("**Type scale** (*Site Styles → Fonts → each style*; desktop / mobile)")
    w("")
    for row in [("Heading 1", "Instrument Serif 400", "140px", "64px", "0.92", "−0.01em", "\"Hi, I’m Yasmin.\""),
                ("Heading 2", "Instrument Serif 400", "80px", "40px", "1.02", "−0.01em (0 on mobile)", "Page and cover titles, \"Projects\", the contact line"),
                ("Heading 3", "Instrument Serif 400", "46px", "34px", "1.08", "0", "Chapter titles, \"Snippets About My Life\"; panel names and row titles (prototype 34 / 32px)"),
                ("Heading 4", "Instrument Serif 400", "24px", "24px", "1.3", "0", "Her sub-headings, prev/next titles; italic for \"How might we…\""),
                ("Paragraph 1", "Inter Tight 400", "40px", "28px", "1.2", "−0.015em", "The Snippets statement"),
                ("Paragraph 2", "Inter Tight 400", "17px", "16px", "1.6", "0", "All her body text"),
                ("Paragraph 3", "Inter Tight 500, **uppercase**", "11px", "11px", "1.45", "0.08em", "Labels, captions (\"FIG. 03 — …\"), \"PASSWORD PROTECTED\"")]:
        w(f"- [ ] **{row[0]}** · {row[1]} · **{row[2]}** desktop / **{row[3]}** mobile · line height {row[4]} · tracking {row[5]} · {row[6]}")
    w("")
    w("**Colours** (*Site Styles → Colours*, mono)")
    w("- [ ] Palette: `#FFFFFF` (white) · `#F4F3F0` (stone) · `#111111` (ink). No accent colour.")
    w("- [ ] Section theme **White**: background `#FFFFFF`, text `#111111`, links `#111111` underlined.")
    w("- [ ] Section theme **Stone**: background `#F4F3F0`, text `#111111` (Snippets, Contact, each Reflection).")
    w("- [ ] Section theme **Ink**: background `#111111`, text `#FFFFFF` (the discipline panels, so their names are white without CSS).")
    w("- [ ] Paragraph 3 colour: `#6B6B6B` (62% ink; 55% fails contrast at 11px). Image captions get the same through CSS rule 2.")
    w("")
    w("**Buttons** (*Site Styles → Buttons → Primary*)")
    w("- [ ] Style **outline**, 1px `#111111`, **square** corners (radius 0), Inter Tight 14px, tracking 0.02em, padding about 14 × 22px. Hover: filled ink, white text.")
    w("")
    w("**Spacing** (*Site Styles → Spacing*; **verify** the names in her account)")
    w("- [ ] Page max width **1600px**; site margins **48px** desktop, **20px** mobile (the prototype's margin is 3.4% of the width, between those).")
    w("- [ ] Fluid Engine gap between blocks **16px**. The desktop grid is **24 columns**, the mobile grid **8**: every block below gives both.")
    w(f"- [ ] Section spacing target: **144px** top and bottom at 1600px and wider (130px at 1440), **88px** on phones. Fluid Engine has no px field for this ({fl('padding', 'Site Styles')}).")
    w("")
    w("**Animations, images**")
    w("- [ ] *Site Styles → Animations*: **Fade**, speed **Slow**. No parallax, no scroll effects.")
    w("- [ ] Image blocks by default: clickthrough **Lightbox**, caption **below**, no border, no shadow, corner radius **0** (CSS rule 6 enforces 0).")
    w("")
    w("**Pages and navigation** (create them empty now; each page below fills one)")
    w("- [ ] **Home**: regular page, set as homepage.")
    w("- [ ] **Projects**: regular page, URL `/projects`, in the navigation as \"Projects\".")
    w("- [ ] **Case studies**: Portfolio page, URL `/projects-private`, **not linked** (not in the navigation). Its four project pages are built on pages 1–5.")
    w("- [ ] Navigation links: **About** → `/#snippets`, **Contact** → `/#contact` (anchor links to Home sections).")
    w("")
    w("**Header** (*Edit Site Header*)")
    w("- [ ] Layout: site title left, navigation right. Site title as text: \"Yasmin Bajwa\", Inter Tight 15px. Navigation 15px, gap about 28px; the current page underlined.")
    w(f"- [ ] Style **Solid**, theme **White**, a 1px rule under it (14% ink): the header border setting if her template has one, else CSS rule 1. Mobile: the menu icon ({fl('mobilemenu', 'Header')}).")
    w("- [ ] On the two photo-cover case studies (Rooms 01, 02) the header sits over the photo with white text: *header → transparent over the first section* (**verify** per-page header overlay).")
    w("")
    w("**Footer** (*Edit Footer*, one Fluid Engine section shared by every page)")
    foot = D["index"]["1440"]["sections"][-1]["blocks"]
    w("- [ ] Theme **White**; a **Line** block across the top (1px, 14% ink); 28px above and below the text.")
    w(f"- [ ] **Text** · cols 1–8 · mobile 1–4 · Paragraph 2 (prototype: 13px, 62% ink, {fl('size', 'Footer')}):")
    OUT.extend(fence([foot[0]["lines"][0]["text"]]))
    w("- [ ] **Text** · cols 17–24, right-aligned · mobile 5–8 · Paragraph 2 (13px) · link → `#` (back to top), underlined:")
    OUT.extend(fence([foot[1]["lines"][0]["text"]]))
    w("")
    w("**Files**: everything to upload is in this repository under `yasmin/site/assets/` (paths below start at `site/`). The zip `yasmin-portfolio-prototype.zip` has the same files.")
    w("")


# ---------------------------------------------------------------- case-study pages
CASE_SEC = {
    "cover": ("Cover (photo)", "Blank section · content width **Full** · height **Large** · background image (below) · theme **Ink** text (white)"),
    "meta": ("Meta table on a white card", "**Same section as the cover**, in its bottom rows ({F})"),
    "dochead": ("Document header (title + meta table)", "Blank section · theme **White** · no background image"),
    "chindex": ("Chapter index", "Blank section · theme **White** · 1px ink Line blocks above and below the index"),
    "coverplate": ("FIG. 01 · the cover image, whole", "Same section as the chapter index (below it), or its own White section"),
    "chapter": ("Chapter", "Blank section · theme **White** · anchor link `{id}` (*Edit Section → Anchor*)"),
    "reflection": ("Reflection", "Blank section · theme **Stone** · anchor link `{id}` · text centred"),
    "pn": ("Previous / all / next", "Blank section · theme **White** · a 1px ink **Line** block across the top · 28px above, 40px below"),
    "foot": ("Footer", "Site footer (Page 0)"),
}


def case_page(pg, n, title):
    d, m = D[pg]["1440"], D[pg]["390"]
    full_title, title = title, title.split(" · ")[0]
    room = pg[:7]
    prefix = f"{n}"
    REF["n"] = 0
    w(f"## Page {n} · {full_title}")
    w("")
    w(f"- [ ] *Case studies → +* project page · title as below · URL slug `{SLUG[pg]}` · thumbnail: not needed (the Portfolio grid is never shown).")
    if n == 2:
        w("- [ ] Build this page **completely first**; save the cover, meta card, chapter index, each module, the Reflection and the prev/next section (heart icon → *My saved sections*). Pages 3–5 reuse them.")
    else:
        w("- [ ] Start from a **duplicate** of Room 01 (*Pages → ⋯ → Duplicate*, **verify**) or from the saved sections; replace every text and image with the ones below.")
    w("- [ ] Site Styles used: Heading 2–4, Paragraph 2–3, captions, Line blocks; module images; CSS rules 3–5 (lists) and 6 (corners).")
    w("")
    for si, (s, ms) in enumerate(zip(d["sections"], m["sections"])):
        sel = s["sel"]
        if sel.startswith("footer"):
            w(f"### {prefix}.{si + 1} · Footer")
            w("- [ ] Nothing to build: the site footer (Page 0).")
            w("")
            continue
        key = ("coverplate" if ".coverplate" in sel else "cover" if ".cover" in sel else "meta" if sel.startswith("div.meta") else "dochead" if ".dochead" in sel else "reflection" if "reflection" in sel else "chapter" if ".chapter" in sel else
               "pn" if sel.startswith("nav.pn") else "chindex")
        name, setting = CASE_SEC[key]
        setting = setting.replace("{id}", s.get("id") or "").replace("{F}", fl("overlap", title) if key == "meta" else "")
        heading = name
        if key in ("chapter", "reflection"):
            first = s["blocks"][0] if s["blocks"] else None
            t = None
            for b in s["blocks"]:
                for L in b.get("lines", []):
                    if L["tag"] in ("h2",) and L.get("text"):
                        t = L["text"]; break
                if t: break
            heading = f"{name} · {t}" if t and t != name else name
        w(f"### {prefix}.{si + 1} · {heading}")
        sp = "" if key in ("meta", "coverplate", "pn", "chindex", "cover") else f" · {spacing(s, ms)} ({fl('padding', title)})"
        REF["n"] = 0
        w(f"- [ ] **Section:** {setting}{sp}")
        if key == "chapter" and any(b.get("module") for b in s["blocks"]):
            w("- [ ] Images keep her order; captions are \"Fig. nn — …\" in Paragraph 3 (the style uppercases them).")
        if key == "pn":
            w("- [ ] **Line** block · cols 1–24 · 1px ink · at the top of the section")
        OUT.extend(blocks_md(prefix + "." + str(si + 1), s, ms, title))
        w("")


# ---------------------------------------------------------------- the document
w("# Squarespace build checklist · Yasmin Bajwa portfolio")
w("")
w("Tick each box as you build. Every block lists its **Fluid Engine columns** (desktop grid of 24, mobile grid of 8), its **Site Styles text style**, and the "
  "**exact text to paste** in a grey box (use the box's copy button; the text is her source spelling, so labels are typed in normal case and the Paragraph 3 style uppercases them). "
  "Images give the **file to upload** and the **shape to size the block to**.")
w("")
w("Generated from the current build (`site/`, the built **mono** palette) and SQUARESPACE-BUILD-NOTES.md by `tools/build_checklist.py`: the text, columns, files and ratios are read from the "
  "rendered pages, so they match the prototype exactly. Things Squarespace can't reproduce exactly are flagged **F1…F" + "{NFLAGS}" + "** with the nearest native setting, all listed on Page 10. Where this checklist and the build notes differ (the lock-screen font, the CSS numbering), the checklist follows the current build.")
w("")
w("**Build order, and why:** Page 0 (Site Styles, header, footer) → **Pages 1–5 the Case studies Portfolio** (its four project URLs are what Projects and Home link to; Room 01 is "
  "built first and its sections saved for reuse) → **Page 6 Lock Screen** (password on, tested) → **Page 7 Projects** → **Page 8 Homepage** (links to everything above; built last so "
  "no link points at a page that doesn't exist yet) → **Page 9 Custom CSS** (pasted last: two of its rules need block and section IDs from Home and Projects) → Page 10 flags, Page 11 final checks.")
w("")
w("**Notation:** `cols 9–20 · mobile 1–8` = the block spans desktop columns 9 to 20 and mobile columns 1 to 8. \"A → B\" in a text block = several lines in one block, each in its own style. "
  "\"Line block above\" = a 1px Line block directly above, same columns. Spacing is given in px at 1440 (and phone) widths.")
w("")
w("<!-- summary -->")
w("")
w('<div style="page-break-after: always"></div>')
w("")
site_styles()
w('<div style="page-break-after: always"></div>')
w("")
w("## Page 1 · Portfolio collection: Case studies")
w("")
w("- [ ] *Pages → +* **Portfolio** · title \"Case studies\" · URL `/projects-private` · **Not linked** (keep it out of the navigation).")
w("- [ ] Portfolio layout: any (the grid is never shown publicly: the password locks it with the projects, and Home and Projects link straight to each project page).")
w("- [ ] Inside it, four project pages in this order, built on Pages 2–5:")
for pg, t in [("room-01-jackson-home", "The Henry Ford Jackson Home Visitor Flow Simulation"), ("room-02-power-energy", "Designing an Interactive Museum Experience for Power & Energy"),
              ("room-03-rhode-island", "Rhode Island State COVID Vaccine App/401 Health App"), ("room-04-littelfuse", "Reimagining How Engineers Discover Littelfuse Products")]:
    w(f"  - [ ] `{SLUG[pg]}` · \"{t}\"")
w("- [ ] Password: **not yet**. Set it on Page 6 once all four pages are built (it protects the Portfolio and every project in it with one shared password).")
w("- [ ] Saved sections to create while building Room 01 (heart icon on each, name them like this): *Case · cover*, *Case · meta card*, *Case · chapter index*, *Case · chapter (text)*, "
  "*Module · plate pair*, *Module · board 2×2*, *Module · board 1+3*, *Module · strip*, *Module · full plate*, *Module · video panel*, *Case · reflection*, *Case · prev-next*.")
w("")
w('<div style="page-break-after: always"></div>')
w("")
for n, (pg, t) in enumerate([("room-01-jackson-home", "Room 01 · The Henry Ford Jackson Home Visitor Flow Simulation"),
                             ("room-02-power-energy", "Room 02 · Designing an Interactive Museum Experience for Power & Energy"),
                             ("room-03-rhode-island", "Room 03 · Rhode Island State COVID Vaccine App/401 Health App"),
                             ("room-04-littelfuse", "Room 04 · Reimagining How Engineers Discover Littelfuse Products")], 2):
    case_page(pg, n, t)
    w('<div style="page-break-after: always"></div>')
    w("")

# ---------------------------------------------------------------- lock screen
lk = D["private-view"]["1440"]["sections"]
lb = {i: b for i, b in enumerate(lk[1]["blocks"])}
T = lambda b: b["lines"][0]["text"]
w("## Page 6 · Lock Screen")
w("")
w("The lock screen is a settings panel, not a Fluid Engine page: no columns. *Case studies → Page settings → Password*, then *Lock Screen → Customize* (or *Design → Lock Screen*, **verify** which her account has).")
w("")
w("- [ ] **Password** on the *Case studies* Portfolio (*Page settings → General → Password*). One password protects all four projects; Squarespace can't give each project its own.")
w("- [ ] Layout **centred**; lock icon **off**; background image **none** (nothing from the case studies may show before the password).")
w(f"- [ ] Colours: background `#FFFFFF`, text `#111111`. Field rule, button fill and error style come from CSS rules 7–14 ({fl('lockcss', 'Lock Screen')}).")
w("- [ ] Site title / branding at the top (Inter Tight 15px), 24px from the top edge:")
OUT.extend(fence([T(lk[0]["blocks"][0])]))
w(f"- [ ] Headline (Heading 2 at 56px if the lock screen allows a size, else Heading 2; Instrument Serif 400; italic: \"{', '.join(lb[0]['lines'][0].get('italic_parts', []))}\"):")
OUT.extend(fence([T(lb[0])]))
w("- [ ] Description (Paragraph 2, 15px):")
OUT.extend(fence([T(lb[1])]))
w("- [ ] Password field label (Paragraph 3) and the button text:")
OUT.extend(fence([T(lb[2]), T(lb[4])]))
w(f"- [ ] Below the form, a link line (14px) ({fl('locklink', 'Lock Screen')}): link \"Email Yasmin →\" → `mailto:` her address with subject \"Portfolio access\":")
OUT.extend(fence([T(lb[6])]))
w(f"- [ ] Wrong password: Squarespace's own message ({fl('lockwrong', 'Lock Screen')}). The prototype's text, for reference only:")
OUT.extend(fence([T(lb[5])]))
w("- [ ] Footer line at the bottom (13px, 62% ink), 24px from the bottom edge:")
OUT.extend(fence([T(lk[2]["blocks"][0])]))
w("- [ ] **Test** in a private window: a project URL shows this screen; the wrong password shows the message without a shake; the right one opens all four projects.")
w("")
w('<div style="page-break-after: always"></div>')
w("")

# ---------------------------------------------------------------- projects page
pj, pm = D["projects"]["1440"]["sections"], D["projects"]["390"]["sections"]
REF["n"] = 0
w("## Page 7 · Projects")
w("")
w("A **regular page** (not the Portfolio grid: that locks with the password). One Blank section, theme **White**.")
w("- [ ] Site Styles used: Heading 2, Heading 4 (26px titles), Paragraph 2–3; logo plates (CSS rules 18–19); one section ID for rule 18 (Page 9).")
w(f"- [ ] **Section:** Blank · theme White · space above the title {pj[0]['pt']}px (mobile {pm[0]['pt']}), 40px between title and grid, **{144}px** below the grid at 1600 ({fl('padding', 'Projects')})")
OUT.extend(blocks_md("7.1", pj[0], pm[0], "Projects"))
w(f"- [ ] Then four cards in a 2 × 2 grid (cols 1–12 / 13–24; mobile one column), **56px** between the rows of cards. Each card: the logo plate, then one text block. "
  f"Link the image and the title to the project page ({fl('rowlink', 'Projects')}).")
cards = pj[1]["blocks"]; mcards = pm[1]["blocks"]
for i in range(0, len(cards), 4):
    grp = cards[i:i + 4]; mgrp = mcards[i:i + 4]
    OUT.extend(image_block("7.2", grp[0], mgrp[0], "Projects", logo=True, href=grp[0].get("href")))
    merged = dict(grp[1]); merged["lines"] = [grp[1]["lines"][0], grp[2]["lines"][0], grp[3]["lines"][0]]
    OUT.extend(text_block("7.2", merged, mgrp[1], "Projects"))
w("")
w('<div style="page-break-after: always"></div>')
w("")

# ---------------------------------------------------------------- homepage
hd, hm = D["index"]["1440"]["sections"], D["index"]["390"]["sections"]
REF["n"] = 0
w("## Page 8 · Homepage")
w("")
w("- [ ] Site Styles used: Heading 1–3, Paragraph 1–3, Primary button, themes White / Stone / Ink; CSS rules 15–16 (panels) and 18–19 (logo tiles). Collect two IDs for Page 9: the four panel image blocks and this page's Projects section.")
w("")
HOME = {
    "section.wrap.g24.hero": ("Hero", "Blank section · theme **White**"),
    "hr.hairline": ("Rule under the hero", None),
    "section#snippets": ("Snippets About My Life", "Blank section · theme **Stone** · anchor link `snippets`"),
    "section.panels": ("Four disciplines", "Blank section · content width **Full** · theme **Ink** · no space above or below · panels about 60% of the screen tall (540px at 1440; 42% on phones, 2 × 2)"),
    "section#projects": ("Projects", "Blank section · theme **White** · anchor link `projects`"),
    "section#contact": ("Contact", "Blank section · theme **Stone** · anchor link `contact`"),
    "footer.foot": ("Footer", None),
}
for si, (s, ms) in enumerate(zip(hd, hm)):
    key = next(k for k in HOME if s["sel"].startswith(k))
    name, setting = HOME[key]
    w(f"### 8.{si + 1} · {name}")
    REF["n"] = 0
    if key == "hr.hairline":
        w("- [ ] **Line** block · cols 1–24, section content width Full (edge to edge) · 1px, 14% ink · at the top of the next section (or a section divider, if her template has one).")
        w("")
        continue
    if key == "footer.foot":
        w("- [ ] Nothing to build: the site footer (Page 0).")
        w("")
        continue
    sp = f" · {spacing(s, ms)} ({fl('padding', 'Homepage')})" if key != "section.panels" else f" ({fl('panelsfull', 'Homepage')})"
    w(f"- [ ] **Section:** {setting}{sp}")
    if key == "section#projects":
        bs, mbs = s["blocks"], ms["blocks"]
        OUT.extend(blocks_md("8." + str(si + 1), {"blocks": bs[:2]}, {"blocks": mbs[:2]}, "Homepage"))
        w(f"- [ ] **Line** block · cols 1–24 · 1px ink · above the first row. Then four rows, each followed by a 1px, 14% ink Line block across cols 1–24; 22px above and below each row's content. "
          f"Link each title and logo to its project page ({fl('rowlink', 'Homepage')}; {fl('rowhover', 'Homepage')}).")
        for i in range(2, len(bs), 3):
            grp, mgrp = bs[i:i + 3], mbs[i:i + 3]
            OUT.extend(blocks_md("8." + str(si + 1), {"blocks": grp, "href": grp[0].get("href")}, {"blocks": mgrp}, "Homepage"))
            w("- [ ] **Line** block · cols 1–24 · 1px, 14% ink")
        w("")
        continue
    if key == "section.panels":
        w("- [ ] Each panel: an **Image** block filling the panel (Fill), then two **Text** blocks layered on top of it (*Bring forward*): the number in the panel's top rows, the name in its bottom rows. A 1px, 14% white rule between panels (Shape block outline, or none if the gaps show). Mobile: 2 × 2, panels 1–2 in the first row, 3–4 in the second.")
    OUT.extend(blocks_md("8." + str(si + 1), s, ms, "Homepage"))
    w("")
w('<div style="page-break-after: always"></div>')
w("")

# ---------------------------------------------------------------- custom CSS
CSS = [
    (".header{border-bottom:1px solid rgba(17,17,17,.14)}", "1px rule under the header, if the template has no header-border setting"),
    (".image-caption,.image-caption p{font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:rgba(17,17,17,.62)}", "image captions in the Paragraph 3 look (11px caps, 62% ink); text blocks already get it from Site Styles"),
    (".sqs-html-content li::marker{color:rgba(17,17,17,.62)}", "her bullet and number markers in 62% ink"),
    (".sqs-html-content ol{padding-left:0;list-style-position:inside;border-top:1px solid #111}", "numbered lists (Findings, Impact, the Littelfuse audit): 1px ink rule above the list"),
    (".sqs-html-content ol>li{padding:14px 0;border-bottom:1px solid rgba(17,17,17,.14)}", "…and a hairline under each item, 14px above and below it"),
    (".sqs-block-button-element,.fluid-image-container,.video-player,.sqs-video-wrapper{border-radius:0!important}", "square corners on buttons, images and videos, whatever the template's default"),
    (".sqs-slide-container input[type=\"password\"]{border:0!important;border-bottom:1px solid #111!important;border-radius:0!important;background:transparent!important;letter-spacing:.12em}", "lock screen: the password field is a single 1px ink line, no box"),
    (".sqs-slide-container input[type=\"password\"]:focus{border-bottom-width:2px!important;box-shadow:none!important}", "lock screen: the line thickens to 2px while typing"),
    (".sqs-slide-container button,.sqs-slide-container input[type=\"submit\"]{border-radius:0!important;background:#111!important;color:#fff!important;border:1px solid #111!important}", "lock screen: the Enter button solid ink, square"),
    (".sqs-slide-container .error,.sqs-slide-container .form-error{color:rgba(17,17,17,.62)!important;font-size:14px!important;animation:none!important}", "lock screen: the wrong-password message as quiet 14px text, no shake"),
    (".sqs-slide-container .sqs-slide-layer-content{max-width:560px;margin:0 auto}", "lock screen: the form column 560px wide, centred"),
    (".sqs-slide-container h1,.sqs-slide-container h2{font-weight:400!important;letter-spacing:-.01em}", "lock screen: the headline in regular weight with the headings' −0.01em tracking (Instrument Serif has no bold)"),
    (".sqs-slide-container a{text-decoration:underline;text-underline-offset:.22em}", "lock screen: links underlined, like the rest of the site"),
    (".sqs-slide-container .sqs-slide-layer{background:#fff}", "lock screen: white ground (no image behind it)"),
    (".I1 img,.I2 img,.I3 img,.I4 img{filter:brightness(.55);transition:filter .3s ease}", "discipline panels: each photo always under a 45% black layer (replace .I1–.I4 with the four image blocks' fe-block classes)"),
    (".I1:hover img,.I2:hover img,.I3:hover img,.I4:hover img{filter:brightness(.7)}", "discipline panels: hover lightens the layer to 30% (300ms)"),
    (".T1,.T2,.T3,.T4,.N1,.N2,.N3,.N4{pointer-events:none}", "discipline panels: the name and number text blocks let the pointer through to the photo (replace with their fe-block classes)"),
    (".L .fluid-image-container{background:#F4F3F0;transition:background-color .3s}", "logo tiles: the light ground behind each transparent plate (replace .L with the Home Projects section and the Projects page section: section[data-section-id=\"…\"], comma-separated)"),
    (".L .fluid-image-container:hover{background:#ECEAE5}", "logo tiles: a shade darker on hover"),
]
w("## Page 9 · Custom CSS (*Website → Pages → Custom code → Custom CSS*)")
w("")
w(f"**{len(CSS)} lines**, one rule per line, each with its comment (budget 30). The rules are the build notes' twenty, renumbered one per line (the notes counted the caption rule as two). Paste it after Home and Projects exist, then replace the placeholders:")
w("- [ ] `.I1`–`.I4`: right-click each **discipline photo** on Home → *Inspect* → copy the wrapper's `fe-block-…` class (rules 15–16).")
w("- [ ] `.T1`–`.T4`, `.N1`–`.N4`: the same for each panel's **name** and **number** text blocks (rule 17).")
w("- [ ] `.L`: the **Projects section on Home** and the **section on the Projects page**: `section[data-section-id=\"…\"]`, both, comma-separated (rules 18–19).")
w(f"- [ ] Lock-screen rules 7–14: check each class in the inspector on her site ({fl('lockcss', 'Custom CSS')}).")
w("- [ ] Other palettes: only the hex values change (the build notes list them per palette); cream adds one line, venues three to seven.")
w("")
w("```css")
num = 1
for rule, cmt in CSS:
    w(f"{rule} /* {num:>2}  {cmt} */")
    num += 1
w("```")
assert len(CSS) <= 30
w("")
w('<div style="page-break-after: always"></div>')
w("")

# ---------------------------------------------------------------- flags
w("## Page 10 · What Squarespace can't reproduce exactly")
w("")
w("Each flag is cited next to the blocks it affects. **Nearest native setting** in bold.")
w("")
for k, f in sorted(((k, f) for k, f in FLAGS.items() if f["n"]), key=lambda kv: kv[1]["n"]):
    where = sorted(set(f["where"]), key=f["where"].index)
    w(f"- [ ] **F{f['n']} · {f['title']}.** {f['native']} *Affects: {', '.join(where)} ({len(f['where'])} {'place' if len(f['where']) == 1 else 'places'}).*")
w("")
w("Not carried over at all: the theme switcher, the `?theme=` links, and the five-palette comparison (prototype tools). The prototype's one script stands in for the native slideshow.")
w("")
w('<div style="page-break-after: always"></div>')
w("")

# ---------------------------------------------------------------- final checks
w("## Page 11 · Final checks")
w("")
w("- [ ] Every page in **Preview** at desktop width and in the mobile view; compare with the prototype (`site/*.html`, or the screenshots in `screenshots/`).")
w("- [ ] Every text block against **COPY-CHECK.md**: her copy is verbatim; the captions are the ones listed under *Added captions* (she approves them).")
w("- [ ] Links: header (Projects, About, Contact), \"View Projects →\", every row and card (title + logo), chapter indexes (each `#ch-n` jumps to its chapter), prev / all / next on each project, Back to top, Email, Phone.")
w("- [ ] Lock screen: test the password in a private window (Page 6).")
w("- [ ] Pending before launch: LinkedIn URL, Littelfuse wireframes, snippet 21 confirmed (" + fl("pending", "Final checks") + ").")
w("- [ ] Contrast spot-check: captions and labels stay at 62% ink (not lighter). The panel number \"04\" measures 3.6:1 on its photo in the prototype (THEMES.md, rendered audit): set that number's text to full white, or the darkening to 50% on that panel.")

text = "\n".join(OUT)
summary = (f"**In this checklist:** {STATS['text']} text pastes, {STATS['image']} images (including {len(D['index']['1440']['sections'][2]['blocks'][-1]['slides'])} slideshow photos), "
           f"{STATS['video']} videos, {STATS['caption']} image captions, {len(CSS)} lines of CSS, {sum(1 for f in FLAGS.values() if f['where'])} flags.")
text = text.replace("<!-- summary -->", summary).replace("{NFLAGS}", str(NUM["next"] - 1))
open("SQUARESPACE-BUILD-CHECKLIST.md", "w").write(text + "\n")
print("SQUARESPACE-BUILD-CHECKLIST.md", len(OUT), "lines;", dict(STATS))
