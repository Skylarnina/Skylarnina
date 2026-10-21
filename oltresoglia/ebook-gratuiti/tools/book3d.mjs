// 3D book mockup on a transparent background: cover + page block + fanned "turning" pages + soft shadow.
import { chromium } from 'playwright'
import { readFileSync } from 'node:fs'
const [SRC, OUT, ...slugs] = process.argv.slice(2)
const b = await chromium.launch()
const p = await (await b.newContext({ viewport: { width: 1000, height: 1100 }, deviceScaleFactor: 2 })).newPage()
for (const slug of slugs) {
  const img = 'data:image/png;base64,' + readFileSync(`${SRC}/${slug}.png`).toString('base64')
  // Painted back-to-front (no preserve-3d, so layers can't intersect). Each layer carries its own perspective.
  const T = (dx, dz, ry = 0) => `transform: perspective(2400px) rotateY(${-24 + ry}deg) rotateX(2deg) translateX(${dx}px) translateZ(${dz}px)`
  // fanned page edges: the deeper the page, the further it peeks out on the right and the more it curls
  const fan = [
    [66, -40, 10.5, 46], [57, -35, 9, 40], [48, -30, 7.6, 34], [40, -25, 6.2, 28], [32, -20, 5, 22], [24, -15, 3.8, 17], [17, -11, 2.7, 13], [10, -7, 1.6, 9], [4, -3, .7, 6],
  ]
  const pages = fan.map(([dx, dz, ry, curl], k) =>
    `<div class="pg" style="${T(dx, dz, ry)}; border-radius: 2px ${curl}px ${curl * 1.3}px 2px; filter: brightness(${0.93 + k * 0.01})"></div>`).join('')
  await p.setContent(`<!doctype html><html><head><style>
    html,body{margin:0;background:transparent}
    .scene{width:1000px;height:1100px;display:grid;place-items:center}
    .book{position:relative;width:520px;height:735px}
    .book > *{position:absolute;inset:0;transform-origin:left center}
    .shadow{inset:auto -40px -40px 10px !important;height:80px;background:radial-gradient(closest-side,rgba(0,0,0,.6),transparent);filter:blur(16px)}
    .back{background:#141414;border-radius:3px 8px 8px 3px}
    .pg{top:5px !important;bottom:5px !important;
      background:linear-gradient(90deg,#d8d3c9 0%,#f7f5f0 5%,#fffefb 60%,#f0ede6 90%,#cdc7bb 100%);
      box-shadow:1px 0 0 rgba(0,0,0,.18),3px 0 6px rgba(0,0,0,.12)}
    .cover{border-radius:2px 5px 5px 2px;overflow:hidden;box-shadow:0 1px 2px rgba(0,0,0,.45),18px 26px 50px rgba(0,0,0,.35)}
    .cover img{width:100%;height:100%;display:block;object-fit:cover}
    .cover::after{content:'';position:absolute;inset:0;background:
      linear-gradient(90deg,rgba(0,0,0,.6) 0,rgba(255,255,255,.22) 1.4%,rgba(0,0,0,.28) 3%,transparent 6%),
      linear-gradient(115deg,transparent 35%,rgba(255,255,255,.09) 52%,transparent 68%)}
  </style></head><body><div class="scene"><div class="book" id="book">
    <div class="shadow" style="${T(60, -40)}"></div>
    <div class="back" style="${T(70, -44, 11.5)}"></div>${pages}
    <div class="cover" style="${T(0, 0)}"><img src="${img}"></div>
  </div></div></body></html>`)
  await p.waitForTimeout(200)
  const box = await p.evaluate(() => {
    const r = [...document.querySelectorAll('.cover,.pg,.back')].map((e) => e.getBoundingClientRect())
    const x0 = Math.min(...r.map((q) => q.left)), y0 = Math.min(...r.map((q) => q.top)), x1 = Math.max(...r.map((q) => q.right)), y1 = Math.max(...r.map((q) => q.bottom))
    return { x: x0, y: y0, width: x1 - x0, height: y1 - y0 }
  })
  const pad = 70
  await p.screenshot({ path: `${OUT}/${slug}-3d.png`, omitBackground: true,
    clip: { x: Math.max(0, box.x - pad), y: Math.max(0, box.y - pad / 2), width: Math.min(1000, box.width + pad * 2), height: Math.min(1100, box.height + pad * 1.5) } })
  console.log(slug, Math.round(box.width), 'x', Math.round(box.height))
}
await b.close()
