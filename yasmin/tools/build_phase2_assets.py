"""Phase 2 image exports (run from yasmin/):  python3 tools/build_phase2_assets.py

Snippets (media/snippets/ -> site/assets/img/snippets/snippet-NN.jpg)
  Squarespace's Gallery "Slideshow: Simple" fills its frame (it crops to the aspect ratio).
  So, as uploaded to Squarespace:
    - portrait photos (3:4) go up as they are; the 4:5 frame trims about 6% top and bottom;
    - landscape photos are letterboxed here onto a 4:5 canvas of the light ground #F4F3F0,
      so the slideshow shows them whole, never cropped.
  Web size: 1600px on the long side.

Logos (media/logos/ -> site/assets/img/logos/)
  (a) colour, as supplied:   the-henry-ford.png, itc.png (upscaled x3), and the two SVGs with
                              their white background shapes removed (so the tile ground shows).
  (b) ink #111111:           Rhode Island and Littelfuse SVGs recoloured; The Henry Ford as
                              lettering only (the orange square removed); ITC thresholded to a
                              clean single-colour mark and upscaled.
  Squarespace plates:        transparent 3:2 PNGs (1200x800) with the logo optically sized and
                              centred and a 121px margin (= 32px at the 316px homepage tile).
  logos/sizes.json           the optical size of each logo inside the tile's padded box.
"""
import json, os, re, subprocess
import numpy as np
from PIL import Image, ImageOps, ImageFilter

Image.MAX_IMAGE_PIXELS = None
GROUND = (244, 243, 240)
INK = (17, 17, 17)
SN_SRC, SN_OUT = "media/snippets", "site/assets/img/snippets"
LG_SRC, LG_OUT = "media/logos", "site/assets/img/logos"
os.makedirs(SN_OUT, exist_ok=True)
os.makedirs(LG_OUT, exist_ok=True)

# ------------------------------------------------------------------ snippets
for f in sorted(os.listdir(SN_SRC)):
    n = int(f[8:10])
    im = ImageOps.exif_transpose(Image.open(f"{SN_SRC}/{f}")).convert("RGB")
    if im.height >= im.width:                                   # portrait: as is, 1600 tall
        im = im.resize((round(im.width * 1600 / im.height), 1600), Image.LANCZOS)
        out = im
    else:                                                       # landscape: whole, on a 4:5 ground
        W, H = 1280, 1600
        s = W / im.width
        im = im.resize((W, round(im.height * s)), Image.LANCZOS)
        out = Image.new("RGB", (W, H), GROUND)
        out.paste(im, (0, (H - im.height) // 2))
    out.save(f"{SN_OUT}/snippet-{n:02d}.jpg", quality=82, optimize=True, progressive=True)
print("snippets:", len(os.listdir(SN_OUT)))

# ------------------------------------------------------------------ logos: files
def clean_svg(src, dst, drop_classes, recolour=None):
    s = open(src).read()
    for c in drop_classes:                      # remove the white background shape(s)
        s = re.sub(rf'<path class="{c}"[^>]*/>\s*', "", s)
    if recolour:
        s = re.sub(r"fill:\s*#[0-9a-fA-F]{3,6}", f"fill: {recolour}", s)
    open(dst, "w").write(s)


clean_svg(f"{LG_SRC}/rhode-island-doh.svg", f"{LG_OUT}/rhode-island-doh.svg", ["st1"])
clean_svg(f"{LG_SRC}/rhode-island-doh.svg", f"{LG_OUT}/rhode-island-doh-ink.svg", ["st1"], "#111111")
clean_svg(f"{LG_SRC}/littelfuse.svg", f"{LG_OUT}/littelfuse.svg", ["st0"])
clean_svg(f"{LG_SRC}/littelfuse.svg", f"{LG_OUT}/littelfuse-ink.svg", ["st0"], "#111111")

def crop_viewbox(path):
    """Tighten the viewBox to the artwork, so the file's own proportions are the logo's (no empty square)."""
    svg = open(path).read()
    vb = [float(x) for x in re.search(r'viewBox="([^"]+)"', svg).group(1).split()]
    tmp = f"/tmp/p2_vb_{os.path.basename(path)}.png"
    subprocess.run(["node", "tools/svg_to_png.js", path, tmp, "2000"], check=True)
    x0, y0, x1, y1 = Image.open(tmp).getbbox()
    k = vb[2] / 2000
    pad = 2
    nb = [vb[0] + x0 * k - pad, vb[1] + y0 * k - pad, (x1 - x0) * k + 2 * pad, (y1 - y0) * k + 2 * pad]
    svg = re.sub(r'viewBox="[^"]+"', 'viewBox="%s"' % " ".join(f"{v:.1f}" for v in nb), svg, count=1)
    open(path, "w").write(svg)


for f in ("rhode-island-doh.svg", "rhode-island-doh-ink.svg", "littelfuse.svg", "littelfuse-ink.svg"):
    crop_viewbox(f"{LG_OUT}/{f}")

# The Henry Ford: colour as supplied; ink = lettering only (white letters -> ink, orange square removed)
thf = Image.open(f"{LG_SRC}/the-henry-ford.png").convert("RGBA")
thf.save(f"{LG_OUT}/the-henry-ford.png")
a = np.asarray(thf).astype(float)
blue = a[..., 2]                                   # orange ~ B 32, white letters ~ B 255
letters = np.clip((blue - 60) / (235 - 60), 0, 1) * (a[..., 3] / 255)
big = Image.fromarray((letters * 255).astype("uint8")).resize((thf.width * 2, thf.height * 2), Image.BICUBIC)
ink = Image.new("RGBA", big.size, INK + (0,))
ink.putalpha(big)
ink.crop(ink.getbbox()).save(f"{LG_OUT}/the-henry-ford-ink.png")

# ITC: already transparent (no box in the supplied file). Colour: upscale x3. Ink: threshold to one colour.
itc = Image.open(f"{LG_SRC}/itc.png").convert("RGBA")
up = itc.resize((itc.width * 3, itc.height * 3), Image.LANCZOS)
up.crop(up.getbbox()).save(f"{LG_OUT}/itc.png")
a = np.asarray(itc).astype(float)
lum = 0.2126 * a[..., 0] + 0.7152 * a[..., 1] + 0.0722 * a[..., 2]
m = (a[..., 3] / 255) * np.clip((215 - lum) / 60, 0, 1)   # the light-grey swoosh edge drops out, blues become ink
mask = Image.fromarray((m * 255).astype("uint8")).resize((itc.width * 4, itc.height * 4), Image.BICUBIC)
mask = mask.filter(ImageFilter.GaussianBlur(1.2)).point(lambda v: 0 if v < 70 else (255 if v > 185 else int((v - 70) * 255 / 115)))
ink = Image.new("RGBA", mask.size, INK + (0,))
ink.putalpha(mask)
ink.crop(ink.getbbox()).save(f"{LG_OUT}/itc-ink.png")

# ------------------------------------------------------------------ logos: optical sizing
def raster(name):
    path = f"{LG_OUT}/{name}"
    if name.endswith(".svg"):
        tmp = f"/tmp/p2_{name}.png"
        subprocess.run(["node", "tools/svg_to_png.js", path, tmp, "1200"], check=True)
        im = Image.open(tmp).convert("RGBA")
    else:
        im = Image.open(path).convert("RGBA")
    return im.crop(im.getbbox())


def weight(im):
    """bbox aspect and ink density (share of the bbox that is 'ink', alpha-weighted)."""
    al = np.asarray(im)[..., 3] / 255
    return im.width / im.height, float(al.mean())


# Inner box of the tile (3:2 tile minus 32px padding) at the homepage size: 316x211 -> 252x147.
BOX_W, BOX_H = 252, 147
SETS = {"colour": ["the-henry-ford.png", "itc.png", "rhode-island-doh.svg", "littelfuse.svg"],
        "ink": ["the-henry-ford-ink.png", "itc-ink.png", "rhode-island-doh-ink.svg", "littelfuse-ink.svg"]}
# Optical rule: equal "visual mass" = bbox area x density^0.5 (a dense solid square reads heavier
# than a thin seal of the same size), then capped to the box. Hand trims after checking side by side.
TRIM = {"the-henry-ford.png": 1.55, "the-henry-ford-ink.png": 0.85, "itc.png": 1.0, "itc-ink.png": 1.0,
        "rhode-island-doh.svg": 0.8, "rhode-island-doh-ink.svg": 0.8, "littelfuse.svg": 1.0, "littelfuse-ink.svg": 1.0}
TARGET = 8200                                     # px^2 of "visual mass" at the homepage tile size
sizes = {}
for variant, names in SETS.items():
    for name in names:
        im = raster(name)
        ratio, dens = weight(im)
        area = TARGET / (dens ** 0.5) * TRIM[name]
        h = (area / ratio) ** 0.5
        w = h * ratio
        s = min(1, BOX_W / w, BOX_H / h)
        w, h = w * s, h * s
        sizes[name] = {"w_pct": round(100 * w / BOX_W, 1), "h_pct": round(100 * h / BOX_H, 1),
                       "ratio": round(ratio, 3), "density": round(dens, 3)}
        # Squarespace plate: transparent 1200x800, logo optically sized, 121px margin (= 32px at 316px)
        PW, PH, MARGIN = 1200, 800, 121
        bw, bh = PW - 2 * MARGIN, PH - 2 * MARGIN
        pw = round(bw * w / BOX_W)
        ph = round(pw / ratio)
        plate = Image.new("RGBA", (PW, PH), (0, 0, 0, 0))
        big = im.resize((pw, ph), Image.LANCZOS)
        plate.alpha_composite(big, ((PW - pw) // 2, (PH - ph) // 2))
        plate.save(f"{LG_OUT}/plate-{name.rsplit('.', 1)[0]}.png", optimize=True)
json.dump(sizes, open(f"{LG_OUT}/sizes.json", "w"), indent=1)
for k, v in sizes.items():
    print(f"{k:28s} w {v['w_pct']:5}%  h {v['h_pct']:5}%  ratio {v['ratio']}  density {v['density']}")
