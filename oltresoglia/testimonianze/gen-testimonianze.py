"""Testimonianze: section structure on the Apex Coaching Academy reference (two auto-scrolling rows: messages, then
before/after photos) with Bibi's message-card design (black card, Saffron border, bold name at text size, the message, a tick).
Same rules as the other pages: one type role per text element, no type properties outside styles/type.css, Italian only.
"""
import base64, html, os, re, sys
S = '/tmp/claude-0/-home-user-Skylarnina/d3a326d7-8059-5f41-b39f-346e6a334423/scratchpad'
R = '/home/user/Skylarnina/oltresoglia'
OUT = f'{R}/testimonianze'
sys.path.insert(0, S)
from testimonials_copy import TITLE, DESC, MESSAGES, PHOTOS, PENDING
TYPE_CSS = open(f'{R}/styles/type.css').read()
def esc(t): return html.escape(t, quote=False)

css = r"""
  :root {
    --oltre-dark-charcoal: #0D0D0D; --oltre-porcelain: #F5F3EE; --oltre-saffron-mango: #F9BF58;
    --ink-2: color-mix(in srgb, var(--oltre-porcelain) 78%, transparent);
    --line: color-mix(in srgb, var(--oltre-porcelain) 14%, transparent);
    --edge: max(clamp(16px, 4vw, 48px), calc((100vw - 1232px) / 2 + 32px));
    --gap: 24px;
    color-scheme: dark;
  }
  *, *::before, *::after { box-sizing: border-box; }
  html, body { margin: 0; background: var(--oltre-dark-charcoal); color: var(--oltre-porcelain); }
  body { font-family: var(--font-text); -webkit-font-smoothing: antialiased; overflow-x: clip; }
  h2, p { margin: 0; }

  .tst { padding: var(--space-section) 0; display: grid; gap: clamp(32px, 4vw, 56px); }
  .tst__head { padding: 0 var(--edge); display: grid; justify-items: center; text-align: center; gap: var(--space-heading); }
  .tst__head .t-h1 { max-width: 22ch; }
  .tst__head .t-lead { max-width: 60ch; color: var(--ink-2); }

  .rows { display: grid; gap: var(--gap); }
  .marquee { overflow: hidden; -webkit-mask-image: linear-gradient(90deg, transparent, #000 6%, #000 94%, transparent); mask-image: linear-gradient(90deg, transparent, #000 6%, #000 94%, transparent); }
  .track { display: flex; gap: var(--gap); width: max-content; padding-block: 4px; animation: slide var(--dur, 60s) linear infinite; }
  .marquee--rev .track { animation-direction: reverse; }
  .marquee:hover .track, .marquee:focus-within .track { animation-play-state: paused; }
  @keyframes slide { to { transform: translateX(calc(-50% - var(--gap) / 2)); } }

  .msg { width: clamp(280px, 26vw, 360px); min-height: clamp(280px, 26vw, 340px); padding: clamp(24px, 2.8vw, 40px); border-radius: 24px;
    background: #141414; border: 2px solid var(--oltre-saffron-mango); display: flex; flex-direction: column; gap: 10px; }
  .msg .t-body { color: var(--oltre-porcelain); max-width: none; white-space: pre-line; }
  .msg .pending { color: color-mix(in srgb, var(--oltre-porcelain) 45%, transparent); }
  .msg__tick { margin-top: auto; align-self: flex-end; width: 26px; height: 26px; color: var(--oltre-saffron-mango); }

  .ba { width: clamp(280px, 26vw, 360px); aspect-ratio: 1; border-radius: 18px; overflow: hidden; display: grid; grid-template-columns: 1fr 1fr; gap: 2px;
    background: var(--line); border: 1px solid var(--line); position: relative; }
  .ba__half { position: relative; display: grid; place-items: center; background: #161616; }
  .ba__half:last-child { background: #1d1d1d; }
  .ba__half .t-small { position: absolute; top: 12px; left: 12px; padding: 4px 10px; border-radius: 999px; background: rgba(5,5,5,.7); color: var(--oltre-porcelain); max-width: none; }
  .ba__half svg { width: 40%; color: color-mix(in srgb, var(--oltre-porcelain) 18%, transparent); }
  .ba__mark { position: absolute; left: 12px; bottom: 12px; padding: 6px 10px; background: var(--oltre-saffron-mango); color: var(--oltre-dark-charcoal); border-radius: 4px; }

  @media (prefers-reduced-motion: reduce) {
    .marquee { overflow-x: auto; -webkit-mask-image: none; mask-image: none; padding-inline: var(--edge); }
    .track { animation: none; }
    .track [aria-hidden="true"] { display: none; }
  }
"""
for banned in ('font-size', 'line-height', 'letter-spacing', 'font-weight', 'text-transform', 'font:'):
    assert banned not in css, banned
css = re.sub(r'\n?\s*/\*.*?\*/', '', css, flags=re.S)

TICK = '<svg class="msg__tick" viewBox="0 0 24 24" aria-hidden="true"><path d="m4 12.5 5 5L20 6.5" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>'
SIL = '<svg viewBox="0 0 40 60" aria-hidden="true"><circle cx="20" cy="11" r="7" fill="currentColor"/><path d="M8 58V30c0-6 5-10 12-10s12 4 12 10v28z" fill="currentColor"/></svg>'

HID = ' aria-hidden="true"'
def msg(name, text, hidden):
    cls = 't-body pending' if text == PENDING else 't-body'
    return (f'<figure class="msg"{HID if hidden else ""} style="margin:0">'
            f'<p class="t-body"><strong>{esc(name)}</strong></p><blockquote style="margin:0"><p class="{cls}">{esc(text)}</p></blockquote>{TICK}</figure>')

def photo(n, hidden):
    return (f'<figure class="ba"{HID if hidden else ""} style="margin:0" aria-label="Foto prima e dopo {n} (in arrivo)">'
            f'<div class="ba__half"><span class="t-small">Prima</span>{SIL}</div><div class="ba__half"><span class="t-small">Dopo</span>{SIL}</div>'
            f'<span class="ba__mark t-button">OLTRESOGLIA</span></figure>')

msgs = ''.join(msg(n, t, False) for n, t in MESSAGES) + ''.join(msg(n, t, True) for n, t in MESSAGES)
photos = ''.join(photo(i + 1, False) for i in range(PHOTOS)) + ''.join(photo(i + 1, True) for i in range(PHOTOS))

doc = f'''<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>OLTRESOGLIA Testimonianze</title>
<link rel="stylesheet" href="../styles/type.css" />
<style>{css}</style>
</head>
<body>
  <section class="tst" aria-labelledby="tst-title">
    <div class="tst__head">
      <h2 class="t-h1" id="tst-title">{esc(TITLE)}</h2>
      <p class="t-lead">{esc(DESC)}</p>
    </div>
    <div class="rows">
      <div class="marquee" style="--dur: 70s" aria-label="Messaggi dei clienti"><div class="track">{msgs}</div></div>
      <div class="marquee marquee--rev" style="--dur: 80s" aria-label="Foto prima e dopo"><div class="track">{photos}</div></div>
    </div>
  </section>
</body>
</html>
'''
for banned in ('font-size', 'line-height', 'letter-spacing', 'font-weight', 'text-transform'):
    assert banned not in doc, banned
os.makedirs(f'{OUT}/export', exist_ok=True)
open(f'{OUT}/index.html', 'w').write(doc)
standalone = doc.replace('<link rel="stylesheet" href="../styles/type.css" />', '<style>' + TYPE_CSS.replace("url('../fonts/", "url('../../fonts/") + '</style>')
open(f'{OUT}/export/index.html', 'w').write(standalone)
a = re.sub(r'<!doctype html>\s*<html lang="it">\s*<head>\s*<meta charset="utf-8" />\s*<meta name="viewport"[^>]*>\s*', '', standalone)
a = a.replace('</head>\n<body>\n', '').replace('</body>\n</html>\n', '')
open(f'{S}/oltresoglia-testimonianze.html', 'w').write(a)
print('ok', len(doc))
