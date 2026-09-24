# Asset Gaps

The case study PDF (`source/CASE STUDY-Yasmin Bajwa_compressed.pdf`) has 9
"insert here"-style placeholders. This is what's resolved vs. genuinely
still missing, after organizing everything you uploaded to `yasmin/`.

## Resolved (7 of 9)

| Placeholder (page) | Filled by |
|---|---|
| p.20 — "screen grab of what it looks like" | `media/power-energy/final-setup.mp4` |
| p.20 — "INSERT POWER & ENERGY VIDEO HERE" (CMS channels) | `media/power-energy/channels.mp4` |
| p.21 — "USE PDF VERSION HERE OF DRAWINGS" | `media/power-energy/shop-drawing-*.png` (3 sheets, rendered from `source/127505-...pdf`) |
| p.23 — "ADD COLUMN FABRICATION VIDEO HERE" | `media/power-energy/column-fabrication-progression.mp4` |
| p.27 — "INSERT VIDEO OF APP STORE REVIEWS HERE" | `media/rhode-island/app-store-reviews.mp4` |
| p.29 — "INSERT PDF OR VIDEO OF DESKTOP & MOBILE WIRE FRAMES HERE" | `media/rhode-island/wireframes.mp4` |
| p.35 — "INSERT WIREFRAMES FROM PDF HERE" (Littelfuse) | Partially — see gap below. `media/littelfuse/persona-*.jpg` cover the personas half of that section, but the actual click-through wireframes are not recoverable here. |

## Genuinely missing (2, plus 1 partial)

1. **Jackson Home discrete-event simulation video** (p.8 — "INSERT VIDEO
   HERE - DISCRETE EVENT SIMULATION"). Everything uploaded for Jackson Home
   is static charts/diagrams (15 images now in `media/jackson-home/`,
   including several new ones pulled from the case study PDF). None of them
   is a video of the simulation actually running. `IMG_7910.GIF`, which you
   flagged as a possible match, is **not** this — it's an animated version
   of headshot #3 (see below). If a simulation recording exists, it wasn't
   among the files uploaded to `yasmin/`.

2. **Power & Energy "Final Results" video** (p.23 — right after the Results
   & Impact paragraph, distinct from the column-fabrication video above,
   with its own Google Drive link in the source text). No uploaded
   Power & Energy video is labeled as a results/outcome video — the four
   present (`final-setup.mp4`, `channels.mp4`, `column-fabrication-progression.mp4`,
   `user-flow.mp4`) all cover setup, CMS, fabrication, or user flow, not a
   "results" cut.

3. **Littelfuse wireframes, partial gap.** `Little Fuse Wireframes .docx`
   turned out to contain no embedded images — it's a list of ~15 links to
   an external Adobe XD prototype (`xd.adobe.com/view/...`). That domain
   isn't reachable from this environment (network policy blocks it), so the
   actual wireframe screens couldn't be pulled from either the docx or the
   live prototype. What *is* now available — `media/littelfuse/journey-map.png`,
   `user-archetypes.png`, `engineering-personas.mp4`, and the two new
   persona images — covers the personas/journey side of that section but
   not literal wireframe screens. To close this, either export/screenshot
   the Adobe XD prototype yourself, or re-upload the wireframes as a PDF or
   images directly.

## One correction to your note

You flagged `IMG_7910.GIF` as a possible match for "the simulation." It's
actually an animated (subtle motion/cinemagraph-style) version of headshot
#3 — same neutral-backdrop, blazer photo, just in motion. It's filed in
`media/headshots/` as `headshot-03-animated.gif`, not in
`media/jackson-home/`.
