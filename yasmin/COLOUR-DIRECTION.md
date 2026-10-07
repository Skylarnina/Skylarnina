# Colour direction: cream, wine and The Henry Ford's colours together

**The question:** the Figma file now has cream and wine; the client also gave the five colours from her business card (The Henry Ford's venues). How do they mix without getting loud, and while keeping the site editorial, minimal and premium?

**The answer in one line:** give every colour **one job**. Cream is the paper, navy-black is the type, **wine is Yasmin**, and **the card colours are wayfinding**. They mark *which project you're in* and never decorate.

Live in the prototype as **Heritage** and **Heritage rich** (the theme switcher, top-right; or open any page with `?theme=heritage`). Side by side with the ChatGPT mockup: `screenshots/heritage-compare.png`. Values and contrast checks: `THEMES.md`.

---

## 1. What the ChatGPT mockup got right, and what it got wrong

**Kept (the instinct is good):**
- Warm cream paper instead of white: it reads as print, which suits a museum designer.
- Navy for type and one dark band, the card's own Henry Ford Academy navy.
- A colour per project beside each row: the strongest idea in the mockup.
- A five-colour rule near the projects: the card itself, as a quiet signature.
- One olive band for the personal section.

**Dropped:**
- **The site title reads "Henry Ford Museum".** This is Yasmin's portfolio. Branding it as the museum would misrepresent whose site it is, and it is her employer's name. It stays **Yasmin Bajwa**.
- **Too many loud devices at once:** an orange header bar, an olive band, a navy band, a red footer, swooshes, colour-washed photos, paper texture and a script font. Each could work alone; together they read as a gift shop, not an editorial portfolio. **Premium comes from restraint.** In Heritage at most one coloured band is visible at a time, and nothing is decorative.
- **The orange "Yasmin."** measures **2.5:1** on cream, so it fails contrast. In Heritage her name is **wine** (7.3:1). That is the one place her personal colour speaks loudest.
- **Gradients, waves, the blob behind the portrait, textured paper:** not native to Squarespace, and they date quickly.
- **Changed copy.** The mockup rewrote her words: "USA", "UI Research", the discipline names, a new "Beyond the work" text, "Built with purpose. Inspired by history.", "© 2026". None of it is used; the site keeps her copy verbatim. If the "Beyond the work" text is new copy she wants, send it and it can go in as copy, separately from the colour decision.

---

## 2. The system (use these as Figma colour variables)

| Variable | Hex | Job | Share of the page |
|---|---|---|---|
| `paper` | `#F3F0EA` | Page ground, header, footer, chapters | ~60% |
| `paper-2` | `#E9E4DB` | Second ground: Snippets (Heritage), Reflection, logo tiles | |
| `ink` | `#1C2635` | All type and rules. A navy-black, so the navy band belongs to it. | ~30% with the band |
| `ink-muted` | `#1C2635` at 68% | Labels, captions (5.0:1, passes) | |
| `wine` | `#8C2F1E` | **Yasmin's accent**: "Yasmin.", link underlines, "Password protected", the active chapter, the Enter button | ~2% |
| `navy` | `#1E3F63` | The one dark band: Contact (cream text) | |
| `olive-band` | `#5E6337` | Heritage rich only: the Snippets band (cream text). The card olive, deepened so cream text passes. | |
| `venue-orange` · `venue-olive` · `venue-red` · `venue-blue` · `venue-navy` | `#E9A35B` · `#8A8D4F` · `#B04A44` · `#6E94AB` · `#1E3F63` | **Wayfinding fills** (the card values): a 3px bar beside each project row, the five-colour rule, the tile hover tint. **Never text.** | ~1% |
| `venue-*-text` | olive `#63653A` · orange `#8E5412` · blue `#48677A` · red `#A8443F` | The same colours deepened for **small text**: project numbers, case-study chapter and FIG. numbers | |

**Which colour belongs to which project** follows the venues, not decoration:
- **01 Jackson Home: olive.** It stands in Greenfield Village.
- **02 Power & Energy: orange.** It is in the Henry Ford Museum.
- **03 Rhode Island: light blue.** Research (Benson Ford Research Center).
- **04 Littelfuse: red.** Engineering (the Rouge factory).

On each case study, that project's colour marks its chapter numbers, figure numbers and active chapter, so you always know which "room" you're in.

## 3. Why wine and the card red can live together

Wine (`#8C2F1E`) and the card's Rouge red (`#B04A44`) are one family, a deep and a lighter brick. They don't fight because they never do the same job. **Wine is always Yasmin** (her name, her links, her button). **The red is only ever Littelfuse's marker**: a 3px bar, a number. Keep them apart in role and they read as one warm thread through the site.

## 4. Rules that keep it premium

1. **One coloured band at a time.** Heritage has one (navy Contact). Heritage rich has two (olive Snippets and navy Contact), far apart, with the photo panels between them as the only other dark moment.
2. **Venue colours are marks, not fills.** At most 3–4px of a venue colour per element, except the tile hover tint.
3. **Never coloured headings, never coloured photos.** Images stay true; the panels' darkening layer is navy-ink, not a colour wash.
4. **Type does the hierarchy.** Size and the serif carry the page, and colour only labels.
5. **No gradients, textures, waves or second display font.**
6. **Every text pair passes 4.5:1.** Checked on the rendered pages, text on photos included (`THEMES.md`, rendered audit).

## 5. The two options for Yasmin

| | Heritage | Heritage rich |
|---|---|---|
| Feel | Quiet, gallery-like, closest to the current build | Warmer, more personal, closest to the ChatGPT mood |
| Coloured bands | Contact (navy) | Snippets (olive) + Contact (navy) |
| Snippets section | Paper 2 `#E9E4DB` | Olive `#5E6337`, cream text |
| Everything else | Same | Same |

My recommendation is **Heritage** for the case studies (the work should carry the colour), with **Heritage rich** as the option if she wants the homepage to feel more personal. The two differ in one section, so switching later is a single section setting.

## 6. In Squarespace

The full settings for each palette are in SQUARESPACE-BUILD-NOTES.md (*Site Styles per theme*).
- **Palette slots:** Heritage `#F3F0EA` · `#E9E4DB` · `#1C2635` · `#8C2F1E` · `#1E3F63`. Heritage rich needs `#5E6337` as well, which is one more than the five slots. Drop `#E9E4DB` from the palette (the logo tiles get their ground from CSS anyway) and give the Reflection the paper ground.
- **The five-colour rule over the projects:** an Image block of `site/assets/img/stripe-venues.png`. Native, no CSS.
- **Row bars and per-project numbers:** a 3px-wide Shape block per row in the venue colour (**verify** the Shape colour picker takes a custom hex), or 4 lines of CSS.
- **CSS budget:** about 28–30 lines, at the limit. If needed, drop the coloured tile hovers (−4 lines) first.
