// Dump every data-id / data-ref / data-added element of the built pages, in DOM order.
// Run from yasmin/:  node tools/dom_text.js > content/dom.json
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const path = require('path');
const DIR = process.argv[2] || 'site';   // 'wireframes' to check the wireframe files
const pages = ['index', 'projects', 'room-01-jackson-home', 'room-02-power-energy', 'room-03-rhode-island', 'room-04-littelfuse', 'private-view'];
(async () => {
  const b = await chromium.launch();
  const out = {};
  for (const w of [1440, 390]) {
    const p = await b.newPage({ viewport: { width: w, height: 900 } });
    for (const pg of pages) {
      await p.goto('file://' + path.resolve(DIR + '/' + pg + '.html'), { waitUntil: 'domcontentloaded' });
      out[`${pg}@${w}`] = await p.evaluate(() => [...document.querySelectorAll('[data-id],[data-ref],[data-added]')].map((el, i) => {
        const cs = getComputedStyle(el);
        const visible = el.getClientRects().length > 0 && cs.visibility !== 'hidden' && cs.display !== 'none';
        return { i, id: el.dataset.id || null, ref: el.dataset.ref || null, added: el.dataset.added || null,
                 kind: el.dataset.kind || null, tag: el.tagName.toLowerCase(), text: el.innerText, visible };
      }));
    }
    await p.close();
  }
  await b.close();
  process.stdout.write(JSON.stringify(out));
})();
