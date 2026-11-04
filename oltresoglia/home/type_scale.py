"""Homepage text hierarchy: one set of named text styles with fixed sizes per Framer breakpoint
(Desktop >= 1280, Tablet 810-1279, Phone < 810). Every font declaration in the page CSS is mapped to a style."""
import re
p = '/home/user/Skylarnina/oltresoglia/home/index.html'
t = open(p).read()
head, rest = t.split('</style>', 1)

TOKENS = '''
  /* TEXT STYLES (Framer: one Text Style each; sizes per breakpoint). Spec: HOME-TYPOGRAPHY.md */
  :root {
    --t-display: 120px; --t-h1: 40px; --t-h2: 36px; --t-stmt: 30px; --t-h3: 22px; --t-h4: 17px;
    --t-num: 56px; --t-numxl: 92px; --t-logo: 20px; --t-logo-s: 17px; --t-menu: 24px; --t-cap: 13px;
    --t-eyebrow: 13px; --t-lead: 20px; --t-bodyl: 18px; --t-body: 16px; --t-small: 13px; --t-label: 12px;
    --t-btn: 15px; --t-btn-s: 14px; --t-btncaps: 13px; --t-nav: 15px; --t-nav-s: 14px;
  }
  @media (max-width: 1279px) { :root {
    --t-display: 80px; --t-h1: 36px; --t-h2: 30px; --t-stmt: 26px; --t-h3: 20px; --t-h4: 16px;
    --t-num: 48px; --t-numxl: 80px; --t-logo: 18px; --t-lead: 18px; --t-bodyl: 17px;
  } }
  @media (max-width: 809px) { :root {
    --t-display: 38px; --t-h1: 30px; --t-h2: 26px; --t-stmt: 22px; --t-h3: 19px; --t-h4: 16px;
    --t-num: 40px; --t-numxl: 64px; --t-logo: 17px; --t-eyebrow: 12px; --t-lead: 17px; --t-bodyl: 16px; --t-body: 15px;
    --t-label: 11px; --t-btn: 14px; --t-btncaps: 12px;
  } }
'''

# (selector, old declaration, new declaration or '' to drop it)
MAP = [
    ('.h1', 'font: 800 clamp(36px, 4.6vw, 64px)/1.04 var(--display)', 'font: 800 var(--t-h1)/1.1 var(--display)'),
    ('.h2', 'font: 800 clamp(24px, 2.5vw, 36px)/1.12 var(--display)', 'font: 800 var(--t-h2)/1.12 var(--display)'),
    ('.h3', 'font: 700 clamp(19px, 1.5vw, 22px)/1.25 var(--display)', 'font: 700 var(--t-h3)/1.25 var(--display)'),
    ('.statement', 'font: 300 clamp(21px, 2vw, 30px)/1.25 var(--display)', 'font: 300 var(--t-stmt)/1.25 var(--display)'),
    ('.num', 'font: 800 clamp(34px, 3.4vw, 50px)/1 var(--display)', 'font: 800 var(--t-num)/1 var(--display)'),
    ('.eyebrow', 'font: 600 13px/1.3 var(--text)', 'font: 600 var(--t-eyebrow)/1.3 var(--text)'),
    ('.lead', 'font: 400 clamp(17px, 1.4vw, 20px)/1.55 var(--text)', 'font: 400 var(--t-lead)/1.55 var(--text)'),
    ('.body', 'font: 400 16px/1.6 var(--text)', 'font: 400 var(--t-body)/1.6 var(--text)'),
    ('.small', 'font: 500 13px/1.45 var(--text)', 'font: 500 var(--t-small)/1.45 var(--text)'),
    ('.btn', 'font: 700 15px/1.2 var(--text)', 'font: 700 var(--t-btn)/1.2 var(--text)'),
    ('.btn--o', 'font: 700 13px/1.2 var(--text)', 'font: 700 var(--t-btncaps)/1.2 var(--text)'),
    ('.btn--d', 'font: 700 13px/1.2 var(--text)', 'font: 700 var(--t-btncaps)/1.2 var(--text)'),
    ('.ph > span', 'font: 500 11px/1.3 var(--text)', 'font: 500 var(--t-label)/1.3 var(--text)'),
    ('.hero__word', 'font: 900 clamp(48px, 10.2vw, 132px)/1 var(--display)', 'font: 900 var(--t-display)/1 var(--display)'),
    ('.logo', 'font: 800 italic 20px/1 var(--display)', 'font: 800 italic var(--t-logo)/1 var(--display)'),
    ('.nav__links a', 'font: 500 15px/1 var(--text)', 'font: 500 var(--t-nav)/1 var(--text)'),
    ('.nav .btn', 'font-size: 14px', 'font-size: var(--t-btn-s)'),
    ('.hero__body .h1', 'font-size: clamp(28px, 2.9vw, 40px); line-height: 1.1;', ''),
    ('.hero__sub strong', 'font: 700 clamp(15px, 1.2vw, 17px)/1.5 var(--text)', 'font: 700 var(--t-bodyl)/1.5 var(--text)'),
    ('.chip b', 'font: 800 18px/1 var(--display)', 'font: 800 var(--t-h4)/1 var(--display)'),
    ('.chip--video', 'font: 700 15px/1 var(--text)', 'font: 700 var(--t-btn)/1 var(--text)'),
    ('.numbers__who', 'font: 600 15px/1.4 var(--text)', 'font: 600 var(--t-body)/1.4 var(--text)'),
    ('.rcard .ph div span', 'font: 500 11px/1 var(--text)', 'font: 500 var(--t-label)/1 var(--text)'),
    ('.rcard__label b', 'font: 800 clamp(16px, 1.4vw, 20px)/1.1 var(--display)', 'font: 800 var(--t-h3)/1.1 var(--display)'),
    ('.pill', 'font: 700 12px/1 var(--text)', 'font: 700 var(--t-label)/1 var(--text)'),
    ('.vc__title', 'font: 800 13px/1.25 var(--display)', 'font: 800 var(--t-cap)/1.25 var(--display)'),
    ('.vc__who b', 'font: 700 16px/1.2 var(--display)', 'font: 700 var(--t-h4)/1.2 var(--display)'),
    ('.fam__ic', 'font: 800 17px/1 var(--display)', 'font: 800 var(--t-h4)/1 var(--display)'),
    ('.band p.statement', 'font-size: clamp(24px, 2.4vw, 34px); line-height: 1.18;', 'font-size: var(--t-h2); line-height: 1.12;'),
    ('.band__imgs .ph p', 'font: 700 20px/1.25 var(--display)', 'font: 700 var(--t-h3)/1.25 var(--display)'),
    ('.vsl__mini .body', 'font-size: 14px; line-height: 1.5;', ''),
    ('.phase .k', 'font: 700 12px/1.2 var(--text)', 'font: 700 var(--t-label)/1.2 var(--text)'),
    ('.phase .h3', 'font-size: clamp(18px, 1.5vw, 21px);', ''),
    ('.phase .body', 'font-size: 14.5px; line-height: 1.55;', ''),
    ('.note', 'font: 400 15px/1.5 var(--text)', 'font: 400 var(--t-body)/1.5 var(--text)'),
    ('.perc__more p', 'font: 700 17px/1.3 var(--display)', 'font: 700 var(--t-h4)/1.3 var(--display)'),
    ('.plan__h b', 'font: 800 22px/1.2 var(--display)', 'font: 800 var(--t-h3)/1.2 var(--display)'),
    ('.tag', 'font: 700 11px/1 var(--text)', 'font: 700 var(--t-label)/1 var(--text)'),
    ('.plan li', 'font: 400 15px/1.5 var(--text)', 'font: 400 var(--t-body)/1.5 var(--text)'),
    ('.tcard__label b', 'font: 700 16px/1.15 var(--display)', 'font: 700 var(--t-h4)/1.15 var(--display)'),
    ('.fcard .h3', 'font-size: clamp(20px, 1.7vw, 24px);', ''),
    ('.fcard li', 'font: 400 15px/1.55 var(--text)', 'font: 400 var(--t-body)/1.55 var(--text)'),
    ('.fit__foot p', 'font: 700 clamp(18px, 1.6vw, 22px)/1.3 var(--display)', 'font: 700 var(--t-h3)/1.3 var(--display)'),
    ('.how__sign b', 'font: 700 16px/1.25 var(--display)', 'font: 700 var(--t-h4)/1.25 var(--display)'),
    ('.how__sign small', 'font: 500 13px/1.3 var(--text)', 'font: 500 var(--t-small)/1.3 var(--text)'),
    ('.hrow__n', 'font: 900 clamp(40px, 5vw, 68px)/.9 var(--display)', 'font: 900 var(--t-num)/.9 var(--display)'),
    ('.hrow__txt .h3', 'font-size: clamp(20px, 1.8vw, 26px);', ''),
    ('.hrow__txt .body', 'font-size: 16.5px;', ''),
    ('.guar__big b', 'font: 900 clamp(60px, 6.2vw, 92px)/.82 var(--display)', 'font: 900 var(--t-numxl)/.82 var(--display)'),
    ('.guar__big span', 'font: 700 12px/1 var(--text)', 'font: 700 var(--t-label)/1 var(--text)'),
    ('.guar__txt .h3', 'font-size: clamp(20px, 1.9vw, 28px);', ''),
    ('.foot__word', 'font: 900 clamp(44px, 9.1vw, 122px)/.9 var(--display)', 'font: 900 var(--t-display)/.9 var(--display)'),
    ('.foot__links', 'font: 500 14px/1 var(--text)', 'font: 500 var(--t-nav-s)/1 var(--text)'),
    ('.foot__bottom', 'font: 400 13px/1.5 var(--text)', 'font: 400 var(--t-small)/1.5 var(--text)'),
    ('.stick .logo', 'font-size: 17px', 'font-size: var(--t-logo-s)'),
    ('.stick .nav__links a', 'font-size: 14px', 'font-size: var(--t-nav-s)'),
    ('.stick .btn', 'font-size: 14px', 'font-size: var(--t-btn-s)'),
    ('.mmenu::after', 'font: 900 64px/1 var(--display)', 'font: 900 var(--t-numxl)/1 var(--display)'),
    ('.mmenu__top .logo', 'font-size: 17px', 'font-size: var(--t-logo-s)'),
    ('.mmenu__list small', 'font: 600 11px/1 var(--text)', 'font: 600 var(--t-label)/1 var(--text)'),
    ('.mmenu__list span', 'font: 700 24px/1.1 var(--display)', 'font: 700 var(--t-menu)/1.1 var(--display)'),
    ('.mmenu__ghost', 'font-size: 13px', 'font-size: var(--t-small)'),
    ('.mmenu__note', 'font: 500 12px/1.4 var(--text)', 'font: 500 var(--t-small)/1.4 var(--text)'),
]

done = 0
for sel, old, new in MAP:
    # every rule whose selector list contains `sel` exactly and whose body has `old`
    pat = re.compile(r'(^|[\s}])(' + re.escape(sel) + r'(?:\s*,[^{]*)?)\s*\{([^{}]*)\}', re.M)
    hit = False
    for m in pat.finditer(head):
        body = m.group(3)
        if old in body:
            nb = body.replace(old, new, 1)
            nb = re.sub(r';\s*;', ';', nb)
            head = head[:m.start(3)] + nb + head[m.end(3):]
            hit = True
            break
    assert hit, (sel, old)
    done += 1

# drop the vw-based phone overrides for the two wordmarks (the tokens handle them)
for a in ['    .hero__word { font-size: 15.5vw; }\n', '    .foot__word { font-size: 10.6vw; }\n']:
    assert head.count(a) == 1, a; head = head.replace(a, '')
head = head.replace(' .hero__word { bottom: 84px; }', ' .hero__word { bottom: 84px; }')
# rules emptied by the mapping
head = re.sub(r'\n  [^{}\n]+\{\s*\}', '', head)

head = head.replace('  *, *::before, *::after { box-sizing: border-box; }', TOKENS.rstrip('\n') + '\n  *, *::before, *::after { box-sizing: border-box; }', 1)
open(p, 'w').write(head + '</style>' + rest)
# report anything still sized outside the tokens
css = head.split('/* TEXT STYLES')[0] + head.split('--t-btncaps: 12px;\n  } }')[1]
print(done, 'mapped; leftovers:', re.findall(r'font(?:-size)?:[^;]*?\d+px[^;]*', css))
