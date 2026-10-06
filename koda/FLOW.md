# Kóda booking flow, 1.0 (Fillout)

Source of truth: *KÓDA 1.0 Pricing architecture & build specification* (Ana, Google Doc) and the brand book's question template (section 05). Ana's decisions of 28 September are applied: Day / Night / Kóda Weekend first; no language question; no occasion step; an optional note at the end; one exact total; no prices in page copy; 48 hours' notice or the enquiry route; no saved shortcuts in 1.0; "Kóda / Kódas" everywhere, never "companion".

Prototype: `koda/site/v4/flow.html` (board of screens). Figma frames: `koda/exports/figma/v4/koda-flow.html`, post with selector `.cell > .scr, .desk`.

## Screens

| # | Screen | Control | Advances | Price shown |
|---|---|---|---|---|
| 01 | Day, night, or the whole weekend? | Three hairline rows: Kóda Day · Kóda Night · Kóda Weekend, equal footing (spec §5) | On tap | No |
| 02 | Which date? | Boxed date pill + calendar; dates inside 48 h are low and route to enquiry (spec §9.3); busier dates outlined (peak calendar, §4.4) | Continue | No |
| 03 | When should your Kóda arrive? | Boxed time pill + half-hour chips (§3.1); hint explains that 20:00 or later is Night (§3.2) | Continue | No |
| 04 | How many of you? | Stepper 1–12; "Two Kódas · seven to twelve" from 7; 13 routes to enquiry | Continue | From here (§9.2) |
| 05 | How long? | Chips 4–8 hours, 5 pre-selected (§9.1) | On tap | Yes |
| 06 | Where will you be? | Serif-underline free text + four quick chips; "doesn't change the price" (§9.1) | Continue | Yes |
| 07 | Anything we should know? | Optional note, italic placeholder | Skip / Continue | Yes |
| 08 | Who should we confirm to? | Name · Email · Phone (WhatsApp) | Continue | Yes |
| 09 | Your evening, read back. | Seven summary rows, cancellation terms in plain language, terms chip (§11) | Pay €… and request | Yes |
| 10 | Pay in full, once. | Apple Pay · Google Pay · card (§10), one total | Pay and request | Yes |
| 11 | Your Kóda is being assigned. | Navy. Reference, when, where, people, charged. WhatsApp pill | — | Charged |
| Route | Sooner than two days? | Enquiry: a line of plans + WhatsApp number; also used for 13+ people and outside Barcelona (§9.3) | WhatsApp / Send enquiry | No |
| 02w · 03w | Which weekend? · How many of you? | Weekend replaces date, time and duration with one weekend pick and the three fixed windows (§5); 7 questions instead of 9 | Continue | From people |

## The one price line

`€460` in Cormorant 400 at 24px, then in Inter 300 muted: `Night presence · Thursday 12 March · 21:00–02:00 · up to 6 guests`. Nothing else, ever (spec §2.1). The figures in the prototype come from the spec's tables and are illustrative:

| Example | Figure | Table |
|---|---|---|
| Night, 6 guests, 5 h, Thursday | €460 | §4.2 Band C |
| Night, 8 guests, 5 h, Thursday | €830 | §4.2, 7–12 guests |
| Kóda Weekend, 5 guests, Fri 13–Sat 14 March | €1,140 | §5, peak (Fri/Sat always peak) |

## Open for Ana or the Fillout build

1. The brand book's template has the price appear from the Duration question; the spec says from People. The prototype follows the spec.
2. The spec's example line uses "Saturday 14 March" at €460, but every Saturday is peak (§4.4), which would be €530. The prototype uses a Thursday so the figure matches the table.
3. Quote expiry of 30 minutes (§9.4) has no screen; it recalculates silently.
4. Terms text and the confirmation email are placeholders until the legal review (§16.5).
