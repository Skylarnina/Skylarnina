# Kóda landing page: source conflicts

Status: **Phase 1, waiting for client confirmation.**
Each item names the rule applied in the prototype. Anything marked **Confirm** needs a yes or no from the client before the Framer build.

## Which document decides what

| Topic | Final word | Status |
|---|---|---|
| Visuals (colour, type, radius, lines, motion, imagery) | Kóda Brand Book v1.0 (PDF export, 17 Sep 2026) | **Read.** |
| Business rules (notice, group size, Weekend, cancellation, price) | `pricing-spec.md` | **Not supplied yet.** The rules below are taken from the build brief's summary of the spec. |
| Page structure and copy direction | `Koda Homepage.dc.html` | **Not supplied yet.** |
| Exact colour and font variables | `koda-web-tokens.css` | **Not supplied yet.** The prototype uses the brand book's hex values. |
| Photography | `koda/images/` | **Not supplied yet.** The prototype uses flat navy or paper blocks, which the brand book allows ("the layout must still work with the images removed"). |

When the missing files arrive, this list will be checked against them again. The homepage may well contain more conflicts than the three the brief already fixes.

---

## A. Brand book vs. pricing spec (business rules: the spec wins)

**A1. Notice period.** *Confirm.*
The brand book says "at least two hours' notice" three times (booking-flow intro, the When question and the "Not in 1.0" list). The spec says 48 hours, and anything sooner goes to WhatsApp.
**Applied:** 48 hours everywhere on the page. The Fillout When question needs a 48-hour minimum date, and the brand book text should be updated.

**A2. Price visibility.** *Confirm.*
The brand book says the home screen always shows an indicative hourly range ("pricing is never hidden until the end"). Its shortcut rows and estimate bar also show figures (~€420, ~€140). The spec says the page copy must not hardcode a price, hourly rate or per-person figure.
**Applied:** one global `PriceNote` component that shows `[PRICE — pending client]` and can be hidden with a single flag. No figures appear anywhere. Please confirm whether the Fillout estimate bar still shows a live estimate. (That is computed, not hardcoded, so the spec may allow it.)

**A3. Confirmation time vs. notice.** *Confirm.*
The brand book's Confirmed screen says a Kóda "is being assigned and confirmation follows by email within two hours". That is a promise about how fast confirmation arrives, not a notice period, but it is easy to misread next to the 48-hour rule.
**Applied:** the landing page makes no claim about confirmation speed.

**A4. Kóda Weekend is not in the booking flow.** *Confirm.*
The brand book's Brief has a "Kind" question and separate When and Duration questions. The spec adds Kóda Weekend, a package with fixed windows (Fri 20:00–01:00, Sat 12:00–16:00, Sat 21:00–02:00). Those windows make Duration, and most of When, pointless for that option.
**Applied:** the landing page passes `?kind=weekend`. The Fillout logic should skip Duration and ask only for the weekend date when kind is weekend.

**A5. Group size vs. the People stepper.** No conflict, only a gap.
The brand book gives no maximum. The spec says one Kóda covers up to 6 people and 7–12 people get two.
**Applied:** the stepper should cap at 12, with a hint shown from 7 people up. Groups larger than 12 go to WhatsApp. *Confirm the over-12 route.*

**A6. "No instant path" vs. WhatsApp for short notice.** *Confirm.*
The brand book's "Not in 1.0" list rules out instant or on-demand booking and chat. The spec sends bookings with less than 48 hours' notice to WhatsApp.
**Applied:** WhatsApp appears only as a quiet secondary link ("or message us first") and in the FAQ, worded as a conversation rather than a faster way to book. There is no chat widget.

## B. Brand book vs. the build brief (visuals: the brand book wins unless the client overrides)

These are requests in the brief that the brand book forbids or does not cover. I have followed the brief because it is the direct instruction, but each one needs the client's approval.

**B1. Daytime hero on Paper.** *Confirm.*
The brand book says "Carry this to web: navy hero" and describes the imagery as "Barcelona at dusk… most of the frame is shadow". The brief, like Ana's homepage, switches the hero to Paper with a daylight photo before 18:00.
**Applied:** the day and night states as the brief describes. The daylight photo still gets the cool cast and low saturation. The navy confirmation screen at the end of the flow is unchanged.

**B2. Italic for the founder's note.** *Confirm.*
The brand book allows Cormorant italic 400 for "optional-field placeholders only". The brief asks for the founder's note in italic.
**Applied:** italic 400 for the founder's note only. The fallback, if refused, is Cormorant 300 upright.

**B3. Section spacing.** Resolved.
The brand book sets web section padding at 64px top and bottom. The brief asks for different vertical spacing in every section.
**Applied:** 64px is the minimum, and sections vary above it on the 8px grid (for example 64, 96, 128, 160).

**B4. Sticky bar fade duration.** Resolved.
The brief asks for a 240ms opacity fade. The brand book allows one 220ms transition, plus opacity fades on scroll-into-view at 200–400ms.
**Applied:** 240ms, because the bar appears in response to scrolling and 240ms sits inside the 200–400ms range. If the client prefers a single duration, use 220ms.

**B5. Hover colours outside the six.** Resolved.
The brand book says "six colours, no others", but its own button spec uses hover fills of #B8AC98 (stone) and #163043 (navy).
**Applied:** both hover fills, since they are the brand book's own values. `FRAMER-NOTES.md` will list them as hover states only, not as brand colours.

## C. Brand book rules that fail accessibility (the ≥4.5:1 text contrast in the brief)

Measured with WCAG 2.x relative luminance:

| Pair | Ratio | Brand book use |
|---|---|---|
| Stone on Paper | **1.79** | "Every eyebrow label" is stone |
| Stone on Bone | **1.58** | Same |
| Navy 38% on Paper / Bone | **2.34 / 2.29** | Labels and placeholders |
| Bone 38% on Navy | **3.15** | Labels on dark |
| Navy 62% on Bone | **4.49** | Muted text (just under 4.5) |
| Blue-mid on Navy | **2.49** | Inline links and verification labels |
| Navy 62% on Paper | 4.70 | Muted text, passes |
| Bone 62% on Navy | 6.17 | Muted text, passes |
| Stone on Navy | 8.96 | Labels on dark, passes |
| Blue-mid on Paper / Bone | 6.45 / 5.68 | Links, passes |

**C1. Stone eyebrow labels on light surfaces.** *Confirm.*
Stone text at 9.5px on Paper cannot be read by many people.
**Applied:** on light surfaces, eyebrow labels use navy 62% and stone is kept for hairlines. On navy, labels stay stone (8.96:1).

**C2. The 38% "low" text value.** *Confirm.*
**Applied:** 38% is used only for decorative repeats that are never the sole carrier of meaning, such as the section index numbers 01–09, and for Fillout placeholders (WCAG does not measure placeholder text, although it is still low). Captions and labels use 62%.

**C3. Navy 62% on Bone is 4.49:1.**
**Applied:** muted text on Bone surfaces (the founder's note, the cancellation block, the sticky bar) uses navy at 64%, which measures 4.77:1. This is an opacity tweak, not a new colour. *Confirm, or keep 62% and accept 4.49.*

**C4. Blue-mid links on navy.** *Confirm.*
**Applied:** Blue-mid appears only on light surfaces. On navy, links are bone with a 0.5px underline, and verification labels in the Who a Kóda is section sit on Paper so Blue-mid passes.

## D. Brand book vs. the homepage (copy: the homepage wins, except the naming guardrail)

The homepage file has not been supplied. These three items come from the brief:

**D1. The FAQ question that uses a banned word.** Resolved: the brand book's naming guardrail overrides everything.
**Applied:** "Is a Kóda a guide, or something more?"

**D2. "Extend at the same rate."** Resolved: this implies a rate, which the spec does not allow.
**Applied:** "Your Kóda can arrange more time on the night."

**D3. "Two hours' notice" in How it works and the FAQ.** Resolved, see A1.
**Applied:** 48 hours' notice.

**D4. Hero CTA label.** *Confirm.*
The brand book's hero button reads BOOK A KÓDA. The brief and the homepage use PLAN YOUR EVENING.
**Applied:** PLAN YOUR EVENING, per the copy hierarchy. It reads oddly on the Day option, so the three option pills say PLAN YOUR DAY, PLAN YOUR NIGHT and PLAN YOUR WEEKEND. *Confirm.*

**D5. Hero proposition.** Resolved.
The brand book's specimen reads "Trusted human presence." The homepage reads "Someone who knows the city, with your group, start to finish."
**Applied:** the homepage line, set in the brand book's three-part hero unit (serif, one stone hairline, muted sans).

## E. Gaps the brand book defines but the brief leaves out

**E1. Express lane and saved shortcuts.** *Confirm.*
The brand book says saved shortcut rows on the landing page skip to step 09 and "should be visually prominent, not buried". The brief does not mention them. With guest checkout and no accounts, a first-time visitor has no shortcuts.
**Applied:** left out of v1 of the page. It can be added later as hairline rows above the hero CTA once a way to store shortcuts exists (a cookie or an emailed link).

**E2. First Fillout question.** *Confirm.*
The brand book's Brief order is Kind, Occasion, People, Language, Location, When, Duration, Comfort note. The brief's overlay stub opens on "What do you need a Kóda for?", which is the Occasion question.
**Applied:** when `?kind=` is passed, Kind is pre-filled and hidden, so the flow opens on Occasion, now 1 / 7. Without the parameter it opens on Kind.

**E3. Where the wordmark sits.** Resolved, as a constraint rather than a conflict.
The brand book says the wordmark is never placed on a photograph, and "Barcelona" sits centred beneath it.
**Applied:** on mobile the wordmark sits on a flat navy or paper band above the hero photo. On desktop it sits in the type column.

**E4. Photos of people.** *Confirm the image selection.*
The brand book says "place and atmosphere rather than people" and allows "a figure in motion". The image brief allows people from behind or at a distance.
**Applied:** at most one or two small figures in motion per image. Groups must never be the subject of the photo.

---

## Housekeeping

- The brand book PDF was **not committed** because this repository is public. Put the source files in `koda/source/` only if the repo becomes private, or keep them outside git.
- The banned-word check will be run on `koda/` only. The repo's installed skills legitimately contain some of those words, and changing them is out of scope.
