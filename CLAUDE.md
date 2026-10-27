# Správa BOZP – nový web

Statický web (HTML + CSS + JS, bez build kroku) pro Správa BOZP s.r.o., Hradec Králové.
Design: inspirace crox.framer.website (šedá #e3e7eb, grafit, písmo Geist, tenké linky, pohyb)
+ barvy starého webu spravabozp.cz (žlutá #ffb400, červená → #ef4423, modrá z loga).

## Struktura
- `index.html`, `sluzby.html`, `mekke-cile.html`, `prvni-pomoc.html`, `kontakt.html`
- 8 stránek služeb (`bozp.html`, `pozarni-ochrana.html`, `zivotni-prostredi-ems.html`, `dokumentace.html`, `skoleni.html`,
  `prace-ve-vyskach.html`, `haccp.html`, `sluzby-klientum.html`) – obsah v `tools/services.py` (slovník S, převzato z varianty MQ)
- Menu: Služby (odkaz na sluzby.html; najetí myší / šipka otevře pás 4 + 4 služeb od tlačítka k pravému okraji, na mobilu seznam), Měkké cíle,
  První pomoc & AED (světle zelené tlačítko, třída .aed), O nás, Požární bezpečnost (spravapo.cz), Kontakt. Mobilní menu pod 1181 px.
- Růžová přilba sedí nakřivo na levém rohu „SP“ v hero a jen jemně se pohupuje (HELMET v build.py, .helmet v CSS) – bez trajektorie.
- Fotka helma = nízký pás (cca 46 % výšky okna, mobil 32 %); mapa služeb na PC o 20 % vyšší než původně, mobil beze změny.
- Písma Geist uložená v `assets/fonts` (fonts.css), fotka helma ve WebP (720/1280/1920).
- Do strany se web nikdy neposouvá: html/body mají overflow-x: clip (konec style.css). Nový široký prvek vždy ověřit v šířce 320–430 px.
- `assets/style.css` – tokeny barev nahoře, sekce „POHYB A ANIMACE“ dole
- `assets/main.js` – animace (připnuté sekce, vodorovný scroll, parallaxa, interaktivní mapa služeb na rotujícím 3D tělese – položky v MAP_NODES v build.py)
- `tools/build.py` – generuje všech 13 stránek se společnou hlavičkou a patičkou.
  Obsah upravuj v build.py a spusť `python3 tools/build.py .` (jinak se ruční úpravy HTML přepíšou).

## Pravidla obsahu
- Na webu NESMÍ být (přeškrtnuto klientem): revize hasicích přístrojů/elektro/plyn/tlak. zařízení…, Služby pro obce,
  „školení, revize“ v kartě Požární ochrana. UP One nahrazeno značkou „Sky Pro“.
- Školení PO, revize PBZ, EPS, ucpávky, hasicí přístroje → odkaz na partnera http://www.spravapo.cz (SPBS).
- Údaje (aktuality, ERC 2025, NV 322/2025 Sb., MŠMT standard 2024, linka 800 255 255) ověřeny 25. 10. 2026.
- GitHub: https://github.com/jobi94/BOZP (větev main). 27. 10. 2026 nahrazen původní web (zůstává v historii, commit 8ad48b3). Nasazení na Vercel až na pokyn.
- Bezpečnost (bodyguard 27. 10. 2026): hlavičky (CSP aj.) ve `vercel.json` – nová externí služba = upravit CSP; `.vercelignore` nepouští ven
  CLAUDE.md a tools/; mapa na kontaktu se načte až po kliknutí; partner odkazován přes https://spravapo.cz (www. má neplatný certifikát).
- Hlavička: jen logo (bez textu) na všech zařízeních. Úvod: jedno tlačítko Nezávazná konzultace; na telefonu jen první věta textu (.lead-more skryté) a větší název.
- Telefon: služby na úvodu = karusel (.svc-table.carousel + tečky v main.js); mobilní menu i seznam služeb v něm se plynule rozbalují.
- Výkon: `lite` v main.js (telefony/dotyk) vypíná efekty navázané na scroll, mapa kreslí 30 snímků/s a během scrollu stojí, spouští se až po načtení.
