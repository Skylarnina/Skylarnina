# Snapshots slideshow: setup

Code: `snapshots-slideshow.html` (paste the whole file into one Code Block).

What it does:
- Moves to the next photo every 4 seconds with a soft fade.
- Pauses while the mouse is over it, while it is scrolled out of view, and while the enlarged view is open.
- Visitors can still use the arrows (or swipe on a phone), plus a Pause / Play link under the photo.
- Clicking a photo opens it large on a dark background (lightbox): arrows, keyboard ← → and Esc, swipe on phones, click outside to close.
- People who have "reduce motion" switched on in their device settings get the slideshow paused; they can press Play.

## 1. Get the image addresses (before removing the current slideshow)

**Quick way (all photos at once):**
1. Open the page with the current slideshow in its own browser tab, as a visitor sees it (not inside the Squarespace editor).
2. Right-click anywhere → **Inspect** → **Console** tab.
3. Paste this, press Enter:

```js
(function(){var seen={},out=[],imgs=document.querySelectorAll('[class*="gallery"] img,[class*="slideshow"] img');if(!imgs.length)imgs=document.querySelectorAll('img');imgs.forEach(function(im){var s=(im.getAttribute('data-src')||im.getAttribute('data-image')||im.currentSrc||im.src||'').split('?')[0];if(!/squarespace/.test(s)||seen[s])return;seen[s]=1;out.push("    ['"+s+"', '"+(im.alt||'').replace(/'/g,"\\'")+"'],");});copy(out.join('\n'));console.log(out.length+' photos copied:\n'+out.join('\n'));})();
```

4. It says how many photos it copied. In the code, replace the three example lines inside `var PHOTOS = [ ... ];` with what you copied (Ctrl/Cmd + V).
5. Check the list: one line per photo, in the order you want; delete any line that isn't a snapshot (e.g. a logo). Fill in a short description in the second quotes where it's empty.

**By hand:** right-click each photo → **Copy image address**, and paste it into a line like
`['https://images.squarespace-cdn.com/…/photo.jpg', 'Short description'],`

## 2. Add the code
1. Edit the page → the Snapshots section.
2. Add a **Code** block where the slideshow is, the same width. Paste the whole code. **Display Source: off.** Save.
3. Remove the old slideshow (gallery) block.
4. Open the page in a new tab, not in the editor: Squarespace doesn't run code inside the editor, so it may show "Script disabled" there. That's normal.

## Settings (top of the code)
- `SECONDS_PER_PHOTO = 4` — change the speed.
- `ASPECT_RATIO = '4/5'` — frame shape: `'1/1'` square, `'3/2'` landscape.
- To add a photo later: upload it anywhere on the site (e.g. an image block on a hidden page), copy its address, add a line to `PHOTOS`.

## Notes
- JavaScript in Code Blocks needs a Squarespace **Core plan or higher** (it doesn't run on Personal/Basic).
- Photos hosted on Squarespace are automatically requested at 1000px for the slideshow and 2500px for the enlarged view, so the page stays fast.
- The text and controls take the section's own text colour and font, so they match whatever colour theme the section uses.
