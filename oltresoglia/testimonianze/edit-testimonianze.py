"""Testimonianze page (artifact 4URKbBXp), Bibi 30 Oct: new order.
1. 17 video testimonials in a horizontal carousel   2. 45 before/after photos   3. 20 written testimonials (name underneath).
The content is on WeTransfer: every slot is a placeholder with its number, ready to swap.
Writes the repo file (fonts inlined) and the artifact source (fonts as ./assets/ files).
"""
import re, sys
S = '/tmp/claude-0/-home-user-Skylarnina/d3a326d7-8059-5f41-b39f-346e6a334423/scratchpad'
REPO = '/home/user/Skylarnina/oltresoglia/testimonianze/oltresoglia-testimonianze-pagina.html'
ASSETS = ['78ebecc50a9ae7e198f8b13497a5a81e', 'db0e506ffc4f86db9432a382ad0974a8', '41efe2b321d4cd2e69964afdc9d224d8',
          '5f651b234d14e5e6c0c520868640f91e', '576805f56c6be2a6272f8f8001bedd3a', '58f6062e479663611935cc0642627940']
VIDEOS, PHOTOS, QUOTES, PHOTOS_FIRST = 17, 45, 20, 12
MARCO = ("Forse anche più in discesa di quanto riportato poiché ero con altre bilancia. Ma ciò che conta per ora e' che mi sento "
         "con più energie e riesco ad allenarmi costantemente seguendo bene alimentazione. Per il peso credo calerà continuando così")

src = open(REPO).read()
start, end = '  <!-- ============ INTRO ============ -->', '  <!-- ============ INIZIA DA QUI ============ -->'
assert src.count(start) == 1 and src.count(end) == 1

CSS = """
.eyebrow{font-weight:600;font-size:13px;letter-spacing:.16em;color:#8A5A00}
.h2{margin:0;font-family:'Bounded',sans-serif;font-weight:800;font-size:clamp(26px,3vw,38px);line-height:1.15;letter-spacing:-.01em;color:#0D0D0D;max-width:760px;text-wrap:balance}
.rule{width:72px;height:3px;background:#F9BF58}
.sec-head{display:flex;flex-direction:column;gap:22px}
.sec-text{margin:0;font-size:17px;line-height:1.6;color:#5E5A52;max-width:640px}
.jump{display:flex;align-items:baseline;gap:14px;padding:12px 0;border-top:1px solid #2A2A2A;color:#E8E4DC;text-decoration:none;font-size:15px}
.jump:first-of-type{border-top:0}
.jump b{font-family:'Bounded',sans-serif;font-weight:800;font-size:22px;color:#F9BF58;min-width:2ch}
.jump:hover{color:#FFFFFF}
/* 1 · video carousel */
.vwrap{box-sizing:border-box;padding:0 20px}
.vsec{border-radius:28px;background:#141414;color:#FFFFFF;padding:clamp(56px,7vw,96px) 0;display:flex;flex-direction:column;gap:40px;overflow:hidden}
.vsec .eyebrow{color:#F9BF58}.vsec .h2{color:#FFFFFF}.vsec .sec-text{color:#BDB8AE}
.vhead{max-width:1200px;width:100%;margin:0 auto;padding:0 24px;display:flex;flex-wrap:wrap;align-items:flex-end;justify-content:space-between;gap:24px 40px}
.vctrl{display:flex;align-items:center;gap:12px}
.vcount{font-size:14px;letter-spacing:.12em;color:#BDB8AE;font-variant-numeric:tabular-nums;min-width:7ch;text-align:right}
.vctrl button{width:48px;height:48px;border-radius:999px;border:1px solid #4A4A4A;background:transparent;color:#FFFFFF;display:grid;place-items:center;cursor:pointer;transition:background .3s,border-color .3s,color .3s}
.vctrl button:hover:not(:disabled){background:#F9BF58;border-color:#F9BF58;color:#0D0D0D}
.vctrl button:disabled{opacity:.35;cursor:default}
.vtrack{list-style:none;margin:0;display:flex;gap:20px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-behavior:smooth;overscroll-behavior-x:contain;scrollbar-width:none;
  --edge:max(24px,calc((100% - 1200px) / 2 + 24px));padding:0 var(--edge);scroll-padding-inline:var(--edge)}
.vtrack::-webkit-scrollbar{display:none}
.vid{flex:0 0 clamp(230px,24vw,300px);scroll-snap-align:start;display:flex;flex-direction:column;gap:14px}
.vid__media{position:relative;aspect-ratio:9/16;border-radius:20px;overflow:hidden;background:#1D1D1B;border:1px dashed #4A4A4A}
.vid__media video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;background:#000}
.vid__play{position:absolute;inset:0;width:100%;border:0;padding:0;background:linear-gradient(180deg,transparent 55%,rgba(5,5,5,.75));cursor:pointer;display:grid;place-items:center;color:#0D0D0D}
.vid__play span{width:64px;height:64px;border-radius:999px;background:#F9BF58;display:grid;place-items:center;transition:transform .4s ease}
.vid__play:hover span{transform:scale(1.08)}
.vid__no{position:absolute;top:14px;left:14px;font-size:12px;letter-spacing:.12em;color:#BDB8AE;pointer-events:none}
.vid__cap{display:flex;justify-content:space-between;gap:12px;font-size:15px;color:#E8E4DC}
.vid__cap b{font-family:'Bounded',sans-serif;font-weight:700;color:#FFFFFF}
.vbar{max-width:1200px;width:calc(100% - 48px);margin:0 auto;height:2px;background:#2A2A2A;position:relative}
.vbar i{position:absolute;left:0;top:0;bottom:0;background:#F9BF58;width:0;transition:width .3s ease}
/* 2 · before / after */
.bagrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,260px),1fr));gap:20px}
.ba2{margin:0;display:flex;flex-direction:column;gap:10px}
.ba2__img{aspect-ratio:4/5;border-radius:18px;background:#141414;overflow:hidden;position:relative;display:grid;place-items:center}
.ba2__img img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.ba2__ph{position:absolute;inset:12px;border:1px dashed #4A4A4A;border-radius:12px;display:flex;align-items:flex-start;justify-content:space-between;padding:12px;font-size:12px;letter-spacing:.12em;color:#8C877E}
.ba2__ph span:last-child{color:#F9BF58}
.ba2 figcaption{font-size:12px;letter-spacing:.12em;color:#8C877E}
.js-on .ba2--more{display:none}
.js-on.ba-open .ba2--more{display:flex}
.more{align-self:center;display:none;align-items:center;gap:10px;background:#0D0D0D;color:#FFFFFF;border:2px solid #F9BF58;border-radius:999px;padding:16px 26px;min-height:48px;font:800 14px/1 'Manrope',sans-serif;letter-spacing:.06em;cursor:pointer}
.js-on .more{display:inline-flex}.js-on.ba-open .more{display:none}
.more:hover{background:#F9BF58;color:#0D0D0D}
/* 3 · written */
.quotes{columns:3 300px;column-gap:24px}
.quotes .quote{break-inside:avoid;margin:0 0 24px!important;flex:none}
.quote .who{font-family:'Bounded',sans-serif;font-weight:700;font-size:17px;color:#0D0D0D}
:where(.vctrl button,.vid__play,.more,.jump):focus-visible{outline:2px solid #F9BF58;outline-offset:3px}
@media (max-width:640px){.vwrap{padding:0 12px}.vsec{border-radius:24px}.vctrl button{width:44px;height:44px}}
@media (prefers-reduced-motion:reduce){.vtrack{scroll-behavior:auto}.quote,.vid__play span{transition:none}}
"""

PLAY = '<svg width="22" height="22" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5.5v13l11-6.5z" fill="currentColor"/></svg>'
TICK = '<svg width="24" height="24" viewBox="0 0 24 24" aria-hidden="true"><path d="m4 12.5 5 5L20 6.5" fill="none" stroke="#F9BF58" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ARROW_L = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 5l-7 7 7 7"/></svg>'
ARROW_R = ARROW_L.replace('M15 5l-7 7 7 7', 'M9 5l7 7-7 7')

def video(n):
    # data-src: the video file (mp4); data-poster: a still. Empty = placeholder.
    return f'''        <li class="vid" aria-label="Video {n} di {VIDEOS}">
          <div class="vid__media">
            <span class="vid__no">VIDEO {n:02d}</span>
            <button class="vid__play" type="button" data-src="" data-poster="" aria-label="Guarda il video {n:02d}"><span>{PLAY}</span></button>
          </div>
          <div class="vid__cap"><b>[Nome]</b><span>[durata]</span></div>
        </li>'''

def photo(n):
    more = ' ba2--more' if n > PHOTOS_FIRST else ''
    return f'''        <figure class="ba2{more}" aria-label="Foto prima e dopo {n:02d} (in arrivo)">
          <div class="ba2__img"><div class="ba2__ph"><span>PRIMA</span><span>DOPO</span></div></div>
          <figcaption>[FOTO {n:02d} · PRIMA / DOPO]</figcaption>
        </figure>'''

def quote(n):
    text, name, ink = (MARCO, 'Marco', '#2A2A2A') if n == 1 else (f'[Testimonianza scritta {n:02d} · copy da WeTransfer]', '[Nome]', '#8C877E')
    return f'''      <figure class="quote">
        <div style="font-family: 'Bounded', sans-serif; font-weight: 800; font-size: 44px; line-height: .6; color: #F9BF58;" aria-hidden="true">“</div>
        <blockquote style="margin: 0; flex: 1; font-size: 17px; line-height: 1.6; color: {ink};">{text}</blockquote>
        <figcaption style="display: flex; align-items: center; justify-content: space-between; gap: 12px; padding-top: 16px; border-top: 1px solid #E6E1D7;">
          <span class="who">{name}</span>
          {TICK}
        </figcaption>
      </figure>'''

nl = '\n'
MIDDLE = f'''  <!-- ============ INTRO ============ -->
  <section style="background: #F5F3EE;">
    <div style="max-width: 1200px; margin: 0 auto; padding: 80px 24px 56px; display: flex; flex-wrap: wrap; gap: 32px 56px; align-items: flex-end;">
      <div style="flex: 999 1 560px; min-width: 0; display: flex; flex-direction: column; gap: 22px;">
        <div class="eyebrow">STORIE REALI</div>
        <h2 class="h2">Meno grasso. Più atletici. Più forti nel lavoro e nella vita.</h2>
        <div class="rule"></div>
        <p style="margin: 0; font-size: clamp(18px, 1.6vw, 21px); line-height: 1.55; color: #2A2A2A; max-width: 680px;">Qui trovi le storie reali di chi ha scelto OLTRESOGLIA: ex sportivi con l’agenda piena, che hanno perso grasso e sono tornati atletici, senza fermare il lavoro né la vita.</p>
      </div>
      <nav aria-label="In questa pagina" style="flex: 1 1 280px; min-width: 0; background: #141414; border-radius: 20px; padding: 20px 32px; display: flex; flex-direction: column; color: #FFFFFF;">
        <a class="jump" href="#video"><b>{VIDEOS}</b>Video testimonianze</a>
        <a class="jump" href="#prima-dopo"><b>{PHOTOS}</b>Foto prima e dopo</a>
        <a class="jump" href="#messaggi"><b>{QUOTES}</b>Testimonianze scritte</a>
      </nav>
    </div>
  </section>

  <!-- ============ 1 · VIDEO TESTIMONIANZE (carosello orizzontale) ============ -->
  <div class="vwrap" id="video">
    <section class="vsec" aria-labelledby="video-title">
      <div class="vhead">
        <div class="sec-head">
          <div class="eyebrow">VIDEO TESTIMONIANZE</div>
          <h2 class="h2" id="video-title">Raccontato da loro.</h2>
          <div class="rule"></div>
        </div>
        <div class="vctrl">
          <span class="vcount" aria-live="polite"><span data-vnow>01</span> / {VIDEOS}</span>
          <button type="button" data-vprev aria-label="Video precedente">{ARROW_L}</button>
          <button type="button" data-vnext aria-label="Video successivo">{ARROW_R}</button>
        </div>
      </div>
      <ul class="vtrack" aria-label="Video testimonianze" tabindex="0">
{nl.join(video(i) for i in range(1, VIDEOS + 1))}
      </ul>
      <div class="vbar" aria-hidden="true"><i data-vbar></i></div>
    </section>
  </div>

  <!-- ============ 2 · PRIMA E DOPO ============ -->
  <section id="prima-dopo" style="background: #F5F3EE;">
    <div style="max-width: 1200px; margin: 0 auto; padding: 96px 24px; display: flex; flex-direction: column; gap: 40px;">
      <div class="sec-head">
        <div class="eyebrow">PRIMA E DOPO</div>
        <h2 class="h2">I cambiamenti, fotografati.</h2>
        <div class="rule"></div>
        <p class="sec-text">Le foto vengono pubblicate solo con il consenso del cliente.</p>
      </div>
      <div class="bagrid">
{nl.join(photo(i) for i in range(1, PHOTOS + 1))}
      </div>
      <button class="more" type="button" data-bamore>MOSTRA TUTTE LE FOTO ({PHOTOS})</button>
    </div>
  </section>

  <!-- ============ 3 · TESTIMONIANZE SCRITTE ============ -->
  <section id="messaggi" style="background: #FFFFFF; border-top: 1px solid #E6E1D7; border-bottom: 1px solid #E6E1D7;">
    <div style="max-width: 1200px; margin: 0 auto; padding: 96px 24px; display: flex; flex-direction: column; gap: 40px;">
      <div class="sec-head">
        <div class="eyebrow">TESTIMONIANZE SCRITTE</div>
        <h2 class="h2">Con le loro parole.</h2>
        <div class="rule"></div>
        <p class="sec-text">I messaggi arrivano così come i clienti li hanno scritti, senza ritocchi.</p>
      </div>
      <div class="quotes">
{nl.join(quote(i) for i in range(1, QUOTES + 1))}
      </div>
    </div>
  </section>

'''

SCRIPT = """<script>
(() => {
  const root = document.querySelector('.vwrap').parentElement
  root.classList.add('js-on')
  // Before / after: first 12 visible, the rest on request
  document.querySelector('[data-bamore]').addEventListener('click', () => root.classList.add('ba-open'))

  // Video carousel: arrows, counter, progress bar
  const track = document.querySelector('.vtrack')
  const items = [...track.children]
  const prev = document.querySelector('[data-vprev]'), next = document.querySelector('[data-vnext]')
  const now = document.querySelector('[data-vnow]'), bar = document.querySelector('[data-vbar]')
  const step = () => items[1].offsetLeft - items[0].offsetLeft
  const update = () => {
    const max = track.scrollWidth - track.clientWidth
    const i = Math.min(items.length - 1, Math.round(track.scrollLeft / step()))
    now.textContent = String(i + 1).padStart(2, '0')
    bar.style.width = (max > 0 ? Math.max(track.clientWidth / track.scrollWidth, track.scrollLeft / max) * 100 : 100) + '%'
    prev.disabled = track.scrollLeft <= 2
    next.disabled = track.scrollLeft >= max - 2
  }
  prev.addEventListener('click', () => track.scrollBy({ left: -step() }))
  next.addEventListener('click', () => track.scrollBy({ left: step() }))
  track.addEventListener('scroll', update, { passive: true })
  addEventListener('resize', update)
  update()

  // Play: swap the card for the video; only one plays at a time
  track.addEventListener('click', (e) => {
    const btn = e.target.closest('.vid__play')
    if (!btn || !btn.dataset.src) return
    const v = document.createElement('video')
    Object.assign(v, { src: btn.dataset.src, controls: true, autoplay: true, playsInline: true })
    if (btn.dataset.poster) v.poster = btn.dataset.poster
    v.addEventListener('play', () => track.querySelectorAll('video').forEach((o) => o !== v && o.pause()))
    btn.replaceWith(v)
  })
})()
</script>
"""

out = src[:src.index(start)] + MIDDLE + src[src.index(end):]
out = out.replace('@media (max-width:640px){.quote,.ba{flex-basis:100%}}\n', '@media (max-width:640px){.quote,.ba{flex-basis:100%}}\n' + CSS.lstrip('\n'), 1)
closing = '\n</div>\n</body>\n</html>'
assert out.count(closing) == 1
out = out.replace(closing, '\n</div>\n' + SCRIPT + '</body>\n</html>')
open(REPO, 'w').write(out)

# Artifact source: same page, fonts from the artifact's own asset files
art, n = re.subn(r'url\("data:font/ttf;base64,[A-Za-z0-9+/=]+"\)', lambda m, it=iter(ASSETS): f'url("./assets/{next(it)}.ttf")', out)
assert n == 6
open(f'{S}/tst/testimonianze-artifact.html', 'w').write(art)
print('ok', len(out), len(art), out.count('class="vid"'), out.count('class="ba2'), out.count('class="quote"'))
