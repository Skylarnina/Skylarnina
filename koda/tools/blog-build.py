#!/usr/bin/env python3
"""Builds koda/site/v4/blog.html (journal index) and post.html (one note) from the homepage's base.

The bar, buttons, photo slots, route line, overlay, prototype switches and script are lifted from index.html
so the three pages share one system. Run after any change to index.html:  python3 koda/tools/blog-build.py
"""
import re, pathlib

SITE = pathlib.Path(__file__).resolve().parent.parent / "site" / "v4"
src = (SITE / "index.html").read_text()

def between(a, b, s=src):
    i = s.index(a); j = s.index(b, i) + len(b); return s[i:j]

head_links = between('<link rel="preconnect"', 'display=swap">')
style = between('<style>', '</style>')
header = between('<header class="bar"', '</header>')
close_footer = between('<section class="close-band', '</footer>')
chrome = between('<div class="sticky"', '</div>\n</div>')          # sticky + proto + booking overlay
scripts = between('<script src="vendor/gsap.min.js">', '</script>\n')
scripts = src[src.index('<script src="vendor/gsap.min.js">'):].rstrip()

# nav for the journal pages: section links point back at the homepage, Journal is current
header = header.replace('href="#ways"', 'href="index.html#ways"').replace('href="#evening"', 'href="index.html#evening"') \
               .replace('href="#who"', 'href="index.html#who"').replace('href="#answers"', 'href="index.html#answers"') \
               .replace('href="#top"', 'href="index.html"')
header = header.replace('<a href="blog.html">Journal</a>', '<a href="blog.html" aria-current="page" style="color:var(--navy)">Journal</a>')
close_footer = close_footer.replace('href="#ways"', 'href="index.html#ways"').replace('href="#evening"', 'href="index.html#evening"') \
                           .replace('href="#who"', 'href="index.html#who"').replace('href="#how"', 'href="index.html#how"') \
                           .replace('href="#founder"', 'href="index.html#founder"').replace('href="#cancellations"', 'href="index.html#cancellations"') \
                           .replace('href="#answers"', 'href="index.html#answers"').replace('href="#top"', 'href="index.html"')

BLOG_CSS = """
<style>
/* ======================================================
   JOURNAL — index and note, built on the homepage system
   ====================================================== */
.bar-time{ white-space:nowrap; }
.jhero{ padding-block:72px 48px; }
.jhero .grid{ align-items:end; }
.jhero .t{ grid-column:1 / 8; display:flex; flex-direction:column; gap:22px; align-items:flex-start; }
.jhero .t h1{ font-size:clamp(46px,6.2vw,88px); line-height:.98; }
.jhero .r{ grid-column:9 / 13; display:flex; flex-direction:column; gap:14px; }
.jhero .r .nums{ display:flex; border-top:.5px solid var(--stone); }
.jhero .r .nums div{ flex:1; padding:16px 16px 0 0; border-right:.5px solid var(--stone-50); } .jhero .r .nums div + div{ padding-left:18px; } .jhero .r .nums div:last-child{ border-right:0; }
.jhero .r .nums b{ display:block; font:300 36px/1 var(--serif); font-variant-numeric:lining-nums; } .jhero .r .nums span{ display:block; margin-top:6px; font:300 12px/1.5 var(--sans); color:rgba(13,31,45,.62); }
.featured.photo-card{ display:block; margin-top:56px; aspect-ratio:16 / 8; text-decoration:none; color:inherit; }
.featured .fx{ position:absolute; inset:auto 0 0 0; z-index:3; padding:40px; display:grid; grid-template-columns:7fr 5fr; column-gap:24px; align-items:end; background:rgba(13,31,45,.6); }
html[data-look="colour"] .featured .fx{ background:linear-gradient(to top, rgba(0,0,0,.82) 0%, rgba(0,0,0,.45) 60%, rgba(0,0,0,0) 100%); padding-top:110px; }
.featured .fx .eyebrow{ color:var(--stone); margin-bottom:14px; }
.featured .fx h2{ font:300 clamp(32px,3.6vw,52px)/1.04 var(--serif); color:var(--bone); text-wrap:balance; }
.featured .fx p{ font:300 14px/1.6 var(--sans); color:rgba(240,235,227,.62); max-width:40ch; margin-top:12px; }
.featured .fx .go{ justify-self:end; display:flex; align-items:center; gap:14px; color:var(--bone); }
.featured .fx .go .ring{ border-color:var(--bone); color:var(--bone); }
.featured .pin-lbl{ left:40px; top:36px; }
.filters{ margin-top:72px; display:flex; justify-content:space-between; align-items:center; gap:24px; flex-wrap:wrap; }
.filters .chips .chip{ height:40px; }
.posts{ margin-top:48px; display:grid; grid-template-columns:repeat(12,minmax(0,1fr)); gap:56px 24px; }
.post{ display:flex; flex-direction:column; }
.post .photo-card{ aspect-ratio:4 / 3; }
.post.tall .photo-card{ aspect-ratio:4 / 4.6; }
.post.wide .photo-card{ aspect-ratio:16 / 8.5; }
.post .meta{ margin-top:20px; display:flex; justify-content:space-between; gap:16px; }
.post h3{ margin-top:12px; font:300 30px/1.08 var(--serif); color:var(--navy); text-wrap:balance; }
.post.sm h3{ font-size:26px; }
.post p{ margin-top:10px; font:300 14px/1.6 var(--sans); color:rgba(13,31,45,.62); max-width:46ch; }
.post .more{ margin-top:18px; padding-top:14px; border-top:.5px solid var(--stone-50); display:flex; justify-content:space-between; align-items:center; }
.post .more .ring{ width:36px; height:36px; font-size:14px; }
.post .pin-lbl{ left:20px; top:20px; }
.p1{ grid-column:1 / 8; } .p2{ grid-column:8 / 13; } .p3{ grid-column:1 / 5; } .p4{ grid-column:5 / 9; } .p5{ grid-column:9 / 13; } .p6{ grid-column:1 / 6; } .p7{ grid-column:6 / 13; }
.pull{ grid-column:1 / 13; background:var(--bone); border-radius:var(--r); padding:56px 64px; display:grid; grid-template-columns:2fr 7fr 3fr; column-gap:24px; align-items:center; }
.pull blockquote{ font:italic 400 clamp(24px,2.4vw,34px)/1.3 var(--serif); color:var(--navy); text-wrap:balance; }
.pull .who{ display:flex; flex-direction:column; gap:4px; justify-self:end; text-align:right; }
.pull .who b{ font:300 28px/1 var(--serif); }
.pull .who span{ font:300 12.5px/1.5 var(--sans); color:rgba(13,31,45,.64); }
.pager{ margin-top:72px; padding-top:28px; border-top:.5px solid var(--stone); display:flex; justify-content:space-between; align-items:center; gap:16px; }
.pager .pages{ display:flex; gap:8px; }
.car-btn{ height:44px; padding:0 22px; border-radius:999px; border:.5px solid var(--navy); font:500 11px/1 var(--sans); letter-spacing:.16em; text-transform:uppercase; color:var(--navy); transition:background-color 220ms ease,color 220ms ease; display:inline-flex; align-items:center; }
.car-btn:hover, .car-btn.on{ background:var(--navy); color:var(--bone); }
.car-btn.n{ width:44px; padding:0; justify-content:center; }
.jindex{ padding-bottom:128px; }
@media (max-width:899px){
  .jhero{ padding-block:48px 32px; } .jhero .t h1{ font-size:46px; } .jhero .r{ margin-top:24px; }
  .featured.photo-card{ margin-top:36px; aspect-ratio:4 / 5; } .featured .fx{ grid-template-columns:1fr; padding:24px; } .featured .fx h2{ font-size:30px; } .featured .fx .go{ justify-self:start; margin-top:18px; } .featured .pin-lbl{ left:20px; top:20px; }
  .filters{ margin-top:48px; } .posts{ grid-template-columns:1fr; gap:44px; margin-top:36px; } .posts > *{ grid-column:1 / -1 !important; }
  .post .photo-card, .post.tall .photo-card, .post.wide .photo-card{ aspect-ratio:4 / 3; } .post h3, .post.sm h3{ font-size:26px; }
  .pull{ grid-template-columns:1fr; padding:36px 24px; row-gap:24px; } .pull .who{ justify-self:start; text-align:left; }
  .pager{ margin-top:48px; flex-wrap:wrap; } .jindex{ padding-bottom:88px; }
}

/* ---------- the note ---------- */
.note-head{ padding-block:72px 40px; }
.note-head .t{ grid-column:1 / 10; display:flex; flex-direction:column; gap:22px; align-items:flex-start; }
.note-head h1{ font-size:clamp(40px,5.4vw,76px); line-height:1; }
.note-head .dek{ font:300 18px/1.6 var(--sans); color:rgba(13,31,45,.62); max-width:52ch; }
.byline{ display:flex; align-items:center; gap:16px; padding-top:20px; border-top:.5px solid var(--stone); width:100%; max-width:520px; }
.byline .ring{ background:var(--navy); border-color:var(--navy); color:var(--bone); font-size:20px; letter-spacing:.1em; }
.byline b{ display:block; font:400 18px/1.2 var(--serif); } .byline span{ display:block; font:300 12.5px/1.5 var(--sans); color:rgba(13,31,45,.62); }
.note-hero .photo-card{ aspect-ratio:16 / 7.5; }
.note-hero .pin-lbl{ left:32px; bottom:28px; }
.note-hero .cap{ margin-top:12px; }
.note-body{ padding-block:72px 96px; }
.rail{ grid-column:1 / 4; position:sticky; top:calc(var(--bar) + 32px); align-self:start; display:flex; flex-direction:column; gap:28px; }
.rail .eyebrow{ margin-bottom:10px; }
.toc{ border-top:.5px solid var(--stone); }
.toc a{ display:grid; grid-template-columns:32px 1fr; gap:10px; padding-block:12px; border-bottom:.5px solid var(--stone-50); font:300 14px/1.4 var(--sans); color:rgba(13,31,45,.62); text-decoration:none; transition:color 220ms ease; }
.toc a i{ font:300 14px/1.4 var(--serif); font-style:normal; color:var(--navy); font-variant-numeric:lining-nums; }
.toc a:hover, .toc a.on{ color:var(--navy); }
.share{ display:flex; flex-direction:column; gap:10px; }
.share .link{ align-self:flex-start; font-size:14px; }
.article{ grid-column:5 / 12; display:flex; flex-direction:column; gap:28px; }
.article p{ font:300 17px/1.75 var(--sans); color:rgba(13,31,45,.8); max-width:62ch; text-wrap:pretty; }
.article p.lede{ font-size:20px; color:var(--navy); }
.article h2{ font:300 36px/1.08 var(--serif); color:var(--navy); margin-top:24px; text-wrap:balance; scroll-margin-top:calc(var(--bar) + 24px); }
.article .pq{ margin-block:16px; padding-block:28px; border-top:.5px solid var(--stone); border-bottom:.5px solid var(--stone); font:italic 400 clamp(24px,2.2vw,30px)/1.35 var(--serif); color:var(--navy); text-wrap:balance; }
.article figure{ margin-block:12px; } .article figure .photo-card{ aspect-ratio:16 / 9; } .article figcaption{ margin-top:12px; }
.article .photo-card .pin-lbl{ left:20px; bottom:20px; }
.article ol.serif{ border-top:.5px solid var(--stone); }
.article ol.serif li{ display:grid; grid-template-columns:48px 1fr; gap:16px; padding-block:16px; border-bottom:.5px solid var(--stone-50); font:300 16px/1.65 var(--sans); color:rgba(13,31,45,.8); }
.article ol.serif li i{ font:300 28px/1 var(--serif); font-style:normal; color:var(--navy); font-variant-numeric:lining-nums tabular-nums; }
.aside{ background:var(--bone); border-radius:var(--r); padding:32px; display:flex; flex-direction:column; gap:14px; }
.aside h3{ font:300 26px/1.1 var(--serif); color:var(--navy); }
.aside dl{ border-top:.5px solid var(--stone); }
.aside dl div{ display:flex; justify-content:space-between; gap:16px; padding-block:10px; border-bottom:.5px solid var(--stone-50); font:300 13px/1.5 var(--sans); color:rgba(13,31,45,.64); }
.aside dd{ font:400 16px/1.4 var(--serif); color:var(--navy); text-align:right; }
.route-tile{ position:relative; overflow:hidden; background:var(--navy); color:var(--bone); border-radius:var(--r); padding:32px; min-height:300px; display:flex; flex-direction:column; justify-content:space-between; }
.route-tile h3{ font:300 30px/1.05 var(--serif); max-width:12em; position:relative; z-index:3; }
.route-tile .stops{ position:relative; z-index:3; display:flex; gap:32px; flex-wrap:wrap; }
.route-tile .stops div{ display:flex; flex-direction:column; gap:2px; font:500 9.5px/1.5 var(--sans); letter-spacing:.18em; text-transform:uppercase; color:var(--stone); }
.route-tile .stops b{ font:300 24px/1 var(--serif); letter-spacing:0; text-transform:none; color:var(--bone); font-variant-numeric:lining-nums; }
.tags{ margin-top:12px; display:flex; flex-wrap:wrap; gap:8px; align-items:center; }
.tags .eyebrow{ margin-right:8px; }
.author{ margin-top:28px; padding-top:28px; border-top:.5px solid var(--stone); display:grid; grid-template-columns:56px 1fr; gap:20px; align-items:start; }
.author .ring{ background:var(--navy); border-color:var(--navy); color:var(--bone); font-size:22px; letter-spacing:.1em; }
.author b{ display:block; font:400 20px/1.2 var(--serif); } .author p{ font-size:14px; margin-top:6px; }
.more-notes{ padding-block:0 128px; }
.more-notes .posts{ margin-top:40px; }
.more-notes .row-head{ display:flex; justify-content:space-between; align-items:flex-end; gap:24px; flex-wrap:wrap; }
@media (max-width:899px){
  .note-head{ padding-block:40px 28px; } .note-head h1{ font-size:40px; } .note-head .dek{ font-size:16px; }
  .note-hero .photo-card{ aspect-ratio:4 / 4.4; } .note-hero .pin-lbl{ left:20px; bottom:20px; }
  .note-body{ padding-block:40px 64px; } .note-body .grid{ row-gap:40px; } .rail{ position:static; }
  .article p{ font-size:16px; } .article p.lede{ font-size:18px; } .article h2{ font-size:30px; } .aside, .route-tile{ padding:24px; }
  .more-notes{ padding-bottom:88px; }
}
</style>
"""

PINS = {
 'cathedral': ('media/hero-cathedral.jpg', '50% 62%'), 'street': ('media/hero-street.jpg', '50% 55%'), 'rooftops': ('media/hero-rooftops.jpg', '50% 40%'),
 'lane': ('media/lane-vertical.jpg', '50% 40%'), 'walk': ('media/strip-walk.jpg', '50% 50%'), 'lobby': ('media/lobby.jpg', '40% 50%'),
 'dinner': ('media/strip-dinner.jpg', '60% 50%'), 'home': ('media/strip-home.jpg', '45% 50%'), 'day': ('media/eixample-day.jpg', '50% 60%'),
 'neon': ('media/neon-street.jpg', '50% 50%'), 'coast': ('media/coast.jpg', '50% 55%'), 'taxi': ('media/taxi-night.jpg', '72% 50%'),
 'market': ('media/born-market.jpg', '50% 50%'), 'next': ('media/strip-next.jpg', '50% 50%'),
}
def ph(key):
    s, p = PINS[key]; return f'<div class="ph" data-src="{s}" data-pos="{p}"></div>'

def card(cls, key, cat, date, mins, title, dek, pin=None):
    pinhtml = f'<span class="pin-lbl"><b>{pin[0]}</b>{pin[1]}</span>' if pin else ''
    return f'''      <article class="post {cls} fade-in">
        <a class="photo-card" href="post.html" aria-label="{title}">{ph(key)}{pinhtml}</a>
        <div class="meta"><span class="eyebrow">{cat} · {date}</span><span class="eyebrow">{mins} min</span></div>
        <h3>{title}</h3>
        <p>{dek}</p>
        <div class="more"><a class="link" href="post.html">Read the note</a><span class="ring" aria-hidden="true">→</span></div>
      </article>
'''

INDEX_MAIN = f'''
<main>
<section class="jhero" id="statement" aria-labelledby="j-h">
  <div class="wrap grid">
    <div class="t fade-in">
      <p class="eyebrow"><span class="ix">00</span>Journal · Barcelona · <span data-bcn-time>21:40</span></p>
      <h1 class="display" id="j-h">Notes from <em>the evening.</em></h1>
      <p class="body">Short notes on the city after dark, from the people who walk it: which streets, which tables, which hour. <span class="price-note" style="color:var(--blue-mid)">Placeholder copy until Ana writes the first notes.</span></p>
    </div>
    <div class="r fade-in">
      <p class="eyebrow">In the journal</p>
      <div class="nums"><div><b>12</b><span>notes so far</span></div><div><b>5</b><span>neighbourhoods</span></div><div><b>1</b><span>evening at a time</span></div></div>
    </div>
  </div>
</section>

<section class="jindex" aria-label="Notes">
  <div class="wrap">
    <a class="photo-card featured fade-in" href="post.html" aria-label="Featured note">
      {ph('cathedral')}
      <svg class="route" viewBox="0 0 1200 600" preserveAspectRatio="none" aria-hidden="true"><path d="M -20 420 C 200 300, 380 480, 560 360 S 820 140, 980 260 S 1140 420, 1240 330"/><circle class="pin" cx="560" cy="360" r="8"/><circle class="pin-dot" cx="560" cy="360" r="2.5"/><circle class="pin" cx="980" cy="260" r="8"/><circle class="pin-dot" cx="980" cy="260" r="2.5"/></svg>
      <span class="pin-lbl"><b>22:15</b>El Born</span>
      <div class="fx">
        <div><p class="eyebrow">Featured · Neighbourhoods · 6 min</p><h2>El Born after midnight: where the evening actually goes.</h2><p>Placeholder. The dinner that runs long, the place after, and the two streets your Kóda takes instead of the obvious one.</p></div>
        <span class="go"><span class="eyebrow" style="color:var(--bone)">Read the note</span><span class="ring" aria-hidden="true">→</span></span>
      </div>
    </a>

    <div class="filters fade-in">
      <div class="ix-row"><span>01</span><span class="ln"></span><span class="rest"><span>02</span><span>03</span></span></div>
      <div class="chips" role="group" aria-label="Filter notes"><button class="chip on">All</button><button class="chip">Neighbourhoods</button><button class="chip">Nights out</button><button class="chip">Families</button><button class="chip">Practical</button><button class="chip">From the founder</button></div>
    </div>

    <div class="posts">
{card('p1 wide', 'lane', 'Nights out', 'March 2026', 5, 'The walk home is part of the evening.', 'Placeholder. Why the last forty minutes decide how the whole night is remembered, and what a Kóda does in them.', ('00:40', 'Carrer del Bisbe'))}
{card('p2 tall', 'lobby', 'Practical', 'March 2026', 3, 'What to tell us before we meet you.', 'Placeholder. The three details that make the first ten minutes effortless.', ('20:30', 'Hotel lobby'))}
      <div class="pull fade-in">
        <p class="eyebrow">From the founder</p>
        <blockquote>"That person who spends the whole night quietly counting heads deserves the dinner too."</blockquote>
        <div class="who"><b>Ana</b><span>[Surname] · Founder, Kóda</span></div>
      </div>
{card('p3 sm', 'day', 'Families', 'February 2026', 4, 'A Saturday in Barcelona with children, and no map.', 'Placeholder. Markets, a long lunch, and the afternoon that ends before anyone gets tired.')}
{card('p4 sm', 'dinner', 'Neighbourhoods', 'February 2026', 6, 'Where the table is worth the wait.', 'Placeholder. A note on the restaurants that still take the late reservation.')}
{card('p5 sm', 'taxi', 'Practical', 'January 2026', 3, 'Taxis at two in the morning, counted in.', 'Placeholder. How the ride home is arranged and why nobody waits on the kerb.', ('02:10', 'Passeig de Gràcia'))}
{card('p6 tall', 'coast', 'Nights out', 'January 2026', 7, 'Kóda Weekend: three windows, one person.', 'Placeholder. Friday night to Saturday night with the same Kóda, told as one weekend.')}
{card('p7 wide', 'neon', 'Neighbourhoods', 'December 2025', 5, 'Gràcia on a Thursday, which is its best night.', 'Placeholder. The plaças, the small bars, and the walk back down to the Eixample.', ('23:10', 'Gràcia'))}
    </div>

    <div class="pager fade-in">
      <button class="car-btn">Previous</button>
      <div class="pages"><button class="car-btn n on">01</button><button class="car-btn n">02</button><button class="car-btn n">03</button></div>
      <button class="car-btn">Next</button>
    </div>
  </div>
</section>
'''

POST_MAIN = f'''
<main>
<article>
<header class="note-head" id="statement">
  <div class="wrap grid">
    <div class="t fade-in">
      <p class="eyebrow"><a class="link" href="blog.html" style="text-decoration:none;font:inherit;letter-spacing:inherit;color:var(--blue-mid)">Journal</a> &nbsp;·&nbsp; Neighbourhoods · 12 March 2026 · 6 min read</p>
      <h1 class="display">El Born after midnight: <em>where the evening actually goes.</em></h1>
      <p class="dek">Placeholder copy. The dinner that runs long, the place after, and the two streets your Kóda takes instead of the obvious one. Written to show the layout; Ana's words replace it.</p>
      <div class="byline"><span class="ring">A</span><div><b>Ana [Surname]</b><span>Founder, Kóda · Barcelona</span></div></div>
    </div>
  </div>
</header>

<div class="wrap note-hero fade-in">
  <div class="photo-card">{ph('dinner')}<span class="pin-lbl"><b>22:15</b>Passeig del Born</span></div>
  <p class="cap">Dinner runs long. They've already spoken to the next place. · Placeholder caption</p>
</div>

<section class="note-body">
  <div class="wrap grid">
    <aside class="rail fade-in">
      <div><p class="eyebrow">In this note</p>
        <nav class="toc"><a href="#s1" class="on"><i>01</i>Where the night starts</a><a href="#s2"><i>02</i>The place after</a><a href="#s3"><i>03</i>Two streets, not one</a><a href="#s4"><i>04</i>Everyone home</a></nav></div>
      <div class="share"><p class="eyebrow">Share</p><a class="link" href="#">WhatsApp</a><a class="link" href="#">Copy link</a></div>
      <button class="btn btn-ghost" data-book data-kind="night">Plan your night</button>
    </aside>

    <div class="article fade-in">
      <p class="lede">Placeholder paragraph. El Born works differently after eleven. The restaurants that were full at nine have a second sitting that nobody books, the bars on Passeig del Born fill from the far end, and the street that looks closed is the one that is open.</p>
      <h2 id="s1">Where the night starts</h2>
      <p>Placeholder paragraph. The table under your name is the small thing that changes everything. It means nobody stands at the door reading a menu, nobody negotiates, and the evening begins the moment you sit down. Your Kóda will have confirmed it that afternoon and will have spoken to the floor about the time you might leave.</p>
      <p>Placeholder paragraph. This is the part of the night that looks like nothing is happening. That is the point.</p>
      <blockquote class="pq">"Dinner runs long. They've already spoken to the next place."</blockquote>
      <h2 id="s2">The place after</h2>
      <p>Placeholder paragraph. There are three kinds of second place in El Born, and your group only ever wants one of them. The right one depends on how loud the dinner was, who is tired, and whether anyone has a flight. A Kóda reads this at the table and makes one call.</p>
      <figure><div class="photo-card">{ph('neon')}<span class="pin-lbl"><b>23:40</b>Carrer de l'Argenteria</span></div><figcaption class="cap">The lit street and the quiet one beside it. · Placeholder caption</figcaption></figure>
      <h2 id="s3">Two streets, not one</h2>
      <p>Placeholder paragraph. The obvious route from the Born to the Gòtic is the one everyone takes. The better one is two streets over, lit end to end, and it brings you out by the cathedral with the square empty.</p>
      <ol class="serif">
        <li><i>01</i>Placeholder. Leave by the side door, not the front; the pavement is wider and the taxis queue there.</li>
        <li><i>02</i>Placeholder. Carrer de la Princesa to Via Laietana is quicker than it looks on the map at this hour.</li>
        <li><i>03</i>Placeholder. The last stretch to the hotel is where people drift. Your Kóda walks at the back.</li>
      </ol>
      <div class="aside">
        <h3>What a Kóda does here</h3>
        <dl><div><dt>At the table</dt><dd>Confirms the next place</dd></div><div><dt>On the street</dt><dd>Takes the lit route</dd></div><div><dt>At the kerb</dt><dd>Counts everyone into the taxi</dd></div></dl>
        <p class="cap">Placeholder rows. Every note ends with the practical version.</p>
      </div>
      <h2 id="s4">Everyone home</h2>
      <p>Placeholder paragraph. A taxi, an address confirmed, everyone counted in. The evening simply ended well, and nobody had to be the one who made sure of it.</p>
      <div class="route-tile">
        <svg class="route" viewBox="0 0 700 300" preserveAspectRatio="none" aria-hidden="true"><path d="M -10 220 C 120 140, 220 260, 340 180 S 520 60, 720 140"/><circle class="pin" cx="340" cy="180" r="7"/><circle class="pin-dot" cx="340" cy="180" r="2"/></svg>
        <h3>The route this note walks.</h3>
        <div class="stops"><div><b>20:30</b>Hotel lobby</div><div><b>22:15</b>Dinner, El Born</div><div><b>00:40</b>Carrer del Bisbe</div><div><b>02:30</b>Everyone home</div></div>
      </div>
      <div class="tags"><span class="eyebrow">Tags</span><span class="chip">El Born</span><span class="chip">Nights out</span><span class="chip">Kóda Night</span></div>
      <div class="author"><span class="ring">A</span><div><b>Ana [Surname]</b><p class="body">Founder of Kóda. Placeholder bio: started Kóda after too many evenings where one person in the group spent the whole night quietly counting heads.</p></div></div>
    </div>
  </div>
</section>

<section class="more-notes" aria-label="More notes">
  <div class="wrap">
    <div class="row-head fade-in"><div><p class="eyebrow"><span class="ix">02</span>More notes</p><h2 class="display h-mid">Next <em>evening.</em></h2></div><a class="link" href="blog.html">All notes</a></div>
    <div class="posts">
{card('p1 wide', 'lane', 'Nights out', 'March 2026', 5, 'The walk home is part of the evening.', 'Placeholder. Why the last forty minutes decide how the whole night is remembered.', ('00:40', 'Carrer del Bisbe'))}
{card('p2 tall', 'lobby', 'Practical', 'March 2026', 3, 'What to tell us before we meet you.', 'Placeholder. The three details that make the first ten minutes effortless.', ('20:30', 'Hotel lobby'))}
    </div>
  </div>
</section>
</article>
'''

def page(title, main):
    return ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
            f'<title>{title}</title>\n{head_links}\n{style}\n{BLOG_CSS}'
            '<style>:root{color-scheme:light}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style></head><body>\n'
            f'{header}\n{main}\n{close_footer}\n</main>\n\n{chrome}\n\n{scripts}\n</body></html>\n')

(SITE / "blog.html").write_text(page("Kóda Journal", INDEX_MAIN))
(SITE / "post.html").write_text(page("Kóda Journal · El Born after midnight", POST_MAIN))
print("wrote blog.html and post.html")
