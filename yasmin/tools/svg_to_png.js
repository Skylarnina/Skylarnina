// Render an SVG to a transparent PNG (used by tools/build_phase2_assets.py):  node tools/svg_to_png.js in.svg out.png width
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const path = require('path'); const fs = require('fs');
(async () => {
  const [inp, out, w] = process.argv.slice(2);
  const b = await chromium.launch(); const p = await b.newPage();
  const svg = fs.readFileSync(inp, 'utf8');
  const vb = svg.match(/viewBox="([\d.\s-]+)"/)[1].split(/\s+/).map(Number);
  const W = +w, H = Math.round(W * vb[3] / vb[2]);
  await p.setViewportSize({ width: W, height: H });
  await p.setContent(`<html><body style="margin:0;background:transparent"><img src="data:image/svg+xml;base64,${Buffer.from(svg).toString('base64')}" style="display:block;width:${W}px;height:${H}px"></body></html>`);
  await p.waitForTimeout(200);
  await p.screenshot({ path: out, omitBackground: true, clip: { x: 0, y: 0, width: W, height: H } });
  await b.close();
})();
