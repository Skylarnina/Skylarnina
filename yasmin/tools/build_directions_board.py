"""The colour-direction usage guide: brand/colour-directions.html (+ screenshots/colour-directions.png).

Run from yasmin/ after rendering the homepages into screenshots/directions/ (see the end of this file):
    python3 tools/build_directions_board.py
For each of the three directions (Archive, Salon, Campus): the idea, the palette with its share of the page,
a section-by-section colour map of the homepage, a case study and the lock screen (each block labelled with
its ground, its text and any accent), the rules, and the real homepage beside the map. Values match r3.css.
"""
import html

P, P2, INK, WINE, NAVY, WINK = "#F3F0EA", "#E9E4DB", "#1C2635", "#8C2F1E", "#1E3F63", "#16140F"
V = {"orange": "#E9A35B", "olive": "#8A8D4F", "red": "#B04A44", "blue": "#6E94AB", "navy": NAVY}
VT = {"olive": "#63653A", "orange": "#8E5412", "blue": "#48677A", "red": "#A8443F"}
ROWS = [("01", "olive"), ("02", "orange"), ("03", "blue"), ("04", "red")]   # project → venue colour
CREAM = P

D = [
    {"id": "heritage", "name": "Archive", "lead": ("navy", NAVY),
     "idea": "The museum label. Quiet paper and navy type; the card's colours only tell you which project you're in. The work carries the colour.",
     "share": [("paper", P, 62), ("paper 2", P2, 12), ("navy ink", INK, 16), ("navy band", NAVY, 7), ("wine", WINE, 2), ("venue colours", "linear", 1)],
     "palette": [("paper", P, "page"), ("paper 2", P2, "Snippets, Reflection, tiles"), ("ink", INK, "all type"), ("navy", NAVY, "Contact band"), ("wine", WINE, "“Yasmin.”, links, Enter")],
     "home": [("Header", P, INK, "paper · ink"), ("Hero", P, INK, "paper · ink · “Yasmin.” in wine", "name"), ("Snippets", P2, INK, "paper 2 · ink"),
              ("Disciplines", "panels-ink", "#FFFFFF", "photos under navy ink 60% · white"), ("Projects", "rows-bar", INK, "paper · 3px venue bar + number per project · five-colour rule over the list"),
              ("Contact", NAVY, CREAM, "navy band · cream text · orange link underline"), ("Footer", P, INK, "paper · ink")],
     "case": [("Cover", "cover-ink", "#FFFFFF", "photo under navy ink 60% · cream title"), ("Meta", P, INK, "paper card"), ("Index", P, INK, "ink rules · numbers in project colour"),
              ("Chapters", P, INK, "paper · chapter + FIG. numbers in project colour"), ("Reflection", P2, INK, "paper 2"), ("Prev / next", P, INK, "paper")],
     "lock": (P, INK, WINE, "paper · Enter in wine"),
     "rules": ["One coloured band per page: navy Contact.", "Venue colours are marks: 3px bars, numbers. Never a fill, never text larger than a number.",
               "Wine only for Yasmin: her name, links, the Enter button."]},
    {"id": "salon", "name": "Salon", "lead": ("wine", WINE),
     "idea": "Yasmin's own room. Wine is her voice: it fills the sections that are about her (Snippets, every Reflection, the door to her work). Everything else stays paper.",
     "share": [("paper", P, 58), ("paper 2", P2, 10), ("warm ink", WINK, 14), ("wine", WINE, 17), ("venue colours", "linear", 1)],
     "palette": [("paper", P, "page"), ("paper 2", P2, "Contact"), ("warm ink", WINK, "all type"), ("wine", WINE, "Snippets, Reflection, lock, “Yasmin.”"), ("cream on wine", CREAM, "text on wine")],
     "home": [("Header", P, WINK, "paper · warm ink"), ("Hero", P, WINK, "paper · “Yasmin.” in wine", "name"), ("Snippets", WINE, CREAM, "wine band · cream text · slideshow on a 12px cream frame"),
              ("Disciplines", "panels-warm", "#FFFFFF", "photos under warm ink 60% · white"), ("Projects", "rows-bar", WINK, "paper · 3px venue bar + number per project · five-colour rule"),
              ("Contact", P2, WINK, "paper 2 · wine link underline"), ("Footer", P, WINK, "paper")],
     "case": [("Cover", "cover-warm", "#FFFFFF", "photo under warm ink 60% · cream title"), ("Meta", P, WINK, "paper card"), ("Index", P, WINK, "ink rules · numbers in project colour"),
              ("Chapters", P, WINK, "paper · numbers in project colour"), ("Reflection", WINE, CREAM, "wine band · cream italic"), ("Prev / next", P, WINK, "paper")],
     "lock": (WINE, CREAM, WINE, "wine ground · paper card · Enter in wine"),
     "rules": ["Wine only where the page is about her: Snippets, Reflection, the lock screen, her name.", "Never wine on the work (case-study chapters stay paper).",
               "Wine and the card red never touch: red is only Littelfuse's 3px bar and number."]},
    {"id": "campus", "name": "Campus", "lead": ("the card", "venues"),
     "idea": "The business card as a map. Each section takes a soft tint of a venue colour in the card's order, and each project sits on its own venue tint. Colourful, but never loud: tints, not fills.",
     "share": [("paper", P, 40), ("venue tints", "tints", 34), ("navy ink", INK, 14), ("navy band", NAVY, 8), ("venue colours", "linear", 3), ("wine", WINE, 1)],
     "palette": [("orange tint", "#F1E4D3", "Hero"), ("olive tint", "#E2E0D1", "Snippets"), ("row tints", "#E3E5E2", "one per project"), ("navy", NAVY, "Contact, links, Enter"), ("wine", WINE, "“Yasmin.” only")],
     "home": [("Header", P, INK, "paper"), ("Hero", "#F1E4D3", INK, "orange tint #F1E4D3 · “Yasmin.” in wine", "name"), ("Snippets", "#E2E0D1", INK, "olive tint #E2E0D1"),
              ("Disciplines", "panels-venue", "#FFFFFF", "photos under orange · olive · red · light blue at 55% · white"), ("Projects", "rows-tint", INK, "each row on its venue tint (12%) · plate on paper"),
              ("Contact", NAVY, CREAM, "navy band (the card ends navy)"), ("Footer", P, INK, "paper")],
     "case": [("Cover", "cover-ink", "#FFFFFF", "photo under navy ink 60%"), ("Meta", P, INK, "paper card"), ("Index", "index-room", INK, "3px rule in the project colour"),
              ("Chapters", P, INK, "paper · numbers in project colour"), ("Reflection", "#E2E0D0", INK, "the project's tint"), ("Prev / next", P, INK, "paper")],
     "lock": ("#DEE1E0", INK, NAVY, "light-blue tint · Enter in navy"),
     "rules": ["Tints for grounds (12–16%), full colour only on the photos and 3px marks.", "Keep the card's order down the page: orange, olive, the four, navy.",
               "Navy is the accent (links, Enter); wine is only her name."]},
]
H = {"Header": 28, "Hero": 92, "Snippets": 112, "Disciplines": 70, "Projects": 150, "Contact": 76, "Footer": 26}
HC = {"Cover": 74, "Meta": 36, "Index": 36, "Chapters": 92, "Reflection": 46, "Prev / next": 28}
E = html.escape


def stripe():
    return '<div class="stripe">' + "".join(f'<i style="background:{c}"></i>' for c in V.values()) + "</div>"


def block(name, ground, ink, label, h, extra=None, d=None):
    lab = f'<b>{E(name)}</b><span>{E(label)}</span>'
    if ground == "rows-bar":
        rows = "".join(f'<div class="r"><i style="background:{V[c]}"></i><em style="color:{VT[c]}">{n}</em><u></u></div>' for n, c in ROWS)
        return f'<div class="blk proj" style="background:{P};color:{ink}">{lab}{stripe()}{rows}</div>'
    if ground == "rows-tint":
        tints = {"olive": "#E6E4D7", "orange": "#F2E7D9", "blue": "#E3E5E2", "red": "#EBDCD6"}
        rows = "".join(f'<div class="r" style="background:{tints[c]}"><em style="color:{VT[c]}">{n}</em><u style="background:{P}"></u></div>' for n, c in ROWS)
        return f'<div class="blk proj" style="background:{P};color:{ink}">{lab}{stripe()}{rows}</div>'
    if ground.startswith("panels"):
        layer = {"panels-ink": [INK] * 4, "panels-warm": [WINK] * 4, "panels-venue": [V["orange"], V["olive"], V["red"], V["blue"]]}[ground]
        cells = "".join(f'<div class="p" style="background:linear-gradient({c}99,{c}99),#7d7468"></div>' for c in layer)
        return f'<div class="blk pan" style="height:{h}px;color:{ink}">{cells}<div class="pl">{lab}</div></div>'
    if ground.startswith("cover"):
        c = {"cover-ink": INK, "cover-warm": WINK}[ground]
        return f'<div class="blk" style="height:{h}px;background:linear-gradient({c}99,{c}99),#7d7468;color:{ink}">{lab}</div>'
    if ground == "index-room":
        return f'<div class="blk" style="height:{h}px;background:{P};color:{ink};box-shadow:inset 0 3px 0 {V["olive"]}">{lab}</div>'
    style = f"height:{h}px;background:{ground};color:{ink}"
    if extra == "name":
        lab = f'<b>{E(name)}</b><span>{E(label)}</span><span class="nm">Hi, I’m <i style="color:{WINE}">Yasmin.</i></span>'
    return f'<div class="blk" style="{style}">{lab}</div>'


cols = ""
for d in D:
    lead = d["lead"]
    lead_chip = stripe() if lead[1] == "venues" else f'<i class="lc" style="background:{lead[1]}"></i>'
    share = "".join(f'<i style="flex:{p};background:{c if c.startswith("#") else ("linear-gradient(90deg," + ",".join(V.values()) + ")" if c == "linear" else "linear-gradient(90deg,#F1E4D3,#E2E0D1,#E3E5E2,#EBDCD6)")}" title="{n} {p}%"></i>' for n, c, p in d["share"])
    share_lab = " · ".join(f"{n} {p}%" for n, c, p in d["share"])
    pal = "".join(f'<div class="ch"><i style="background:{c}"></i><b>{E(n)}</b><code>{c}</code><span>{E(r)}</span></div>' for n, c, r in d["palette"])
    home = "".join(block(n, g, i, l, H[n], *(x[4:5] if len(x) > 4 else [None])) for x in d["home"] for n, g, i, l in [x[:4]])
    case = "".join(block(n, g, i, l, HC[n]) for n, g, i, l in d["case"])
    lg, li, le, ll = d["lock"]
    card = P if d["id"] == "salon" else "transparent"
    lock = (f'<div class="lock" style="background:{lg};color:{li}"><div class="card" style="background:{card};color:{INK if d["id"]=="salon" else li}">'
            f'<span>Projects are shared <i>by invitation.</i></span><em style="background:{le}">Enter</em></div><span class="ll">{E(ll)}</span></div>')
    rules = "".join(f"<li>{E(r)}</li>" for r in d["rules"])
    cols += f'''<section class="dir">
  <header><h2>{d["name"]}</h2><div class="lead">{lead_chip}<span>lead: {E(lead[0])}</span></div></header>
  <p class="idea">{E(d["idea"])}</p>
  <div class="share">{share}</div><p class="sl">{E(share_lab)}</p>
  <div class="pal">{pal}</div>
  <div class="maps">
    <div class="map"><h3>Homepage, section by section</h3>{home}<h3>Case study</h3>{case}<h3>Lock screen</h3>{lock}</div>
    <div class="shot"><h3>As built</h3><img src="../screenshots/directions/{d["id"]}_home.png" alt="{d["name"]} homepage"></div>
  </div>
  <h3>Rules</h3><ul>{rules}</ul>
</section>'''

page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Colour directions · Yasmin Bajwa</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter+Tight:ital,wght@0,400;0,500;1,400&display=swap">
<style>
*{{box-sizing:border-box}} body{{margin:0;background:#DCD9D3;font:400 13px/1.45 'Inter Tight',Arial,sans-serif;color:#1C2635}}
.wrap{{padding:44px 44px 56px;width:max-content}}
h1{{font:400 46px/1 'Instrument Serif',Georgia,serif;margin:0 0 10px}}
.intro{{max-width:1500px;font-size:15px;margin:0 0 8px}}
.const{{display:flex;gap:22px;align-items:center;background:#F3F0EA;padding:14px 18px;margin:16px 0 26px;width:1812px}}
.const b{{font:500 10px/1.3 'Inter Tight';letter-spacing:.1em;text-transform:uppercase}}
.const .k{{display:flex;gap:8px;align-items:center}} .const i{{display:inline-block;width:22px;height:22px;border:1px solid rgba(0,0,0,.15)}}
.grid{{display:grid;grid-template-columns:repeat(3,588px);gap:24px}}
.dir{{background:#fff;padding:22px 22px 18px}}
.dir header{{display:flex;justify-content:space-between;align-items:baseline}}
h2{{font:400 40px/1 'Instrument Serif',Georgia,serif;margin:0}}
.lead{{display:flex;gap:8px;align-items:center;font:500 10px/1 'Inter Tight';letter-spacing:.1em;text-transform:uppercase}}
.lead .lc{{width:26px;height:14px;display:inline-block}} .lead .stripe{{width:70px}}
.idea{{font-size:14px;margin:10px 0 14px;min-height:62px}}
.share{{display:flex;height:16px}} .share i{{display:block}} .sl{{font-size:10.5px;color:#555;margin:5px 0 12px}}
.pal{{display:grid;grid-template-columns:repeat(5,1fr);gap:8px;margin-bottom:16px}}
.ch i{{display:block;height:34px;border:1px solid rgba(0,0,0,.14);margin-bottom:5px}} .ch b{{display:block;font-weight:500;font-size:11px}}
.ch code{{font:10.5px/1.3 ui-monospace,monospace;color:#333}} .ch span{{display:block;font-size:10px;color:#666;line-height:1.3}}
h3{{font:500 10px/1.3 'Inter Tight';letter-spacing:.1em;text-transform:uppercase;margin:12px 0 6px;color:#555}}
.maps{{display:grid;grid-template-columns:1fr 200px;gap:16px}}
.map{{display:flex;flex-direction:column}}
.blk{{position:relative;padding:5px 8px;display:flex;flex-direction:column;gap:1px;border-bottom:1px solid rgba(0,0,0,.08);overflow:hidden}}
.blk b{{font:500 10px/1.2 'Inter Tight';letter-spacing:.08em;text-transform:uppercase}} .blk span{{font-size:10.5px;line-height:1.3}}
.blk .nm{{font:400 22px/1 'Instrument Serif',serif;margin-top:6px}}
.pan{{display:grid;grid-template-columns:repeat(4,1fr);padding:0;gap:1px;background:#fff}} .pan .p{{height:100%}}
.pan .pl{{position:absolute;inset:0;padding:5px 8px;display:flex;flex-direction:column;gap:1px}}
.proj .r{{display:grid;grid-template-columns:3px 22px 1fr 52px;gap:6px;align-items:center;height:24px;border-top:1px solid rgba(0,0,0,.08);margin:0 -8px;padding:0 8px}}
.proj .r i{{height:16px;display:block}} .proj .r em{{font:500 10px/1 'Inter Tight';font-style:normal}} .proj .r u{{grid-column:4;height:16px;background:#E9E4DB;display:block;text-decoration:none}}
.proj .stripe{{margin:6px 0 2px}}
.stripe{{display:flex;height:3px}} .stripe i{{flex:1}}
.lock{{height:84px;display:grid;place-items:center;position:relative}} .lock .card{{padding:8px 12px;display:flex;gap:10px;align-items:center;font:400 13px/1 'Instrument Serif',serif}}
.lock .card em{{font:500 9px/1 'Inter Tight';color:#fff;padding:5px 7px;font-style:normal}} .lock .ll{{position:absolute;bottom:4px;left:8px;font-size:10px}}
.shot img{{width:200px;display:block;outline:1px solid rgba(0,0,0,.15)}}
ul{{margin:0;padding-left:16px;font-size:12.5px}} li{{margin:2px 0}}
</style></head><body><div class="wrap">
<h1>Three colour directions</h1>
<p class="intro">Same layout, same copy, same photographs. Each direction gives cream, wine and The Henry Ford's colours a different job, so Yasmin can choose a mood, not just a swatch. Live in the prototype: the theme switcher, top-right (Archive · Salon · Campus).</p>
<div class="const"><b>Constant in all three</b>
<span class="k"><i style="background:{P}"></i>paper {P}</span><span class="k"><i style="background:{WINE}"></i>wine = “Yasmin.”</span>
<span class="k">{stripe().replace('class="stripe"', 'class="stripe" style="width:80px"')}project colours: 01 olive · 02 orange · 03 light blue · 04 red</span>
<span class="k">type: Instrument Serif + Inter Tight · every text ≥ 4.5:1</span></div>
<div class="grid">{cols}</div></div></body></html>'''
open("brand/colour-directions.html", "w").write(page)
print("brand/colour-directions.html")
