"""Round 4 image exports (Phase 2: the homepage row covers, panel images and About mosaic were retired;
the homepage no longer shows case-study media) (run from yasmin/, after build_assets.py and build_r3_assets.py).

Rule from the round 4 review: a cover is a finished image, placed as-is. Drawings,
screens and documents sit WHOLE on the light ground (#F4F3F0) or white, never cropped.
Only photographs may be cropped, and only to the frame's own ratio.

  r5-ri-five-screens.jpg Rhode Island cover plate (FIG. 01): five screens in a row, whole
  r4-ri-screens.jpg      the two frameless RI screens, side by side (Plate pair, tall slot)
  r4-whiteboard-stack.jpg  her two whiteboard photos, one above the other (Plate pair, tall slot)
Module tiles (drawings/screens/documents at their module ratio, on #F4F3F0 with the 24px
padding inside the file) are exported by tools/build_r3.py as it lays out each module.
"""
import subprocess, imageio_ffmpeg
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
FF = imageio_ffmpeg.get_ffmpeg_exe()
IMG = "site/assets/img"
M = "media"
GROUND = (244, 243, 240)
WHITE = (255, 255, 255)


def save(im, name, q=86):
    im.convert("RGB").save(f"{IMG}/{name}", quality=q, optimize=True, progressive=True)
    print(name, im.size)


def frame(src, t):
    out = f"/tmp/r4_{abs(hash((src, t)))}.jpg"
    subprocess.run([FF, "-loglevel", "error", "-y", "-ss", str(t), "-i", src, "-frames:v", "1", "-q:v", "2", out], check=True)
    return Image.open(out).convert("RGB")


def crop_to(im, ratio, cx=.5, cy=.5):
    """Photographs only: centre-crop to a ratio."""
    w, h = im.size
    if w / h > ratio:
        nw = round(h * ratio); x = round((w - nw) * cx); return im.crop((x, 0, x + nw, h))
    nh = round(w / ratio); y = round((h - nh) * cy); return im.crop((0, y, w, y + nh))


def place(items, W, H, pad, gap, ground=GROUND):
    """Lay whole images side by side, same height, centred on a ground. Nothing is cropped."""
    ims = [i.convert("RGB") for i in items]
    avail_w, avail_h = W - 2 * pad, H - 2 * pad
    ratios = [i.width / i.height for i in ims]
    h = min(avail_h, (avail_w - gap * (len(ims) - 1)) / sum(ratios))
    ws = [round(h * r) for r in ratios]
    h = round(h)
    canvas = Image.new("RGB", (W, H), ground)
    x = (W - sum(ws) - gap * (len(ims) - 1)) // 2
    y = (H - h) // 2
    for im, w in zip(ims, ws):
        canvas.paste(im.resize((w, h), Image.LANCZOS), (x, y))
        x += w + gap
    return canvas


plan_paths = Image.open(f"{M}/room01-jackson-home/r01_plan_house-visitor-paths.png")
screens = [Image.open(f"{IMG}/r03-screen-record.jpg"), Image.open(f"{IMG}/r03-screen-doses.jpg")]
journey = Image.open(f"{M}/room04-littelfuse/r04_doc_journey-map.png")
itc = Image.open(f"{M}/room02-power-energy/r02_board_itc-employee-research.png")


# ---- round 5: Rhode Island's cover image, the five 401 Health screens in a row, whole and unpadded.
# Shown as FIG. 01, a full plate under the chapter index (the builder adds the 48px padding).
# Littelfuse's cover plate is her journey map, used as is.
ri_row = [Image.open(f"{IMG}/r03-screen-{s}.jpg").convert("RGB") for s in ("welcome", "home", "record", "doses", "household")]
H5, G5 = 1600, 64
ws = [round(i.width * H5 / i.height) for i in ri_row]
five = Image.new("RGB", (sum(ws) + G5 * 4, H5), GROUND)
x = 0
for im, w in zip(ri_row, ws):
    five.paste(im.resize((w, H5), Image.LANCZOS), (x, 0)); x += w + G5
save(five, "r5-ri-five-screens.jpg")




# ---- Plate pair (Power & Energy): her two whiteboard photos (fig 12) stacked, so they fill the tall slot
wb = Image.open(f"{IMG}/r3-fig-whiteboard.jpg").convert("RGB")
half = wb.width // 2
stack = Image.new("RGB", (half, wb.height * 2 + 24), GROUND)
stack.paste(wb.crop((0, 0, half, wb.height)), (0, 0))
stack.paste(wb.crop((half, 0, wb.width, wb.height)), (0, wb.height + 24))
save(stack, "r4-whiteboard-stack.jpg")

# ---- Plate pair (Rhode Island): the two frameless screens as one tall plate
save(place(screens, 1100, 1400, 60, 40), "r4-ri-screens.jpg")
print("ok")
