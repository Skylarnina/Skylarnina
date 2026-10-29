# Contact page: Squarespace build

Prototype: `site/contact.html` (in the theme switcher like every page; the header's **Contact** now opens it).
Screenshots: `screenshots/contact/contact_1440.png`, `contact_390.png`, `contact_sent.png`.
Native blocks only; **no custom CSS** needed.

## Layout

| Desktop (24 columns) | Mobile (stacked, top to bottom) |
|---|---|
| Photo, columns 1–10, portrait 4:5, top-aligned · column 11 empty · columns 12–24: label, heading, intro, form, contact details | label, heading, intro → form → contact details → photo |

## Before you start
- [ ] If the site already has a Contact page, edit that one (keep its URL). Otherwise **Pages → Main Navigation → + → Blank page**, title **Contact**, URL slug `/contact`.
- [ ] Header navigation: **Projects · About · Contact**, with **Contact** → `/contact`.
- [ ] Upload `site/assets/img/contact-yasmin.jpg` (Yasmin at the painting, cropped 4:5 from her clean upload of snippet 10).

## The section
- [ ] One section, the page's light colour theme (same as most pages). Space above / below as the other pages' sections (desktop 130px, mobile 88px).

**Desktop (Fluid Engine, 24 columns)**
- [ ] **Image block**, columns 1–10, starting at the top row, tall enough for a 4:5 portrait (Design → Shape: rectangle; focal point on Yasmin). Alt text: `Yasmin looking at a framed painting in a gallery`. No caption, no link.
- [ ] **Text block**, columns 12–24, top row:
  - `CONTACT` — Paragraph 3 (the small capitals label style).
  - `Let’s create something people will remember.` — Heading 2 (the 80px title style).
  - `Working on an exhibit, a digital experience or a research question? I’d love to hear about it.` — Paragraph 1, muted colour. **New wording: Yasmin approves or replaces it.**
- [ ] **Form block**, columns 12–24, under the text:
  - Fields, in order:
    1. **Name** (First / Last), required.
    2. **Email**, required.
    3. **Dropdown** — label `What’s it about?`, options: `An exhibit or project` · `UX design or research` · `A collaboration` · `Just saying hello` (**new wording for Yasmin to approve**).
    4. **Text area** — label `Message`, required.
  - Submit button label: `Send message`.
  - Storage → **Email**: send to `yasminbajwa248@gmail.com` (**confirm the address with Yasmin**; it's the one on the homepage).
  - **Post-submit message:** `Thank you. Your message is on its way, and I’ll get back to you soon.` (**new wording**).
  - Form title: none. Required fields show "(required)" automatically.
  - Design: field style **underline** (or the plainest the block offers), square corners, primary button = the solid accent button (same as the lock screen's Enter). Check: *Site Styles → Buttons* and the form block's Design tab (**verify** names in her account).
- [ ] **Text block(s)** for the contact details, columns 12–24 under the form: three columns (12–15 · 16–19 · 20–24) or one block with three short lines. Each: a Paragraph 3 label, then the link:
  - `EMAIL` → `yasminbajwa248@gmail.com` (link: `mailto:yasminbajwa248@gmail.com`)
  - `PHONE` → `(313) 979-2205` (link: `tel:+13139792205`)
  - `LINKEDIN` → her LinkedIn URL (**still pending**: leave this line out until it arrives)
- [ ] **Line block** (1px, ink), columns 12–24, just above the contact details.

**Mobile (switch to the mobile view and arrange)**
- [ ] Order: text block → form → contact details (stacked, one per line) → photo, all full width.
- [ ] Submit button full width if the form block offers it; otherwise left-aligned.

## Check
- [ ] Send a test message from the live page: it should arrive at the address above and show the thank-you message.
- [ ] Email and phone links open the mail app / dialler on a phone.
- [ ] **Contact** in the header is underlined (current page) when on this page.

## To decide with Yasmin
- **Phone number on a public page?** It's on the homepage already; some people prefer email + form only, to avoid spam calls. Easy to drop.
- The three pieces of new wording above (intro line, dropdown options, thank-you message).
- **Homepage Contact band:** keep it as is (quick details at the end of the homepage); the header's Contact now goes to this page.
