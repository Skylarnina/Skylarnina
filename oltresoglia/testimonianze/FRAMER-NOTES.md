# Testimonianze: Framer handoff

Prototype: `oltresoglia/testimonianze/index.html`. Structure from the Apex Coaching Academy reference (auto-scrolling rows),
message card from Bibi's visual (25 Oct). Copy: title and description from Bibi, verbatim.

## Structure

| Part | Content | Styles |
|---|---|---|
| Head (centred) | H1 "Meno grasso. Più atletici. Più forti nel lavoro e nella vita." + Lead (description) | H1, Lead |
| Row 1 · messages | Cards scrolling left: black #111, 2px Saffron border, radius 26, padding 34. **Name in bold at the same size as the text** (Pietro), then the message, tick bottom right | Body (bold name), Body |
| Row 2 · before / after | Square cards scrolling right: two halves "Prima" / "Dopo" with the photos, OLTRESOGLIA label bottom left | Small (labels), Button (label) |

## Build in Framer
- Each row is Framer's built-in **Ticker** component (Insert → Ticker): direction Left for messages, Right for photos;
  speed ≈ 40 (messages) / 35 (photos); **Hover → Slow down 0** (pauses, like the reference); gap 22; fade edges on (6%).
- Message card = one component with two text props (Nome, Messaggio); variable height up to the longest message, min 340.
- Photo card = one component with two image props (Prima, Dopo), each Fill, centred on the face.
- Reduced motion: Ticker respects the OS setting.

## Content (pending)
- Messages: from the "FEEDBACK" WhatsApp group; client name only (first name). If the name isn't there, Pietro says to invent one.
  Card 1 already has the message from Bibi's reference (typos kept as sent: "altre bilancia", "e' che").
- Photos: before / after pairs, same crop for both halves.
- The tick is Saffron here (the reference shows it green; the brand palette has no green). Easy to switch if they prefer green.
