// Interakce a pohyb webu (inspirace crox): menu, odkrývání při scrollu,
// parallaxa, připnuté sekce, vodorovný scroll, ticker se setrvačností,
// drátěný 3D objekt, počítadla a šipky >>><<<.
const root = document.documentElement;
root.classList.remove('no-js');
const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
const desktop = () => innerWidth > 860;
// telefony a tablety: méně efektů navázaných na scroll, mapa jen 30 snímků/s
const lite = matchMedia('(max-width: 860px), (pointer: coarse)').matches;
const clamp = (v, a, b) => Math.min(b, Math.max(a, v));

let scrolling = false, scrollTimer = 0;
addEventListener('scroll', () => {
  scrolling = true;
  clearTimeout(scrollTimer);
  scrollTimer = setTimeout(() => (scrolling = false), 140);
}, { passive: true });

// ---------- načtení: rozjetí nadpisů ----------
const loaded = () => requestAnimationFrame(() => root.classList.add('is-loaded'));
if (document.fonts && document.fonts.ready) {
  Promise.race([document.fonts.ready, new Promise((r) => setTimeout(r, 500))]).then(loaded);
} else loaded();

// ---------- mobilní menu ----------
const burger = document.querySelector('.burger');
const nav = document.getElementById('nav');
if (burger && nav) {
  burger.addEventListener('click', () => {
    const open = burger.getAttribute('aria-expanded') === 'true';
    // menu začíná přesně pod hlavičkou (nad ní může být ještě horní proužek)
    nav.style.setProperty('--nav-top', Math.round(document.querySelector('.header').getBoundingClientRect().bottom) + 'px');
    burger.setAttribute('aria-expanded', String(!open));
    nav.classList.toggle('open', !open);
  });
  nav.querySelectorAll('a').forEach((a) =>
    a.addEventListener('click', () => {
      burger.setAttribute('aria-expanded', 'false');
      nav.classList.remove('open');
    })
  );
}

// ---------- menu Služby: na počítači vodorovný pás od tlačítka k pravému okraji, na mobilu rozbalovací seznam ----------
document.querySelectorAll('.has-dd').forEach((dd) => {
  const btn = dd.querySelector('.dd-btn');
  const panel = dd.querySelector('.dd');
  const wide = () => innerWidth > 1180;
  let timer = 0;
  const place = () => panel.style.setProperty('--dd-left', Math.round(dd.getBoundingClientRect().left) + 'px');
  const set = (open) => {
    clearTimeout(timer);
    if (open && wide()) place();
    dd.classList.toggle('open', open);
    btn.setAttribute('aria-expanded', String(open));
  };
  btn.addEventListener('click', () => set(!dd.classList.contains('open')));
  dd.addEventListener('pointerenter', (e) => { if (e.pointerType === 'mouse' && wide()) set(true); });
  dd.addEventListener('pointerleave', (e) => { if (e.pointerType === 'mouse' && wide()) timer = setTimeout(() => set(false), 220); });
  dd.querySelector('.dd-link').addEventListener('focus', () => { if (wide()) set(true); });
  dd.addEventListener('focusout', (e) => { if (wide() && !dd.contains(e.relatedTarget)) set(false); });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && dd.classList.contains('open')) { set(false); btn.focus(); } });
  document.addEventListener('click', (e) => { if (wide() && !dd.contains(e.target)) set(false); });
  let wasWide = wide();
  addEventListener('resize', () => {
    // při přepnutí mezi počítačem a mobilem menu zavřít, ať nezůstane v nesprávné podobě
    if (wide() !== wasWide) { wasWide = wide(); set(false); }
    else if (dd.classList.contains('open') && wide()) place();
  }, { passive: true });
});

// ---------- příprava: pořadí prvků ve skupinách, kreslení ikon ----------
document.querySelectorAll('[data-stagger]').forEach((g) =>
  [...g.children].forEach((c, i) => c.style.setProperty('--i', i))
);
document.querySelectorAll('.ico svg').forEach((svg) =>
  svg.querySelectorAll('path, circle, rect, ellipse, line, polyline').forEach((el) => el.setAttribute('pathLength', '1'))
);

// ---------- počítadla ----------
function countUp(el) {
  const end = +el.dataset.count;
  if (reduced) return;
  const t0 = performance.now();
  const dur = 1400;
  const tick = (t) => {
    const k = clamp((t - t0) / dur, 0, 1);
    el.textContent = Math.round(end * (1 - Math.pow(1 - k, 3)));
    if (k < 1) requestAnimationFrame(tick);
  };
  el.textContent = '0';
  requestAnimationFrame(tick);
}

// ---------- odkrývání při scrollu ----------
const targets = document.querySelectorAll('.reveal, [data-stagger], .ico');
if ('IntersectionObserver' in window && !reduced) {
  const io = new IntersectionObserver(
    (entries) =>
      entries.forEach((e) => {
        if (!e.isIntersecting) return;
        e.target.classList.add('in');
        e.target.querySelectorAll('[data-count]').forEach(countUp);
        io.unobserve(e.target);
      }),
    { rootMargin: '0px 0px -10% 0px' }
  );
  targets.forEach((el) => io.observe(el));
} else {
  targets.forEach((el) => el.classList.add('in'));
}

// ---------- šipky >>>><<<< ----------
document.querySelectorAll('[data-chev]').forEach((el) => {
  const n = 22;
  let k = 0, dir = 1;
  const draw = () => (el.textContent = '>'.repeat(k) + '<'.repeat(n - k));
  draw();
  if (reduced) return;
  let iv = 0;
  new IntersectionObserver(([e]) => {
    clearInterval(iv);
    if (e.isIntersecting) iv = setInterval(() => {
      k += dir;
      if (k >= n || k <= 0) dir *= -1;
      draw();
    }, 110);
  }).observe(el);
});

// ---------- interaktivní mapa služeb ----------
// Ikony sedí na vrcholech drátěného tělesa. Tažením myši (mimo ikonu) se těleso otáčí,
// po puštění dobíhá setrvačností a pak se zase pomalu točí samo. Klik na ikonu otevře službu.
document.querySelectorAll('[data-wire]').forEach((cv) => {
  const box = cv.parentElement;
  const ctx = cv.getContext('2d');
  const nodes = [...box.querySelectorAll('.node')];
  const V = [[0, 1.25, 0], [1, 0, 0], [0, 0, 1], [-1, 0, 0], [0, 0, -1], [0, -1.25, 0]];
  const E = [[0, 1], [0, 2], [0, 3], [0, 4], [5, 1], [5, 2], [5, 3], [5, 4], [1, 2], [2, 3], [3, 4], [4, 1]];
  let w = 0, h = 0, visible = true;
  let ry = 0.6, rx = 0.42, vy = 0.004, vx = 0, hot = -1;
  let drag = null, idleAt = 0;

  const size = () => {
    const r = cv.getBoundingClientRect();
    const d = Math.min(devicePixelRatio || 1, lite ? 1.5 : 2);
    if (Math.abs(r.width - w) < 1 && Math.abs(r.height - h) < 1) return false;
    w = r.width; h = r.height;
    cv.width = w * d; cv.height = h * d;
    ctx.setTransform(d, 0, 0, d, 0, 0);
  };
  const rot = (p, ry, rx) => {
    let [x, y, z] = p;
    [x, z] = [x * Math.cos(ry) - z * Math.sin(ry), x * Math.sin(ry) + z * Math.cos(ry)];
    [y, z] = [y * Math.cos(rx) - z * Math.sin(rx), y * Math.sin(rx) + z * Math.cos(rx)];
    return [x, y, z];
  };
  // s = [vodorovné, svislé] měřítko – těleso je roztažené do šířky
  const proj = (p, s, ry, rx) => {
    const [x, y, z] = rot(p, ry, rx);
    const f = 3.2 / (3.2 + z);
    return [w / 2 + x * s[0] * f, h / 2 + 6 - y * s[1] * f, z];
  };

  const frame = () => {
    ctx.clearRect(0, 0, w, h);
    const sy = h * 0.22;
    const sx = Math.min(w * (w < 600 ? 0.28 : 0.34), sy * 2.8);
    const A = V.map((p) => proj(p, [sx, sy], ry, rx));
    const B = V.map((p) => proj(p, [sx * 0.55, sy * 0.55], -1.4 * ry, rx));
    const lines = (P, col, dash, edges = E) => {
      ctx.strokeStyle = col; ctx.setLineDash(dash); ctx.beginPath();
      edges.forEach(([i, j]) => { ctx.moveTo(P[i][0], P[i][1]); ctx.lineTo(P[j][0], P[j][1]); });
      ctx.stroke();
    };
    ctx.lineWidth = 1.3;
    lines(A, 'rgba(255,255,255,.75)', [6, 5]);
    lines(B, 'rgba(255,180,0,.9)', [2, 5]);
    ctx.strokeStyle = 'rgba(255,255,255,.2)'; ctx.setLineDash([1, 4]); ctx.beginPath();
    A.forEach((p, i) => { ctx.moveTo(p[0], p[1]); ctx.lineTo(B[i][0], B[i][1]); });
    ctx.stroke();
    if (hot > -1) { ctx.lineWidth = 2; lines(A, '#ffb400', [], E.filter((e) => e.includes(hot))); }
    nodes.forEach((n) => {
      const [x, y, z] = A[+n.dataset.v];
      const k = 1 - z * 0.2;
      n.style.transform = `translate3d(${x}px, ${y}px, 0) scale(${k.toFixed(3)})`;
      n.style.opacity = (0.5 + 0.5 * (1 - (z + 1.25) / 2.5)).toFixed(2);
      const zi = z < 0 ? '3' : '2';
      if (n.style.zIndex !== zi) n.style.zIndex = zi;
    });
  };

  // zvýraznění při najetí na ikonu
  nodes.forEach((n) => {
    n.addEventListener('pointerenter', () => { hot = +n.dataset.v; n.classList.add('on'); frame(); });
    n.addEventListener('pointerleave', () => { hot = -1; n.classList.remove('on'); frame(); });
    n.addEventListener('focus', () => { hot = +n.dataset.v; frame(); });
    n.addEventListener('blur', () => { hot = -1; frame(); });
    n.addEventListener('dragstart', (e) => e.preventDefault());
  });

  // otáčení tažením myši / prstu (mimo ikony)
  box.addEventListener('pointerdown', (e) => {
    if (e.target.closest('.node') || e.button > 0) return;
    drag = { x: e.clientX, y: e.clientY, t: performance.now(), id: e.pointerId, type: e.pointerType };
    vy = 0; vx = 0;
    box.classList.add('dragging');
    box.setPointerCapture(e.pointerId);
  });
  box.addEventListener('pointermove', (e) => {
    if (!drag || e.pointerId !== drag.id) return;
    const dx = e.clientX - drag.x, dy = e.clientY - drag.y;
    const now = performance.now(), dt = Math.max(1, now - drag.t);
    ry += dx * 0.008;
    // na dotyku jen vodorovně, aby šlo stránku dál scrollovat
    if (drag.type === 'mouse') rx = clamp(rx + dy * 0.006, -1.2, 1.2);
    vy = (dx * 0.008) / dt * 16;
    vx = drag.type === 'mouse' ? (dy * 0.006) / dt * 16 : 0;
    drag.x = e.clientX; drag.y = e.clientY; drag.t = now;
    frame();
  });
  const end = (e) => {
    if (!drag || e.pointerId !== drag.id) return;
    drag = null; idleAt = performance.now();
    box.classList.remove('dragging');
  };
  box.addEventListener('pointerup', end);
  box.addEventListener('pointercancel', end);

  let raf = 0, odd = false, started = false;
  const loop = () => {
    raf = 0;
    if (!visible) return;
    // na telefonu kreslit jen každý druhý snímek a během scrollování vůbec – scroll pak neseká
    odd = !odd;
    if (lite && (odd || scrolling)) { raf = requestAnimationFrame(loop); return; }
    if (!drag) {
      ry += vy; rx = clamp(rx + vx, -1.2, 1.2);
      vx *= 0.94;
      // setrvačnost doběhne k pomalé samostatné rotaci a sklon se vrátí
      const auto = performance.now() - idleAt > 1800 ? 0.004 : 0;
      vy += ((auto || vy * 0.94) - vy) * (auto ? 0.02 : 1);
      if (auto) rx += (0.42 - rx) * 0.01;
      frame();
    }
    raf = requestAnimationFrame(loop);
  };
  size(); frame();
  addEventListener('resize', () => { if (size() !== false) frame(); }, { passive: true });
  const kick = () => { if (started && visible && !raf && !reduced) raf = requestAnimationFrame(loop); };
  new IntersectionObserver(([e]) => { visible = e.isIntersecting; kick(); }).observe(cv);
  // otáčení spustit až po načtení stránky, ať nebrzdí úvodní animace
  const start = () => setTimeout(() => { started = true; kick(); }, 600);
  document.readyState === 'complete' ? start() : addEventListener('load', start, { once: true });
});

// ---------- vodorovný scroll: výška sekce podle délky pásu ----------
const hsList = [...document.querySelectorAll('.hs')];
function sizeHs() {
  hsList.forEach((hs) => {
    const track = hs.querySelector('.hs-track');
    if (!desktop() || reduced) { hs.style.height = ''; track.style.transform = ''; return; }
    const over = Math.max(0, track.scrollWidth - innerWidth);
    hs.dataset.over = over;
    hs.style.height = innerHeight + over + 'px';
  });
}
sizeHs();
let lastW = innerWidth;
addEventListener('resize', () => { if (desktop() || innerWidth !== lastW) { lastW = innerWidth; sizeHs(); } }, { passive: true });

// ---------- smyčka řízená scrollem ----------
const speedEls = [...document.querySelectorAll('[data-speed]')];
const stripes = [...document.querySelectorAll('.stripes')];
const zooms = [...document.querySelectorAll('[data-zoom]')];
const pins = [...document.querySelectorAll('.pin')].map((el) => ({
  el,
  steps: [...el.querySelectorAll('.pin-step')],
  nav: [...el.querySelectorAll('.pin-nav li')],
  card: el.querySelector('.pin-card'),
  bar: el.querySelector('.pin-bar'),
  cur: -1,
}));
const ticker = document.querySelector('.ticker-track');
const tickerAnim = ticker && ticker.getAnimations ? ticker.getAnimations()[0] : null;
let lastY = scrollY, boost = 0, ticking = false;

function progress(el) {
  const r = el.getBoundingClientRect();
  return clamp(-r.top / Math.max(1, r.height - innerHeight), 0, 1);
}

function update() {
  ticking = false;
  const y = scrollY;
  boost = Math.min(6, boost + Math.abs(y - lastY) * 0.04);
  lastY = y;

  if (!reduced && !lite) {
    speedEls.forEach((el) => {
      if (y < innerHeight * 1.5) el.style.transform = `translate3d(0, ${y * +el.dataset.speed}px, 0)`;
    });
    stripes.forEach((el) => (el.style.backgroundPositionX = `${-y * 0.25}px`));
    zooms.forEach((img) => {
      const r = img.closest(".stage").getBoundingClientRect();
      const k = clamp(1 - (r.top + r.height * 0.15) / innerHeight, 0, 1);
      img.style.transform = `scale(${1.22 - 0.22 * k})`;
    });
  }

  pins.forEach((p) => {
    if (!desktop()) return;
    const k = progress(p.el);
    p.bar && p.bar.style.setProperty('--p', k);
    const i = Math.min(p.steps.length - 1, Math.floor(k * p.steps.length * 0.999));
    if (i !== p.cur) {
      p.steps.forEach((s, j) => { s.classList.toggle('on', j === i); s.classList.toggle('past', j < i); });
      p.nav.forEach((n, j) => n.classList.toggle('on', j === i));
      if (p.cur !== -1 && !reduced) { p.card.classList.remove('morph'); void p.card.offsetWidth; p.card.classList.add('morph'); }
      p.cur = i;
    }
  });

  hsList.forEach((hs) => {
    if (!desktop() || reduced) return;
    const k = progress(hs);
    hs.querySelector('.hs-track').style.transform = `translate3d(${-k * +hs.dataset.over}px, 0, 0)`;
    const bar = hs.querySelector('.hs-bar');
    bar && bar.style.setProperty('--p', k);
  });
}
addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });
addEventListener('resize', update, { passive: true });
update();

// ticker zrychlí při scrollu a pak se uklidní
if (tickerAnim && !reduced && !lite) {
  let calming = false;
  const calm = () => {
    boost *= 0.92;
    if (boost < 0.01) boost = 0;
    tickerAnim.playbackRate = 1 + boost;
    calming = boost > 0;
    if (calming) requestAnimationFrame(calm);
  };
  addEventListener('scroll', () => { if (!calming) { calming = true; requestAnimationFrame(calm); } }, { passive: true });
}

// mapa na kontaktu se načte z Google až po kliknutí (ochrana soukromí návštěvníků)
document.querySelectorAll('[data-map-load]').forEach((btn) =>
  btn.addEventListener('click', () => {
    const box = btn.closest('[data-map-src]');
    const f = document.createElement('iframe');
    f.title = 'Mapa – Zemědělská 1145/4a, Hradec Králové';
    f.src = box.dataset.mapSrc;
    f.referrerPolicy = 'strict-origin-when-cross-origin';
    box.replaceChildren(f);
  })
);

// ---------- karusel (na telefonu se seznam služeb posouvá do strany) ----------
document.querySelectorAll('.carousel').forEach((c) => {
  const items = [...c.children];
  const dots = document.createElement('div');
  dots.className = 'carousel-dots';
  dots.setAttribute('aria-hidden', 'true');
  items.forEach(() => dots.append(document.createElement('i')));
  c.after(dots);
  let raf = 0;
  const mark = () => {
    raf = 0;
    const step = items[1] ? items[1].offsetLeft - items[0].offsetLeft : 1;
    const i = Math.round(c.scrollLeft / step);
    [...dots.children].forEach((d, j) => d.classList.toggle('on', j === i));
  };
  c.addEventListener('scroll', () => { if (!raf) raf = requestAnimationFrame(mark); }, { passive: true });
  mark();
});

document.querySelectorAll('[data-year]').forEach((el) => (el.textContent = new Date().getFullYear()));
