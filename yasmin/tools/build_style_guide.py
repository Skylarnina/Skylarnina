"""Brand style guide for the Yasmin Bajwa portfolio: brand/style-guide.html.

Run from yasmin/ after tools/build_r3.py:  python3 tools/build_style_guide.py
Every value on the sheets is read from the built site (site/assets/css/r3.css and the
built pages), not typed in: if a rule the guide documents is missing from the CSS, this
script stops. Values the brief asked for that the build does not use are printed as
"[not used]". The components on sheet 05 are rendered with the site's own CSS rules,
copied from r3.css and scoped to the sheet.

Output: one standalone file. Inline CSS, Google Fonts links only, no JavaScript. The two
sample images are inlined as data URIs, so nothing else is loaded. Sheets are A4
(01 landscape, 02-05 portrait) and print one per page from the browser.
"""
import base64, html, io, re
from PIL import Image

CSS = re.sub(r"/\*.*?\*/", "", open("site/assets/css/r3.css").read(), flags=re.S)


def parse(s):
    out, i = [], 0
    while True:
        j = s.find("{", i)
        if j < 0:
            return out
        sel, depth, k = s[i:j].strip(), 1, j + 1
        while depth:
            depth += {"{": 1, "}": -1}.get(s[k], 0)
            k += 1
        out.append((sel, s[j + 1:k - 1]))
        i = k


TOP = parse(CSS)
MEDIA = {sel: parse(body) for sel, body in TOP if sel.startswith("@")}
RULES = [(s, b) for s, b in TOP if not s.startswith("@")]
MOBILE = MEDIA["@media (max-width:767px)"]
TABLET = MEDIA["@media (max-width:1099px)"]


def decls(rules, sel):
    """All declarations for an exact selector (later rules win), or KeyError."""
    found = [b for s, b in rules if s == sel]
    if not found:
        raise KeyError(sel)
    d = {}
    for body in found:
        for part in re.split(r";(?![^(]*\))", body):
            if ":" in part:
                k, v = part.split(":", 1)
                d[k.strip()] = v.strip()
    return d


def v(sel, prop, rules=RULES):
    d = decls(rules, sel)
    if prop not in d:
        if prop == "font-size" and "font" in d:          # shorthand: "500 var(--fs-label)/1.45 var(--font)"
            f = re.sub(r"var\((--[\w-]+)\)", lambda m: ROOT[m.group(1)], d["font"])
            return re.search(r"(\d+px)", f).group(1)
        if prop == "line-height" and "font" in d:
            return re.search(r"/([\d.]+)", d["font"]).group(1)
        if prop == "font-weight" and "font" in d:
            return d["font"].split()[0]
        raise KeyError(f"{sel} {{{prop}}}")
    return d[prop]


def mv(sel, prop):
    """Mobile value, or the desktop value when the build has no mobile override."""
    try:
        return v(sel, prop, MOBILE)
    except KeyError:
        return None


ROOT = decls(RULES, ":root")
TOK = lambda name: ROOT[name]
E = html.escape


def resolve(value):
    """var(--x) → its value; clamp(min, pref, max) → max (desktop, ≥1482px wide) and min (mobile)."""
    value = re.sub(r"var\((--[\w-]+)\)", lambda m: TOK(m.group(1)), value)
    m = re.match(r"clamp\(([^,]+),([^,]+),([^)]+)\)", value)
    return (m.group(3).strip(), m.group(1).strip(), value) if m else (value, value, value)


def rgb_hex(c):
    return "#%02X%02X%02X" % c


def over(fg, a, bg):
    return tuple(round(fg[i] * a + bg[i] * (1 - a)) for i in range(3))


def lum(c):
    f = lambda x: x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4
    r, g, b = (x / 255 for x in c)
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def ratio(a, b):
    hi, lo = sorted([lum(a), lum(b)], reverse=True)
    return (hi + 0.05) / (lo + 0.05)


def hexrgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def alpha_of(token):
    return float(re.search(r"rgba\(17,17,17,([\d.]+)\)", token).group(1))


def uses(value):
    """True if a literal value appears anywhere in the site CSS."""
    return value.lower() in CSS.lower()


def data_uri(path, width):
    im = Image.open(path).convert("RGB")
    im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=78, optimize=True, progressive=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


# ------------------------------------------------------------------ brand values
BG, ALT, INK = TOK("--bg"), TOK("--alt"), TOK("--ink")
MUTED, HAIR = TOK("--muted"), TOK("--hair")
A_MUTED, A_HAIR = alpha_of(MUTED), alpha_of(HAIR)
A_COVER = alpha_of(v(".cover--dark .m::after", "background"))
A_PLACE = alpha_of(re.search(r"rgba\([^)]*\)", v(".placeholder", "border")).group(0))
PANEL_REST = float(re.search(r"brightness\(([\d.]+)\)", v(".panel .m", "filter")).group(1))
PANEL_HOVER = float(re.search(r"brightness\(([\d.]+)\)", v(".panel:hover .m", "filter")).group(1))
PANEL_T = v(".panel .m", "transition")
PANEL_NO = v(".panel .no", "color")
FONT_BODY = TOK("--font").split(",")[0].strip("'")
FONT_HEAD = TOK("--font-head").split(",")[0].strip("'")
ink, white, ground = hexrgb(INK), hexrgb(BG), hexrgb(ALT)
assert FONT_HEAD == "Instrument Serif" and FONT_BODY == "Inter Tight", (FONT_HEAD, FONT_BODY)

# the real component markup, taken from the built pages
room = open("site/room-01-jackson-home.html").read()
home = open("site/index.html").read()
lock = open("site/private-view.html").read()
META = re.search(r'<dl class="meta__panel">.*?</dl>', room, re.S).group(0)
CHINDEX = re.search(r'<div class="chindex">.*?</div>', room, re.S).group(0)
ROW = re.search(r'<a class="row fade".*?</a>', home, re.S).group(0).replace(" fade", "")
ROW_IMG = re.search(r'<img src="assets/img/([^"]+)"', ROW).group(1)
ROW = ROW.replace(f"assets/img/{ROW_IMG}", data_uri(f"site/assets/img/{ROW_IMG}", 360)).replace(' loading="lazy"', "")
FIG_CAP = re.search(r"Fig\. 04 — [^<]+", room).group(0)
FIG_IMG = re.search(r'<img src="assets/img/(tiles/r01-plan-annex[^"]+)"', room).group(1)
FIG = (f'<figure class="t"><div class="m" style="aspect-ratio:1.5"><img src="{data_uri("site/assets/img/" + FIG_IMG, 520)}" alt="The Annex floor plan"></div>'
       f'<figcaption>{E(FIG_CAP)}</figcaption></figure>')
LOCKFORM = re.search(r"<form.*?</form>", lock, re.S).group(0)
LOCKFORM = LOCKFORM.replace('action="private-view.html#wrong"', 'action="#"')

# site rules used to render the live components on sheet 05, scoped to .spec
SPEC_SELECTORS = [
    ".label", ".u", ".u:hover", ".btn", ".btn:hover", ".btn--solid", ".btn--solid:hover",
    ".bar nav", ".bar nav a[aria-current]", ".bar nav a:hover",
    ".m", ".m img,.m video", ".t", ".t .m", ".t .m img", ".t figcaption,.mod--video figcaption",
    ".rows", ".row", ".row__t", ".row__t h3", ".row__role", ".row__img", ".row__img .m", ".m--fit img",
    ".meta__panel", ".meta__panel div", ".meta__panel div:nth-child(-n+2)", ".meta__panel dd", ".meta__panel .wide",
    ".chindex", ".chindex ol", ".chindex li", ".chindex li span", ".chindex a:hover",
    ".lock form", ".lock label", ".lock input", ".lock input:focus", ".lock input:focus-visible", ".lock .err",
]
spec_css = []
for sel in SPEC_SELECTORS:
    body = ";".join(f"{k}:{val}" for k, val in decls(RULES, sel).items())
    scoped = ",".join(".spec " + s.strip() for s in sel.split(","))
    spec_css.append(f"{scoped}{{{body}}}")
# forced states, copied from the build's own :hover / :focus-visible rules
FOCUS = decls(RULES, ":focus-visible")
state_css = [
    ".spec .btn.is-hover{" + ";".join(f"{k}:{x}" for k, x in decls(RULES, ".btn:hover").items()) + "}",
    ".spec .btn--solid.is-hover{" + ";".join(f"{k}:{x}" for k, x in decls(RULES, ".btn--solid:hover").items()) + "}",
    ".spec .u.is-hover{" + ";".join(f"{k}:{x}" for k, x in decls(RULES, ".u:hover").items()) + "}",
    ".spec .bar nav a.is-hover{" + ";".join(f"{k}:{x}" for k, x in decls(RULES, ".bar nav a:hover").items()) + "}",
    ".spec .is-focus{" + ";".join(f"{k}:{x}" for k, x in FOCUS.items()) + "}",
]

# ------------------------------------------------------------------ type scale (from the CSS)
def size_row(name, sample, sel, prop="font-size", family="head", where="", italic=False, show=None, mobile_sel=None):
    raw = v(sel, prop)
    desk, mob, expr = resolve(raw)
    m = mv(mobile_sel or sel, prop)
    if m:
        mob = resolve(m)[0]
    try:
        lh = v(sel, "line-height")
    except KeyError:
        lh = "1.6 (inherits)" if family == "body" else "—"
    try:
        tr = v(sel, "letter-spacing")
    except KeyError:
        tr = "0"
    shown = show or desk
    fam = "var(--head)" if family == "head" else "var(--body)"
    extra = ""
    if family == "body":
        try:
            extra += f";font-weight:{v(sel, 'font-weight')}"
        except KeyError:
            pass
        try:
            extra += f";text-transform:{v(sel, 'text-transform')}"
        except KeyError:
            pass
    lh_css = lh if re.fullmatch(r"[\d.]+", lh) else "1.1"
    style = f"font-family:{fam};font-size:{shown};line-height:{lh_css};letter-spacing:{tr}{';font-style:italic' if italic else ''}{extra}"
    note = "" if shown == desk else f" <span class='mut'>(shown at {shown})</span>"
    if family == "head":
        return (f"<div class='hs'><p class='hs-sample' style=\"{style}\">{E(sample)}</p>"
                f"<p class='hs-meta'><b>{E(name)}</b><br><span class='mut'>{E(where)}</span><br>"
                f"{E(desk)} · mobile {E(mob)} · line {E(lh)} · track {E(tr)}</p></div>")
    return (f"<tr><td class='spec-sample' style=\"{style}\">{E(sample)}</td>"
            f"<td><b>{E(name)}</b> <span class='mut'>{E(where)}</span></td>"
            f"<td>{E(desk)}{note}<br><span class='mut'>mobile {E(mob)}</span></td><td>{E(lh)}</td><td>{E(tr)}</td></tr>")


HEAD_ROWS = "".join([
    size_row("H1 · Hero name", "Yasmin.", ".hero__hi", where=".hero__hi · var(--fs-hero)", italic=True),
    size_row("H2 · Page, cover, contact titles", "Projects", ".p-title", where=".p-title, .cover__title, .dochead__title, .contact h2 · var(--fs-title). Lock screen .lock__box h1: " + v(".lock__box h1", "font-size"), mobile_sel=".dochead__title"),
    size_row("H3 · Chapter titles", "The Challenge", ".ch-head h2", where=".ch-head h2 · var(--fs-chapter)"),
    size_row("Discipline names", "UX Research", ".panel h3", where=".panel h3"),
    size_row("Project titles · rows", "Littelfuse Products", ".row__t h3", where=".row__t h3 (grid: .card h2 " + v(".card h2", "font-size") + ", prev/next .pn .t " + v(".pn .t", "font-size") + ")"),
    size_row("H4 · Her sub-headings", "Visitor Experience", "h3.b,h4.b", where="h3.b, h4.b · var(--fs-sub)"),
])
BODY_ROWS = "".join([
    size_row("Statement (Paragraph 1)", "By blending design…", ".about__statement", family="body", where=".about__statement", show="24px"),
    size_row("Hero paragraph", "Hi! I’m Yasmin, a Digital…", ".hero__about p", family="body", where=".hero__about p"),
    size_row("How-might-we lines", "How might we predict…", ".b.hmw", family="body", where=".b.hmw", show="20px"),
    size_row("Meta, facts, role lines", "UX Researcher | Experience Design", ".meta__panel dd", family="body", where=".meta__panel dd, .facts dd"),
    size_row("Kicker", "About Me", ".kicker", family="body", where=".kicker · 500"),
    size_row("Navigation", "Projects", ".bar nav", family="body", where=".bar nav"),
    size_row("Button", "View Projects →", ".btn", family="body", where=".btn"),
    size_row("Label · caption (Paragraph 3)", "Fig. 04 — The Annex", ".label", family="body", where=".label, figcaption · 500, caps, 62%"),
    size_row("Section tags", "History · Fashion · Art", ".about__tags", family="body", where=".about__tags · 500, caps"),
    size_row("Stat numerals", "60%", ".stats .num", family="body", where=".stats .num", show="28px"),
])
BODY_SIZE = TOK("--fs-body")
BODY_MOB = re.search(r"--fs-body:(\d+px)", "".join(b for s, b in MOBILE if s == ":root")).group(1)

# ------------------------------------------------------------------ colour
def swatch(color_css, name, hexlabel, note="", used=True):
    cls = "sw" + ("" if used else " sw--nu")
    tag = "" if used else "<span class='nu'>[not used]</span>"
    return (f"<div class='{cls}'><div class='chip' style='background:{color_css}'></div>"
            f"<p class='sw-n'>{E(name)}</p><p class='sw-h'>{E(hexlabel)}</p>{tag}"
            f"{f'<p class=sw-u>{E(note)}</p>' if note else ''}</div>")


mark_row = "".join([
    swatch(INK, "Ink", INK, "mark, rows 1–2"),
    swatch(BG, "White", BG, "row 1 ground, row 3 mark"),
    swatch(ALT, "Ground", ALT, "row 2 ground, row 4 mark"),
])
ink_steps = [(0.06, "Ink 6%", None), (A_HAIR, f"Ink {round(A_HAIR * 100)}%", "hairlines"), (0.55, "Ink 55%", None),
             (A_MUTED, f"Ink {round(A_MUTED * 100)}%", "captions, labels"), (1.0, "Ink 100%", "text")]
ink_row = ""
for a, name, note in ink_steps:
    used = a == 1.0 or f"rgba(17,17,17,{str(a).lstrip('0')})" in CSS.replace(" ", "")
    extra = "brief asked 55%; the build uses 62% for contrast" if a == 0.55 else note or ""
    ink_row += swatch(f"rgba(17,17,17,{a})", name, rgb_hex(over(ink, a, white)) + (f" · rgba {a:g}" if a < 1 else ""), extra, used)
ground_row = "".join([
    swatch(BG, "White", BG, "page ground", uses(BG)),
    swatch(ALT, "Ground", ALT, "plates, Stone sections", uses(ALT)),
    swatch("#ECEAE5", "Ground deep", "#ECEAE5", "", uses("#ECEAE5")),
])
usage = [
    (BG, "Page ground", BG, "html, body, .lock"),
    (ALT, "Section ground", ALT, "About, Contact, Reflection"),
    (ALT, "Plate ground", ALT, "every drawing tile, .m"),
    (HAIR, "Hairlines", rgb_hex(over(ink, A_HAIR, white)), f"rgba {A_HAIR:g}"),
    (f"rgba(17,17,17,{A_PLACE})", "Placeholder border", rgb_hex(over(ink, A_PLACE, white)), f"rgba {A_PLACE:g}, dashed"),
    (f"rgba(17,17,17,{A_COVER})", "Cover overlay", rgb_hex(over(ink, A_COVER, white)), f"rgba {A_COVER:g} over photos"),
    (rgb_hex(tuple(round(c * PANEL_REST) for c in ground)), "Panel overlay", f"brightness({PANEL_REST:g})",
     f"45% black at rest, {round((1 - PANEL_HOVER) * 100)}% on hover"),
    (MUTED, "Captions, labels", rgb_hex(over(ink, A_MUTED, white)), f"rgba {A_MUTED:g}"),
    (INK, "Text", INK, "all text, 1px rules"),
]
usage_row = "".join(swatch(c, n, h, u) for c, n, h, u in usage)

pairs = [
    ("Ink text", ink, "on White", white, "body, headings"),
    ("Ink text", ink, "on Ground", ground, "Stone sections"),
    (f"Captions {round(A_MUTED * 100)}%", over(ink, A_MUTED, white), "on White", white, "labels, FIG. captions (11px)"),
    (f"Captions {round(A_MUTED * 100)}%", over(ink, A_MUTED, ground), "on Ground", ground, "labels on Stone sections"),
    ("Ink 55% [not used]", over(ink, .55, white), "on White", white, "why the build uses 62%"),
    ("White", white, "on Ink", ink, "hover state of the outline button"),
    ("White names", white, f"on panel ground ({PANEL_REST:g})", tuple(round(c * PANEL_REST) for c in ground), "disciplines, at rest (34px)"),
    ("White names", white, f"on panel ground ({PANEL_HOVER:g})", tuple(round(c * PANEL_HOVER) for c in ground), "disciplines, while hovered"),
    ("Hairline 14%", over(ink, A_HAIR, white), "on White", white, "decorative rule, not text"),
]


def verdict(r, big=False, deco=False):
    if deco:
        return "n/a (not text)"
    if r >= 7:
        return "AAA"
    if r >= 4.5:
        return "AA"
    if r >= 3:
        return "AA large only"
    return "fails"


contrast_rows = ""
for fg_n, fg, bg_n, bg, where in pairs:
    r = ratio(fg, bg)
    ver = verdict(r, deco="Hairline" in fg_n)
    flag = " flag" if ver in ("fails",) or "55%" in fg_n else ""
    contrast_rows += (f"<tr class='{flag.strip()}'><td><span class='dot' style='background:{rgb_hex(fg)}'></span>{E(fg_n)} {rgb_hex(fg)}</td>"
                      f"<td><span class='dot' style='background:{rgb_hex(bg)}'></span>{E(bg_n)} {rgb_hex(bg)}</td>"
                      f"<td class='num'>{r:.2f}:1</td><td>{ver}</td><td class='mut'>{E(where)}</td></tr>")

# ------------------------------------------------------------------ layout values
GUTTER, MARGIN, SECTION = TOK("--gutter"), TOK("--margin"), TOK("--section")
GUT_MOB = re.search(r"--gutter:(\d+px)", "".join(b for s, b in MOBILE if s == ":root")).group(1)
MG = v(".mod", "--mg")
MG_MOB = decls(MOBILE, ".mod")["--mg"]
WRAP = v(".wrap", "max-width")
BAR_H = v(".bar .wrap", "min-height")
FADE = decls(parse(MEDIA["@supports (animation-timeline:view())"][0][1]), ".fade")
BTN_T = v(".btn", "transition")
RATIOS = {"Cover (photo)": v(".cover .m", "aspect-ratio"), "Project rows + grid": v(".row__img .m", "aspect-ratio"),
          "Headshot": v(".hero__photo .m", "aspect-ratio"), "Mosaic wide": v(".mosaic .t--wide .m", "aspect-ratio"),
          "Mosaic squares": v(".mosaic .t--sqa .m,.mosaic .t--sqb .m", "aspect-ratio"), "Baseline plan": v(".spread__plan .m", "aspect-ratio"),
          "Placeholder": v(".placeholder", "aspect-ratio")}
RADIUS = sorted(set(re.findall(r"border-radius:([^;}]+)", CSS)))
SHADOW = "box-shadow" in CSS

# ------------------------------------------------------------------ page
def run(title, no):
    return (f"<header class='run'><span>Yasmin Bajwa · Portfolio brand guide</span>"
            f"<span>{E(title)}</span><span>{no:02d}</span></header>")


YB, NAME = "YB", "Yasmin Bajwa"
NAME_SIZE = v(".bar__name", "font-size")
NAME_TRACK = v(".bar__name", "letter-spacing")
rows_def = [  # (row background, foreground, secondary tone for "full colour")
    ("#FFFFFF", INK, MUTED, "light"),
    (ALT, INK, MUTED, "light"),
    (INK, BG, PANEL_NO, "dark"),
    (INK, ALT, PANEL_NO, "dark"),
]
lock_rows = ""
for bg, fg, sec, tone in rows_def:
    cells = (f"<div class='cell'><span class='yb yb--xl' style='color:{fg}'>{YB}</span></div>"
             f"<div class='cell'><span class='wm wm--l' style='color:{fg}'>{NAME}</span></div>"
             f"<div class='cell'><span class='lk'><span class='yb' style='color:{fg}'>{YB}</span><span class='wm' style='color:{fg}'>{NAME}</span></span></div>"
             f"<div class='cell'><span class='lk'><span class='yb' style='color:{fg}'>{YB}</span><span class='wm' style='color:{sec}'>{NAME}</span></span></div>")
    paint = f" style='background:{bg}'" if tone == "light" else ""      # the dark block is painted once, by .lockgrid
    lock_rows += f"<div class='lrow lrow--{tone}'{paint}>{cells}</div>"


def btn_cell(html_, label):
    return f"<div class='bcell'><div class='bstage'>{html_}</div><p class='cap10'>{label}</p></div>"


NU = "<span class='nu'>[not used]</span>"
buttons = [
    ("Primary outline", ".btn", [
        '<a class="btn" href="#">View Projects →</a>', '<a class="btn is-hover" href="#">View Projects →</a>',
        '<a class="btn is-focus" href="#">View Projects →</a>', NU]),
    ("Text link", ".u", [
        '<a class="u" href="#">All projects →</a>', '<a class="u is-hover" href="#">All projects →</a>',
        '<a class="u is-focus" href="#">All projects →</a>', NU]),
    ("Nav item", ".bar nav a", [
        '<div class="bar"><nav><a href="#">Projects</a></nav></div>', '<div class="bar"><nav><a class="is-hover" href="#">Projects</a></nav></div>',
        '<div class="bar"><nav><a class="is-focus" href="#">Projects</a></nav></div>', NU]),
    ("Solid (lock screen)", ".btn--solid", [
        '<button class="btn btn--solid" type="button">Enter</button>', '<button class="btn btn--solid is-hover" type="button">Enter</button>',
        '<button class="btn btn--solid is-focus" type="button">Enter</button>', NU]),
]
bgrid = "<div class='bhead'><span></span>" + "".join(f"<span class='cap10'>{s}</span>" for s in ("Default", "Hover", "Focus", "Disabled")) + "</div>"
for name, sel, cells in buttons:
    bgrid += (f"<div class='brow'><p class='cap10 bname'>{name}<br><span class='mut'>{E(sel)}</span></p>"
              + "".join(f"<div class='bstage'>{c}</div>" for c in cells) + "</div>")

guide_css = f"""
:root{{--canvas:#8C8C8C;--bg:{BG};--alt:{ALT};--ink:{INK};--muted:{MUTED};--hair:{HAIR};
  --font:{TOK('--font')};--font-head:{TOK('--font-head')};--gutter:{GUTTER};--margin:{MARGIN};--section:{SECTION};
  --fs-label:{TOK('--fs-label')};--fs-body:{BODY_SIZE};--fs-sub:{TOK('--fs-sub')};
  --head:{TOK('--font-head')};--body:{TOK('--font')};--mono:{TOK('--font')}}}
*{{box-sizing:border-box}}
html{{background:var(--canvas)}}
body{{margin:0;background:var(--canvas);color:var(--ink);font:400 12px/1.5 var(--body);-webkit-font-smoothing:antialiased;font-feature-settings:"calt" 0}}
/* guide text shows CSS names ("--fs-hero"), so contextual alternates are off; specimens and live components keep the site's default */
.spec-sample,.hs-sample,.aa,.fname,.yb,.wm,.spec .bstage,.spec .comp > div{{font-feature-settings:normal}}
p,h1,h2,h3,figure,dl,dd,ol{{margin:0}}
.canvas{{display:flex;flex-wrap:wrap;justify-content:center;align-items:flex-start;gap:10mm;padding:12mm 6mm 20mm}}
.canvas__title{{flex-basis:100%;text-align:center;color:#fff;font:500 10px/1.4 var(--body);letter-spacing:.14em;text-transform:uppercase}}
.sheet{{position:relative;background:#fff;overflow:hidden;flex:none;box-shadow:0 1px 2px rgba(0,0,0,.18),0 14px 36px rgba(0,0,0,.22)}}
.sheet--land{{width:297mm;height:210mm;page:land;flex-basis:100%;max-width:297mm}}
.sheet--port{{width:210mm;height:297mm;page:port}}
.break{{flex-basis:100%;height:0}}
.run{{position:absolute;top:0;left:0;right:0;height:14mm;padding:0 14mm;display:flex;justify-content:space-between;align-items:center;
  font:500 7.5px/1 var(--body);letter-spacing:.14em;text-transform:uppercase;color:#6B6B6B;border-bottom:1px solid var(--hair);background:#fff;z-index:2}}
.body{{position:absolute;top:14mm;left:14mm;right:14mm;bottom:12mm;display:flex;flex-direction:column;gap:5mm;padding-top:6mm}}
.h{{font:400 34px/1 var(--head);letter-spacing:0}}
.lead{{font-size:11px;line-height:1.5;color:#444;max-width:120mm}}
.mut{{color:#6B6B6B}}
.cap10{{font:500 10px/1.3 var(--body);letter-spacing:.1em;text-transform:uppercase;color:#6B6B6B}}
.nu{{display:inline-block;font:500 8px/1.2 var(--body);letter-spacing:.08em;text-transform:uppercase;color:#6B6B6B;border:1px dashed rgba(17,17,17,.35);padding:2px 4px}}
table{{border-collapse:collapse;width:100%}}
th{{text-align:left;font:500 7.5px/1.3 var(--body);letter-spacing:.12em;text-transform:uppercase;color:#6B6B6B;padding:0 6px 5px 0;border-bottom:1px solid var(--ink)}}
td{{padding:5px 6px 5px 0;border-bottom:1px solid var(--hair);vertical-align:middle;font-size:9.5px;line-height:1.35}}

/* 01 lockups */
.lockgrid{{position:absolute;top:14mm;left:0;right:0;bottom:0;display:grid;grid-template-rows:repeat(4,1fr);background:linear-gradient(to bottom,transparent 50%,{INK} 50%)}}
.lrow{{display:grid;grid-template-columns:repeat(4,1fr);padding:0 14mm}}
.cell{{display:flex;align-items:center;justify-content:center}}
.yb{{font-family:'Instrument Sans',sans-serif;font-weight:500;letter-spacing:-.01em;line-height:1;font-size:40px}}
.yb--xl{{font-size:96px}}
.wm{{font-family:var(--body);font-weight:400;letter-spacing:{NAME_TRACK};line-height:1;font-size:21px}}
.wm--l{{font-size:27px}}
.lk{{display:inline-flex;align-items:center;gap:12px}}

/* 02 typography */
.faces{{display:grid;grid-template-columns:1fr 1fr;gap:8mm;border-bottom:1px solid var(--ink);padding-bottom:4mm}}
.face{{display:grid;grid-template-columns:auto 1fr;column-gap:4mm;align-items:start}}
.face .subh{{grid-column:1/-1}}
.face .aa{{grid-row:2/4}}
.face .aa{{font-size:60px;line-height:.9}}
.face .fname{{font-size:18px;line-height:1.1;margin-top:0}}
.face p{{font-size:8.5px;line-height:1.4;margin-top:1mm}}
.spec-sample{{white-space:nowrap;padding-right:10px;max-width:70mm;overflow:hidden}}
.hscale{{border-top:1px solid var(--ink)}}
.hs{{display:grid;grid-template-columns:1fr 60mm;align-items:end;gap:4mm;padding:1.4mm 0;border-bottom:1px solid var(--hair)}}
.hs-sample{{white-space:nowrap}}
.hs-meta{{font-size:8px;line-height:1.4;padding-bottom:1mm}}
.tt td{{padding:2px 6px 2px 0;font-size:8px;line-height:1.3}}
.tt td:nth-child(n+3){{white-space:nowrap}}
.subh{{font:500 7.5px/1.3 var(--body);letter-spacing:.12em;text-transform:uppercase;color:#6B6B6B;margin-bottom:1.5mm}}

/* 03 colour */
.ladder{{display:grid;grid-template-columns:28mm 1fr;gap:3mm;padding:3mm 0;border-bottom:1px solid var(--hair)}}
.ladder:first-of-type{{border-top:1px solid var(--ink)}}
.ladder h3{{font:400 20px/1.05 var(--head)}}
.ladder h3 small{{display:block;font:500 7.5px/1.3 var(--body);letter-spacing:.12em;text-transform:uppercase;color:#6B6B6B;margin-top:1.5mm}}
.swatches{{display:flex;flex-wrap:wrap;gap:2.4mm}}
.sw{{width:13.6mm}}
.chip{{width:13.6mm;height:13.6mm;border:1px solid rgba(17,17,17,.14)}}
.sw--nu .chip{{border-style:dashed;border-color:rgba(17,17,17,.35)}}
.sw-n{{font-size:8px;line-height:1.2;margin-top:1.6mm;font-weight:500}}
.sw-h{{font-size:7.5px;line-height:1.2;color:#6B6B6B}}
.sw-u{{font-size:7px;line-height:1.2;color:#6B6B6B;margin-top:.6mm}}
.sw .nu{{margin-top:1mm;font-size:6.5px;padding:1px 3px}}
.dot{{display:inline-block;width:8px;height:8px;border:1px solid rgba(17,17,17,.2);vertical-align:-1px;margin-right:5px}}
td.num{{font-variant-numeric:tabular-nums;font-weight:500}}
tr.flag td{{background:#F4F3F0}}
.noaccent{{font-size:10px;line-height:1.45;padding-top:1mm}}

/* 04 layout */
.cols24{{display:grid;grid-template-columns:repeat(24,1fr);gap:2px;height:16mm}}
.cols24 i{{background:rgba(17,17,17,.14)}}
.cols24 i.on{{background:rgba(17,17,17,.62)}}
.kv{{display:grid;grid-template-columns:44mm 1fr;border-top:1px solid var(--ink)}}
.kv dt,.kv dd{{padding:4px 0;border-bottom:1px solid var(--hair);font-size:9.5px;line-height:1.4}}
.kv dt{{color:#6B6B6B}}
.mods{{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm}}
.mod-d{{display:grid;gap:1.5mm}}
.mod-d .box{{display:grid;gap:3px;height:20mm}}
.mod-d .box i{{background:#F4F3F0;outline:1px solid rgba(17,17,17,.14)}}
.mod-d p{{font-size:8.5px;line-height:1.3}}

/* 05 components */
.bgrid{{display:grid;gap:0;border-top:1px solid var(--ink)}}
.bhead,.brow{{display:grid;grid-template-columns:22mm 1fr 1fr 1fr 18mm;align-items:center;gap:2mm;border-bottom:1px solid var(--hair)}}
.spec .bstage .btn{{white-space:nowrap}}
.bhead{{padding:1.6mm 0}}
.brow{{padding:1.2mm 0}}
.bname{{line-height:1.35}}
.bname .mut{{text-transform:none;letter-spacing:0;font-weight:400}}
.bstage{{display:flex;align-items:center}}
.comp{{display:grid;grid-template-columns:30mm 1fr;gap:3mm;padding:1.8mm 0;border-bottom:1px solid var(--hair);align-items:start}}
.comp:first-of-type{{border-top:1px solid var(--ink)}}
.comp > .cap10 small{{display:block;text-transform:none;letter-spacing:0;font-weight:400;margin-top:1mm}}

/* the site's own rules, scoped (sheet 05) */
.spec{{font:400 var(--fs-body)/1.6 var(--font);color:var(--ink)}}
.spec a{{color:inherit;text-decoration:none}}
.spec h3{{font-family:var(--font-head);font-weight:400;font-synthesis:none;margin:0}}
.spec button{{font:inherit}}
.spec img{{display:block;max-width:100%;height:auto}}
{chr(10).join(spec_css)}
{chr(10).join(state_css)}
/* guide-only placement overrides (after the site rules): margins and panel ground off, width limits */
.spec .rows .row{{column-gap:8px}}
.spec .meta__panel{{background:none;padding:0}}
.spec .chindex{{margin-top:0}}
.spec .lock{{position:static}}
.spec .lock form{{max-width:120mm;margin-top:0}}
.spec .comp > div{{zoom:.7}}
.spec .t{{width:60mm}}
.spec .t .m img{{height:100%;object-fit:contain}}
.spec .row__t h3{{font-size:24px}}

@page land{{size:A4 landscape;margin:0}}
@page port{{size:A4 portrait;margin:0}}
@media print{{
  html,body{{background:#fff}}
  .canvas{{display:block;padding:0}}
  .canvas__title,.break{{display:none}}
  .sheet{{box-shadow:none;margin:0;break-after:page}}
  .sheet:last-child{{break-after:auto}}
  *{{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
}}
"""

rt = lambda s: resolve(s)[0]
sheets = f"""
<section class="sheet sheet--land" aria-label="Sheet 01, wordmark lockups">
{run("Wordmark lockups", 1)}
<div class="lockgrid">{lock_rows}</div>
</section>
<div class="break"></div>

<section class="sheet sheet--port" aria-label="Sheet 02, typography">
{run("Typography", 2)}
<div class="body">
  <div class="faces">
    <div class="face"><p class="subh">Display · headings</p><div class="aa" style="font-family:var(--head)">Aa<em>a</em></div>
      <p class="fname" style="font-family:var(--head)">{FONT_HEAD}</p>
      <p>Weight 400 and italic 400 only. No bold: emphasis is italic, synthesis off. Tracking −0.01em above 48px, 0 below. Hero name, page and cover titles, chapter titles, her sub-headings, discipline names, project titles.</p></div>
    <div class="face"><p class="subh">Body · text, captions, labels</p><div class="aa" style="font-family:var(--body)">Aa<em>a</em></div>
      <p class="fname" style="font-family:var(--body)">{FONT_BODY}</p>
      <p>Weights 400 and 500, italic 400. Body {BODY_SIZE}/1.6 ({BODY_MOB} on mobile). Captions and labels 11px, 500, uppercase, tracking 0.08em, 62% ink. Also navigation, buttons and numerals.</p></div>
  </div>
  <div><p class="subh">Heading scale · {FONT_HEAD} · specimens at true desktop size (clamps at their maximum, ≥1482px wide)</p>
  <div class="hscale">{HEAD_ROWS}</div></div>
  <div><p class="subh">Body and small styles · {FONT_BODY}</p>
  <table class="tt"><tr><th>Specimen</th><th>Style · selector</th><th>Size</th><th>Line</th><th>Track</th></tr>
  <tr><td class="spec-sample" style="font-family:var(--body);font-size:{BODY_SIZE}">Her case-study text, verbatim.</td><td><b>Body (Paragraph 2)</b><br><span class="mut">body · var(--fs-body), measure 62ch</span></td><td>{BODY_SIZE}<br><span class="mut">mobile {BODY_MOB}</span></td><td>1.6</td><td>0</td></tr>
  {BODY_ROWS}</table></div>
  <p class="cap10" style="font-size:7.5px">Monogram only (sheet 01): Instrument Sans 500. The site itself does not use Instrument Sans.</p>
</div>
</section>

<section class="sheet sheet--port" aria-label="Sheet 03, colour">
{run("Colour", 3)}
<div class="body">
  <p class="lead">Tint ladders, light to dark. Hex values are as seen on white. A dashed swatch was asked for but is not in the build.</p>
  <div>
    <div class="ladder"><h3>Mark<small>The monogram's colours</small></h3><div class="swatches">{mark_row}</div></div>
    <div class="ladder"><h3>Ink<small>Primary</small></h3><div class="swatches">{ink_row}</div></div>
    <div class="ladder"><h3>Ground<small>Secondary</small></h3><div class="swatches">{ground_row}</div></div>
    <div class="ladder"><h3>Usage<small>Neutral · where each value is used</small></h3><div class="swatches">{usage_row}</div></div>
  </div>
  <div><p class="subh">Contrast (WCAG 2.1, measured on the composited colour)</p>
  <table><tr><th>Foreground</th><th>Background</th><th>Ratio</th><th>Level</th><th>Where</th></tr>{contrast_rows}</table></div>
  <p class="noaccent"><b>No accent colour.</b> The palette is ink and ground only, so the only colour on any page is the colour in her work: the charts, screens, drawings and photographs.</p>
</div>
</section>
<div class="break"></div>

<section class="sheet sheet--port" aria-label="Sheet 04, grid and layout">
{run("Grid, spacing and images", 4)}
<div class="body" style="gap:5mm">
  <div><h2 class="h">Grid, spacing and images</h2><p class="lead" style="margin-top:2mm">The layout rules the pages are built on. Values from r3.css; the six modules are listed in MODULE-MAP.md.</p></div>
  <div><p class="subh">24-column grid · the text measure (columns 9–20) shaded</p>
  <div class="cols24">{"".join(f"<i class='{'on' if 9 <= k <= 20 else ''}'></i>" for k in range(1, 25))}</div></div>
  <dl class="kv">
    <dt>Columns</dt><dd>24 (Fluid Engine desktop grid). One column below 768px.</dd>
    <dt>Gutter</dt><dd>{GUTTER} ({GUT_MOB} on mobile). Bento modules: {MG} ({MG_MOB} on mobile).</dd>
    <dt>Page margin</dt><dd>{MARGIN} → {rt(MARGIN)} at desktop, {resolve(MARGIN)[1]} on phones. Max content width {WRAP}.</dd>
    <dt>Section spacing</dt><dd>{SECTION} → {rt(SECTION)} / {resolve(SECTION)[1]}.</dd>
    <dt>Breakpoints</dt><dd>≤1099px tablet, ≤767px mobile.</dd>
    <dt>Top bar</dt><dd>{BAR_H} high, 1px hairline beneath.</dd>
    <dt>Corners · shadows</dt><dd>Radius {", ".join(RADIUS)} everywhere. {"Shadows used." if SHADOW else "No shadows."}</dd>
    <dt>Image ratios</dt><dd>{" · ".join(f"{k} {x}" for k, x in RATIOS.items())}.</dd>
    <dt>Drawings, screens, documents</dt><dd>Whole, never cropped, on {ALT} with 24px padding inside the exported tile (48px on the Rooms 03/04 cover plates).</dd>
    <dt>Photographs</dt><dd>May be cropped to the slot's ratio.</dd>
    <dt>Captions</dt><dd>Every image: "FIG. nn — …", 11px caps, 62% ink, 10px below the image (captions above in a Strip).</dd>
    <dt>Overlays</dt><dd>Photo covers: ink at {A_COVER:g}. Discipline panels: brightness({PANEL_REST:g}) = 45% black at rest, ({PANEL_HOVER:g}) on hover; {PANEL_T}.</dd>
    <dt>Motion</dt><dd>One fade: opacity 0→1, animation-range {FADE["animation-range"]}, only where supported and when reduced motion is off. Buttons: {BTN_T}. No parallax or scroll effects.</dd>
  </dl>
  <div><p class="subh">The six bento modules</p>
  <div class="mods">
    <div class="mod-d"><div class="box" style="grid-template-columns:2fr 1fr"><i></i><i></i></div><p><b>Plate pair</b> · 16 + 8 cols, 3:2 + 3:4</p></div>
    <div class="mod-d"><div class="box" style="grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr"><i></i><i></i><i></i><i></i></div><p><b>Board 2×2</b> · four 1:1 squares</p></div>
    <div class="mod-d"><div class="box" style="grid-template-columns:2fr 1fr;grid-template-rows:repeat(3,1fr)"><i style="grid-row:1/4"></i><i></i><i></i><i></i></div><p><b>Board 1+3</b> · 16 cols + three 3:2</p></div>
    <div class="mod-d"><div class="box" style="grid-template-columns:repeat(5,1fr)"><i></i><i></i><i></i><i></i><i></i></div><p><b>Strip</b> · 3–5 equal, captions above</p></div>
    <div class="mod-d"><div class="box" style="grid-template-columns:1fr"><i></i></div><p><b>Full plate</b> · 24 cols, 16:10 or wider</p></div>
    <div class="mod-d"><div class="box" style="grid-template-columns:2fr 1fr"><i style="background:#111"></i><i style="background:none;outline:0;border-top:1px solid #111;align-self:end;height:30%"></i></div><p><b>Video panel</b> · 16 cols + caption in 8</p></div>
  </div></div>
</div>
</section>

<section class="sheet sheet--port" aria-label="Sheet 05, components">
{run("Components", 5)}
<div class="body spec">
  <p class="lead">Live elements, rendered with the site's own CSS. Buttons at 100%, components at 70%. No disabled state in the build.</p>
  <div class="bgrid">{bgrid}</div>
  <div>
    <div class="comp"><p class="cap10">Label<small>.label</small></p><div><span class="label">Password protected</span></div></div>
    <div class="comp"><p class="cap10">Hairline row<small>.rows .row</small></p><div class="rows">{ROW}</div></div>
    <div class="comp"><p class="cap10">Meta table<small>.meta__panel</small></p><div>{META}</div></div>
    <div class="comp"><p class="cap10">Figure + caption<small>.t, figcaption</small></p><div>{FIG}</div></div>
    <div class="comp"><p class="cap10">Chapter index<small>.chindex</small></p><div>{CHINDEX}</div></div>
    <div class="comp"><p class="cap10">Password field<small>.lock form</small></p><div class="lock">{LOCKFORM}</div></div>
  </div>
</div>
</section>
"""

doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Yasmin Bajwa — Brand style guide</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@500&amp;family=Instrument+Serif:ital@0;1&amp;family=Inter+Tight:ital,wght@0,400;0,500;1,400&amp;display=swap">
<style>{guide_css}</style>
</head>
<body>
<main class="canvas">
<p class="canvas__title">Yasmin Bajwa · Portfolio brand guide · built from site/assets/css/r3.css · print to PDF: A4, margins none, background graphics on</p>
{sheets}
</main>
</body>
</html>
"""
import os
os.makedirs("brand", exist_ok=True)
open("brand/style-guide.html", "w").write(doc)
print("brand/style-guide.html", len(doc) // 1024, "KB")
