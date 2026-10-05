// Extract the build, block by block, for SQUARESPACE-BUILD-CHECKLIST.md (run from yasmin/):
//   node tools/checklist_extract.js > content/checklist-blocks.json
// Renders each page in the built palette (mono) at 1440 and 390 and records, per section and per block:
// verbatim text (textContent, so the source spelling, not the uppercased display), the computed type style,
// the Fluid Engine column span (24 columns at desktop, 8 on mobile), image files and the ratio of the box
// they sit in, video files, the rules (borders) that become Line blocks, and the section's ground and padding.
const { chromium } = require(process.env.PW || '/opt/node22/lib/node_modules/playwright');
const path = require('path');
const PAGES = ['index', 'projects', 'room-01-jackson-home', 'room-02-power-energy', 'room-03-rhode-island', 'room-04-littelfuse', 'private-view'];

function extract() {
  const W = innerWidth, DESK = W >= 768, N = DESK ? 24 : 8, G = DESK ? 16 : 0;
  const T = el => el.textContent.replace(/\s+/g, ' ').trim();
  const px = v => Math.round(parseFloat(v) || 0);
  const box = el => { const r = el.getBoundingClientRect(); return { x: r.left, y: r.top + scrollY, w: r.width, h: r.height }; };
  function cols(el, full) {
    let left = 0, width = W;
    const wrap = full ? null : el.closest('.wrap,.stripe-wrap');
    if (wrap) { const r = wrap.getBoundingClientRect(), cs = getComputedStyle(wrap); left = r.left + parseFloat(cs.paddingLeft); width = r.width - parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight); }
    const r = el.getBoundingClientRect(), step = (width + G) / N;
    let s = Math.round((r.left - left) / step) + 1, e = Math.round((r.right - left + G) / step);
    s = Math.max(1, Math.min(N, s)); e = Math.max(s, Math.min(N, e));
    return [s, e];
  }
  // A text block's span is its grid area, not its rendered text box (paragraphs have a max-width):
  // find the nearest ancestor-or-self placed on the 24-column grid; use its placement when everything between
  // stacks in one column, otherwise fall back to the box.
  function tracks(e) { const cs = getComputedStyle(e); if (cs.display !== 'grid') return /flex/.test(cs.display) && !/column/.test(cs.flexDirection) ? 99 : 1; return cs.gridTemplateColumns.split(' ').length; }
  function gridCols(el) {
    if (!DESK) return null;
    for (let e = el; e && e.parentElement; e = e.parentElement) {
      const p = e.parentElement;
      if (tracks(p) === 24) {
        const cs = getComputedStyle(e); const st = parseInt(cs.gridColumnStart), en = cs.gridColumnEnd;
        if (isNaN(st)) return null;
        let end = /^span/.test(en) ? st + parseInt(en.split(' ')[1]) - 1 : (parseInt(en) < 0 ? 24 : parseInt(en) - 1);
        if (isNaN(end)) end = st;
        return [st, Math.min(24, end)];
      }
      if (tracks(p) !== 1) return null;
    }
    return null;
  }
  function style(el) {
    const cs = getComputedStyle(el);
    return { serif: cs.fontFamily.includes('Instrument'), size: Math.round(parseFloat(cs.fontSize) * 10) / 10, italic: cs.fontStyle === 'italic',
             upper: cs.textTransform === 'uppercase', weight: +cs.fontWeight, track: cs.letterSpacing, lh: cs.lineHeight, align: cs.textAlign, color: cs.color };
  }
  function rules(el) {
    const out = [];
    for (const [e, who] of [[el, 'self'], [el.parentElement, 'group']]) {
      if (!e) continue; const cs = getComputedStyle(e);
      for (const side of ['Top', 'Bottom']) {
        const w = parseFloat(cs['border' + side + 'Width']);
        if (w > 0 && cs['border' + side + 'Style'] !== 'none' && !/rgba\(\d+, \d+, \d+, 0\)/.test(cs['border' + side + 'Color'])) {
          if (who === 'group' && !((side === 'Top' && e.firstElementChild === el) || (side === 'Bottom' && e.lastElementChild === el))) continue;
          out.push({ side: side.toLowerCase(), color: cs['border' + side + 'Color'], width: w, who });
        }
      }
    }
    return out;
  }
  function list(el) {
    return [...el.children].filter(c => c.tagName === 'LI').map(li => {
      const own = [...li.childNodes].filter(n => !(n.nodeType === 1 && /^(UL|OL)$/.test(n.tagName))).map(n => n.textContent).join('').replace(/\s+/g, ' ').trim();
      const sub = [...li.children].filter(c => /^(UL|OL)$/.test(c.tagName));
      return { text: own, sub: sub.length ? list(sub[0]) : null, ordered: sub.length ? sub[0].tagName === 'OL' : false };
    });
  }
  function textLine(el, role) {
    // flex rows of spans (the Snippets tags) show a gap between items: keep a space there
    const flexText = getComputedStyle(el).display === 'flex' && el.children.length > 1 && [...el.children].every(c => c.tagName === 'SPAN');
    const o = { role, text: flexText ? [...el.children].map(T).join(' ') : T(el), style: style(el), tag: el.tagName.toLowerCase(), cls: el.className || '' };
    const ems = [...el.querySelectorAll('em,i')].map(T).filter(Boolean); if (ems.length) o.italic_parts = ems;
    const bs = [...el.querySelectorAll('b,strong')].map(T).filter(Boolean); if (bs.length) o.bold_parts = bs;
    const links = [...el.querySelectorAll('a')].map(a => [T(a), a.getAttribute('href')]); if (el.tagName === 'A') links.unshift([T(el), el.getAttribute('href')]);
    if (links.length) o.links = links;
    if (/^(UL|OL)$/.test(el.tagName)) { o.items = list(el); o.ordered = el.tagName === 'OL'; o.text = null; }
    return o;
  }
  const base = el => ({ id: el.dataset.id || el.dataset.ref || null, cols: (el.matches('h1,h2,h3,h4,p,ul,ol,blockquote,header,a.u,label,span') && !el.closest('.panel') && gridCols(el)) || cols(el, el.closest('.panels')), box: box(el), rules: rules(el), mt: px(getComputedStyle(el).marginTop) });
  function img(el, role) {
    const im = el.tagName === 'IMG' ? el : el.querySelector('img'); const holder = im.closest('.m,.logo-tile,.ss__frame') || im;
    const hb = holder.getBoundingClientRect(), a = im.closest('a');
    return { role, src: im.getAttribute('src'), alt: im.getAttribute('alt'), ratio: hb.width / hb.height, fit: getComputedStyle(im).objectFit,
             width_pct: im.style.width || null, full: a && a.getAttribute('href') && a.getAttribute('href').startsWith('assets/') ? a.getAttribute('href') : null };
  }
  const blocks = [];
  function push(kind, el, extra) { blocks.push(Object.assign({ kind }, base(el), extra)); }
  function walk(node) {
    for (const c of node.children) {
      if (c.matches('script,style,.theme-sw,.stripe,.stripe-wrap,hr.hairline,[aria-hidden="true"]')) continue;
      if (c.matches('.ss')) { push('slideshow', c, { slides: [...c.querySelectorAll('.ss__slide img')].map(i => ({ src: i.getAttribute('src'), alt: i.getAttribute('alt') })), ratio: c.querySelector('.ss__frame').getBoundingClientRect().width / c.querySelector('.ss__frame').getBoundingClientRect().height }); continue; }
      if (c.matches('figure.mod--video')) { const v = c.querySelector('video'); push('video', c, { src: v.getAttribute('src'), poster: v.getAttribute('poster'), vertical: c.matches('.mod--video-v'), caption: T(c.querySelector('figcaption span')), runtime: T(c.querySelector('.rt')), video_cols: cols(c.querySelector('.v'), false), caption_cols: cols(c.querySelector('figcaption'), false), caption_rules: rules(c.querySelector('figcaption')) }); continue; }
      if (c.matches('.mod')) { const mod = c.dataset.module; const start = blocks.length; walk(c); for (let i = start; i < blocks.length; i++) blocks[i].module = mod; if (blocks[start]) blocks[start].module_start = { mod, mt: px(getComputedStyle(c).marginTop) }; continue; }
      if (c.matches('figure') && !c.querySelector('img')) { const cap = c.querySelector('figcaption'); const ph = c.querySelector('.placeholder'); push('placeholder', c, { label: ph ? T(ph) : '', caption: cap ? T(cap) : null, ratio: ph ? ph.getBoundingClientRect().width / ph.getBoundingClientRect().height : null }); continue; }
      if (c.matches('figure')) { const cap = c.querySelector('figcaption'); push('image', c, Object.assign(img(c, 'figure'), { caption: cap ? T(cap) : null, caption_style: cap ? style(cap) : null })); continue; }
      if (c.matches('.panel')) {
        push('image', c.querySelector('.m'), Object.assign(img(c.querySelector('.m'), 'panel'), { panel: true }));
        push('text', c.querySelector('.no'), { lines: [textLine(c.querySelector('.no'), 'number')] });
        push('text', c.querySelector('h3'), { lines: [textLine(c.querySelector('h3'), 'name')] });
        blocks[blocks.length - 1].cols = blocks[blocks.length - 2].cols;   // the name spans its panel
        continue;
      }
      if (c.matches('.logo-tile')) { push('image', c, Object.assign(img(c, 'logo'), {})); continue; }
      if (c.matches('.cover')) {
        push('cover', c, Object.assign(img(c.querySelector('.m'), 'cover'), { scrim: getComputedStyle(c.querySelector('.m'), '::after').backgroundColor }));
        push('text', c.querySelector('.cover__title'), { lines: [textLine(c.querySelector('.cover__title'), 'title')] });
        continue;
      }
      if (c.matches('a.btn,button')) { push('button', c, { lines: [textLine(c, 'button')], href: c.getAttribute('href') }); continue; }
      if (c.matches('header.ch-head')) { push('text', c, { lines: [...c.children].map(e => textLine(e, e.matches('.no') ? 'number' : 'title')) }); continue; }
      if (c.matches('.stats')) {
        push('text', c.querySelector('.heads'), { lines: [...c.querySelector('.heads').querySelectorAll('span')].map(s => textLine(s, 'head')), stats_head: true });
        for (const d of c.querySelectorAll(':scope > div')) push('text', d, { lines: [...d.children].map(e => textLine(e, e.className)) });
        continue;
      }
      if (c.matches('dl.facts > div, dl.contact__rows > div, dl.meta__panel > div')) { push('text', c, { lines: [...c.children].map(e => textLine(e, e.tagName === 'DT' ? 'label' : 'value')) }); continue; }
      if (c.matches('.chindex')) { const ol = c.querySelector('ol'); push('text', c, { lines: [textLine(ol, 'index')], index: [...ol.children].map(li => ({ no: T(li.querySelector('span')), title: T(li.querySelector('a')), href: li.querySelector('a').getAttribute('href') })) }); continue; }
      if (c.matches('.pn a')) { push('text', c, { lines: [...c.children].map(e => textLine(e, e.className)), href: c.getAttribute('href'), pn: true }); continue; }
      if (c.matches('.row__t, .row__role, .card')) {
        if (c.matches('.card')) { const st = blocks.length; walk(c); const cc = cols(c, false); for (let i = st; i < blocks.length; i++) { blocks[i].cols = cc; blocks[i].href = c.getAttribute('href'); } continue; }
        push('text', c, { lines: [...c.children].map(e => textLine(e, e.className || e.tagName.toLowerCase())), href: c.closest('a') ? c.closest('a').getAttribute('href') : null }); continue;
      }
      if (c.matches('input')) { push('field', c, { type: c.type, label: T(document.querySelector('label[for="' + c.id + '"]') || c) }); continue; }
      if (c.matches('h1,h2,h3,h4,p,blockquote,ul,ol,label,a.u,span.label')) { push('text', c, { lines: [textLine(c, c.tagName.toLowerCase())] }); continue; }
      if (!c.children.length && T(c)) { push('text', c, { lines: [textLine(c, c.tagName.toLowerCase())] }); continue; }   // e.g. the footer's "© Yasmin Bajwa"
      walk(c);
    }
  }
  function centre(sec) {   // the Reflection is one centred column: every block takes the widest block's span
    const bs = sec.blocks; if (!bs.length) return;
    const w = bs.reduce((m, b) => (b.cols[1] - b.cols[0] > m[1] - m[0] ? b.cols : m), bs[0].cols);
    bs.forEach(b => { b.cols = w; b.centred = true; });
  }
  const sections = [];
  const tops = [...document.querySelectorAll('main > *, body > footer')];
  for (const s of tops) {
    if (s.matches('.stripe,hr.hairline,script')) { if (s.matches('hr.hairline')) sections.push({ sel: 'hr.hairline', blocks: [], box: box(s) }); continue; }
    const start = blocks.length; walk({ children: [s] });
    const cs = getComputedStyle(s);
    sections.push({ sel: s.tagName.toLowerCase() + (s.id ? '#' + s.id : '') + (s.className && typeof s.className === 'string' ? '.' + s.className.trim().split(/\s+/).join('.') : ''),
                    id: s.id || null, bg: cs.backgroundColor, pt: px(cs.paddingTop), pb: px(cs.paddingBottom), mt: px(cs.marginTop), box: box(s),
                    full: !s.matches('.wrap') && !s.querySelector(':scope > .wrap') , blocks: blocks.slice(start) });
    if (s.matches('.reflection-sec')) centre(sections[sections.length - 1]);
  }
  if (!tops.length) { walk(document.body); sections.push({ sel: 'body', blocks }); }
  return { width: W, sections };
}

(async () => {
  const b = await chromium.launch(); const out = {};
  for (const w of [1440, 390]) {
    const ctx = await b.newContext({ viewport: { width: w, height: w > 600 ? 900 : 844 } });
    for (const pg of PAGES) {
      const p = await ctx.newPage();
      await p.goto('file://' + path.resolve('site/' + pg + '.html') + '?theme=mono');
      await p.addStyleTag({ content: '.theme-sw{display:none!important}.fade{opacity:1!important;transform:none!important}' });
      await p.evaluate(async () => { await document.fonts.ready; await new Promise(r => setTimeout(r, 200)); });
      (out[pg] = out[pg] || {})[w] = await p.evaluate(extract);
      await p.close();
    }
    await ctx.close();
  }
  await b.close();
  process.stdout.write(JSON.stringify(out));
})();
