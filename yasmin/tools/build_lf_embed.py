"""Littelfuse desktop screens: a ready-to-paste Squarespace Code Block (no uploads, no addresses to fill in).

The screens are served from this public GitHub repo through the jsDelivr CDN, pinned to one commit so the
addresses never change. Run from yasmin/:
    python3 tools/build_lf_embed.py thumbs            # step 1: step-strip thumbnails + phone-row copies (commit and push them)
    python3 tools/build_lf_embed.py embed <commit> [lf|ri]   # step 2: squarespace/<name>-desktop-embed.html and -mobile-embed.html
Each embed is squarespace/littelfuse-screens.html (the shared screens Code Block) with one part and its data filled in.
(Rhode Island's thumbnails and phone copies are made by tools/build_ri_screens.py.)
"""
import json, os, re, sys

KEY = sys.argv[3] if len(sys.argv) > 3 else "lf"           # lf: Littelfuse (Room 04) · ri: Rhode Island (Room 03)
NAME, SITE, ROOM = {"lf": ("littelfuse", "littelfuse.com", "Littelfuse hi-fi screens (Room 04, Fig. 08)"),
                    "ri": ("rhode-island", "health.ri.gov", "Rhode Island screens: test scheduling portal and 401 Health app (Room 03)")}[KEY]
LF = f"site/assets/img/{KEY}"
lf = json.load(open(f"content/{KEY}-screens.json"))

if sys.argv[1] == "thumbs":
    from PIL import Image
    os.makedirs(f"{LF}/thumbs", exist_ok=True)
    for g in lf["desktop"]:
        for x in g["screens"]:
            im = Image.open(f"{LF}/{x['file']}").convert("RGB")
            top = im.crop((0, 0, im.width, min(im.height, round(im.width * 74 / 118))))
            top.resize((360, round(360 * top.height / top.width)), Image.LANCZOS).save(f"{LF}/thumbs/{x['file']}", quality=74, optimize=True)
    print("thumbs written:", len(os.listdir(f"{LF}/thumbs")))
    os.makedirs(f"{LF}/phone", exist_ok=True)   # lighter copies for the phone row (480px wide); the full 720px ones open enlarged
    for g in lf["mobile"]:
        for x in g["screens"]:
            im = Image.open(f"{LF}/{x['file']}").convert("RGB")
            im.resize((480, round(480 * im.height / im.width)), Image.LANCZOS).save(f"{LF}/phone/{x['file']}", quality=76, optimize=True, progressive=True)
    print("phone copies written:", len(os.listdir(f"{LF}/phone")))
    sys.exit()

commit = sys.argv[2]
base = f"https://cdn.jsdelivr.net/gh/Skylarnina/Skylarnina@{commit}/yasmin/{LF}/"
code = open("squarespace/littelfuse-screens.html").read()
code = code[code.index("-->") + 3:].strip().replace("var SITE = 'littelfuse.com';", f"var SITE = '{SITE}';", 1)
code = re.sub(r'\n  <div class="lfx__part" data-part="mobile">.*?\n  </div>\n</div>', "\n</div>", code, count=1, flags=re.S)
assert 'data-part="mobile"' not in code.split("<style>")[0]
desk = [[g["flow"], [[base + x["file"], x["caption"], x["w"], x["h"], base + "thumbs/" + x["file"]] for x in g["screens"]]] for g in lf["desktop"]]
code = code.replace("var DESKTOP = [];", "var DESKTOP = " + json.dumps(desk, ensure_ascii=False) + ";", 1)
nd = sum(len(g["screens"]) for g in lf["desktop"]); nm = sum(len(g["screens"]) for g in lf["mobile"])
head = (f"<!--\n  {ROOM}, desktop. Ready to paste: Squarespace 7.1, one Code Block,\n"
        f"  full width of the section, Display Source off. Nothing to fill in: the {nd} screens load from the portfolio's\n"
        f"  GitHub repo through the jsDelivr CDN, pinned to commit {commit[:7]}.\n-->\n")
open(f"squarespace/{NAME}-desktop-embed.html", "w").write(head + code + "\n")
print(f"squarespace/{NAME}-desktop-embed.html", len(code) // 1024, "KB")

# mobile: the phone row on its own
code = open("squarespace/littelfuse-screens.html").read()
code = code[code.index("-->") + 3:].strip().replace("var SITE = 'littelfuse.com';", f"var SITE = '{SITE}';", 1)
code = re.sub(r'\n  <div class="lfx__part" data-part="desktop">.*?\n  </div>\n(?=  <div class="lfx__part" data-part="mobile">)', "\n", code, count=1, flags=re.S)
assert 'data-part="desktop"' not in code.split("<style>")[0] and 'data-part="mobile"' in code
mob = [[g["flow"], [[base + x["file"], x["caption"], x["w"], x["h"], base + "phone/" + x["file"]] for x in g["screens"]]] for g in lf["mobile"]]
code = code.replace("var MOBILE = [];", "var MOBILE = " + json.dumps(mob, ensure_ascii=False) + ";", 1)
head = (f"<!--\n  {ROOM}, mobile, in phone mockups. Ready to paste: Squarespace 7.1, one Code Block,\n"
        f"  full width of the section, Display Source off. Nothing to fill in: the {nm} screens load from the portfolio's\n"
        f"  GitHub repo through the jsDelivr CDN, pinned to commit {commit[:7]}.\n-->\n")
open(f"squarespace/{NAME}-mobile-embed.html", "w").write(head + code + "\n")
print(f"squarespace/{NAME}-mobile-embed.html", len(code) // 1024, "KB")
