"""Round 3: generate the six prototype pages from content/copy.json + content/site.json.

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

# ---------------------------------------------------------------- figures and films
FIG = {
    1: ("r01-chart-onsite-box.jpg", "Time spent on-site by visitor type", "plate"),
    2: ("r01-chart-dataset-full.jpg", "Congestion, queue sizes, visit time and delays", "plate"),
    3: ("r01-plan-plain.jpg", "Jackson Home floor plan", "plate"),
    4: ("r01-plan-annex.jpg", "The Annex floor plan, with site entrance, entrance line and vestibule", "plate"),
    5: ("r01-plan-paths.jpg", "Jackson Home floor plan with expected visitor paths", "plate"),
    6: ("r01-chart-arrivals-random.jpg", "Arrivals spread randomly through the ticketing window", "plate"),
    7: ("r01-chart-arrivals-ontime.jpg", "Arrivals at the start of the ticketing window", "plate"),
    8: ("r3-fig-visit-times.jpg", "Expected visit times by visitor type", "plate"),
    9: ("r01-chart-docent.jpg", "Skipped exhibits, without and with docent control", "plate"),
    10: ("r01-chart-best-full.jpg", "Best scenario: 20 tickets, 8 walk-ups, with docent control", "plate"),
    11: ("r02-concept-board.jpg", "Content themes and experience flow for the column", "plate"),
    12: ("r3-fig-whiteboard.jpg", "Lo-fi sketches and wireframes for the column", "plain"),
    13: ("r02-itc-full.jpg", "ITC employee research: three roles", "plate"),
    14: ("r02-sides-full.jpg", "Content distribution across the sides of the column", "plate"),
    19: ("r03-goals-full.jpg", "Rhode Island Department of Health population health goals", "plate"),
    21: ("r03-annotated.jpg", "Vaccine details: annotated mobile screens", "plate"),
    22: ("r3-fig-decision-board.jpg", "Survey: who drives component decisions", "plate"),
    23: ("r04-archetypes-full.jpg", "User archetypes: Engineering & Technical, Sales and Procurement", "plate"),
    24: ("r04-journey-full.jpg", "Product-discovery journey map", "plate"),
}
REPLACED = {15, 16, 17, 18, 20}           # shown as the video / vector drawing her note asks for
MOVED = {5}
FULL = {19, 23, 24}                       # full plates (brief: goals table, archetype board, journey map)                               # rendered in the Baseline Assumptions spread (brief)


class Page:
    def __init__(self, name):
        self.name, self.n = name, 0

    def label(self):
        self.n += 1
        return f"Fig. {self.n:02d}"


def fig(pg, src, cap, kind="plate", cls="b w mt", link=True, ratio=None):
    lab = pg.label()
    CAPTIONS.append((pg.name, lab, cap))
    style = f' style="aspect-ratio:{ratio}"' if ratio else ""
    img = f'<div class="m"{style}><img src="{IMG}{src}" alt="{E(cap)}" loading="lazy"></div>'
    if link:
        img = f'<a href="{IMG}{src}" target="_blank" rel="noopener" aria-label="Open full image: {E(cap)}">{img}</a>'
    return f'<figure class="fig fig--{kind} {cls}">{img}<figcaption data-added="caption">{lab} — {E(cap)}</figcaption></figure>'


def film(pg, src, poster, cap, rt, cls="b full mt", vertical=False):
    lab = pg.label()
    CAPTIONS.append((pg.name, lab, cap + " (video)"))
    return (f'<figure class="film{" film--v" if vertical else ""} {cls}">'
            f'<video src="{VID}{src}" poster="{IMG}{poster}" controls muted playsinline preload="none"></video>'
            f'<figcaption data-added="caption"><span>{lab} — {E(cap)}</span><span>{rt}</span></figcaption></figure>')


def fig_doc(pg, doc, cls="b w mt"):
    src, cap, kind = FIG[doc]
    return fig(pg, src, cap, kind, cls)


# ---------------------------------------------------------------- her production notes -> media
def note_html(pg, it):
    t = it["text"]
    if t.startswith("INSERT VIDEO HERE - DISCRETE EVENT SIMULATION"):
        return film(pg, "r01-simulation.mp4", "poster-r01-simulation.jpg", "Discrete event simulation of visitor flow", "0:48")
    if t.startswith("INSERT VIDEO HERE BELOW IS SCREEN GRAB"):
        return film(pg, "r02-interface.mp4", "poster-r02-interface.jpg", "Final interface and user flow", "0:22")
    if t.startswith("INSERT POWER & ENERGY VIDEO HERE"):
        return film(pg, "r02-cms.mp4", "poster-r02-cms.jpg", "CMS channels in Appspace", "0:11", cls="b w mt")
    if t.startswith("USE PDF VERSION HERE OF DRAWINGS"):
        return "".join(fig(pg, s, cap, "plate", "b full mt") for s, cap in [
            ("r02-shop-1.jpg", "Shop drawing, column surround: plan, section and perspective"),
            ("r02-shop-2.jpg", "Shop drawing: elevations and sections"),
            ("r02-shop-3.jpg", "Shop drawing: typical column surround and plan")])
    if t.startswith("ADD COLUMN FABRICATION VIDEO HERE"):
        return film(pg, "r02-fabrication.mp4", "poster-r02-fabrication.jpg", "Column fabrication progression", "0:14", cls="b w mt")
    if t.startswith("ADD Final Results video here"):
        return film(pg, "r02-final-setup.mp4", "poster-r02-final-setup.jpg", "Final setup: the installed column", "0:21", cls="b mt", vertical=True)
    if t.startswith("INSERT VIDEO OF APP STORE REVIEWS HERE"):
        return film(pg, "r03-app-reviews.mp4", "poster-r03-app-reviews.jpg", "App Store and Google Play reviews", "0:23", cls="b mt", vertical=True)
    if t.startswith("INSERT PDF OR VIDEO OF DESKTOP & MOBILE WIRE FRAMES HERE"):
        wide = film(pg, "r03-wireframes.mp4", "poster-r03-wireframes.jpg", "Desktop wireframes", "0:23", cls="")
        tall = (fig(pg, "r03-screen-record.jpg", "Mobile wireframe: vaccination record", "plain", "", ratio="375/812")
                + fig(pg, "r03-screen-doses.jpg", "Mobile wireframe: dose details", "plain", "", ratio="375/812"))
        return f'<div class="pair b mt"><div class="pair__wide">{wide}</div><div class="pair__tall">{tall}</div></div>'
    if t.startswith("INSERT WIREFRAMES FROM PDF HERE"):
        lab = pg.label()
        CAPTIONS.append((pg.name, lab, "Littelfuse wireframes (placeholder)"))
        return (f'<figure class="fig b w mt"><div class="placeholder"><span class="label" data-added="placeholder">'
                f'Littelfuse wireframes — pending export from Adobe XD</span></div>'
                f'<figcaption data-added="caption">{lab} — Littelfuse wireframes (placeholder)</figcaption></figure>')
    raise KeyError(t)


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


def body(pg, items, room, ordered_lists=False, skip_docs=()):
    """Default flow for a run of items: text in the 12-col measure, media wider."""
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
                out.append(sides_board(pg))
            i = j
            continue
        if typ == "figure":
            j, docs = i, []
            while j < len(items) and items[j]["type"] == "figure":
                d = items[j]["doc"]
                if d not in REPLACED and d not in MOVED and d not in skip_docs:
                    docs.append(d)
                j += 1
            full = [d for d in docs if d in FULL]
            rest = [d for d in docs if d not in FULL]
            if len(rest) == 1:
                out.append(fig_doc(pg, rest[0]))
            elif rest:
                out.append(f'<div class="board b full mt">{"".join(fig_doc(pg, d, "") for d in rest)}</div>')
            for d in full:
                out.append(fig_doc(pg, d, "b full mt"))
            if 23 in docs:
                out.append(film(pg, "r04-personas.mp4", "poster-r04-personas.jpg", "Engineering personas", "0:20", cls="b w mt"))
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


def sides_board(pg):
    sides = [("r02-side-wayfinding.jpg", "Exhibit wayfinding"), ("r02-side-stories.jpg", "Innovation stories"),
             ("r02-side-map.jpg", "Interactive exploration"), ("r02-side-careers.jpg", "Career discovery"),
             ("r02-side-artifacts.jpg", "Artifact interpretation")]
    return ('<div class="board board--5 b full mt">'
            + "".join(fig(pg, s, f"Column side: {c}", "plain", "") for s, c in sides) + "</div>")


# ---------------------------------------------------------------- chapter layouts
def head(no, h2, cls="ch-head"):
    return f'<header class="{cls}"><span class="no" data-added="ui">{no:02d}</span><h2 data-id="{h2["id"]}">{E(h2["text"])}</h2></header>'


def ch_default(pg, no, h2, items, room, **kw):
    return f'<div class="wrap g24">{head(no, h2)}{body(pg, items, room, **kw)}</div>'


def ch_spread(pg, no, h2, items, room, plan_doc):
    plan = fig_doc(pg, plan_doc, "spread__plan")
    return f'<div class="wrap g24 spread">{plan}{head(no, h2)}{body(pg, items, room)}</div>'


def ch_a7_numbered(pg, no, h2, items, room, left_docs):
    """A7: plates left; her sub-headed findings as a numbered 01-0n list right."""
    text = [x for x in items if x["type"] != "figure"]
    left = "".join(fig_doc(pg, d, "") for d in left_docs)
    groups, cur = [], None
    for x in text:
        if x["type"] == "h3":
            cur = [x]; groups.append(cur)
        else:
            cur.append(x)
    lis = "".join("<li>" + "".join(text_html(y, "") for y in g) + "</li>" for g in groups)
    return (f'<div class="wrap g24 a7"><div class="a7__left">{left}</div>{head(no, h2)}'
            f'<ol class="b nl">{lis}</ol></div>')


def ch_a7_media_left(pg, no, h2, items, room):
    """Power & Energy Results: the final-setup film left, her text right."""
    note = next(x for x in items if x["type"] == "note")
    rest = [x for x in items if x is not note]
    return (f'<div class="wrap g24 a7"><div class="a7__left">{note_html(pg, note).replace("b mt", "")}</div>'
            f'{head(no, h2)}{body(pg, rest, room)}</div>')


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
    ("room01", "Findings"): lambda pg, n, h, it, r: ch_a7_numbered(pg, n, h, it, r, [9, 10]),
    ("room01", "Impact"): lambda pg, n, h, it, r: ch_default(pg, n, h, it, r, ordered_lists=True),
    ("room02", "Results & Impact"): ch_a7_media_left,
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
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter+Tight:ital,wght@0,400;0,500;1,400&amp;display=swap">
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
    strip = [("r02-column-installed.jpg", "Power & Energy column"), ("r01-plan-16x9.jpg", "Jackson Home visitor paths"),
             ("r3-cover-r03-3x2.jpg", "401 Health app"), ("r02-shop-1-detail.jpg", "Column shop drawing"),
             ("r02-itc-full.jpg", "ITC employee research")]
    strip_html = "".join(
        f'<figure class="fade"><figcaption class="label" data-added="caption">{E(cap)}</figcaption>'
        f'<div class="m"><img src="{IMG}{src}" alt="{E(cap)}" loading="lazy"></div></figure>' for src, cap in strip)
    for _, cap in strip:
        CAPTIONS.append(("index", "Photo strip", cap))
    skills = [A[f"A-{k:02d}"] for k in (9, 10, 11, 12)]
    panels = ""
    for n, s in enumerate(skills, 1):
        img = (f'<div class="m"><img src="{IMG}r02-column-installed.jpg" alt="The installed Power &amp; Energy column" loading="lazy"></div>'
               if n == 1 else "")
        panels += (f'<article class="panel{" panel--img" if n == 1 else ""}">{img}<span class="no" data-added="ui">{n:02d}</span>'
                   f'<h3 data-id="A-{8 + n:02d}">{E(s["text"])}</h3></article>')
    rows = ""
    for n, r in enumerate(ROOMS, 1):
        rows += (f'<a class="row fade" href="{r["slug"]}.html"><div class="row__t"><span class="label" data-added="ui">{n:02d}</span>'
                 f'<h3 data-ref="{r["title"]["id"]}">{E(r["title"]["text"])}</h3></div>'
                 f'<div class="row__role"><span data-ref="{r["role"]["id"]}">{E(r["role"]["text"])}</span>'
                 f'<span class="label" data-added="ui">Password protected</span></div>'
                 f'<div class="row__img"><div class="m"><img src="{IMG}r3-cover-{r["key"].replace("room0", "r0")}-3x2.jpg" alt="" loading="lazy"></div></div></a>')
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
<!-- A9 photo strip at varying heights, A8 captions above -->
<section class="wrap g24 strip" aria-label="Selected images">{strip_html}</section>

<!-- A9 statement: her second About paragraph -->
<section class="section section--alt" id="about"><div class="wrap statement">
  <p class="big fade" data-id="A-07">{E(A["A-07"]["text"])}</p>
</div></section>

<!-- A10: four equal vertical panels, her four skills in her order -->
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
        cards += (f'<a class="card fade" href="{r["slug"]}.html"><div class="m"><img src="{IMG}r3-cover-{r["key"].replace("room0", "r0")}-3x2.jpg" alt="" loading="lazy"></div>'
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
def case(r):
    pg = Page(r["slug"])
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
    parts = []
    for k, (h, its) in enumerate(chapters, 1):
        if h["text"] == "Reflection":
            inner = ch_reflection(pg, k, h, its, r["key"])
            parts.append(f'<section class="chapter section--alt reflection-sec" id="ch-{k}" style="padding-block:var(--section);margin-top:var(--section)">{inner}</section>')
            continue
        fn = SPECIAL.get((r["key"], h["text"]))
        inner = fn(pg, k, h, its, r["key"]) if fn else ch_default(pg, k, h, its, r["key"])
        parts.append(f'<section class="chapter" id="ch-{k}">{inner}</section>')
    i = ROOMS.index(r)
    prv, nxt = ROOMS[i - 1], ROOMS[(i + 1) % 4]
    b = f"""{bar(over=tone, here="projects")}
<main id="top">
<!-- A1 + A4: full-bleed cover with the title on it, meta panel bottom-right -->
<section class="cover cover--{tone}"><div class="m"><img src="{IMG}r3-cover-{r["key"].replace("room0", "r0")}-16x7.jpg" alt=""></div>
  <h1 class="cover__title" data-id="{r["title"]["id"]}">{E(r["title"]["text"])}</h1></section>
<div class="meta"><div class="wrap g24"><dl class="meta__panel">
  <div class="wide"><dt class="label" data-added="ui">Role</dt><dd data-id="{r["role"]["id"]}">{E(r["role"]["text"])}</dd></div>
  <div class="wide"><dt class="label" data-added="ui">Methods</dt><dd data-id="{r["methods"]["id"]}">{E(r["methods"]["text"])}</dd></div>
  <div><dt class="label" data-added="ui">Setting</dt><dd data-added="supplied">{E(sv["setting"])}</dd></div>
  <div><dt class="label" data-added="ui">Year</dt><dd class="{year_cls}" data-added="supplied">{E(sv["year"])}</dd></div>
</dl></div></div>
<!-- A1: numbered chapter index built from her own headings -->
<nav class="wrap" aria-label="Chapters" data-added="ui"><div class="chindex"><ol>{index}</ol></div></nav>
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


if __name__ == "__main__":
    open("site/index.html", "w").write(home())
    open("site/projects.html", "w").write(projects())
    for r in ROOMS:
        open(f"site/{r['slug']}.html", "w").write(case(r))
    open("site/private-view.html", "w").write(lock())
    json.dump(CAPTIONS, open("content/captions.json", "w"), indent=1, ensure_ascii=False)
    print("pages written;", len(CAPTIONS), "captions")
