"""Put the Homepage.pdf copy (3 Nov) into oltresoglia/home/index.html, verbatim."""
import re
p = '/home/user/Skylarnina/oltresoglia/home/index.html'
t = open(p).read()
X = '<span class="ic ic--x"><svg viewBox="0 0 12 12" aria-hidden="true"><path d="M3 3l6 6M9 3l-6 6" stroke="currentColor" stroke-width="1.8"/></svg></span>'
OK = '<span class="ic ic--ok"><svg viewBox="0 0 12 12" aria-hidden="true"><path d="M2.5 6.2l2.3 2.3 4.7-5" fill="none" stroke="currentColor" stroke-width="1.8"/></svg></span>'
GO = '<span class="vc__go"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M7 17L17 7M9 7h8v8"/></svg></span>'


def r(a, b, n=1):
    global t
    assert t.count(a) == n, (t.count(a), a[:90])
    t = t.replace(a, b)


# hero chip + numbers
r('<div><b>+500</b><span class="small tbd">professionisti seguiti</span></div>', '<div><b>+500</b><span class="small">professionisti seguiti</span></div>')
r('<span class="small"><span class="tbd">professionisti seguiti</span></span>', '<span class="small">professionisti seguiti</span>')
r('<span class="small"><span class="tbd">di esperienza sul campo</span></span>', '<span class="small">di esperienza sul campo</span>')
r('<span class="small"><span class="tbd">[testo dal Figma]</span></span>', '<span class="small">rimborso garantito sul metodo concordato</span>')

# results
r('<div><b>92 <i>→</i> 80 kg</b><span class="small">Marco, <span class="tbd">[ruolo · ex sport]</span></span></div><span class="pill tbd" style="color:var(--dark)">[in X mesi]</span>',
  '<div><b>92 <i>→</i> 80 kg</b><span class="small">Marco, manager di una multinazionale ed ex nuotatore</span></div><span class="pill">in 8 mesi</span>')
r('<div><b>72 <i>→</i> 67 kg</b><span class="small">Clara, <span class="tbd">[ruolo]</span></span></div><span class="pill">[mesi]</span>',
  '<div><b>72 <i>→</i> 61 kg</b><span class="small">Clara, infermiera su tre turni ed ex pallavolista</span></div><span class="pill">in 8 mesi</span>')
r('<div><b>86 <i>→</i> 69 kg</b><span class="small">Gianluca, <span class="tbd">[ruolo]</span></span></div><span class="pill">[mesi]</span>',
  '<div><b>86 <i>→</i> 69 kg</b><span class="small">Gianluca, consulente finanziario in trasferta ed ex rugbista</span></div><span class="pill">in un anno</span>')

# videos: 3 cards as in the PDF + "Scorri →"
s = t.index('    <div class="vrow">'); e = t.index('  <!-- 5 · TI SUONA FAMILIARE -->')
cards = ''.join(f'''      <article class="vc"><div class="vc__media"><p class="vc__title">[Titolo in sovraimpressione]</p><span class="play"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 3.5v17l15-8.5z" fill="currentColor"/></svg></span><span class="small" style="position:absolute;left:14px;bottom:12px;z-index:1;color:#8C877E">[VIDEO {n}]</span></div><div class="vc__who"><div><b>[Nome]</b><span class="small">[Una riga sul risultato]</span></div>{GO}</div></article>
''' for n in (1, 2, 3))
t = t[:s] + '    <div class="vrow">\n' + cards + '    </div>\n  </section>\n\n' + t[e:]
r('''    <div class="split">
      <div><p class="eyebrow">Video testimonianze</p></div>
    </div>''', '''    <div class="split" style="align-items:center">
      <div><p class="eyebrow">Video testimonianze</p></div>
      <p class="small" style="justify-self:end;font-weight:700;color:var(--ink)">Scorri →</p>
    </div>''')
r('.vrow { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr));', '.vrow { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); max-width: 1000px; margin-inline: auto;')
r('.vrow .vc:nth-child(2) { margin-top: 64px; } .vrow .vc:nth-child(3) { margin-top: 24px; } .vrow .vc:nth-child(4) { margin-top: 88px; }', '.vrow .vc:nth-child(2) { margin-top: 72px; } .vrow .vc:nth-child(3) { margin-top: 28px; }')
r('    .vrow { grid-template-columns: repeat(2, minmax(0, 1fr)); } .vrow .vc { margin-top: 0 !important; } .vrow .vc:nth-child(even) { margin-top: 48px !important; }\n', '')
r('    .vrow { grid-template-columns: 1fr 1fr; gap: 12px; }\n', '    .vrow { display: flex; overflow-x: auto; scroll-snap-type: x mandatory; gap: 12px; } .vrow .vc { flex: 0 0 72%; scroll-snap-align: start; margin-top: 0 !important; }\n')

# Ti suona familiare
fam = [("Cinque allenamenti a settimana, dieta drastica, sveglia all’alba. Poi arriva una settimana pesante, salta tutto e ricominci da capo.", "Ogni volta con le stesse promesse.<br />Ogni volta con lo stesso risultato."),
       ("Diete drastiche, solo cardio, schede da culturista, app da 9,99 € e corsi di gruppo. Persino coach e nutrizionisti che ti seguivano separatamente, senza mai confrontarsi.", "Hai investito tempo e denaro. Ma il fisico che volevi è ancora lontano."),
       ("Hai dato tutto al lavoro. Torni a casa stanco, senza energie per allenarti, goderti la famiglia o dedicarti alle tue passioni.", "E domani ricomincia tutto da capo.")]
for a, b in fam:
    old = '<p class="body tbd">[testo dal Figma]</p></div></li>'
    assert old in t
    t = t.replace(old, f'<p class="body">{a}</p><p class="body" style="margin-top:8px;font-weight:600;color:var(--ink)">{b}</p></div></li>', 1)

# band: no extra CTA (not in the copy)
r('''      <p class="statement">Il fisico che avevi non l'hai perso in un giorno. <span class="y">L'hai messo da parte, una settimana alla volta.</span></p>
      <a class="btn btn--y" href="#">Ricevi gratis la strategia da cui ripartire →</a>''', '''      <p class="statement">Il fisico che avevi non l’hai perso in un giorno. <span class="y">L’hai messo da parte, una settimana alla volta.</span></p>''')

# piano
for it in ["C’è chi finisce quando lo decide il lavoro, mai alle sei.", "C’è chi passa più sere in albergo che nel proprio letto.", "C’è chi fa le notti e scopre la turnistica il venerdì.", "E c’è chi ha orari regolari, ma ogni ora dell’agenda è già di qualcun altro."]:
    old = '</span><p class="body tbd">[testo dal Figma]</p></article>'
    assert old in t
    t = t.replace(old, f'</span><p class="lead" style="color:var(--ink)">{it}</p></article>', 1)
r('<article class="svc svc--y"><p class="lead"><span class="tbd" style="color:var(--ink)">[Ogni settimana ha una forma… testo dal Figma]</span></p>',
  '<article class="svc svc--y"><div><p class="h3">Ogni settimana ha una forma.</p><p class="lead" style="margin-top:6px">Con il nostro test capisci dove si rompe la tua e da dove ripartire.</p></div>')

# percorso button (no arrow in the copy)
r('<a class="btn btn--o" href="#">Scrivici su WhatsApp e scopri da dove ripartire →</a>', '<a class="btn btn--o" href="#">Scrivici su WhatsApp e scopri da dove ripartire</a>')

# comparison
std = [("Sei tu a doverti adattare al programma.", "Schede e diete che non tengono conto dei tuoi orari, delle trasferte e degli imprevisti."),
       ("Solo pesi o solo cardio.", "Ti rendono più leggero o più grosso, non di nuovo atletico."),
       ("Alla prima settimana storta, perdi il ritmo.", "Salti gli allenamenti, perdi continuità e ti ritrovi a ricominciare da capo."),
       ("Se hai bisogno, devi farti sentire tu.", "Il supporto arriva quando lo chiedi. Nel frattempo, la settimana storta passa e nessuno se ne accorge.")]
us = [("È il programma che si adatta alla tua vita.", "Partiamo dalla tua settimana più difficile, non da quella ideale."),
      ("Forza e fiato insieme.", "Come ti allenavi quando facevi sport, dentro la settimana che hai oggi."),
      ("Il percorso continua anche quando il tempo manca.", "Per le settimane più complicate hai sempre pronta una versione ridotta del programma, e non riparti mai da zero."),
      ("Siamo noi a cercarti, ogni settimana.", "Monitoriamo i tuoi progressi e interveniamo senza aspettare che sia tu a chiedere aiuto.")]
for b, rest in std:
    old = f'<li>{X}<span class="tbd">[testo dal Figma]</span></li>'
    assert old in t
    t = t.replace(old, f'<li>{X}<span><b>{b}</b> {rest}</span></li>', 1)
for b, rest in us:
    old = f'<li>{OK}<span class="tbd">[testo dal Figma]</span></li>'
    assert old in t
    t = t.replace(old, f'<li>{OK}<span><b style="color:#fff">{b}</b> {rest}</span></li>', 1)
r('<div class="plan__h"><b>OLTRESOGLIA</b><span class="tag">Il metodo</span></div>', '<div class="plan__h"><b>OLTRESOGLIA</b></div>')
r('''        </ul>
        <a class="btn btn--y" href="#">Ricevi gratis la strategia da cui ripartire →</a>
      </div>''', '''        </ul>
      </div>''')
r('max-width: 1040px; margin-inline: auto; align-items: center; }', 'max-width: 1100px; margin-inline: auto; align-items: center; }')

# team: arrow instead of the "Scopri" pill (not in the copy)
r('<span class="pill">Scopri</span>', GO, 6)

# per te: the PDF has the "È per te se:" heading with no list under it
s = t.index('      <div class="fcard fcard--yes">'); e = t.index('      <div class="fcard fcard--no">')
t = t[:s] + '''      <div class="fcard fcard--yes">
        <h3 class="h3">È per te se:</h3>
      </div>
''' + t[e:]
r('<span><b>Cerchi scorciatoie.</b> <span class="tbd">[testo dal Figma]</span></span>', '<span><b>Cerchi scorciatoie.</b> Vuoi risultati immediati senza cambiare le tue abitudini.</span>')
r('<span><b>Aspetti il momento perfetto.</b> <span class="tbd">[testo dal Figma]</span></span>', '<span><b>Aspetti il momento perfetto.</b> Continui a rimandare perché il lavoro viene sempre prima.</span>')
r('<span><b>Vuoi sentirti dire quello che ti fa comodo.</b> <span class="tbd">[testo dal Figma]</span></span>', '<span><b>Vuoi sentirti dire quello che ti fa comodo.</b> Non sei disposto a metterti in discussione.</span>')
r('<p>Se ti riconosci, è il momento di partire.</p>', '<p>Se ti riconosci, è il momento di parlarne.</p>')

# come funziona
r('<h3 class="h3">Scrivimi su WhatsApp.</h3><p class="body tbd">[testo dal Figma]</p>', '<h3 class="h3">Scrivimi su WhatsApp.</h3><p class="body">Ti rispondiamo noi e capiamo insieme da dove parti.</p>')
r('<h3 class="h3">Prenota una video consulenza gratuita.</h3><p class="body tbd">[testo dal Figma]</p>', '<h3 class="h3">Fissiamo una video consulenza gratuita</h3><p class="body">In 35 minuti analizziamo la tua settimana, i tuoi obiettivi e ti spieghiamo come costruiremmo il percorso intorno alla tua vita.</p>')
r('<h3 class="h3">Decidi se partire.</h3><p class="body tbd">[testo dal Figma]</p>', '<h3 class="h3">Decidi se partire.</h3><p class="body">Se il metodo fa per te, si parte. Se non partiamo, esci comunque con una strategia da usare.</p>')
r('''<h3 class="h3">L'unico rischio è continuare a rimandare.</h3><p class="body tbd">[testo dal Figma]</p><a class="btn btn--o" href="#" style="justify-self:start;margin-top:8px">Scrivici su WhatsApp ora</a>''',
  '''<h3 class="h3">L’unico rischio è continuare a rimandare.</h3><p class="body">Se entri nel programma, esegui con precisione il metodo concordato e non ottieni i risultati definiti insieme, hai diritto a un rimborso del 100%. Non è uno slogan di marketing. È una clausola del nostro contratto.</p><a class="btn btn--o" href="#" style="justify-self:start;margin-top:8px">Scrivimi su WhatsApp ora</a>''')
r('<div class="seal"><b>100%</b></div>', '<div class="seal"><span style="display:grid;justify-items:center;gap:4px"><b>100%</b><span style="font:700 10px/1 var(--text);letter-spacing:.14em">RIMBORSO</span></span></div>')

# footer
r('<a href="#">Termini e condizioni</a>', '<a href="#">Termini di Servizio</a>')

# typographic apostrophes, as in the PDF
for a, b in [("Perdere grasso è solo l'inizio.", "Perdere grasso è solo l’inizio."), ("Quando facevi sport c'erano", "Quando facevi sport c’erano"), ("se n'è andato", "se n’è andato")]:
    r(a, b)

assert '[testo dal Figma]' not in t and 'class="tbd"' not in t and 'tbd"' not in t.split('</style>')[1], re.findall(r'.{60}tbd.{60}', t.split('</style>')[1])
open(p, 'w').write(t)
print('ok')
