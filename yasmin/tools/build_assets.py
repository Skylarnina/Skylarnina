"""Build every web asset the prototype uses from yasmin/media and yasmin/source.

Run from the yasmin/ folder:  python3 tools/build_assets.py
Needs: Pillow, PyMuPDF (pymupdf), imageio-ffmpeg.
Outputs: site/assets/img/*.jpg|png and site/assets/video/*.mp4.
The same files are the Squarespace upload set (see SQUARESPACE-BUILD-NOTES.md).
"""
import os, subprocess
from PIL import Image, ImageEnhance
import pymupdf
import imageio_ffmpeg

Image.MAX_IMAGE_PIXELS = None
FF = imageio_ffmpeg.get_ffmpeg_exe()
IMG, VID = "site/assets/img", "site/assets/video"
os.makedirs(IMG, exist_ok=True); os.makedirs(VID, exist_ok=True)
M = "media"; R1, R2, R3, R4 = (f"{M}/room01-jackson-home", f"{M}/room02-power-energy",
                               f"{M}/room03-rhode-island", f"{M}/room04-littelfuse")
DOC = f"{M}/doc"


def save(im, name, maxw=1600, q=82):
    im = im.convert("RGB")
    if im.width > maxw:
        im = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
    im.save(f"{IMG}/{name}", quality=q, optimize=True, progressive=True)


def crop(path, box):
    return Image.open(path).convert("RGB").crop(box)


def fit(im, ratio):
    """Centre-crop to a width/height ratio."""
    w, h = im.size
    if w / h > ratio:
        nw = round(h * ratio); x = (w - nw) // 2; return im.crop((x, 0, x + nw, h))
    nh = round(w / ratio); y = (h - nh) // 2; return im.crop((0, y, w, y + nh))


def frame(video, t, out):
    subprocess.run([FF, "-loglevel", "error", "-y", "-ss", str(t), "-i", video, "-frames:v", "1", "-q:v", "2", out], check=True)
    return Image.open(out).convert("RGB")


def pdf_page(path, page, dpi):
    pix = pymupdf.open(path)[page - 1].get_pixmap(dpi=dpi)
    return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)


TMP = "/tmp/yasmin_frames"; os.makedirs(TMP, exist_ok=True)
SIM = f"{R1}/r01_video_discrete-event-simulation.mp4"
FIN = f"{R2}/r02_video_final-setup.mp4"
FAB = f"{R2}/r02_video_fabrication-progression.mp4"


def sim(t):  # simulation frames, minus the burned-in player bar
    im = frame(SIM, t, f"{TMP}/sim_{t}.jpg"); return im.crop((0, 0, im.width, im.height - 100))


# ---------- Room 01, Jackson Home ----------
paths = f"{R1}/r01_plan_house-visitor-paths.png"; plain = f"{R1}/r01_plan_house.png"
save(sim(52), "r01-cover-16x9.jpg", 1920)
save(crop(paths, (40, 380, 1340, 1111)), "r01-plan-16x9.jpg", 1600)  # stops above the stray tooltip
save(crop(paths, (0, 0, 1544, 2232)), "r01-plan-paths.jpg", 1400)
save(Image.open(plain), "r01-plan-plain.jpg", 1024)
save(Image.open(f"{DOC}/room01-jackson-home/doc-04_room01-04_p06.jpeg"), "r01-plan-annex.jpg", 975)
# itinerary stops
save(crop(f"{DOC}/room01-jackson-home/doc-04_room01-04_p06.jpeg", (640, 0, 975, 230)), "r01-stop-entrance.jpg", 700)
save(crop(f"{DOC}/room01-jackson-home/doc-04_room01-04_p06.jpeg", (330, 170, 760, 470)), "r01-stop-vestibule.jpg", 700)
save(crop(paths, (60, 440, 1250, 730)), "r01-stop-front-rooms.jpg", 1000)
save(crop(plain, (252, 517, 809, 968)), "r01-stop-kitchen.jpg", 700)
save(crop(paths, (60, 1500, 900, 2090)), "r01-stop-exit.jpg", 800)
for t, n in [(22, "annex-crowd"), (27, "annex-close"), (33, "exhibit"), (40, "case"), (46, "music-room"), (14, "overview")]:
    save(sim(t), f"r01-sim-{n}.jpg", 900)
# data wall
ds1 = f"{R1}/r01_chart_congestion-queues-visit-delays.png"
save(crop(ds1, (19, 85, 620, 451)), "r01-chart-congestion.jpg", 900)
save(crop(ds1, (626, 85, 1165, 485)), "r01-chart-skips.jpg", 900)
save(crop(ds1, (19, 549, 968, 855)), "r01-chart-queue.jpg", 1000)
save(crop(ds1, (1005, 611, 1767, 861)), "r01-chart-delays.jpg", 900)
save(Image.open(ds1), "r01-chart-dataset-full.jpg", 1774)
save(Image.open(f"{R1}/r01_chart_arrivals-random.png"), "r01-chart-arrivals-random.jpg", 1400)
save(Image.open(f"{R1}/r01_chart_arrivals-on-time.png"), "r01-chart-arrivals-ontime.jpg", 1400)
save(Image.open(f"{R1}/r01_chart_docent-control.png"), "r01-chart-docent.jpg", 1400)
best = f"{DOC}/room01-jackson-home/doc-10_room01-10_p12.jpeg"
save(Image.open(best), "r01-chart-best-full.jpg", 975)
save(crop(best, (16, 60, 513, 224)), "r01-chart-best-entrance.jpg", 700)
save(crop(best, (539, 245, 961, 408)), "r01-chart-best-house.jpg", 700)
evt = f"{R1}/r01_chart_expected-visit-times.png"
save(crop(evt, (20, 305, 1616, 920)), "r01-chart-visit-times.jpg", 1400)
save(crop(f"{DOC}/room01-jackson-home/doc-01_room01-01_p03.jpeg", (578, 52, 965, 440)), "r01-chart-onsite-box.jpg", 700)

# ---------- Room 02, Power & Energy ----------
col = frame(FIN, 0, f"{TMP}/fs0.jpg")
save(col.crop((0, 400, 1080, 1008)), "r02-cover-16x9.jpg", 1600)
save(col, "r02-column-installed.jpg", 1080)
save(frame(FIN, 20, f"{TMP}/fs20.jpg"), "r02-column-installed-b.jpg", 1080)
fab13 = frame(FAB, 13, f"{TMP}/fab13.jpg"); save(fab13, "r02-fab-lit.jpg", 960)
save(frame(FAB, 1, f"{TMP}/fab1.jpg"), "r02-fab-before.jpg", 960)
save(frame(FAB, 10, f"{TMP}/fab10.jpg"), "r02-fab-install.jpg", 960)
arts = {"wayfinding": "PandE_Column_Art_260127", "stories": "PandE_Column_Art_2601273",
        "map": "PandE_Column_CutUpArt_2602188", "careers": "PandE_Column_CutUpArt_2602185",
        "artifacts": "PandE_Column_Art_2601272", "careers-b": "PandE_Column_CutUpArt_2602186",
        "careers-c": "PandE_Column_CutUpArt_2602187"}
for k, f in arts.items():
    save(Image.open(f"{R2}/r02_art_{f}.jpg"), f"r02-side-{k}.jpg", 560, 80)
shop = "source/PandE_Shop-Drawing_Column-Surrounds_AV05.pdf"
for p in (1, 2, 3):
    save(pdf_page(shop, p, 170), f"r02-shop-{p}.jpg", 2400, 85)
save(pdf_page(shop, 1, 300).crop((0, 0, 1650, 1650)), "r02-shop-1-detail.jpg", 1200, 85)
wb = Image.open(f"{R2}/r02_sketch_whiteboard-lofi.png").convert("RGB")
save(wb.crop((0, 0, 836, 941)), "r02-sketch-a.jpg", 836); save(wb.crop((836, 0, 1672, 941)), "r02-sketch-b.jpg", 836)
itc = f"{R2}/r02_board_itc-employee-research.png"
save(Image.open(itc), "r02-itc-full.jpg", 1920); save(crop(itc, (30, 300, 1900, 800)), "r02-itc-detail.jpg", 1600)
sides = f"{R2}/r02_diagram_column-sides-flow.png"
save(Image.open(sides), "r02-sides-full.jpg", 2000); save(crop(sides, (1500, 1900, 4000, 4300)), "r02-sides-detail.jpg", 1200)
save(Image.open(f"{R2}/r02_board_content-themes-experience-flow.png"), "r02-concept-board.jpg", 1536)

# ---------- Room 03, Rhode Island ----------
ri = "source/Rhode_Island_DOH_Wireframes.pdf"
for p, n in [(45, "language"), (47, "welcome"), (55, "home"), (57, "record"), (58, "record-b"), (96, "doses"),
             (97, "record-c"), (66, "symptoms"), (89, "household"), (63, "testing")]:
    save(pdf_page(ri, p, 216), f"r03-screen-{n}.jpg", 750, 85)
for p, n in [(1, "portal"), (9, "map"), (10, "schedule")]:
    save(pdf_page(ri, p, 108), f"r03-desk-{n}.jpg", 1600, 85)
save(Image.open(f"{DOC}/room03-rhode-island/doc-19_room03-01_p27.jpeg"), "r03-goals-full.jpg", 975)
save(crop(f"{DOC}/room03-rhode-island/doc-19_room03-01_p27.jpeg", (0, 648, 975, 787)), "r03-goals-detail.jpg", 975)
save(Image.open(f"{R3}/r03_ui_vaccine-details-annotated.png"), "r03-annotated.jpg", 1536)
# 16:9 header: five screens in a row on the deeper wall
wall = Image.new("RGB", (3200, 1800), (233, 228, 219))
for i, n in enumerate(["language", "home", "record", "doses", "household"]):
    s = Image.open(f"{IMG}/r03-screen-{n}.jpg").convert("RGB"); s = s.resize((520, round(s.height * 520 / s.width)))
    wall.paste(s, (170 + i * 590, 240 + (60 if i % 2 else 0)))
save(wall, "r03-cover-16x9.jpg", 1920)

# ---------- Room 04, Littelfuse ----------
jm = f"{R4}/r04_doc_journey-map.png"; ar = f"{R4}/r04_doc_user-archetypes.png"
save(crop(jm, (110, 0, 1674, 880)), "r04-cover-16x9.jpg", 1564)
save(Image.open(jm), "r04-journey-full.jpg", 1787)
for n, b in [("find", (160, 262, 610, 612)), ("learn", (650, 262, 1128, 612)), ("get", (1170, 262, 1630, 612)),
             ("detailed", (60, 620, 1700, 880))]:
    save(crop(jm, b), f"r04-journey-{n}.jpg", 1600)
for n, b in [("engineering", (30, 40, 1570, 1640)), ("sales", (1620, 30, 2655, 1640)), ("procurement", (2725, 30, 3740, 1640))]:
    save(crop(ar, b), f"r04-archetype-{n}.jpg", 1000)
save(Image.open(ar), "r04-archetypes-full.jpg", 2400)

# ---------- Homepage strips (P4), 4:1 ----------
save(fit(col.crop((0, 640, 1080, 1100)), 4), "strip-exhibit.jpg", 1800)
row = Image.new("RGB", (3600, 900), (233, 228, 219))
for i, n in enumerate(["language", "record", "record-b", "doses", "welcome"]):
    s = Image.open(f"{IMG}/r03-screen-{n}.jpg").convert("RGB"); s = s.resize((680, round(s.height * 680 / s.width)))
    row.paste(s.crop((0, 120, 680, 1020)), (30 + i * 715, 0))
save(row, "strip-ux-design.jpg", 1800)
save(crop(paths, (40, 1330, 1336, 1654)), "strip-ux-research.jpg", 1800)
save(fit(crop(f"{R2}/r02_art_PandE_Column_CutUpArt_2602185.jpg", (0, 150, 2160, 1500)), 4), "strip-marketing.jpg", 1800)  # ITC career-story photo

# ---------- Videos: muted H.264, faststart ----------
def enc(src, out, vf, extra=()):
    subprocess.run([FF, "-loglevel", "error", "-y", "-i", src, *extra, "-an", "-vf", vf, "-c:v", "libx264",
                    "-preset", "slow", "-crf", "30", "-pix_fmt", "yuv420p", "-movflags", "+faststart", "-r", "30",
                    f"{VID}/{out}"], check=True)
    frame(f"{VID}/{out}", 1, f"{IMG}/poster-{out[:-4]}.jpg")

enc(SIM, "r01-simulation.mp4", "crop=iw:ih-100:0:0,scale=1280:-2", ("-t", "48"))
enc(FAB, "r02-fabrication.mp4", "scale=960:-2")
enc(FIN, "r02-final-setup.mp4", "scale=720:-2")
enc(f"{R2}/r02_video_interface-user-flow.mp4", "r02-interface.mp4", "scale=1280:-2")
enc(f"{R2}/r02_video_appspace-cms-channels.mp4", "r02-cms.mp4", "scale=1280:-2")
enc(f"{R3}/r03_video_wireframes.mp4", "r03-wireframes.mp4", "scale=1280:-2")
enc(f"{R3}/r03_video_app-store-reviews.mp4", "r03-app-reviews.mp4", "scale=540:-2")
enc(f"{R4}/r04_video_engineering-personas.mp4", "r04-personas.mp4", "scale=1280:-2")
print("done")
