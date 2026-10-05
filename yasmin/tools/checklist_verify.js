// Verify SQUARESPACE-BUILD-CHECKLIST.md against the build (run from yasmin/):  node tools/checklist_verify.js
// 1. every visible text node on the seven pages appears verbatim in the checklist (a fresh walk, independent of the extractor);
// 2. every file path the checklist names exists;
// 3. the custom CSS block is at most 30 lines.
const { chromium } = require(process.env.PW || '/opt/node22/lib/node_modules/playwright');
const fs = require('fs'); const path = require('path');
const PAGES = ['index', 'projects', 'room-01-jackson-home', 'room-02-power-energy', 'room-03-rhode-island', 'room-04-littelfuse', 'private-view'];
const md = fs.readFileSync('SQUARESPACE-BUILD-CHECKLIST.md', 'utf8');
const flat = md.replace(/\s+/g, ' ');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1440, height: 900 } });
  let total = 0; const miss = [];
  for (const pg of PAGES) {
    await p.goto('file://' + path.resolve('site/' + pg + '.html') + '?theme=mono');
    const texts = await p.evaluate(() => {
      const out = []; const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT); let n;
      while ((n = w.nextNode())) {
        const t = n.textContent.replace(/\s+/g, ' ').trim(); if (!t) continue;
        const el = n.parentElement; if (el.closest('script,style,.theme-sw,[aria-hidden="true"]')) continue;
        // the wrong-password message is visible only in the #wrong state; checked too
        out.push(t);
      }
      return out;
    });
    for (const t of texts) { total++; if (!flat.includes(t)) miss.push(pg + ': ' + t.slice(0, 90)); }
  }
  await b.close();
  const paths = [...new Set([...md.matchAll(/`(site\/[^`\s]+)`/g)].map(m => m[1]))];
  const missingFiles = paths.filter(f => !f.includes('*') && !fs.existsSync(f));   // wildcards (site/*.html) are prose, not files
  const css = md.split('```css')[1].split('```')[0].trim().split('\n');
  console.log(`text nodes: ${total}, missing in checklist: ${miss.length}`); miss.forEach(m => console.log('  MISSING ' + m));
  console.log(`file paths named: ${paths.length}, missing on disk: ${missingFiles.length}`); missingFiles.forEach(f => console.log('  NO FILE ' + f));
  console.log(`custom CSS lines: ${css.length} (limit 30)`);
  console.log(`checkboxes: ${(md.match(/\[ \]/g) || []).length}`);
  process.exit(miss.length || missingFiles.length || css.length > 30 ? 1 : 0);
})();
