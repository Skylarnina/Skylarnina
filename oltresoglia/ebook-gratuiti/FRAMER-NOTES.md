# Ebook gratuiti: Framer handoff

Prototype: `oltresoglia/ebook-gratuiti/index.html` (listing) → `<ebook>.html` (pages 1–5) → pop-up → `grazie-<ebook>.html` (pages 6–10).
Built on the type system (`../TYPOGRAPHY.md`, `../styles/type.css`) and the same header, buttons and starry backdrop as Chi siamo.
Layout from Bibi's references of 17 October. Listing copy is Pietro's "EBOOK GRATUITI - PAGE 1", verbatim.

**Black / white, as on Chi siamo:** full-width black and white (Porcelain) sections; on white, all text is dark and there are no
black blocks. Listing: black header with the title and intro, then the white section with the banner (white, subtle Saffron
gradient at the bottom) and white cards (Saffron border, Saffron tint at the bottom). Ebook page: black hero with the book and
button, white section below for the extra copy. Thank-you page: black header bar, white page. The pop-up stays dark, as in the reference.

## Pages

| Page | Content | Styles |
|---|---|---|
| Listing | Black: Display "Ebook gratuiti" + Lead (intro). White: a banner (radius 24, subtle Saffron gradient at the bottom) holding 5 cards in two columns: 3 left, 2 right. Card: book left; Saffron rule, title, description, button right | Display, Lead, H2 (card title), Body, Button |
| 1–5 · Ebook page | Large book left (Saffron glow); eyebrow link "Ebook gratuiti", H1 title, Lead (description), button "Scarica gratis ora →" opens the pop-up. White section below: eyebrow + Lead + Body (extra copy from Pietro's email) | Eyebrow, H1, Lead, Body, Button |
| Pop-up | Porcelain frame (8px) around a dark panel; "Ci siamo quasi.." (H3), subtitle (Lead), ebook title in Saffron (H1); book left, form right: Nome, Email (icons inside the fields), button "Ricevi l'ebook gratuito ora →", note (Small) | H3, Lead, H1, Body (inputs), Button, Small |
| 6–10 · Thank-you | Book left; eyebrow with the ebook title, H1 + Lead from Pietro's email, button back to the listing | Eyebrow, H1, Lead, Button |

Order of the cards: Gestire la fame · Allenarsi con continuità – Vol.1 · Gestire la pressione · Proteggere il sonno · Migliorare la digestione.
"Allenarsi per un fisico completo – Vol.2" (coming soon) is left out for now, as Bibi asked; the 6th slot (bottom right) stays empty.

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
