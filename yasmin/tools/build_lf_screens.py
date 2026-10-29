"""Littelfuse hi-fi screens (Room 04): Adobe XD captures -> web images + content/lf-screens.json.

Source: her doc "Little Fuse Wireframes" (13 Adobe XD share links). Each XD screen was rendered whole by the XD web viewer
(viewport set to the artboard's full height) and screenshotted: desktop at 1.5x, mobile at 3x; saved at 1600px and 720px wide (capture scripts in the session
scratchpad; see squarespace/LITTELFUSE-SCREENS.md). Run from yasmin/:
    python3 tools/build_lf_screens.py <captures dir>      # full/<k>.png, k = screen index in jobs.json order
Flow names are her doc's headings. Captions are short descriptions of each screen (added, for Yasmin to approve); the XD
screen names are not used because some contain internal notes and a colleague's name.
"""
import json, os, sys
from PIL import Image

CAP = sys.argv[1] if len(sys.argv) > 1 else "."
OUT = "site/assets/img/lf"
os.makedirs(OUT, exist_ok=True)

# (flow, [(capture index, caption), ...]); capture index = order of jobs.json (13 XD files, artboards in XD order)
DESKTOP = [
    ("Home & Mega Menu", [(0, "Home page"), (1, "Mega menu")]),
    ("Product Flow (L0 – L7)", [(2, "L0 · All products"), (3, "L0 · All products, expanded"), (4, "L1 · Product super-category: Fuses & Overcurrent Protection"),
                                 (5, "L2 · Product category: Fuses"), (6, "L3 · Product sub-category: Cartridge Fuses"), (7, "L6 · Series 232, table collapsed"),
                                 (8, "L6 · Series 232, table expanded"), (9, "L7 · Part 02323.15")]),
    ("Check Stock from Parametric Table", [(11, "Home page"), (12, "Check Distributor Stock page"), (13, "Typing a part number: autocomplete"),
                                           (14, "Part number entered"), (15, "Stock results"), (16, "Results: several parts and distributors"),
                                           (17, "Inline error message")]),
    ("Check Stock from Global Navigation", [(18, "Home page"), (19, "Check Distributor Stock page"), (20, "Typing a part number: autocomplete"),
                                            (21, "Part number entered"), (22, "Stock results"), (23, "Results: several parts and distributors"),
                                            (24, "Inline error message")]),
    ("Request Sample from Parametric Table", [(25, "L6 · Product series table"), (26, "L6 · Choosing a part"), (27, "L6 · One product added to the sample list"),
                                              (28, "Sample list"), (29, "Sample list: autosuggestion"), (30, "Sample list: product in the field"),
                                              (31, "Sample list: one product added"), (32, "L0 · All products"), (33, "Sample order: details"),
                                              (34, "Sample order: details, continued"), (35, "Thank-you page")]),
    ("Request Sample from Global Navigation", [(36, "Home page"), (37, "Sample list, from the global navigation"), (38, "Sample list: autosuggestion"),
                                               (39, "Sample list: product in the field"), (40, "Sample list: product added"), (41, "L0 · All products")]),
    ("Where to Buy", [(42, "Home page with the Where to Buy overlay"), (43, "Find distributors: results"), (44, "Find distributors: results, 2"),
                      (45, "Find distributors: results, 3"), (46, "Find distributors: results, 4"), (47, "Find distributors: results, 5"),
                      (48, "Find distributors: results, 6"), (49, "Find distributors: results, 7"), (50, "Check distributor stock")]),
    ("Search (Auto Suggest)", [(51, "Auto-suggestion: “0232 – Fuses”"), (52, "Auto-suggestion: “Cartridge”"), (53, "After the click: L3 sub-category"),
                               (54, "Auto-suggestion: part number “0232”")]),
    ("Search (Results Pages)", [(55, "Results “Cartridge”: products"), (56, "Results “Cartridge”: technical documents"), (57, "Results “232”"),
                                (58, "Interstitial: “Fuse”")]),
]
MOBILE = [
    ("Home & Mega Menu", [(61, "Home page"), (62, "Home page, longer version"), (63, "Home page, menu opening"), (64, "Menu"),
                          (65, "Menu: Products"), (66, "Menu: Fuses & Overcurrent Protection"), (67, "Menu: Fuses")]),
    ("Product Pages L0 – L7", [(69, "L0 · All products"), (70, "L0 · Introduction expanded"), (71, "L0 · Introduction expanded, variant"),
                               (72, "L1 · Fuses & Overcurrent Protection"), (73, "L1 · Introduction expanded"), (74, "L2 · Fuses"),
                               (75, "L3 · Cartridge Fuses"), (76, "L3 · Cartridge Fuses, variant"), (77, "Sort"), (78, "Filters"),
                               (79, "L6 · Series 232"), (80, "L6 · Series 232, continued"), (81, "L7 · Part 02323.15"), (82, "L7 · Part LCFE160804A180TG")]),
    ("Check Distributor Stock", [(84, "Check Distributors Stock: results"), (85, "Filters")]),
    ("Request Sample", [(87, "Sample list: one item"), (88, "Sample list: adding several part numbers"), (89, "Sample list: eleven items"),
                        (90, "Log in to MyLittelfuse")]),
    ("Where to Buy", [(92, "Distributor list"), (93, "Filters"), (94, "Map view")]),
    ("Search Pages", [(96, "Auto-suggestion: “232”"), (97, "Auto-suggestion: “0232”"), (98, "Auto-suggestion: “cart”"),
                      (99, "Results for “Cartridge”: products"), (100, "Results"), (101, "Results, continued"), (102, "Results: refine"),
                      (103, "Product series"), (104, "Results: technical documents")]),
]


def export(k, kind, n_flow, n_screen):
    im = Image.open(f"{CAP}/full/{k}.png").convert("RGB")
    W = 1600 if kind == "d" else 720
    if im.width > W:
        im = im.resize((W, round(im.height * W / im.width)), Image.LANCZOS)
    name = f"lf-{kind}-{n_flow:02d}-{n_screen:02d}.jpg"
    im.save(f"{OUT}/{name}", quality=80 if kind == "d" else 82, optimize=True, progressive=True)
    css_w = 1366 if kind == "d" else 320
    return name, css_w, round(im.height * css_w / im.width)


data = {}
for key, groups, kind in (("desktop", DESKTOP, "d"), ("mobile", MOBILE, "m")):
    out = []
    for fi, (flow, screens) in enumerate(groups, 1):
        rows = []
        for si, (k, cap) in enumerate(screens, 1):
            name, w, h = export(k, kind, fi, si)
            rows.append({"file": name, "caption": cap, "w": w, "h": h, "xd": k})
        out.append({"flow": flow, "screens": rows})
    data[key] = out
json.dump(data, open("content/lf-screens.json", "w"), indent=1, ensure_ascii=False)
n = sum(len(g["screens"]) for v in data.values() for g in v)
size = sum(os.path.getsize(f"{OUT}/{f}") for f in os.listdir(OUT))
print(f"{n} screens -> {OUT} ({size / 1e6:.1f} MB); content/lf-screens.json")

# Console helper for Squarespace: finds the uploaded screens by file name on the page (Asset Library, or a hidden page with a
# gallery of them) and copies the two filled-in data lines for squarespace/littelfuse-screens.html.
spec = {k: [[g["flow"], [[x["file"], x["caption"], x["w"], x["h"]] for x in g["screens"]]] for g in v] for k, v in data.items()}
helper = ("(function(){var S=" + json.dumps(spec, ensure_ascii=False, separators=(",", ":")) + ",u={};"
          "document.querySelectorAll('img').forEach(function(im){[im.getAttribute('data-src'),im.getAttribute('data-image'),im.currentSrc,im.src].forEach(function(s){"
          "s=(s||'').split('?')[0];var m=decodeURIComponent(s).match(/(lf-[dm]-\\d\\d-\\d\\d)(\\.jpe?g)?$/i);if(m&&/squarespace/.test(s))u[m[1].toLowerCase()]=s;});});"
          "var miss=[],n=0;function f(groups){return JSON.stringify(groups.map(function(g){return [g[0],g[1].map(function(x){var k=x[0].replace(/\\.jpg$/,'');"
          "if(u[k])n++;else miss.push(x[0]);return [u[k]||'MISSING:'+x[0],x[1],x[2],x[3]];})];}));}"
          "var out='var DESKTOP = '+f(S.desktop)+';\\n  var MOBILE = '+f(S.mobile)+';';copy(out);"
          "console.log(n+' of '+(n+miss.length)+' screens found and copied.'+(miss.length?' Missing (scroll so they show, or upload them, then run again): '+miss.join(', '):' Paste over the two lines var DESKTOP = []; var MOBILE = []; in the code.'));})();")
open("squarespace/get-littelfuse-addresses.js", "w").write(
    "// Paste into the browser Console on the page that shows the uploaded Littelfuse screens (see LITTELFUSE-SCREENS.md).\n" + helper + "\n")
print("squarespace/get-littelfuse-addresses.js written")
