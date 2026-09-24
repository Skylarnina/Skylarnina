"""Generate the six prototype pages from one set of templates.

Run from the yasmin/ folder:  python3 tools/build_pages.py
Writes site/index.html, site/room-0N-*.html and site/private-view.html.
The four rooms share ONE template (room_page), which is what Squarespace
needs: one Portfolio item layout, filled four times.
Every section carries an HTML comment naming its pin (see PIN-MAP.md).
"""
import html

SITE = "site"
ROOMS = [
    {"no": "01", "slug": "room-01-jackson-home", "short": "Jackson Home", "name": "The Henry Ford Jackson Home",
     "cover": "r01-cover-4x5.jpg", "wide": "r01-cover-16x9.jpg", "meta": ["UX Research", "The Henry Ford", "2026"]},
    {"no": "02", "slug": "room-02-power-energy", "short": "Power & Energy", "name": "Power & Energy Interactive",
     "cover": "r02-cover-4x5.jpg", "wide": "r02-cover-16x9.jpg", "meta": ["Exhibit + UX Design", "The Henry Ford", "2026"]},
    {"no": "03", "slug": "room-03-rhode-island", "short": "Rhode Island", "name": "Rhode Island 401 Health App",
     "cover": "r03-cover-4x5.jpg", "wide": "r03-cover-16x9.jpg", "meta": ["UX Design + Research", "RI Dept. of Health", "2021"]},
    {"no": "04", "slug": "room-04-littelfuse", "short": "Littelfuse", "name": "Littelfuse Product Discovery",
     "cover": "r04-cover-4x5.jpg", "wide": "r04-cover-16x9.jpg", "meta": ["UX Consulting", "Littelfuse", "Year TBC"]},
]
LAZY = ' loading="lazy"'
CUR = ' class="is-current"'
ACUR = ' aria-current="page"'
LOCK = '<svg viewBox="0 0 10 13" aria-hidden="true"><rect x=".5" y="5.5" width="9" height="7"/><path d="M2.5 5.5V3.5a2.5 2.5 0 0 1 5 0v2"/></svg>'
EMAIL = "email to confirm"


def e(s):
    return html.escape(s, quote=True)


def img(src, alt, cls="m", extra="", lazy=True, pos=None):
    style = f' style="object-position:{pos}"' if pos else ""
    return (f'<div class="{cls}"{extra}><img src="assets/img/{src}" alt="{e(alt)}"'
            f'{LAZY if lazy else ""}{style}></div>')


def page(title, desc, body, bar_dark=True, current=None, cls=""):
    nav_cur = ' aria-current="page"' if current == "home" else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&amp;family=Inter+Tight:wght@400;500&amp;display=swap">
<link rel="stylesheet" href="assets/css/exhibition.css">
<script src="assets/js/exhibition.js" defer></script>
</head>
<body{(' class="' + cls + '"') if cls else ''}>
{body}
<div class="proto" aria-label="Prototype controls"><span>Prototype</span><button type="button" id="wf-toggle" aria-pressed="false">Wireframe</button></div>
</body>
</html>
"""


def bar(dark=True, here=""):
    return f"""<header class="bar{' bar--dark' if dark else ''}">
  <div class="wrap">
    <a class="bar__name" href="index.html">Yasmin Bajwa</a>
    <nav class="bar__nav" aria-label="Main">
      <a href="index.html#rooms"{' aria-current="page"' if here == 'rooms' else ''}>Work</a>
      <a href="index.html#about">About</a>
      <a href="index.html#contact">Contact</a>
      <a class="bar__cta" href="index.html#rooms">View Projects</a>
      <a class="bar__menu" href="index.html#rooms">Menu</a>
    </nav>
  </div>
</header>"""


def foot():
    return """<footer class="foot"><div class="wrap label"><span>Yasmin Bajwa &copy; 2026 &middot; Built with care</span><a href="#top">Back to top &uarr;</a></div></footer>"""


# =====================================================================
# HOMEPAGE
# =====================================================================
def index_page():
    idx = "".join(
        f'<a href="{r["slug"]}.html"{CUR if i == 0 else ""}><span class="vindex__name">{e(r["short"])}</span>{r["no"]}</a>'
        for i, r in enumerate(ROOMS))
    strips = [
        ("01", "Interactive Exhibit Design", "strip-exhibit.jpg", "The installed Power and Energy column in the museum", "room-02-power-energy.html",
         "A five-sided digital column at the entrance to Power &amp; Energy."),
        ("02", "UX Design", "strip-ux-design.jpg", "A row of 401Health app wireframes", "room-03-rhode-island.html",
         "Sign-up, records and scheduling for Rhode Island&rsquo;s 401 Health app."),
        ("03", "UX Research", "strip-ux-research.jpg", "The Jackson Home floor plan with visitor paths", "room-01-jackson-home.html",
         "Simulating how visitors would move through the Jackson Home before it opened."),
        ("04", "Digital Marketing", "strip-marketing.jpg", "ITC employee research storyboard", "room-02-power-energy.html",
         "Career stories for a sponsor, written to inform rather than advertise."),
    ]
    strip_html = "\n".join(f"""    <a class="strip" href="{href}">
      {img(src, alt)}
      <span class="strip__no">{no}</span>
      <span class="strip__word">{word}</span>
      <span class="strip__note">{note}</span>
    </a>""" for no, word, src, alt, href, note in strips)

    slides = []
    for i, r in enumerate(ROOMS):
        meta = "".join(f"<span>{e(m)}</span>" for m in r["meta"])
        slides.append(f"""      <article class="depth__slide" id="slide-{r['no']}"{' data-start' if i == 0 else ''}>
        <a class="depth__frame" href="{r['slug']}.html" aria-label="Enter room {r['no']}: {e(r['name'])}">{img(r['cover'], 'Cover of room ' + r['no'] + ', ' + r['name'])}</a>
        <div class="depth__meta">
          <p class="metaline label"><span class="hl">Room {r['no']}</span>{meta}</p>
          <h3 class="title">{e(r['name'])}</h3>
          <p class="label"><a class="textlink" href="{r['slug']}.html">Enter room &rarr;</a> &nbsp; <span class="lock">{LOCK}Password protected</span></p>
        </div>
      </article>""")
    nav = "".join(f'<a href="#slide-{r["no"]}" data-slide data-group="rooms">{r["no"]}</a>' for r in ROOMS)

    body = f"""<main id="top">
{bar(True)}

<!-- P5 (type behind subject, 01-04 index) + P8 (spaced caps, hairline) : EXHIBITION TITLE -->
<section class="h-hero" aria-labelledby="hero-name">
  {img('portrait-4x5.jpg', 'Yasmin Bajwa in a grey blazer', 'm h-hero__photo', lazy=False)}
  <h1 class="h-hero__word" id="hero-name"><span aria-hidden="true">YASMIN</span><span class="sr-only">Yasmin Bajwa</span></h1>
  <div class="h-hero__cut" aria-hidden="true"><img src="assets/img/portrait-cutout.webp" alt=""></div>
  <div class="h-hero__text">
    <p class="spaced">Digital Exhibit Designer &mdash; The Henry Ford</p>
    <hr class="hairline">
    <p class="serif">Hi, I&rsquo;m <em>Yasmin.</em> I design digital experiences for museums, and the research that shapes them.</p>
    <a class="pill pill--solid" href="#rooms">View Projects <span aria-hidden="true">&rarr;</span></a>
  </div>
  <nav class="h-hero__index vindex" aria-label="The four rooms">{idx}</nav>
  <p class="h-hero__caption label">A portfolio in four rooms &mdash; 2026</p>
</section>

<!-- P4 (stacked full-width photo strips, one word each) : FOUR DISCIPLINES -->
<section class="disciplines" aria-labelledby="disc-title">
  <div class="wrap disciplines__head">
    <h2 class="label" id="disc-title">Four disciplines</h2>
    <p class="label">In the order I practise them</p>
  </div>
  <div class="strips">
{strip_html}
  </div>
</section>

<!-- P3 (dark perspective carousel, framed active card) + P10 (meta line) : THE ROOMS -->
<section class="section section--bb" id="rooms" aria-labelledby="rooms-title">
  <div class="wrap grid" style="row-gap:24px;align-items:end">
    <p class="label" style="grid-column:1/7">Selected work</p>
    <h2 class="title" id="rooms-title" style="grid-column:1/8;color:var(--on-bb)">Four rooms, <em>in order of visit.</em></h2>
    <p style="grid-column:9/13;color:var(--on-bb-muted);font-size:15px">Each room is one project, told from brief to outcome. Swipe or use the numbers. The case studies are shared by invitation.</p>
  </div>
  <div class="depth">
    <div class="depth__track" data-track data-group="rooms">
{chr(10).join(slides)}
    </div>
    <nav class="depth__nav" aria-label="Choose a room">
      <a class="arrow" href="#slide-04" data-slide data-group="x" data-prev="rooms" aria-label="Previous room">&larr;</a>
      {nav}
      <a class="arrow" href="#slide-02" data-slide data-group="x" data-next="rooms" aria-label="Next room">&rarr;</a>
    </nav>
  </div>
</section>

<!-- P9 (overlapping thin circles, photo in one, numbered 01-04 list) : BEYOND THE SCREEN -->
<section class="section section--wall" id="about" aria-labelledby="about-title">
  <div class="wrap grid about">
    <div class="about__circles reveal">
      <div class="circles">
        <div class="circle" style="width:44%;aspect-ratio:1;left:0;top:22%"><span class="spaced">History</span></div>
        <div class="circle circle--photo" style="width:46%;aspect-ratio:1;left:27%;top:6%">
          <div class="placeholder"><span class="label">Personal photo pending<br>(fashion)</span></div>
        </div>
        <div class="circle" style="width:40%;aspect-ratio:1;left:58%;top:30%"><span class="spaced">Art</span></div>
        <span class="spaced" style="position:absolute;left:43%;top:0;color:var(--ink-label)">Fashion</span>
      </div>
    </div>
    <div class="about__text">
      <p class="label" id="about-title">Beyond the screen</p>
      <blockquote>I&rsquo;m a Digital Exhibit Designer at The Henry Ford, with a background in UX design, user research and digital marketing. I bring stories to life through digital experiences, and I&rsquo;m inspired by history, fashion and art.</blockquote>
      <p class="spaced about__loves">History &middot; Fashion &middot; Art</p>
      <ol class="numbered">
        <li><span class="n">01</span><span class="t">Stories brought to life</span></li>
        <li><span class="n">02</span><span class="t">Research-led design</span></li>
        <li><span class="n">03</span><span class="t">Exhibit development</span></li>
        <li><span class="n">04</span><span class="t">A curious, experimental eye</span></li>
      </ol>
      <p><a class="textlink" href="#resume-pending">Download r&eacute;sum&eacute;</a> <span class="pending" style="font-size:13px">&nbsp;(PDF to come)</span></p>
    </div>
  </div>
</section>

<!-- P8 (wide-tracked serif centred over a dark photo, tiny caps, short hairline) : CONTACT -->
<section class="contact" id="contact" aria-labelledby="contact-title">
  {img('r02-column-installed.jpg', '', 'm')}
  <div class="contact__inner">
    <p class="spaced" style="color:var(--on-bb-label)">Contact</p>
    <h2 id="contact-title">Let&rsquo;s make something <em>people remember.</em></h2>
    <hr class="hairline">
    <a class="contact__email" href="mailto:">{EMAIL}</a>
    <p class="contact__links spaced"><a href="#linkedin-pending">LinkedIn</a><span aria-hidden="true">&middot;</span><a href="#resume-pending">R&eacute;sum&eacute;</a><span aria-hidden="true">&middot;</span><span>Instagram (to confirm)</span></p>
  </div>
</section>
</main>
{foot()}"""
    return page("Yasmin Bajwa Exhibition", "Yasmin Bajwa designs digital experiences for museums, and the research that shapes them.", body)


# =====================================================================
# ROOM TEMPLATE (one template, four fillings)
# =====================================================================
class Figs:
    def __init__(self): self.n = 0

    def next(self):
        self.n += 1; return f"Fig. {self.n:02d}"


def plate(F, src, cap, kind="", full=None, alt=None, ratio=None):
    fig = F.next()
    style = f' style="aspect-ratio:{ratio}"' if ratio else ""
    inner = f'<div class="m"{style}><img src="assets/img/{src}" alt="{e(alt or cap)}" loading="lazy"></div>'
    if full:
        inner = f'<a class="zoom" href="assets/img/{full}" data-caption="{e(fig + " — " + cap)}">{inner}</a>'
    return f'<figure class="plate {kind}">{inner}<figcaption><span class="fig">{fig}</span><span>{cap}</span></figcaption></figure>'


def screen(F, video, poster, cap, rt, vertical=False):
    fig = F.next()
    return f"""<figure class="screen{' screen--v' if vertical else ''}">
        <div class="screen__box"><video src="assets/video/{video}" poster="assets/img/{poster}" muted playsinline loop preload="none"></video>
          <button class="screen__play" type="button" aria-label="Play: {e(cap)}"><span></span></button></div>
        <figcaption><span><b class="accent" style="font-weight:500">{fig}</b> &nbsp;{cap}</span><span class="rt">{rt}</span></figcaption>
      </figure>"""


def chapter(no, name, title, body_html, extra=""):
    return f"""<section class="section{extra}">
  <div class="wrap grid chapter">
    <p class="chapter-label label"><span class="no">Chapter {no}</span><span>&mdash; {name}</span></p>
    <h2 class="chapter__title">{title}</h2>
    <div class="chapter__body">{body_html}</div>
  </div>"""


def room_page(r, d):
    i = ROOMS.index(r)
    F = Figs()
    rindex = "".join(
        f'<a href="{x["slug"]}.html"{ACUR if x is r else ""}><span class="vindex__name">{e(x["short"])}</span>{x["no"]}</a>'
        for x in ROOMS)
    title = "".join(f"<span>{t}</span>" for t in d["title"])
    meta = "".join(f"<span>{m}</span>" for m in d["meta"])
    cards = "".join(f"""<div class="minicard">{img(c['img'], '', pos=c.get('pos'))}<p class="label">{c['k']}</p><p class="v{' big' if c.get('big') else ''}">{c['v']}</p></div>"""
                    for c in d["cards"])
    body = [f"""<main id="top">
{bar(True, 'rooms')}
<nav class="rindex vindex" aria-label="Rooms">{rindex}</nav>

<!-- P10 (stacked cinematic headline, one word in the accent, meta line with separators) + P12 (fixed 01-04 index) : ROOM HEADER -->
<header class="rhead" aria-labelledby="room-title" style="--cover-op:{d.get('cover_op', .45)}">
  <div class="rhead__cover"><img src="assets/img/{r['wide']}" alt=""></div>
  <div class="wrap grid rhead__grid">
    <h1 class="rhead__title" id="room-title">{title}</h1>
    <div class="rhead__side">
      <p>{d['lede']}</p>
      <div class="rhead__ctas"><a class="pill pill--solid" href="#film">&#9654;&nbsp; {d['film_cta']}</a><a class="pill pill--ghost" href="#signature">{d['sig_cta']}</a></div>
    </div>
    <p class="rhead__meta metaline label"><span class="hl">Room {r['no']}</span>{meta}</p>
  </div>
</header>

<!-- P6 (row of tall mini-cards with captions) : WALL LABEL -->
<section class="walllabel" aria-label="Wall label" style="--card-shade:{d.get('card_shade', .58)}">
  <div class="wrap"><div class="minicards">{cards}</div></div>
</section>

<!-- Overview : two-column editorial (no pin; round-1 system) -->
<section class="section">
  <div class="wrap grid overview">
    <p class="chapter-label label"><span class="no">Overview</span></p>
    <p class="overview__pull reveal">{d['pull']}</p>
    <div class="overview__body">{''.join('<p>' + p + '</p>' for p in d['overview'])}</div>
  </div>
</section>

<!-- Challenge : numbered plaque list + full-width "How might we" lines (round-1 system) -->
<section class="section section--wall">
  <div class="wrap grid">
    <p class="chapter-label label"><span class="no">The challenge</span></p>
    {('<ol class="constraints">' + ''.join(f'<li><span class="n">{k+1:02d}</span><span>{c}</span></li>' for k, c in enumerate(d['constraints'])) + '</ol>') if d.get('constraints') else ''}
    <div class="hmw">{''.join(d['hmw'])}</div>
  </div>
</section>
"""]
    for block in d["blocks"]:
        body.append(block(F) if callable(block) else block)
    # black box
    films = d["films"](F)
    body.append(f"""
<!-- P12 (dark video section, round play marks) : BLACK-BOX GALLERY -->
<section class="section blackbox" id="film" aria-labelledby="film-title">
  <div class="wrap grid blackbox__grid">
    <div class="blackbox__intro"><p class="label">Black-box gallery</p><h2 id="film-title">{d['film_title']}</h2><p>{d['film_text']}</p></div>
    <div class="blackbox__main">{films[0]}</div>
    {('<div class="blackbox__row">' + ''.join(films[1:]) + '</div>') if len(films) > 1 else ''}
  </div>
</section>
""")
    finds = "".join(f'<div class="finding reveal"><div><h3>{h}</h3><p class="numeral">{n}</p></div><p>{t}</p></div>' for h, n, t in d["findings"])
    ticks = "".join(f"<li>{t}</li>" for t in d["impact"])
    body.append(f"""
<!-- Findings / impact : exhibit numerals + hairline rows (round-1 system) -->
<section class="section">
  <div class="wrap grid">
    <p class="chapter-label label"><span class="no">{d.get('find_label', 'Findings')}</span></p>
    <div class="findings">{finds}</div>
    <div class="grid" style="grid-column:1/13;margin-top:clamp(72px,8vw,120px);row-gap:28px">
      <h2 class="chapter__title" style="grid-column:1/6">{d['impact_title']}</h2>
      <div style="grid-column:7/13;display:grid;gap:20px"><p style="color:var(--ink-muted)">{d['impact_intro']}</p><ul class="ticks">{ticks}</ul></div>
    </div>
  </div>
</section>

<!-- Reflection : centred serif italic, the closing text panel -->
<section class="section section--wall">
  <div class="wrap closing">
    <p class="label">Reflection</p>
    <blockquote>{d['reflection']}</blockquote>
    <hr class="hairline">
  </div>
</section>
""")
    # next room (P11)
    nxt = ROOMS[(i + 1) % 4]
    others = [x for x in ROOMS if x is not r and x is not nxt]
    def card(x, cls):
        return (f'<a class="nextroom__card {cls}" href="{x["slug"]}.html">{img(x["cover"], "Cover of room " + x["no"])}'
                f'<span class="cap"><span class="label">Room {x["no"]}</span><span class="t">{e(x["name"])}</span></span></a>')
    body.append(f"""
<!-- P11 (cards floating over a full-bleed landscape, main card emphasised) : NEXT ROOM -->
<section class="nextroom" aria-labelledby="next-title">
  <div class="nextroom__bg"><img src="assets/img/{nxt['wide']}" alt="" loading="lazy"></div>
  <div class="nextroom__head"><p class="label">Next room &rarr;</p><h2 class="title" id="next-title">Room {nxt['no']}, <em>{e(nxt['short'])}</em></h2></div>
  <div class="nextroom__stage">{card(others[0], 'nextroom__card--l')}{card(others[1], 'nextroom__card--r')}{card(nxt, 'nextroom__card--main')}</div>
  <div class="nextroom__foot label"><a class="textlink" href="index.html#rooms">&larr; Back to all rooms</a><span>Room {r['no']} of 04</span></div>
</section>
</main>
{foot()}""")
    return page(f"{r['name']} Room", d["lede"], "\n".join(body), cls="is-room")


# ---------------------------------------------------------------------
# ROOM 01: The Henry Ford Jackson Home
# ---------------------------------------------------------------------
def r01_route(F):
    stops = [
        ("hot", "Arrival", "Entrance line", "Visitors arrive inside a 15- or 30-minute ticket window. The base plan was 24 tickets per 15 minutes; walk-ups join once ticketed visitors are in.",
         "Up to 16.5 min wait in the busiest scenario tested", "r01-stop-entrance.jpg", "r01-sim-annex-close.jpg"),
        ("hot", "Docent-controlled", "Vestibule", "The first threshold. With docent control, about 8 people are let in at a time.",
         "~8 visitors at a time", "r01-stop-vestibule.jpg", "r01-sim-annex-crowd.jpg"),
        ("hot", "Docent-controlled", "Pre-1965", "Part of the entrance area the docent manages, and one of the first exhibits.",
         "Presenters at the first exhibits reduced skipped exhibits", "r01-sim-exhibit.jpg", "r01-sim-case.jpg"),
        ("hot", "Docent-controlled", "Video wall", "The last stop of the entrance area before visitors move on in sequence.",
         "Still inside the ~8-person docent zone", "r01-sim-case.jpg", "r01-sim-overview.jpg"),
        ("", "In sequence", "The rooms", "Front bedroom, living room, dining room, kitchen, music room. Each room has an occupancy limit; when one is full, visitors wait or move on.",
         "", "r01-stop-front-rooms.jpg", "r01-stop-kitchen.jpg"),
        ("", "Digital interactives", "The Annex", "The complementary building with digital interactives. The model helped decide where the interactives went.",
         "", "r01-plan-annex.jpg", "r01-sim-overview.jpg"),
        ("", "Leaving", "Exit", "Streakers leave after 8&ndash;20 minutes, Strollers after 30&ndash;45, Studiers after 50&ndash;65.",
         "", "r01-stop-exit.jpg", "r01-sim-music-room.jpg"),
    ]
    out = []
    for hot, when, h, p, num, a, b in stops:
        f1 = F.next()
        out.append(f"""<li class="stop{' stop--hot' if hot else ''} reveal">
        <div class="stop__text"><p class="when">{when}</p><h3>{h}</h3><p>{p}</p>{f'<p class="hotnum">{num}</p>' if num else ''}<p class="label">{f1}</p></div>
        <div class="stop__pics">{img(a, h + ' on the plan', 'm p1')}{img(b, h + ' in the simulation', 'm p2')}</div>
      </li>""")
    return f"""
<!-- P6 (itinerary timeline with photos along a line) : SIGNATURE, THE VISITOR'S ROUTE -->
<section class="section" id="signature" aria-labelledby="route-title">
  <div class="wrap grid" style="row-gap:24px;margin-bottom:clamp(56px,6vw,96px);align-items:end">
    <p class="chapter-label label"><span class="no">Signature</span><span>&mdash; The visitor&rsquo;s route</span></p>
    <h2 class="title" id="route-title" style="grid-column:1/8">Seven stops, <em>one path.</em></h2>
    <p style="grid-column:9/13;color:var(--ink-muted)">The route every simulated visitor followed. Stops marked in red are where congestion built up, with the numbers from the model.</p>
  </div>
  <div class="wrap"><ol class="route">{''.join(out)}</ol></div>
</section>

<!-- P9 (overlapping thin circles, sized by share) : VISITOR ARCHETYPES -->
<section class="section section--wall" aria-labelledby="arch-title">
  <div class="wrap grid archetypes">
    <p class="chapter-label label"><span class="no">Chapter 03</span><span>&mdash; Visitor archetypes</span></p>
    <div class="archetypes__circles reveal" role="img" aria-label="Circles sized by share: Strollers 60 percent, Streakers 30 percent, Studiers 10 percent">
      <div class="arch arch--a"><span class="pct">60%</span><span class="nm">Strollers</span></div>
      <div class="arch arch--b"><span class="pct">30%</span><span class="nm">Streakers</span></div>
      <div class="arch arch--c"><span class="pct">10%</span><span class="nm">Studiers</span></div>
    </div>
    <div class="archetypes__list">
      <h2 class="chapter__title" id="arch-title" style="margin-bottom:28px">Three ways <em>to visit.</em></h2>
      <ul class="numbered">
        <li><span class="n">60%</span><span><span class="t">Strollers</span><br><span style="color:var(--ink-muted);font-size:15px">Browse most exhibits with moderate viewing time. 30&ndash;45 min on site.</span></span></li>
        <li><span class="n">30%</span><span><span class="t">Streakers</span><br><span style="color:var(--ink-muted);font-size:15px">Move quickly with minimal stopping. 8&ndash;20 min.</span></span></li>
        <li><span class="n">10%</span><span><span class="t">Studiers</span><br><span style="color:var(--ink-muted);font-size:15px">Read the interpretation thoroughly and stay longest in each room. 50&ndash;65 min.</span></span></li>
      </ul>
      <p style="margin-top:20px;font-size:15px;color:var(--ink-muted)">Each simulated visitor was randomly assigned one of these profiles, based on museum research and checked against The Henry Ford&rsquo;s attendance patterns.</p>
    </div>
  </div>
</section>
"""


def r01_build(F):
    return f"""
<!-- Plates (Image System: plans as plates on the deeper wall, multiply) -->
<section class="section">
  <div class="wrap grid chapter">
    <p class="chapter-label label"><span class="no">Chapter 04</span><span>&mdash; Building the simulation</span></p>
    <h2 class="chapter__title">Every visitor made <em>their own decisions.</em></h2>
    <div class="chapter__body">
      <p>Using the behavioural research, I built a discrete event simulation of individual visitors. Each one navigated the home independently, following the expected paths through the house and reacting to the constraints below.</p>
      <ul class="ticks"><li>Timed ticket arrivals</li><li>Room occupancy limits</li><li>Queue formation</li><li>Walking speed, about 2.0 mph</li><li>Exhibit dwell time by visitor type</li><li>Presenter intervention</li><li>Alternative routing when a space is full</li></ul>
    </div>
    <div style="grid-column:1/8;margin-top:56px">{plate(F, 'r01-plan-paths.jpg', 'The house with expected visitor paths, entering from the Annex', 'plate--drawing', full='r01-plan-paths.jpg')}</div>
    <div style="grid-column:8/13;margin-top:56px;display:grid;gap:40px;align-content:start">
      {plate(F, 'r01-plan-annex.jpg', 'The Annex: site entrance, entrance line and vestibule', 'plate--drawing', full='r01-plan-annex.jpg')}
      {plate(F, 'r01-plan-plain.jpg', 'The house before paths: space syntax view', 'plate--drawing', full='r01-plan-plain.jpg')}
    </div>
  </div>
</section>

<!-- Data wall (Image System: small charts + one numeral pulled out) : SCENARIO TESTING -->
<section class="section section--wall">
  <div class="wrap grid datawall">
    <p class="chapter-label label"><span class="no">Chapter 05</span><span>&mdash; Scenario testing</span></p>
    <div class="datawall__tiles">
      {plate(F, 'r01-chart-arrivals-random.jpg', 'Random arrivals: queues stay low', full='r01-chart-arrivals-random.jpg')}
      {plate(F, 'r01-chart-arrivals-ontime.jpg', 'On-time arrivals: queues spike each window', full='r01-chart-arrivals-ontime.jpg')}
      {plate(F, 'r01-chart-docent.jpg', 'Skipped exhibits, without and with docent control', full='r01-chart-docent.jpg')}
      {plate(F, 'r01-chart-congestion.jpg', 'People in the house across a day', full='r01-chart-dataset-full.jpg')}
    </div>
    <div class="datawall__num reveal">
      <p class="numeral">15<small> min</small></p>
      <p class="numeral-label">ticket windows beat 30-minute ones when most visitors arrive at the start of their slot.</p>
      <p style="font-size:14px;color:var(--ink-muted)">Study factors: ticket window (15 or 30 min), arrival pattern, docent control, number of tickets (low, base, high) and walk-up visitors.</p>
    </div>
  </div>
  <div class="wrap grid datawall" style="margin-top:clamp(72px,8vw,120px)">
    <div class="datawall__num reveal" style="grid-column:1/5">
      <p class="numeral">30</p>
      <p class="numeral-label">visitors per 15-minute window felt comfortable. The house could take about 32.</p>
    </div>
    <div class="datawall__tiles" style="grid-column:5/13">
      {plate(F, 'r01-chart-best-entrance.jpg', 'Best scenario: people waiting at the entrance', full='r01-chart-best-full.jpg')}
      {plate(F, 'r01-chart-best-house.jpg', 'Best scenario: people in the house', full='r01-chart-best-full.jpg')}
      {plate(F, 'r01-chart-queue.jpg', 'Queue sizes at the entrance', full='r01-chart-dataset-full.jpg')}
      {plate(F, 'r01-chart-delays.jpg', 'Wait times by line, in minutes', full='r01-chart-dataset-full.jpg')}
    </div>
  </div>
</section>
"""


def r01_questions(F):
    return """
<!-- Prose chapters (round-1 system: narrow text, hairline rows) -->
<section class="section">
  <div class="wrap grid chapter">
    <p class="chapter-label label"><span class="no">Chapter 01</span><span>&mdash; Research questions</span></p>
    <h2 class="chapter__title">Eight questions <em>before opening day.</em></h2>
    <div class="chapter__body">
      <p><strong>Visitor experience.</strong> How long will visitors spend inside the home? Where will they stop, or get stuck? What will waiting look like?</p>
      <p><strong>Capacity planning.</strong> How many visitors can the Jackson Home and the Annex hold without overcrowding? Should tickets use 15- or 30-minute windows? Can walk-up visitors be added without hurting the experience?</p>
      <p><strong>Operations.</strong> Where should docents and presenters stand? What should staff do at peak times?</p>
    </div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap grid chapter">
    <p class="chapter-label label"><span class="no">Chapter 02</span><span>&mdash; Methodology</span></p>
    <h2 class="chapter__title">No baseline data, <em>so I built one.</em></h2>
    <div class="chapter__body">
      <p><strong>Behavioural observation.</strong> I studied visitor movement in comparable historic homes and exhibits at The Henry Ford: arrivals, walking speed, dwell time, congestion, engagement, and decisions at the thresholds between rooms.</p>
      <p><strong>Space syntax analysis.</strong> With the experience design team, I read the home&rsquo;s layout for visibility, connectivity and circulation, to find likely bottlenecks before testing any scenario.</p>
      <p><strong>Behavioural path clustering.</strong> Visitors engage at different depths, so each simulated visitor was assigned a type, and viewing times were set to match.</p>
    </div>
  </div>
</section>
"""


R01 = {
    "title": ["The Jackson Home", 'Visitor <span class="hot">Flow</span>', "Simulation"],
    "meta": ["UX Researcher &middot; Experience Design", "The Henry Ford", "2026"],
    "lede": "A predictive model of how visitors would move through a historic house, built before anyone walked in.",
    "film_cta": "Watch the simulation", "sig_cta": "The visitor&rsquo;s route",
    "cards": [
        {"k": "Role", "v": "UX Researcher, Experience Design", "img": "r01-sim-overview.jpg"},
        {"k": "Methods", "v": "Observation, space syntax, simulation", "img": "r01-plan-plain.jpg", "pos": "50% 30%"},
        {"k": "Setting", "v": "Greenfield Village, The Henry Ford", "img": "r01-sim-music-room.jpg"},
        {"k": "Year", "v": "2026", "big": True, "img": "r01-stop-front-rooms.jpg"},
        {"k": "Key number", "v": "30<br><span style=\"font-size:15px;font-family:var(--sans)\">visitors per 15-minute window</span>", "big": True, "img": "r01-sim-annex-crowd.jpg"},
    ],
    "pull": "The first building added to Greenfield Village in more than forty years, <em>with no visitor data</em> to plan from.",
    "overview": [
        "The Dr. Sullivan and Mrs. Richie Jean Sherrod Jackson Home is a nationally significant house tied to the 1965 Selma to Montgomery marches. Civil rights leaders, including Dr. Martin Luther King Jr., met there to plan the strategies that led to the Voting Rights Act. Moved to Greenfield Village, it opened as a permanent exhibition in summer 2026.",
        "With no historical visitor data, my role was to build a predictive visitor flow model: a forecast of how guests would move through the constrained historic space before opening day.",
        "Using UX research methods and behavioural modelling, the simulation let stakeholders compare ticketing strategies, estimate capacity, find congestion points, and decide where presenters should stand.",
    ],
    "constraints": ["Narrow circulation paths", "Limited room capacity", "Sequential visitor movement", "Preservation rules: no structural changes"],
    "hmw": ['<p><span class="label">How might we</span>predict visitor behaviour and shape the museum experience before the exhibition opened to the public?</p>'],
    "blocks": [r01_questions, r01_route, r01_build],
    "films": lambda F: [screen(F, "r01-simulation.mp4", "poster-r01-simulation.jpg", "Discrete event simulation of visitors moving through the Annex and the house", "0:48")],
    "film_title": "The model, running",
    "film_text": "Each figure is one simulated visitor, deciding where to go based on space and behavioural rules.",
    "findings": [
        ("Ticketing", "15&#8209;min", "15-minute ticket windows spread arrivals more evenly than 30-minute ones and cut congestion through the home."),
        ("Capacity", "30", "visitors per entry window: noticeably more comfortable than the maximum of about 32, and still efficient."),
        ("Presenters", "3&ndash;4", "presenters in key zones, starting near the first exhibits, to regulate entry and reduce skipped exhibits."),
        ("Walk-ups", "Mixed", "A controlled mix of ticketed and walk-up visitors staggered arrivals and shortened waits."),
    ],
    "impact_title": "Decisions made <em>on evidence.</em>",
    "impact_intro": "The simulation gave stakeholders evidence-based recommendations before the Jackson Home opened. It helped teams:",
    "impact": ["Set ticketing schedules for opening operations", "Set comfortable capacity limits", "Find high-congestion areas before opening",
               "Place presenters throughout the home", "Evaluate queue management strategies", "Decide where to place the digital interactives",
               "Improve flow while protecting the building&rsquo;s historic integrity"],
    "reflection": "This project took my understanding of user experience beyond digital products, into physical space. It also deepened my appreciation for how visitors take in complex, emotionally significant stories, especially those centred on difficult history.",
}


# ---------------------------------------------------------------------
# ROOM 02: Power & Energy
# ---------------------------------------------------------------------
def r02_column(F):
    sides = [
        ("01", "Exhibit wayfinding", "A backlit graphic that names the exhibit and its themes.", "r02-side-wayfinding.jpg"),
        ("02", "Innovation stories", "Condensed episodes of The Henry Ford&rsquo;s Innovation Nation.", "r02-side-stories.jpg"),
        ("03", "Interactive exploration", "A touch map of power transmission across Michigan and the US.", "r02-side-map.jpg"),
        ("04", "Career discovery", "ITC employees on careers in power and energy.", "r02-side-careers.jpg"),
        ("05", "Artifact interpretation", "Key artifacts in the exhibit, with more context.", "r02-side-artifacts.jpg"),
    ]
    wins = "".join(f"""<figure class="archwin reveal">{img(src, 'Side ' + n + ' artwork: ' + t)}<figcaption style="display:grid;gap:8px;justify-items:center"><span class="n">{n}</span><span class="t">{t}</span><p>{p}</p></figcaption></figure>"""
                   for n, t, p, src in sides)
    return f"""
<!-- P2 (tall pill/arch windows over one full-bleed background) : SIGNATURE, THE COLUMN -->
<section class="column" id="signature" aria-labelledby="col-title">
  <div class="column__bg"><img src="assets/img/r02-column-installed-b.jpg" alt="" loading="lazy"></div>
  <div class="wrap grid column__head">
    <p class="chapter-label label" style="color:var(--on-bb-label)"><span class="no accent">Signature</span><span>&mdash; The column</span></p>
    <h2 class="title" id="col-title">Five sides, <em>one story.</em></h2>
    <p>Each side of the column has its own job, and together they make one visitor journey: passive storytelling on some faces, touch-based exploration on others.</p>
  </div>
  <div class="wrap"><div class="arches">{wins}</div></div>
</section>
"""


def r02_process(F):
    return f"""
<section class="section">
  <div class="wrap grid chapter">
    <p class="chapter-label label"><span class="no">Chapter 01</span><span>&mdash; The approach</span></p>
    <h2 class="chapter__title">From the Agriculture column <em>to a new one.</em></h2>
    <div class="chapter__body">
      <p>I started from the existing interactive column in the Agriculture exhibit and talked through how the Power &amp; Energy version would look and feel. Then I sketched and built lo-fi wireframes to share with stakeholders.</p>
      <p>The column also carries content from project partner ITC (International Transmission Company), and was built in Appspace, the museum&rsquo;s content system, so internal teams can keep it up to date.</p>
    </div>
  </div>
  <div class="wrap pinned" style="margin-top:56px">
    <figure>{img('r02-sketch-a.jpg', 'Whiteboard sketch of the column sides')}<figcaption class="label">{F.next()} &mdash; Early sketches</figcaption></figure>
    <figure>{img('r02-sketch-b.jpg', 'Whiteboard sketch of the interface flow')}<figcaption class="label">{F.next()} &mdash; Early sketches</figcaption></figure>
  </div>
  <div class="wrap grid" style="margin-top:clamp(72px,8vw,120px);row-gap:40px;align-items:center">
    <div style="grid-column:1/8">{plate(F, 'r02-sides-detail.jpg', 'Content distribution across the sides of the column (detail)', 'plate--doc', full='r02-sides-full.jpg')}</div>
    <div class="datawall__num reveal" style="grid-column:9/13">
      <p class="numeral">5 <small>sides</small></p>
      <p class="numeral-label">1 story: the interconnectedness and trade-offs of energy production, distribution and use.</p>
    </div>
    <div style="grid-column:2/12;margin-top:40px">{plate(F, 'r02-concept-board.jpg', 'Content themes and experience flow for the column', 'plate--doc', full='r02-concept-board.jpg')}</div>
  </div>
</section>

<section class="section section--wall">
  <div class="wrap grid chapter">
    <p class="chapter-label label"><span class="no">Chapter 02</span><span>&mdash; Discovery &amp; stakeholder alignment</span></p>
    <h2 class="chapter__title"><span class="numeral" style="font-size:1.8em;display:block">3</span> employee <em>voices.</em></h2>
    <div class="chapter__body">
      <p>With ITC, I found three employee volunteers from Safety &amp; Security, Engineering and Community Planning, and interviewed each about their role, career path and connection to the energy industry. Their answers became the career content.</p>
      <p>Using The Henry Ford&rsquo;s Model i framework, I wrote short prompts that send younger visitors back into the museum:</p>
      <p style="font:italic 400 22px/1.35 var(--serif);color:var(--ink)">&ldquo;Engineering Together: Thomas Edison employed dozens of engineers, inventors, and chemists at the Menlo Park Laboratory&hellip; Experience Menlo Park Laboratory for yourself in Greenfield Village.&rdquo;</p>
    </div>
  </div>
  <div class="wrap" style="margin-top:56px">
    <div class="voices">
      <figure>{img('r02-side-careers.jpg', 'Career screen: Community Planning', pos='50% 12%')}<figcaption class="label" style="margin-top:10px">{F.next()} &mdash; Community planning</figcaption></figure>
      <figure>{img('r02-side-careers-b.jpg', 'Career screen: Engineering', pos='50% 12%')}<figcaption class="label" style="margin-top:10px">{F.next()} &mdash; Engineering</figcaption></figure>
      <figure>{img('r02-side-careers-c.jpg', 'Career screen: Safety and Security', pos='50% 12%')}<figcaption class="label" style="margin-top:10px">{F.next()} &mdash; Safety &amp; security</figcaption></figure>
    </div>
    <div style="margin-top:56px">{plate(F, 'r02-itc-detail.jpg', 'Employee research: three roles, shared behaviours (detail)', 'plate--doc', full='r02-itc-full.jpg')}</div>
  </div>
</section>

<section class="section">
  <div class="wrap grid chapter">
    <p class="chapter-label label"><span class="no">Chapter 03</span><span>&mdash; Designing the experience &amp; CMS</span></p>
    <h2 class="chapter__title">Built on how visitors <em>actually</em> used the last one.</h2>
    <div class="chapter__body">
      <p>I reviewed the Agriculture column&rsquo;s flow, touchpoints and rules, and findings from earlier guest observations. Those behaviours decided which content suited each side, and how the interaction flow was structured.</p>
      <p>The institution asked for the content to live in Appspace. I led the conversations with the Appspace partner manager on touchpoints, flow and information architecture, then built the content channels, programmed the interface, and kept it updated.</p>
    </div>
  </div>
</section>

<section class="section section--wall">
  <div class="wrap grid chapter">
    <p class="chapter-label label"><span class="no">Chapter 04</span><span>&mdash; Installation &amp; fabrication</span></p>
    <h2 class="chapter__title">Matching <em>the existing columns.</em></h2>
    <div class="chapter__body">
      <p>We worked with Sleet Custom Cabinets, who built the Agriculture columns. I gave them dimensions, specifications and print requirements for the backlit graphics, and coordinated the teams so the build, digital components and graphics came together on schedule.</p>
    </div>
    <div style="grid-column:1/9;margin-top:56px">{plate(F, 'r02-shop-1.jpg', 'Column surround: plan, section and perspective. Fabricator&rsquo;s shop drawing, used as the build spec', 'plate--drawing', full='r02-shop-1.jpg')}</div>
    <div style="grid-column:9/13;margin-top:56px">{plate(F, 'r02-shop-1-detail.jpg', 'Detail: column plan view', 'plate--drawing', full='r02-shop-1-detail.jpg')}</div>
    <div style="grid-column:1/7;margin-top:40px">{plate(F, 'r02-shop-2.jpg', 'Elevations and sections', 'plate--drawing', full='r02-shop-2.jpg')}</div>
    <div style="grid-column:7/13;margin-top:40px">{plate(F, 'r02-shop-3.jpg', 'Typical column surround and plan', 'plate--drawing', full='r02-shop-3.jpg')}</div>
  </div>
</section>
"""


R02 = {
    "title": ["Power &amp; Energy", "Interactive", '<span class="hot">Column</span>'],
    "meta": ["UX Designer &middot; Experience Design &middot; Project Management", "The Henry Ford", "2026"],
    "lede": "A multi-sided digital column that marks the entrance to the Power & Energy exhibit and tells its story.",
    "film_cta": "Watch the installation", "sig_cta": "The five sides",
    "cards": [
        {"k": "Role", "v": "UX Designer, project lead", "img": "r02-fab-install.jpg"},
        {"k": "Methods", "v": "IA, user flows, wireframes, content strategy", "img": "r02-sides-detail.jpg"},
        {"k": "Setting", "v": "Henry Ford Museum, Power &amp; Energy", "img": "r02-column-installed-b.jpg", "pos": "50% 30%"},
        {"k": "Year", "v": "2026", "big": True, "img": "r02-fab-before.jpg"},
        {"k": "Key number", "v": "5<br><span style=\"font-size:15px;font-family:var(--sans)\">sides, one story</span>", "big": True, "img": "r02-side-wayfinding.jpg", "pos": "50% 70%"},
    ],
    "pull": "A column that works as the exhibit&rsquo;s <em>front door</em> and its storyteller, in a hall full of large artifacts.",
    "overview": [
        "The goal was to strengthen The Henry Ford Museum&rsquo;s Power &amp; Energy exhibit with a multi-sided interactive digital column, inspired by an existing column in a nearby exhibit.",
        "Designed for student groups, families and general visitors, it combines video, interactive content, wayfinding and artifact highlights to explain the exhibit&rsquo;s central themes: the interconnectedness and trade-offs of energy production, distribution and use.",
    ],
    "hmw": ['<p><span class="label">Capturing visitor attention &mdash; how might we</span>create an intuitive digital experience that encourages visitors of all ages to pause, explore and learn?</p>',
            '<p><span class="label">Balancing museum and sponsor goals &mdash; how might we</span>introduce students to careers in power and energy, while balancing visitor, museum and sponsor needs?</p>'],
    "blocks": [r02_column, r02_process],
    "films": lambda F: [screen(F, "r02-final-setup.mp4", "poster-r02-final-setup.jpg", "The column installed, cycling through its sides", "0:21", True),
                        screen(F, "r02-fabrication.mp4", "poster-r02-fabrication.jpg", "Fabrication and installation", "0:14"),
                        screen(F, "r02-interface.mp4", "poster-r02-interface.jpg", "Final interface and user flow", "0:22"),
                        screen(F, "r02-cms.mp4", "poster-r02-cms.jpg", "Content channels in Appspace", "0:11")],
    "film_title": "The column, installed",
    "film_text": "From the original gallery column to the lit, finished piece, plus the interface and the content system behind it.",
    "find_label": "Results",
    "findings": [
        ("Journey", "5", "sides, each with a distinct purpose, adding up to one visitor journey at the exhibit entrance."),
        ("Voices", "3", "ITC employees whose stories introduce students to careers in power and energy."),
        ("Platform", "1", "content system (Appspace), so museum staff can manage and update the experience over time."),
        ("Next", "3", "planned evaluations: volunteer focus groups, Henry Ford Academy student testing, and in-gallery observation."),
    ],
    "impact_title": "A clearer <em>entrance.</em>",
    "impact_intro": "The column turned the exhibit entrance into a more intentional visitor touchpoint. Long-term impact hasn&rsquo;t been measured yet.",
    "impact": ["A clear visual anchor at the exhibit entrance", "Artifact discovery, career exploration, wayfinding and interactive learning in one place",
               "Integration into the museum&rsquo;s CMS ecosystem", "For ITC: a way to connect the story to the people behind the industry"],
    "reflection": "Designing for a physical museum meant thinking about spatial interaction, accessibility, visitor behaviour and the space around the screen, not only the interface. Most of all, it reinforced that UX does not stop at the screen.",
}


# ---------------------------------------------------------------------
# ROOM 03: Rhode Island
# ---------------------------------------------------------------------
def r03_app(F):
    feats = [
        ("language", "Multilingual", "Terms in several languages, including Portuguese.", "r03-screen-language.jpg", False),
        ("status", "Vaccination status", "A clear card with each COVID-19 dose.", "r03-screen-record.jpg", False),
        ("schedule", "Scheduling", "Find and book an appointment.", "r03-desk-schedule.jpg", True),
        ("household", "Household", "Manage up to 10 household members from one account.", "r03-screen-household.jpg", False),
        ("diary", "Symptom diary", "Optional, anonymous post-vaccination reporting.", "r03-screen-symptoms.jpg", False),
        ("map", "Testing map", "Find nearby COVID-19 testing.", "r03-desk-map.jpg", True),
    ]
    pills = "".join(f'<a href="#feat-{k}" data-slide data-group="feat">{t}</a>' for k, t, *_ in feats)
    cards = []
    for n, (k, t, p, src, wide) in enumerate(feats):
        fig = F.next()
        cards.append(f"""<figure class="swap__card{' swap__card--wide' if wide else ''}" id="feat-{k}"{' data-start' if k == 'status' else ''}>
          <div class="swap__frame">{img(src, t + ' wireframe')}</div>
          <figcaption><span class="label accent">{fig}</span><span class="t">{t}</span><p>{p}</p></figcaption></figure>""")
    return f"""
<!-- P1 (cards floating over a softened full-bleed scene) + P7 (pill switcher, centre card with neighbours peeking) : SIGNATURE, THE APP -->
<section class="appstage" id="signature" aria-labelledby="app-title">
  <div class="appstage__bg"><img src="assets/img/r03-desk-portal.jpg" alt="" loading="lazy"></div>
  <div class="wrap appstage__head">
    <p class="label"><span class="accent">Signature</span> &mdash; The app</p>
    <h2 class="title" id="app-title">Six features, <em>one record.</em></h2>
    <nav class="pills" aria-label="Features">{pills}</nav>
  </div>
  <div class="swap" data-track data-group="feat">{''.join(cards)}</div>
  <div class="wrap grid" style="margin-top:clamp(56px,6vw,96px);row-gap:32px;align-items:end">
    <div style="grid-column:1/6" class="reveal"><p class="numeral">+23%</p><p class="numeral-label">target increase in completed vaccination reports. This was the project&rsquo;s goal, not a measured result.</p></div>
    <div style="grid-column:7/10" class="reveal"><p class="numeral" style="font-size:clamp(64px,6vw,96px)">3</p><p class="numeral-label">languages in onboarding, including Portuguese.</p></div>
    <div style="grid-column:10/13" class="reveal"><p class="numeral" style="font-size:clamp(64px,6vw,96px)">10</p><p class="numeral-label">household members on one account.</p></div>
  </div>
</section>
"""


def r03_discovery(F):
    return f"""
<section class="section">
  <div class="wrap grid chapter">
    <p class="chapter-label label"><span class="no">Chapter 01</span><span>&mdash; Discovery &amp; stakeholder alignment</span></p>
    <h2 class="chapter__title">Listening to the state, <em>and to the reviews.</em></h2>
    <div class="chapter__body">
      <p>State employees shared user feedback and analytics. I interviewed staff across the program in small groups of no more than two, and mapped the design to the Department of Health&rsquo;s wider goals (goals 20&ndash;23 below).</p>
      <p>Two themes kept coming up: frustration at re-entering vaccination information, and doubt about trusting the system with health data. I also analysed Google Play and App Store reviews for recurring pain points: account setup, blocked tasks, and uncertainty about how records were handled.</p>
    </div>
  </div>
  <div class="wrap grid" style="margin-top:56px;row-gap:32px">
    <div style="grid-column:1/13">{plate(F, 'r03-goals-detail.jpg', 'Detail: goals 20&ndash;23, analyse and communicate data to improve public health', 'plate--doc', full='r03-goals-full.jpg')}</div>
    <p class="label" style="grid-column:1/13">The full table of 23 population health goals opens as a plate.</p>
  </div>
</section>
"""


def r03_design(F):
    return f"""
<section class="section section--wall">
  <div class="wrap grid chapter">
    <p class="chapter-label label"><span class="no">Chapter 02</span><span>&mdash; UX design &amp; feature prioritisation</span></p>
    <h2 class="chapter__title">Records that <em>arrive already filled in.</em></h2>
    <div class="chapter__body">
      <p>The solution was a streamlined authorisation flow that pulled records from RICAIR, the state immunisation registry that providers and pharmacies already report to. Once signed in, residents could review their history, add anything missing, and manage their household in one account.</p>
      <p>Priorities were usability, accessibility and access to essential public health services.</p>
    </div>
    <div style="grid-column:1/13;margin-top:56px">{plate(F, 'r03-annotated.jpg', 'Vaccine details: imported data, feature add-on, dose details and the SMART Health Card', 'plate--doc', full='r03-annotated.jpg')}</div>
  </div>
</section>
"""


R03 = {
    "cover_op": .3, "card_shade": .7,
    "title": ["Rhode Island", '401 <span class="hot">Health</span>', "App"],
    "meta": ["UX Designer &middot; UX Researcher &middot; UX Consultant", "Rhode Island Dept. of Health", "2021"],
    "lede": "Making it easier for Rhode Island residents to report, find and show their vaccination records.",
    "film_cta": "Watch the wireframes", "sig_cta": "The six features",
    "cards": [
        {"k": "Role", "v": "UX Designer, Researcher, Consultant", "img": "r03-screen-record.jpg", "pos": "50% 70%"},
        {"k": "Methods", "v": "Review analysis, heuristic review, wireframes", "img": "r03-desk-portal.jpg"},
        {"k": "Setting", "v": "Public health, COVID-19", "img": "r03-screen-language.jpg"},
        {"k": "Year", "v": "2021", "big": True, "img": "r03-screen-doses.jpg"},
        {"k": "Target", "v": "+23%<br><span style=\"font-size:15px;font-family:var(--sans)\">completed reports (goal)</span>", "big": True, "img": "r03-screen-home.jpg"},
    ],
    "pull": "A digital vaccination record residents could <em>trust</em>, and show at the door.",
    "overview": [
        "The goal was to improve Rhode Island&rsquo;s vaccine website and health app, so residents could report vaccination information and reach their records more easily, while giving the state reliable, timely data during the COVID-19 pandemic.",
        "It also made proof of vaccination easier to present at large events and venues. The experience aimed to raise completed vaccination reports by 23%.",
    ],
    "hmw": ['<p><span class="label">Building trust &mdash; how might we</span>create a sign-up and onboarding experience that encourages residents to complete their vaccination record?</p>',
            '<p>build trust by clearly explaining privacy, security, and how personal information is used?</p>',
            '<p>show the value of a digital record for events, travel and other verification?</p>',
            '<p><span class="label">Reducing friction &mdash; how might we</span>make it simple to securely authorise access to existing vaccination records?</p>',
            '<p>make clear where vaccination data comes from and how it is used?</p>'],
    "blocks": [r03_discovery, r03_app, r03_design],
    "films": lambda F: [screen(F, "r03-wireframes.mp4", "poster-r03-wireframes.jpg", "Desktop wireframes: the test-scheduling portal", "0:23"),
                        screen(F, "r03-app-reviews.mp4", "poster-r03-app-reviews.jpg", "App Store reviews that shaped the pain points", "0:23", True)],
    "film_title": "The flows, in motion",
    "film_text": "The desktop portal wireframes, and the App Store reviews behind the redesign.",
    "find_label": "Results",
    "findings": [
        ("Target", "+23%", "increase in completed vaccination reports: the aim of the redesign, not a measured outcome."),
        ("Access", "3", "languages at the start of onboarding, including Portuguese, for Rhode Island&rsquo;s communities."),
        ("Household", "10", "family members can be managed from a single account."),
        ("Features", "6", "prioritised features, from vaccination status to a testing-location map."),
    ],
    "impact_title": "A digital alternative <em>to the paper card.</em>",
    "impact_intro": "Long-term adoption metrics were outside the scope of my involvement. The design recommendations focused on:",
    "impact": ["Replacing paper vaccination cards with a digital record", "Reducing friction in sign-up and record access",
               "Explaining clearly how personal data is accessed and used", "A multilingual experience for more residents",
               "Flexibility for future vaccination programs"],
    "reflection": "Working with sensitive health information taught me to remove unnecessary friction while being clear about how personal data is used. Doing it during the pandemic showed me the role UX can play in helping communities reach essential services in uncertain times.",
}


# ---------------------------------------------------------------------
# ROOM 04: Littelfuse
# ---------------------------------------------------------------------
def r04_types(F):
    types = [("sales", "Sales", "12%", "of respondents. Sales partners support customers with technical and other requirements.", False),
             ("engineering", "Engineering &amp; Technical", "66%", "of survey respondents. Engineers evaluate specifications and recommend components, so the experience was built around their tasks.", True),
             ("procurement", "Procurement", "5%", "of respondents. Buyers and product managers keep components supplied through to manufacturing.", False)]
    pills = "".join(f'<a href="#type-{k}" data-slide data-group="types">{t}</a>' for k, t, *_ in types)
    cards = []
    for k, t, pct, p, start in types:
        fig = F.next()
        cards.append(f"""<figure class="swap__card" id="type-{k}"{' data-start' if start else ''}>
          <div class="swap__frame">{img('r04-archetype-' + k + '.jpg', t + ' archetype board')}</div>
          <figcaption><span class="label accent">{fig}</span><span class="typestat">{pct}</span><span class="t">{t}</span><p>{p}</p></figcaption></figure>""")
    return f"""
<!-- P7 (pill switcher, large centre card with side cards peeking) : SIGNATURE, THREE KINDS OF USER -->
<section class="types" id="signature" aria-labelledby="types-title">
  <div class="wrap appstage__head">
    <p class="label" style="color:var(--on-bb-label)"><span class="accent">Signature</span> &mdash; Three kinds of user</p>
    <h2 class="title" id="types-title" style="color:var(--on-bb)">Who drives <em>component decisions?</em></h2>
    <nav class="pills" aria-label="Archetypes">{pills}</nav>
  </div>
  <div class="swap" data-track data-group="types">{''.join(cards)}</div>
</section>
"""


def r04_approach(F):
    wires = ["Home + mega menu", "Product flow L0&ndash;L7", "Check stock", "Request a sample", "Where to buy", "Mobile"]
    tiles = "".join(f'<figure class="plate"><div class="placeholder" style="aspect-ratio:16/10"><span class="label">Wireframe pending<br>{w}</span></div><figcaption><span class="fig">{F.next()}</span><span>{w}</span></figcaption></figure>' for w in wires)
    return f"""
<section class="section">
  <div class="wrap grid chapter">
    <p class="chapter-label label"><span class="no">Chapter 01</span><span>&mdash; The approach</span></p>
    <h2 class="chapter__title">From business units <em>to the customer.</em></h2>
    <div class="chapter__body">
      <p>I reviewed existing research, business goals and the end-to-end discovery experience, turned them into primary user needs, mapped the engineer&rsquo;s pre-login journey, and audited the interface against the tasks users needed to finish.</p>
      <p>Research showed customers came to find and compare products, reach technical documents, check availability, request samples and get support. Stakeholder interviews, research and survey data grouped users into three archetypes, and the survey pointed to the design engineer as the primary user.</p>
    </div>
  </div>
  <div class="wrap grid datawall" style="margin-top:clamp(72px,8vw,120px)">
    <div class="datawall__num reveal" style="grid-column:1/5"><p class="numeral">73.2%</p><p class="numeral-label">of users searched by an exact stock number. Everyone else had to dig.</p></div>
    <div class="reveal" style="grid-column:5/9"><p class="numeral" style="font-size:clamp(64px,6vw,96px)">48%</p><p class="numeral-label">said finding products was easy, but took too long. Another 12% found search difficult.</p></div>
    <div class="reveal" style="grid-column:9/13"><p class="numeral" style="font-size:clamp(64px,6vw,96px)">66%</p><p class="numeral-label">of survey respondents were engineers.</p></div>
  </div>
</section>

<!-- Dense document (Image System: wide plate + detail crops) : JOURNEY MAP -->
<section class="section section--wall">
  <div class="wrap grid">
    <p class="chapter-label label"><span class="no">Chapter 02</span><span>&mdash; Mapping the product-discovery journey</span></p>
    <div style="grid-column:1/13">{plate(F, 'r04-journey-full.jpg', 'The engineer&rsquo;s journey, from pre-login discovery to post-login engagement, mapped in a workshop at the client&rsquo;s headquarters', 'plate--doc', full='r04-journey-full.jpg')}</div>
    <div style="grid-column:1/5;margin-top:32px">{plate(F, 'r04-journey-find.jpg', 'Find: home and search', 'plate--doc', full='r04-journey-full.jpg')}</div>
    <div style="grid-column:5/9;margin-top:32px">{plate(F, 'r04-journey-learn.jpg', 'Learn: learn and compare', 'plate--doc', full='r04-journey-full.jpg')}</div>
    <div style="grid-column:9/13;margin-top:32px">{plate(F, 'r04-journey-get.jpg', 'Get: buy, share and save', 'plate--doc', full='r04-journey-full.jpg')}</div>
  </div>
</section>

<section class="section">
  <div class="wrap grid chapter">
    <p class="chapter-label label"><span class="no">Chapter 03</span><span>&mdash; Audit &amp; design principles</span></p>
    <h2 class="chapter__title">Three kinds of <em>gap.</em></h2>
    <div class="chapter__body">
      <ol class="numbered">
        <li><span class="n">01</span><span><span class="t">Navigation &amp; findability</span><br><span style="font-size:15px;color:var(--ink-muted)">Cross Reference, Check Stock, Where to Buy and Request Samples were inconsistently represented. Labels, search and language selection were unclear.</span></span></li>
        <li><span class="n">02</span><span><span class="t">Incomplete task flows</span><br><span style="font-size:15px;color:var(--ink-muted)">Check Stock had missing screens and unclear paths for users without a part number.</span></span></li>
        <li><span class="n">03</span><span><span class="t">Interaction &amp; content gaps</span><br><span style="font-size:15px;color:var(--ink-muted)">Inconsistent labels, unclear states, missing templates and undefined controls.</span></span></li>
      </ol>
      <p>The findings became design principles: clarity, consistency, accessibility and task completion, applied across the header, mega menu, homepage, product pages and supporting modules, with new flows for search, discovery, Check Stock, Where to Buy and privacy/GDPR.</p>
    </div>
  </div>
  <div class="wrap grid datawall" style="margin-top:clamp(72px,8vw,120px)">
    <div class="datawall__tiles datawall__tiles--3" style="grid-column:1/13">{tiles}</div>
    <p class="label" style="grid-column:1/13">The final wireframes are in Adobe XD links only. Exported screens will replace these plates.</p>
  </div>
</section>
"""


R04 = {
    "cover_op": .18, "card_shade": .74,
    "title": ["Littelfuse", "Product", '<span class="hot">Discovery</span>'],
    "meta": ["UX Consultant &middot; UX Designer &middot; UX Researcher", "Littelfuse", "Year TBC"],
    "lede": "Reimagining how engineers discover products across a vast technical catalogue.",
    "film_cta": "Watch the personas", "sig_cta": "Three kinds of user",
    "cards": [
        {"k": "Role", "v": "UX Consultant, Designer, Researcher", "img": "r04-archetype-engineering.jpg", "pos": "50% 60%"},
        {"k": "Methods", "v": "Workshop, data analysis, IA, heuristic evaluation", "img": "r04-journey-learn.jpg"},
        {"k": "Setting", "v": "B2B manufacturing", "img": "r04-journey-get.jpg"},
        {"k": "Year", "v": "TBC", "big": True, "img": "r04-archetype-sales.jpg", "pos": "50% 50%"},
        {"k": "Key number", "v": "73.2%<br><span style=\"font-size:15px;font-family:var(--sans)\">searched by exact stock number</span>", "big": True, "img": "r04-journey-find.jpg"},
    ],
    "pull": "Engineers who didn&rsquo;t know the <em>exact part number</em> were left to guess.",
    "overview": [
        "Littelfuse is a global manufacturer of electronic components for automotive, industrial, electronics and other industries.",
        "I worked with Littelfuse to improve its digital portal, making it more intuitive for engineers to discover, evaluate and access products across a huge portfolio, and moving it from a structure organised by business unit to one organised around the customer. For the business, it opened up cross-selling and upselling across categories.",
    ],
    "hmw": ['<p><span class="label">How might we</span>help engineers discover the right product without knowing an exact stock number?</p>',
            '<p>connect engineers with relevant and complementary products across the wider portfolio?</p>',
            '<p>streamline key tasks, from comparing products and technical documents to ordering, samples and support?</p>'],
    "blocks": [r04_types, r04_approach],
    "films": lambda F: [screen(F, "r04-personas.mp4", "poster-r04-personas.jpg", "From research to personas: OEM Engineer, CM Engineer, Technical Advisor", "0:20")],
    "film_title": "The personas",
    "film_text": "Survey data, customer interviews and stakeholder research, synthesised into detailed engineering personas.",
    "find_label": "Results",
    "findings": [
        ("Search", "73.2%", "of users searched by exact stock number; broader searches often failed to surface results."),
        ("Time", "48%", "found search easy but too slow; 12% found it difficult."),
        ("Users", "66%", "of respondents were engineers, so the experience centred on their core tasks."),
        ("After launch", "+6%", "mobile logins, pointing to stronger engagement with the improved mobile experience."),
    ],
    "impact_title": "Clearer paths <em>to the right part.</em>",
    "impact_intro": "The redesign streamlined discovery and evaluation across desktop and mobile:",
    "impact": ["Clearer pathways through search and navigation", "Complete Check Stock, Where to Buy and sample flows",
               "Defined states, errors, filters and responsive behaviour, ready for development", "Mobile logins up 6% after launch"],
    "reflection": "A highly specialised industry meant extra secondary research, and that surfaced questions we hadn&rsquo;t considered and led to more discovery sessions. Good UX sometimes means slowing down to understand a complex ecosystem before designing for it.",
}


# =====================================================================
# PRIVATE VIEW (P8 + P1)
# =====================================================================
def private_page():
    body = f"""<main id="top">
<!-- P8 (wide-tracked serif, spaced caps, short hairline) + P1 (a panel floating over a soft full-bleed scene) : PRIVATE VIEW -->
<section class="pv" aria-labelledby="pv-title">
  <div class="pv__bg"><img src="assets/img/r01-plan-16x9.jpg" alt=""></div>
  <div class="pv__corner label"><a href="index.html">Yasmin Bajwa</a><a href="index.html#rooms">&larr; All rooms</a></div>
  <div class="pv__card">
    <p class="spaced">Private view</p>
    <h1 class="pv__title" id="pv-title">Room 01 &mdash; The Jackson Home</h1>
    <hr class="hairline">
    <p>Case studies are shared by invitation. Enter the password to continue.</p>
    <form action="#" novalidate>
      <label for="pw" class="label">Password</label>
      <input type="password" id="pw" name="pw" autocomplete="current-password" aria-describedby="pw-error">
      <p class="error" id="pw-error" role="alert">That password didn&rsquo;t work. Try again.</p>
      <button class="pill pill--solid" type="submit">Enter</button>
    </form>
    <p class="pv__ask">No password? <a href="mailto:?subject=Portfolio%20access"><em>Ask Yasmin for access</em> &rarr;</a></p>
  </div>
</section>
</main>"""
    return page("Private View", "Case studies are shared by invitation.", body)


if __name__ == "__main__":
    open(f"{SITE}/index.html", "w").write(index_page())
    for r, d in zip(ROOMS, [R01, R02, R03, R04]):
        open(f"{SITE}/{r['slug']}.html", "w").write(room_page(r, d))
    open(f"{SITE}/private-view.html", "w").write(private_page())
    print("wrote 6 pages")
