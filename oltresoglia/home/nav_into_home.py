"""Add the sticky scroll bar and the phone menu (from nav.html) to the homepage."""
p = '/home/user/Skylarnina/oltresoglia/home/index.html'
t = open(p).read()
WA = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 11.5a8.4 8.4 0 0 1-12.4 7.4L3 21l2.1-5.4A8.4 8.4 0 1 1 21 11.5z"/></svg>'
ARR = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M7 17L17 7M9 7h8v8"/></svg>'
LINKS = ['Home', 'Il team', 'La strategia', 'Ebook gratuiti', 'Testimonianze', 'Contatti']


def r(a, b):
    global t
    assert t.count(a) == 1, a[:80]
    t = t.replace(a, b)


css = '''
  /* NAV · sticky bar while scrolling + phone menu (states drawn in nav.html) */
  .stick { position: fixed; z-index: 50; top: 16px; left: 50%; width: min(1180px, calc(100% - 32px)); transform: translate(-50%, -140%); transition: transform .5s var(--ease);
    display: flex; align-items: center; justify-content: space-between; gap: 24px; height: 68px; padding: 0 12px 0 28px; border-radius: 999px;
    background: rgba(13,13,13,.86); backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px); border: 1px solid rgba(255,255,255,.06); box-shadow: 0 20px 40px -24px rgba(0,0,0,.6); }
  body.is-stuck .stick { transform: translate(-50%, 0); }
  .stick .logo { font-size: 17px; }
  .stick .nav__links { background: none; backdrop-filter: none; padding: 0; }
  .stick .nav__links a { font-size: 14px; }
  .stick__right { display: flex; gap: 10px; align-items: center; }
  .stick .btn { min-height: 46px; padding: 0 22px; font-size: 14px; }
  .stick .nav__menu { display: none; }
  .mmenu { position: fixed; z-index: 60; inset: 12px; border-radius: 24px; background: var(--dark); color: var(--on-dark); display: flex; flex-direction: column; padding: 0 16px 22px 22px;
    overflow: hidden auto; opacity: 0; visibility: hidden; transform: translateY(-16px); transition: opacity .5s var(--ease), transform .5s var(--ease), visibility 0s .5s; }
  body.menu-open { overflow: hidden; }
  body.menu-open .mmenu { opacity: 1; visibility: visible; transform: none; transition: opacity .5s var(--ease), transform .5s var(--ease); }
  .mmenu::after { content: 'OLTRESOGLIA'; position: absolute; left: -6px; bottom: 236px; font: 900 64px/1 var(--display); letter-spacing: -.03em; color: transparent; -webkit-text-stroke: 1px #2E2E2E; white-space: nowrap; pointer-events: none; }
  .mmenu__top { display: flex; align-items: center; justify-content: space-between; min-height: 76px; }
  .mmenu__top .logo { font-size: 17px; }
  .mmenu__close { width: 46px; height: 46px; border-radius: 999px; border: 1.5px solid var(--yellow); background: none; color: var(--yellow); display: grid; place-items: center; cursor: pointer; }
  .mmenu__close svg { width: 18px; }
  .mmenu__list { margin-top: 18px; display: grid; }
  .mmenu__list a { display: grid; grid-template-columns: 34px 1fr auto; align-items: center; gap: 8px; padding: 17px 6px 17px 0; border-bottom: 1px solid var(--hair-d); text-decoration: none; color: var(--on-dark);
    opacity: 0; transform: translateY(10px); transition: opacity .4s var(--ease), transform .4s var(--ease); }
  .mmenu__list li:first-child a { border-top: 1px solid var(--hair-d); }
  body.menu-open .mmenu__list a { opacity: 1; transform: none; }
  .mmenu__list li:nth-child(2) a { transition-delay: .04s; } .mmenu__list li:nth-child(3) a { transition-delay: .08s; } .mmenu__list li:nth-child(4) a { transition-delay: .12s; }
  .mmenu__list li:nth-child(5) a { transition-delay: .16s; } .mmenu__list li:nth-child(6) a { transition-delay: .2s; }
  .mmenu__list small { font: 600 11px/1 var(--text); letter-spacing: .12em; color: #6E6A62; }
  .mmenu__list span { font: 700 24px/1.1 var(--display); letter-spacing: -.01em; }
  .mmenu__list svg { width: 18px; color: #6E6A62; }
  .mmenu__list a[aria-current] :is(small, span, svg) { color: var(--yellow); }
  .mmenu__foot { margin-top: auto; padding-top: 28px; display: grid; gap: 12px; position: relative; z-index: 1; }
  .mmenu__foot .btn { width: 100%; }
  .mmenu__ghost { border: 1.5px solid #4A4A4A; color: var(--on-dark); font-size: 13px; white-space: nowrap; }
  .mmenu__note { font: 500 12px/1.4 var(--text); color: #6E6A62; text-align: center; }
  .nav__menu { cursor: pointer; }
'''
r('  /* Responsive */', css + '\n  /* Responsive */')
r('    .nav__links { display: none; } .nav__menu { display: grid; }',
  '    .nav__links { display: none; } .nav__menu { display: grid; } .stick .nav__menu { display: grid; } .stick { padding-left: 22px; }')
r('    .nav .btn span { display: none; } .nav .btn { padding: 0 16px; }',
  '    .nav .btn span, .stick .btn span { display: none; } .nav .btn, .stick .btn { padding: 0 16px; } .stick { top: 12px; width: calc(100% - 24px); height: 64px; padding: 0 9px 0 18px; }')

# burger in the hero: two lines, opens the menu
old = [l for l in t.splitlines() if '<button class="nav__menu"' in l]
assert len(old) == 1
burger = '<button class="nav__menu" type="button" aria-label="Apri il menu" aria-controls="mmenu" aria-expanded="false" data-menu-open><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 8h16M4 16h16"/></svg></button>'
t = t.replace(old[0], '        ' + burger)

CUR = ' aria-current="page"'
links_nav = ''.join(f'<a href="#"{CUR if i == 0 else ""}>{n}</a>' for i, n in enumerate(LINKS))
NL = '\n'
links_menu = NL.join(f'      <li><a href="#"{CUR if i == 0 else ""}><small>0{i + 1}</small><span>{n}</span>{ARR}</a></li>' for i, n in enumerate(LINKS))
extra = f'''  </header>

  <!-- NAV · sticky bar (appears after the hero) -->
  <nav class="stick" aria-label="Menu principale (fisso)">
    <a class="logo" href="#">OLTRESOGLIA</a>
    <div class="nav__links">{links_nav}</div>
    <div class="stick__right">
      <a class="btn btn--y" href="#">{WA}<span>Whatsapp</span></a>
      {burger}
    </div>
  </nav>

  <!-- NAV · phone menu -->
  <div class="mmenu" id="mmenu" role="dialog" aria-modal="true" aria-label="Menu">
    <div class="mmenu__top">
      <a class="logo" href="#">OLTRESOGLIA</a>
      <button class="mmenu__close" type="button" aria-label="Chiudi il menu" data-menu-close><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg></button>
    </div>
    <ul class="mmenu__list">
{links_menu}
    </ul>
    <div class="mmenu__foot">
      <a class="btn btn--y" href="#">{WA}Whatsapp</a>
      <a class="btn mmenu__ghost" href="#">Ricevi gratis la strategia da cui ripartire →</a>
      <p class="mmenu__note">Dott. Pietro Vecchi, Biologo Nutrizionista</p>
    </div>
  </div>'''
r('  </header>', extra)

js = '''
  // Sticky bar after the hero; phone menu open / close
  const hero = document.querySelector('.hero')
  new IntersectionObserver(([e]) => document.body.classList.toggle('is-stuck', !e.isIntersecting), { rootMargin: '-80px 0px 0px 0px' }).observe(hero)
  const setMenu = (open) => {
    document.body.classList.toggle('menu-open', open)
    document.querySelectorAll('[data-menu-open]').forEach((b) => b.setAttribute('aria-expanded', String(open)))
    if (open) document.querySelector('[data-menu-close]').focus()
  }
  document.querySelectorAll('[data-menu-open]').forEach((b) => b.addEventListener('click', () => setMenu(true)))
  document.querySelector('[data-menu-close]').addEventListener('click', () => setMenu(false))
  document.querySelectorAll('.mmenu a').forEach((a) => a.addEventListener('click', () => setMenu(false)))
  addEventListener('keydown', (e) => { if (e.key === 'Escape') setMenu(false) })
</script>'''
assert t.count('</script>') == 1
t = t.replace('</script>', js)
open(p, 'w').write(t)
print('ok')
