"""Rhode Island screens (Room 03): her PDF "Rhode Island Dept of Health" (98 pages) -> web images + content/ri-screens.json.

Wide pages (1440pt) are the desktop COVID-19 test scheduling portal; narrow pages (375pt) are the 401 Health mobile app.
Run from yasmin/:  python3 tools/build_ri_screens.py <path to the PDF>
Sections follow the PDF's own order. Captions describe each screen (added, for Yasmin to approve).
Page 15 is blank and is left out.
"""
import json, os, subprocess, sys, tempfile
from PIL import Image

PDF = sys.argv[1]
OUT = "site/assets/img/ri"
for d in (OUT, f"{OUT}/thumbs", f"{OUT}/phone"):
    os.makedirs(d, exist_ok=True)

DESKTOP = [
    ("Test Scheduling: Hi-Fi Designs", [(1, "Welcome: log in or create an account"), (2, "Portal home: schedule a test or update a profile"),
        (3, "Schedule a COVID-19 test: who is it for?"), (4, "Add a new dependent child"), (5, "Schedule a test: dependent added"),
        (6, "Add a new dependent child, with primary care provider"), (7, "Insurance information"), (8, "Reason for scheduling"),
        (9, "Select a testing facility on the map"), (10, "Select an appointment time"), (11, "Appointment confirmation")]),
    ("Portal Screenshots", [(12, "Daily activities"), (13, "Schedule a COVID-19 test"), (14, "Insurance information"),
        (16, "Select a test facility"), (17, "Facility selected: available times"), (18, "Select a time"), (19, "Appointment confirmed")]),
    ("Wireframes", [(20, "Welcome"), (21, "Portal home"), (22, "Schedule a COVID-19 test"), (23, "Add a new dependent child"),
        (24, "Demographic information"), (25, "Daily activities"), (26, "Insurance information"), (27, "Reasons for scheduling"),
        (28, "Select a testing facility"), (29, "Select an appointment time"), (30, "Appointment confirmation"),
        (31, "Home with the upcoming appointment"), (32, "Testing facilities with distances"), (33, "Appointment time selected"),
        (34, "Upcoming appointment details")]),
    ("Wireframe Notes & Options", [(35, "Note: a progress bar for the scheduling steps"), (36, "Select a test facility: option"),
        (37, "Profile updated"), (38, "Testing facilities by zip code"), (39, "Note: two looks for the calendar selector"),
        (40, "Update contact information"), (41, "Note: using the map and shared location"), (42, "Update your details")]),
]
MOBILE = [
    ("Onboarding", [(43, "Launch screen"), (44, "Choose a language"), (45, "Language options"), (46, "English selected"),
        (47, "Welcome: what the app does"), (48, "Terms of use & privacy policy"), (49, "Location and notification permissions"),
        (50, "Set-up complete"), (51, "Terms of use, expanded"), (52, "Location permission prompt"), (53, "Permissions updated"),
        (54, "Notification permission prompt")]),
    ("Home & Menu", [(55, "Home dashboard"), (56, "Menu")]),
    ("Vaccine Record", [(57, "COVID-19 vaccination record"), (58, "Vaccination card with QR code"), (96, "Vaccine doses"),
        (97, "Vaccination record"), (98, "QR code for verification")]),
    ("Help & Resources", [(59, "Get Help"), (60, "Get Informed"), (61, "Get Involved"), (62, "Get Involved, expanded"),
        (63, "Get Tested"), (64, "Get Tested, expanded")]),
    ("Symptom Diary", [(65, "Symptom Diary"), (66, "My Symptom Diary"), (67, "Symptom survey: step 1"), (68, "Symptom survey: step 2"),
        (69, "Symptom survey: step 3"), (70, "Symptom survey: step 4"), (71, "Symptom survey: step 5"), (72, "Symptom survey: step 6"),
        (73, "Symptom survey: step 7"), (74, "Symptom survey: step 8"), (75, "Survey, second version: step 1"),
        (76, "Survey, second version: step 2"), (77, "Survey, second version: step 3"), (78, "Survey, second version: last step"),
        (79, "Survey, second version: step 4"), (80, "Survey, second version: step 5"), (83, "Survey, second version: step 6"),
        (84, "Survey, second version: step 7"), (85, "Survey, second version: step 8")]),
    ("Screening Status", [(81, "My Screening Status"), (82, "Screening status: choose a household member"),
        (86, "Screening status: symptoms reported"), (87, "Screening status: feeling well")]),
    ("Household", [(88, "Manage my household"), (89, "Add a household member"), (90, "Edit household members")]),
    ("Settings & Support", [(91, "Settings"), (92, "Notifications"), (93, "Contact us"), (94, "FAQs"), (95, "FAQ: app privacy")]),
]

tmp = tempfile.mkdtemp()


def render(page, width):
    base = f"{tmp}/p{page}"
    subprocess.run(["pdftoppm", "-f", str(page), "-l", str(page), "-png", "-scale-to-x", str(width), "-scale-to-y", "-1", PDF, base], check=True)
    f = next(x for x in os.listdir(tmp) if x.startswith(f"p{page}-") or x == f"p{page}.png")
    im = Image.open(f"{tmp}/{f}").convert("RGB")
    os.remove(f"{tmp}/{f}")
    return im


data = {}
for key, groups, kind, W, cssw in (("desktop", DESKTOP, "d", 1600, 1440), ("mobile", MOBILE, "m", 720, 375)):
    out = []
    for fi, (flow, screens) in enumerate(groups, 1):
        rows = []
        for si, (page, cap) in enumerate(screens, 1):
            im = render(page, W)
            name = f"ri-{kind}-{fi:02d}-{si:02d}.jpg"
            im.save(f"{OUT}/{name}", quality=80 if kind == "d" else 82, optimize=True, progressive=True)
            if kind == "d":   # step-strip thumbnail: the top of the screen
                top = im.crop((0, 0, im.width, min(im.height, round(im.width * 74 / 118))))
                top.resize((360, round(360 * top.height / top.width)), Image.LANCZOS).save(f"{OUT}/thumbs/{name}", quality=74, optimize=True)
            else:             # lighter copy for the phone row
                im.resize((480, round(480 * im.height / im.width)), Image.LANCZOS).save(f"{OUT}/phone/{name}", quality=76, optimize=True, progressive=True)
            rows.append({"file": name, "caption": cap, "w": cssw, "h": round(im.height * cssw / im.width), "page": page})
        out.append({"flow": flow, "screens": rows})
    data[key] = out
json.dump(data, open("content/ri-screens.json", "w"), indent=1, ensure_ascii=False)
n = sum(len(g["screens"]) for v in data.values() for g in v)
print(f"{n} screens ({sum(len(g['screens']) for g in data['desktop'])} desktop, {sum(len(g['screens']) for g in data['mobile'])} mobile) -> {OUT}; content/ri-screens.json")
