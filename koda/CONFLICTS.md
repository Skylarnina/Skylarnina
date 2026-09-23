# Kóda landing page: source conflicts

Status: **v2 brief, Step 1, waiting for client confirmation.**
Each item names the rule applied in the prototype. Anything marked **Confirm** needs a yes or no from the client before the Framer build.
Sections A–E come from the first brief. **Section F adds the conflicts introduced by the v2 brief** ("Dusk falls as you scroll", the two motion levels, the reference-driven sections). Where F replaces an earlier item, it says so.

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

## F. v2 brief vs. the brand book

Brand mode follows the brand book exactly. Enhanced mode is the client's to approve, and every enhanced-only item below is off in brand mode and whenever `prefers-reduced-motion` is set.

**F1. The background changes colour as you scroll.** *Confirm (enhanced only).*
The brand book says there are six colours and nothing else, and no gradients. Blending the background from Paper through Bone and Blue-rich to Navy while scrolling shows every colour in between (for example the mix of Bone and Blue-rich), so across time it works like a gradient.
**Applied:**
- Brand mode: each section sits on one flat brand colour, and the colour changes at section edges only.
- Enhanced mode: the background blends continuously, but it is always one flat colour on screen at any moment, never a gradient.
- Text colour switches from navy to bone at a fixed point in the sequence, so text never sits on a halfway colour with poor contrast.

**F2. Blue-rich as a full section background.** *Confirm.*
The brand book reserves Blue-rich for "sub-surfaces inside dark sections only". The v2 brief blends to Blue-rich across all of Section 4.
**Applied:** Blue-rich is used only as a background colour inside the dusk stretch, always with bone text. Measured: bone 100% on Blue-rich is 9.80:1 and bone 62% is 4.81:1, so text passes. Stone labels on Blue-rich are 6.21:1.

**F3. One italic phrase in every headline.** *Confirm.* (This widens B2.)
The brand book allows Cormorant italic 400 only for placeholders; B2 already asks to extend it to the founder's note. The v2 brief puts an italic phrase in every display headline, as Wispr does.
**Applied:** italic 400 on the last phrase of display headlines, and on the founder's note. Never in body copy, labels or buttons. The fallback, if refused, is all upright Cormorant 300.

**F4. Headline size.** *Confirm.*
The brand book says desktop hero type is 64–76px. The v2 brief allows 64–96px.
**Applied:** the hero stays at 76px. Only the closing "Everyone *home.*" goes to 96px, as the one moment of maximum scale. Labels stay at 9.5–11px.

**F5. Enhanced motion as a whole.** *Confirm (enhanced only).*
The brand book forbids parallax and entrance choreography and allows one 220ms colour or opacity transition plus 200–400ms fades. Enhanced mode adds:
- smooth scrolling;
- the route line drawing itself as you scroll;
- text drifting along the hero path;
- the pinned scroll story;
- panels sliding over earlier sections;
- 600ms crossfades.

None of these use bounce, spin, scale or blur.
**Applied:** all of these run in enhanced mode only, behind the `MOTION` toggle. Brand mode is static apart from the allowed fades and the hero film. The 600ms tile crossfade is the only duration above 400ms.

**F6. A 28px top radius on sliding panels.** *Confirm (enhanced only).*
The brand book says everything that isn't tappable has square corners.
**Applied:** 28px top radius in enhanced mode, 0px in brand mode.

**F7. FAQ rows animate their height, and use "+" / "−".** *Confirm.*
The brand book allows only colour and opacity transitions, and no iconography "beyond the tracked initial and the serif step numeral".
**Applied:**
- Brand mode: the answer appears at once and fades in over 220ms.
- Enhanced mode: the height also animates over 300ms.
- "+" and "−" are Inter 300 text characters, following the v2 brief.

**F8. Hero film.** Resolved.
The brand book allows landing-page imagery (graded cool, mostly shadow, full-bleed), and a muted, looping film counts as that imagery. v2 fixes the hero at golden hour, so **the v1 day/night hero switch (B1) is retired.** The live Barcelona time moves to the top bar.

**F9. The wordmark would sit on the film.** *Confirm.*
The brand book says never to place the wordmark on a photograph. In the v2 brief, the top bar is transparent over the hero film, with the wordmark in the centre.
**Applied:** the top bar is solid Paper from the start, and the film begins directly below it. So the wordmark never touches the film, and the bar doesn't change on scroll. The alternative, if the client wants the transparent bar: hide the wordmark while the bar is over the film and fade it in (220ms) when the bar turns Paper.

**F10. The hero headline drops "with your group".** *Confirm.*
The homepage line is "Someone who knows the city, with your group, start to finish." The v2 brief shortens it to "Someone who knows the city, / *start to finish.*" Copy direction belongs to the homepage.
**Applied:** the v2 wording, because the italic split reads better, but it's flagged. "With your group" moves into the supporting line.

**F11. Contrast of text on film.** Resolved, as a constraint.
Bone text over moving footage can't be guaranteed to pass contrast.
**Applied:** every piece of hero text sits inside the flat navy 60% block on the bottom third. The route-path text also stays inside that block, or sits over the film at bone 100% with nothing essential in it: it repeats the timeline, so it isn't the only place that information appears.

**F12. Dimmed lines at 38%.** *Confirm.* (This extends C2.)
In the pinned story index and the Section 6 list, inactive items sit at 38% (bone at 38% on Navy is 3.15:1), which fails 4.5:1.
**Applied:** 38% for inactive items is accepted, because the same text reaches 100% when active and brand mode shows everything at full strength. For stricter compliance, use 62% for inactive items (6.17:1 on Navy).

**F13. "Four to eight hours."** *Confirm against the pricing spec.*
Section 6's copy states a duration range. My summary of the spec only covers the Weekend windows.
**Applied:** the text is shown in the prototype, marked `[confirm against spec]`.

**F14. Otter's framed panel vs. the full-bleed hero.** *Confirm.*
The brief takes both "a big framed hero panel" (Otter) and "a full-bleed cinematic hero" (Ooshot and Squarespace), and they can't both be the hero.
**Applied:** the hero is full-bleed, per the section spec. The framed-panel idea goes to the Section 5 Navy panel (inset from the viewport edges).

**F15. The drifting city-lights dots.** *Confirm (enhanced only).*
The brand book bans texture, and in brand mode the only thing that moves is fades.
**Applied:** 60 or fewer flat bone dots with no glow. Static in brand mode, drifting very slowly in enhanced mode, and paused when off screen or when `prefers-reduced-motion` is set.

**F16. A photo of the founder.** *Confirm.*
The brand book says "no faces of named people, no posed portraits". The v2 brief asks for a large candid photo of Ana.
**Applied:** a placeholder slot marked `[founder photo — candid, not posed; confirm the brand book allows the founder's face]`. If not allowed, use a candid shot of her hands, from behind, or at a distance, or fall back to the brand book's tracked serif initial.

**F17. More people in the photos.** *Confirm the image selection.*
Otter's "candid human warmth" pulls towards people. The brand book puts place and atmosphere first.
**Applied:** people only in motion, from behind or far away, never the subject of the frame. Warmth comes from light, hands and doorways.

**F18. Booking overlay: "1 / 8" vs. a pre-set kind.** *Confirm.* (This replaces E2's count.)
The v2 brief says the overlay shows "Back" and "1 / 8". With `?kind=` passed, the Kind question is already answered.
**Applied:** the count is always 1 / 8 and the flow opens on "What do you need a Kóda for?". The pre-set kind shows as a quiet eyebrow ("KÓDA NIGHT"). "Back" closes the overlay on the first question.

**F19. GSAP and Locomotive in a Framer spec.** Resolved, as a note.
Framer can't run GSAP or Locomotive.
**Applied:** the prototype uses them only to demonstrate the motion. `FRAMER-NOTES.md` will map every effect to Framer's own tools: scroll transforms, sticky, the Smooth Scroll component, variants, the video component and overlays. Nothing is built that Framer can't reproduce. The published preview loads GSAP from cdnjs, because the preview host can only load scripts from there.

**F20. "Everyone gets home." then "Everyone home."** A copy note.
The Section 2 statement and the closing headline use nearly the same line.
**Applied:** both are kept as written; the repetition works as a bookend. Tell me if you'd rather change one of them.

**F21. Round 2: Night is larger than Day and Weekend.** *Confirm.*
The pricing spec says Kóda Weekend must sit "on equal visual footing" with a single booking. The round-2 direction makes Night large (7 columns) with Day and Weekend stacked (5 columns).
**Applied:** as directed. Weekend keeps the same label style, price note and pill as the others, but its tile is smaller. If the client holds to the spec, the fallback is to make Weekend the large tile, or to rotate which option is large.

**F22. Round 2: headline sizes above the brand book's range.** *Confirm.* (This extends F4.)
The brand book caps desktop hero type at 76px. Round 2 sets the hero at 104px, the statement at 96px, section headlines at 72–88px, the story times at 140px and the closing line at up to 172px. Labels stay at 9.5–11px, as the brand book requires.

## G. Round 3 (sky-design-taste and the Pinterest pins)

**G1. Arch window in "Who a Kóda is".** *Needs Ana's approval.*
The brand book says non-interactive elements are 0px radius. In enhanced mode, the window over the night photo is a tall arch (full radius at the top), and so is its 0.5px stone frame.
**Applied:** brand mode is a sharp rectangle; the arch appears in enhanced mode only.

**G2. The word BARCELONA sits on the photo without a navy block.** *Confirm.*
The brand book asks for navy 60% wherever type sits on an image. The depth-type hero puts the big word straight onto the photo, behind the cut-out foreground. It is decorative and hidden from screen readers; the real headline sits in the navy 60% block.
**Applied:** in both modes, because the word is the hero's main idea. If refused, the fallback is to keep the word in enhanced mode only.

**G3. Depth carousel.** *Confirm (the motion is enhanced only).*
The side tiles at 80% scale and 60% opacity are a static layout, so they appear in both modes. The 900ms `cubic-bezier(0.76,0,0.24,1)` slide runs in enhanced mode only; brand mode switches instantly with a 220ms opacity change.
**Applied:** the round-3 brief asks for arrows, but the brand book bans arrow glyphs. The controls are text pills instead: PREVIOUS / 02 / 03 / NEXT. Swipe and the keyboard arrow keys also work.
This also changes F21: Night is the active tile by default, but each option becomes the same large framed tile when selected, which brings Weekend back towards equal footing.

**G4. Scroll depth and strip drift.** *Confirm (enhanced only).*
- The hero foreground rises about 180px while the word rises 70px.
- Each strip photo drifts ±7% inside its band.

Both are forbidden by the brand book's motion rules (parallax), so they are off in brand mode and when reduced motion is on.

**G5. The hero cycles through five scenes.** *Confirm.*
In enhanced mode the hero crossfades to the next clip every 6.5 seconds (1200ms, same curve). In brand mode it stays on scene 01 until someone taps the 01–05 index.

**G6. Story numerals at 160px, strips in spaced caps.** These extend F22, which covers headline sizes above the brand book's range. Labels stay at 9.5–11px.

---

## Housekeeping

- The brand book PDF was **not committed** because this repository is public. Put the source files in `koda/source/` only if the repo becomes private, or keep them outside git.
- The reference captures (Wispr, Ooshot, Squarespace, Otter, Adomate) are kept locally in `koda/references/`, which is git-ignored because they are other companies' pages and this repository is public.
- The banned-word check will be run on `koda/` only. The repo's installed skills legitimately contain some of those words, and changing them is out of scope.
