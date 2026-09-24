"""Round 3 image additions (run from yasmin/, after tools/build_assets.py).
Covers: 16:7 for case-study headers, 3:2 for the project rows and grid.
Figures: full, uncropped versions of her doc images that had no full export yet."""
import subprocess, imageio_ffmpeg
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
FF = imageio_ffmpeg.get_ffmpeg_exe()
IMG = "site/assets/img"
M = "media"


def save(im, name, maxw=2000, q=84):
    im = im.convert("RGB")
    if im.width > maxw:
        im = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
    im.save(f"{IMG}/{name}", quality=q, optimize=True, progressive=True)


def fit(im, ratio, cx=.5, cy=.5):
    w, h = im.size
    if w / h > ratio:
        nw = round(h * ratio); x = round((w - nw) * cx); return im.crop((x, 0, x + nw, h))
    nh = round(w / ratio); y = round((h - nh) * cy); return im.crop((0, y, w, y + nh))


def frame(src, t, out):
    subprocess.run([FF, "-loglevel", "error", "-y", "-ss", str(t), "-i", src, "-frames:v", "1", "-q:v", "2", out], check=True)
    return Image.open(out).convert("RGB")


sim = frame(f"{M}/room01-jackson-home/r01_video_discrete-event-simulation.mp4", 52, "/tmp/r3_sim.jpg")
sim = sim.crop((0, 0, sim.width, sim.height - 100))                       # drop the burned-in player bar
col = frame(f"{M}/room02-power-energy/r02_video_final-setup.mp4", 0, "/tmp/r3_col.jpg")
screens = Image.open(f"{IMG}/r03-cover-16x9.jpg").convert("RGB")
journey = Image.open(f"{M}/room04-littelfuse/r04_doc_journey-map.png").convert("RGB")

# the RI composite was built on the old deeper-wall colour; move it to the new #F4F3F0 ground
px = screens.load()
for y in range(screens.height):
    for x in range(screens.width):
        if px[x, y] == (233, 228, 219) or sum(abs(a - b) for a, b in zip(px[x, y], (233, 228, 219))) < 6:
            px[x, y] = (244, 243, 240)

save(fit(sim, 16 / 7, cy=.55), "r3-cover-r01-16x7.jpg", 2000)
save(fit(col, 16 / 7, cy=.42), "r3-cover-r02-16x7.jpg", 2000)
save(fit(screens, 16 / 7, cy=.3), "r3-cover-r03-16x7.jpg", 2000)
save(fit(journey.crop((0, 60, journey.width, journey.height)), 16 / 7, cy=.35), "r3-cover-r04-16x7.jpg", 2000)

save(fit(sim, 3 / 2), "r3-cover-r01-3x2.jpg", 1200)
save(fit(col, 3 / 2, cy=.45), "r3-cover-r02-3x2.jpg", 1200)
save(fit(screens, 3 / 2, cy=.2), "r3-cover-r03-3x2.jpg", 1200)
save(fit(journey.crop((150, 250, 1640, 620)), 3 / 2), "r3-cover-r04-3x2.jpg", 1200)

# full figures that were only exported as crops before
save(Image.open(f"{M}/room01-jackson-home/r01_chart_expected-visit-times.png"), "r3-fig-visit-times.jpg", 1616)
save(Image.open(f"{M}/room02-power-energy/r02_sketch_whiteboard-lofi.png"), "r3-fig-whiteboard.jpg", 1672)
save(Image.open(f"{M}/doc/room04-littelfuse/doc-22_room04-01_p33.jpeg"), "r3-fig-decision-board.jpg", 975)
save(Image.open(f"{M}/doc/room01-jackson-home/doc-01_room01-01_p03.jpeg"), "r3-fig-visitor-type-sheet.jpg", 975)
print("ok")
