"""Come funziona v2: one dark block. Left: title + three steps on a vertical yellow line, stepping right.
Right: Pietro with the tablet (cut-out) rising out of a Saffron glow. Bottom: the guarantee as a band with a giant outline 100%."""
p = '/home/user/Skylarnina/oltresoglia/home/index.html'
t = open(p).read()

s = t.index('  /* 13 · COME FUNZIONA */'); e = t.index('  /* 14 · EBOOK')
css = '''  /* 13 · COME FUNZIONA (dark block: steps on a line + Pietro cut-out; guarantee band) */
  .how { position: relative; overflow: hidden; padding-bottom: 0; }
  .how__top { display: grid; grid-template-columns: minmax(0, 1.15fr) minmax(0, .85fr); gap: 40px; }
  .how__steps { position: relative; display: grid; gap: clamp(28px, 3vw, 40px); padding-bottom: clamp(40px, 5vw, 64px); }
  .how__steps::before { content: ''; position: absolute; left: 27px; top: 28px; bottom: 96px; width: 2px;
    background: linear-gradient(var(--yellow), color-mix(in srgb, var(--yellow) 20%, transparent)); }
  .hstep { position: relative; display: grid; grid-template-columns: 56px minmax(0, 1fr); gap: 24px; align-items: start; }
  .hstep:nth-child(2) { margin-left: clamp(0px, 3vw, 40px); }
  .hstep:nth-child(3) { margin-left: clamp(0px, 6vw, 80px); }
  .hstep:nth-child(2)::before, .hstep:nth-child(3)::before { content: ''; position: absolute; right: 100%; top: 27px; width: clamp(0px, 3vw, 40px); height: 2px; background: color-mix(in srgb, var(--yellow) 45%, transparent); }
  .hstep__n { width: 56px; height: 56px; border-radius: 999px; background: var(--dark); border: 2px solid var(--yellow); color: var(--yellow);
    display: grid; place-items: center; font: 800 18px/1 var(--display); position: relative; z-index: 1; transition: background .4s, color .4s; }
  .hstep:hover .hstep__n { background: var(--yellow); color: var(--dark); }
  .hstep__txt { display: grid; gap: 8px; padding: 6px 0 0; max-width: 46ch; }
  .hstep__txt .h3 { color: #fff; }
  .how__vis { position: relative; align-self: end; height: 100%; min-height: 520px; }
  .how__vis::before { content: ''; position: absolute; left: 50%; bottom: -10%; width: 120%; aspect-ratio: 1; transform: translateX(-50%);
    background: radial-gradient(closest-side, color-mix(in srgb, var(--yellow) 38%, transparent), transparent 70%); }
  .how__vis img { position: absolute; left: 50%; bottom: 0; height: 100%; max-height: 640px; width: auto; transform: translateX(-50%); filter: drop-shadow(0 30px 40px rgba(0,0,0,.5)); }
  .guar { position: relative; z-index: 1; display: grid; grid-template-columns: auto minmax(0, 1fr) auto; gap: clamp(24px, 3vw, 48px); align-items: center;
    margin-inline: calc(-1 * var(--pad)); padding: clamp(28px, 3vw, 40px) var(--pad); background: var(--dark-2); border-top: 1px solid var(--hair-d); }
  .guar__big { display: grid; justify-items: start; gap: 6px; }
  .guar__big b { font: 900 clamp(64px, 7vw, 104px)/.85 var(--display); letter-spacing: -.03em; color: transparent; -webkit-text-stroke: 1.5px var(--yellow); }
  .guar__big span { font: 700 12px/1 var(--text); letter-spacing: .3em; color: var(--yellow); padding-left: 4px; }
  .guar__txt { display: grid; gap: 10px; max-width: 62ch; }
  .guar__txt .h3 { color: #fff; font-size: clamp(19px, 1.7vw, 24px); }
  .guar__txt .body { color: var(--on-dark-2); }

'''
t = t[:s] + css + t[e:]

# responsive rules of the old layout -> new ones
for a, b in [
    ("    .guar { grid-template-columns: 200px minmax(0, 1fr); } .seal { display: none; } .guar__cta { grid-column: 2; }\n",
     "    .guar { grid-template-columns: auto minmax(0, 1fr); } .guar > .btn { grid-column: 2; justify-self: start; }\n"),
    ("    .grid3, .steps { grid-template-columns: 1fr; } .svc--y { grid-column: auto; }\n", "    .grid3 { grid-template-columns: 1fr; } .svc--y { grid-column: auto; }\n"),
    ("    .step:not(:last-child)::after { display: none; }\n", "    .how__top { grid-template-columns: 1fr; } .how__vis { min-height: 380px; order: -1; } .how__vis img { max-height: 380px; }\n    .hstep:nth-child(n) { margin-left: 0; } .hstep::before { display: none; }\n"),
]:
    assert t.count(a) == 1, a[:60]; t = t.replace(a, b)
old = [l for l in t.splitlines() if l.startswith('    .guar { grid-template-columns: 1fr; padding: 12px 12px 24px; }')]
assert len(old) == 1
t = t.replace(old[0], '    .guar { grid-template-columns: 1fr; } .guar > .btn { grid-column: auto; }')

s = t.index('  <!-- 13 · COME FUNZIONA -->'); e = t.index('  <!-- 14 · EBOOK -->')
html = '''  <!-- 13 · COME FUNZIONA -->
  <section class="box box--d on-dark how" aria-labelledby="come-t">
    <div class="how__top">
      <div>
        <div class="head"><h2 class="h2" id="come-t">Come funziona</h2><div class="rule"></div></div>
        <ol class="how__steps">
          <li class="hstep"><span class="hstep__n">1</span><div class="hstep__txt"><h3 class="h3">Scrivimi su WhatsApp.</h3><p class="body">Ti rispondiamo noi e capiamo insieme da dove parti.</p></div></li>
          <li class="hstep"><span class="hstep__n">2</span><div class="hstep__txt"><h3 class="h3">Fissiamo una video consulenza gratuita</h3><p class="body">In 35 minuti analizziamo la tua settimana, i tuoi obiettivi e ti spieghiamo come costruiremmo il percorso intorno alla tua vita.</p></div></li>
          <li class="hstep"><span class="hstep__n">3</span><div class="hstep__txt"><h3 class="h3">Decidi se partire.</h3><p class="body">Se il metodo fa per te, si parte. Se non partiamo, esci comunque con una strategia da usare.</p></div></li>
        </ol>
      </div>
      <div class="how__vis" aria-hidden="true"><img src="assets/pietro-consulenza-cutout.png" alt="" /></div>
    </div>
    <div class="guar">
      <div class="guar__big"><b>100%</b><span>RIMBORSO</span></div>
      <div class="guar__txt"><h3 class="h3">L’unico rischio è continuare a rimandare.</h3><p class="body">Se entri nel programma, esegui con precisione il metodo concordato e non ottieni i risultati definiti insieme, hai diritto a un rimborso del 100%. Non è uno slogan di marketing. È una clausola del nostro contratto.</p></div>
      <a class="btn btn--y" href="#">Scrivimi su WhatsApp ora</a>
    </div>
  </section>

'''
t = t[:s] + html + t[e:]
open(p, 'w').write(t)
print('ok')
