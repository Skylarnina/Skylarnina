/* Builds one static HTML page per screen state of ../index.html, for importing into Figma
   (html.to.design). Each page is the live DOM frozen after it has rendered: scripts removed,
   motion switched off, assets pointed at ../assets/.
   Run: node build-states.js   (needs Playwright; set PLAYWRIGHT_PATH if it isn't resolvable) */
const path = require('path'), fs = require('fs');
const { chromium } = require(process.env.PLAYWRIGHT_PATH || 'playwright');

const SRC = 'file://' + path.resolve(__dirname, '../index.html');
const OUT = __dirname;
const ANSWERS = { q1: 0, q2: 3, q3: 0, q4: 2, q5: 1, q6: 0, q7: 1, q8: 2 };
const wait = ms => new Promise(r => setTimeout(r, ms));
const settle = p => p.waitForTimeout(1300);

async function toQuestion(p, n) {           // n is 1-based
  await p.click('#start'); await settle(p);
  for (let i = 1; i < n; i++) { await p.click(`.opt[data-k="${ANSWERS['q' + i]}"]`); await settle(p); }
}
async function toEmail(p) { await toQuestion(p, 8); await p.click(`.opt[data-k="${ANSWERS.q8}"]`); await settle(p); }

const STATES = [
  ['01-ingresso', 'Ingresso', async p => {}],
  ['02-ingresso-riprendi', 'Ingresso · utente di ritorno', null, { answers: { q1: 0, q2: 3, q3: 0 } }],
  ...[1, 2, 3, 4, 5, 6, 7, 8].map(n => [`${String(n + 2).padStart(2, '0')}-domanda-${n}`, `Domanda ${n}`, p => toQuestion(p, n)]),
  ['11-domanda-1-selezionata', 'Domanda 1 · risposta selezionata', async p => {
    await p.click('#start'); await settle(p);
    await p.evaluate(() => { CONFIG.autoAdvanceMs = 1e9; });
    await p.click('.opt[data-k="0"]'); await wait(700);
  }],
  ['12-domanda-8-rivisitata', 'Domanda 8 · tornando indietro (pulsante Continua)', async p => {
    await toEmail(p); await p.click('#back'); await settle(p);
  }],
  ['13-email', 'Email', toEmail],
  ['14-email-errore', 'Email · errore', async p => {
    await toEmail(p); await p.fill('#email', 'mario@'); await p.click('#email-submit'); await wait(800);
  }],
  ['15-email-suggerimento', 'Email · suggerimento dominio', async p => {
    await toEmail(p); await p.fill('#email', 'mario@gmial.com'); await p.locator('#email').blur(); await wait(500);
  }],
  ['16-analisi', 'Analisi in corso', async p => {
    await toEmail(p);
    await p.evaluate(() => { CONFIG.processingMs = 1e7; });
    await p.fill('#email', 'mario@gmail.com'); await p.click('#email-submit'); await wait(1500);
  }, null, () => {                          // runs at freeze time, after the page's own timers
    const li = [...document.querySelectorAll('.steps li')];
    li[0].className = 'done'; li[1].className = 'active'; li[2].className = '';
  }],
  ['17-risultato', 'Risultato (anteprima)', async p => {
    await toEmail(p); await p.fill('#email', 'mario@gmail.com'); await p.click('#email-submit'); await wait(4200);
  }]
];

const FREEZE = `<style id="figma-freeze">
*, *::before, *::after { animation: none !important; transition: none !important; }
.mark-loader path { stroke-dashoffset: 0 !important; fill-opacity: 1 !important; }
</style>`;

(async () => {
  const browser = await chromium.launch();
  const index = [];
  for (const [file, label, go, seed, fixup] of STATES) {
    for (const [w, h, suffix] of [[390, 844, ''], [1440, 900, '-desktop']]) {
      const ctx = await browser.newContext({ viewport: { width: w, height: h } });
      if (seed) await ctx.addInitScript(s => localStorage.setItem('oltresoglia-test:v1', JSON.stringify(s)), seed);
      const p = await ctx.newPage();
      await p.goto(SRC); await settle(p);
      if (go) await go(p);
      await wait(400);
      let html = await p.evaluate(fix => {
        if (fix) (0, eval)('(' + fix + ')')();
        document.querySelectorAll('input').forEach(i => i.setAttribute('value', i.value));   // keep typed text
        document.querySelectorAll('script').forEach(s => s.remove());
        return '<!doctype html>\n' + document.documentElement.outerHTML;
      }, fixup ? fixup.toString() : null);
      html = html.replace('</head>', FREEZE + '\n</head>')
                 .replace(/src="assets\//g, 'src="../assets/')
                 .replace(/<title>[^<]*<\/title>/, `<title>${label}${suffix ? ' · desktop' : ''} — Test Oltresoglia</title>`);
      fs.writeFileSync(path.join(OUT, file + suffix + '.html'), html);
      await ctx.close();
    }
    index.push([file, label]);
    console.log('✓', file);
  }
  const list = index.map(([f, l]) => `<li><span>${f.slice(0, 2)}</span><a href="${f}.html">${l}</a><a class="d" href="${f}-desktop.html">desktop</a></li>`).join('\n');
  fs.writeFileSync(path.join(OUT, 'index.html'), `<!doctype html><html lang="it"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>Schermate per Figma — Test Oltresoglia</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@400..800&display=swap">
<style>body{margin:0;padding:48px 20px;background:#050505;color:#EBF0F2;font:500 16px/1.5 Manrope,Arial,sans-serif}
main{max-width:560px;margin:0 auto}h1{font-weight:800;letter-spacing:-.02em;margin:0 0 6px}p{color:#9CA3A7;margin:0 0 28px}
ol{list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:8px}
li{display:grid;grid-template-columns:32px 1fr auto;gap:12px;align-items:center;padding:14px 16px;border:1px solid rgba(235,240,242,.1);border-radius:12px;background:#0F1112}
li span{color:#EFC04D;font-weight:800;font-size:13px}a{color:#EBF0F2;text-decoration:none}a:hover{color:#EFC04D}
a.d{font-size:13px;color:#9CA3A7;border:1px solid rgba(235,240,242,.18);padding:4px 10px;border-radius:99px}</style></head>
<body><main><h1>Schermate per Figma</h1><p>Una pagina statica per ogni stato del test. Apri ciascuna e importala con html.to.design (390 px per mobile, 1440 px per desktop).</p>
<ol>${list}</ol></main></body></html>`);
  await browser.close();
})();
