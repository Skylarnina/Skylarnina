# Contact page: Framer handoff

> **Round 1 client feedback applied** (more contrast, grey banner, outline buttons, new copy).
> The banner colour is still open: the prototype bar switches between *Grigio scuro* and *Grigio chiaro*.

Prototype: `oltresoglia/contact/index.html` (open it directly; use the dashed "Prototipo" bar or
`?stato=errore` / `?stato=inviato` to see the three form states). Everything matches the approved
test build. Token source: `oltresoglia-quiz/src/index.css`, audited in `../TOKENS.md`.

## Styles to create in Framer (match the test)

### Colour styles

| Framer style | Value | Used for |
| --- | --- | --- |
| Oltre/Dark Charcoal | `#050505` | page ground, text on saffron |
| Oltre/Porcelain | `#EBF0F2` | headings, labels, input text, icons |
| Oltre/Saffron Mango | `#EFC04D` | button border + text + glyph, eyebrow, focus ring, invalid border, check mark, social hover |
| Oltre/Whiteout | `#FFFFFF` | wordmark only |
| Oltre/Blackout | `#000000` | button fill, background artwork |
| Oltre/Banner Grey (option A) | `#232526` (Porcelain 13% mixed into Dark Charcoal) | banner fill, *Grigio scuro* |
| Oltre/Porcelain as banner (option B) | `#EBF0F2` | banner fill, *Grigio chiaro*; left-column text becomes Dark Charcoal |

Porcelain at fixed opacities (make these as separate styles, or set the opacity on the fill):

Round 1 raised these one step above the test for more contrast (test value in brackets):

| Opacity | Role |
| --- | --- |
| 85% (75%) | body text (supporting line, WhatsApp lead-in, nav links, socials label, details values) |
| 75% (70%) | small labels |
| 65% (55%) | muted text: required `*`, privacy line, details labels, loading button text |
| 45% (35%) | placeholders |
| 50% (40%) | border of a valid, filled field |
| 28% (20%) | field border, menu button border, loading button border |
| 14% (10%) | banner border, form-card border, hairlines |
| 12% (8%) | social button fill |
| 6% (4%) | field fill |

Form card fill: Dark Charcoal 88% (solid Dark Charcoal on the light banner). Background overlay: 45% (test 60%).
Button glow: 0 0 18px Saffron 35% (hover 0 0 26px Saffron 50%, fill Saffron 14% over Blackout); no glow on the light banner.
No other colours: no red, no green, no gradients.

### Text styles

| Framer style | Font | Size / line height | Weight | Case / tracking | Colour |
| --- | --- | --- | --- | --- | --- |
| Eyebrow | Bounded | 12 / 16 | Regular 400 | UPPER, 0.18em | Saffron |
| Headline light | Bounded | 56 / 59 (mobile 40 / 42) | ExtraLight 200 | sentence | Porcelain |
| Headline strong | Bounded | 56 / 59 (mobile 40 / 42) | Black 900 | sentence | Porcelain |
| Lede | Manrope | 18 / 29 | 400 | none | Porcelain 75% |
| Nav link | Manrope | 14 / 20 | 500 | none | Porcelain 75%, hover 100% |
| Field label | Manrope | 14 / 20 | 600 | none | Porcelain |
| Input | Manrope | **16** / 24 | 400 | none | Porcelain; placeholder 35% |
| Field message | Manrope | 14 / 20 | 400 | none | Porcelain, with a 16px saffron "!" icon |
| Button | Manrope | 16 | 600 | none ("Fai il test") | Saffron |
| Button caps | Manrope | 16 | 600 (WhatsApp) / 700 (Invia) | UPPER, 0.12em / 0.14em | Saffron |
| WhatsApp lead-in | Manrope | 16 / 24 | 400 | none | Porcelain 85% |
| Privacy | Manrope | 12 / 18 | 400 | none | Porcelain 55%, link 75% underlined |
| Success | Manrope | 20 / 28 | 400 | none | Porcelain |
| Wordmark (temporary) | Bounded | 14 | Black 900 | UPPER, 0.22em | Whiteout. Replace with the logotype SVG |

Bounded: upload ExtraLight / Regular / Black as custom fonts. Until then the prototype uses Archivo (200)
and Archivo Black as stand-ins, so final spacing may shift slightly once Bounded is in.
Manrope: Google Fonts, as in the test.

### Radii, sizes, effects

| Token | Value |
| --- | --- |
| Buttons (all) | outline pill: fill Blackout, 2px Saffron border, Saffron text and glyph, glow as above; radius 999, height 56 (nav pill 44) |
| Fields | radius 12, height 56, padding 0 × 16 (textarea: 5 rows, padding 14 × 16, vertical resize) |
| Form card | radius 16, padding 32 (mobile 20) |
| Banner | radius 24 (mobile 20), padding 64 (tablet 40, mobile 24), max width 1200 |
| Social buttons | 48 × 48 circle, 20px glyph |
| Background blur | banner 12px, form card 12px, fields 4px (same frosted panels as the test) |
| Focus | 2px Saffron outline, 2px offset (4px on pills) |
| Transitions | 200ms colour/border/glow; pills scale to 0.98 on press. No load animation |

## Page structure

1. **Background**: fixed full-screen image `assets/soglia.svg` (the test's artwork), grayscale,
   with a Dark Charcoal overlay at 60%. Page fill Dark Charcoal.
2. **Header** (not sticky, transparent): wordmark left; right: links Home · Metodo · Programma ·
   Guide · Test, then the "Fai il test" saffron pill. Below 960px the links move into a menu button (44px circle)
   that opens a stacked list; the pill stays visible.
3. **Banner**: a Frame, fill Banner Grey (option A) or Porcelain (option B), 1px border Porcelain 14% (none on B),
   radius 24, padding 64, max width 1200, centred. Inside, a horizontal Stack (gap 64)
   with two children sized 5fr / 7fr:
   - **Left** (vertical Stack, left aligned): Eyebrow "Contatti" → Headline "Domande?" (light) /
     "Contattaci." (strong), gap 16 → Lede "Nessun bot, nessuna attesa. Ti rispondiamo noi, e in fretta." (gap 20)
     → lead-in "Vuoi una risposta ancora più rapida? Scrivici su WhatsApp" (Manrope 16, gap 32)
     → WhatsApp button (gap 16) → socials block (gap 40).
   - **Right**: form card, a Frame with fill Dark Charcoal 88% + 12px blur, 1px border Porcelain 14%, radius 16, padding 32.
4. **Details row**: 1px top border Porcelain 10%, 3 equal columns: Email / Dove / Orari with
   `[… da confermare]` placeholders until the client sends them.
5. **Footer**: pending homepage, not designed yet.

## Components

### WhatsApp button: Link
- Outline pill (see Buttons), height 56, min width 240 (full width on mobile), WhatsApp glyph 20px left, label "WhatsApp" in Button caps.
- URL: `https://wa.me/<NUMBER>?text=Ciao%20Pietro%2C%20ti%20scrivo%20dal%20sito.%20Vorrei%20qualche%20informazione%20sul%20percorso.`
  Number pending: international format, digits only, no `+`. Open in new tab.

### Socials: 4 Link components
Order: Instagram, TikTok, Facebook, LinkedIn. 48px circle, fill Porcelain 8%, glyph Porcelain;
hover: fill Saffron, glyph Charcoal (200ms). Each needs an accessible name (the platform name).
URLs pending from the client. Glyphs are in `index.html` as inline SVG (Simple Icons paths).

### Form: Framer native Form
| Field | Framer input | Name | Required | Label | Placeholder |
| --- | --- | --- | --- | --- | --- |
| 1a | Text | `nome` | yes | Nome * | Il tuo nome |
| 1b | Text | `cognome` | yes | Cognome * | Il tuo cognome |
| 2 | Email | `email` | yes | Email * | nome@dominio.it |
| 3 | Phone / Text | `telefono` | yes | Numero di telefono * | +39 333 123 4567 |
| 4 | Text area (5 rows) | `messaggio` | yes | Messaggio * | Scrivi qui la tua domanda |

- Row 1 is a 2-column grid (gap 20); it stacks to one column below 560px. All other rows full width, gap 20.
- Submit: full-width outline pill, label "Invia" (Button caps, 700, 0.14em). Loading: spinner + "Invio in corso…", border Porcelain 28%, no glow.
- Under the button: "Inviando accetti l'informativa sulla privacy." with the link underlined (URL pending).
- Validation (same pattern as the test): invalid field gets a Saffron border and, beneath it, the
  saffron "!" icon + message in Porcelain:
  - empty required field → "Campo obbligatorio."
  - email → "Controlla l'indirizzo: sembra incompleto (es. nome@dominio.it)."
  - phone → "Controlla il numero: servono almeno 6 cifre."
  Messages appear on blur or submit and disappear as soon as the value is valid.
- Success: replace the form with the saffron check mark (56px circle) and
  "Messaggio inviato. Ti rispondiamo presto." centred vertically in the card.

## Breakpoints

| Breakpoint | Changes |
| --- | --- |
| ≥ 960 (desktop) | banner 2 columns 5/7, padding 64, radius 24; nav links visible |
| 640–959 (tablet) | banner stacks, padding 40, radius 24; nav links in the menu; WhatsApp full width |
| < 640 (mobile, designed at 390) | banner padding 24, radius 20; form card padding 20; page gutters 16 |
| < 560 | Nome and Cognome stack |

Mobile stacking order: eyebrow → headline → lede → WhatsApp (full width) → socials → form card
(Nome, Cognome, Email, Telefono, Messaggio, Invia, privacy) → details row.
Fields stay 56px tall with 16px text (so iOS Safari doesn't zoom the page on focus).

## Still pending from the client
WhatsApp number · social profile URLs · privacy policy URL · email, city, hours for the details row ·
Bounded font files · logotype SVG · the contact reference screenshot (to check the layout against).
