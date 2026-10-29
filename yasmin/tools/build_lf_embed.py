"""Littelfuse desktop screens: a ready-to-paste Squarespace Code Block (no uploads, no addresses to fill in).

The screens are served from this public GitHub repo through the jsDelivr CDN, pinned to one commit so the
addresses never change. Run from yasmin/:
    python3 tools/build_lf_embed.py thumbs            # step 1: step-strip thumbnails (commit and push them)
    python3 tools/build_lf_embed.py embed <commit>    # step 2: squarespace/littelfuse-desktop-embed.html
The Code Block is squarespace/littelfuse-screens.html with only its desktop part.
"""
import json, os, re, sys

LF = "site/assets/img/lf"
lf = json.load(open("content/lf-screens.json"))

if sys.argv[1] == "thumbs":
    from PIL import Image
    os.makedirs(f"{LF}/thumbs", exist_ok=True)
    for g in lf["desktop"]:
        for x in g["screens"]:
            im = Image.open(f"{LF}/{x['file']}").convert("RGB")
            top = im.crop((0, 0, im.width, min(im.height, round(im.width * 74 / 118))))
            top.resize((360, round(360 * top.height / top.width)), Image.LANCZOS).save(f"{LF}/thumbs/{x['file']}", quality=74, optimize=True)
    print("thumbs written:", len(os.listdir(f"{LF}/thumbs")))
    sys.exit()

commit = sys.argv[2]
base = f"https://cdn.jsdelivr.net/gh/Skylarnina/Skylarnina@{commit}/yasmin/{LF}/"
code = open("squarespace/littelfuse-screens.html").read()
code = code[code.index("-->") + 3:].strip()
code = re.sub(r'\n  <div class="lfx__part" data-part="mobile">.*?\n  </div>\n</div>', "\n</div>", code, count=1, flags=re.S)
assert 'data-part="mobile"' not in code.split("<style>")[0]
desk = [[g["flow"], [[base + x["file"], x["caption"], x["w"], x["h"], base + "thumbs/" + x["file"]] for x in g["screens"]]] for g in lf["desktop"]]
code = code.replace("var DESKTOP = [];", "var DESKTOP = " + json.dumps(desk, ensure_ascii=False) + ";", 1)
head = ("<!--\n  Littelfuse hi-fi screens, desktop flows (Room 04, Fig. 08). Ready to paste: Squarespace 7.1, one Code Block,\n"
        "  full width of the section, Display Source off. Nothing to fill in: the 58 screens load from the portfolio's\n"
        f"  GitHub repo through the jsDelivr CDN, pinned to commit {commit[:7]}.\n-->\n")
open("squarespace/littelfuse-desktop-embed.html", "w").write(head + code + "\n")
print("squarespace/littelfuse-desktop-embed.html", len(code) // 1024, "KB")
