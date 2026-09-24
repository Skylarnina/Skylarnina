# Squarespace build notes: "The Exhibition"

How to build the prototype in `site/` on **Squarespace 7.1 with Fluid Engine**. It takes no custom JavaScript: the prototype's small script is only for the wireframe toggle, the lightbox and conveniences that already work without it.

Sources for platform facts are listed at the end. Anything marked **verify** is how I understand the current editor; check it in her account before building on it.

---

## 0. Before you start

| Item | Setting |
|---|---|
| Plan | Any plan with the **Custom CSS** panel. Nothing here needs JavaScript. JavaScript in Code Blocks, and Lock Page code injection, need **Core or higher**. The per-room lock title (§5) is the only optional extra that needs it. |
| Fonts | **Instrument Serif** (Google; regular + italic) for headlines, the name and all numerals. **Neue Haas Grotesk Text** (Adobe, if listed in the font picker) or **Inter Tight** (Google) for body, labels and nav. The prototype uses Inter Tight. Check both in *Site Styles → Fonts* before building. If Instrument Serif is missing from the picker, upload it as a custom font (it's open-licensed), or fall back to **Newsreader**. |
| Uploads | Everything in `site/assets/img/` and `site/assets/video/`, built by `tools/build_assets.py`. Upload the PNG cut-out (`portrait-cutout.png`), not the WebP. |
| Video | Upload the MP4s in `site/assets/video/` to Video blocks, or host them on Vimeo (the cleaner muted loop). All are already muted, H.264, ≤3.6 MB. |

## 1. Site Styles

**Colours → palette** (then *Colour themes*):

| Theme | Background | Text / headings | Accent / links | Used for |
|---|---|---|---|---|
| Lightest 1 | `#F3F0EA` | `#16140F` | `#8C2F1E` | Gallery ground: most sections |
| Light 1 | `#E9E4DB` | `#16140F` | `#8C2F1E` | Deeper wall: alternate sections, plates |
| Darkest 1 | `#141311` | `#F3F0EA` | `#D0664F` | Black box: home hero, rooms carousel, room headers, black-box gallery, next room, lock screen |

`#D0664F` is archive red lifted for dark grounds. `#8C2F1E` is only 2.3:1 on `#141311`; `#D0664F` is 5.0:1.

**Fonts → sizes** (desktop / mobile):

| Style | Font | Size | Line height | Tracking |
|---|---|---|---|---|
| Heading 1 (home name) | Instrument Serif | 22vw → set 300px / 84px | 0.8 | 0.12em |
| Heading 2 (room titles, section titles) | Instrument Serif | 88px / 44px | 0.96 | −0.01em |
| Heading 3 (chapter titles) | Instrument Serif | 56px / 34px | 1.02 | 0 |
| Heading 4 (numerals) | Instrument Serif | 152px / 88px | 0.86 | −0.02em |
| Paragraph 1 (pull quotes, About) | Instrument Serif | 30–40px / 24–28px | 1.2 | 0 |
| Paragraph 2 (body) | Inter Tight / Neue Haas | 17px / 16px | 1.65 | 0 |
| Paragraph 3 (labels) | Inter Tight / Neue Haas, 500, UPPERCASE | 11px | 1.4 | 0.14em |

**Buttons:** Primary = pill, fully rounded, 12px, 500, uppercase, 0.16em, solid ground-on-ink (on dark: ink-on-ground). Secondary = outline pill.

**Animations** (*Site Styles → Animations*): style **Fade**, speed **Slow**, **gentlest** setting. Background scroll effects: **Zoom** on the room-header covers only. No other effects.

**Images:** Lightbox **on** for plate image blocks (*Image block → Design → Clickthrough → Lightbox*).

## 2. Custom CSS (Website → Pages → Custom Code → Custom CSS)

Paste this once. Class names like `#rooms-carousel` go on Code Blocks. Section-level rules use **section IDs**: get them with the free "Squarespace ID Finder" extension, and replace the `[data-section-id="…"]` placeholders.

```css
/* tokens */
:root{--ground:#F3F0EA;--wall:#E9E4DB;--ink:#16140F;--accent:#8C2F1E;--accent-dark:#D0664F;--bb:#141311}

/* labels: 66% ink passes WCAG AA; the brief's 45% does not */
.sqs-block-html p.label,.label{font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:rgba(22,20,15,.66)}

/* PLATES: drawings sit ON the wall (multiply makes the white paper disappear) */
.plate-drawing .sqs-block-image img,
[data-section-id="PLATES_SECTION"] .image-block-wrapper img{mix-blend-mode:multiply}

/* PINNED SKETCHES (Room 02): the only playful move */
.pinned-a img{transform:rotate(-1.5deg)} .pinned-b img{transform:rotate(1.2deg) translateY(28px)}

/* P4 STRIPS: 55% black-box overlay that lifts to 35% on hover */
[data-section-id="STRIP_1"] .section-background-overlay,
[data-section-id="STRIP_2"] .section-background-overlay,
[data-section-id="STRIP_3"] .section-background-overlay,
[data-section-id="STRIP_4"] .section-background-overlay{background:#141311!important;opacity:.55!important;transition:opacity .6s}
[data-section-id^="STRIP_"]:hover .section-background-overlay{opacity:.35!important}

/* P2 ARCH WINDOWS (Room 02): pill-shaped image blocks */
.arch .sqs-block-image .image-block-wrapper,.arch .fluid-image-container{border-radius:999px;overflow:hidden}

/* P9 CIRCLES: image blocks set to a circle; hairline circles are empty blocks */
.circle-photo .fluid-image-container{border-radius:50%;overflow:hidden}
.circle-line .sqs-block-content{aspect-ratio:1;border:1px solid #16140F;border-radius:50%}

/* P12 ROOM INDEX: a Code Block, pinned to the right edge on desktop */
@media (min-width:768px){.room-index{position:fixed;right:32px;top:50%;transform:translateY(-50%);z-index:30}}
@media (max-width:767px){.room-index{display:none}}

/* hide Squarespace's own portfolio pagination (we use "Next room") */
.item-pagination{display:none}
```

The two carousels (§3.3 and the room signatures) and the room index are **Code Blocks** with HTML + CSS only. Copy their markup and CSS from `site/index.html` and `site/assets/css/exhibition.css` (the `.depth`, `.swap`, `.pills`, `.vindex` rules).

## 3. Homepage: one page, five sections

Fluid Engine's desktop grid has **24 columns**; the prototype's 12-column grid doubles (prototype col 1–7 = FE col 1–14). Mobile has 8 columns and its own layout: arrange mobile in the mobile view after desktop.

### 3.1 Hero: P5 + P8
- **Section:** blank, theme Darkest 1, height *Large* (≈100vh), content width full.
- **Blocks (desktop):**
  1. Text block "YASMIN" (Heading 1, centred), FE cols 3–22, rows 3–9. **Arrange → Send to back.**
  2. Image block `portrait-cutout.png`, FE cols 8–17, rows 5 → bottom edge, fit *Contain*, bottom-aligned. **Arrange → Bring to front** (above the text). Its head covers the lower half of the S and M.
  3. Text block (spaced caps + a `—` hairline line + serif paragraph), FE cols 1–7, lower rows.
  4. Button block "View Projects →" (primary pill) under it.
  5. Code Block `.vindex`: 01–04 links, FE cols 23–24, middle rows.
- **Mobile (flat fallback):** hide blocks 1–2 on mobile (block *Visibility → Desktop only* where available; otherwise make them 1 row tall and move them off-canvas). Add a **mobile-only** image block with `portrait-4x5.jpg` at the top, then the YASMIN text at 84px, then the text and button.

### 3.2 Four disciplines: P4
- **Four sections** stacked with **0 padding**, each: *Section background → Image* (`strip-exhibit.jpg`, `strip-ux-design.jpg`, `strip-ux-research.jpg`, `strip-marketing.jpg`), height **Small** (≈26vh desktop, ≈18vh mobile), overlay per the CSS above.
- One centred text block per section (Paragraph 3, 24px, tracking 0.5em), plus a left numeral text block (italic serif, accent) and a right note. Link the whole text block to the related room.
- Above them, a slim section with the two labels "Four disciplines" / "In the order I practise them".

### 3.3 The rooms: P3
- **Section:** theme Darkest 1. Title and intro text blocks (FE cols 1–14 and 17–24).
- **Carousel = a Code Block** (HTML + CSS, **no JS**). A horizontal scroll-snap row of four linked covers, plus CSS **scroll-driven** depth (neighbours at 70% scale / 50% opacity, rotated back; the centred card framed in accent red). This works on every plan.
  - Swipe and trackpad scroll work everywhere. The number/arrow links are plain `#anchors`, which scroll the row. Without JS the page may also shift vertically to bring the row into view; `scroll-margin-block:20vh` keeps that small.
  - Browsers without scroll-driven animations (Firefox today) show equal-size cards, still in a clean swipe row.
- **Simpler fallback if the Code Block is unwanted:** *List section → Carousel* (arrows + swipe built in, "items per row" 3). The depth scaling can't be done there (no "active" state exposed to CSS): equal cards.

### 3.4 Beyond the screen: P9
- **Section:** theme Light 1.
- **Circles:** two *empty text blocks* with class `circle-line` (hairline circles, CSS above), overlapping one *image block* with class `circle-photo` (personal photo; placeholder until it arrives). Labels are small text blocks placed on top. Overlap them freely in Fluid Engine (cols 1–13).
- **Right side** (cols 15–24): label, About text (Paragraph 1, 30px), "HISTORY · FASHION · ART", the 01–04 list (text block with hairline rules via CSS or a List block), "Download résumé" link to the PDF (upload via *Link → File*).
- **Mobile:** the circles stack vertically, 58% width, overlapping by about 18vw.

### 3.5 Contact: P8
- **Section:** background image `r02-column-installed.jpg`, overlay Darkest 1 at **68%**, height *Large*, content centred.
- Blocks: spaced caps "Contact"; heading "Let's make something *people remember.*" (Heading 2, tracking 0.06em); a thin line block; email as a large underlined link; a caps row: LinkedIn · Résumé · Instagram.

## 4. Projects: the four rooms

### 4.1 Collection
- Create a **Portfolio** page named **Rooms** (URL `/rooms`). Add four items: `room-01-jackson-home`, `room-02-power-energy`, `room-03-rhode-island`, `room-04-littelfuse`.
- Thumbnails: `r0N-cover-4x5.jpg`. The Portfolio index page itself isn't linked from the nav: the homepage carousel is the index. Nav: Work → `/#rooms`, About → `/#about`, Contact → `/#contact`.

### 4.2 One template, four fillings
Squarespace has no locked item template, so build **Room 01 completely**, then **duplicate the item** three times (*Portfolio → item ⋯ → Duplicate*, **verify**) and swap the content. Save the header, black box and next-room sections as **Saved Sections** so all rooms stay identical.

| # | Section (pin) | Squarespace build |
|---|---|---|
| — | Room index (P12) | Code Block `.vindex` in the header section, class `room-index` (fixed by the CSS above). The current room gets `aria-current="page"` in its own copy of the markup. |
| 1 | Header (P10 + P12) | Section background = `r0N-cover-16x9.jpg`, overlay Darkest 1 at **55%** (= cover at 45%; use 70% for Room 03 and 82% for Room 04, whose covers are white documents), background scroll effect **Zoom**. Blocks: title as three lines in Heading 1 with the accent word in italic + link colour (select the word → *Text colour → accent*), side text + two pill buttons (Watch → `#film`, signature → `#signature` anchor), meta line as a caps text block with `|` separators. |
| 2 | Wall label (P6) | Five image blocks side by side with staggered heights (FE lets each block be a different height), each with an overlay text block on top: label + value. Image block *Design → Overlay* at 58%, or a darkened export. |
| 3 | Overview | Two columns: pull sentence (Paragraph 1, 40px) cols 1–12; body cols 15–24. |
| 4 | Challenge | Theme Light 1. Constraints as four small text blocks; each "How might we" line its own text block (italic, 56px), alternately left and right aligned. |
| 5 | Signature | Per room, see 4.3. |
| 6 | Plates / data walls | Image blocks (Lightbox on) with a caption text block "FIG. 07 — …" beneath. Drawings: class `plate-drawing` (multiply). Data walls: four small image blocks in a 2×2 plus one numeral text block (Heading 4). Figures are numbered by hand; the prototype numbering is final. |
| 7 | Black-box gallery (P12) | Theme Darkest 1. Video block(s) with the poster `poster-*.jpg` as thumbnail; the round play mark is Squarespace's own play icon (restyle round via CSS: `.video-player .sqs-video-icon{border-radius:50%}`, **verify** class). Caption + running time as a text block. |
| 8 | Findings / impact | Four numeral text blocks in a 2×2 with hairline rules (Line blocks), then a list text block with ✓ characters in accent. |
| 9 | Reflection | Theme Light 1, one centred italic text block, max width ≈ 60ch (cols 5–20). |
| 10 | Next room (P11) | Section background = next room's `-16x9` cover, overlay 50%. Three image blocks overlapping in the centre: the next room large (4:5) with a 1px accent border (image block → *Design → Stroke*, **verify**), the other two smaller and behind. Each links to its item. A "← Back to all rooms" link. |

### 4.3 Room signatures
- **Room 01, "The visitor's route" (P6):** a Line block (vertical) down the middle, or one text block with a CSS left border; seven rows, each with a text block on one side and two overlapping image blocks (plan crop + simulation still) on the other, alternating. Red dot markers = small accent-colour shape blocks, **or** a `●` character in accent. Archetype circles (P9): three empty text blocks with class `circle-line` sized 56% / 40% / 23% of the column (areas proportional to 60 / 30 / 10), overlapping, with numerals inside.
- **Room 02, "The column" (P2):** section background `r02-column-installed-b.jpg`, overlay 74%. Five image blocks (`r02-side-*.jpg`) with class `arch` (pill radius), the middle one taller with an accent outline, the 2nd and 4th raised about 28px. Captions below. Mobile: a horizontal row of the five, swipeable (FE mobile: place them side by side and let the section scroll, or use a *Gallery section → Slideshow: Reel*).
- **Room 03, "The app" (P1 + P7):** section theme Light 1 with background `r03-desk-portal.jpg` at a very low opacity (overlay Light 1 at 94%). Pill switcher + cards = a Code Block (same `.pills` + `.swap` markup and CSS, **no JS**: pills are `#anchors`). **Fallback:** *Gallery section → Slideshow* with captions ("Vaccination status", "Multilingual"…). The pill switcher then becomes the slideshow's own arrows. The "+23%" numeral must always read "target".
- **Room 04, "Three kinds of user" (P7):** as Room 03, dark theme; Engineering starts centred (it's the middle card).

## 5. Password gate and lock screen (P8 + P1)

**Protect the case studies only:** open the **Rooms** portfolio page → *Settings → Password* → set one password. The homepage stays public. The four items share the collection's password (Squarespace can't set a separate password per portfolio item; one password matches "shared by invitation").

**Design the lock screen** (*Pages → the Rooms page → Lock screen*, or *Design → Lock screen* depending on the account; **verify**). Squarespace has **one lock screen design for the whole site**, so it can't show a different room title per room.

| Setting | Value |
|---|---|
| Layout | Centred / card |
| Media → Background image | `r01-plan-16x9.jpg` (the Jackson Home plan) |
| Styles → Background colour | `#141311` |
| Styles → Image overlay | `#141311` at **65%** (= the plan at 35%) |
| Branding & text → Headline | **PRIVATE VIEW — FOUR ROOMS** (generic, because the screen is sitewide) |
| Branding & text → Body text | "Case studies are shared by invitation. Enter the password to continue." |
| Lock icon | Off |
| Fonts | Headline: Instrument Serif, 36px, tracking 0.14em, uppercase; body: Inter Tight 15px |
| Colours | Headline and body `#F3F0EA`; field line `#F3F0EA` at 50% |

**Custom CSS for the lock screen.** The class names below are from Squarespace's 7.1 lock page; **verify** them in the browser inspector, because Squarespace changes them occasionally.

```css
/* card behind the form */
.sqs-slide-container .sqs-slide-layer-content,
.lock-screen .lock-screen-content{background:rgba(20,19,17,.85);border:1px solid rgba(243,240,234,.18);padding:56px;max-width:560px;margin:auto}
/* hairline password field */
.sqs-slide-container input[type=password]{background:transparent!important;border:0!important;border-bottom:1px solid rgba(243,240,234,.5)!important;border-radius:0!important;color:#F3F0EA!important;letter-spacing:.2em}
/* Enter pill */
.sqs-slide-container .sqs-button-element--primary,.sqs-slide-container button[type=submit]{border-radius:999px!important;background:#F3F0EA!important;color:#141311!important;letter-spacing:.16em;text-transform:uppercase;font-size:12px}
/* wrong-password message in archive red (lifted), no shake */
.sqs-slide-container .error,.sqs-slide-container .form-error{color:#D0664F!important;animation:none!important}
```

**What Squarespace can't do natively, and the closest match:**
- **Per-room title ("ROOM 01 — THE JACKSON HOME")** needs JavaScript in *Settings → Advanced → Code Injection → Lock Page* (Core plan or higher): read the requested URL and write the room name into the headline. Without it, use the generic headline above.
- **The "Ask Yasmin for access →" mailto line:** put it in the body text as a link, if the body field keeps links (**verify**); otherwise add it through Lock Page code injection, or leave the line as plain text with her email.
- **The wrong-password copy:** Squarespace shows its own message ("Incorrect password" or similar). The CSS above makes it calm and red, but the wording is Squarespace's own unless changed through code injection.

## 6. What was simplified for Squarespace

1. **Depth carousels (P3, P7):** CSS-only (scroll-snap + scroll-driven animation) inside a Code Block. Firefox shows equal cards. The native List-section fallback has no depth effect.
2. **Carousel arrows and pills without JS** are `#anchor` links; the page can nudge vertically when they are clicked.
3. **Lock screen:** one design sitewide, generic title; the per-room title needs code injection.
4. **Portfolio "template":** built once, duplicated, kept in sync with Saved Sections, since there is no locked template.
5. **Hero depth (P5):** exact on desktop. Mobile uses the flat layout (photo above, name below).
6. **Video play marks:** Squarespace's own icon, restyled round.
7. **The fixed room index (P12):** fixed with CSS; hidden on mobile.
8. **Room covers with callouts** are exported images (callouts can't be layered over a background image and stay aligned across breakpoints).

## 7. Accessibility checks already made
- Text contrast (WCAG 2.x, computed): ink on ground 16.2:1; muted text (72%) 6.9:1 on ground and 6.6:1 on wall; labels (66%) 5.6:1 on ground and 5.4:1 on wall (the brief's 45% measures 2.9:1, so it was raised); ground text on black box 16.3:1; muted and label text on black box 9.3:1 and 7.1:1; archive red `#8C2F1E` 7.3:1 on ground, 6.5:1 on wall, but only 2.3:1 on the black box, so dark sections use `#D0664F` (5.0:1). Text laid over photos (strips, headers) relies on the overlays; check each final photo in place.
- Every image has alt text in the prototype; copy it into each image block's alt field.
- Videos are muted and never autoplay with sound; each has a caption and a running time.

## Sources
- [Customizing a lock screen – Squarespace Help Center](https://support.squarespace.com/hc/en-us/articles/205815178-Customizing-a-lock-screen)
- [Lock Screen 7.1 customisation – Squarespace Forum](https://forum.squarespace.com/topic/205522-lock-screen-71-customisation/)
- [Code blocks – Squarespace Help Center](https://support.squarespace.com/hc/en-us/articles/206543167-Code-blocks)
- [Auto layouts (list sections) – Squarespace Help Center](https://support.squarespace.com/hc/en-us/articles/360057763852-Auto-layouts)
