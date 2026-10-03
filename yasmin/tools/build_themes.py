"""Theme comparison (prototype only): THEMES.md and the swatch rows, read from site/assets/css/r3.css.

Run from yasmin/:  python3 tools/build_themes.py
Every value comes from the stylesheet (:root = mono, [data-theme="cream"], [data-theme="venues"],
and the venues per-room blocks), so the document can't drift from what the prototype shows.
Contrast is WCAG 2.x relative luminance; translucent colours are composited over the ground they sit on.
"""
import os, re
from PIL import Image, ImageDraw, ImageFont

CSS = re.sub(r"/\*.*?\*/", "", open("site/assets/css/r3.css").read(), flags=re.S)
OUT_IMG = "screenshots/themes"
os.makedirs(OUT_IMG, exist_ok=True)


def block(sel):
    m = re.search(re.escape(sel) + r"\s*\{([^}]*)\}", CSS)
    return dict((k.strip(), v.strip()) for k, v in (p.split(":", 1) for p in m.group(1).split(";") if ":" in p))


ROOT = block(":root")
THEMES = {"mono": ROOT, "cream": {**ROOT, **block('[data-theme="cream"]')}, "venues": {**ROOT, **block('[data-theme="venues"]')}}
ROOMS = {r: block(f'[data-theme="venues"] .{r}') for r in ("room01", "room02", "room03", "room04")}
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
NAMES = {"mono": "Mono (current build, baseline)", "cream": "Cream", "venues": "Venues"}


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
      "Three palettes for the same pages, so the client can choose. **Only colour changes:** type, spacing, images, copy and layout are identical in all three "
      "(checked: mono screenshots are pixel-identical to the round-5 build; cream and venues pages have the same heights).",
      "Squarespace will get **one** palette at the end, set in Site Styles (see SQUARESPACE-BUILD-NOTES.md, *Site Styles per theme*).", "",
      "- **Switcher:** top-right corner of every prototype page (MONO · CREAM · VENUES). The choice is remembered while navigating "
      "(localStorage, plus `?theme=` on internal links so it also works where storage is blocked). Any page can be opened in a theme directly, e.g. `index.html?theme=venues`.",
      "- **How it works:** every colour in `site/assets/css/r3.css` is a variable; `data-theme` on `<html>` swaps the set. Generated by `tools/build_themes.py` from the stylesheet.",
      "- **Comparison sheet:** `screenshots/theme-compare.png` (homepage, project row 01 hovered, Room 01 header with chapter 02 active, password page, footer).",
      "- **Rule checked:** every text/ground pair ≥ 4.5:1 (all text on the site that changes colour is under 24px, so 4.5:1 applies throughout; headings are ink).", ""]

for t in THEMES:
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

# venues signature stripe as an image, so Squarespace can place it with a native Image block (no CSS)
V = THEMES["venues"]
stripe = Image.new("RGB", (2400, 8))
for i, k in enumerate(("--v-orange", "--v-olive", "--v-red", "--v-blue", "--v-navy")):
    stripe.paste(rgba(V[k])[:3], (i * 480, 0, (i + 1) * 480, 8))
stripe.save("site/assets/img/stripe-venues.png")
open("THEMES.md", "w").write("\n".join(md))
print("THEMES.md written;", ", ".join(f"swatch-{t}.png" for t in THEMES))
