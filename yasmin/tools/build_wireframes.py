"""Round 5: greyscale HTML wireframes of the seven pages, for client layout approval.

Run from yasmin/ after tools/build_r3.py:  python3 tools/build_wireframes.py
Each page is the built design page with:
  - every image and video swapped for a grey box of the same proportions, labelled
    "IMAGE — FIG. n" / "VIDEO — FIG. n · running time" (or what it is, e.g. "IMAGE — PORTRAIT");
  - her real copy, the hairlines and the grid unchanged;
  - no photos and no colour (the warm #F4F3F0 ground becomes neutral grey);
  - everything inline (CSS and the two web fonts as data URIs), so each file opens standalone.
Writes wireframes/*.html and wireframes/index-wireframes.html.
"""
import base64, html, os, re, urllib.parse
from PIL import Image

PAGES = [("index", "Homepage"), ("projects", "Projects"),
         ("room-01-jackson-home", "Case study 01 — The Henry Ford Jackson Home"),
         ("room-02-power-energy", "Case study 02 — Power & Energy"),
         ("room-03-rhode-island", "Case study 03 — Rhode Island 401 Health App"),
         ("room-04-littelfuse", "Case study 04 — Littelfuse"),
         ("private-view", "Private view (password page)")]
OUT = "wireframes"
os.makedirs(OUT, exist_ok=True)


def font_face(family, style, weight, file):
    b64 = base64.b64encode(open(f"tools/fonts/{file}", "rb").read()).decode()
    return (f"@font-face{{font-family:'{family}';font-style:{style};font-weight:{weight};font-display:block;"
            f"src:url(data:font/woff2;base64,{b64}) format('woff2')}}")


FONTS = "\n".join([
    font_face("Inter Tight", "normal", "400 500", "inter-tight-latin.woff2"),
    font_face("Inter Tight", "italic", "400", "inter-tight-italic-latin.woff2"),
    font_face("Instrument Sans", "normal", "400 500", "instrument-sans-latin.woff2"),
    font_face("Instrument Sans", "italic", "400", "instrument-sans-italic-latin.woff2")])

WF_CSS = """
/* ---- wireframe overrides: greyscale, grey boxes, labels ---- */
:root{--alt:#F2F2F2}
.m,.v{position:relative}
.wf-label{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);max-width:90%;padding:5px 8px;background:#fff;border:1px solid #9a9a9a;
  font:500 11px/1.3 'Inter Tight',Arial,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:#333;text-align:center;white-space:normal;pointer-events:none;z-index:1}
.panel .wf-label{top:40%}
.mod--video .wf-vid{display:block;width:100%;height:auto}
.mod--video-v .wf-vid{width:auto;max-height:78vh}
.panel .m,.panel:hover .m{filter:brightness(.55)}
.wf-tag{position:fixed;right:12px;bottom:12px;z-index:50;padding:6px 10px;background:#111;color:#fff;font:500 11px/1.3 'Inter Tight',Arial,sans-serif;letter-spacing:.08em;text-transform:uppercase}
.wf-tag a{text-decoration:underline;text-underline-offset:.2em}
"""


def box(w, h):
    """A grey placeholder with the source's exact proportions and a wireframe cross."""
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" preserveAspectRatio="none">'
           f'<rect width="{w}" height="{h}" fill="#D6D6D6"/>'
           f'<path d="M0 0L{w} {h}M{w} 0L0 {h}" stroke="#B4B4B4" stroke-width="1.5" vector-effect="non-scaling-stroke"/></svg>')
    return "data:image/svg+xml," + urllib.parse.quote(svg)


def size(src):
    return Image.open("site/" + src).size


def ph_img(tag, label):
    src = re.search(r'src="([^"]+)"', tag).group(1)
    w, h = size(src)
    alt = re.search(r'alt="([^"]*)"', tag)
    alt = alt.group(1) if alt else ""
    return f'<img src="{box(w, h)}" alt="{alt}" width="{w}" height="{h}"><span class="wf-label">{html.escape(label)}</span>'


def ph_video(tag, label):
    poster = re.search(r'poster="([^"]+)"', tag).group(1)
    w, h = size(poster)
    return f'<img class="wf-vid" src="{box(w, h)}" alt="" width="{w}" height="{h}"><span class="wf-label">{html.escape(label)}</span>'


def convert(page, name):
    s = open(f"site/{page}.html").read()
    # 1. figures with a FIG. number: label every image / video inside with that number
    def fig(m):
        block = m.group(0)
        n = re.search(r"Fig\. (\d+)", block)
        if not n:
            return block
        lab = f"FIG. {n.group(1)}"
        rt = re.search(r"Running time ([0-9:]+)", block)
        block = re.sub(r"<img [^>]*>", lambda i: ph_img(i.group(0), f"IMAGE — {lab}"), block)
        block = re.sub(r"<video[^>]*></video>", lambda v: ph_video(v.group(0), f"VIDEO — {lab}" + (f" · {rt.group(1)}" if rt else "")), block)
        return block
    s = re.sub(r"<figure\b.*?</figure>", fig, s, flags=re.S)
    # 2. the other images, labelled by what they are
    counters = {}

    def other(m):
        tag, before = m.group(0), s_[max(0, m.start() - 260):m.start()]
        if "data:image/svg" in tag:
            return tag
        if "hero__photo" in before:
            lab = "IMAGE — PORTRAIT"
        elif 'class="cover' in before:
            lab = "IMAGE — COVER PHOTO"
        elif 'class="panel' in before:
            counters["panel"] = counters.get("panel", 0) + 1
            lab = f"IMAGE — PANEL {counters['panel']:02d}"
        elif "row__img" in before or 'class="card' in before:
            counters["proj"] = counters.get("proj", 0) + 1
            lab = f"IMAGE — PROJECT {counters['proj']:02d} COVER"
        elif "lock__bg" in before:
            lab = "IMAGE — BACKGROUND (8%)"
        else:
            lab = "IMAGE"
        return ph_img(tag, lab)
    s_ = s
    s = re.sub(r"<img [^>]*>", other, s)
    assert "assets/img/" not in re.sub(r'href="assets/img/[^"]*"', "", s), page
    # 3. no links to full-size images; no external files
    s = re.sub(r'href="assets/[^"]*"', 'href="#"', s)
    s = s.replace(' target="_blank" rel="noopener"', "")
    s = re.sub(r'<link rel="preconnect"[^>]*>\n?', "", s)
    s = re.sub(r'<link rel="stylesheet" href="https://fonts[^>]*>\n?', "", s)
    css = open("site/assets/css/r3.css").read()
    s = s.replace('<link rel="stylesheet" href="assets/css/r3.css">', f"<style>\n{FONTS}\n{css}\n{WF_CSS}</style>")
    s = re.sub(r"<title>(.*?)</title>", r"<title>Wireframe — \1</title>", s, count=1)
    s = s.replace("</body>", f'<p class="wf-tag">Wireframe · {html.escape(name)} · <a href="index-wireframes.html">all pages</a></p>\n</body>')
    assert not re.search(r'(?:src|href)="(?:https?://|assets/)', s), page    # standalone: nothing external
    open(f"{OUT}/{page}.html", "w").write(s)
    return os.path.getsize(f"{OUT}/{page}.html")


sizes = {p: convert(p, n) for p, n in PAGES}

rows = "".join(f'<li><a href="{p}.html"><span class="n">{k:02d}</span><span class="t">{html.escape(n)}</span>'
               f'<span class="f">{p}.html</span></a></li>' for k, (p, n) in enumerate(PAGES, 1))
index = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Wireframes — Yasmin Bajwa portfolio</title>
<style>
{FONTS}
*{{box-sizing:border-box}}
body{{margin:0;background:#fff;color:#111;font:400 17px/1.6 'Inter Tight',Arial,sans-serif}}
main{{max-width:1100px;margin:0 auto;padding:clamp(48px,7vw,112px) clamp(20px,3.4vw,48px)}}
.label{{font:500 11px/1.45 'Inter Tight',Arial,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:rgba(17,17,17,.62)}}
h1{{font:400 clamp(40px,5vw,72px)/1.02 'Instrument Sans',Arial,sans-serif;letter-spacing:-.01em;margin:12px 0 24px}}
p{{max-width:62ch;margin:0 0 12px}}
ol{{list-style:none;padding:0;margin:48px 0 0;border-top:1px solid #111}}
li a{{display:grid;grid-template-columns:56px 1fr auto;gap:16px;align-items:baseline;padding:18px 0;border-bottom:1px solid rgba(17,17,17,.14);color:inherit;text-decoration:none}}
li a:hover .t{{text-decoration:underline;text-underline-offset:.22em}}
.n{{font-family:'Instrument Sans',Arial,sans-serif;color:rgba(17,17,17,.62)}}
.t{{font:400 24px/1.25 'Instrument Sans',Arial,sans-serif}}
.f{{font-size:13px;color:rgba(17,17,17,.62)}}
@media (max-width:600px){{li a{{grid-template-columns:40px 1fr}}.f{{display:none}}.t{{font-size:20px}}}}
</style>
</head>
<body>
<main>
<p class="label">Yasmin Bajwa · portfolio · for layout approval</p>
<h1>Wireframes</h1>
<p>Greyscale wireframes of all seven pages. They have the same grid, proportions and hairlines as the design, and all of Yasmin's text is in place. Every image and video is a grey box labelled with its figure number (“IMAGE — FIG. 3”), so the layout can be approved before the visuals.</p>
<p>Each file opens on its own in any browser. Nothing else needs to be downloaded.</p>
<ol>{rows}</ol>
</main>
</body>
</html>
"""
open(f"{OUT}/index-wireframes.html", "w").write(index)
print({k: f"{v // 1024} KB" for k, v in sizes.items()})
