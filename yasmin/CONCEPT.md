# Concept: "The Exhibition"

**One line:** Yasmin's portfolio is a small exhibition of her own work. The homepage is the entrance, each case study is a gallery room, and every image is catalogued like an object on the wall.

## Why this concept, from her material

- **Her work is literally about how people move through rooms.** Room 01 is a visitor-flow simulation of a historic house. Building the site as rooms you walk through, with a "Next room →" exit, turns her subject into the navigation. It isn't a decorative theme.
- **Her assets are mostly not photographs.** They are floor plans, shop drawings, simulation charts, persona boards and wireframes. Dropped into a template, they read as a slide deck. Treated as **plates** (numbered, captioned and mounted on a deeper wall), they read as a catalogue. The concept solves the hardest practical problem in the brief.
- **It gives UX research a museum voice without museum clichés.** The vocabulary is borrowed, not the decoration: wall labels, figure numbers, room numbers, a closing text panel, exhibit statistics set large. No gold frames, velvet, columns or parchment.

## How the design-taste rules and the client brief fit together

The sky-design-taste skill defaults to dark, cinematic, full-bleed photography. **The client brief wins** on ground colour (gallery white), the asymmetric hero and the no-shadow rule. The taste moves are carried in ways that fit an editorial, gallery-white site:

| Taste move | Where it lives here |
|---|---|
| Film leads / cinematic moment | One **black-box gallery** (`#141311`) per room: muted exhibit films shown like a screen in a darkened gallery. The Room 02 installation footage is the most cinematic material she has. |
| Depth-layered type | Enhanced hero: "Yasmin" in 140px+ Instrument Serif italic runs *behind* her shoulder (cut-out layer). The flat fallback is always designed alongside it. |
| Frame within the frame | The headshot **hung like an artwork**: 4:5, square corners, with a museum placard beneath. UI screens float on a deeper-wall panel instead of in device mockups. |
| Journey structure | Room 01 → 04, numbered chapters inside each room, a figure count that runs through the room, a "Next room →" exit band. |
| Scale contrast | 140px+ name and 120px exhibit numerals against 11px tracked-caps labels. |
| Photo strips | Room 02's **"five sides, unfolded"**: the column's 9:32 artwork strips set side by side as one band. This is the site's one strip rhythm. |
| Never list | No equal card grids, no icon rows, no mockups, no shadows or gradients, no generic copy, and no two consecutive sections with the same layout. |

## The components (built once, reused everywhere)

1. **Wall label.** A hairline table in 11px caps (Role · Methods · Setting · Year). The same component appears in the hero fact column, every room row on the homepage and every room header. This consistency makes it feel curated.
2. **Plate.** Image on `#E9E4DB`, multiply blend for line drawings, a "Fig. 07 — caption" line in small caps beneath, and a lightbox for the full sheet.
3. **Data wall.** A 2×2 or 3-up group of small chart plates, with one serif numeral beside it that states the finding. Charts are never full-width.
4. **Exhibit numeral.** Instrument Serif at 120px+ with a one-line label. Used for findings and statistics; claims she marks as targets are labelled as targets (Rhode Island "+23% target").
5. **Black box.** A dark section with the film centred, running time and caption.
6. **Pinned pair.** Two sketches rotated ±1.5°, captioned "Early sketches". This is the only playful moment, used once (Room 02).
7. **Archive red, `#8C2F1E`: "the curator's pencil".** Used only for room numbers, the lock mark, links, plan callouts and one rule per section.

**Optional addition to the brief (small, buildable):** each room ends with a **"Checklist of works"**, the list of figures in the room set in small type like an exhibition catalogue's checklist, just before "Next room →". It is a single text block in Squarespace. Your call.

## Room plan (from the source material)

| Room | Cover | Signature moments |
|---|---|---|
| 01 Jackson Home | House plan with the green visitor paths, with 2–3 red callouts at the entrance-area pinch points | Before/after plans (no paths → paths) · the archetypes as numerals **60 / 10 / 30%** · the data wall · the findings numerals **15-min windows · 30 per window · 3–4 presenters · controlled walk-ups** · the simulation film (pending) |
| 02 Power & Energy | Installed column in the gallery (frame from the final-setup film until the photo arrives) | **"5 sides, 1 story"** · the unfolded column strips · **"3 employee voices"** · the pinned sketches · shop drawings as plates · black box with fabrication + final setup |
| 03 Rhode Island | Two 401Health screens, frameless, on a deeper-wall panel (rebuilt from the vector PDF) | **"+23% target completion increase"** (always labelled as a target) · "Multilingual, incl. Portuguese" · detail crop of goals 20–23 · the app-review film beside the pain points |
| 04 Littelfuse | Detail crop of the journey map (Find → Learn → Get) | **73.2%** searched by exact stock number · **66%** engineers · **+6%** mobile logins after launch · the three archetypes · the personas film |

## Reading the references: one move from each

**Client reference, ayushfolio.** The PNG isn't in the repo (see ASSET-GAPS D9). Structure taken from the brief: italic greeting, fact side-column, linked rows, "What else?", contact footer.

**design-references/**, one concrete move per image:

| Reference | Move borrowed (or why not) |
|---|---|
| `434def…` "Unit 14 / The Arc" floor plan on paper | **The key reference.** A plan laid on a warm ground with an italic serif title and hairline area labels. This is exactly the Room 01 cover and plate treatment (multiply blend, italic serif, hairline labels). |
| `e04bea…` "Titans of the Mavericks / 8m — 20m" | A huge numeral range set beside an image with a tiny date and caption. This is the model for the exhibit numerals ("8–20 min · 30–45 · 50–65"). |
| `7ec34bc…` Sirotov "#MD1H" + "by numbers" | Outline wordmark behind the photo (depth type) and a 2×2 hairline number grid. Used for the enhanced hero and the Findings grid. |
| `43c8546…` "Process" | Hairline rows, each with a label left, text centre and a small image right. The homepage "Four disciplines" rows follow this. |
| `e269703…` "Case study: critique layout" | Numbered 01–04 principles in a narrow column beside drawings. Used for the Room 01 constraint plaque list. |
| `1153199…` Committed / stats strip | A single row of small area statistics under a hero. The wall-label strip under each room header. |
| `b2391a…` plans + renders on warm ivory | Plans floating on a warm off-white with no frame. Confirms the multiply-on-wall approach. |
| `a92e7e…` Foster plans | Two plans side by side at the same scale. Used for the Room 01 house + annex pair. |
| `d7590e…` / `cc683c…` El Retiro / Long Plan House | A section drawing as a thin full-width band above text. The shop-drawing detail crop in Room 02. |
| `d2cdf1…` "The Studio" | One centred statement in large sans between image rows. Adapted as the centred serif-italic reflection panel. |
| `92d6f7…` NÔR | Widely tracked caps wordmark over a subject. The tracked "HISTORY · FASHION · ART" line. |
| `bb8979…` ELEGANCE | Oversized headline cropped by the frame edge. Room titles may run into the gutter (Room 02 row). |
| `f7cf64…` Visionary columns | Tall thin panels in a row. Supports the "five sides, unfolded" strip band. |
| `4e61e9…` EAT / HIKE / CAMP strips | Stacked full-width strips with one tracked word each. Considered for the rooms index and rejected there (it would compete with the covers). The rhythm moves into the column strips. |
| `3d3427…` Studio projects | A projects list over a photo. Not borrowed: its equal 3-card grid is on the Never list. |
| `0bf800…` Spot Stash case study | A numbered left rail ("01 about / 02 goals / 03 research"). The chapter labels in the left column. |
| `64520d…` Building Quality | Big stat row (15+ / 34 / 100%). Numerals yes, its heavy grotesk no. |
| `5a77b1…` baroque | Colour-palette and type specimen strip. The format for the Site Styles sheet in the build notes. |
| `60816a…` Project №85 | House-layout plan with a hairline spec table beside it. The Annex plate + caption table. |
| `9c3af8…` go.arch | Vertical "01" slide index in a thin rail. Room numbers "ROOM 01 / 04". |
| `47642d…` Fillory | A dark, candle-lit section rhythm. The mood of the black-box gallery (only there). |
| `a29587…` Country Harmony | Outline circles as dividers. Not borrowed (too ornamental next to the hairlines). |
| `5f3aee…` Ambient | Warm brown frame around the site. Not borrowed (the ground stays light). |
| `0cfc66…` Booked (glass UI) | Not borrowed: glassmorphism is on the Never list. |
| `10fd21…` Travel Hub arches | Arch windows over a photo. Not borrowed (reads as travel ads; clichéd next to museum content). |
| `507072…` Adventure | Not borrowed: icon rows plus a dark template grid. |
| `80a4ea…` Choose a Destination | Depth carousel, active card larger. Considered for mobile "rooms"; rejected in favour of full-width cover + label per the brief. |
| `ce9fa9…` Nexetrip | Not borrowed: loud accent colour and a carousel. |
| `c0e150…` One Last Flight | Not borrowed: game-poster type. |
| `dabe4a…` Home Decor dark | Line drawings reversed out on dark. Kept as the option for shop drawings in the black-box section. |
| `64dd18…` Japan | Thin timeline with photos. The findings could hang on a thin line; kept in reserve. |
| `f5049d…` Visit Tokyo | Not borrowed: condensed display type and a stock hero. |

## Type check (to verify in Phase 2)

Instrument Serif (Google Fonts, 2023) is the first choice. Squarespace's Google catalogue lags new releases, so it will be **confirmed in the Site Styles font picker before Phase 2 is signed off**. Fallbacks in order: Newsreader → Libre Caslon Display. Sans: Neue Haas Grotesk Display/Text (Adobe, listed in Squarespace) → Inter Tight.
