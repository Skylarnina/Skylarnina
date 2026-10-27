# Snapshots marquee: setup

Code: `snapshots-marquee.html` (paste the whole file into one Code Block).

What it does:
- A strip of photos that glides slowly and continuously to the left, looping without a gap: **4 photos in view on a computer**, 3 on a tablet, 2 on a phone.
- Slows to a stop while the mouse is over it (so a visitor can pick a photo), while it is scrolled out of view, and while a photo is enlarged; then glides on again.
- Visitors can drag it (mouse) or swipe it (phone) by hand. A Pause / Play link sits under the strip.
- Clicking (tapping) a photo opens it large on a dark background (lightbox): arrows, keyboard ← → and Esc, swipe on phones, click outside to close.
- People who have "reduce motion" switched on in their device settings get the strip standing still; they can press Play or drag it.

## 1. Get the image addresses (all 21 at once)

Squarespace doesn't show image addresses in the editor, so upload the photos into a gallery first and copy all the addresses in one go.

**a. Upload the 21 photos into a gallery that stays on the site**
1. **Pages → Not Linked → +** → Blank page. Name it `Snapshot photos (do not delete)`. It's hidden from the menu; it just keeps the photos stored on Squarespace. If the photos were deleted, the strip would show empty squares.
2. On that page: **Edit → + → Gallery** block → **Add images** → select all 21 files at once → upload. Drag them into the order you want in the strip. **Save.**

**b. Copy the addresses**
1. Open that page in its own tab, not inside the editor: e.g. `yasminbajwa.com/snapshot-photos` (the URL is in the page's settings → URL slug).
2. Open the browser **Console**: in Chrome, `Ctrl+Shift+J` (Windows) or `Cmd+Option+J` (Mac).
3. Chrome may refuse the first paste. If it does, type `allow pasting`, press Enter, then paste.
4. Paste the code below (also in `get-photo-addresses.js`) and press **Enter**. It should say **21 photos copied**.

```js
(function(){var D={"4P7BVQATO5BI":"Violins of Hope exhibit","snippet-01":"Violins of Hope exhibit","IMG_0413":"A gallery mid-install","snippet-02":"A gallery mid-install","IMG_0420":"A gallery mid-install under a skylight","snippet-03":"A gallery mid-install under a skylight","IMG_0603":"An exhibit gallery with panels and cases","snippet-04":"An exhibit gallery with panels and cases","IMG_2745":"Painting supplies, a painted pumpkin and a charcuterie board","snippet-05":"Painting supplies, a painted pumpkin and a charcuterie board","IMG_3249":"Street mural: a portrait with a lightbulb hat","snippet-06":"Street mural: a portrait with a lightbulb hat","IMG_3327":"An ornate painted ceiling","snippet-07":"An ornate painted ceiling","IMG_3358":"A crown and sceptre on red","snippet-08":"A crown and sceptre on red","IMG_3636":"A pastry case of custard tarts","snippet-09":"A pastry case of custard tarts","IMG_4523":"Yasmin looking at a framed painting","snippet-10":"Yasmin looking at a framed painting","IMG_4528":"A hat exhibit","snippet-11":"A hat exhibit","IMG_6146":"A blazer hanging outside a vintage shop","snippet-12":"A blazer hanging outside a vintage shop","IMG_6193":"A robotic head sculpture","snippet-13":"A robotic head sculpture","IMG_6251":"Orangutans playing chess, a diorama","snippet-14":"Orangutans playing chess, a diorama","IMG_6252":"Marble figures installation with digital counters","snippet-15":"Marble figures installation with digital counters","IMG_6811":"A carved standing figure","snippet-16":"A carved standing figure","IMG_6824":"Bookshop shelves","snippet-17":"Bookshop shelves","IMG_7200":"Measuring tape against a gallery wall","snippet-18":"Measuring tape against a gallery wall","IMG_7250":"Anatomical fashion pieces on mannequins","snippet-19":"Anatomical fashion pieces on mannequins","IMG_7316":"The Power & Energy column being installed","snippet-20":"The Power & Energy column being installed","IMG_7390":"The Henry Ford cap on a notebook with a handwritten note","snippet-21":"The Henry Ford cap on a notebook with a handwritten note"};var K=Object.keys(D),seen={},out=[],imgs=document.querySelectorAll('[class*="gallery"] img,[class*="slideshow"] img');if(!imgs.length)imgs=document.querySelectorAll('img');imgs.forEach(function(im){var s=(im.getAttribute('data-src')||im.getAttribute('data-image')||im.currentSrc||im.src||'').split('?')[0];if(!/squarespace/.test(s)||seen[s])return;seen[s]=1;var f=decodeURIComponent(s.split('/').pop()).toLowerCase(),d=im.alt||'';K.forEach(function(k){if(f.indexOf(k.toLowerCase())>-1)d=D[k];});out.push("    ['"+s+"', '"+d.replace(/\\/g,'').replace(/'/g,"\\'")+"'],");});copy(out.join('\n'));console.log(out.length+' photos copied. Paste them into PHOTOS in the code:\n'+out.join('\n'));})();
```

It already knows the descriptions of her 21 snapshots (from their file names), so you don't need to type them. Any photo it doesn't recognise keeps the description you gave it in Squarespace, or an empty one you can fill in.

**c. Put them in the code**
In `snapshots-marquee.html`, inside `var PHOTOS = [ ... ];`, select the three example lines and paste (`Ctrl/Cmd + V`). You should now have 21 lines, each like:
`['https://images.squarespace-cdn.com/…/IMG_7316.jpg', 'The Power & Energy column being installed'],`

**By hand instead (slower):** on that page, right-click each photo → **Copy image address**, and paste it into a line like the one above.

## 2. Add the code
1. Edit the page → the Snapshots section.
2. Add a **Code** block under the section heading and stretch it to the **full width of the section** (all 24 columns), so 4 photos have room. Paste the whole code. **Display Source: off.** Save.
3. Remove the old slideshow from the Snapshots section, if there is one. Keep the hidden `Snapshot photos` page.
4. Open the page in a new tab, not in the editor: Squarespace doesn't run code inside the editor, so it may show "Script disabled" there. That's normal.

## Settings (top of the code)
- `PHOTOS_IN_VIEW = 4` — photos visible at once on a computer.
- `SPEED = 40` — 25 slow, 40 calm, 70 lively.
- `ASPECT_RATIO = '4/5'` — photo shape: `'1/1'` square, `'3/2'` landscape.
- `GAP = 16` — space between photos.
- `HINT` — the small line under the strip; `''` hides it.
- To add a photo later: add it to the gallery on the hidden `Snapshot photos` page, run the Console step again, and replace the `PHOTOS` lines.

## Notes
- JavaScript in Code Blocks needs a Squarespace **Core plan or higher** (it doesn't run on Personal/Basic).
- Photos hosted on Squarespace are automatically requested at 800px for the strip and 2500px for the enlarged view, so the page stays fast.
- The text and controls take the section's own text colour and font, so they match whatever colour theme the section uses.
