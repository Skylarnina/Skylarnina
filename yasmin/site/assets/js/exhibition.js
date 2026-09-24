/* The Exhibition: prototype script.
   Only what the brief allows: the wireframe toggle and the lightbox, plus
   small conveniences that degrade to plain links without JavaScript
   (carousel links, play marks, the prototype password form).
   None of this is needed in Squarespace; see the build notes. */
(function () {
  var root = document.documentElement;

  /* 1. Wireframe mode: persists across the six pages; #wireframe forces it on */
  var KEY = 'yb-wireframe';
  function store(v) { try { localStorage.setItem(KEY, v ? '1' : '0'); } catch (e) {} }
  function stored() { try { return localStorage.getItem(KEY) === '1'; } catch (e) { return false; } }
  function setWF(on) {
    root.classList.toggle('wf', on);
    var b = document.getElementById('wf-toggle');
    if (b) b.setAttribute('aria-pressed', on ? 'true' : 'false');
  }
  setWF(location.hash === '#wireframe' || stored());
  document.addEventListener('click', function (e) {
    var b = e.target.closest('#wf-toggle');
    if (!b) return;
    var on = !root.classList.contains('wf'); setWF(on); store(on);
  });

  /* 2. Lightbox for "view full plate" links (Squarespace: image block → Lightbox) */
  var box = document.createElement('div');
  box.className = 'lightbox'; box.setAttribute('role', 'dialog'); box.setAttribute('aria-modal', 'true'); box.setAttribute('aria-label', 'Full plate');
  box.innerHTML = '<button type="button">Close &times;</button><figure><img alt=""><p></p></figure>';
  document.addEventListener('DOMContentLoaded', function () { document.body.appendChild(box); });
  var last = null;
  function close() { box.classList.remove('is-open'); if (last) last.focus(); }
  box.addEventListener('click', function (e) { if (e.target === box || e.target.tagName === 'BUTTON') close(); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && box.classList.contains('is-open')) close(); });
  document.addEventListener('click', function (e) {
    var a = e.target.closest('a.zoom');
    if (!a) return;
    e.preventDefault(); last = a;
    box.querySelector('img').src = a.getAttribute('href');
    box.querySelector('img').alt = a.dataset.caption || '';
    box.querySelector('p').textContent = a.dataset.caption || '';
    box.classList.add('is-open'); box.querySelector('button').focus();
  });

  /* 3. Carousels: links to slides scroll sideways only (no page jump), and the
        current slide is marked. Without JS they are ordinary #anchors. */
  document.addEventListener('click', function (e) {
    var a = e.target.closest('a[data-slide]');
    if (!a) return;
    var t = document.getElementById(a.getAttribute('href').slice(1));
    if (!t) return;
    e.preventDefault();
    var track = t.parentElement;
    track.scrollTo({ left: t.offsetLeft - (track.clientWidth - t.offsetWidth) / 2, behavior: 'smooth' });
  });
  function watch(track) {
    var slides = [].slice.call(track.children);
    var group = track.dataset.group;
    function mark(id) {
      slides.forEach(function (s) { s.classList.toggle('is-active', s.id === id); });
      document.querySelectorAll('a[data-slide][data-group="' + group + '"]').forEach(function (a) {
        var on = a.getAttribute('href') === '#' + id;
        a.classList.toggle('is-current', on);
        if (on) a.setAttribute('aria-current', 'true'); else a.removeAttribute('aria-current');
      });
      document.querySelectorAll('[data-prev="' + group + '"],[data-next="' + group + '"]').forEach(function (a) {
        var i = slides.findIndex(function (s) { return s.id === id; });
        var j = a.hasAttribute('data-prev') ? Math.max(0, i - 1) : Math.min(slides.length - 1, i + 1);
        a.setAttribute('href', '#' + slides[j].id);
      });
    }
    var ticking = false;
    function nearest() {
      var c = track.scrollLeft + track.clientWidth / 2, best = slides[0], d = Infinity;
      slides.forEach(function (s) { var m = Math.abs(s.offsetLeft + s.offsetWidth / 2 - c); if (m < d) { d = m; best = s; } });
      mark(best.id); ticking = false;
    }
    track.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(nearest); } }, { passive: true });
    var start = track.querySelector('[data-start]') || slides[0];
    requestAnimationFrame(function () {
      track.scrollLeft = start.offsetLeft - (track.clientWidth - start.offsetWidth) / 2;
      mark(start.id);
    });
  }
  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('[data-track]').forEach(watch);
  });

  /* 4. Round play marks on the black-box screens */
  document.addEventListener('click', function (e) {
    var p = e.target.closest('.screen__play');
    if (!p) return;
    var fig = p.closest('.screen'); var v = fig.querySelector('video');
    v.controls = true; v.play(); fig.classList.add('is-playing');
  });

  /* 5. Private view (prototype only): any password shows the wrong-password state.
        #wrong shows it on load. Squarespace checks the real password itself. */
  document.addEventListener('DOMContentLoaded', function () {
    var pv = document.querySelector('.pv');
    if (!pv) return;
    if (location.hash === '#wrong') pv.classList.add('is-wrong');
    var f = pv.querySelector('form');
    f.addEventListener('submit', function (e) {
      e.preventDefault(); pv.classList.add('is-wrong');
      var i = f.querySelector('input'); i.value = ''; i.focus();
    });
  });
})();
