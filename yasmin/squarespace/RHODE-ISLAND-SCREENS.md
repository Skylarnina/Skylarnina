# Rhode Island screens (Room 03, Fig. 04): Squarespace build

**What it is:** the 98-page PDF *Rhode Island Dept of Health*, shown on the Rhode Island page where her text asks for the desktop and mobile wireframes (after the feature list ending "…Testing Location Map…").
- **Desktop (41 screens, 1440 wide):** the COVID-19 test scheduling portal. It's a flow viewer in a browser frame (health.ri.gov), section by section, following the PDF's order:
  1. Test Scheduling: Hi-Fi Designs (pages 1–11)
  2. Portal Screenshots (12–19)
  3. Wireframes (20–34)
  4. Wireframe Notes & Options (35–42)
- **Mobile (56 screens, 375 wide):** the 401 Health app, in phone mockups, swipeable and filtered by group: Onboarding, Home & Menu, Vaccine Record, Help & Resources, Symptom Diary, Screening Status, Household, Settings & Support.
- Page 15 is blank and is left out. Every screen opens full size, with ← →, the arrow keys, Esc and swiping.

## Build (ready to paste, nothing to upload)
- [ ] On the Rhode Island page, replace the "desktop wireframes" video with a full-width **Code** block. Paste all of `rhode-island-desktop-embed.html` and turn **Display Source** off.
- [ ] Under it, add a second full-width **Code** block with all of `rhode-island-mobile-embed.html`, **Display Source** off.
- [ ] Under both, add a **Text** block in Paragraph 3: `Fig. 04 — Desktop and mobile designs: the COVID-19 test scheduling portal and the 401 Health app`.
- [ ] Check it on the live page in a new tab (Squarespace doesn't run code in the editor).

The screens load from the portfolio's public GitHub repo through the jsDelivr CDN, pinned to a fixed commit (`tools/build_lf_embed.py embed <commit> ri`). If the repo is made private, they stop loading.

## To confirm with Yasmin
- **Section names and captions are mine.** Check them, especially "Portal Screenshots" (pages 12–19). Those look like screenshots of the built portal, with test data dated October 2021, but she may want to call them "Existing portal" or "Final build".
- **Permission:** confirm she may show these RIDOH screens publicly. The vaccine-record screens use sample data ("Jane Doe") and a sample QR code.
- The old "Desktop wireframes" video (`r03-wireframes.mp4`) is no longer used on the page.

Source files: `tools/build_ri_screens.py` (PDF → `site/assets/img/ri/`, captions in `content/ri-screens.json`).
