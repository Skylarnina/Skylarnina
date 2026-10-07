# Squarespace build notes: Phase 2

How to build the prototype (`site/`) in **Squarespace 7.1 with Fluid Engine**, using only standard sections and blocks, Site Styles, and **20 lines of custom CSS** (§2; the budget is 30). There is **no custom JavaScript** and **no Code Block used for layout**. The prototype has one small script, which only stands in for Squarespace's own Gallery slideshow (§3, section 3); everything else in it is HTML and CSS, so what you see is what the native build can do.

**Phase 2 changes (client feedback):** no project years anywhere (the case-study meta table is ROLE / METHODS / SETTING); BASED IN is United States; the résumé link is gone; the contact section is three hairline rows, Email · Phone · LinkedIn; the About section is now **Snippets About My Life**, a Gallery slideshow of her 21 photos (§3); the project rows and Projects grid show **logo tiles** instead of covers (§3); and nothing from inside the case studies appears before the password (the discipline panels use her snippet photos, and the lock screen has no background image).

**Round 6 change:** headings are now **Instrument Serif** (one weight plus italic); body, captions, labels and numerals stay Inter Tight. Heading sizes went up a step because the serif is narrower and lighter (§0).

**Round 5 changes:** the discipline panels always show their image under a 45% black overlay, and hover only lightens it to 30% (§2 lines 16–18; the opacity-0 CSS is gone). Rooms 03 and 04 get a white header with no image behind the title, and their cover moves to FIG. 01, a full plate under the chapter index (§4, 0a–0c). Headings were switched to Instrument Sans (replaced by Instrument Serif in round 6). Greyscale HTML wireframes of every page are in `wireframes/` (§7).

**Round 4 changes:** no photo strip under the hero; discipline panels with images (revised in round 5); the About section as a bento (statement + four-image mosaic); finished 3:2 row covers with the subject whole; every case-study image in one of six bento modules (§4a, full list in `MODULE-MAP.md`). Drawing, screen and document tiles are exported with the light ground and 24px padding **inside the file**, so no CSS is needed to stop Squarespace cropping them.

Items marked **verify** are how I understand the current editor. Check each once in her account before relying on it. Platform sources are at the end.

---

## 0. Set-up

| Item | Setting |
|---|---|
| Template | Any 7.1 template; everything below is set per section. |
| Fonts (*Site Styles → Fonts*) | **Headings: Instrument Serif** (Google Fonts; **verify** it is listed in her account's picker under *Site Styles → Fonts → Headings*; if it isn't, it can be added as a custom font). Use it for Heading 1–4: the hero name, page and cover titles, chapter titles, her sub-headings, the discipline names and the project titles (rows, Projects grid, previous/next). Instrument Serif comes in **one weight (400) plus italic**, so there is no bold heading: where a heading needs emphasis (her "How might we…" labels, the Littelfuse audit headings), use *italic*. Tracking **−0.01em on sizes above 48px**, 0 below. **Body, captions, labels, numerals, navigation and buttons: Inter Tight** (Google), 400/500. |
| Colours (*Site Styles → Colours*) | Palette: `#FFFFFF`, `#F4F3F0`, `#111111`. Three themes: **White** (background `#FFFFFF`, text `#111111`), **Stone** (background `#F4F3F0`, text `#111111`) and **Ink** (background `#111111`, text `#FFFFFF`, used only by the discipline panels so their names are white without CSS). No accent colour; links `#111111`, underlined. These are the **mono** values; for cream or venues see *Site Styles per theme* below. |
| Buttons | Primary: **outline**, **square corners**, 1px, 14px text. The lock screen's Enter button is solid (§5). |
| Animations (*Site Styles → Animations*) | **Fade**, speed **Slow**. Nothing else: no scroll effects, no parallax. |
| Images | Every image block: *Design → Clickthrough: Lightbox* (native lightbox), **Caption: below**, no border, no shadow, **corner radius 0**. |

### Type scale (Site Styles → Fonts)

| Style | Desktop | Mobile | Used for |
|---|---|---|---|
| Heading 1 (Instrument Serif) | 140px / 0.92, tracking −0.01em | 64px | "Hi, I'm *Yasmin.*" |
| Heading 2 (Instrument Serif) | 80px / 1.02, tracking −0.01em | 40px, tracking 0 | Page titles, cover titles, "Projects", contact line |
| Heading 3 (Instrument Serif) | 46px / 1.08, tracking 0 | 34px | Chapter titles; discipline names at 34px (28px mobile); project-row titles at 32px |
| Heading 4 (Instrument Serif) | 24px / 1.3 | 24px | Her sub-headings ("Visitor Experience", "Ticketing Strategy"…); italic for her "How might we…" labels |
| Paragraph 1 (Inter Tight) | 40px / 1.2 | 28px | The About statement (left 12 columns) |
| Paragraph 2 (Inter Tight) | 17px / 1.6 | 16px | All her body text, in a 12-column measure (~62ch) |
| Paragraph 3 (Inter Tight) | 11px / 1.45, **uppercase, tracking 0.08em**, colour 62% ink | 11px | Labels, captions, "FIG. 03 — …", "PASSWORD PROTECTED" |

Captions and labels use **62% ink, not 55%**. At 11px, 55% measures 4.4:1 on white, which fails WCAG AA; 62% passes at 5.2:1.

### Site Styles per theme (theme comparison: the client picks one)

The prototype can show seven palettes (switcher, top-right; values and contrast in `THEMES.md`; side by side in `screenshots/theme-compare.png`). **Squarespace gets only the chosen one.** Everything else in these notes (type, layout, blocks) is the same for all five; only colours change. The first table covers the three calm palettes; the bold two follow. Squarespace colours are solid, so the translucent prototype values are given as their solid equivalent on the page ground.

| Setting | Mono (built) | Cream | Venues |
|---|---|---|---|
| Palette (*Site Styles → Colours*, five slots; **verify** slot names in her account) | `#FFFFFF` · `#F4F3F0` · `#111111` | `#F3F0EA` · `#E9E4DB` · `#16140F` · `#8C2F1E` · `#FFFFFF` | `#FAFAF8` · `#F1F1EC` · `#1E3F63` · `#4F7084` · `#9B5C15` |
| Section theme **White** (most sections) | background `#FFFFFF`, text `#111111` | background `#F3F0EA`, text `#16140F` | background `#FAFAF8`, text `#1E3F63` |
| Section theme **Stone** (Snippets, Contact, Reflection) | background `#F4F3F0`, text `#111111` | background `#E9E4DB`, text `#16140F` | background `#F1F1EC`, text `#1E3F63` |
| Section theme **Ink** (discipline panels; the photos cover it) | background `#111111`, text `#FFFFFF` | background `#16140F`, text `#FFFFFF` | background `#1E3F63`, text `#FFFFFF` |
| Paragraph 3 colour (labels, captions) | `#6B6B6B` (62% ink) | `#66635E` (64% ink) | `#556E88` (75% navy) |
| Links | `#111111`, underlined | text `#16140F`; underline `#8C2F1E` (CSS +1 line, below) | `#4F7084`, underlined |
| Primary button (outline) | `#111111` | `#16140F` | `#1E3F63` |
| Section index numbers (project 01–04, chapter numbers) and PASSWORD PROTECTED | 62% ink | `#8C2F1E` | `#9B5C15` on Home/Projects; room colour on case pages (below) |
| Lock screen Enter button (CSS line 10) | `#111` fill, `#fff` text | `#8C2F1E` fill, `#fff` text | `#4F7084` fill, `#fff` text |
| Logo tile ground / hover (CSS lines 19–20) | `#F4F3F0` / `#ECEAE5` | `#E9E4DB` / `#E1DCD3` | `#F1F1EC` / per room: 01 `#DADBC9`, 02 `#EFE0CC`, 03 `#D4DDDE`, 04 `#E3CCC7` |
| Signature stripe | none | none | **Image block**, full width, `site/assets/img/stripe-venues.png` (2400×8, shown at 4px): under the hero, and above the footer. Replaces the hairline at both places. No CSS. |
| Per-room colour (case pages) | none | none | Chapter numbers, chapter-index numbers, FIG. numbers, active chapter: 01 `#6D6F41`, 02 `#9B5C15`, 03 `#4F7084`, 04 `#A8443F`. Set as the text colour of those text blocks on each project page (**verify** the text colour picker takes a custom hex; if not, +4 CSS lines scoped by each page's `#collection-…` ID). Captions' FIG. numbers need the CSS route. |

**Custom CSS per theme.** The §2 lines stay; only their hex values change: `rgba(17,17,17,.14)` → the theme hairline (cream `rgba(22,20,15,.15)`, venues `rgba(30,63,99,.15)`); `rgba(17,17,17,.62)` → the Paragraph 3 colour above; `#111` → the theme ink, except line 10, which takes the Enter fill; `#fff` on line 15 → the White background; lines 19–20 → the logo tile values. Line counts: **mono 20**; **cream 21** (+ `.sqs-html-content a{text-decoration-color:#8C2F1E}`); **venues 23** (line 20 split into four, one per room's tile section; up to 27 if per-room numbers need CSS). All three stay under the 30-line budget.

**Bold palettes: colour as sections.** Same Site Styles as their calm parent (Cream bold = Cream's palette and type colours; Venues bold = Venues' with a white page ground), plus **section colour themes**. In 7.1 each section picks one of the palette's colour themes (background + text); **verify** in her account whether a theme's background can take a colour outside the five palette slots. Where it can't, the line marked *CSS* is the fallback.

| Where | Cream bold | Venues bold |
|---|---|---|
| Palette (five slots) | `#F3F0EA` · `#E9E4DB` · `#16140F` · `#8C2F1E` · `#FFFFFF` | `#FFFFFF` · `#F1F1EC` · `#1E3F63` · `#E9A35B` · `#9DB9CB` |
| Hero | cream `#F3F0EA`, text `#16140F` | white, text `#1E3F63`; stripe Image block under it |
| Snippets About My Life (statement + slideshow) | theme **Wine**: background `#8C2F1E`, text `#F3F0EA`; the slideshow on a 12px cream frame (*CSS* +1, on the gallery's slideshow wrapper) | theme **Light**: `#F1F1EC`, text navy |
| Four disciplines (panels) | Ink theme as built; image overlay **60%** (CSS lines 16–17: `brightness(.4)`, hover `.5`) | each panel's image under its colour at 55% on top of the built darkening: orange · olive · red · light blue, white text (*CSS* +4, one `::after` per panel block, +1 hover) |
| Projects (homepage) | cream; rows 02 and 04 on a full-width **Shape** block `#E9E4DB` behind the row (**verify** a Shape block can span the full-width section) | theme **Navy**: `#1E3F63`, text white; logo plates on white (lines 19–20 values `#FFFFFF`, room tints on hover) |
| Contact | theme **Ink**: `#16140F`, text `#F3F0EA`; wine link underline (cream's +1 line covers it) | theme **Orange**: `#E9A35B`, text navy; white link underline (*CSS* +1) |
| Footer | cream | Navy (footer colour theme); stripe Image block above it |
| Case header, photo covers (01, 02) | section background overlay **wine at 82%** instead of `#111` at 38%; title cream | overlay **room colour**: 01 olive `#72743F` at 92%, 02 orange `#E9A35B` at 96% (strong enough that the title passes 4.5:1 over the photo); title white (01) / navy (02). Room 02's header text navy on that page (*CSS* +1, scoped to the page) |
| Case header, document headers (03, 04) | section theme **Wine**; the meta table on a **Shape** block of `#F3F0EA` | section ground 03 light blue `#9DB9CB` (navy title), 04 red `#B04A44` (white title; *CSS* +1 if red can't be a theme background); meta on a white Shape block |
| Chapters / Reflection | cream / `#E9E4DB` (Stone theme) | white / the room colour at 12% (`#EEEEE8`, `#FCF4EB`, `#F3F7F9`, `#F6E9E9`: *CSS* +4, or use the Light theme `#F1F1EC` and skip them) |
| Lock screen | background `#8C2F1E` (*CSS* +1), name and footer cream; the form on line 15's layer in `#F3F0EA`; Enter wine | background navy (*CSS* +1), name and footer white; layer white; Enter `#4F7084` |
| Olive panel / band colour | — | `#72743F`, outside the palette: *CSS* for the Room 01 cover overlay if the overlay picker only offers palette colours |

**CSS cost.** Cream bold: the calm Cream set (21 lines) + slideshow frame + lock background = **about 23 lines**, inside the 30 budget. Venues bold: the calm Venues set (23) + panel colours (5) + contact underline (1) + Room 02 header (1) + lock background (1) + red band (1) = **about 32 lines, plus 4 for the reflection tints**, so **over the 30-line budget**. To bring it under: drop the reflection tints (use the Light theme) and the panels' hover change, and merge the four room tile hovers into one rule per line pair; that lands at about 30. This is the real cost of choosing Venues bold.

**Heritage palettes (the refined colour direction; reasoning in COLOUR-DIRECTION.md).** Cream paper, navy-ink type, wine as Yasmin's accent, the card colours as per-project wayfinding.

| Where | Heritage | Heritage rich |
|---|---|---|
| Palette (five slots) | `#F3F0EA` · `#E9E4DB` · `#1C2635` · `#8C2F1E` · `#1E3F63` | `#F3F0EA` · `#1C2635` · `#8C2F1E` · `#1E3F63` · `#5E6337` (`#E9E4DB` only through CSS) |
| Section themes | **Paper** (bg `#F3F0EA`, text `#1C2635`) for most sections; **Paper 2** (`#E9E4DB`) for Snippets and Reflection; **Navy** (bg `#1E3F63`, text `#F3F0EA`) for Contact | Same, but Snippets uses **Olive** (bg `#5E6337`, text `#F3F0EA`) and the Reflection uses Paper |
| Paragraph 3 colour | `#61676F` (68% ink) | same |
| "Yasmin." in the hero | text colour **wine** `#8C2F1E` on the italic word (text colour picker; **verify**) | same |
| Links | text ink, underline wine (*CSS* +1); in Contact, cream text with an orange `#E9A35B` underline (*CSS* +1) | same |
| Primary button / Enter | outline ink / solid wine (CSS rule 9's value) | same |
| Project list | a five-colour rule over the list: **Image block** `stripe-venues.png` (native); a 3px venue-colour bar beside each row and the number in the venue's text colour (Shape block per row, or *CSS* +4) | same |
| Discipline panels | the 45% layer in navy-ink instead of black, 60% (*CSS*: rules 15–16 values) | same |
| Case studies | cover overlay navy-ink `#1C2635` at 60%; per-project chapter, FIG. and index numbers in the venue text colour (as Venues: text colour or *CSS* +4) | same |
| CSS cost | about **28–30 lines** (the limit): drop the coloured tile hovers first if needed | same |

**Not carried to Squarespace:** the theme switcher, the `?theme=` links and the `data-theme` attribute are prototype tools only.

Fluid Engine desktop grid is **24 columns**; every position below uses it (e.g. "cols 9–20" = 12 columns). After desktop, switch to the **mobile view** and arrange blocks for 390px as described under each section. Fluid Engine keeps a separate mobile layout.

---

## 1. Pages and navigation

| Page | Type | In navigation | Password |
|---|---|---|---|
| Home | Regular page | (logo link) | No |
| Projects | **Regular page** (public), see §3 | "Projects" | No |
| About, Contact | Anchor links to sections on Home: `/#snippets` (Snippets About My Life), `/#contact` | "About", "Contact" | — |
| Case studies | **Portfolio page** "Case studies" (URL `/projects-private`), **Not linked**, four project pages inside | — | **Yes**, one password (§5) |

Header (*Edit Site Header*): layout **logo/site title left, navigation right**; site title "Yasmin Bajwa" as text, 15px; nav 15px; style **Solid, White**; a hairline under the header (header border, if her template offers it; **verify**; otherwise CSS line 1).

---

## 2. Custom CSS (Website → Pages → Custom code → Custom CSS)

The complete list: **20 lines** (15 from round 3, 3 for the discipline panels, 2 for the logo tiles).

```css
/* 1  hairline under the header, if the template has no header border setting */
.header{border-bottom:1px solid rgba(17,17,17,.14)}
/* 2-3  captions and labels: small caps, 62% ink (Paragraph 3 in Site Styles covers text blocks; this covers image captions) */
.image-caption p,.image-caption{font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:rgba(17,17,17,.62)}
/* 4  muted list markers in her bullet lists */
.sqs-html-content li::marker{color:rgba(17,17,17,.62)}
/* 5-6  A7 numbered lists (Findings, Impact, Littelfuse audit): hairline between items */
.sqs-html-content ol{padding-left:0;list-style-position:inside;border-top:1px solid #111}
.sqs-html-content ol > li{padding:14px 0;border-bottom:1px solid rgba(17,17,17,.14)}
/* 7  square corners everywhere (buttons, images, video) */
.sqs-block-button-element,.fluid-image-container,.video-player,.sqs-video-wrapper{border-radius:0!important}
/* 8-15  lock screen (§5); class names from community examples, NOT verified here: check each in the browser inspector */
.sqs-slide-container input[type="password"]{border:0!important;border-bottom:1px solid #111!important;border-radius:0!important;background:transparent!important;letter-spacing:.12em}
.sqs-slide-container input[type="password"]:focus{border-bottom-width:2px!important;box-shadow:none!important}
.sqs-slide-container button,.sqs-slide-container input[type="submit"]{border-radius:0!important;background:#111!important;color:#fff!important;border:1px solid #111!important}
.sqs-slide-container .error,.sqs-slide-container .form-error{color:rgba(17,17,17,.62)!important;font-size:14px!important;animation:none!important}
.sqs-slide-container .sqs-slide-layer-content{max-width:560px;margin:0 auto}
.sqs-slide-container h1,.sqs-slide-container h2{font-weight:400!important;letter-spacing:-.025em}
.sqs-slide-container a{text-decoration:underline;text-underline-offset:.22em}
.sqs-slide-container .sqs-slide-layer{background:#fff}
/* 16-18  A10 discipline panels: every image always visible under a 45% black overlay; hover lightens it to 30% (300ms).
   brightness(.55) is exactly a 45% black layer; .7 is 30%. Fluid Engine blocks can't take custom classes, so use each
   block's own class from the inspector: I1-I4 = image blocks' wrappers (.fe-block-yui_3_17_2_1_…), T1-T4 / N1-N4 = name and "01"-"04" text blocks. */
.I1 img,.I2 img,.I3 img,.I4 img{filter:brightness(.55);transition:filter .3s ease}
.I1:hover img,.I2:hover img,.I3:hover img,.I4:hover img{filter:brightness(.7)}
.T1,.T2,.T3,.T4,.N1,.N2,.N3,.N4{pointer-events:none}
/* 19-20  logo tiles (homepage project rows + Projects page): the light ground behind each transparent logo plate, darker on hover.
   .L = the two sections, e.g. section[data-section-id="…"] (copy each section's ID from the inspector; list both, comma-separated). */
.L .fluid-image-container{background:#F4F3F0;transition:background-color .3s}
.L .fluid-image-container:hover{background:#ECEAE5}
```

**How lines 16–18 work.** Each panel is a **Shape** block (the hairline outline, at the back), an **Image** block filling the panel (Phase 2: her snippet photos `snippet-15`, `-13`, `-18`, `-06`, set to Fill; no case-study images before the password) and two **Text** blocks on top ("0N" at the top, her skill name at the bottom). The section uses the **Ink** theme, so the names are white natively. Line 16 puts a 45% black overlay on every image, always, on desktop and phones. Line 17 lightens it to 30% while the pointer is over a panel. Line 18 lets the pointer pass through the text blocks to the image. Nothing appears or disappears: the image, number and name are always visible. To find a block's class, right-click it → *Inspect* and copy the `fe-block-…` class from the wrapper `div`. **Verify** once in the browser. If line 17 doesn't fire in her template, delete it: the panels still read correctly at rest.

**Lines 19–20, logo tiles.** Each tile is an **Image** block showing a transparent logo plate (`site/assets/img/logos/plate-*.png`, 1200×800, 3:2). The logo is already sized for equal visual weight inside the plate, with a 121px transparent margin, which is 32px at the homepage tile size (316px wide). Line 19 paints the light ground behind it; line 20 darkens the ground to `#ECEAE5` on hover. Squarespace can't make a whole row one link, so the hover is on the tile itself. **Verify** once in the browser.

Everything else is Site Styles or block settings. **Not needed:** code blocks, JavaScript, plugins.

---

## 3. Homepage and Projects page

### Home: sections in order

| # | Reference | Section | Fluid Engine blocks (desktop, 24 cols) | Mobile (390px) |
|---|---|---|---|---|
| 1 | **A9 + A8** hero | Blank section, theme White, padding M | **Text** "Hi, I'm *Yasmin.*" (H1) cols 1–14, rows 1–7. **Text** "About Me" (bold paragraph) + her paragraph (P2) cols 1–12, under it. **Button** "View Projects →" (outline) → `/projects`, cols 1–4. **Image** headshot 4:5, cols 15–19, caption "Digital Exhibit Designer — The Henry Ford". **Facts**: four **Text** blocks (label in P3 + value) separated by **Line** blocks, cols 21–24; "BASED IN: United States". | Headshot first, then greeting, text, button, facts. |
| 2 | Hairline | Section divider (or a full-width **Line** block at the top of section 3) | 1px, `#111` at 14%, full width. **The round-3 photo strip is removed.** | — |
| 3 | **Snippets About My Life** | Blank section, theme **Stone**, padding L, anchor link `snippets` | Left, cols 1–10: **Text** "Snippets About My Life" (Heading 3), **Text** her second About paragraph (P1, 40px), **Line**, **Text** "HISTORY · FASHION · ART" (12px, 500, tracking 0.24em, uppercase). Right, cols 13–24: the slideshow, 4:5, autoplay 5 s (see *Snippets slideshow* below). | Slideshow first, full width, then the heading, text and tags. |
| 4 | **A10** four disciplines | Blank section, **content width Full**, no padding, section height ~60vh | Four equal columns (cols 1–6, 7–12, 13–18, 19–24). Each: **Shape** (outline, at the back), **Image** filling the panel (Phase 2: `snippet-15` installation, `snippet-13` robotic head, `snippet-18` measuring tape, `snippet-06` mural; Fill; no case-study images before the password), **Text** "01"–"04" at top (13px, muted) and her skill name at the bottom (28px), **in her order**. All four images always visible under a 45% black overlay; hover lightens it to 30% (CSS §2 lines 16–18). Section theme **Ink** (names white). | 2 × 2 panels at 42vh, same 45% overlay. |
| 5 | **A3** projects | Blank section, White, anchor link `projects` | **Text** "Projects" (H2) cols 1–12, link "All projects →" cols 20–24. Then per project a row: **Line** (full width), **Text** number + title cols 1–10, **Text** her Role line + "PASSWORD PROTECTED" cols 12–17, **Image** logo tile cols 19–24, block sized exactly 3:2: `logos/plate-the-henry-ford.png`, `plate-itc.png`, `plate-rhode-island-doh.png`, `plate-littelfuse.png` (colour, the default; the `plate-*-ink.png` files are option b). CSS lines 19–20 add the ground and hover. Title, image and link all go to the project's URL. (A whole row can't be one link in Fluid Engine; title and image are.) | Image, then title, then role. |
| 6 | Contact | Blank section, theme Stone, anchor link `contact` | **Text** "CONTACT" (P3), **Text** "Let's create something people will remember." (H2) cols 1–14, then three hairline rows in the facts-column pattern (a **Line**, a P3 label, the value at 17px) cols 1–10: EMAIL `yasminbajwa248@gmail.com` → `mailto:yasminbajwa248@gmail.com`; PHONE `(313) 979-2205` → `tel:+13139792205`; LINKEDIN → her profile URL (pending). No icons. **No résumé link** (removed in Phase 2). | Stacked. |
| — | Footer | Site footer | "© Yasmin Bajwa" left (no year), "Back to top ↑" right (link to `#`). | — |

### Snippets slideshow (section 3)

| Setting | Value |
|---|---|
| Section | **Add section → Gallery → Slideshow: Simple**; theme Stone to match the text above it. |
| Aspect ratio | **4:5**. |
| Autoplay | **On**, slide duration **5 seconds**. |
| Navigation | Arrows on; dots/pagination on if her template offers them (**verify**: the options differ by template). Captions **off**. |
| Transition | Squarespace's own fade. The prototype uses a 400ms crossfade; the native timing may differ slightly (**verify**). |
| Images | Upload `site/assets/img/snippets/snippet-NN.jpg` in the order below. Slideshow: Simple **fills** the frame, so the 5 landscape photos (01, 02, 03, 04, 10) are supplied already letterboxed on `#F4F3F0` at 4:5, so they show whole. The 16 portrait photos are 3:4, and the 4:5 frame trims about 6% top and bottom. |
| Order | 20 (column install) · 06 (mural) · 09 (pastries) · 11 (hat exhibit) · 01 (Violins of Hope) · 19 · 10 · 13 · 12 · 07 · 03 · 14 · 05 · 15 · 02 · 16 · 08 · 17 · 04 · 18 · **21 last** (the handwritten note: publish only once the client confirms). |
| Editing | She adds, removes and reorders photos in the gallery panel by dragging. **For a new landscape photo**, either letterbox it to 4:5 first (like the five here) or accept the crop. |

**Layout note.** A Gallery section is a whole section, so the text-left / slideshow-right arrangement is two sections: the text in a Blank section (cols 1–10), then the Gallery section. For a true side-by-side, use a **Gallery block** (Slideshow) inside the Blank section, cols 13–24, with the same settings (**verify** that her plan offers the Gallery block in Fluid Engine).

### Projects page (A13)

Squarespace **can't** show the password-protected Portfolio's grid publicly: locking a Portfolio page locks its grid page too. So **Projects is a regular page**:
- **Text** "Projects" (H2);
- four **Image** blocks, the same logo tiles as the homepage (`logos/plate-*.png`, blocks at exactly 3:2, CSS lines 19–20), in a 2 × 2 grid (cols 1–12 / 13–24), each with a **Text** block beneath: "01 · PASSWORD PROTECTED", her title, her Role line;
- image and title link to the project page.

**No filter pills.** Portfolio pages have no native filtering, and the brief made them optional.

---

## 4. Case-study template (one Portfolio project page, filled four times)

Each project page in the Portfolio is built from ordinary sections.

| # | Reference | Section | Blocks (desktop) | Notes |
|---|---|---|---|---|
| 0a | **A1** cover, **photo** (Jackson Home, Power & Energy) | Blank section, **content width Full**, height L (≈16:7), **background image** = `r3-cover-r01/r02-16x7.jpg`, overlay **#111 at 38%** | **Text** her title (H2, 72px, white) bottom-left, cols 1–12. | As built in round 3. Mobile: image, then the title below in ink. |
| 0b | **A4** meta panel (photo covers) | Same section as 0a | **Shape** block (white rectangle, no stroke) cols 14–24, lower rows, overlapping the section's bottom edge; on it **three columns** of **Text** blocks, each under a **Line**: ROLE (her Role line), METHODS (her Methods line), SETTING. **No YEAR** (removed in Phase 2). | Mobile: panel below the cover, the three stacked. |
| 0c | **A1** header, **document** (Rhode Island, Littelfuse) | Blank section, theme **White**, **no background image** | **Text** her title (H2, 72px, ink) cols 1–13, bottom-aligned; the meta table in three columns (ROLE, METHODS, SETTING as **Text** + **Line** blocks; no YEAR) cols 15–24. After the chapter index (row 1), a **Full plate**: one **Image** block cols 1–24, captioned "FIG. 01 — …": Rhode Island `tiles/r5-ri-five-screens--nat-p48.jpg` (the five 401 Health screens), Littelfuse `tiles/r04-journey-full--nat-p48.jpg` (the journey map). The tiles already hold the `#F4F3F0` ground and the **48px** padding. | Title, meta, index, then the plate. |
| 1 | **A1** chapter index | Blank section, White | One **Text** block, full width, between two **Line** blocks: "01 Project Overview · 02 The Challenge · …", each linked to `#ch-1`, `#ch-2`… | Each chapter section gets its **Anchor link** (`ch-1`…) in *Edit Section → Design*. |
| 2 | **A2 + A3** chapter | One Blank section per chapter, White | **Text** "01" (P3) + chapter title (H3) cols 1–6. **Text** her copy cols 9–20: paragraphs, her sub-headings as Heading 4 with a **Line** block above, bullets as real (nested) lists. **Images** where her doc places them, cols 9–24 (or 1–24 for plates), caption "FIG. nn — …" below. | Mobile: title above text. |
| 3 | **A4** stats strip | Inside Jackson Home "Research Methodology" | Three **Text** blocks cols 1–8 / 9–16 / 17–24 under a **Line**: "60%" (72–96px), "Strollers" (H4), her characteristic text; the column heads as P3 labels. | Stacked. |
| 4 | **A5 / A14** spread | Jackson Home "Baseline Assumptions" | **Image** (plan with paths) cols 1–11; chapter number/title and her list cols 14–24. | Plan first. |
| 5 | **Bento modules** | Every image and video (§4a) | One of the six modules, built once and saved (heart icon), then reused. `MODULE-MAP.md` lists every tile, its module and its file. | See §4a. |
| 7 | **A7** findings / impact | Jackson Home Findings & Impact; Littelfuse audit | Chapter title + her items as a numbered list (CSS lines 5–6 add the hairlines); Findings closes with a Full plate. | — |
| 8 | Reflection | Blank section, theme Stone, padding L | **Text**, centred, 28px italic, cols 5–20: her paragraph(s) verbatim. | — |
| 9 | **A5** prev / next | Blank section, White | **Line**, then three **Text** blocks: "← Previous project" + title (cols 1–8), "All projects" (cols 10–15, centred), "Next project →" + title (cols 17–24, right-aligned). | Stacked. |

**Figure captions** are listed in COPY-CHECK.md ("Added captions") for Yasmin to approve.

### 4a. The six bento modules (round 4)

Build each once on the Jackson Home or Power & Energy page, **save it** (heart icon), then add it from *My saved sections* wherever `MODULE-MAP.md` says. All positions on the 24-column grid. Every tile gets a caption "FIG. nn — …" (P3). **Tiles:** use the file in `site/assets/img/tiles/` named in MODULE-MAP. Drawings, screens and documents are already whole on `#F4F3F0` with 24px padding inside the file. Size the image block to the tile's ratio (or set the gallery's aspect ratio to match) and nothing gets cropped. Photographs may be cropped to the module ratio. The lightbox opens the tile; to open her full-resolution original instead, set the block's *Clickthrough URL* to the source file.

| Module | Build | Mobile |
|---|---|---|
| **Plate pair** | Fluid Engine: **Image** cols 1–16 (3:2) + **Image** cols 17–24 (3:4), tops and bottoms aligned; captions below. Mirrored (tall on the left) where that keeps her figure order. | Stacked, wide first. |
| **Board 2×2** | **Gallery section → Grid: Simple**, 2 columns, aspect ratio **1:1**, spacing 24px, *Lightbox* on, captions below (or four image blocks cols 1–12 / 13–24). | 1 column. |
| **Board 1+3** | Fluid Engine: **Image** cols 1–16 spanning the height of the three small ones; three **Image** blocks cols 17–24 stacked (3:2). | Stacked, large first. |
| **Strip** | **Gallery section → Grid: Simple**, 3–5 columns at the tile ratio (column sides: 9:32), captions *above* (in Fluid Engine, a P3 text block above each image). | 2 columns. |
| **Full plate** | Fluid Engine: one **Image** block cols 1–24 (tile ratio 16:10 or wider). | Full width. |
| **Video panel** | **Video** block cols 1–16 (upload the MP4 from `site/assets/video/`, thumbnail `poster-*.jpg`, controls on); **Text** block cols 17–24 bottom-aligned: a **Line**, "FIG. nn — …" (P3) and "Running time 0:48". Vertical videos (final set-up, app reviews): the video block centred in cols 1–16 on a Stone section, max ~78% of the screen height. | Video full width, caption below. |

**Rules:** 24px gutters; never more than two modules of the same type in a row (checked automatically, see MODULE-MAP). Her figures keep her order. Exceptions are listed in MODULE-MAP: figs 6 and 9 moved into the Scenario Testing board; the plan with paths stays in the Baseline spread; the five column sides form a 5-tile strip.

### How she edits projects

1. **Build Room 01 completely** as a project page inside the "Case studies" Portfolio.
2. **Save each reusable section** (cover, meta panel, chapter index, A7 list, reflection, prev/next): hover → **heart icon** → *Your account* → name it. Saved sections appear under **My saved sections** when adding a section. They are snapshots: editing a saved copy doesn't change the others.
3. **Duplicate** the finished project page three times (*Pages → project ⋯ → Duplicate*, **verify** in her account) and swap in each project's copy and images, following COPY-INVENTORY.md and `content/copy.json`.
4. **To add a project later**, she duplicates any project page and edits it. Every element is a standard text, image, video, line, shape or button block she can click and change.
5. **Password:** set it **once on the Portfolio page** (*Page settings → Password*). It protects all four project pages. Squarespace can't give individual projects their own passwords, so this is one shared password.

---

## 5. Lock screen (prototype: `site/private-view.html`)

One lock screen design serves the whole site (*Page settings of the protected page → Lock Screen → Customize*, or *Design → Lock screen*, depending on the account; **verify**).

| Setting | Value |
|---|---|
| Layout | Centred |
| Media → Background image | **None** (Phase 2: no case-study image may show before the password). White ground (CSS line 15). |
| Branding & text → Site title | "Yasmin Bajwa" (top) |
| Headline | Projects are shared *by invitation.* (56px, Instrument Serif 400; the heading font since round 6) |
| Body | Enter the password to continue. (15px) · then a link line: **No password? Email Yasmin →** (`mailto:` her address) |
| Lock icon | Off |
| Colours | Background `#FFFFFF`, text `#111111` |
| Password field | Hairline, bottom border only (CSS 8–9) |
| Button | "Enter", solid ink, square (CSS 10) |
| Wrong password | Squarespace shows its own message; CSS 11 sets it to plain 14px text at 62% ink with no shake. The prototype writes "Incorrect password."; her site will show Squarespace's exact wording (**verify**). |

The prototype's wrong-password state is `private-view.html#wrong` (pure CSS `:target`, no script).

---

## 6. Native-only checklist

| Page | Section | Built from | Custom CSS |
|---|---|---|---|
| Home | Hero, facts | Text, Image, Button, Line | — |
| Home | Hairline | Section divider / Line | — |
| Home | Snippets About My Life | Text, Line, Gallery section (Slideshow: Simple) | — |
| Home | Four disciplines | Shape, Image, Text (Ink theme) | 16–18 |
| Home | Projects rows | Text, Line, Image (logo plates) | 19–20 |
| Home | Contact / footer | Text, Line, footer | — |
| Projects | Grid | Image (logo plates), Text | 19–20 |
| Case study | Cover + meta | Section background + overlay, Text, Shape, Line | — |
| Case study | Chapter index | Text + anchor links, Line | — |
| Case study | Chapters | Text (lists), Line, Image, Video | list markers (4) |
| Case study | Stats strip, spread | Text, Line, Image | — |
| Case study | Six bento modules | Image, Gallery section (Grid: Simple), Video, Text, Line | — (ground and padding are in the tile files) |
| Case study | A7 lists | Text (ordered list), Image | 5–6 |
| Case study | Reflection, prev/next | Text, Line | — |
| Lock screen | — | Native lock screen | 8–15 |
| All | Square corners | Block settings | 7 |

**Simplified for Squarespace:**
- **Whole-row links on the homepage** become title-and-image links.
- **No row hover tint** (Fluid Engine has no hover state for a group).
- **The Projects page is a regular page, not the Portfolio grid** (the grid locks with the password).
- **No filter pills.**
- **One shared password and one lock-screen design.**
- **The five column-art panels are a 2-up grid on mobile, not a swipe row.**

## Sources
- [Page passwords – Squarespace Help Center](https://support.squarespace.com/hc/en-us/articles/205814618-Page-passwords)
- [Portfolio pages – Squarespace Help Center](https://support.squarespace.com/hc/en-us/articles/360035611791)
- [Password protect individual portfolio projects (Squarespace Forum)](https://forum.squarespace.com/topic/175445-password-protect-lock-individual-portfolio-project-pages/)
- [Creating anchor links – Squarespace Help Center](https://support.squarespace.com/hc/en-us/articles/207135178-Creating-anchor-links)
- [Save and reuse page sections – Squarespace Help Center](https://support.squarespace.com/hc/en-us/articles/46489432825613-Save-and-reuse-page-sections)
- [Customizing a lock screen – Squarespace Help Center](https://support.squarespace.com/hc/en-us/articles/205815178-Customizing-a-lock-screen)
- [Lock Screen 7.1 customisation (Squarespace Forum)](https://forum.squarespace.com/topic/205522-lock-screen-71-customisation/)

---

## 7. Wireframes for client approval (`wireframes/`)

Greyscale HTML wireframes of all seven pages (Phase 2: slideshow frame, logo tiles, three-column meta), generated from the same build (`tools/build_wireframes.py`), so structure and proportions match the design exactly. Every image and video is a grey box labelled "IMAGE — FIG. n" / "VIDEO — FIG. n" (or what it is, e.g. "IMAGE — PORTRAIT"). All her copy is in place and the hairlines are kept. There are no photos and no colour. Each file is **standalone**: CSS and the two web fonts are inline, with no external files, so the files can be downloaded and sent as they are. `wireframes/index-wireframes.html` links all seven.
