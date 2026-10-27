"""Jednorázový generátor statických stránek (sdílená hlavička a patička)."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from services import S, ORDER, PATHS

OUT = pathlib.Path(sys.argv[1])
PO = "https://spravapo.cz"

ICONS = {
 "helmet": '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M8 44h48M12 44c0-12 8-22 20-22s20 10 20 22"/><path d="M26 22v-6h12v6M22 44V30M42 44V30M32 22v22"/><path d="M6 44h52v5H6z"/></svg>',
 "fire": '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.4"><rect x="22" y="18" width="20" height="40" rx="8"/><path d="M28 18v-6h8v6M36 12h10l4 6M30 34c0 4 2 6 2 6s2-2 2-6-4-6-4-6M27 44h10"/></svg>',
 "leaf": '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M12 52C12 26 28 12 54 10c0 26-14 42-38 42"/><path d="M12 52 40 24M24 40h10M30 34v-9"/></svg>',
 "doc": '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M16 6h22l12 12v40H16z"/><path d="M38 6v12h12M22 28h22M22 34h22M22 40h22M22 46h14"/></svg>',
 "class": '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.4"><rect x="6" y="8" width="40" height="28"/><path d="M12 16h20M12 22h26M12 28h14M50 26a5 5 0 1 0 0-.1M42 58V44c0-4 3-7 8-7s8 3 8 7v14M46 36l-6-6"/></svg>',
 "rope": '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M32 2v14"/><circle cx="32" cy="20" r="4"/><path d="M24 30h16l-2 16H26z M26 30l6 8 6-8M28 46l-4 14M36 46l4 14M24 34l-8 10M40 34l8 10"/></svg>',
 "food": '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M8 36h48M12 36c0 10 8 16 20 16s20-6 20-16M20 28c0-6 4-10 4-14M30 28c0-6 4-10 4-14M40 28c0-6 4-10 4-14"/></svg>',
 "shield": '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M32 4 8 12v18c0 15 10 26 24 30 14-4 24-15 24-30V12z"/><path d="M22 32l7 7 13-14"/></svg>',
 "heart": '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M32 54S6 38 6 21C6 13 12 8 19 8c6 0 10 4 13 8 3-4 7-8 13-8 7 0 13 5 13 13 0 17-26 33-26 33z"/><path d="M34 18l-8 14h10l-6 14"/></svg>',
 "person": '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.4"><circle cx="32" cy="18" r="9"/><path d="M12 58c0-12 9-20 20-20s20 8 20 20"/></svg>',
 "clock": '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.4"><circle cx="32" cy="32" r="24"/><path d="M32 16v16l10 8"/><path d="M32 4v4M32 56v4M4 32h4M56 32h4"/></svg>',
 "hand": '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M6 34l12-12 10 4 8-4 10 6 12 10-14 12-10-8-8 4-8-6z"/><path d="M28 26l-6 10 6 2 8-8"/></svg>',
 "chip": '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.4"><rect x="16" y="16" width="32" height="32"/><rect x="24" y="24" width="16" height="16"/><path d="M24 8v8M32 8v8M40 8v8M24 48v8M32 48v8M40 48v8M8 24h8M8 32h8M8 40h8M48 24h8M48 32h8M48 40h8"/></svg>',
 "eye": '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M4 32s10-16 28-16 28 16 28 16-10 16-28 16S4 32 4 32z"/><circle cx="32" cy="32" r="8"/></svg>',
 "map": '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M6 14l16-6 20 6 16-6v42l-16 6-20-6-16 6z"/><path d="M22 8v42M42 14v42"/></svg>',
 "team": '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.4"><circle cx="22" cy="22" r="7"/><circle cx="44" cy="24" r="6"/><path d="M6 52c0-9 7-16 16-16s16 7 16 16M36 38c2-1 5-2 8-2 8 0 14 6 14 14"/></svg>',
 "phone": '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M14 6h10l4 12-6 4c3 8 10 15 18 18l4-6 12 4v10c0 4-3 6-6 6C28 54 10 36 8 12c0-3 2-6 6-6z"/></svg>',
 "drop": '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M32 6S14 28 14 40a18 18 0 0 0 36 0C50 28 32 6 32 6z"/><path d="M24 42a8 8 0 0 0 8 8"/></svg>',
 "pulse": '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M2 34h14l6-14 8 28 8-22 5 8h19"/></svg>',
}
for _k, _v in PATHS.items():
    ICONS.setdefault(_k, f'<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.4">{_v}</svg>')
def ico(n): return f'<div class="ico" aria-hidden="true">{ICONS[n]}</div>'

NAV = [("mekke-cile.html", "Měkké cíle", ""), ("prvni-pomoc.html", "První pomoc &amp; AED", "aed"), ("index.html#o-nas", "O nás", "")]

AC = ' aria-current="page"'
CHEV_DOWN = '<svg class="chev-d" viewBox="0 0 12 12" width="10" height="10" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M2 4l4 4 4-4"/></svg>'

def head(title, desc, current):
    links = "".join(
        f'<a href="{h}"' + (f' class="{c}"' if c else "") + f'{AC if h == current else ""}>{t}</a>' for h, t, c in NAV)
    in_svc = current == "sluzby.html" or current[:-5] in S
    # Rozbalovací pás služeb: na počítači vodorovně od tlačítka Služby až k pravému okraji obrazovky.
    dd = "".join(
        f'<a href="{k}.html" style="--i:{i}"{AC if current == k + ".html" else ""}><span class="n">0{i+1}</span>{ICONS[S[k]["icon"]]}<b>{S[k]["name"]}</b><small>{S[k]["short"]}</small></a>'
        for i, k in enumerate(ORDER))
    return f'''<!doctype html>
<html lang="cs" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#e3e7eb">
<link rel="icon" href="assets/img/logo.png">
<link rel="preload" href="assets/fonts/geist-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/geist-latin-ext.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/fonts.css">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<div class="vframe" aria-hidden="true"></div>
<a class="skip" href="#obsah">Přeskočit na obsah</a>
<div class="topbar label">
  <div class="wrap">
    <span class="hide-sm">BOZP · PO · EMS · Měkké cíle — po celé ČR</span>
    <span>Pohotovost 24 / 7 / 365</span>
    <span><a href="tel:+420737517995">737 517 995</a><span class="hide-sm"> · <a href="mailto:asistentka@spravabozp.cz">asistentka@spravabozp.cz</a></span></span>
  </div>
</div>
<header class="header">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="Správa BOZP – úvod">
      <img src="assets/img/logo.png" alt="" width="50" height="50">
    </a>
    <button class="burger" aria-expanded="false" aria-controls="nav" aria-label="Menu"><span></span><span></span><span></span></button>
    <nav class="nav" id="nav" aria-label="Hlavní menu">
      <div class="has-dd{" current" if in_svc else ""}">
        <a class="dd-link" href="sluzby.html"{AC if current == "sluzby.html" else ""}>Služby</a>
        <button type="button" class="dd-btn" aria-expanded="false" aria-controls="dd-sluzby" aria-label="Rozbalit seznam služeb">{CHEV_DOWN}</button>
        <div class="dd" id="dd-sluzby">
          <div class="dd-row">{dd}</div>
        </div>
      </div>
      {links}
      <a class="ext" href="{PO}" target="_blank" rel="noopener">Požární bezpečnost</a>
      <a class="btn" href="kontakt.html"{AC if current == "kontakt.html" else ""}>Kontakt <span class="arr">→</span></a>
    </nav>
  </div>
</header>
<main id="obsah">
'''

FOOT = f'''</main>
<footer class="footer">
  <div class="wrap"><div class="footer-big">
    <div>
      <p class="claim">Bezpečnost je naše práce.<br>Vaše je podnikání.</p>
      <a class="btn" href="kontakt.html">Nezávazná konzultace <span class="arr">→</span></a>
    </div>
    <div>
      <h3>Sídlo &amp; doručovací adresa</h3>
      <p>Správa BOZP s.r.o.<br>Zemědělská 1145/4a<br>Slezské Předměstí<br>500 03 Hradec Králové</p>
    </div>
    <div>
      <h3>Fakturační údaje</h3>
      <p>IČ: 07414552<br>Č. ú.: 1027014087/6100<br>Datová schránka: 5hviy3m</p>
    </div>
    <div>
      <h3>Kontakt</h3>
      <ul>
        <li><a href="tel:+420737517995">tel.: 737 517 995</a></li>
        <li><a href="mailto:asistentka@spravabozp.cz">asistentka@spravabozp.cz</a></li>
        <li><a href="{PO}" target="_blank" rel="noopener">Požární bezpečnost staveb ↗</a></li>
      </ul>
    </div>
  </div></div>
  <div class="wrap"><div class="footer-word" aria-hidden="true">Správa BOZP</div></div>
  <div class="footer-bottom">
    <div class="wrap">
      <span>© <span data-year>2026</span> Správa BOZP s.r.o.</span>
      <span><a href="sluzby.html">Služby</a> · <a href="bozp.html">BOZP</a> · <a href="mekke-cile.html">Měkké cíle</a> · <a href="prvni-pomoc.html">První pomoc</a> · <a href="https://www.spravabozp.cz/prohlaseni-o-zasadach-ochrany-osobnich-udaju/">Ochrana osobních údajů</a></span>
    </div>
  </div>
</footer>
<script src="assets/main.js" defer></script>
</body>
</html>
'''

PARTNER = f'''
<section class="section--tight">
  <div class="wrap">
    <div class="partner reveal">
      <div class="l">
        <span class="label" style="color:#aeb4bb">Partnerská společnost</span>
        <h2 class="h-md mt-s">Požární bezpečnost staveb <span class="flame">↗</span></h2>
        <p>Školení požární ochrany, revize požárně bezpečnostních zařízení, EPS, protipožární ucpávky, hasicí přístroje i součinnost s HZS zajišťuje naše sesterská společnost SPBS – Správa požární bezpečnosti staveb s.r.o. Jeden partner, jedna adresa, jedna odpovědnost.</p>
        <a class="btn btn--signal" href="{PO}" target="_blank" rel="noopener">Přejít na spravapo.cz <span class="arr">→</span></a>
      </div>
      <div class="r">
        <a href="{PO}" target="_blank" rel="noopener">Školení požární ochrany <span>↗</span></a>
        <a href="{PO}" target="_blank" rel="noopener">EPS a revize PBZ <span>↗</span></a>
        <a href="{PO}" target="_blank" rel="noopener">Protipožární ucpávky <span>↗</span></a>
        <a href="{PO}" target="_blank" rel="noopener">Hasicí přístroje <span>↗</span></a>
        <a href="{PO}" target="_blank" rel="noopener">Požární dokumentace a součinnost HZS <span>↗</span></a>
      </div>
    </div>
  </div>
</section>'''

def cta(title, text, btn="Domluvit konzultaci"):
    return f'''
<section class="section section--dark">
  <div class="wrap cta reveal">
    <div>
      <span class="label label--dot">Další krok</span>
      <h2 class="h-lg mt-s">{title}</h2>
      <p class="lead mt-s">{text}</p>
    </div>
    <div class="flex-gap">
      <a class="btn btn--amber" href="kontakt.html">{btn} <span class="arr">→</span></a>
      <a class="btn btn--ghost-light" href="tel:+420737517995">737 517 995</a>
    </div>
  </div>
</section>'''

TICKER_ITEMS = ["Vyhledávání a hodnocení rizik", "Školení zaměstnanců", "Kategorizace prací", "Dokumentace BOZP", "Požární ochrana", "Životní prostředí – EMS", "Ochrana měkkých cílů", "První pomoc a AED", "HACCP", "Práce ve výškách", "Kniha úrazů online", "Pohotovost 24/7"]
TICKER = '<div class="ticker" aria-hidden="true"><div class="ticker-track">' + "".join(f"<span>{t}</span><i>/</i>" for t in TICKER_ITEMS * 2) + "</div></div>"

def page_hero(crumb, title, lead):
    return f'''
<section class="page-hero">
  <div class="wrap">
    <p class="crumbs label"><a href="index.html">Úvod</a> / {crumb}</p>
    <div class="row">
      <h1 class="lines">{"".join(f'<span class="ln"><span>{x}</span></span>' for x in title.split("<br>"))}</h1>
      <p class="lead" data-reveal="fade">{lead}</p>
    </div>
  </div>
  <div class="colgrid" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i></div>
</section>'''

def pin(label, title, lead, steps, tone="dark"):
    """Připnutá sekce: karta se mění krok po kroku při scrollu (crox 'process')."""
    nav = "".join(f'<li data-i="{i}"><span>0{i+1}</span>{t}</li>' for i, (t, _, _) in enumerate(steps))
    cards = "".join(
        f'<article class="pin-step" data-i="{i}"><div class="pin-top"><span class="dot"></span><span class="label">Krok 0{i+1} / 0{len(steps)}</span><span class="dot"></span></div>'
        f'<h3>{t}</h3><p>{d}</p><div class="pin-tags">' + "".join(f"<span>{g}</span>" for g in tags) + "</div></article>"
        for i, (t, d, tags) in enumerate(steps))
    return f'''
<section class="pin" style="--n:{len(steps)}">
  <div class="pin-sticky gridbg">
    <div class="wrap pin-grid">
      <div class="pin-head">
        <span class="label label--dot">{label}</span>
        <h2 class="h-lg mt-s">{title}</h2>
        <p class="lead mt-s">{lead}</p>
        <ol class="pin-nav">{nav}</ol>
        <div class="pin-bar"><i></i></div>
      </div>
      <div class="pin-card pin-card--{tone}">{cards}</div>
    </div>
  </div>
</section>'''

CHEV = '<div class="chev-bar" aria-hidden="true"><span class="label">{0}</span><span class="chev" data-chev></span></div>'

# Interaktivní mapa služeb: ikony sedí na vrcholech rotujícího drátěného tělesa.
MAP_NODES = [
  ("helmet", "BOZP", "Rizika, kategorizace prací, dokumentace, školení a pravidelné dohlídky. Celá agenda pod jednou střechou.", "bozp.html"),
  ("fire", "Požární ochrana", "Agenda a dokumentace PO. Školení PO, revize PBZ a hasicí přístroje zajišťuje partnerská SPBS.", "pozarni-ochrana.html"),
  ("shield", "Měkké cíle", "Bezpečnostní analýza, plány, školení a nácvik pro školy, úřady a instituce.", "mekke-cile.html"),
  ("leaf", "Životní prostředí – EMS", "Zavedení a správa EMS, evidence odpadů a chemických látek, metodika ČOV.", "zivotni-prostredi-ems.html"),
  ("class", "Školení", "BOZP, PO a EMS, práce ve výškách, vazači, jeřábníci, referenční řidiči a další.", "skoleni.html"),
  ("heart", "První pomoc & AED", "Interaktivní školení na resuscitační figuríně a s tréninkovým AED.", "prvni-pomoc.html"),
]
MAP = ('<div class="wire gridbg--dark" data-map><canvas data-wire aria-hidden="true"></canvas>'
  '<span class="wire-tag label">Mapa služeb · tažením otočíte · klikem na ikonu otevřete</span><span class="wire-tag wire-tag--r label">Rev. 2026</span>'
  + "".join(f'<a class="node" href="{h}" data-v="{i}" title="{d}">{ICONS[ic]}<span class="node-l">{t}</span></a>'
            for i, (ic, t, d, h) in enumerate(MAP_NODES))
  + '</div>')

# Růžová přilba z varianty MQ – jen balancuje na nápisu „Správa“ (žádná trajektorie).
HELMET = '''<span class="helmet" aria-hidden="true"><span class="helmet-in"><svg viewBox="0 0 120 80">
<path d="M14 66c0-27 20-48 46-48s46 21 46 48z" fill="#ff5fa8" stroke="#1a1b1c" stroke-width="4" stroke-linejoin="round"/>
<path d="M48 20h24l2 18H46z" fill="#ff8dc3" stroke="#1a1b1c" stroke-width="4" stroke-linejoin="round"/>
<path d="M30 30c-8 9-12 20-12 34" fill="none" stroke="#fff" stroke-opacity=".55" stroke-width="5" stroke-linecap="round"/>
<path d="M4 66h112c2 0 3 2 3 4v4c0 2-1 4-3 4H4c-2 0-3-2-3-4v-4c0-2 1-4 3-4z" fill="#e6448f" stroke="#1a1b1c" stroke-width="4" stroke-linejoin="round"/>
<text x="60" y="58" text-anchor="middle" font-family="Geist, Arial, sans-serif" font-weight="700" font-size="19" letter-spacing="-.3" fill="#1a1b1c">BOZP</text>
</svg></span></span>'''

# ------------------------------------------------------------------ INDEX
INDEX = f'''
<section class="hero">
  <div class="colgrid" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i></div>
  <div class="wrap hero-in">
    <div class="hero-top">
      <h1 class="h-xl lines" data-speed="0.12">{HELMET}<span class="ln"><span>Správa</span></span><span class="ln"><span><span class="amber">BOZP</span><span class="sro">s.r.o.</span></span></span></h1>
      <div class="hero-side" data-reveal="fade">
        <p class="lead">Specialisté na bezpečnost práce a požární ochranu.<span class="lead-more"> Převezmeme celou agendu – rizika, dokumentaci, školení i kontroly úřadů – a vy se můžete věnovat svému podnikání.</span></p>
        <div class="flex-gap">
          <a class="btn btn--amber" href="kontakt.html">Nezávazná konzultace <span class="arr">→</span></a>
        </div>
      </div>
    </div>
    <dl class="hero-stats" data-reveal="fade">
      <div><dt>Pohotovost</dt><dd class="live">24/7/365</dd></div>
      <div><dt>Technici na klienta</dt><dd>2</dd></div>
      <div><dt>Pojištění</dt><dd>20 mil. Kč</dd></div>
      <div><dt>Výpovědní lhůta</dt><dd>1 den</dd></div>
      <div><dt>Kontroly úřadů</dt><dd>Jsme u toho</dd></div>
    </dl>
  </div>
</section>
<section class="map-band" aria-label="Interaktivní mapa služeb">
  <div class="bar">Mapa služeb · Hradec Králové · celá ČR</div>
  {MAP}
</section>
{TICKER}
<div class="stage">
  <div class="stage-photo"><picture><source type="image/webp" srcset="assets/img/helma-720.webp 720w, assets/img/helma-1280.webp 1280w, assets/img/helma-1920.webp 1920w" sizes="(max-width: 700px) 75vh, 100vw"><img data-zoom src="assets/img/helma.jpg" alt="Pracovník drží žlutou ochrannou přilbu" width="1920" height="842" loading="lazy" decoding="async"></picture><a class="round-btn" href="#sluzby" aria-label="Přejít na služby"><svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M9 5l7 7-7 7"/></svg></a></div>
  <div class="stage-over">
  <div class="tri-labels label" aria-hidden="true"><span>Bezpečnost práce</span><span>Požární ochrana</span><span>Životní prostředí</span></div>
<section class="about-frame">
  <div class="side" aria-hidden="true"></div>
  <div class="field stripes stripes--light">
    <div class="about-card reveal">
      <div class="hatch" aria-hidden="true"></div>
      <div>
        <h2 class="h-md">Žádný projekt není příliš velký ani malý.</h2>
        <p>Naší hlavní náplní je outsourcing bezpečnosti práce a požární ochrany. Naši technici jsou odborně způsobilé osoby dle platné legislativy. Zastupujeme klienty při jednání se státní správou i při kontrolách odborného dozoru a vedeme za ně kompletní evidenci – včetně hlídání termínů revizí.</p>
        <a class="btn" href="#o-nas">Jak pracujeme <span class="arr">→</span></a>
      </div>
    </div>
  </div>
</section>

{CHEV.format("Hlavní obory")}
<section class="section" id="sluzby">
  <div class="wrap">
    <div class="section-head">
      <div>
        <span class="label label--dot">Služby</span>
        <h2 class="h-lg">Jeden partner<br>pro celou bezpečnost</h2>
      </div>
      <div>
        <p class="lead mb-s">BOZP, požární ochrana, životní prostředí, a nově i ochrana měkkých cílů a interaktivní školení první pomoci s AED.</p>
        <a class="link-arrow" href="sluzby.html">Všechny služby →</a>
      </div>
    </div>
    <div class="svc-table carousel" data-stagger>
      <a class="svc-row" href="bozp.html"><span class="num">01</span><h3>BOZP</h3><p class="muted">Rizika, kategorizace prací, dokumentace, školení, dohlídky na pracovištích.</p><span class="tags">Outsourcing · OZO</span></a>
      <a class="svc-row" href="pozarni-ochrana.html"><span class="num">02</span><h3>Požární ochrana</h3><p class="muted">Komplexní agenda a dokumentace PO, ve spolupráci se SPBS.</p><span class="tags">Dokumentace · PO</span></a>
      <a class="svc-row" href="zivotni-prostredi-ems.html"><span class="num">03</span><h3>Životní prostředí – EMS</h3><p class="muted">Zavedení a správa EMS, odpady, chemické látky, metodika ČOV.</p><span class="tags">EMS · EMAS · ČOV</span></a>
      <a class="svc-row" href="skoleni.html"><span class="num">04</span><h3>Školení</h3><p class="muted">BOZP, PO a EMS, vazači, jeřábníci, referenční řidiči, motorové pily a další.</p><span class="tags">Vstupní · Periodická</span></a>
      <a class="svc-row" href="prace-ve-vyskach.html"><span class="num">05</span><h3>Práce ve výškách</h3><p class="muted">Prodej, servis a revize OOPP proti pádu Sky Pro, speciální školení.</p><span class="tags">ČSN EN 365</span></a>
      <a class="svc-row" href="haccp.html"><span class="num">06</span><h3>HACCP</h3><p class="muted">Analýza rizik a kritické kontrolní body od příjmu surovin po výdej.</p><span class="tags">Potraviny</span></a>
      <a class="svc-row svc-row--accent" href="mekke-cile.html"><span class="num">07</span><h3>Měkké cíle</h3><p class="muted">Bezpečnostní analýza, plány a nácvik pro školy, úřady a instituce.</p><span class="tags">MŠMT · MV ČR</span></a>
      <a class="svc-row svc-row--accent" href="prvni-pomoc.html"><span class="num">08</span><h3>První pomoc &amp; AED</h3><p class="muted">Interaktivní školení na resuscitační figuríně a s tréninkovým AED.</p><span class="tags">Praxe · ERC 2025</span></a>
    </div>
  </div>
</section>

  </div>
</div>

<section class="section section--dark" id="o-nas">
  <div class="wrap">
    <div class="section-head">
      <div>
        <span class="label label--dot">O nás</span>
        <h2 class="h-lg">Dělejte, co vás baví.<br>My budeme dělat, co baví nás.</h2>
      </div>
      <p class="lead">Víme, že BOZP a PO odvádějí pozornost od businessu. Proto je převezmeme celé – s námi už nemusíte hlídat ani termíny revizí. Náš tým tvoří specialisté na BOZP, PO a životní prostředí.</p>
    </div>
    <div class="stats" data-stagger>
      <div><b><span data-count="24">24</span><sup>h</sup></b><span>denně pohotovost</span></div>
      <div><b data-count="365">365</b><span>dní v roce</span></div>
      <div><b data-count="2">2</b><span>technici na každého klienta</span></div>
      <div><b><span data-count="20">20</span><sup>mil.</sup></b><span>Kč pojištění odpovědnosti</span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <div><span class="label label--dot">Na co klademe důraz</span><h2 class="h-lg">Řízeni zákazníkem</h2></div>
      <p class="lead">Výpovědní lhůta je ze strany klienta jediný den. Pokud bychom službu dělali špatně, můžete kdykoli odejít – a to nás drží v kondici.</p>
    </div>
    <div class="cells" data-stagger style="--cols:4">
      <div class="cell">{ico("person")}<h3>Osobní přístup</h3><p>Každý klient má přiděleného technika, který řeší všechny služby. Nesedí vám? Obratem přidělíme jiného.</p></div>
      <div class="cell">{ico("clock")}<h3>Dosažitelnost</h3><p>Při kontrole státního dozoru jsme vždy přítomni. Při „havárii“ jsme k dispozici 24 hodin, 365 dní v roce.</p></div>
      <div class="cell">{ico("hand")}<h3>Loajalita</h3><p>Spolupráci stavíme dlouhodobě. Nemáme nedůležité klienty – jde o zdraví, a proto pracujeme vždy na 100 %. Samozřejmostí je mlčenlivost.</p></div>
      <div class="cell cell--dark">{ico("chip")}<h3>Informační systém</h3><p>Agendu vedeme v CRM systému: elektronická kniha úrazů, evidence revizí a hlídání legislativních změn. O každé změně vás informujeme.</p></div>
    </div>
  </div>
</section>

<section class="section section--paper">
  <div class="wrap">
    <div class="section-head">
      <div><span class="label label--dot">Aktuálně v BOZP</span><h2 class="h-lg">Co se mění</h2></div>
      <p class="lead">Legislativu sledujeme za vás. Tady je výběr změn, které se týkají většiny zaměstnavatelů.</p>
    </div>
    <div class="news" data-stagger>
      <article>
        <div class="meta"><span class="pill pill--amber">Pracovní úrazy</span><span class="label">Od 1. 1. 2026</span></div>
        <h3>Úrazy se hlásí jen elektronicky přes Portál SÚIP</h3>
        <p>Nařízení vlády č. 322/2025 Sb. nahradilo nařízení č. 201/2010 Sb. Ohlašování úrazů a zasílání záznamů probíhá výhradně elektronicky a nově se vymezuje i kategorie závažného pracovního úrazu.</p>
        <p class="src">Zdroj: <a href="https://mpsv.gov.cz/novy-rok-prinese-zmenu-v-hlaseni-pracovnich-urazu-nove-pouze-elektronicky-prostrednictvim-portalu-inspekce-prace" target="_blank" rel="noopener">MPSV</a></p>
      </article>
      <article>
        <div class="meta"><span class="pill pill--red">První pomoc</span><span class="label">ERC 2025</span></div>
        <h3>Nová doporučení pro resuscitaci</h3>
        <p>Evropská rada pro resuscitaci vydala Guidelines 2025: volat pomoc co nejdříve, kvalitní komprese 100–120/min do hloubky 5–6 cm a AED co nejrychleji – použít ho smí kdokoli.</p>
        <p class="src">Zdroj: <a href="https://www.cprguidelines.eu/" target="_blank" rel="noopener">ERC Guidelines 2025</a></p>
      </article>
      <article>
        <div class="meta"><span class="pill">Školy</span><span class="label">MŠMT</span></div>
        <h3>Minimální standard bezpečnosti ve školství</h3>
        <p>Metodické doporučení MŠMT z listopadu 2024 nahradilo standard z roku 2015. Popisuje bezpečnostní analýzu, bezpečnostní a koordinační plán i vzdělávání zaměstnanců.</p>
        <p class="src">Zdroj: <a href="https://edu.gov.cz/pro-vedeni-skoly/bezpecnost-na-skolach/materialy/" target="_blank" rel="noopener">edu.gov.cz</a> · <a href="mekke-cile.html">Měkké cíle →</a></p>
      </article>
    </div>
  </div>
</section>
{PARTNER}
{cta("Nabízíme obchodní spolupráci", "Stačí krátký telefonát nebo e-mail. Domluvíme se na úvodní schůzce a projdeme, co vaše firma potřebuje.")}
'''

# ------------------------------------------------------------------ SLUŽBY
SVC_CELLS = "".join(
    f'<a class="cell cell--link" href="{k}.html">{ico(S[k]["icon"])}<h3>{S[k]["name"]}</h3><p>{S[k]["short"]}</p>'
    f'<ul>{"".join(f"<li>{b}</li>" for b in S[k]["bullets"])}</ul><span class="foot link-arrow">Detail služby →</span></a>'
    for k in ORDER)
SLUZBY = page_hero("Služby", "Služby", "Komplexní služby v oblasti BOZP, PO a EMS – od prvního auditu po každodenní správu agendy.") + f'''
<section class="section">
  <div class="wrap">
    <div class="cells" data-stagger>
      {SVC_CELLS}
      <div class="cell cell--amber">{ico("heart")}<h3>Nové: první pomoc &amp; měkké cíle</h3><p>Interaktivní školení první pomoci s figurínou a AED. Příprava škol a institucí na mimořádné události.</p>
        <div class="foot flex-gap"><a class="btn" href="prvni-pomoc.html">První pomoc <span class="arr">→</span></a><a class="btn btn--ghost" href="mekke-cile.html">Měkké cíle</a></div></div>
    </div>
  </div>
</section>

<section class="section section--paper">
  <div class="wrap">
    <div class="section-head">
      <div><span class="label label--dot">Systém EMS</span><h2 class="h-lg">Čtyři pilíře<br>environmentálního řízení</h2></div>
      <p class="lead">Neexistuje jedna univerzální metoda zavedení EMS. Postup přizpůsobíme velikosti firmy, druhu výroby i způsobu řízení – a pomáháme i s jeho dodržováním.</p>
    </div>
    <ol class="steps" data-stagger>
      <li><h3>Plánování</h3><p>Environmentální politika, významné aspekty, zákonné požadavky, cíle a programy.</p></li>
      <li><h3>Zavedení</h3><p>Odpovědnosti, výcvik a kompetence, komunikace, dokumentace, havarijní připravenost.</p></li>
      <li><h3>Kontrola</h3><p>Monitorování a měření, nápravná opatření, záznamy, interní audit EMS.</p></li>
      <li><h3>Zlepšování</h3><p>Přezkoumání vedením, environmentální prohlášení a ověření.</p></li>
    </ol>
  </div>
</section>

{pin("Spolupráce", "Jak to probíhá", "Každého klienta mají v péči dva technici – hlavní a zástupce. Agenda tak nestojí ani během dovolené.", [
  ("Úvodní schůzka", "Prohlídka provozu a zjištění, v jakém stavu je vaše agenda. Nezávazně a zdarma.", ["Prohlídka", "Stav agendy"]),
  ("Audit a rizika", "Vyhledáme a vyhodnotíme rizika, zařadíme práce do kategorií a navrhneme opatření.", ["Rizika", "Kategorizace", "OOPP"]),
  ("Dokumentace a školení", "Doplníme, co chybí, a proškolíme zaměstnance i vedoucí pracovníky.", ["Dokumentace", "Školení"]),
  ("Průběžná správa", "Dohlídky, hlídání termínů, legislativní změny a zastupování při kontrolách úřadů.", ["Dohlídky", "Termíny", "Kontroly"]),
])}
{PARTNER}
{cta("Potřebujete převzít agendu?", "Popište nám svůj provoz. Ozveme se a navrhneme rozsah služeb, který dává smysl.")}
'''

# ------------------------------------------------------------------ MĚKKÉ CÍLE
MC = page_hero("Měkké cíle", 'Měkké<br><span class="accent-red">cíle</span>', "Školy, úřady, nemocnice, kulturní a sportovní akce. Místa s mnoha lidmi a malou ochranou. Pomůžeme je připravit – věcně, bez strašení a podle oficiální metodiky.") + f'''
<section class="section">
  <div class="wrap split split--top">
    <div class="reveal">
      <span class="label label--dot">Co je měkký cíl</span>
      <h2 class="h-md mt-s mb-m">Místo, kde se schází hodně lidí a zabezpečení je nízké.</h2>
      <p class="lead">Za ochranu odpovídá především provozovatel objektu nebo pořadatel akce. Policie ČR a Ministerstvo vnitra poskytují metodiku a konzultace – praktické nastavení opatření ale musí udělat každá instituce sama. S tím pomáháme.</p>
    </div>
    <ul class="checks" data-stagger="left">
      <li><b>Školy a školská zařízení</b><span>Podle Minimálního standardu bezpečnosti MŠMT.</span></li>
      <li><b>Úřady a veřejné instituce</b><span>Podatelny, přepážky, zasedací místnosti.</span></li>
      <li><b>Zdravotnická a sociální zařízení</b><span>Nepřetržitý provoz, klienti se sníženou pohyblivostí.</span></li>
      <li><b>Kultura, sport a veřejné akce</b><span>Bezpečnost pro pořadatele i návštěvníky.</span></li>
      <li><b>Obchodní centra a firmy</b><span>Recepce, vstupy, velké provozy.</span></li>
    </ul>
  </div>
</section>

{CHEV.format("Co pro vás uděláme")}
<section class="section section--paper">
  <div class="wrap">
    <div class="section-head">
      <div><span class="label label--dot">Co pro vás uděláme</span><h2 class="h-lg">Od analýzy<br>po nácvik</h2></div>
      <p class="lead">Postupujeme podle Minimálního standardu bezpečnosti v regionálním školství (MŠMT, 2024) a metodik Ministerstva vnitra. Pro jiné instituce obsah upravíme podle jejich provozu.</p>
    </div>
    <div class="cells" data-stagger>
      <div class="cell">{ico("eye")}<h3>Bezpečnostní analýza</h3><p>Prohlídka objektu a vyhodnocení ohroženosti. Ukáže, co funguje a kde jsou slabá místa – a kam má smysl investovat.</p></div>
      <div class="cell">{ico("doc")}<h3>Bezpečnostní a koordinační plán</h3><p>Jasné postupy pro mimořádné události, role krizového týmu a karta objektu pro součinnost se složkami IZS.</p></div>
      <div class="cell">{ico("class")}<h3>Školení zaměstnanců</h3><p>Podezřelý předmět, bombová hrozba, násilný vstup, aktivní útočník. Právní minimum a komunikace v krizi.</p></div>
      <div class="cell cell--dark">{ico("map")}<h3>Praktický nácvik</h3><p>Simulace přímo ve vaší budově, vždy bez dětí a klientů. Vedení zná scénář předem, na závěr dostanete písemné vyhodnocení.</p></div>
      <div class="cell">{ico("person")}<h3>Varovné signály</h3><p>Útočníci svůj záměr obvykle předem někomu prozradí. Naučíme vás signály rozpoznat a nastavit, kam je nahlásit.</p></div>
      <div class="cell">{ico("heart")}<h3>První pomoc v krizi</h3><p>Zástava masivního krvácení a pomoc pod stresem do příjezdu záchranky. <a class="ext-link" href="prvni-pomoc.html">Školení první pomoci →</a></p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <div><span class="label label--dot">Při útoku</span><h2 class="h-lg">Utíkej.<br>Schovej se. Bojuj.</h2></div>
      <p class="lead">Základní princip, který doporučuje Policie ČR pro situaci s aktivním útočníkem. Pořadí je důležité.</p>
    </div>
    <div class="ush" data-stagger="wipe">
      <div><span class="n">01</span><h3>Utíkej</h3><p>Pokud můžeš, opusť nebezpečné místo bezpečnou cestou. Věci nech být. Pomoz ostatním, pokud to jde.</p></div>
      <div><span class="n">02</span><h3>Schovej se</h3><p>Nelze-li utéct, zabarikáduj se v uzamykatelné místnosti, ztlum telefon, buď potichu a mimo dohled dveří.</p></div>
      <div><span class="n">03</span><h3>Bojuj</h3><p>Až jako poslední možnost, když jde o život. Jednej rozhodně a využij cokoli po ruce.</p></div>
    </div>
    <div class="callout callout--red mt-m reveal">
      <span class="big">158</span>
      <p>Až budeš v bezpečí, volej Policii ČR. Popiš místo, počet útočníků, jejich vzhled a zbraně. Po příjezdu policie měj prázdné ruce viditelně nahoře.</p>
      <span class="label">Tísňová linka</span>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="wrap split split--top">
    <div class="reveal">
      <span class="label label--dot">Prevence</span>
      <h2 class="h-lg mt-s">Nejlepší útok je ten, který se nestane.</h2>
      <p class="lead mt-s">Většina opatření nestojí mnoho peněz. Nejvíc záleží na jasných pravidlech a na tom, aby je všichni dodržovali.</p>
    </div>
    <ul class="checks" data-stagger="left">
      <li><b>Jeden kontrolovaný vstup</b><span>Ostatní vstupy během provozu zamčené, návštěvy s doprovodem.</span></li>
      <li><b>Každá místnost jde zamknout</b><span>Klíčový režim, který umožní okamžité uzamčení.</span></li>
      <li><b>Bezpečné nahlašování</b><span>Zaměstnanci, žáci i rodiče vědí, kam nahlásit znepokojivé chování.</span></li>
      <li><b>Plány nepatří na web</b><span>Plánky budovy, bezpečnostní postupy ani fotky vstupů nezveřejňujte.</span></li>
      <li><b>Pravidelný nácvik</b><span>Plán, který nikdo nezkoušel, v krizi nefunguje.</span></li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="callout reveal">
      <span class="big">800 255 255</span>
      <p>Bezplatná nonstop konzultační linka Policie ČR pro provozovatele měkkých cílů a pořadatele akcí. Spojí vás s koordinátorem ochrany měkkých cílů ve vašem kraji. Není to tísňová linka – v ohrožení volejte 158.</p>
      <span class="label">Policie ČR</span>
    </div>
  </div>
</section>
{pin("Postup", "Jak začít", "Ke všemu přistupujeme s mlčenlivostí. Výsledky analýzy jsou důvěrné a patří jen vedení instituce.", [
  ("Konzultace", "Probereme typ objektu, stávající dokumenty a vaše možnosti.", ["Online", "Na místě"]),
  ("Analýza", "Prohlídka objektu a vyhodnocení ohroženosti přímo na místě.", ["Ohroženost", "Slabá místa"]),
  ("Plány a školení", "Bezpečnostní a koordinační plán na míru a školení všech zaměstnanců.", ["Plány", "Karta pro IZS", "Školení"]),
  ("Nácvik a vyhodnocení", "Praktické cvičení ve vaší budově a písemná zpráva s doporučeními.", ["Nácvik", "Zpráva"]),
], "red")}
<section class="section--tight">
  <div class="wrap">
    <p class="sources">Zdroje: <a href="https://edu.gov.cz/pro-vedeni-skoly/bezpecnost-na-skolach/materialy/" target="_blank" rel="noopener">MŠMT – Minimální standard bezpečnosti v regionálním školství (2024)</a> · <a href="https://policie.gov.cz/ochrana-mekkych-cilu" target="_blank" rel="noopener">Policie ČR – Ochrana měkkých cílů</a> · <a href="https://policie.gov.cz/informace-pro-provozovatele" target="_blank" rel="noopener">Informace pro provozovatele</a></p>
  </div>
</section>
{cta("Připravte svou instituci", "Domluvte si úvodní konzultaci – zjistíme, co už máte, a navrhneme, kde začít.")}
'''

# ------------------------------------------------------------------ PRVNÍ POMOC
MANNEQUIN = '''
<figure class="mannequin reveal" aria-labelledby="mq-cap">
<svg viewBox="0 0 600 420" role="img" aria-label="Ilustrace resuscitační figuríny s rukama na hrudníku a připojeným AED">
  <defs><pattern id="hatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="6" stroke="#1a1b1c" stroke-opacity=".18" stroke-width="1"/></pattern></defs>
  <rect width="600" height="420" fill="url(#hatch)"/>
  <rect x="170" y="56" width="260" height="336" fill="#f3f5f7" stroke="#1a1b1c" stroke-width="1.4"/>
  <!-- hlava -->
  <ellipse cx="300" cy="112" rx="36" ry="42" fill="#e3e7eb" stroke="#1a1b1c" stroke-width="1.6"/>
  <path d="M286 100h4M310 100h4M292 126c5 4 11 4 16 0" stroke="#1a1b1c" stroke-width="1.6" fill="none" stroke-linecap="round"/>
  <path d="M288 152v16h24v-16" fill="#e3e7eb" stroke="#1a1b1c" stroke-width="1.6"/>
  <!-- trup -->
  <path d="M214 196c0-14 10-24 26-26h120c16 2 26 12 26 26l4 150c0 16-12 28-28 28H238c-16 0-28-12-28-28z" fill="#e3e7eb" stroke="#1a1b1c" stroke-width="1.6"/>
  <path d="M300 180v96" stroke="#1a1b1c" stroke-opacity=".35" stroke-width="1.2" stroke-dasharray="3 4"/>
  <path d="M244 214c20 10 38 12 56 12s36-2 56-12M240 250c22 10 40 12 60 12s38-2 60-12" stroke="#1a1b1c" stroke-opacity=".3" stroke-width="1.2" fill="none"/>
  <!-- místo stlačení -->
  <circle class="pulse" cx="300" cy="236" r="26" fill="#ffb400" fill-opacity=".6"/>
  <!-- elektrody -->
  <rect x="326" y="186" width="34" height="24" rx="4" fill="#fff" stroke="#00924a" stroke-width="2" transform="rotate(-12 343 198)"/>
  <rect x="344" y="290" width="34" height="24" rx="4" fill="#fff" stroke="#00924a" stroke-width="2" transform="rotate(20 361 302)"/>
  <path d="M358 192C430 176 450 250 488 274M376 306c40 6 70 0 112-8" stroke="#00924a" stroke-width="2" fill="none"/>
  <!-- ruce zachránce (klečí po levé straně) -->
  <g class="hands">
    <path d="M178 330 286 242M200 350 296 248" stroke="#1a1b1c" stroke-width="15" stroke-linecap="round"/>
    <ellipse cx="300" cy="238" rx="22" ry="13" fill="#1a1b1c"/>
    <ellipse cx="301" cy="233" rx="18" ry="10" fill="#3c3f44"/>
  </g>
  <!-- AED -->
  <g transform="translate(470 250)">
    <rect width="104" height="118" rx="12" fill="#00924a" stroke="#1a1b1c" stroke-width="1.6"/>
    <rect x="12" y="12" width="80" height="32" rx="4" fill="#0b6b39"/>
    <text x="52" y="34" text-anchor="middle" font-family="Geist, sans-serif" font-weight="700" font-size="16" fill="#fff">AED</text>
    <path d="M52 98s-22-13-22-27c0-7 5-11 11-11 5 0 9 3 11 7 2-4 6-7 11-7 6 0 11 4 11 11 0 14-22 27-22 27z" fill="#fff"/>
    <path class="bolt" d="M55 64l-7 13h8l-5 12" stroke="#ef4423" stroke-width="3" fill="none" stroke-linejoin="round"/>
  </g>
  <!-- popisky -->
  <g font-family="Geist Mono, monospace" font-size="11" fill="#1a1b1c">
    <polyline points="16,168 150,168 282,226" fill="none" stroke="#1a1b1c" stroke-width="1"/><circle cx="282" cy="226" r="3"/>
    <text x="16" y="158">STŘED HRUDNÍKU</text><text x="16" y="186" fill="#62666d">5–6 CM · 100–120/MIN</text>
    <line x1="343" y1="186" x2="343" y2="36" stroke="#1a1b1c" stroke-width="1"/><text x="351" y="40">ELEKTRODY AED</text>
  </g>
</svg>
<figcaption class="cap"><span class="label" id="mq-cap">Resuscitační figurína + tréninkový AED</span><span class="label muted">Animace: rytmus 110 stlačení / min</span></figcaption>
</figure>'''

PP = page_hero("První pomoc &amp; AED", 'První<br>pomoc <span class="accent-red">&amp; AED</span>', "Interaktivní školení na resuscitační figuríně a s tréninkovým defibrilátorem. Žádné dvě hodiny slajdů – každý si resuscitaci vyzkouší vlastníma rukama.") + f'''
<section class="section">
  <div class="wrap split">
    {MANNEQUIN}
    <div class="reveal">
      <span class="label label--dot">Interaktivní školení s figurínou</span>
      <h2 class="h-md mt-s mb-m">Ruce si zapamatují víc než hlava.</h2>
      <ul class="checks">
        <li><b>Resuscitace na figuríně</b><span>Správné místo, hloubka a rytmus stlačení. Každý účastník si to vyzkouší.</span></li>
        <li><b>Práce s tréninkovým AED</b><span>Nalepení elektrod, hlasové pokyny přístroje, bezpečnost při výboji.</span></li>
        <li><b>Modelové situace</b><span>Bezvědomí, dušení, masivní krvácení, úraz na pracovišti – nacvičené ve vašem prostředí.</span></li>
        <li><b>Podle aktuálních doporučení</b><span>Obsah vychází z doporučení Evropské rady pro resuscitaci (ERC Guidelines 2025).</span></li>
      </ul>
    </div>
  </div>
</section>

<section class="section--tight">
  <div class="wrap">
    <div class="kpis" data-stagger>
      <div><b>100–120</b><span>stlačení hrudníku za minutu</span></div>
      <div><b>5–6 cm</b><span>hloubka stlačení u dospělého</span></div>
      <div><b>30 : 2</b><span>stlačení a vdechy (umíte-li je)</span></div>
      <div><b>155 / 112</b><span>záchranná služba / jednotné evropské číslo</span></div>
    </div>
  </div>
</section>

<section class="hs">
  <div class="hs-sticky gridbg">
    <div class="wrap hs-head">
      <div><span class="label label--dot">Program</span><h2 class="h-lg mt-s">Co se naučíte</h2></div>
      <p class="lead">Obsah a délku přizpůsobíme vašemu provozu – kancelář, výroba, stavba, škola nebo sociální služba.</p>
    </div>
    <div class="hs-track">
      <div class="cell hs-card">{ico("phone")}<h3>Přivolání pomoci</h3><p>Bezpečnost zachránce, volání 155 / 112, aplikace Záchranka a resuscitace s pomocí operátora po telefonu.</p></div>
      <div class="cell hs-card">{ico("pulse")}<h3>Neodkladná resuscitace</h3><p>Rozpoznání zástavy oběhu, kvalitní stlačování hrudníku, střídání zachránců. Trénink na figuríně.</p></div>
      <div class="cell hs-card cell--dark">{ico("heart")}<h3>Defibrilace AED</h3><p>Kde AED najít, jak ho zapnout a použít. Přístroj vás vede hlasem a výboj podá jen tehdy, když je potřeba.</p></div>
      <div class="cell hs-card">{ico("drop")}<h3>Krvácení a úrazy</h3><p>Zástava masivního krvácení, popáleniny, zlomeniny, poleptání – nejčastější úrazy na pracovišti.</p></div>
      <div class="cell hs-card">{ico("person")}<h3>Bezvědomí a náhlé stavy</h3><p>Zotavovací poloha, infarkt, cévní mozková příhoda, epileptický záchvat, alergická reakce, dušení.</p></div>
      <div class="cell hs-card">{ico("team")}<h3>Organizace první pomoci</h3><p>Kdo na pracovišti pomáhá, kde je lékárnička a AED, co zapsat do dokumentace BOZP.</p></div>
    </div>
    <div class="wrap"><div class="pin-bar hs-bar"><i></i></div></div>
  </div>
</section>

<section class="section section--dark">
  <div class="wrap split split--top">
    <div class="reveal">
      <span class="label label--dot">Proč AED</span>
      <h2 class="h-lg mt-s">Rozhodují minuty.</h2>
      <p class="lead mt-s">Při náhlé zástavě oběhu klesá s každou minutou bez resuscitace a defibrilace šance na přežití. Záchranka potřebuje na příjezd čas – prvních několik minut je na lidech kolem.</p>
    </div>
    <ul class="checks" data-stagger="left">
      <li><b>AED smí použít kdokoli</b><span>Školení není podmínkou, ale s nácvikem jednáte rychleji a jistěji.</span></li>
      <li><b>Nemůžete ublížit</b><span>Přístroj sám vyhodnotí srdeční rytmus a výboj doporučí, jen když je potřeba.</span></li>
      <li><b>Nepřerušujte stlačování</b><span>Kvalitní komprese hrudníku pokračují, dokud vás AED nevyzve k pauze.</span></li>
      <li><b>Umístění na pracovišti</b><span>Doporučíme, kde má být AED dostupné a jak ho označit.</span></li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="wrap split split--top">
    <div class="reveal">
      <span class="label label--dot">Povinnost zaměstnavatele</span>
      <h2 class="h-md mt-s mb-s">Co říká zákoník práce</h2>
      <p class="lead">Podle § 102 zákoníku práce musí zaměstnavatel určit dostatečný počet zaměstnanců, kteří organizují poskytnutí první pomoci a přivolání záchranné služby, a zajistit jejich odbornou přípravu a vybavení. Spolupracuje přitom s poskytovatelem pracovnělékařských služeb.</p>
    </div>
    <div class="faq reveal">
      <details open><summary>Pro koho je školení určené?</summary><div><p>Pro všechny zaměstnance, zvlášť pro ty, kteří jsou určeni k poskytování první pomoci. Hodí se i pro školy, sociální služby a pořadatele akcí.</p></div></details>
      <details><summary>Jak často školení opakovat?</summary><div><p>Dovednosti bez opakování rychle mizí. Doporučujeme praktické osvěžení jednou ročně, nejpozději jednou za dva roky.</p></div></details>
      <details><summary>Kde školení probíhá?</summary><div><p>U vás na pracovišti. Figurínu i tréninkový AED přivezeme, nacvičujeme ve vašich prostorách a na situacích, které u vás reálně hrozí.</p></div></details>
      <details><summary>Dostaneme záznam do dokumentace?</summary><div><p>Ano, školení zaznamenáme tak, aby bylo doložitelné při kontrole – navazuje na vaši dokumentaci BOZP, kterou pro vás vedeme.</p></div></details>
    </div>
  </div>
</section>
{cta("Objednejte školení první pomoci", "Napište nám počet účastníků a typ provozu. Navrhneme termín a obsah na míru.", "Poptat školení")}
'''


# ------------------------------------------------------------------ STRÁNKA JEDNÉ SLUŽBY
def service_page(k):
    s = S[k]
    short = s["name"].split(" – ")[0]
    facts = "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in s["facts"])
    what = "".join(f"<p>{x}</p>" for x in s["what"])
    note = f'<p class="note mt-m">{s["note"]}</p>' if "note" in s else ""
    who = "".join(f"<li><b>{w}</b></li>" for w in s["who"])
    cells = "".join(f'<div class="cell">{ico(i)}<h3>{a}</h3><p>{b}</p></div>' for i, a, b in s["deliver"])
    law = "".join(f'<div class="law-row"><b>{a}</b><span>{b}</span></div>' for a, b in s["law"])
    faq = "".join(f"<details{' open' if j == 0 else ''}><summary>{q}</summary><div><p>{a}</p></div></details>" for j, (q, a) in enumerate(s["faq"]))
    rel = "".join(f'<a class="svc-row" href="{r}.html"><span class="num">0{ORDER.index(r)+1}</span><h3>{S[r]["name"]}</h3><p class="muted">{S[r]["short"]}</p><span class="tags">Detail →</span></a>' for r in s["related"])
    src = " · ".join(f'<a href="{u}" target="_blank" rel="noopener">{a}</a>' for a, u in s["sources"])
    extra = ""
    if "pillars" in s:
        extra = f'''
<section class="section section--paper">
  <div class="wrap">
    <div class="section-head"><div><span class="label label--dot">Systém EMS</span><h2 class="h-lg">Čtyři pilíře</h2></div><p class="lead">Postup zavedení podle cyklu plánuj – dělej – kontroluj – zlepšuj.</p></div>
    <ol class="steps" data-stagger>{"".join(f"<li><h3>{a}</h3><p>{b}</p></li>" for a, b in s["pillars"])}</ol>
  </div>
</section>'''
    if "principles" in s:
        extra = f'''
<section class="section section--paper">
  <div class="wrap">
    <div class="section-head"><div><span class="label label--dot">Jak HACCP funguje</span><h2 class="h-lg">Zásady systému</h2></div><p class="lead">Sedm zásad HACCP doplněných o pravidelnou aktualizaci systému.</p></div>
    <ol class="steps steps--4" data-stagger>{"".join(f"<li><h3>{a}</h3><p>{b}</p></li>" for a, b in s["principles"])}</ol>
  </div>
</section>'''
    h1 = s["h1"].replace('class="hl"', 'class="accent-amber-bg"')
    body = f'''
<section class="page-hero page-hero--svc">
  <div class="wrap">
    <p class="crumbs label"><a href="index.html">Úvod</a> / <a href="sluzby.html">Služby</a> / {s["name"]}</p>
    <div class="row">
      <div><span class="svc-ico" aria-hidden="true">{ICONS[s["icon"]]}</span><h1 data-reveal="fade">{h1}</h1></div>
      <p class="lead" data-reveal="fade">{s["lead"]}</p>
    </div>
    <dl class="hero-stats svc-facts" data-reveal="fade">{facts}</dl>
  </div>
  <div class="colgrid" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i></div>
</section>
<section class="section">
  <div class="wrap split split--top">
    <div class="prose reveal"><span class="label label--dot">{s["name"]}</span><h2 class="h-md mt-s mb-m">{s["what_title"]}</h2>{what}{note}</div>
    <div class="reveal"><h3 class="h-sm mb-s">{s["who_title"]}</h3><ul class="checks">{who}</ul></div>
  </div>
</section>
{extra}
{CHEV.format("Co pro vás uděláme")}
<section class="section">
  <div class="wrap">
    <div class="section-head"><div><span class="label label--dot">Co pro vás uděláme</span><h2 class="h-lg">Naše služby<br>v oblasti {short}</h2></div><p class="lead">Rozsah nastavíme podle velikosti a provozu vaší firmy. Všechno doložitelně a s hlídáním termínů.</p></div>
    <div class="cells" data-stagger style="--cols:{4 if len(s["deliver"]) % 4 == 0 else 3}">{cells}</div>
  </div>
</section>
<section class="section section--dark">
  <div class="wrap split split--top">
    <div class="reveal"><span class="label label--dot">Legislativa</span><h2 class="h-lg mt-s">Co říkají předpisy</h2><p class="lead mt-s">Hlavní předpisy, kterými se tato oblast řídí. Jejich změny sledujeme za vás.</p></div>
    <div class="law" data-stagger="left">{law}</div>
  </div>
</section>
<section class="section">
  <div class="wrap split split--top">
    <div class="reveal"><span class="label label--dot">Časté dotazy</span><h2 class="h-lg mt-s">{short} – FAQ</h2><p class="lead mt-s">Nenašli jste odpověď? Zavolejte na <a href="tel:+420737517995">737 517 995</a>.</p></div>
    <div class="faq reveal">{faq}</div>
  </div>
</section>
<section class="section--tight section--paper">
  <div class="wrap">
    <span class="label label--dot">Související služby</span>
    <div class="svc-table mt-s" data-stagger>{rel}</div>
    <p class="sources mt-m">Zdroje: {src}</p>
  </div>
</section>
{cta("Chcete to mít vyřešené?", "Domluvte si nezávaznou konzultaci. Projdeme váš provoz a navrhneme, co je potřeba.")}
'''
    return (s["title"] + " – Správa BOZP", s["lead"][:155].rsplit(" ", 1)[0] + "…" if len(s["lead"]) > 155 else s["lead"], body)

# ------------------------------------------------------------------ KONTAKT
KONTAKT = page_hero("Kontakt", "Kontakt", "Zavolejte nebo napište. Ozveme se a domluvíme úvodní schůzku – u vás, nebo online.") + f'''
<section class="section">
  <div class="wrap">
    <div class="contact-grid" data-stagger>
      <div><span class="label">Telefon · asistentka</span><a class="big" href="tel:+420737517995">737 517 995</a><p class="muted small">Administrativa a koordinace</p></div>
      <div><span class="label">E-mail</span><a class="big" href="mailto:asistentka@spravabozp.cz">asistentka@<wbr>spravabozp.cz</a><p class="muted small">Odpovídáme v pracovní dny</p></div>
      <div style="background:var(--amber)"><span class="label" style="color:var(--ink)">Pohotovost pro klienty</span><span class="big">24 / 7 / 365</span><p class="small">Pro havárie a kontroly státního dozoru</p></div>
      <div><span class="label">Sídlo &amp; doručovací adresa</span><p class="mt-s">Správa BOZP s.r.o.<br>Zemědělská 1145/4a<br>Slezské Předměstí<br>500 03 Hradec Králové</p></div>
      <div><span class="label">Fakturační údaje</span><p class="mt-s">IČ: 07414552<br>Č. ú.: 1027014087/6100<br>Datová schránka: 5hviy3m</p></div>
      <div style="background:var(--ink);color:#fff"><span class="label" style="color:#aeb4bb">Požární bezpečnost staveb</span><p class="mt-s" style="color:#c3c8ce">Školení PO, EPS, revize PBZ, ucpávky a hasicí přístroje řeší partnerská SPBS.</p><a class="btn btn--signal mt-s" href="{PO}" target="_blank" rel="noopener">spravapo.cz <span class="arr">↗</span></a></div>
    </div>
    <div class="map-frame reveal" data-map-src="https://maps.google.com/maps?q=Zem%C4%9Bd%C4%9Blsk%C3%A1%201145%2F4a%2C%20Hradec%20Kr%C3%A1lov%C3%A9&amp;z=15&amp;output=embed">
      <div class="map-consent">
        <p><b>Mapa se načte ze služby Google Maps.</b><br>Po kliknutí Google uvidí vaši IP adresu a může ukládat cookies.</p>
        <div class="flex-gap"><button type="button" class="btn" data-map-load>Zobrazit mapu</button><a class="btn btn--ghost" href="https://www.google.com/maps/search/?api=1&amp;query=Zem%C4%9Bd%C4%9Blsk%C3%A1%201145%2F4a%2C%20Hradec%20Kr%C3%A1lov%C3%A9" target="_blank" rel="noopener">Otevřít v Google Maps ↗</a></div>
      </div>
    </div>
  </div>
</section>
'''

PAGES = {
  "index.html": ("Správa BOZP s.r.o. – bezpečnost práce a požární ochrana", "Outsourcing BOZP, PO a EMS po celé ČR. Školení první pomoci s figurínou a AED, ochrana měkkých cílů. Pohotovost 24/7.", INDEX),
  "sluzby.html": ("Služby – Správa BOZP", "BOZP, požární ochrana, EMS, dokumentace, školení, práce ve výškách, HACCP.", SLUZBY),
  "mekke-cile.html": ("Ochrana měkkých cílů – Správa BOZP", "Bezpečnostní analýza, plány, školení a nácvik pro školy, úřady a instituce podle metodiky MŠMT a MV ČR.", MC),
  "prvni-pomoc.html": ("Školení první pomoci a AED – Správa BOZP", "Interaktivní školení první pomoci na resuscitační figuríně a s tréninkovým AED podle ERC 2025.", PP),
  "kontakt.html": ("Kontakt – Správa BOZP", "Správa BOZP s.r.o., Zemědělská 1145/4a, Hradec Králové. Tel. 737 517 995.", KONTAKT),
}
PAGES.update({k + ".html": service_page(k) for k in ORDER})
for name, (title, desc, body) in PAGES.items():
    (OUT / name).write_text(head(title, desc, name) + body + FOOT, encoding="utf-8")
print("ok", list(PAGES))
