# Littelfuse screens (Room 04, Fig. 08): Squarespace build

**What it is:** the hi-fi screens from Yasmin's doc *Little Fuse Wireframes* (13 Adobe XD links), shown on the Littelfuse page where her text says "Below are the completed wire frames."
- **Desktop:** a flow viewer. Buttons for the nine flows (her doc's headings), the current screen in a browser window that scrolls like the real page, numbered steps, ← →, and **View full screen**.
- **Mobile:** a row of phone mockups, swipeable, filtered by flow (the six section titles from her mobile XD file). Each phone scrolls to show the whole screen; click or tap to enlarge.
- The full-screen viewer works for both, with the arrow keys, Esc, and swiping on phones.

**Files:**
- `littelfuse-screens.html`: the Code Block.
- `get-littelfuse-addresses.js`: the Console helper.
- The screens themselves: `site/assets/img/lf/`, 97 JPGs: 58 desktop, 39 mobile (also sent as a zip):
  - `lf-d-<flow>-<screen>.jpg` (desktop)
  - `lf-m-<flow>-<screen>.jpg` (mobile)

Captions are in `content/lf-screens.json`.

## Steps
- [ ] **Upload the 97 screens.** Go to **Website → Assets** (Asset Library) → **Upload**, and select all the files in the zip at once. Keep the file names: the helper finds the screens by name.
- [ ] **Copy their addresses.**
  1. Stay on the Asset Library page and scroll down until all the `lf-` screens have appeared.
  2. Open the browser Console: `Ctrl+Shift+J` on Windows, `Cmd+Option+J` on Mac. If Chrome asks, type `allow pasting` first.
  3. Paste the contents of `get-littelfuse-addresses.js` and press Enter. It should say **"97 of 97 screens found and copied."**
  4. If it lists missing ones, scroll so they show and run it again.
  5. If it finds none, the Asset Library doesn't show its images in a way the helper can read. Instead, make a hidden page (**Pages → Not Linked**), add a **Gallery** block with all 97 screens, open that page in its own tab, and run the helper there.
- [ ] **Fill in the code.** Open `littelfuse-screens.html` in a text editor. Select the two lines `var DESKTOP = [];` and `var MOBILE = [];` and paste over them.
- [ ] **Add it to the page.**
  1. On the Littelfuse page, after the paragraph ending "…Below are the completed wire frames.", add a **Code** block across the **full width** (columns 1–24; on mobile, full width).
  2. Paste the whole code and turn **Display Source** off.
  3. Under it, add a **Text** block in Paragraph 3 with the caption: `Fig. 08 — Hi-fi screens: nine desktop flows and the mobile designs`.
- [ ] **Check it on the page itself, in a new tab.** Squarespace doesn't run code inside the editor. Test each flow button, ← →, View full screen, the phone row and its flow buttons, and enlarging a phone screen.

## Notes
- The page is behind the portfolio password, which is right for client work. **Confirm with Yasmin that she may show these Littelfuse designs.** The mobile file's cover credits Cognizant, so check any agreement with Littelfuse or Cognizant.
- The XD files' cover and divider cards (the green "Mobile Mockups" cover and the section titles) aren't shown as screens; their titles name the mobile groups.
- Repeats are kept where a flow starts from the same page (several flows begin on the home page), so each flow reads on its own.
- **Image size:** the longest mobile screen is 720 × 17,636 px. If Squarespace refuses it on upload, tell me and I'll split it.
- **To change a caption:** edit `tools/build_lf_screens.py`, re-run it, and run the helper again. Or edit the caption text directly in the pasted code.
