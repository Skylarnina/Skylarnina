"""Theme comparison (prototype only): THEMES.md and the swatch rows, read from site/assets/css/r3.css.

Run from yasmin/:  python3 tools/build_themes.py
Every value comes from the stylesheet (:root = mono, the cream / venues blocks, the bold themes' surface,
panel and band rules, and the venues per-room blocks), so the document can't drift from what the prototype shows.
Contrast is WCAG 2.x relative luminance; translucent colours are composited over the ground they sit on.
Text on photographs (bold panels, photo covers) is reported from the rendered audit, content/contrast-audit.json
(tools/contrast_audit.js), which measures every piece of text against the pixels behind it.
"""
import collections, json, os, re
from PIL import Image, ImageDraw, ImageFont

CSS = re.sub(r"/\*.*?\*/", "", open("site/assets/css/r3.css").read(), flags=re.S)
OUT_IMG = "screenshots/themes"
os.makedirs(OUT_IMG, exist_ok=True)


def block(sel):
    m = re.search(re.escape(sel) + r"\s*\{([^}]*)\}", CSS)
    return dict((k.strip(), v.strip()) for k, v in (p.split(":", 1) for p in m.group(1).split(";") if ":" in p))


ROOT = block(":root")
CREAM, VEN = block(':is([data-theme="cream"],[data-theme="cream-bold"])'), block(':is([data-theme="venues"],[data-theme="venues-bold"])')
THEMES = {"mono": ROOT, "cream": {**ROOT, **CREAM}, "cream-bold": {**ROOT, **CREAM, **block('[data-theme="cream-bold"]')},
          "venues": {**ROOT, **VEN}, "venues-bold": {**ROOT, **VEN, **block('[data-theme="venues-bold"]')}}
HER = block(':is([data-theme="heritage"],[data-theme="heritage-rich"],[data-theme="salon"],[data-theme="campus"])')
THEMES["heritage"] = {**ROOT, **HER}
THEMES["heritage-rich"] = {**ROOT, **HER}
THEMES["salon"] = {**ROOT, **HER, **block('[data-theme="salon"]')}
THEMES["campus"] = {**ROOT, **HER, **block('[data-theme="campus"]')}
ROOMS = {r: block(f':is([data-theme="venues"],[data-theme="venues-bold"]) .{r}') for r in ("room01", "room02", "room03", "room04")}
AUDIT = json.load(open("content/contrast-audit.json"))
ROOM_NAME = {"room01": "Room 01 · olive", "room02": "Room 02 · orange", "room03": "Room 03 · light blue", "room04": "Room 04 · red"}


def resolve(t, v, extra=None):
    d = {**THEMES[t], **(extra or {})}
    while "var(" in v:
        v = re.sub(r"var\((--[\w-]+)\)", lambda m: d[m.group(1)], v)
    return v


def rgba(v):
    v = v.strip()
    if v.startswith("#"):
        return tuple(int(v[i:i + 2], 16) for i in (1, 3, 5)) + (1.0,)
    r, g, b, a = re.match(r"rgba\(([\d.]+),([\d.]+),([\d.]+),([\d.]+)\)", v.replace(" ", "")).groups()
    return int(r), int(g), int(b), float(a)


def over(fg, bg):
    r, g, b, a = rgba(fg)
    R, G, B, _ = rgba(bg)
    return tuple(round(x * a + y * (1 - a)) for x, y in ((r, R), (g, G), (b, B)))


def lum(rgb):
    c = [x / 255 for x in rgb]
    c = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def ratio(fg, bg):
    a, b = sorted((lum(over(fg, bg)), lum(rgba(bg)[:3])), reverse=True)
    return (a + 0.05) / (b + 0.05)


def hx(rgb):
    return "#%02X%02X%02X" % rgb


VARS = ["--ground", "--ground-2", "--ink", "--ink-muted", "--ink-low", "--hairline", "--accent", "--accent-2", "--tile", "--tile-hover", "--link"]
WHERE = {
    "--ground": "Page ground: top bar, white sections, case-study meta panel, password page, theme switcher.",
    "--ground-2": "Secondary ground: Snippets and Contact sections, the ground behind image tiles, placeholders.",
    "--ink": "Body text, all headings, 1px ink rules (chapter index, contact, video captions), outline button, password field rule.",
    "--ink-muted": "11px caps labels, figure captions, footer text, password error, inactive switcher buttons.",
    "--ink-low": "Non-text only: the dashed placeholder border.",
    "--hairline": "Non-text only: hairline rules (top bar, project rows, panels, footer), inactive slideshow dots.",
    "--accent": {"mono": "= ink. Enter button fill. (Mono has no active-chapter state.)",
                 "cream": "Wine. Enter button fill and the active chapter in the index.",
                 "venues": "Light blue. Link text, current nav item, active slideshow dot, Enter button fill, active chapter on Home/Projects."},
    "--accent-2": {"mono": "= ink-muted. Section index numbers (project 01–04, chapter numbers) and the PASSWORD PROTECTED marker.",
                   "cream": "Wine. Section index numbers (project 01–04, chapter numbers) and the PASSWORD PROTECTED marker.",
                   "venues": "Orange (used sparingly). Project numbers 01–04 and the PASSWORD PROTECTED marker. Case pages use the room colour instead."},
    "--tile": "Logo tile ground (homepage project rows, Projects grid).",
    "--tile-hover": {"mono": "Logo tile ground on row/card hover.", "cream": "Logo tile ground on row/card hover.",
                     "venues": "Neutral fallback; each tile actually hovers to a pale tint of its own room colour (table below)."},
    "--link": {"mono": "Link underline = the link's own text colour (currentColor), as built.",
               "cream": "Wine. Link underlines and the current nav item's underline only; link text stays ink.",
               "venues": "Light blue. Link text and its underline."},
}
NAMES = {"mono": "Mono (current build, baseline)", "cream": "Cream", "venues": "Venues", "cream-bold": "Cream bold", "venues-bold": "Venues bold",
         "heritage": "Archive (heritage)", "heritage-rich": "Heritage rich", "salon": "Salon", "campus": "Campus"}


def where(t, k):
    w = WHERE[k]
    return w[t] if isinstance(w, dict) else w


def shown(t, k):
    v = resolve(t, THEMES[t][k])
    if v == "currentColor":
        return "currentColor", None
    g = resolve(t, THEMES[t]["--ground"])
    return v, hx(over(v, g))


# ---------------------------------------------------------------- swatch rows
try:
    F = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 15)
    FB = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 15)
except OSError:
    F = FB = ImageFont.load_default()


def swatches(t):
    W, H, PAD, GAP = 132, 84, 24, 12
    keys = VARS + (["--v-orange", "--v-olive", "--v-red", "--v-blue", "--v-navy"] if t == "venues" else [])
    img = Image.new("RGB", (PAD * 2 + len(keys) * (W + GAP) - GAP, PAD * 2 + H + 54), (255, 255, 255))
    d = ImageDraw.Draw(img)
    g = resolve(t, THEMES[t]["--ground"])
    for i, k in enumerate(keys):
        x = PAD + i * (W + GAP)
        v = resolve(t, THEMES[t][k])
        fill = over(resolve(t, THEMES[t]["--ink"]), g) if v == "currentColor" else over(v, g)
        d.rectangle([x, PAD, x + W, PAD + H], fill=fill, outline=(200, 200, 200))
        d.text((x, PAD + H + 8), k[2:], font=FB, fill=(17, 17, 17))
        d.text((x, PAD + H + 30), "= text colour" if v == "currentColor" else hx(fill), font=F, fill=(90, 90, 90))
    path = f"{OUT_IMG}/swatch-{t}.png"
    img.save(path)
    return path


# ---------------------------------------------------------------- contrast pairs
def pairs(t):
    T = lambda k: resolve(t, THEMES[t][k])
    G, G2 = T("--ground"), T("--ground-2")
    P = [("Body text, headings", "--ink", "ground", T("--ink"), G, 17),
         ("Body text in Snippets / Contact", "--ink", "ground-2", T("--ink"), G2, 17),
         ("Labels, captions, footer (11px)", "--ink-muted", "ground", T("--ink-muted"), G, 11),
         ("Labels in Snippets / Contact (11px)", "--ink-muted", "ground-2", T("--ink-muted"), G2, 11),
         ("Index numbers, lock marker (11–14px)", "--accent-2", "ground", T("--accent-2"), G, 11),
         ("Active chapter (14px)" + (", links, current nav" if t == "venues" else ""), "--accent", "ground", T("--accent"), G, 14),
         ("Enter button text (14px)", "--on-accent", "accent", T("--on-accent"), T("--accent"), 14)]
    if t == "venues":
        P.append(("Contact links (17px) on Contact ground", "--accent", "ground-2", T("--accent"), G2, 17))
        for r, d in ROOMS.items():
            P.append((f"{ROOM_NAME[r]}: chapter numbers, FIG. numbers, active chapter", "--room", "ground",
                      resolve(t, d["--room"]), G, 11))
    return P


def nontext(t):
    T = lambda k: resolve(t, THEMES[t][k])
    G = T("--ground")
    return [("Hairline rules", "--hairline", T("--hairline"), G), ("Placeholder border", "--ink-low", T("--ink-low"), G)]


md = ["# Themes: colour comparison (prototype only)", "",
      "Nine palettes for the same pages. **The three colour directions to choose from: Archive, Salon and Campus** (COLOUR-DIRECTIONS.md). **Mono** is the uncoloured build; Cream, Cream bold, Venues, Venues bold and Heritage rich are earlier rounds, kept for reference. "
      "**Only colour changes:** type, spacing, images, copy and layout are the same in all five. Checked: every page has the same height in every theme at 1440 and 390, "
      "and mono renders as the round-5 build (a pixel comparison shows only sub-pixel anti-aliasing shifts in a few figure captions, where the FIG. number "
      "now has its own span, plus frames of animated media).",
      "Squarespace will get **one** palette at the end, set in Site Styles (see SQUARESPACE-BUILD-NOTES.md, *Site Styles per theme*).", "",
      "- **Switcher:** top-right corner of every prototype page (ARCHIVE · SALON · CAMPUS · MONO, and EARLIER for the previous rounds). The choice is remembered while navigating "
      "(localStorage, plus `?theme=` on internal links so it also works where storage is blocked). Any page can be opened in a theme directly, e.g. `index.html?theme=venues-bold`.",
      "- **How it works:** every colour in `site/assets/css/r3.css` is a variable; `data-theme` on `<html>` swaps the set, and in the bold themes each coloured section "
      "re-sets the text, rule and link variables for its own ground. This file is generated by `tools/build_themes.py` from the stylesheet.",
      "- **Comparison sheet:** `screenshots/theme-compare.png`, five columns: the whole homepage, project row 01 hovered, the Room 01 header with chapter 02 active, the password page.",
      "- **Contrast, two ways:** (1) the tables below compute every text/ground pair from the CSS values; (2) a rendered audit (`tools/contrast_audit.js`, results in "
      "`content/contrast-audit.json`) measures **every piece of text on every page, in every theme, at 1440 and 390** against the pixels actually behind it, "
      "which is the only honest check for text on tinted photos. Rule: 4.5:1, or 3:1 for text 24px and larger. Summary at the end.", ""]

for t in ("mono", "cream", "venues"):
    md += [f"## {NAMES[t]}", "", f"![{t} swatches]({swatches(t)})", "",
           "| Variable | Value | On ground | Where it's used |", "|---|---|---|---|"]
    for k in VARS:
        v, solid = shown(t, k)
        md.append(f"| `{k}` | `{v}` | {('`' + solid + '`') if solid else '—'} | {where(t, k)} |")
    md += ["", "**Contrast (text)**", "", "| Pair | Text | Ground | Ratio | Needs | Result |", "|---|---|---|---|---|---|"]
    for name, fk, gk, fg, bg, px in pairs(t):
        r = ratio(fg, bg)
        need = 3.0 if px >= 24 else 4.5
        md.append(f"| {name} | `{fk}` {hx(over(fg, bg))} | `{gk}` {hx(rgba(bg)[:3])} | **{r:.2f}:1** | {need}:1 | {'pass' if r >= need else '**FAIL**'} |")
        assert r >= need, (t, name, r)
    md += ["", "Non-text (decorative, informative only; never carries meaning): " +
           "; ".join(f"{n} `{k}` {hx(over(fg, bg))} = {ratio(fg, bg):.2f}:1" for n, k, fg, bg in nontext(t)) + ".", ""]
    if t == "cream":
        md += ["Wine `#8C2F1E` appears only on: section index numbers, the PASSWORD PROTECTED marker, link underlines (and the current nav item's underline), "
               "the active chapter in the index, and the Enter button fill. It is never a large fill: the Enter button (~88×44px) is the largest wine area.", ""]
    if t == "venues":
        md += ["**The five venue colours.** Sampled from the business card (`references/business-card.png`) and refined to web values. "
               "Each has a **fill** value (the card colour, used for the stripe and the tile-hover tints, never for text) and, where it is used for text, "
               "a darker **text-safe** value that passes 4.5:1:", "",
               "| Venue | Fill (stripe) | Text-safe | Used for |", "|---|---|---|---|"]
        V = THEMES["venues"]
        for name, f, tx, use in [("Orange (Henry Ford Museum)", "--v-orange", "--t-orange", "Project numbers, lock marker; Room 02 marks"),
                                 ("Olive (Greenfield Village)", "--v-olive", "--t-olive", "Stripe; Room 01 marks; Room 01 tile hover"),
                                 ("Red (Ford Rouge Factory Tour)", "--v-red", "--t-red", "Stripe; Room 04 marks; Room 04 tile hover"),
                                 ("Light blue (Benson Ford Research Center)", "--v-blue", "--t-blue", "Links, active states, Enter button; Room 03 marks"),
                                 ("Navy (Henry Ford Academy)", "--v-navy", "--ink", "Ink: all text, rules")]:
            md.append(f"| {name} | `{V[f]}` | `{resolve('venues', V[tx])}` | {use} |")
        md += ["", "**Per-room colour** (case-study pages only; small elements: chapter numbers, chapter-index numbers, FIG. numbers, the active chapter). "
               "Headers stay on the light ground. Each project's logo tile hovers to a pale tint of its room colour:", "",
               "| Room | Text colour | Tile hover tint |", "|---|---|---|"]
        for r, d in ROOMS.items():
            md.append(f"| {ROOM_NAME[r]} | `{resolve('venues', d['--room'])}` | `{d['--room-tint']}` |")
        md += ["", "**Signature stripe:** one 4px rule in five equal segments (orange · olive · red · light blue · navy, fill values). On the homepage it appears "
               "exactly twice: under the hero (replacing the full-width hairline there) and above the footer (replacing the footer rule, at the content width). "
               "Other pages have no hero, so they show only the footer stripe. It overlays the rule it replaces and takes no space.",
               "No coloured section backgrounds, headings or bands. Logos stay in colour on the secondary ground.", "",
               "**Deviation from the brief:** muted ink is **75%** of navy, not 64%. At 64% it measures 3.79:1 on `#FAFAF8` and 3.65:1 on `#F1F1EC` (fails 4.5:1 at 11px); "
               "75% gives 5.06:1 and 4.81:1. Low ink stays at 45% and is used for non-text only.", ""]

# ---------------------------------------------------------------- bold themes
def rules_for(theme):
    """(selector, declarations) for every rule scoped to one bold theme."""
    out = []
    for m in re.finditer(r'([^{}]*\[data-theme="' + theme + r'"\][^{}]*)\{([^}]*)\}', CSS):
        d = dict((k.strip(), v.strip()) for k, v in (q.split(":", 1) for q in m.group(2).split(";") if ":" in q))
        out.append((m.group(1).strip(), d))
    return out


def audit_worst(theme, region=None, page=None):
    xs = [x for x in AUDIT if x["theme"] == theme and (region is None or x["region"] == region) and (page is None or x["page"] == page)]
    if not xs:
        return None
    w = min(xs, key=lambda x: x["p5"] / x["need"])
    return w, len(xs), all(x["pass"] for x in xs)


def fmt_audit(theme, region, page=None):
    r = audit_worst(theme, region, page)
    if not r:
        return "—"
    w, n, ok = r
    return f"worst **{w['p5']:.2f}:1** (needs {w['need']}:1), {n} items, {'all pass' if ok else '**FAILS**'}"


SECTION_NAME = {"#snippets": "Snippets About My Life (statement + slideshow; the brief's \"Beyond The Work\")", "#contact": "Contact",
                "#projects": "Projects (homepage)", ".foot": "Footer", ".lock": "Password page ground"}
REGION_OF = {"#snippets": "#snippets", "#contact": "#contact", "#projects": "#projects", ".foot": ".foot", ".lock": ".lock"}


def surfaces(theme):
    T = THEMES[theme]
    res = []
    for sel, d in rules_for(theme):
        if "--s" not in d:
            continue
        targets = re.findall(r"(#[\w-]+|\.[\w-]+)", sel.split("]", 1)[1])
        g, ink, rule = (resolve(theme, d[k], d) for k in ("--s", "--s-ink", "--s-rule"))
        link = resolve(theme, d.get("--s-link", d["--s-ink"]), d)
        for tg in targets:
            res.append((tg, g, ink, rule, link))
    order = ["#snippets", "#projects", "#contact", ".foot", ".lock"]
    return sorted(res, key=lambda r: order.index(r[0]))


def swatch_list(t, items):
    W, H, PAD, GAP = 150, 84, 24, 12
    img = Image.new("RGB", (PAD * 2 + len(items) * (W + GAP) - GAP, PAD * 2 + H + 54), (255, 255, 255))
    d = ImageDraw.Draw(img)
    for i, (label, c) in enumerate(items):
        x = PAD + i * (W + GAP)
        d.rectangle([x, PAD, x + W, PAD + H], fill=rgba(c)[:3], outline=(200, 200, 200))
        d.text((x, PAD + H + 8), label, font=FB, fill=(17, 17, 17))
        d.text((x, PAD + H + 30), c.upper(), font=F, fill=(90, 90, 90))
    path = f"{OUT_IMG}/swatch-{t}.png"
    img.save(path)
    return path


def bold(theme):
    T = THEMES[theme]
    R = dict(rules_for(theme))
    out = [f"## {NAMES[theme]}", ""]
    if theme == "cream-bold":
        sw = [("ground", T["--ground"]), ("ground-2", T["--ground-2"]), ("ink", T["--c-ink"]), ("wine", T["--wine"]), ("cream text", T["--cream"])]
        out += [f"![{theme} swatches]({swatch_list(theme, sw)})", "",
                "Cream and wine with colour as **sections**. The base values (ground, ink, muted ink, hairlines, wine on small marks, logo tiles) are **Cream**'s, above; "
                "the sections below take their own ground, and on those grounds all text is cream or ink, never a third colour.", ""]
    else:
        sw = [("white ground", T["--ground"]), ("orange", T["--b-orange"]), ("olive", T["--b-olive"]), ("red", T["--b-red"]),
              ("light blue", T["--b-blue"]), ("navy", T["--b-navy"])]
        out += [f"![{theme} swatches]({swatch_list(theme, sw)})", "",
                "The business card's five colours as **section grounds**. The base values are **Venues**' (above), except the page ground, which is white `#FFFFFF`. "
                "On a coloured ground text is white or navy, whichever passes 4.5:1 (never a third colour). That rule decides the **ground values** too: "
                "the card's light blue `#6E94AB` and olive `#8A8D4F` pass with neither white nor navy (3.2–3.5:1), so as grounds they are refined to "
                f"light blue `{T['--b-blue']}` (navy text, {ratio(T['--b-navy'], T['--b-blue']):.2f}:1) and olive `{T['--b-olive']}` (white text, {ratio('#FFFFFF', T['--b-olive']):.2f}:1). "
                f"Orange `{T['--b-orange']}` and red `{T['--b-red']}` are the card values (orange takes navy text, {ratio(T['--b-navy'], T['--b-orange']):.2f}:1; "
                f"red takes white, {ratio('#FFFFFF', T['--b-red']):.2f}:1). The stripe keeps the card values.", ""]
    out += ["**Sections**", "", "| Section | Ground | Text | Rules · link underline | Text on ground | Rendered audit |", "|---|---|---|---|---|---|"]
    for tg, g, ink, rule, link in surfaces(theme):
        r = ratio(ink, g)
        assert r >= 4.5, (theme, tg, r)
        out.append(f"| {SECTION_NAME[tg]} | `{g}` | `{ink}` | `{rule}` · `{link}` | **{r:.2f}:1** | {fmt_audit(theme, REGION_OF[tg])} |")
    if theme == "cream-bold":
        out += ["| Hero, Projects, chapters, footer | `#F3F0EA` (cream) | `#16140F` | as Cream | 16.18:1 | " + fmt_audit(theme, ".hero") + " (hero) |",
                "| Project rows | alternate `#F3F0EA` / `#E9E4DB`, full-bleed; the logo tile takes the other ground | `#16140F` | as Cream | 14.53:1 on `#E9E4DB` | " + fmt_audit(theme, "#projects") + " |",
                "| Reflection | `#E9E4DB` | `#16140F` | as Cream | 14.53:1 | " + fmt_audit(theme, ".reflection-sec") + " |"]
        out += ["", "Inside the wine Snippets section the slideshow sits on a **12px cream frame** (drawn inside the frame's box, so the slideshow keeps its size). "
                "The slideshow arrows stay ink on their white chips.", ""]
    else:
        out += ["| Hero, chapters, case pages | `#FFFFFF` | `#1E3F63` | as Venues | 10.79:1 | " + fmt_audit(theme, ".hero") + " (hero) |",
                "| Snippets About My Life (statement + slideshow) | `#F1F1EC` (secondary ground) | `#1E3F63` | as Venues | 9.52:1 | " + fmt_audit(theme, "#snippets") + " |"]
        out += ["", "Logo tiles in the navy Projects section are white `#FFFFFF`; on hover each takes its room's pale tint (as in Venues). "
                "Contact links are navy text with a **white underline** (decoration only, not text).", ""]
    # panels
    out += ["**Discipline panels** (all four panels have a photo in this build, so every panel is its photo under a flat colour layer)", "",
            "| Panel | Layer over the photo | Text | Hover | Rendered audit (text on the actual photo) |", "|---|---|---|---|---|"]
    names = ["01 Interactive Exhibit Design", "02 UX (User Experience) Design", "03 UX Research", "04 Digital Marketing"]
    for i in range(4):
        if theme == "cream-bold":
            d = R['[data-theme="cream-bold"] .panels']
            tint, ink, hov = d["--tint"], resolve(theme, d["--p-ink"], d), "layer to 80% of itself (lighter), as mono lightens"
        else:
            d = R[f'[data-theme="venues-bold"] .panel:nth-child({i + 1})']
            tint, ink, hov = d["--tint"] + " over the photo at brightness .55", resolve(theme, d["--p-ink"], d), "layer 10% darker"
        out.append(f"| {names[i]} | `{tint}` | `{ink}` | {hov} | {fmt_audit(theme, f'panel {i + 1}')} |")
    # case headers
    out += ["", "**Case-study headers.** A full-width band behind the title: on the photo covers (Rooms 01, 02) the band is the cover's overlay; "
            "on the document headers (Rooms 03, 04) it is the header's ground, and the meta table sits on a card of the page ground (drawn behind it, so nothing moves). "
            "On phones, where the cover title sits below the photo, the band goes behind the title. Chapters stay on the page ground.", "",
            "| Room | Band | Over the cover photo | Title & nav | Title on flat band | Rendered audit: cover / header |", "|---|---|---|---|---|---|"]
    rooms = [("room01", "room-01-jackson-home"), ("room02", "room-02-power-energy"), ("room03", "room-03-rhode-island"), ("room04", "room-04-littelfuse")]
    for r, pg in rooms:
        if theme == "cream-bold":
            d = R['[data-theme="cream-bold"] body.case']
        else:
            d = R[f'[data-theme="venues-bold"] body.{r}']
        band, band_a, bink = resolve(theme, d["--band"], d), d["--band-a"], resolve(theme, d["--band-ink"], d)
        reg = ".cover" if r in ("room01", "room02") else ".dochead"
        extra = ""
        out.append(f"| {ROOM_NAME[r].split(' · ')[0]} | `{band}` | `{band_a}` | `{bink}`{extra} | {ratio(bink, band):.2f}:1 | "
                   f"{fmt_audit(theme, reg, pg)}; nav {fmt_audit(theme, '.bar', pg).split(',')[0]} |")
    if theme == "venues-bold":
        out += ["", "Room 02's title and nav are **navy**, not white: white on orange is 2.13:1, navy 5.06:1. Rooms 03's title is navy for the same reason "
                f"(white on light blue `{T['--b-blue']}` is {ratio('#FFFFFF', T['--b-blue']):.2f}:1).", "",
                "| Room | Reflection ground (12% of the room colour on white) | Navy text on it |", "|---|---|---|"]
        for r, pg in rooms:
            d = R[f'[data-theme="venues-bold"] body.{r}']
            out.append(f"| {ROOM_NAME[r]} | `{d['--refl']}` | {ratio(T['--b-navy'], d['--refl']):.2f}:1 |")
    # password page
    lock = [x for x in surfaces(theme) if x[0] == ".lock"][0]
    card_ink = T.get("--c-ink", T.get("--b-navy"))
    out += ["", f"**Password page:** ground `{lock[1]}`, name and footer in `{lock[2]}` ({ratio(lock[2], lock[1]):.2f}:1); the form on a card of the page ground "
            f"`{T['--ground']}` (drawn behind the form, so nothing moves) with `{card_ink}` text ({ratio(card_ink, T['--ground']):.2f}:1); Enter button "
            f"`{resolve(theme, T['--accent'])}` with white text ({ratio('#FFFFFF', resolve(theme, T['--accent'])):.2f}:1). Rendered audit, card: {fmt_audit(theme, '.lock__box')}.", ""]
    if theme == "venues-bold":
        out += ["**Signature stripe:** kept under the hero and above the footer, drawn as five flat segments (no gradient). Above the navy footer it sits on the "
                "section before it (white on case pages and Projects), so all five segments show; on the homepage that section is orange, so there it sits on the "
                "footer's top edge and its navy segment runs into the footer.", ""]
    return out


md += ["## Bold themes: where the brief and the build differ", "",
       "The bold brief describes the homepage as hero → Four disciplines → statement → Projects → Beyond The Work → Contact. In this build the order is "
       "**hero → Snippets About My Life (the statement and the slideshow, one section) → Four disciplines (panels) → Projects → Contact → footer**, and the layout "
       "is fixed. With the rule *no two adjacent sections share a colour*, a few assignments had to move. Each change is the smallest one that keeps every rule:", "",
       "- **Cream bold, panels:** the brief's wine panels would sit directly under the wine Snippets section. They take **ink** at 60% over the photos instead "
       "(cream text). Wine stays on Snippets (the brief's full-bleed wine \"Beyond The Work\" with the slideshow on a cream frame).",
       "- **Venues bold, Snippets:** the statement and the slideshow share one section, so it can't be both white (statement) and light blue (Beyond The Work). "
       "It is the light secondary ground `#F1F1EC`: the statement is on (near) white, and it isn't white beside the white hero.",
       "- **Venues bold, panels:** every panel touches both Snippets and the navy Projects section, so no panel can be navy. The panels run **orange · olive · red · "
       "light blue**, and with navy Projects below they complete the card's five bands in the card's own order. This uses red, which the brief skipped here.",
       "- **All four panels have photos** in this build (the brief expected one). Every panel is therefore its photo under the colour layer.",
       "- **Venues bold, light grounds:** text on orange (Contact, Room 02) and light blue (Room 03) is navy, not white, because white fails there "
       "(\"use white or ink, whichever passes\" wins over \"white title\").",
       "- **Case headers:** on Rooms 03 and 04 the meta table is beside the title, not below it, so it sits on a page-ground card inside the band.", ""]
for t in ("cream-bold", "venues-bold"):
    md += bold(t)


# ---------------------------------------------------------------- heritage themes
def heritage():
    T = THEMES["heritage"]
    R = lambda k: resolve("heritage", T[k])
    G, G2, INK = R("--ground"), R("--ground-2"), R("--ink")
    CONTACT = block(':is([data-theme="heritage"],[data-theme="heritage-rich"],[data-theme="salon"],[data-theme="campus"]) #contact')
    RICH = block('[data-theme="heritage-rich"] #snippets')
    navy, olive, cream = CONTACT["background"], RICH["background"], CONTACT["color"]
    out = ["## Archive (the `heritage` theme) and Heritage rich", "",
           f"![heritage swatches]({swatch_list('heritage', [('paper', G), ('paper 2', G2), ('ink', INK), ('wine', R('--accent')), ('navy band', navy), ('olive band', olive)])})", "",
           f"![venue colours]({swatch_list('heritage-venues', [('orange', T['--v-orange']), ('olive', T['--v-olive']), ('red', T['--v-red']), ('light blue', T['--v-blue']), ('navy', T['--v-navy'])])})", "",
           "The ChatGPT mockup's direction (cream paper, navy, olive, the card colours), kept to the site's layout and copy and made quieter. "
           "Archive is one of the three colour directions; the reasoning, the section-by-section map and what was kept and dropped from the mockup are in **COLOUR-DIRECTIONS.md**.", "",
           "**Roles (60 / 30 / 10).** Paper carries the page. Navy ink carries the type, and one navy band (Contact). **Wine is Yasmin's accent**: her name, "
           "link underlines, \"Password protected\", the active chapter, the Enter button. **The card colours are wayfinding only**: each project keeps its venue "
           "colour (a 3px bar beside its row, its number, its case-study marks), and one five-colour rule sits over the project list as their legend. "
           "Heritage rich adds one olive band (Snippets About My Life). No gradients, textures, shapes or coloured header/footer bars.", "",
           "| Token | Value | Where it's used |", "|---|---|---|",
           f"| paper | `{G}` | Page ground, header, footer, chapters |",
           f"| paper 2 | `{G2}` | Snippets (Heritage), Reflection, logo tiles |",
           f"| ink | `{INK}` | All type, rules, outline button (a navy-black, so the navy band belongs) |",
           f"| ink muted | `{R('--ink-muted')}` | Labels, captions |",
           f"| wine | `{R('--accent')}` | Yasmin's accent: \"Yasmin.\", link underlines, lock marker, Enter button |",
           f"| navy band | `{navy}` | Contact (cream text; links underlined in the card orange) |",
           f"| olive band | `{olive}` | Snippets, Heritage rich only (cream text) |",
           f"| venue fills | `{T['--v-orange']}` `{T['--v-olive']}` `{T['--v-red']}` `{T['--v-blue']}` `{T['--v-navy']}` | Row bars, the five-colour rule, tile hovers (never text) |",
           f"| venue text | olive `{T['--h-olive']}`, orange `{T['--h-orange']}`, light blue `{T['--h-blue']}`, red `{T['--h-red']}` | Project numbers, case-study chapter and FIG. numbers |",
           "", "**Project colours** (same logic as Venues): Room 01 olive (Jackson Home is in Greenfield Village), Room 02 orange (Power & Energy is in the Henry Ford Museum), "
           "Room 03 light blue (research), Room 04 red (engineering, the Rouge factory).", "",
           "**Contrast (text)**", "", "| Pair | Text | Ground | Ratio | Result |", "|---|---|---|---|---|"]
    pairs = [("Body text, headings", INK, G), ("Text on paper 2", INK, G2), ("Labels, captions", R("--ink-muted"), G), ("Labels on paper 2", R("--ink-muted"), G2),
             ("Wine marks, \"Yasmin.\"", R("--accent"), G), ("Enter button text", "#FFFFFF", R("--accent")), ("Contact text", cream, navy), ("Snippets text (rich)", cream, olive)]
    for k in ("--h-olive", "--h-orange", "--h-blue", "--h-red"):
        pairs += [(f"Venue text {k[4:]} on paper", R(k), G), (f"Venue text {k[4:]} on paper 2", R(k), G2)]
    for name, fg, bg in pairs:
        r = ratio(fg, bg)
        assert r >= 4.5, (name, r)
        out.append(f"| {name} | {hx(over(fg, bg))} | {hx(rgba(bg)[:3])} | **{r:.2f}:1** | pass |")
    out += ["", "Text on photographs (discipline panels, case-study covers) sits on a 60% navy-ink layer; the rendered audit measures it against the actual photos: "
            f"Heritage {fmt_audit('heritage', None)}; Heritage rich {fmt_audit('heritage-rich', None)}.", ""]
    return out


def directions():
    out = ["## Salon and Campus (the other two colour directions)", "",
           "Same constant layer as Archive (paper, wine for \"Yasmin.\", project colours as wayfinding). Section-by-section map: COLOUR-DIRECTIONS.md; "
           "visual guide: `screenshots/colour-directions.png`.", "",
           f"![salon swatches]({swatch_list('salon', [('paper', '#F3F0EA'), ('paper 2', '#E9E4DB'), ('warm ink', '#16140F'), ('wine', '#8C2F1E'), ('cream on wine', '#F3F0EA')])})", "",
           f"![campus swatches]({swatch_list('campus', [('orange tint', '#F1E4D3'), ('olive tint', '#E2E0D1'), ('olive row', '#E6E4D7'), ('orange row', '#F2E7D9'), ('blue row', '#E3E5E2'), ('red row', '#EBDCD6'), ('ink', '#1C2635'), ('navy', '#1E3F63')])})", "",
           "**Contrast (text)**", "", "| Direction | Pair | Text | Ground | Ratio |", "|---|---|---|---|---|"]
    WI, P, P2, INK, NAVY, WINE = "#16140F", "#F3F0EA", "#E9E4DB", "#1C2635", "#1E3F63", "#8C2F1E"
    pairs = [("Salon", "Body text", WI, P), ("Salon", "Muted labels on paper 2", "rgba(22,20,15,.64)", P2), ("Salon", "Cream on wine (Snippets, Reflection, lock)", P, WINE),
             ("Salon", "Wine \"Yasmin.\"", WINE, P), ("Campus", "Ink on the orange tint (hero)", INK, "#F1E4D3"), ("Campus", "Muted labels on the olive tint", "rgba(28,38,53,.68)", "#E2E0D1"),
             ("Campus", "Olive number on its row", "#63653A", "#E6E4D7"), ("Campus", "Orange number on its row", "#8E5412", "#F2E7D9"), ("Campus", "Blue number on its row", "#48677A", "#E3E5E2"),
             ("Campus", "Red number on its row (a shade deeper)", "#983A35", "#EBDCD6"), ("Campus", "Muted labels on the red row", "rgba(28,38,53,.68)", "#EBDCD6"),
             ("Campus", "Enter: white on navy", "#FFFFFF", NAVY), ("Campus", "Ink on the lock tint", INK, "#DEE1E0")]
    for d, name, fg, bg in pairs:
        r = ratio(fg, bg)
        assert r >= 4.5, (d, name, r)
        out.append(f"| {d} | {name} | {hx(over(fg, bg))} | {hx(rgba(bg)[:3])} | **{r:.2f}:1** |")
    out += ["", f"Rendered audit (every text item, text on photos and tints included): Salon {fmt_audit('salon', None)}; Campus {fmt_audit('campus', None)}.", ""]
    return out


md += heritage()
md += directions()

# ---------------------------------------------------------------- rendered audit summary
md += ["## Rendered contrast audit (all themes)", "",
       "Every visible piece of text on the seven prototype pages, in every theme, at 1440 and 390, measured against the rendered pixels behind it "
       "(text hidden, nothing moved; 95% of the background under each line must pass). Hover states are not covered. Re-run: "
       "`node tools/contrast_audit.js > content/contrast-audit.json` (and `WIDTH=390`).", "",
       "| Theme | Width | Text items | Pass | Fail | Closest to its limit |", "|---|---|---|---|---|---|"]
for t in THEMES:
    for w in (1440, 390):
        xs = [x for x in AUDIT if x["theme"] == t and x["width"] == w]
        if not xs:
            continue
        lo = min(xs, key=lambda x: x["p5"] / x["need"])
        md.append(f"| {NAMES[t].split(' (')[0]} | {w} | {len(xs)} | {sum(x['pass'] for x in xs)} | {sum(not x['pass'] for x in xs)} | "
                  f"{lo['p5']:.2f}:1 ({lo['region']}, needs {lo['need']}) |")
fails = [x for x in AUDIT if not x["pass"]]
bold_items = [x for x in AUDIT if x["theme"].endswith("-bold")]
lo = min(bold_items, key=lambda x: x["p5"])
md += ["", f"In both bold themes **every** text item passes **4.5:1**, large text included (lowest: {lo['p5']:.2f}:1, {lo['region']} on {lo['page']} at {lo['width']}, {lo['theme']}).", ""]
if fails:
    md += ["**Failures:**", ""]
    for (reg, text, sel), group in collections.OrderedDict(((x["region"], x["text"], x["sel"]), None) for x in fails).items():
        g = [x for x in fails if (x["region"], x["text"], x["sel"]) == (reg, text, sel)]
        md.append(f"- \"{text}\" ({reg}, {g[0]['page']}): {', '.join(sorted(set(x['theme'] + ' @' + str(x['width']) + ' ' + format(x['p5'], '.2f') + ':1' for x in g)))} (needs {g[0]['need']}:1).")
    md += ["", "These are all the panel number \"04\" (13px, white at 85%) over the fourth discipline photo, under the built 45% black layer. It is in the **built** "
           "palette (mono) and in Cream and Venues, which keep the built panels; the earlier pair-only check could not see it because it is text on a photo. "
           "Fix when the palette is chosen: the number at full white, or the layer at 50% on that panel. Both bold themes pass everywhere.", ""]

# venues signature stripe as an image, so Squarespace can place it with a native Image block (no CSS)
V = THEMES["venues"]
stripe = Image.new("RGB", (2400, 8))
for i, k in enumerate(("--v-orange", "--v-olive", "--v-red", "--v-blue", "--v-navy")):
    stripe.paste(rgba(V[k])[:3], (i * 480, 0, (i + 1) * 480, 8))
stripe.save("site/assets/img/stripe-venues.png")
open("THEMES.md", "w").write("\n".join(md))
print("THEMES.md written;", ", ".join(f"swatch-{t}.png" for t in THEMES))
