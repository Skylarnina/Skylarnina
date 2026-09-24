# Squarespace build notes: Round 3

How to build the Round 3 prototype (`site/`) in **Squarespace 7.1 with Fluid Engine**, using only standard sections and blocks, Site Styles, and **16 lines of custom CSS** (§2). There is **no custom JavaScript** and **no Code Block used for layout**. The prototype itself has no JavaScript either, so what you see is what the native build can do.

Items marked **verify** are how I understand the current editor. Check each once in her account before relying on it. Platform sources are at the end.

---

## 0. Set-up

| Item | Setting |
|---|---|
| Template | Any 7.1 template; everything below is set per section. |
| Fonts (*Site Styles → Fonts*) | **Neue Haas Grotesk Display** (Adobe Fonts, in the Squarespace picker) for headings, paragraphs, buttons and navigation. If it isn't listed in her account (**verify**), use **Inter Tight** (Google), which is what the prototype uses. Weights 400 and 500 only, plus italic 400 for "*Yasmin.*". |
| Colours (*Site Styles → Colours*) | Palette: `#FFFFFF`, `#F4F3F0`, `#111111`. Two themes: **White** (background `#FFFFFF`, text `#111111`) and **Stone** (background `#F4F3F0`, text `#111111`). No accent colour; links `#111111`, underlined. |
| Buttons | Primary: **outline**, **square corners**, 1px, 14px text. The lock screen's Enter button is solid (§5). |
| Animations (*Site Styles → Animations*) | **Fade**, speed **Slow**. Nothing else: no scroll effects, no parallax. |
| Images | Every image block: *Design → Clickthrough: Lightbox* (native lightbox), **Caption: below**, no border, no shadow, **corner radius 0**. |

### Type scale (Site Styles → Fonts)

| Style | Desktop | Mobile | Used for |
|---|---|---|---|
| Heading 1 | 140px / 0.92, tracking −0.035em | 64px | "Hi, I'm *Yasmin.*" |
| Heading 2 | 72px / 1.02, tracking −0.03em | 40px | Page titles, cover titles, "Projects", contact line |
| Heading 3 | 40px / 1.08, tracking −0.02em | 30px | Chapter titles |
| Heading 4 | 20px / 1.3 | 20px | Her sub-headings ("Visitor Experience", "Ticketing Strategy"…) |
| Paragraph 1 | 40px / 1.25 | 26px | The centred statement (A9) |
| Paragraph 2 | 17px / 1.6 | 16px | All her body text, in a 12-column measure (~62ch) |
| Paragraph 3 | 11px / 1.45, **uppercase, tracking 0.08em**, colour 62% ink | 11px | Labels, captions, "FIG. 03 — …", "PASSWORD PROTECTED" |

Captions and labels use **62% ink, not 55%**. At 11px, 55% measures 4.4:1 on white, which fails WCAG AA; 62% passes at 5.2:1.

Fluid Engine desktop grid is **24 columns**; every position below uses it (e.g. "cols 9–20" = 12 columns). After desktop, switch to the **mobile view** and arrange blocks for 390px as described under each section. Fluid Engine keeps a separate mobile layout.

---

## 1. Pages and navigation

| Page | Type | In navigation | Password |
|---|---|---|---|
| Home | Regular page | (logo link) | No |
| Projects | **Regular page** (public), see §3 | "Projects" | No |
| About, Contact | Anchor links to sections on Home: `/#about`, `/#contact` | "About", "Contact" | — |
| Case studies | **Portfolio page** "Case studies" (URL `/projects-private`), **Not linked**, four project pages inside | — | **Yes**, one password (§5) |

Header (*Edit Site Header*): layout **logo/site title left, navigation right**; site title "Yasmin Bajwa" as text, 15px; nav 15px; style **Solid, White**; a hairline under the header (header border, if her template offers it; **verify**; otherwise CSS line 1).

---

## 2. Custom CSS (Website → Pages → Custom code → Custom CSS)

The complete list: **16 lines**.

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
/* 8-16  lock screen (§5); class names from community examples, NOT verified here: check each in the browser inspector */
.sqs-slide-container input[type="password"]{border:0!important;border-bottom:1px solid #111!important;border-radius:0!important;background:transparent!important;letter-spacing:.12em}
.sqs-slide-container input[type="password"]:focus{border-bottom-width:2px!important;box-shadow:none!important}
.sqs-slide-container button,.sqs-slide-container input[type="submit"]{border-radius:0!important;background:#111!important;color:#fff!important;border:1px solid #111!important}
.sqs-slide-container .error,.sqs-slide-container .form-error{color:rgba(17,17,17,.62)!important;font-size:14px!important;animation:none!important}
.sqs-slide-container .sqs-slide-layer-content{max-width:560px;margin:0 auto}
.sqs-slide-container h1,.sqs-slide-container h2{font-weight:400!important;letter-spacing:-.025em}
.sqs-slide-container a{text-decoration:underline;text-underline-offset:.22em}
.sqs-slide-container .sqs-slide-background-content{opacity:.08}
.sqs-slide-container .sqs-slide-layer{background:#fff}
```

Everything else is Site Styles or block settings. **Not needed:** code blocks, JavaScript, plugins.

---

## 3. Homepage and Projects page

### Home: sections in order

| # | Reference | Section | Fluid Engine blocks (desktop, 24 cols) | Mobile (390px) |
|---|---|---|---|---|
| 1 | **A9 + A8** hero | Blank section, theme White, padding M | **Text** "Hi, I'm *Yasmin.*" (H1) cols 1–14, rows 1–7. **Text** "About Me" (bold paragraph) + her paragraph (P2) cols 1–12, under it. **Button** "View Projects →" (outline) → `/projects`, cols 1–4. **Image** headshot 4:5, cols 15–19, caption "Digital Exhibit Designer — The Henry Ford". **Facts**: four **Text** blocks (label in P3 + value) separated by **Line** blocks, cols 21–24; "BASED IN: [pending client]" in italic until she answers. | Headshot first, then greeting, text, button, facts. |
| 2 | **A9** photo strip | Blank section, White | Five **Image** blocks, bottoms aligned, different heights: cols 1–5 (3:4), 6–10 (4:5.4), 11–14 (4:3.4), 15–19 (1:1.1), 20–24 (4:2.9). A P3 **Text** caption *above* each (A8). | 2 columns; the fifth image full width. |
| 3 | **A9** statement | Blank section, theme **Stone**, padding L, anchor link `about` | **Text** block, P1 (40px), centred, cols 6–19: her second About paragraph. | Full width, 26px. |
| 4 | **A10** four disciplines | Blank section, **content width Full**, no padding, section height ~60vh | Four equal columns (cols 1–6, 7–12, 13–18, 19–24), each a **Shape** block (rectangle, no fill, 1px stroke `#111` at 14%) as the panel. Panel 1: **Image** block (installed column) filling it, with overlay text in white. In each: a **Text** "01"–"04" at top (13px, muted) and her skill name at the bottom (28px), **in her order**. | 2 × 2 panels at 42vh. |
| 5 | **A3** projects | Blank section, White, anchor link `projects` | **Text** "Projects" (H2) cols 1–12, link "All projects →" cols 20–24. Then per project a row: **Line** (full width), **Text** number + title cols 1–10, **Text** her Role line + "PASSWORD PROTECTED" cols 12–17, **Image** 3:2 cols 19–24. Title, image and link all go to the project's URL. (A whole row can't be one link in Fluid Engine; title and image are.) | Image, then title, then role. |
| 6 | Contact | Blank section, theme Stone, anchor link `contact` | **Text** "CONTACT" (P3), **Text** "Let's create something people will remember." (H2) cols 1–14, **Text** links: Email · LinkedIn · Résumé (underlined; the résumé links to an uploaded PDF). | Stacked. |
| — | Footer | Site footer | "Yasmin Bajwa © 2026" left, "Back to top ↑" right (link to `#`). | — |

### Projects page (A13)

Squarespace **can't** show the password-protected Portfolio's grid publicly: locking a Portfolio page locks its grid page too. So **Projects is a regular page**:
- **Text** "Projects" (H2);
- four **Image** blocks (3:2) in a 2 × 2 grid (cols 1–12 / 13–24), each with a **Text** block beneath: "01 · PASSWORD PROTECTED", her title, her Role line;
- image and title link to the project page.

**No filter pills.** Portfolio pages have no native filtering, and the brief made them optional.

---

## 4. Case-study template (one Portfolio project page, filled four times)

Each project page in the Portfolio is built from ordinary sections.

| # | Reference | Section | Blocks (desktop) | Notes |
|---|---|---|---|---|
| 0a | **A1** cover | Blank section, **content width Full**, height L (≈16:7), **background image** = `r3-cover-rNN-16x7.jpg` | **Text** her title (H2, 72px) bottom-left, cols 1–12. | Jackson Home and Power & Energy: overlay **#111 at 38%**, title white. Rhode Island and Littelfuse (white documents): overlay **#FFF at 78%**, title ink. |
| 0b | **A4** meta panel | Same section as 0a | **Shape** block (white rectangle, no stroke) cols 14–24, lower rows, overlapping the section's bottom edge; on it **Text** blocks: ROLE (her Role line), METHODS (her Methods line), SETTING, YEAR, with **Line** blocks between. | YEAR: "[YEAR — pending client]" in italic where pending. Mobile: panel below the cover. |
| 1 | **A1** chapter index | Blank section, White | One **Text** block, full width, between two **Line** blocks: "01 Project Overview · 02 The Challenge · …", each linked to `#ch-1`, `#ch-2`… | Each chapter section gets its **Anchor link** (`ch-1`…) in *Edit Section → Design*. |
| 2 | **A2 + A3** chapter | One Blank section per chapter, White | **Text** "01" (P3) + chapter title (H3) cols 1–6. **Text** her copy cols 9–20: paragraphs, her sub-headings as Heading 4 with a **Line** block above, bullets as real (nested) lists. **Images** where her doc places them, cols 9–24 (or 1–24 for plates), caption "FIG. nn — …" below. | Mobile: title above text. |
| 3 | **A4** stats strip | Inside Jackson Home "Research Methodology" | Three **Text** blocks cols 1–8 / 9–16 / 17–24 under a **Line**: "60%" (72–96px), "Strollers" (H4), her characteristic text; the column heads as P3 labels. | Stacked. |
| 4 | **A5 / A14** spread | Jackson Home "Baseline Assumptions" | **Image** (plan with paths) cols 1–11; chapter number/title and her list cols 14–24. | Plan first. |
| 5 | **A6** board | Jackson Home charts; Power & Energy column-art panels; shop drawings | 2-up image blocks (cols 1–12 / 13–24), or 5-up for the column sides (cols 1–5 … 20–24, 9:32 portrait); shop drawings full width. Captions below each. | 1 column; the five column sides as a 2-up grid (Fluid Engine mobile doesn't scroll sideways). |
| 6 | **A5** video | Wherever her notes say INSERT VIDEO | **Video** block (upload the MP4 from `site/assets/video/`, or a Vimeo link), thumbnail = `poster-*.jpg`, *show controls*, caption row below: "FIG. nn — …" and the running time. | Full width. |
| 7 | **A7** findings / impact | Jackson Home Findings & Impact; Littelfuse audit; Power & Energy results | **Images** stacked cols 1–10; chapter title + her items cols 13–24 as a numbered list (CSS lines 5–6 add the hairlines). | Images after the list. |
| 8 | Reflection | Blank section, theme Stone, padding L | **Text**, centred, 28px italic, cols 5–20: her paragraph(s) verbatim. | — |
| 9 | **A5** prev / next | Blank section, White | **Line**, then three **Text** blocks: "← Previous project" + title (cols 1–8), "All projects" (cols 10–15, centred), "Next project →" + title (cols 17–24, right-aligned). | Stacked. |

**Figure captions** are listed in COPY-CHECK.md ("Added captions") for Yasmin to approve.

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
| Media → Background image | `r01-plan-plain.jpg` (Jackson Home plan). Opacity 8% via CSS line 15, on a white ground (line 16). |
| Branding & text → Site title | "Yasmin Bajwa" (top) |
| Headline | Projects are shared *by invitation.* (48px, Neue Haas Display 400) |
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
| Home | Photo strip | 5 Image + 5 Text | caption style (2–3) |
| Home | Statement | Text | — |
| Home | Four disciplines | Shape, Image, Text | — |
| Home | Projects rows | Text, Line, Image | — |
| Home | Contact / footer | Text, footer | — |
| Projects | Grid | Image, Text | — |
| Case study | Cover + meta | Section background + overlay, Text, Shape, Line | — |
| Case study | Chapter index | Text + anchor links, Line | — |
| Case study | Chapters | Text (lists), Line, Image, Video | list markers (4) |
| Case study | Stats strip, spread, boards | Text, Line, Image | — |
| Case study | A7 lists | Text (ordered list), Image | 5–6 |
| Case study | Reflection, prev/next | Text, Line | — |
| Lock screen | — | Native lock screen | 8–16 |
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
