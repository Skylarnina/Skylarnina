"""Rounds 3-4: generate the six prototype pages from content/copy.json + content/site.json.
Round 4: every image sits in one of six bento modules (pair, board, one3, strip, full,
video); drawings/screens/documents are exported as finished tiles (whole, on #F4F3F0,
24px padding in the file) into site/assets/img/tiles/. Writes MODULE-MAP.md.

Run from yasmin/:  python3 tools/build_r3.py
Every element that carries Yasmin's copy has data-id="<inventory id>", so
tools/copy_check.py can prove each item is on the page, exact, visible and in order.
Words that are not hers carry data-added="caption|supplied|ui". No JavaScript.
"""
import html, json

c = json.load(open("content/copy.json"))
site = json.load(open("content/site.json"))
E = lambda s: html.escape(s, quote=True)
IMG = "assets/img/"
IMG_DIR = "site/assets/img/"
VID = "assets/video/"
CAPTIONS = []          # (page, fig label, caption) for COPY-CHECK "Added captions"

ROOMS = [
    dict(key="room01", pre="J", slug="room-01-jackson-home", short="Jackson Home", tone="dark"),
    dict(key="room02", pre="P", slug="room-02-power-energy", short="Power & Energy", tone="dark"),
    dict(key="room03", pre="R", slug="room-03-rhode-island", short="Rhode Island", tone="light"),
    dict(key="room04", pre="L", slug="room-04-littelfuse", short="Littelfuse", tone="light"),
]
for r in ROOMS:
    r["items"] = [dict(it, id=f"{r['pre']}-{i + 1:03d}") for i, it in enumerate(c[r["key"]])]
    r["title"] = r["items"][0]
    r["role"] = next(it for it in r["items"] if it["type"] == "meta" and it["label"] == "Role")
    r["methods"] = next(it for it in r["items"] if it["type"] == "meta" and it["label"] == "Methods")
DOCID = {(r["key"], it["doc"]): it["id"] for r in ROOMS for it in r["items"] if it["type"] == "figure"}

# ---------------------------------------------------------------- figures (her doc images)
# kind: "doc" = drawing, screen or document (placed whole on #F4F3F0, never cropped)
#       "photo" = photograph (may be cropped to the module ratio)
FIG = {
    1: ("r01-chart-onsite-box.jpg", "Time spent on-site by visitor type", "doc"),
    2: ("r01-chart-dataset-full.jpg", "Congestion, queue sizes, visit time and delays", "doc"),
    3: ("r01-plan-plain.jpg", "Jackson Home floor plan", "doc"),
    4: ("r01-plan-annex.jpg", "The Annex floor plan, with site entrance, entrance line and vestibule", "doc"),
    5: ("r01-plan-paths.jpg", "Jackson Home floor plan with expected visitor paths", "doc"),
    6: ("r01-chart-arrivals-random.jpg", "Arrivals spread randomly through the ticketing window", "doc"),
    7: ("r01-chart-arrivals-ontime.jpg", "Arrivals at the start of the ticketing window", "doc"),
    8: ("r3-fig-visit-times.jpg", "Expected visit times by visitor type", "doc"),
    9: ("r01-chart-docent.jpg", "Skipped exhibits, without and with docent control", "doc"),
    10: ("r01-chart-best-full.jpg", "Best scenario: 20 tickets, 8 walk-ups, with docent control", "doc"),
    11: ("r02-concept-board.jpg", "Content themes and experience flow for the column", "doc"),
    12: ("r4-whiteboard-stack.jpg", "Lo-fi sketches and wireframes for the column", "doc"),
    13: ("r02-itc-full.jpg", "ITC employee research: three roles", "doc"),
    14: ("r02-sides-full.jpg", "Content distribution across the sides of the column", "doc"),
    19: ("r03-goals-full.jpg", "Rhode Island Department of Health population health goals", "doc"),
    21: ("r03-annotated.jpg", "Vaccine details: annotated mobile screens", "doc"),
    22: ("r3-fig-decision-board.jpg", "Survey: who drives component decisions", "doc"),
    24: ("r04-journey-full.jpg", "Product-discovery journey map", "doc"),
}
# her archetype board (doc 23) is shown as its three archetype cards, whole, in a Board 2x2
FIG23 = [("r04-archetype-engineering.jpg", "User archetype: Engineering & Technical", "doc"),
         ("r04-archetype-sales.jpg", "User archetype: Sales", "doc"),
         ("r04-archetype-procurement.jpg", "User archetype: Procurement", "doc")]
REPLACED = {15, 16, 17, 18, 20}           # shown as the video / vector drawing her note asks for
MOVED = {5, 6, 9}                         # 5: Baseline spread; 6 and 9: the Scenario Testing data board
TILE_DIR = "tiles/"
FIGMAP = {}                               # page -> {inventory id: [captions shown for it]}
MODLOG = []                               # every module, for MODULE-MAP.md and the order rule


class Page:
    def __init__(self, name):
        self.name, self.n, self.ch, self.mods = name, 0, "", []

    def label(self):
        self.n += 1
        return f"Fig. {self.n:02d}"


# Module widths at 1440px (the 24-column content width is 1344px, module gutters 24px).
CONTENT = 1344
MG = 24


def export_tile(src, kind, ratio, disp_w, pad_css=MG):
    """A finished tile for the module slot: drawings/screens/documents whole on the light
    ground with 24px (display) padding inside the file; photographs cropped to the ratio.
    ratio=None keeps the image's own ratio (plus padding). Returns the tile's file name."""
    from PIL import Image
    Image.MAX_IMAGE_PIXELS = None
    im = Image.open(IMG_DIR + src).convert("RGB")
    W = min(2400, round(disp_w * 2))
    pad = round(pad_css * W / disp_w)
    tag = ("nat" if ratio is None else f"{ratio:.3f}".replace(".", "_")) + ("" if pad_css == MG else f"-p{pad_css}")
    name = f"{TILE_DIR}{src.rsplit('.', 1)[0]}--{tag}.jpg"
    if kind == "photo":
        r = ratio or im.width / im.height
        w, h = im.size
        if w / h > r:
            nw = round(h * r); x = (w - nw) // 2; im = im.crop((x, 0, x + nw, h))
        else:
            nh = round(w / r); y = (h - nh) // 2; im = im.crop((0, y, w, y + nh))
        out = im.resize((W, round(W / r)), Image.LANCZOS)
    else:
        if ratio is None:
            s = (W - 2 * pad) / im.width
            H = round(im.height * s) + 2 * pad
        else:
            H = round(W / ratio)
            s = min((W - 2 * pad) / im.width, (H - 2 * pad) / im.height)
        iw, ih = round(im.width * s), round(im.height * s)
        out = Image.new("RGB", (W, H), (244, 243, 240))
        out.paste(im.resize((iw, ih), Image.LANCZOS), ((W - iw) // 2, (H - ih) // 2))
    out.save(IMG_DIR + name, quality=85, optimize=True, progressive=True)
    return name


def tile(pg, src, cap, kind, ratio, disp_w, src_id=None, cls="", pad_css=MG):
    """One captioned tile. The page shows the finished tile; a click opens her full image."""
    lab = pg.label()
    CAPTIONS.append((pg.name, lab, cap))
    if src_id:
        FIGMAP.setdefault(pg.name, {}).setdefault(src_id, []).append(cap)
    t = export_tile(src, kind, ratio, disp_w, pad_css)
    pg.tiles.append(dict(label=lab, src=src, tile=t, cap=cap, kind=kind, src_id=src_id))
    style = f' style="aspect-ratio:{ratio:.4f}"' if ratio else ""
    return (f'<figure class="t{(" " + cls) if cls else ""}"><a class="m" href="{IMG}{src}"{style} target="_blank" rel="noopener" '
            f'aria-label="Open full image: {E(cap)}"><img src="{IMG}{t}" alt="{E(cap)}" loading="lazy"></a>'
            f'<figcaption data-added="caption">{lab} — {E(cap)}</figcaption></figure>')


def module(pg, typ, inner, note="", tag="div", extra="", style=""):
    pg.mods.append(typ)
    MODLOG.append(dict(page=pg.name, chapter=pg.ch, module=typ, tiles=pg.tiles, note=note))
    pg.tiles = []
    st = f' style="{style}"' if style else ""
    return f'<{tag} class="mod mod--{typ}{extra} b full mt" data-module="{typ}"{st}>{inner}</{tag}>'


def start(pg):
    pg.tiles = []


# ---- the six modules ------------------------------------------------------------------
W_PAIR_WIDE, W_PAIR_TALL = (CONTENT - MG) * 2 / 3, (CONTENT - MG) / 3
W_HALF = (CONTENT - MG) / 2


def m_pair(pg, wide, tall, tall_first=False, note=""):
    """Plate pair: one wide (16 cols, 3:2) + one tall (8 cols, 3:4): the same height."""
    start(pg)
    parts = [("w", wide), ("t", tall)]
    if tall_first:
        parts.reverse()
    html_ = "".join(f(W_PAIR_WIDE if k == "w" else W_PAIR_TALL, 3 / 2 if k == "w" else 3 / 4, "t--wide" if k == "w" else "t--tall")
                    for k, f in parts)
    return module(pg, "pair", html_, note, extra=" mod--pair-r" if tall_first else "")


def m_board(pg, fns, note=""):
    """Board 2x2: four equal squares, a caption under each; each opens full size."""
    start(pg)
    return module(pg, "board", "".join(f(W_HALF, 1.0, "") for f in fns), note)


def m_one3(pg, large, smalls, note=""):
    """Board 1+3: one large (16 cols, the full height) + three small stacked (8 cols)."""
    start(pg)
    inner = large(W_PAIR_WIDE, None, "t--large") + "".join(f(W_PAIR_TALL, 3 / 2, "") for f in smalls)
    return module(pg, "one3", inner, note)


def m_strip(pg, fns, ratio, note=""):
    """Strip: three to five equal tiles in one row, captions above (A8)."""
    start(pg)
    n = len(fns)
    w = (CONTENT - MG * (n - 1)) / n
    return module(pg, "strip", "".join(f(w, ratio, "") for f in fns), note, style=f"--n:{n}")


def m_full(pg, fn, note=""):
    """Full plate: one image across all 24 columns, on the light ground."""
    start(pg)
    return module(pg, "full", fn(CONTENT, "plate", ""), note)


def m_video(pg, src, poster, cap, rt, vertical=False, src_id=None, note=""):
    """Video panel: the video at 16 cols, its caption and running time in the other 8 (A5)."""
    start(pg)
    lab = pg.label()
    CAPTIONS.append((pg.name, lab, cap + " (video)"))
    if src_id:
        FIGMAP.setdefault(pg.name, {}).setdefault(src_id, []).append(cap + " (video)")
    pg.tiles.append(dict(label=lab, src=src, tile=poster, cap=cap + " (video)", kind="video", src_id=src_id))
    inner = (f'<div class="v{" v--tall" if vertical else ""}"><video src="{VID}{src}" poster="{IMG}{poster}" controls muted playsinline preload="metadata"></video></div>'
             f'<figcaption data-added="caption"><span>{lab} — {E(cap)}</span><span class="rt">Running time {rt}</span></figcaption>')
    return module(pg, "video", inner, note, tag="figure", extra=" mod--video-v" if vertical else "")


def T(src, cap, kind="doc", src_id=None):
    """A tile factory for module functions: f(disp_w, ratio, cls)."""
    def f(disp_w, ratio, cls):
        if ratio == "plate":                      # full plate: at least 16:10, taller drawings sit whole inside
            from PIL import Image
            im = Image.open(IMG_DIR + src)
            ratio_ = max((im.width + 96) / (im.height + 96), 1.6)
            return tile(pg_now[0], src, cap, kind, ratio_, disp_w, src_id, cls)
        return tile(pg_now[0], src, cap, kind, ratio, disp_w, src_id, cls)
    return f


def D(room, d):
    src, cap, kind = FIG[d]
    return T(src, cap, kind, DOCID[(room, d)])


pg_now = [None]


# ---------------------------------------------------------------- her production notes -> media
def note_html(pg, it):
    t, nid = it["text"], it["id"]
    if t.startswith("INSERT VIDEO HERE - DISCRETE EVENT SIMULATION"):
        return m_video(pg, "r01-simulation.mp4", "poster-r01-simulation.jpg", "Discrete event simulation of visitor flow", "0:48", src_id=nid)
    if t.startswith("INSERT VIDEO HERE BELOW IS SCREEN GRAB"):
        return m_video(pg, "r02-interface.mp4", "poster-r02-interface.jpg", "Final interface and user flow", "0:22", src_id=nid)
    if t.startswith("INSERT POWER & ENERGY VIDEO HERE"):
        return m_video(pg, "r02-cms.mp4", "poster-r02-cms.jpg", "CMS channels in Appspace", "0:11", src_id=nid)
    if t.startswith("USE PDF VERSION HERE OF DRAWINGS"):
        return m_one3(pg, T("r02-shop-1.jpg", "Shop drawing, column surround: plan, section and perspective", src_id=nid),
                      [T("r02-shop-2.jpg", "Shop drawing: elevations and sections", src_id=nid),
                       T("r02-shop-3.jpg", "Shop drawing: typical column surround and plan", src_id=nid),
                       T("r02-shop-1-detail.jpg", "Shop drawing, detail: column plan view", src_id=nid)])
    if t.startswith("ADD COLUMN FABRICATION VIDEO HERE"):
        return m_video(pg, "r02-fabrication.mp4", "poster-r02-fabrication.jpg", "Column fabrication progression", "0:14", src_id=nid)
    if t.startswith("ADD Final Results video here"):
        return m_video(pg, "r02-final-setup.mp4", "poster-r02-final-setup.jpg", "Final setup: the installed column", "0:21", vertical=True, src_id=nid)
    if t.startswith("INSERT VIDEO OF APP STORE REVIEWS HERE"):
        return m_video(pg, "r03-app-reviews.mp4", "poster-r03-app-reviews.jpg", "App Store and Google Play reviews", "0:23", vertical=True, src_id=nid)
    if t.startswith("INSERT PDF OR VIDEO OF DESKTOP & MOBILE WIRE FRAMES HERE"):
        return m_video(pg, "r03-wireframes.mp4", "poster-r03-wireframes.jpg", "Desktop wireframes", "0:23", src_id=nid)
    if t.startswith("INSERT WIREFRAMES FROM PDF HERE"):
        start(pg)
        lab = pg.label()
        CAPTIONS.append((pg.name, lab, "Littelfuse wireframes (placeholder)"))
        FIGMAP.setdefault(pg.name, {}).setdefault(nid, []).append("Littelfuse wireframes (placeholder)")
        pg.tiles.append(dict(label=lab, src="—", tile="—", cap="Littelfuse wireframes (placeholder)", kind="placeholder", src_id=nid))
        return module(pg, "full", f'<figure class="t"><div class="m placeholder"><span class="label" data-added="placeholder">'
                      f'Littelfuse wireframes — pending export from Adobe XD</span></div>'
                      f'<figcaption data-added="caption">{lab} — Littelfuse wireframes (placeholder)</figcaption></figure>',
                      "Placeholder until she exports the XD screens (ASSET-GAPS).")
    raise KeyError(t)


def note_id(room, prefix):
    return next(x["id"] for x in next(r for r in ROOMS if r["key"] == room)["items"] if x["type"] == "note" and x["text"].startswith(prefix))


# ---- figure runs in her text -> modules (keyed by the docs in the run, after REPLACED/MOVED)
RUNS = {
    ("room01", (1, 2)): lambda pg: m_pair(pg, D("room01", 2), D("room01", 1), tall_first=True),
    ("room01", (3, 4)): lambda pg: m_pair(pg, D("room01", 4), D("room01", 3), tall_first=True),
    ("room01", ()): lambda pg: "",
    ("room01", (7, 8)): lambda pg: m_board(pg, [D("room01", d) for d in (6, 7, 8, 9)],
                                           "Figs 6 and 9 moved here so the four scenario charts read as one set."),
    ("room02", (11, 12)): lambda pg: m_pair(pg, D("room02", 11), D("room02", 12)),
    ("room02", (13,)): lambda pg: m_full(pg, D("room02", 13)),
    ("room02", (14,)): lambda pg: m_full(pg, D("room02", 14)),
    ("room02", ()): lambda pg: "",
    ("room03", (19,)): lambda pg: m_full(pg, D("room03", 19)),
    ("room03", ()): lambda pg: "",
    ("room03", (21,)): lambda pg: m_pair(pg, D("room03", 21),
                                         T("r4-ri-screens.jpg", "Mobile wireframes: vaccination record and dose details",
                                           src_id=note_id("room03", "INSERT PDF OR VIDEO OF DESKTOP")),
                                         note="Tall slot: the frameless mobile screens from her vector PDF (Q7)."),
    ("room04", (22, 23)): lambda pg: m_board(pg, [D("room04", 22)] + [T(s, c_, k, DOCID[("room04", 23)]) for s, c_, k in FIG23],
                                             "Her archetype board (doc 23) shown as its three cards, whole.")
                                     + m_video(pg, "r04-personas.mp4", "poster-r04-personas.jpg", "Engineering personas", "0:20",
                                               note="Added media (Q6): directly under the archetype board."),
    ("room04", (24,)): lambda pg: m_full(pg, D("room04", 24)),
}


# ---------------------------------------------------------------- her text -> HTML
def text_html(it, cls="b"):
    t, i = it["text"], it["id"]
    typ = it["type"]
    if typ == "p":
        return f'<p class="{cls}" data-id="{i}">{E(t)}</p>'
    if typ == "h3":
        return f'<h3 class="{cls}" data-id="{i}">{E(t)}</h3>'
    if typ == "h4":
        run = " run" if t.lower().startswith("how might we") else ""
        return f'<h4 class="{cls}{run}" data-id="{i}">{E(t)}</h4>'
    if typ == "hmw":
        return f'<p class="{cls} hmw" data-id="{i}">{E(t)}</p>'
    if typ == "quote":
        k = t.find(":")
        return f'<blockquote class="{cls}" data-id="{i}"><b>{E(t[:k + 1])}</b>{E(t[k + 1:])}</blockquote>'
    raise KeyError(typ)


def list_html(lis, cls="b", ordered=False):
    """Nested list from flat items with levels 1-3."""
    tag = "ol" if ordered else "ul"
    out, depth = [], 0
    for it in lis:
        lv = it.get("level", 1)
        if lv > depth:
            out.append((f'<{tag} class="{cls}">' if depth == 0 else f"<{tag}>") * (lv - depth))
        elif lv < depth:
            out.append(f"</li></{tag}>" * (depth - lv) + "</li>")
        elif depth:
            out.append("</li>")
        out.append(f'<li><span data-id="{it["id"]}">{E(it["text"])}</span>')
        depth = lv
    out.append(f"</li></{tag}>" * depth)
    return "".join(out)


def stats_html(it):
    rows = it["rows"]
    heads = it["head"]
    cells = "".join(
        f'<div><span class="num">{E(r[2])}</span><span class="name">{E(r[0])}</span><span class="char">{E(r[1])}</span></div>'
        for r in rows)
    return (f'<div class="stats" data-id="{it["id"]}" data-kind="table">'
            f'<p class="heads label">{" ".join(f"<span>{E(h)}</span>" for h in (heads[2], heads[0], heads[1]))}</p>{cells}</div>')


def body(pg, items, room, ordered_lists=False):
    """Default flow for a run of items: text in the 12-col measure, media in modules."""
    out, i = [], 0
    while i < len(items):
        it = items[i]
        typ = it["type"]
        if typ == "li":
            j = i
            while j < len(items) and items[j]["type"] == "li":
                j += 1
            run = items[i:j]
            out.append(list_html(run, "b nl" if ordered_lists else "b", ordered_lists))
            if room == "room02" and any(x["text"].startswith("Artifact interpretation:") for x in run):
                out.append(sides_strip(pg))
            i = j
            continue
        if typ == "figure":
            j, docs = i, []
            while j < len(items) and items[j]["type"] == "figure":
                d = items[j]["doc"]
                if d not in REPLACED and d not in MOVED:
                    docs.append(d)
                j += 1
            out.append(RUNS[(room, tuple(docs))](pg))
            i = j
            continue
        if typ == "note":
            out.append(note_html(pg, it))
        elif typ == "table":
            out.append(stats_html(it))
        else:
            out.append(text_html(it))
        i += 1
    return "".join(out)


def sides_strip(pg):
    sides = [("r02-side-wayfinding.jpg", "Exhibit wayfinding"), ("r02-side-stories.jpg", "Innovation stories"),
             ("r02-side-map.jpg", "Interactive exploration"), ("r02-side-careers.jpg", "Career discovery"),
             ("r02-side-artifacts.jpg", "Artifact interpretation")]
    return m_strip(pg, [T(s, f"Column side: {c_}") for s, c_ in sides], 9 / 32,
                   "Added media (Q6). Five tiles, not three or four: the column has five sides and the set reads as one object.")


# ---------------------------------------------------------------- chapter layouts
def head(no, h2, cls="ch-head"):
    return f'<header class="{cls}"><span class="no" data-added="ui">{no:02d}</span><h2 data-id="{h2["id"]}">{E(h2["text"])}</h2></header>'


def ch_default(pg, no, h2, items, room, **kw):
    return f'<div class="wrap g24">{head(no, h2)}{body(pg, items, room, **kw)}</div>'


def ch_spread(pg, no, h2, items, room, plan_doc):
    """A14 spread, kept from round 3: her plan beside the baseline list it illustrates."""
    start(pg)
    src, cap, kind = FIG[plan_doc]
    plan = tile(pg, src, cap, kind, 2 / 3, (CONTENT - 13 * 16) * 11 / 24 + 10 * 16, DOCID[(room, plan_doc)], "spread__plan")
    MODLOG.append(dict(page=pg.name, chapter=pg.ch, module="spread", tiles=pg.tiles,
                       note="Not a run of images: one plan beside the list it illustrates (round-3 A14 spread, kept)."))
    pg.tiles = []
    return f'<div class="wrap g24 spread">{plan}{head(no, h2)}{body(pg, items, room)}</div>'


def ch_findings(pg, no, h2, items, room):
    """Jackson Home Findings: her sub-headed findings as a numbered 01-0n list, then the best-scenario plate."""
    text = [x for x in items if x["type"] != "figure"]
    groups, cur = [], None
    for x in text:
        if x["type"] == "h3":
            cur = [x]; groups.append(cur)
        else:
            cur.append(x)
    lis = "".join("<li>" + "".join(text_html(y, "") for y in g) + "</li>" for g in groups)
    return (f'<div class="wrap g24">{head(no, h2)}<ol class="b nl">{lis}</ol>'
            f'{m_full(pg, D(room, 10))}</div>')


def ch_reflection(pg, no, h2, items, room):
    ps = "".join(f'<p class="q" data-id="{x["id"]}">{E(x["text"])}</p>' for x in items)
    return (f'<div class="wrap reflection"><p class="label" data-added="ui">{no:02d}</p>'
            f'<h2 class="kicker" data-id="{h2["id"]}">{E(h2["text"])}</h2>{ps}<p class="label" data-added="ui">—</p></div>')


def ch_littelfuse_approach(pg, no, h2, items, room):
    """Littelfuse 'The Approach': her audit items 01-03 laid out as an A7 numbered list."""
    a = next(k for k, x in enumerate(items) if x["type"] == "h4" and x["text"].startswith("Audited critical tasks"))
    b = next(k for k, x in enumerate(items) if x["type"] == "h4" and x["text"].startswith("Translated findings"))
    before, audit, after = items[:a], items[a:b], items[b:]
    intro, pairs = audit[:2], audit[2:]
    lis = "".join("<li>" + text_html(pairs[k], "") + text_html(pairs[k + 1], "") + "</li>" for k in range(0, len(pairs), 2))
    left = "".join(text_html(x, "") for x in intro)
    return (f'<div class="wrap g24">{head(no, h2)}{body(pg, before, room)}</div>'
            f'<div class="wrap g24 a7 mt-seg"><div class="a7__left a7__text">{left}</div>'
            f'<ol class="b nl plain">{lis}</ol></div>'
            f'<div class="wrap g24 seg">{body(pg, after, room)}</div>')


SPECIAL = {
    ("room01", "Building the Simulation"): lambda pg, n, h, it, r: ch_default(pg, n, h, it, r),
    ("room01", "Baseline Assumptions"): lambda pg, n, h, it, r: ch_spread(pg, n, h, it, r, 5),
    ("room01", "Findings"): ch_findings,
    ("room01", "Impact"): lambda pg, n, h, it, r: ch_default(pg, n, h, it, r, ordered_lists=True),
    ("room04", "The Approach"): ch_littelfuse_approach,
}


# ---------------------------------------------------------------- page shell
def page(title, desc, body_html, cls=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Sans:ital,wght@0,400;0,500;1,400&amp;family=Inter+Tight:ital,wght@0,400;0,500;1,400&amp;display=swap">
<link rel="stylesheet" href="assets/css/r3.css">
</head>
<body{f' class="{cls}"' if cls else ''}>
{body_html}
</body>
</html>
"""


def bar(over=None, here=""):
    cls = "bar" + (" bar--over" if over else "") + (" bar--ink" if over == "light" else "")
    cur = lambda k: ' aria-current="page"' if here == k else ""
    return (f'<header class="{cls}"><div class="wrap"><a class="bar__name" href="index.html" data-added="ui">Yasmin Bajwa</a>'
            f'<nav aria-label="Main" data-added="ui"><a href="projects.html"{cur("projects")}>Projects</a>'
            f'<a href="index.html#about">About</a><a href="index.html#contact">Contact</a></nav></div></header>')


def foot():
    return ('<footer class="foot" data-added="ui"><div class="wrap"><span>Yasmin Bajwa © 2026</span>'
            '<a class="u" href="#top">Back to top ↑</a></div></footer>')


# ---------------------------------------------------------------- homepage
def home():
    pg = Page("index")
    A = {f"A-{i + 1:02d}": it for i, it in enumerate(c["about"])}
    facts = "".join(
        f'<div><dt class="label" data-added="ui">{E(f["label"])}</dt><dd class="{"pending" if f.get("pending") else ""}" data-added="supplied">{E(f["value"])}</dd></div>'
        for f in site["home"]["facts"])
    # A10 + round 5: four panels, each image always visible under a 45% black overlay; hover lightens it to 30%.
    PANEL = [("r4-panel-01.jpg", "The installed Power & Energy column", "photo"),
             ("r4-panel-02.jpg", "Rhode Island 401 Health app: two mobile screens", "doc"),
             ("r4-panel-03.jpg", "Jackson Home floor plan with expected visitor paths", "doc"),
             ("r4-panel-04.jpg", "ITC employee research storyboard", "doc")]
    skills = [A[f"A-{k:02d}"] for k in (9, 10, 11, 12)]
    panels = ""
    for n, (s_, (src, alt, kind)) in enumerate(zip(skills, PANEL), 1):
        panels += (f'<article class="panel">'
                   f'<div class="m m--{kind}"><img src="{IMG}{src}" alt="{E(alt)}" loading="lazy"></div>'
                   f'<span class="no" data-added="ui">{n:02d}</span>'
                   f'<h3 data-id="A-{8 + n:02d}">{E(s_["text"])}</h3></article>')
    # A9 + A4: About bento. Work images stand in until she sends personal photos (ASSET-GAPS R4-1..4)
    MOSAIC = [("tall", "r4-about-tall-4x5.jpg", "Power & Energy column, installed at The Henry Ford"),
              ("wide", "r4-about-wide-3x2.jpg", "Installing the column in the Power & Energy gallery"),
              ("sqa", "r4-about-sq-a.jpg", "The gallery column before the build"),
              ("sqb", "r4-about-sq-b.jpg", "Column plan view, from the shop drawings")]
    mosaic = ""
    for slot, src, cap in MOSAIC:
        lab = pg.label()
        CAPTIONS.append(("index", lab, cap))
        mosaic += (f'<figure class="t t--{slot}"><div class="m"><img src="{IMG}{src}" alt="{E(cap)}" loading="lazy"></div>'
                   f'<figcaption data-added="caption">{lab} — {E(cap)}</figcaption></figure>')
    rows = ""
    for n, r in enumerate(ROOMS, 1):
        rows += (f'<a class="row fade" href="{r["slug"]}.html"><div class="row__t"><span class="label" data-added="ui">{n:02d}</span>'
                 f'<h3 data-ref="{r["title"]["id"]}">{E(r["title"]["text"])}</h3></div>'
                 f'<div class="row__role"><span data-ref="{r["role"]["id"]}">{E(r["role"]["text"])}</span>'
                 f'<span class="label" data-added="ui">Password protected</span></div>'
                 f'<div class="row__img"><div class="m m--fit"><img src="{IMG}{ROW[r["key"]]}" alt="" loading="lazy"></div></div></a>')
    b = f"""{bar(here="home")}
<main id="top">
<!-- A9 + A8: greeting, her About sentence, headshot and facts -->
<section class="wrap g24 hero">
  <h1 class="hero__hi" data-added="supplied">Hi, I’m <em>Yasmin.</em></h1>
  <div class="hero__about">
    <p class="kicker" data-id="A-05">{E(A["A-05"]["text"])}</p>
    <p data-id="A-06">{E(A["A-06"]["text"])}</p>
    <a class="btn" href="projects.html" data-added="ui">View Projects →</a>
  </div>
  <figure class="hero__photo"><div class="m"><img src="{IMG}portrait-4x5.jpg" alt="Yasmin Bajwa"></div>
    <figcaption class="label" data-added="caption">Digital Exhibit Designer — The Henry Ford</figcaption></figure>
  <dl class="facts">{facts}</dl>
</section>
<hr class="hairline">

<!-- A9 auren + A4 Finnhütte: About bento on the light ground. Statement left 12, mosaic right 12 -->
<section class="section section--alt" id="about"><div class="wrap g24 about">
  <p class="about__statement" data-id="A-07">{E(A["A-07"]["text"])}</p>
  <div class="about__right">
    <div class="mosaic">{mosaic}</div>
    <p class="about__tags" data-added="ui"><span>History</span><span aria-hidden="true">·</span><span>Fashion</span><span aria-hidden="true">·</span><span>Art</span></p>
  </div>
</div></section>

<!-- A10: four equal vertical panels, her four skills in her order; image revealed on hover -->
<section class="panels" aria-label="Disciplines">{panels}</section>

<!-- A3: project rows with hairlines -->
<section class="section" id="projects"><div class="wrap">
  <div class="projects-head"><h2 data-added="ui">Projects</h2><a class="u" href="projects.html" data-added="ui">All projects →</a></div>
  <div class="rows">{rows}</div>
</div></section>

<!-- Contact -->
<section class="section section--alt" id="contact"><div class="wrap contact">
  <p class="label" data-added="ui">Contact</p>
  <h2 data-added="supplied">{E(site["home"]["contact_heading"])}</h2>
  <p class="contact__links" data-added="ui"><a class="u" href="mailto:">Email</a> <span class="pending">[email — pending client]</span>
    <a class="u" href="#linkedin">LinkedIn</a> <span class="pending">[URL — pending client]</span>
    <a class="u" href="#resume">Résumé</a> <span class="pending">[PDF — pending client]</span></p>
</div></section>
</main>
{foot()}"""
    return page("Yasmin Bajwa", A["A-06"]["text"][:150], b)


# ---------------------------------------------------------------- projects page (A13)
def projects():
    cards = ""
    for n, r in enumerate(ROOMS, 1):
        cards += (f'<a class="card fade" href="{r["slug"]}.html"><div class="m m--fit"><img src="{IMG}{ROW[r["key"]]}" alt="" loading="lazy"></div>'
                  f'<span class="label" data-added="ui">{n:02d} · Password protected</span>'
                  f'<h2 data-ref="{r["title"]["id"]}">{E(r["title"]["text"])}</h2>'
                  f'<p data-ref="{r["role"]["id"]}">{E(r["role"]["text"])}</p></a>')
    b = f"""{bar(here="projects")}
<main id="top" class="wrap">
  <h1 class="p-title" data-added="ui">Projects</h1>
  <div class="grid2">{cards}</div>
  <div style="height:var(--section)"></div>
</main>
{foot()}"""
    return page("Projects — Yasmin Bajwa", "Four case studies.", b)


# ---------------------------------------------------------------- case study template
COVER = {"room01": "r3-cover-r01-16x7.jpg",      # simulation still (footage): cropped to 16:7
         "room02": "r3-cover-r02-16x7.jpg",      # photograph: cropped to 16:7
         }
# Round 5: document rooms get a white header (no image behind the title) and their cover
# shown whole as FIG. 01, a full plate with 48px padding directly under the chapter index.
COVER_PLATE = {"room03": ("r5-ri-five-screens.jpg", "401 Health app: five mobile screens"),
               "room04": ("r04-journey-full.jpg", "Product-discovery journey map: overview")}
ROW = {k: f"r4-row-{k.replace('room0', 'r0')}-3x2.jpg" for k in ("room01", "room02", "room03", "room04")}


def case(r):
    pg = Page(r["slug"])
    pg_now[0] = pg
    items = r["items"]
    sv = site["rooms"][r["key"]]
    # split into chapters at H2
    chapters, cur = [], None
    for it in items[3:]:                          # after title, Role, Methods
        if it["type"] == "h2":
            cur = [it, []]; chapters.append(cur)
        else:
            cur[1].append(it)
    index = "".join(f'<li><span>{k:02d}</span><a href="#ch-{k}">{E(h["text"])}</a></li>' for k, (h, _) in enumerate(chapters, 1))
    year_cls = "pending" if sv.get("year_pending") else ""
    tone = r["tone"]
    doc = r["key"] in COVER_PLATE
    meta = f"""<dl class="meta__panel">
  <div class="wide"><dt class="label" data-added="ui">Role</dt><dd data-id="{r["role"]["id"]}">{E(r["role"]["text"])}</dd></div>
  <div class="wide"><dt class="label" data-added="ui">Methods</dt><dd data-id="{r["methods"]["id"]}">{E(r["methods"]["text"])}</dd></div>
  <div><dt class="label" data-added="ui">Setting</dt><dd data-added="supplied">{E(sv["setting"])}</dd></div>
  <div><dt class="label" data-added="ui">Year</dt><dd class="{year_cls}" data-added="supplied">{E(sv["year"])}</dd></div>
</dl>"""
    title = f'<h1 class="{"dochead__title" if doc else "cover__title"}" data-id="{r["title"]["id"]}">{E(r["title"]["text"])}</h1>'
    if doc:
        header = (f'<!-- A1, document cover: white header, title left, meta table right, no image behind -->\n'
                  f'<section class="wrap g24 dochead">{title}{meta}</section>')
        src, cap = COVER_PLATE[r["key"]]
        pg.ch = "Cover"
        start(pg)
        plate = ('<!-- the cover, whole: FIG. 01, full plate on the light ground, 48px padding -->\n'
                 '<section class="wrap g24 coverplate">'
                 + module(pg, "full", tile(pg, src, cap, "doc", None, CONTENT, None, "", 48),
                          "Round 5: the document cover, shown whole under the chapter index (no image behind the title).")
                 + '</section>')
    else:
        header = (f'<!-- A1 + A4: full-bleed photo cover with the title on it, meta panel bottom-right -->\n'
                  f'<section class="cover cover--{tone}"><div class="m"><img src="{IMG}{COVER[r["key"]]}" alt=""></div>\n  {title}</section>\n'
                  f'<div class="meta"><div class="wrap g24">{meta}</div></div>')
        plate = ""
    parts = []
    for k, (h, its) in enumerate(chapters, 1):
        pg.ch = f"{k:02d} {h['text']}"
        if h["text"] == "Reflection":
            inner = ch_reflection(pg, k, h, its, r["key"])
            parts.append(f'<section class="chapter section--alt reflection-sec" id="ch-{k}" style="padding-block:var(--section);margin-top:var(--section)">{inner}</section>')
            continue
        fn = SPECIAL.get((r["key"], h["text"]))
        inner = fn(pg, k, h, its, r["key"]) if fn else ch_default(pg, k, h, its, r["key"])
        parts.append(f'<section class="chapter" id="ch-{k}">{inner}</section>')
    i = ROOMS.index(r)
    prv, nxt = ROOMS[i - 1], ROOMS[(i + 1) % 4]
    b = f"""{bar(over=None if doc else tone, here="projects")}
<main id="top">
{header}
<!-- A1: numbered chapter index built from her own headings -->
<nav class="wrap" aria-label="Chapters" data-added="ui"><div class="chindex"><ol>{index}</ol></div></nav>
{plate}
<!-- A2 + A3 chapters; A4 / A5 / A6 / A7 where her content calls for them -->
{"".join(parts)}
<!-- A5: previous / all / next -->
<nav class="pn" aria-label="More projects" data-added="ui"><div class="wrap g24">
  <a class="prev" href="{prv["slug"]}.html"><span class="label">← Previous project</span><span class="t">{E(prv["title"]["text"])}</span></a>
  <a class="all" href="projects.html"><span class="label">All projects</span></a>
  <a class="next" href="{nxt["slug"]}.html"><span class="label">Next project →</span><span class="t">{E(nxt["title"]["text"])}</span></a>
</div></nav>
</main>
{foot()}"""
    return page(f"{r['short']} — Yasmin Bajwa", r["title"]["text"], b, "case")


# ---------------------------------------------------------------- lock screen
def lock():
    b = f"""<main class="lock" id="wrong">
  <div class="lock__bg"><img src="{IMG}r01-plan-plain.jpg" alt=""></div>
  <p class="lock__top" data-added="ui">Yasmin Bajwa</p>
  <div class="lock__box" data-added="ui">
    <h1>Projects are shared <em>by invitation.</em></h1>
    <p>Enter the password to continue.</p>
    <form action="private-view.html#wrong" method="get">
      <label class="label" for="pw">Password</label>
      <input type="password" id="pw" name="pw" autocomplete="current-password">
      <button class="btn btn--solid" type="submit">Enter</button>
      <p class="err" role="alert">Incorrect password.</p>
    </form>
    <p class="lock__ask">No password? <a class="u" href="mailto:?subject=Portfolio%20access">Email Yasmin →</a></p>
  </div>
  <p class="lock__foot" data-added="ui">© 2026 Yasmin Bajwa</p>
</main>"""
    return page("Private View — Yasmin Bajwa", "Projects are shared by invitation.", b)


MODULE_NAMES = {"pair": "Plate pair", "board": "Board 2×2", "one3": "Board 1+3", "strip": "Strip",
                "full": "Full plate", "video": "Video panel", "spread": "Spread (round-3 A14, kept)"}
SQS = {"pair": "Fluid Engine row: image block 16 cols + image block 8 cols, same height",
       "board": "Gallery section → Grid: Simple, 2 columns, 1:1, lightbox on",
       "one3": "Fluid Engine row: one image block 16 cols × 3 rows tall + three image blocks 8 cols",
       "strip": "Gallery section → Grid: Simple, n columns, captions above (or a Fluid Engine row)",
       "full": "Fluid Engine row: one image block, 24 cols",
       "video": "Fluid Engine row: video block 16 cols + text block 8 cols",
       "spread": "Fluid Engine: image block 11 cols beside text blocks"}


def rule_check():
    """Never more than two modules of the same type in a row (per page, text between ignored)."""
    bad = []
    for r in ROOMS:
        seq = [m["module"] for m in MODLOG if m["page"] == r["slug"] and m["module"] != "spread"]
        for k in range(len(seq) - 2):
            if seq[k] == seq[k + 1] == seq[k + 2]:
                bad.append((r["slug"], k, seq[k]))
    return bad


def module_map():
    L = ["# Module map (round 4)", "",
         "Every image and video on the four case-study pages, the module it sits in, and why. "
         "Generated by `tools/build_r3.py` (do not edit by hand; edit the `RUNS` table and re-run).", "",
         "## The six modules", "",
         "| Module | Layout (24-col grid, 24px gutters) | Use it for | Squarespace |", "|---|---|---|---|",
         "| **Plate pair** | one wide 16 cols (3:2) + one tall 8 cols (3:4), same height; may be mirrored to keep her figure order | a plan beside a detail, a photo beside a drawing | " + SQS["pair"] + " |",
         "| **Board 2×2** | four equal squares, caption under each, each opens full size | chart sets, data walls | " + SQS["board"] + " |",
         "| **Board 1+3** | one large 16 cols (full height) + three small stacked 8 cols (3:2) | a key visual with supporting figures | " + SQS["one3"] + " |",
         "| **Strip** | three or four equal tiles in one row, captions above (A8) | column art panels, persona cards, wireframe screens | " + SQS["strip"] + " |",
         "| **Full plate** | one image across all 24 cols on the light ground, at least 16:10 | shop drawings, the journey map, the 23-goals table | " + SQS["full"] + " |",
         "| **Video panel** | video 16 cols; caption and running time in the other 8 (A5) | every video | " + SQS["video"] + " |", "",
         "**Rules applied to every tile:** drawings, screens and documents are placed whole (never cropped) on `#F4F3F0` "
         "with 24px padding. The padding and ground are *inside the exported tile* (`site/assets/img/tiles/`), "
         "so Squarespace needs no CSS for it. Photographs may be cropped to the module ratio. 24px gutters. "
         "A FIG. caption on every tile. Never more than two modules of the same type in a row.", ""]
    bad = rule_check()
    L.append("**Order rule check:** " + ("✔ no page has three modules of the same type in a row." if not bad else "✘ " + str(bad)))
    L.append("")
    for r in ROOMS:
        mods = [m for m in MODLOG if m["page"] == r["slug"]]
        seq = " → ".join(MODULE_NAMES[m["module"]] for m in mods)
        L += [f"## {r['short']} — `site/{r['slug']}.html`", "", f"Sequence: {seq}", "",
              "| # | Chapter | Module | Fig. | Caption | Her item | Source file | Tile (as placed) | Fit | Note |",
              "|---|---|---|---|---|---|---|---|---|---|"]
        for k, m in enumerate(mods, 1):
            for j, t in enumerate(m["tiles"]):
                fit = {"doc": "whole on #F4F3F0", "photo": "cropped to ratio", "video": "video", "placeholder": "placeholder"}[t["kind"]]
                L.append(f"| {k if j == 0 else ''} | {m['chapter'] if j == 0 else ''} | {MODULE_NAMES[m['module']] if j == 0 else ''} | "
                         f"{t['label']} | {t['cap']} | {t['src_id'] or '➕ added'} | `{t['src']}` | `{t['tile']}` | {fit} | {m['note'] if j == 0 else ''} |")
        L.append("")
    L += ["## Homepage (not modules, listed for completeness)", "",
          "| Where | File | Fit |", "|---|---|---|",
          "| Project rows + Projects grid | `r4-row-r01..r04-3x2.jpg` | finished 3:2, subject whole (plan, column ×3, two screens, journey map) |",
          "| Discipline panels 01–04 | `r4-panel-01..04.jpg` | 2:3; 01 photograph (cropped), 02–04 whole on #F4F3F0 |",
          "| About mosaic | `r4-about-tall-4x5.jpg`, `r4-about-wide-3x2.jpg`, `r4-about-sq-a.jpg`, `r4-about-sq-b.jpg` | stand-ins from her work until personal photos arrive (ASSET-GAPS R4-1..R4-4) |",
          "| Case-study covers | `r3-cover-r01/r02-16x7.jpg` (footage/photo, cropped to 16:7). Rooms 03/04 have no header image; their cover is FIG. 01 above | |", ""]
    open("MODULE-MAP.md", "w").write("\n".join(L) + "\n")
    return bad


def asset_map_section():
    """Rewrite the 'Round 4: module per image' section at the end of ASSET-MAP.md."""
    head = "## Round 4: module per image"
    L = [head, "", "Every image and video on the case-study pages, by source file, with the module it sits in "
         "(generated by `tools/build_r3.py`; details and reasons in `MODULE-MAP.md`).", "",
         "| Source file | Page | Fig. | Module | Tile placed | Fit |", "|---|---|---|---|---|---|"]
    for m in MODLOG:
        for t in m["tiles"]:
            fit = {"doc": "whole on #F4F3F0", "photo": "cropped to ratio", "video": "video", "placeholder": "placeholder"}[t["kind"]]
            L.append(f"| `{t['src']}` | {m['page']} | {t['label']} | {MODULE_NAMES[m['module']]} | `{t['tile']}` | {fit} |")
    L += ["", "Homepage (round 4): `r4-row-r01…r04-3x2.jpg` (rows + Projects grid), `r4-panel-01…04.jpg` (disciplines), "
          "`r4-about-*.jpg` (About mosaic), `r5-ri-five-screens.jpg` (Rhode Island cover plate). All made by `tools/build_r4_assets.py`.", ""]
    s = open("ASSET-MAP.md").read()
    if head in s:
        s = s[:s.index(head)]
    open("ASSET-MAP.md", "w").write(s.rstrip() + "\n\n" + "\n".join(L))


if __name__ == "__main__":
    import os
    os.makedirs(IMG_DIR + TILE_DIR, exist_ok=True)
    open("site/index.html", "w").write(home())
    open("site/projects.html", "w").write(projects())
    for r in ROOMS:
        open(f"site/{r['slug']}.html", "w").write(case(r))
    open("site/private-view.html", "w").write(lock())
    json.dump(CAPTIONS, open("content/captions.json", "w"), indent=1, ensure_ascii=False)
    json.dump(FIGMAP, open("content/figmap.json", "w"), indent=1, ensure_ascii=False)
    bad = module_map()
    json.dump(MODLOG, open("content/modules.json", "w"), indent=1, ensure_ascii=False)
    asset_map_section()
    print("pages written;", len(CAPTIONS), "captions;", len(MODLOG), "modules; order rule:", "ok" if not bad else bad)
