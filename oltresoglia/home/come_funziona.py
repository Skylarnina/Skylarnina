"""Come funziona v3 (editorial): photo card of Pietro left, three big numbered rows right,
guarantee as a full yellow card with a giant solid 100%."""
p = '/home/user/Skylarnina/oltresoglia/home/index.html'
t = open(p).read()

s = t.index('  /* 13 · COME FUNZIONA'); e = t.index('  /* 14 · EBOOK')
css = '''  /* 13 · COME FUNZIONA (editorial rows + Pietro card; guarantee as a yellow card) */
  .how { display: grid; gap: var(--gap); }
  .how__main { display: grid; grid-template-columns: minmax(0, 5fr) minmax(0, 7fr); gap: clamp(24px, 4vw, 64px); align-items: stretch; }
  .how__card { position: relative; border-radius: var(--r-box); overflow: hidden; min-height: 560px; color: #fff; display: flex; flex-direction: column; justify-content: space-between; padding: clamp(24px, 2.8vw, 36px); isolation: isolate; }
  .how__card img { position: absolute; inset: 0; z-index: -2; width: 100%; height: 100%; object-fit: cover; object-position: 50% 22%; }
  .how__card::after { content: ''; position: absolute; inset: 0; z-index: -1; background: linear-gradient(180deg, rgba(10,10,10,.82) 0%, rgba(10,10,10,.1) 38%, rgba(10,10,10,.1) 60%, rgba(10,10,10,.85) 100%); }
  .how__card .h2 { color: #fff; }
  .how__sign { display: flex; align-items: center; gap: 14px; }
  .how__sign span { width: 44px; height: 44px; border-radius: 999px; background: var(--yellow); display: grid; place-items: center; color: var(--dark); flex: none; }
  .how__sign span svg { width: 20px; }
  .how__sign b { display: block; font: 700 16px/1.25 var(--display); }
  .how__sign small { font: 500 13px/1.3 var(--text); color: #E8E4DC; }
  .how__rows { display: grid; align-content: center; }
  .hrow { display: grid; grid-template-columns: clamp(76px, 8vw, 112px) minmax(0, 1fr); gap: clamp(16px, 2vw, 28px); padding: clamp(24px, 2.6vw, 34px) 0; border-top: 1px solid #DDD7CB; }
  .hrow:last-child { border-bottom: 1px solid #DDD7CB; }
  .hrow__n { font: 900 clamp(56px, 6vw, 84px)/.85 var(--display); letter-spacing: -.03em; color: transparent; -webkit-text-stroke: 1.5px var(--ink); transition: color .5s var(--ease), -webkit-text-stroke-color .5s; }
  .hrow:hover .hrow__n { color: var(--yellow); -webkit-text-stroke-color: var(--yellow); }
  .hrow__txt { display: grid; gap: 10px; align-content: start; padding-top: 4px; }
  .hrow__txt .h3 { font-size: clamp(20px, 1.8vw, 26px); }
  .hrow__txt .body { font-size: 16.5px; max-width: 52ch; }
  .guar { display: grid; grid-template-columns: auto minmax(0, 1fr) auto; gap: clamp(24px, 3.4vw, 56px); align-items: center; background: var(--yellow); color: var(--ink);
    border-radius: var(--r-box); padding: clamp(28px, 3.4vw, 48px) clamp(24px, 4vw, 56px); position: relative; overflow: hidden; }
  .guar::after { content: ''; position: absolute; right: -80px; top: -80px; width: 260px; height: 260px; border-radius: 999px; border: 1.5px solid rgba(13,13,13,.14); box-shadow: 0 0 0 40px rgba(255,255,255,.08); pointer-events: none; }
  .guar__big { display: grid; gap: 8px; }
  .guar__big b { font: 900 clamp(72px, 8vw, 120px)/.82 var(--display); letter-spacing: -.04em; }
  .guar__big span { font: 700 12px/1 var(--text); letter-spacing: .32em; padding-left: 4px; }
  .guar__txt { display: grid; gap: 10px; max-width: 60ch; padding-left: clamp(0px, 3vw, 48px); border-left: 1.5px solid rgba(13,13,13,.18); }
  .guar__txt .h3 { font-size: clamp(20px, 1.9vw, 28px); }
  .guar__txt .body { color: rgba(13,13,13,.78); }
  .guar .btn { position: relative; z-index: 1; }

'''
t = t[:s] + css + t[e:]

# responsive rules from v2 -> v3
for a, b in [
    ("    .guar { grid-template-columns: auto minmax(0, 1fr); } .guar > .btn { grid-column: 2; justify-self: start; }\n",
     "    .guar { grid-template-columns: auto minmax(0, 1fr); } .guar > .btn { grid-column: 2; justify-self: start; }\n    .how__main { grid-template-columns: 1fr; } .how__card { min-height: 420px; }\n"),
    ("    .how__top { grid-template-columns: 1fr; } .how__vis { min-height: 380px; order: -1; } .how__vis img { max-height: 380px; }\n", ""),
    ("    .guar { grid-template-columns: 1fr; } .guar > .btn { grid-column: auto; }",
     "    .guar { grid-template-columns: 1fr; } .guar > .btn { grid-column: auto; } .guar__txt { padding-left: 0; border-left: 0; }"),
]:
    assert t.count(a) == 1, a[:70]; t = t.replace(a, b)

s = t.index('  <!-- 13 · COME FUNZIONA -->'); e = t.index('  <!-- 14 · EBOOK -->')
html = '''  <!-- 13 · COME FUNZIONA -->
  <section class="box box--open how" aria-labelledby="come-t">
    <div class="how__main">
      <div class="how__card">
        <img src="../chi-siamo/assets/team/pietro-hero.jpg" alt="Pietro Vecchi" />
        <div class="head" style="margin:0"><h2 class="h2" id="come-t">Come funziona</h2><div class="rule"></div></div>
        <div class="how__sign"><span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 11.5a8.4 8.4 0 0 1-12.4 7.4L3 21l2.1-5.4A8.4 8.4 0 1 1 21 11.5z"/></svg></span><div><b>Dott. Pietro Vecchi</b><small>Biologo Nutrizionista</small></div></div>
      </div>
      <ol class="how__rows">
        <li class="hrow"><span class="hrow__n">01</span><div class="hrow__txt"><h3 class="h3">Scrivimi su WhatsApp.</h3><p class="body">Ti rispondiamo noi e capiamo insieme da dove parti.</p></div></li>
        <li class="hrow"><span class="hrow__n">02</span><div class="hrow__txt"><h3 class="h3">Fissiamo una video consulenza gratuita</h3><p class="body">In 35 minuti analizziamo la tua settimana, i tuoi obiettivi e ti spieghiamo come costruiremmo il percorso intorno alla tua vita.</p></div></li>
        <li class="hrow"><span class="hrow__n">03</span><div class="hrow__txt"><h3 class="h3">Decidi se partire.</h3><p class="body">Se il metodo fa per te, si parte. Se non partiamo, esci comunque con una strategia da usare.</p></div></li>
      </ol>
    </div>
    <div class="guar">
      <div class="guar__big"><b>100%</b><span>RIMBORSO</span></div>
      <div class="guar__txt"><h3 class="h3">L’unico rischio è continuare a rimandare.</h3><p class="body">Se entri nel programma, esegui con precisione il metodo concordato e non ottieni i risultati definiti insieme, hai diritto a un rimborso del 100%. Non è uno slogan di marketing. È una clausola del nostro contratto.</p></div>
      <a class="btn btn--d" href="#">Scrivimi su WhatsApp ora</a>
    </div>
  </section>

'''
t = t[:s] + html + t[e:]
open(p, 'w').write(t)
print('ok')
