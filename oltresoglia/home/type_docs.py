"""Write HOME-TYPOGRAPHY.md and the visual type board (home/tipografia.html) from one table."""
import html
R = '/home/user/Skylarnina/oltresoglia'

# name, token, family, weight, (desktop, tablet, phone), line height, letter spacing, case, colour note, used for, sample
STYLES = [
    ('Display', '--t-display', 'Bounded', 'Black 900', (120, 80, 38), '1.0', '-3%', 'UPPER', 'Outline only (1.5px yellow 55% / #3A3A3A on footer)', 'OLTRESOGLIA wordmark behind Pietro in the hero; footer wordmark', 'OLTRESOGLIA'),
    ('H1', '--t-h1', 'Bounded', 'ExtraBold 800', (40, 36, 30), '1.1', '-1.5%', 'Sentence', 'White; last line yellow', 'Hero headline (one per page)', 'Eri uno sportivo. Il lavoro si è preso tutto.'),
    ('H2', '--t-h2', 'Bounded', 'ExtraBold 800', (36, 30, 26), '1.12', '-1%', 'Sentence', 'Charcoal on light, white on dark', 'Section titles; the "Il fisico che avevi…" band', 'Risultati reali, senza filtri'),
    ('Statement', '--t-stmt', 'Bounded', 'Light 300', (30, 26, 22), '1.25', '-1%', 'Sentence', 'Charcoal on yellow', 'The credo sentence (yellow card)', 'Noi crediamo che non esistano professionisti senza costanza.'),
    ('H3', '--t-h3', 'Bounded', 'Bold 700', (22, 20, 19), '1.25', '0', 'Sentence', 'Charcoal / white', 'Card and step titles, phase names, plan titles, kg results (800), "Se ti riconosci…"', 'Parti forte. Dopo pochi giorni molli.'),
    ('H4', '--t-h4', 'Bounded', 'Bold 700', (17, 16, 16), '1.25', '0', 'Sentence', 'Charcoal / white', 'Names on cards (team, videos, Pietro), "Vuoi saperne di più?", +500 chip, 01–03 badges (800)', 'Pietro Vecchi'),
    ('Numeral L', '--t-num', 'Bounded', 'ExtraBold 800 / Black 900', (56, 44, 40), '1.0', '-2%', '—', 'Charcoal; outline on the Come funziona rows', 'Numbers row (+500, +10 anni, 100%); 01–03 in Come funziona', '+10 anni'),
    ('Numeral XL', '--t-numxl', 'Bounded', 'Black 900', (92, 80, 64), '0.82', '-4%', '—', 'Charcoal on yellow', '100% in the guarantee card', '100%'),
    ('Logo', '--t-logo', 'Bounded', 'ExtraBold 800 Italic', (20, 18, 17), '1.0', '+8%', 'UPPER', 'White', 'Wordmark in the nav (17 in the sticky bar and phone menu) until the logo SVG is in', 'OLTRESOGLIA'),
    ('Menu link', '--t-menu', 'Bounded', 'Bold 700', (24, 24, 24), '1.1', '-1%', 'Sentence', 'White; current page yellow', 'Links in the phone/tablet menu', 'Ebook gratuiti'),
    ('Caption caps', '--t-cap', 'Bounded', 'ExtraBold 800', (13, 13, 13), '1.25', '0', 'UPPER', 'White on video', 'Title over the video thumbnails', '[TITOLO IN SOVRAIMPRESSIONE]'),
    ('Eyebrow', '--t-eyebrow', 'Manrope', 'SemiBold 600', (13, 13, 12), '1.3', '+16%', 'UPPER', 'Gold #8A5A00 on light, yellow on dark', 'Small label above each section title', 'RISULTATI E TESTIMONIANZE'),
    ('Lead', '--t-lead', 'Manrope', 'Regular 400', (20, 18, 17), '1.55', '0', 'Sentence', 'Charcoal 80% / #BDB8AE on dark', 'Intro paragraphs (hero, credo, team), the four week types', 'Nel lavoro reggi tutto e tutti. Il tuo corpo è finito in fondo alla lista.'),
    ('Body L', '--t-bodyl', 'Manrope', 'Bold 700', (18, 17, 16), '1.5', '0', 'Sentence', 'White', 'The bold hero sentence', 'OLTRESOGLIA è il sistema per perdere grasso e tornare atletico'),
    ('Body', '--t-body', 'Manrope', 'Regular 400 (bold leads 700)', (16, 16, 15), '1.6', '0', 'Sentence', 'Charcoal 70% / #BDB8AE on dark', 'All running text: cards, steps, phases, comparison, lists, guarantee, note', 'Ti rispondiamo noi e capiamo insieme da dove parti.'),
    ('Small', '--t-small', 'Manrope', 'Medium 500', (13, 13, 13), '1.45', '0', 'Sentence', '#8C877E', 'Stat labels, captions under names, "Test immediato · meno di 2\'", footer line', "Test immediato · meno di 2'"),
    ('Label', '--t-label', 'Manrope', 'Bold 700', (12, 12, 11), '1.0', '+12% (caps)', 'UPPER or Sentence', 'Gold / grey / charcoal on yellow pill', 'PRIMA / DOPO, FASE 1:, RIMBORSO, pills ("in 8 mesi"), menu numbers, photo-slot labels', 'FASE 1:'),
    ('Button', '--t-btn', 'Manrope', 'Bold 700', (15, 15, 14), '1.2', '0', 'Sentence', 'Charcoal on yellow', 'Yellow buttons (14 in the nav and sticky bar)', 'Ricevi gratis la strategia da cui ripartire →'),
    ('Button caps', '--t-btncaps', 'Manrope', 'Bold 700', (13, 13, 12), '1.2', '+10%', 'UPPER', 'Yellow on black', 'Outline and black buttons', 'SCOPRI IL TEAM OLTRESOGLIA →'),
    ('Nav', '--t-nav', 'Manrope', 'Medium 500', (15, 15, 15), '1.0', '0', 'Sentence', '#E8E4DC; current yellow + 2px underline', 'Navbar links (14 in the sticky bar and footer)', 'La strategia'),
]

FONT_CSS = {'Bounded': "'Bounded', 'Archivo Black', sans-serif", 'Manrope': "'Manrope', system-ui, sans-serif"}
WEIGHT = lambda w: int(''.join(c for c in w.split('/')[0] if c.isdigit()) or 400)

# ---------- markdown ----------
md = ['# OLTRESOGLIA Home: text hierarchy across breakpoints', '',
      'One Text Style per row. Breakpoints match the Framer file: **Desktop ≥ 1280**, **Tablet 810–1279**, **Phone < 810**.',
      'Sizes are fixed per breakpoint (no fluid scaling), so they can be set exactly in Framer. In the prototype they are the',
      '`--t-*` tokens at the top of `home/index.html`; every text on the page uses one of them.', '',
      '| Style | Font | Weight | Desktop | Tablet | Phone | Line height | Letter spacing | Case | Colour | Used for |',
      '|---|---|---|---|---|---|---|---|---|---|---|']
for n, tok, fam, w, (d, tb, ph), lh, ls, case, col, use, _ in STYLES:
    md.append(f'| **{n}** | {fam} | {w} | {d} | {tb} | {ph} | {lh} | {ls} | {case} | {col} | {use} |')
md += ['', '## Rules', '',
       '- One H1 per page (the hero). Every section title is H2; nothing between H2 and H3.',
       '- Sentence case for all titles (as in the Figma file); UPPERCASE only for Eyebrow, Label, Button caps, Caption caps and the wordmarks.',
       '- Bounded for titles, numbers and names; Manrope for everything you read in sentences, labels and buttons.',
       '- Bold leads inside Body (e.g. "**Solo pesi o solo cardio.** Ti rendono…") stay Body size, weight 700.',
       '- Line length: Lead and Body max ~60 characters per line on desktop.',
       '- Wordmarks are decorative outlines (aria-hidden); the real logo SVG replaces the Logo style when it arrives.', '',
       '## Framer setup', '',
       '1. Create the 20 Text Styles above (Assets → Text Styles), each with three breakpoint sizes.',
       '2. Name them exactly as in the table, so they match this document and the prototype tokens.',
       '3. Colours are separate colour styles (already set up in Framer); apply them per use, not inside the text style.', '']
open(f'{R}/home/HOME-TYPOGRAPHY.md', 'w').write('\n'.join(md))

# ---------- visual board ----------
rows = []
for n, tok, fam, w, (d, tb, ph), lh, ls, case, col, use, sample in STYLES:
    ls_css = ls.split(' ')[0].replace('%', '')
    ls_css = f'{float(ls_css) / 100}em' if ls_css not in ('0', '—') else '0'
    tt = 'uppercase' if case.startswith('UPPER') else 'none'
    ital = 'italic' if 'Italic' in w else 'normal'
    outline = n == 'Display'
    style = (f"font-family:{FONT_CSS[fam]};font-weight:{WEIGHT(w)};font-style:{ital};font-size:{min(d, 72)}px;line-height:{lh if lh != '—' else 1.2};"
             f"letter-spacing:{ls_css};text-transform:{tt};" + ("color:transparent;-webkit-text-stroke:1.5px #C99A3E;" if outline else ""))
    rows.append(f'''    <div class="row">
      <div class="meta"><b>{html.escape(n)}</b><span>{fam} · {html.escape(w)}</span><span>LH {lh} · LS {html.escape(ls)} · {html.escape(case)}</span></div>
      <div class="sizes"><span><i>D</i>{d}</span><span><i>T</i>{tb}</span><span><i>P</i>{ph}</span></div>
      <div class="sample"><p style="{style}">{html.escape(sample)}</p><small>{html.escape(use)}{' · shown at 72px' if d > 72 else ''}</small></div>
    </div>''')

board = f'''<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>OLTRESOGLIA · Home text styles</title>
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" />
<style>
  /* Text hierarchy board for Figma (html.to.design). Source of truth: HOME-TYPOGRAPHY.md */
  @font-face {{ font-family: 'Bounded'; src: url('../fonts/Bounded-Variable.ttf') format('truetype'); font-weight: 200 900; font-style: normal; font-display: swap; }}
  *, *::before, *::after {{ box-sizing: border-box; }}
  body {{ margin: 0; background: #F5F3EE; color: #0D0D0D; font-family: 'Manrope', system-ui, sans-serif; -webkit-font-smoothing: antialiased; }}
  p {{ margin: 0; }}
  .wrap {{ max-width: 1280px; margin: 0 auto; padding: 56px 40px 80px; }}
  .top {{ display: flex; justify-content: space-between; align-items: end; gap: 24px; padding-bottom: 28px; border-bottom: 2px solid #0D0D0D; }}
  .top h1 {{ margin: 0; font: 800 40px/1.1 'Bounded', sans-serif; letter-spacing: -.015em; }}
  .top p {{ font: 500 14px/1.5 'Manrope', sans-serif; color: #4A4740; max-width: 46ch; text-align: right; }}
  .legend {{ display: grid; grid-template-columns: 260px 210px 1fr; gap: 32px; padding: 14px 0; border-bottom: 1px solid #DDD7CB; font: 700 11px/1 'Manrope', sans-serif; letter-spacing: .14em; text-transform: uppercase; color: #8A5A00; }}
  .row {{ display: grid; grid-template-columns: 260px 210px 1fr; gap: 32px; align-items: center; padding: 26px 0; border-bottom: 1px solid #DDD7CB; }}
  .meta {{ display: grid; gap: 4px; }}
  .meta b {{ font: 700 17px/1.2 'Bounded', sans-serif; }}
  .meta span {{ font: 500 12.5px/1.4 'Manrope', sans-serif; color: #6E6A62; }}
  .sizes {{ display: flex; gap: 8px; }}
  .sizes span {{ display: grid; justify-items: center; gap: 4px; width: 62px; padding: 10px 0; border-radius: 12px; background: #fff; font: 800 18px/1 'Bounded', sans-serif; }}
  .sizes i {{ font: 700 10px/1 'Manrope', sans-serif; font-style: normal; letter-spacing: .12em; color: #8C877E; }}
  .sample {{ display: grid; gap: 8px; min-width: 0; }}
  .sample p {{ overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }}
  .sample small {{ font: 500 12.5px/1.4 'Manrope', sans-serif; color: #8C877E; }}
  .group {{ margin-top: 40px; font: 700 12px/1 'Manrope', sans-serif; letter-spacing: .16em; text-transform: uppercase; color: #0D0D0D; padding: 8px 12px; background: #F9BF58; border-radius: 999px; display: inline-block; }}
</style>
</head>
<body>
<div class="wrap">
  <div class="top"><h1>Home · text styles</h1><p>20 Text Styles. Sizes in px for Desktop (≥ 1280) · Tablet (810–1279) · Phone (&lt; 810). Bounded for titles, numbers and names; Manrope for reading, labels and buttons.</p></div>
  <p class="group">Bounded</p>
  <div class="legend"><span>Style</span><span>D · T · P (px)</span><span>Sample · where it is used</span></div>
{chr(10).join(rows[:11])}
  <p class="group">Manrope</p>
  <div class="legend"><span>Style</span><span>D · T · P (px)</span><span>Sample · where it is used</span></div>
{chr(10).join(rows[11:])}
</div>
</body>
</html>
'''
open(f'{R}/home/tipografia.html', 'w').write(board)
print('ok', len(STYLES))
