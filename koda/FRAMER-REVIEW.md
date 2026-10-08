# Framer build review · exquisite-gecko-307188.framer.app

Captured 8 October at 1440 and 390 (`koda/screenshots/framer/`). Compared against `koda/site/v4/index.html` at commit `f751201` and the brand book.

## 1. The import is the earlier v4, before Ana's decisions

The copy on the site predates the 6 October update. Eleven strings need changing (or re-import `koda/site/v4/index.html`):

| Where | Framer has | Should be |
|---|---|---|
| Hero and close band link | or message us first | or send an enquiry |
| Who card 2 | …the last door. English and Spanish. Your Kóda stays… | …the last door. Vetted before their first evening. Your Kóda stays… |
| Built around your evening, row 2 | English and Spanish / Matched to your group's language. | Vetted before their first evening / Every Kóda is checked and trained before they meet a guest. VETTING STEPS · PENDING CLIENT |
| Built around your evening, body | Tell us the plans, the people and the language. | Tell us the plans, the date and how many of you. |
| How it works, body | Eight questions, one per page. | Nine questions, one per page, one total. |
| Phone 1, top row | Back · 1 / 8 | Close · 1 / 9 |
| Phone 1, question | Kóda Night · pre-set / What do you need a Kóda for? / six chips | The booking / Day, night, or the whole weekend? / Every booking is the same person, the same care. / chips: Kóda Day · Kóda Night (selected) · Kóda Weekend |
| Phone 1, footer | Eight questions, one per page. | Nine questions, one per page. One total, no breakdown. |
| Phone 2, top row and rows | Kóda · 8 / 8 · Language: English | Kóda · Confirmed · Duration: Five hours |
| The night, price ring | FROM [PRICE — PENDING] | Remove (no prices in page copy) |
| Three ways, price lines | [PRICE — PENDING CLIENT] ×3 | Remove |
| What a Kóda does, 05 | Speaks English and Spanish. | Is vetted and trained before their first evening. |

## 2. Layout broken by the import (desktop 1440)

1. **Hero pin labels.** 20:30 / 22:15 / 02:30 are stacked at the bottom centre instead of sitting at their pins. Prototype positions (percent of hero width/height): 43% / 17%, 69.4% / 13.8%, 88.2% / 22.7%. Make each label an absolutely positioned text layer inside the hero frame, or drop them and keep the line.
2. **Hero status panel ("Tonight") is not visible** at 1440, although its text is in the page. It should sit right-aligned beside the headline column, 380px wide, Bone fill, 0.5px Stone border, 20px radius.
3. **Check-a-date bar overflows** to the right; Kind and Check are clipped. It is a 4-column grid (1fr 1fr 1.4fr auto) spanning the content width (max 1200px), padding 8px, 0.5px Bone 22% border.
4. **Nav lockup and links collide.** "Three ways" starts right after the wordmark. The bar is a 3-column grid (1fr auto 1fr): lockup left, links centred with 32px gaps, time + pill right. Clear space around the wordmark equals its cap height.
5. **Bento dark tile.** The pin circle sits detached at the bottom-left; the line should pass through it. The lane photo tile lost its route line.
6. **Refund rows.** The ring numeral overlaps the row text. Grid is 56px / 1fr / auto with a 24px gap, padding 22px 32px 22px 24px.
7. **Footer.** The legal line renders at about 6px on one line at the far right; it should span the full width above the bottom rule at 11px. The WhatsApp · Email line breaks inside the brackets.

## 3. Layout broken by the import (phone 390)

1. **Nav overflows both sides** and the Plan pill is gone. At 390 the links hide; only the lockup and a 44px "Plan" pill remain.
2. **Hero height.** About 1150px of hero with empty photo below the check bar. Prototype: auto height, content stacked with 32px gaps, the panel and bar in flow.
3. **Bento tiles.** Two narrow columns with desktop type, so words break mid-word ("Barcelo / na"). At 390 the row is a 2-column grid with 14px gaps, tile padding 20px, titles 22–26px, body 13px.
4. **Built around your evening rows** and the refund rows: ring overlaps the title. Same grid fix as desktop.
5. **How it works** is a scaled-down desktop (both phones shrunk to about 300px wide). It should reflow: one phone per row, 320px wide, text above each.
6. **The night cluster** collapsed into slivers with clipped labels and a 600px empty navy gap. At 390 it is a 6-column grid: frames span 2/2/2 then 3/3 columns, heights 140 / 220 / 170 / 240 / 160, labels bottom-left at 18px.
7. **Close band input.** The placeholder is clipped by the Check pill. The input should shrink (min-width 0) and the pill keep 44px height.
8. Three ways (Night first), founder, does/doesn't, answers and footer columns reflow correctly.

## 4. Type

Computed fonts on the page include **Inter Variable UI 450** and **sans-serif 400**, which means some text (nav links, some body) is falling back to Framer's defaults. Brand book: Cormorant Garamond 300/400 (italic 400), Inter 300/500 only. Set the site's text styles once and apply them: Display (Cormorant 300), Body (Inter 300 15–16px), Label (Inter 500 9.5px, 0.18em caps), Button (Inter 500 12px, 0.14em caps). Nav links are Inter 300 14px.

## 5. Behaviour not yet built

- **Plan your evening** does nothing. It must open the Fillout flow: a Framer overlay on desktop (the split card, 1080×720, over a navy 60% scrim) and a full-screen overlay on phone. Until the Fillout embed exists, link it to a placeholder page.
- **Live Barcelona time** is static (13:09 from the import). A small code component with `Intl.DateTimeFormat('en-GB',{timeZone:'Europe/Madrid',hour:'2-digit',minute:'2-digit'})` updated every minute, in the bar, hero eyebrow and status panel.
- **FAQ rows** do not open. Framer accordion component, opacity-only reveal, 220ms (300ms in enhanced).
- **Motion** is absent: route line draw-on (1.8s, cubic-bezier(.76,0,.24,1)), section fades (320ms), running strip. Brand-level fades first; the rest is optional.
- **Mobile sticky bar** ("48 hours' notice · Barcelona" + Check a date) is missing.
- **Page title** is "My Framer Site". Set "Kóda · Barcelona", a meta description, and the favicon (tracked K on navy, from the brand book).
- The **Made in Framer** badge shows; it goes with a paid site plan.

## 6. Recommendation

The import flattened absolute positioning and breakpoint rules, so fixing layer by layer will take longer than rebuilding six components natively in Framer with stacks and grids: the nav, the hero (text column, status panel, check bar, route line as an SVG layer), the bento row, the numbered rows (one component reused for "Built around your evening" and the refund tiers), the phones section, and the night cluster. Everything else imported cleanly and can stay. The values above come from the prototype's CSS and are breakpoint-exact.
