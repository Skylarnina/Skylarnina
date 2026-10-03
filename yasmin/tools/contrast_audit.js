// Rendered contrast audit (prototype themes). Run from yasmin/:
//   node tools/contrast_audit.js [themes] [pages] > content/contrast-audit.json
// For every visible piece of text on each page, in each theme, at 1440px (or WIDTH):
//   1. read its colour (alpha included) and size from the browser,
//   2. hide all text (colour transparent; nothing moves) and take a screenshot,
//   3. measure the text colour against the pixels actually behind each line box
//      (so text on tinted photos is checked against the photo, not an assumed ground).
// Each line box is sampled 1-3px inside its edges (a rule touching the box is not the text's ground).
// A pair passes when 95% of the background pixels give at least 4.5:1 (3:1 for 24px+ or 18.66px+ bold).
// Hover states are not covered.
const { chromium } = require(process.env.PW || '/opt/node22/lib/node_modules/playwright');
const path = require('path'); const fs = require('fs');
const WIDTH = +(process.env.WIDTH || 1440);   // WIDTH=390 for the phone layout
const THEMES = (process.argv[2] || 'mono,cream,cream-bold,venues,venues-bold').split(',');
const PAGES = (process.argv[3] || 'index,projects,room-01-jackson-home,room-02-power-energy,room-03-rhode-island,room-04-littelfuse,private-view').split(',');
let fontroute = null; try { fontroute = require(process.env.FONTROUTE); } catch (e) {}

const lin = v => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); };
const L = (r, g, b) => 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b);
const ratio = (a, b) => { const [x, y] = a > b ? [a, b] : [b, a]; return (x + 0.05) / (y + 0.05); };

(async () => {
  const b = await chromium.launch(); const out = [];
  const { PNG } = require(process.env.PW_UTILS || '/opt/node22/lib/node_modules/playwright/node_modules/playwright-core/lib/utilsBundle');   // pngjs, bundled with Playwright
  for (const theme of THEMES) {
    const ctx = await b.newContext({ viewport: { width: WIDTH, height: WIDTH < 600 ? 844 : 900 }, reducedMotion: 'reduce' });
    if (fontroute) await fontroute(ctx);
    for (const pg of PAGES) {
      const p = await ctx.newPage();
      await p.goto('file://' + path.resolve('site/' + pg + '.html') + '?theme=' + theme);
      await p.addStyleTag({ content: '.theme-sw{display:none!important}.fade{opacity:1!important;transform:none!important}' });
      await p.evaluate(async () => { document.querySelectorAll('img[loading]').forEach(i => i.loading = 'eager'); await document.fonts.ready;
        await Promise.race([Promise.all([...document.images].map(i => i.complete ? 1 : new Promise(r => { i.onload = i.onerror = r; }))), new Promise(r => setTimeout(r, 5000))]);
        const id = setInterval(() => {}, 1e6); for (let i = 0; i <= id; i++) clearInterval(i); });
      await p.waitForTimeout(300);
      const items = await p.evaluate(() => {
        const res = []; const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
        let n; while ((n = w.nextNode())) {
          if (!n.textContent.trim()) continue; const el = n.parentElement;
          if (!el || el.closest('script,style,.theme-sw,[aria-hidden="true"]')) continue;
          if (!el.checkVisibility({ opacityProperty: true, visibilityProperty: true })) continue;
          const cs = getComputedStyle(el); const r = document.createRange(); r.selectNodeContents(n);
          const rects = [...r.getClientRects()].filter(q => q.width > 2 && q.height > 2).map(q => [q.x, q.y + scrollY, q.width, q.height]);
          if (!rects.length) continue;
          let op = 1; for (let e = el; e; e = e.parentElement) op *= parseFloat(getComputedStyle(e).opacity);
          const REG = ['.lock__box', '.lock', '.panel', '.cover', '.bar', '.dochead', '.meta', '.chindex', '.reflection-sec', '#snippets', '#projects', '#contact', '.foot', '.hero', '.pn', '.grid2', '.chapter', 'main'];
          let region = 'page'; for (const c of REG) { const a = el.closest(c); if (a) { region = c === '.panel' ? 'panel ' + ([...a.parentElement.children].indexOf(a) + 1) : c; break; } }
          res.push({ region, text: n.textContent.trim().slice(0, 60), sel: el.tagName.toLowerCase() + (el.className && typeof el.className === 'string' ? '.' + el.className.trim().split(/\s+/).join('.') : ''),
                     color: cs.color, size: parseFloat(cs.fontSize), weight: parseInt(cs.fontWeight), op, rects });
        }
        return res;
      });
      await p.addStyleTag({ content: '*,*::before,*::after{color:transparent!important;text-decoration-color:transparent!important;text-shadow:none!important}' });
      await p.waitForTimeout(150);
      const H = await p.evaluate(() => document.documentElement.scrollHeight);
      const buf = await p.screenshot({ fullPage: true, clip: { x: 0, y: 0, width: WIDTH, height: H } });
      const png = PNG.sync.read(buf);
      for (const it of items) {
        const m = it.color.match(/rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?/);
        const [cr, cg, cb] = [+m[1], +m[2], +m[3]]; const ca = (m[4] === undefined ? 1 : +m[4]) * it.op;
        const ratios = [];
        for (const [x0, y0, w0, h0] of it.rects) {
          const ins = Math.min(3, h0 / 6), x = x0 + 1, y = y0 + ins, w = w0 - 2, h = h0 - 2 * ins;   // inside the line box: rules touching its edge are not the text's ground
          const step = Math.max(1, Math.floor(Math.min(w, h) / 12));
          for (let yy = Math.floor(y); yy < y + h && yy < png.height; yy += step)
            for (let xx = Math.floor(x); xx < x + w && xx < png.width; xx += step) {
              const i = (png.width * yy + xx) * 4; const br = png.data[i], bg = png.data[i + 1], bb = png.data[i + 2];
              const fr = cr * ca + br * (1 - ca), fg = cg * ca + bg * (1 - ca), fb = cb * ca + bb * (1 - ca);
              ratios.push(ratio(L(fr, fg, fb), L(br, bg, bb)));
            }
        }
        if (!ratios.length) continue;
        ratios.sort((a, b) => a - b);
        const p5 = ratios[Math.floor(ratios.length * 0.05)];
        const large = it.size >= 24 || (it.size >= 18.66 && it.weight >= 700);
        const need = large ? 3 : 4.5;
        out.push({ theme, width: WIDTH, page: pg, region: it.region, text: it.text, sel: it.sel, size: it.size, color: it.color, p5: +p5.toFixed(2), min: +ratios[0].toFixed(2), need, pass: p5 >= need });
      }
      await p.close();
    }
    await ctx.close();
  }
  await b.close();
  process.stdout.write(JSON.stringify(out));
})();
