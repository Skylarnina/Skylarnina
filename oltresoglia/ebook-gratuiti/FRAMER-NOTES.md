# Ebook gratuiti: Framer handoff

Prototype: `oltresoglia/ebook-gratuiti/index.html` (listing) → `<ebook>.html` (pages 1–5) → pop-up → `grazie-<ebook>.html` (pages 6–10).
Built on the type system (`../TYPOGRAPHY.md`, `../styles/type.css`) and the same header, buttons and starry backdrop as Chi siamo.
Layout from Bibi's references of 17 October. Listing copy is Pietro's "EBOOK GRATUITI - PAGE 1", verbatim.

**v2: looser layout** on Sky's references (Creatiwise light/black flow, a dark book-app feature panel, books with depth).
Light Porcelain page with black rounded blocks; nothing sits on a rigid grid.

## Pages

| Page | Content | Styles | Build in Framer |
|---|---|---|---|
| Listing · hero | Left: Display "Ebook gratuiti" with a hand-drawn star, Lead (intro). Right: a black rounded block (horizon artwork) with the five books fanned out over its top edge (−14° to +14°) and the five titles as rotated pill tags that jump to each card | Display, Lead, Nav (tags) | Fan = 5 book images in a Stack, each rotated, centre one on top; hover lifts the fan 6px. Tags: pills, rotation per pill, hover straightens and fills Saffron |
| Listing · board | Five white cards, pinned (dark pin at the top), tilted −2° to +2°, left column 3 / right column 2 offset 160px down, dashed path behind. Each card: book popping out of the top-left corner (−5°), Saffron rule, title, description, button | H2, Body, Button | Cards as a component with a Rotation variable; hover: rotation 0, lift 6px, deeper shadow (0.6s, cubic-bezier(.76,0,.24,1)). Phone: one column, tilt reduced to 40% |
| Listing · CTA | Black rounded block: "Il primo passo", "Scopri che tipo di professionista ad alta pressione sei", "Fai il test →", Saffron squiggle | Eyebrow, H1, Button | — |
| 1–5 · Ebook page | Black rounded feature panel: eyebrow link, H1 title, Lead, "Scarica gratis ora →" (opens the pop-up); the big book on the right breaks out of the panel's top edge (+5°). The other four books peek over the panel's bottom edge with their titles below (links). Then a light section for the extra copy | Eyebrow, H1, Lead, Body, Small, Button | Panel overflow visible; "others" row with negative top margin so it overlaps the panel edge; hover lifts a book 10px |
| Pop-up | Unchanged: Porcelain frame around a dark panel; "Ci siamo quasi..", subtitle, ebook title in Saffron, book, Nome / Email, button, note | H3, Lead, H1, Body, Button, Small | — |
| 6–10 · Thank-you | Same feature panel: eyebrow (ebook title), H1 + Lead from Pietro's email, button back to the listing; the other four books peek below | Eyebrow, H1, Lead, Button, Small | — |

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
