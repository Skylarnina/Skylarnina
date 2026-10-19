# Ebook gratuiti: Framer handoff

Prototype: `oltresoglia/ebook-gratuiti/index.html` (listing) → `<ebook>.html` (pages 1–5) → pop-up → `grazie-<ebook>.html` (pages 6–10).
Built on the type system (`../TYPOGRAPHY.md`, `../styles/type.css`) and the same header, buttons and starry backdrop as Chi siamo.
Layout from Bibi's references of 17 October. Listing copy is Pietro's "EBOOK GRATUITI - PAGE 1", verbatim.

**v3: refined.** Light Porcelain page with black rounded blocks and a calm flow: no tilts, pins or hand-drawn marks.

## Pages

| Page | Content | Styles | Build in Framer |
|---|---|---|---|
| Listing · hero | Left: Display "Ebook gratuiti", Lead (intro). Right: a black rounded block (horizon artwork) with the five books in a gentle fan (−6° to +6°) rising over its top edge | Display, Lead | Fan = 5 book images in a Stack, slight rotation each, centre on top |
| Listing · cards | Five white cards with a 1px hairline and a soft shadow; left column 3, right column 2 offset 96px down. Each card: small index 01–05 top right, book left, Saffron rule, title, description, small button | Small (index), H3 (title), Body, Button | Hover: lift 4px, border turns Saffron 55%, deeper soft shadow (0.6s, cubic-bezier(.76,0,.24,1)). Phone: one column in order 01–05 |
| Listing · CTA | Black rounded block: "Il primo passo", "Scopri che tipo di professionista ad alta pressione sei", "Fai il test →" | Eyebrow, H1, Button | — |
| 1–5 · Ebook page | Black rounded feature panel: eyebrow link, H1 title, Lead, "Scarica gratis ora →" (opens the pop-up); the big book breaks out of the panel's top edge (+2°). The other four books sit over the panel's bottom edge with their titles below (links). Then a light section for the extra copy | Eyebrow, H1, Lead, Body, Small, Button | Panel overflow visible; "others" row overlaps the panel edge; hover lifts a book 6px |
| Pop-up | Unchanged: Porcelain frame around a dark panel; "Ci siamo quasi..", subtitle, ebook title in Saffron, book, Nome / Email, button, note | H3, Lead, H1, Body, Button, Small | — |
| 6–10 · Thank-you | Same feature panel: eyebrow (ebook title), H1 + Lead from Pietro's email, button back to the listing; the other four books below | Eyebrow, H1, Lead, Button, Small | — |

Card titles use H3 (Bounded Regular, sentence case) for a quieter, more editorial look than the bold caps in Bibi's first reference.
On the light page the books get a soft cast shadow; the Saffron glow behind books is kept only on the black panels.

Order of the cards: Gestire la fame · Allenarsi con continuità – Vol.1 · Gestire la pressione · Proteggere il sonno · Migliorare la digestione
(left: 1, 3, 5; right: 2, 4). "Allenarsi per un fisico completo – Vol.2" (coming soon) is left out for now, as Bibi asked.

## Form behaviour
- Errors follow the test / Contact pattern: Saffron border + "!" icon + message. Empty field: "Campo obbligatorio."; bad email:
  "Controlla l'indirizzo: sembra incompleto (es. nome@dominio.it)." Shown on submit or when leaving a field, cleared as soon as it is valid.
- On a valid submit the visitor goes to that ebook's thank-you page. The form also sends which ebook was chosen (hidden field `ebook`),
  so the email tool can tag the contact and send the right guide.
- Framer: use a native Form with a Redirect to the thank-you page; the email tool (Brevo / MailerLite / Sender) receives the
  submission and sends the guide. See the email-automation notes sent to Pietro.

## Pending from the client
- **Book covers** (Pietro is sending them): the cards and pages show placeholder covers ("Copertina in arrivo").
- **Copy for pages 1–10** (in Pietro's email): slots marked `[IT — pending client]`.
- Pop-up copy is taken from the reference image as written: "Ci siamo quasi.." (two dots) and "*tuoi dati sono protetti…"
  (no "I"). Confirm, or correct to "Ci siamo quasi…" / "*I tuoi dati sono protetti…".
- Consent: the reference has no consent checkbox. Sending the requested guide is fine without one; adding people to a
  newsletter later needs an unticked consent checkbox and a privacy-policy link.
- Buttons follow the site style (black fill, Saffron border, as asked in round 1); the reference shows filled yellow buttons.
