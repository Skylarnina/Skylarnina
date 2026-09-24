"""Round 4 image exports (run from yasmin/, after build_assets.py and build_r3_assets.py).

Rule from the round 4 review: a cover is a finished image, placed as-is. Drawings,
screens and documents sit WHOLE on the light ground (#F4F3F0) or white, never cropped.
Only photographs may be cropped, and only to the frame's own ratio.

  r4-row-rNN-3x2.jpg     project rows + projects grid (3:2, subject whole)
  r4-cover-rNN-16x7.jpg  case-study covers for the two light rooms (screens, journey map)
  r4-panel-0N.jpg        homepage discipline panels (2:3)
  r4-about-*.jpg         homepage About mosaic (4:5, 3:2, 1:1, 1:1)
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


col_src = f"{M}/room02-power-energy/r02_video_final-setup.mp4"
fab_src = f"{M}/room02-power-energy/r02_video_fabrication-progression.mp4"
col_whole = [frame(col_src, t) for t in (1, 5, 15)]          # frames where the whole column is in shot
plan_paths = Image.open(f"{M}/room01-jackson-home/r01_plan_house-visitor-paths.png")
screens = [Image.open(f"{IMG}/r03-screen-record.jpg"), Image.open(f"{IMG}/r03-screen-doses.jpg")]
journey = Image.open(f"{M}/room04-littelfuse/r04_doc_journey-map.png")
itc = Image.open(f"{M}/room02-power-energy/r02_board_itc-employee-research.png")

# ---- project rows and projects grid: finished 3:2, subject whole
save(place([plan_paths], 1800, 1200, 72, 0), "r4-row-r01-3x2.jpg")                 # the whole plan, with paths
save(place(col_whole, 1800, 1200, 120, 28), "r4-row-r02-3x2.jpg")                  # the whole column, three states
save(place(screens, 1800, 1200, 96, 56), "r4-row-r03-3x2.jpg")                     # both phone screens
save(place([journey], 1800, 1200, 72, 0, WHITE), "r4-row-r04-3x2.jpg")             # the whole journey map

# ---- case-study covers for the light rooms: 16:7, subject whole
ri_row = [Image.open(f"{IMG}/r03-screen-{s}.jpg") for s in ("welcome", "home", "record", "doses", "household")]
save(place(ri_row, 2000, 875, 80, 40), "r4-cover-r03-16x7.jpg")
save(place([journey], 2000, 875, 60, 0, WHITE), "r4-cover-r04-16x7.jpg")

# ---- homepage discipline panels, 2:3
save(crop_to(Image.open(f"{IMG}/r02-column-installed.jpg"), 2 / 3, cy=.45), "r4-panel-01.jpg")   # photograph
def upper(items, pad, gap):
    """2:3 panel with the subject whole in the upper 70%, so the name below sits on plain ground."""
    top = place(items, 1000, 1050, pad, gap)
    canvas = Image.new("RGB", (1000, 1500), GROUND)
    canvas.paste(top, (0, 30))
    return canvas


save(upper(screens, 90, 40), "r4-panel-02.jpg")
save(upper([plan_paths], 70, 0), "r4-panel-03.jpg")
save(upper([itc], 60, 0), "r4-panel-04.jpg")

# ---- About mosaic: stand-ins from her work until she supplies personal photos (ASSET-GAPS R4-1..R4-4)
save(crop_to(frame(col_src, 19), 4 / 5, cy=.35), "r4-about-tall-4x5.jpg")           # photograph
save(crop_to(frame(fab_src, 12), 3 / 2, cy=.55), "r4-about-wide-3x2.jpg")           # photograph
save(crop_to(frame(fab_src, 0), 1, cx=.5), "r4-about-sq-a.jpg")                      # photograph
save(place([Image.open(f"{IMG}/r02-shop-1-detail.jpg")], 1000, 1000, 48, 0), "r4-about-sq-b.jpg")   # drawing, whole

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
