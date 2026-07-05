/* ============================================================
   Správa BOZP – Popup: Průvodce BOZP, PO a EMS
   Triggers: 30s desktop / 60s mobile / 50% scroll / exit intent
   Suppressed: 7 days after close, excluded paths
   ============================================================ */
(function () {
  'use strict';

  var STORAGE_KEY       = 'bozp_popup_dismissed';
  var DISMISS_DAYS      = 7;
  var DELAY_DESKTOP     = 30000;   // 30 s
  var DELAY_MOBILE      = 60000;   // 60 s
  var SCROLL_THRESHOLD  = 0.50;    // 50 % stránky

  // ── Excluded paths ─────────────────────────────────────
  var EXCLUDED = ['/kontakt', '/dekujeme', '/pruvodce-bozp-po-ems'];
  var path = window.location.pathname.toLowerCase();
  for (var i = 0; i < EXCLUDED.length; i++) {
    if (path.indexOf(EXCLUDED[i]) !== -1) return;
  }

  // ── 7-day suppression ──────────────────────────────────
  function wasDismissed() {
    try {
      var ts = localStorage.getItem(STORAGE_KEY);
      if (!ts) return false;
      return (Date.now() - parseInt(ts, 10)) < DISMISS_DAYS * 86400000;
    } catch (e) { return false; }
  }
  function markDismissed() {
    try { localStorage.setItem(STORAGE_KEY, Date.now().toString()); } catch (e) {}
  }

  if (wasDismissed()) return;

  // ── State ──────────────────────────────────────────────
  var shown = false;
  var timerHandle;
  var isMobile = window.matchMedia('(max-width: 768px)').matches;

  // ── Show ───────────────────────────────────────────────
  function showPopup() {
    if (shown) return;
    shown = true;
    clearTimeout(timerHandle);
    window.removeEventListener('scroll', onScroll, false);
    document.removeEventListener('mouseleave', onExitIntent, false);
    _inject();
  }

  // ── Triggers ───────────────────────────────────────────
  timerHandle = setTimeout(showPopup, isMobile ? DELAY_MOBILE : DELAY_DESKTOP);

  function onScroll() {
    var maxScroll = document.documentElement.scrollHeight - window.innerHeight;
    if (maxScroll > 0 && window.scrollY / maxScroll >= SCROLL_THRESHOLD) showPopup();
  }
  window.addEventListener('scroll', onScroll, { passive: true });

  function onExitIntent(e) {
    if (e.clientY <= 0) showPopup();
  }
  if (!isMobile) document.addEventListener('mouseleave', onExitIntent, false);

  // ── Build & inject ────────────────────────────────────
  function _inject() {

    // CSS
    var style = document.createElement('style');
    style.textContent = [
      '@keyframes bozpFadeIn{from{opacity:0}to{opacity:1}}',
      '@keyframes bozpSlideUp{from{opacity:0;transform:translate(-50%,-46%)}to{opacity:1;transform:translate(-50%,-50%)}}',

      '#bozp-overlay{',
        'position:fixed;inset:0;z-index:99999;',
        'background:rgba(11,25,41,.72);',
        'animation:bozpFadeIn .3s ease;',
        'display:flex;align-items:center;justify-content:center;',
        'padding:16px;',
      '}',

      '#bozp-modal{',
        'position:relative;',
        'display:grid;grid-template-columns:1fr 1fr;',
        'width:100%;max-width:760px;max-height:92vh;',
        'overflow:hidden;',
        'box-shadow:0 32px 80px rgba(0,0,0,.5);',
        'animation:bozpSlideUp .35s cubic-bezier(.22,.68,0,1.2);',
      '}',

      /* ── Left panel ── */
      '#bozp-left{',
        'background:#0B1929;',
        'display:flex;flex-direction:column;align-items:center;justify-content:center;',
        'padding:36px 24px;gap:20px;',
        'position:relative;overflow:hidden;',
      '}',
      '#bozp-left::before{',
        'content:"";position:absolute;top:50%;right:-24px;width:80px;height:80px;',
        'border:1px solid rgba(245,163,0,.12);transform:translateY(-50%) rotate(45deg);',
        'pointer-events:none;',
      '}',
      '#bozp-left::after{',
        'content:"";position:absolute;top:50%;right:-8px;width:50px;height:50px;',
        'border:1px solid rgba(245,163,0,.08);transform:translateY(-50%) rotate(45deg);',
        'pointer-events:none;',
      '}',
      '#bozp-badge{',
        'display:inline-flex;align-items:center;gap:6px;',
        'background:#F5A300;color:#0B1929;',
        'font-size:10px;font-weight:700;letter-spacing:.2em;',
        'padding:6px 14px;text-transform:uppercase;',
      '}',
      '#bozp-badge svg{width:12px;height:12px;flex-shrink:0;}',
      '#bozp-cover{',
        'width:100%;max-width:220px;',
        'box-shadow:0 16px 48px rgba(0,0,0,.55);',
        'display:block;',
      '}',
      '#bozp-left-sub{',
        'color:rgba(255,255,255,.45);font-size:11px;text-align:center;',
        'font-family:inherit;letter-spacing:.02em;line-height:1.6;',
      '}',

      /* ── Right panel ── */
      '#bozp-right{',
        'background:#fff;',
        'padding:36px 36px 28px;',
        'display:flex;flex-direction:column;justify-content:center;',
        'overflow-y:auto;',
        'font-family:inherit;',
      '}',
      '#bozp-overline{',
        'font-size:10px;font-weight:700;letter-spacing:.28em;',
        'color:#F5A300;text-transform:uppercase;margin-bottom:12px;',
      '}',
      '#bozp-h2{',
        'font-size:20px;font-weight:700;color:#0B1929;line-height:1.25;',
        'margin:0 0 12px;',
      '}',
      '#bozp-perex{',
        'font-size:13.5px;color:#4b5563;line-height:1.7;margin:0 0 18px;',
      '}',
      '#bozp-bullets{',
        'list-style:none;padding:0;margin:0 0 20px;',
        'display:flex;flex-direction:column;gap:8px;',
      '}',
      '#bozp-bullets li{',
        'display:flex;align-items:center;gap:10px;',
        'font-size:13px;color:#374151;font-weight:500;',
      '}',
      '#bozp-bullets li::before{',
        'content:"✓";',
        'display:inline-flex;align-items:center;justify-content:center;',
        'width:20px;height:20px;flex-shrink:0;',
        'background:#F5A300;color:#0B1929;',
        'font-size:11px;font-weight:900;',
      '}',

      /* ── Form ── */
      '#bozp-form{display:flex;flex-direction:column;gap:10px;}',
      '#bozp-input{',
        'width:100%;padding:13px 16px;',
        'border:2px solid #e5e7eb;',
        'font-size:13.5px;font-family:inherit;color:#0B1929;',
        'outline:none;transition:border-color .2s;',
        'background:#fff;',
      '}',
      '#bozp-input:focus{border-color:#F5A300;}',
      '#bozp-input::placeholder{color:#9ca3af;}',
      '#bozp-btn{',
        'width:100%;padding:14px 20px;',
        'background:#F5A300;color:#0B1929;',
        'font-size:13px;font-weight:700;letter-spacing:.15em;',
        'text-transform:uppercase;border:none;cursor:pointer;',
        'font-family:inherit;',
        'transition:background .2s;',
        'display:flex;align-items:center;justify-content:center;gap:8px;',
      '}',
      '#bozp-btn:hover{background:#F7B733;}',
      '#bozp-btn svg{width:16px;height:16px;flex-shrink:0;}',
      '#bozp-microcopy{',
        'font-size:11px;color:#9ca3af;line-height:1.6;margin-top:2px;',
      '}',
      '#bozp-skip{',
        'display:block;text-align:center;margin-top:12px;',
        'font-size:11.5px;color:#9ca3af;text-decoration:none;',
        'transition:color .2s;border-bottom:none;',
      '}',
      '#bozp-skip:hover{color:#0B1929;}',

      /* ── Success state ── */
      '#bozp-success{',
        'display:none;flex-direction:column;align-items:flex-start;gap:16px;',
      '}',
      '#bozp-success-icon{',
        'width:48px;height:48px;background:#F5A300;',
        'display:flex;align-items:center;justify-content:center;',
        'flex-shrink:0;',
      '}',
      '#bozp-success-icon svg{width:24px;height:24px;color:#0B1929;}',
      '#bozp-success h3{',
        'font-size:18px;font-weight:700;color:#0B1929;margin:0;',
      '}',
      '#bozp-success p{',
        'font-size:13px;color:#4b5563;line-height:1.7;margin:0;',
      '}',
      '#bozp-download{',
        'display:inline-flex;align-items:center;gap:10px;',
        'background:#0B1929;color:#F5A300;',
        'padding:13px 24px;',
        'font-size:12px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;',
        'text-decoration:none;cursor:pointer;transition:background .2s;',
      '}',
      '#bozp-download:hover{background:#152438;}',
      '#bozp-download svg{width:16px;height:16px;flex-shrink:0;}',

      /* ── Close ── */
      '#bozp-close-wrap{',
        'position:absolute;top:12px;right:12px;z-index:10;',
        'display:flex;flex-direction:column;align-items:center;gap:2px;cursor:pointer;',
        'color:#fff;background:rgba(11,25,41,.55);',
        'padding:8px 10px;',
        'transition:background .2s;',
      '}',
      '#bozp-close-wrap:hover{background:rgba(11,25,41,.85);}',
      '#bozp-close-x{font-size:18px;font-weight:700;line-height:1;}',
      '#bozp-close-label{font-size:9px;letter-spacing:.06em;line-height:1.4;text-align:center;opacity:.75;max-width:72px;}',

      /* ── Mobile ── */
      '@media(max-width:640px){',
        '#bozp-modal{grid-template-columns:1fr;}',
        '#bozp-left{padding:28px 24px 20px;flex-direction:row;gap:16px;justify-content:flex-start;align-items:center;}',
        '#bozp-cover{max-width:80px;}',
        '#bozp-left-sub{display:none;}',
        '#bozp-left::before,#bozp-left::after{display:none;}',
        '#bozp-right{padding:24px 20px 20px;}',
        '#bozp-h2{font-size:17px;}',
        '#bozp-close-wrap{color:#fff;}',
      '}',
    ].join('');
    document.head.appendChild(style);

    // HTML
    var wrap = document.createElement('div');
    wrap.innerHTML =
      '<div id="bozp-overlay">' +
        '<div id="bozp-modal">' +

          /* Close */
          '<div id="bozp-close-wrap" role="button" tabindex="0" aria-label="Zavřít">' +
            '<span id="bozp-close-x">×</span>' +
            '<span id="bozp-close-label">Ne, díky. Raději riskuji pokutu.</span>' +
          '</div>' +

          /* Left */
          '<div id="bozp-left">' +
            '<span id="bozp-badge">' +
              '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>' +
              'Zdarma ke stažení' +
            '</span>' +
            '<img id="bozp-cover" src="img./pruvodce-cover.avif" alt="Průvodce BOZP, PO a EMS – obálka" loading="lazy">' +
            '<p id="bozp-left-sub">PDF · 10 oblastí · Checklisty · BOZP + PO + EMS</p>' +
          '</div>' +

          /* Right */
          '<div id="bozp-right">' +

            /* Form state */
            '<div id="bozp-form-state">' +
              '<p id="bozp-overline">Průvodce BOZP, PO a EMS</p>' +
              '<h2 id="bozp-h2">Víte, co kontroluje inspektorát jako první?</h2>' +
              '<p id="bozp-perex">Stáhněte si průvodce zdarma a zjistěte, co musí mít vaše firma v&nbsp;pořádku – než přijde kontrola a bude pozdě.</p>' +
              '<ul id="bozp-bullets">' +
                '<li>10 oblastí BOZP, PO a EMS na jednom místě</li>' +
                '<li>Checklisty, které si rovnou odškrtnete</li>' +
                '<li>Bez zbytečné legislativy – jen to podstatné</li>' +
              '</ul>' +
              '<div id="bozp-form">' +
                '<input id="bozp-input" type="email" placeholder="Váš e-mail" autocomplete="email" inputmode="email">' +
                '<button id="bozp-btn" type="button">' +
                  'Chci průvodce zdarma' +
                  '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M17 8l4 4m0 0l-4 4m4-4H3"/></svg>' +
                '</button>' +
                '<p id="bozp-microcopy">Žádný spam. Jen jednou vám pošleme odkaz ke stažení. Odhlásit se můžete kdykoliv jedním klikem.</p>' +
              '</div>' +
              '<a id="bozp-skip" href="pruvodce-bozp-po-ems.html">Raději si nejdřív přečtěte, co průvodce obsahuje →</a>' +
            '</div>' +

            /* Success state */
            '<div id="bozp-success">' +
              '<div id="bozp-success-icon">' +
                '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>' +
              '</div>' +
              '<h3>Výborně! Průvodce je připraven.</h3>' +
              '<p>Stáhněte si PDF průvodce. Vaše kontaktní informace jsme si zaznamenali – pokud budete mít zájem, ozveme se.</p>' +
              '<a id="bozp-download" href="Sprava_BOZP_Pruvodce.pdf" download="Sprava_BOZP_Pruvodce.pdf">' +
                '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>' +
                'Stáhnout průvodce (PDF)' +
              '</a>' +
            '</div>' +

          '</div>' + /* #bozp-right */
        '</div>' +   /* #bozp-modal */
      '</div>';      /* #bozp-overlay */

    document.body.appendChild(wrap);

    // ── Event bindings ──────────────────────────────────
    var overlay     = document.getElementById('bozp-overlay');
    var modal       = document.getElementById('bozp-modal');
    var closeWrap   = document.getElementById('bozp-close-wrap');
    var input       = document.getElementById('bozp-input');
    var btn         = document.getElementById('bozp-btn');
    var formState   = document.getElementById('bozp-form-state');
    var successState = document.getElementById('bozp-success');

    function close() {
      markDismissed();
      var o = document.getElementById('bozp-overlay');
      if (o) {
        o.style.animation = 'bozpFadeIn .2s ease reverse';
        setTimeout(function () { if (o.parentNode) o.parentNode.removeChild(o); }, 200);
      }
    }

    // Close on overlay click (not modal click)
    overlay.addEventListener('click', function (e) {
      if (e.target === overlay) close();
    });

    // Close button
    closeWrap.addEventListener('click', close);
    closeWrap.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') close();
    });

    // ESC key
    document.addEventListener('keydown', function escHandler(e) {
      if (e.key === 'Escape') { close(); document.removeEventListener('keydown', escHandler); }
    });

    // Submit
    btn.addEventListener('click', function () {
      var email = input.value.trim();
      if (!email || !email.includes('@') || !email.includes('.')) {
        input.focus();
        input.style.borderColor = '#E63939';
        setTimeout(function () { input.style.borderColor = ''; }, 1800);
        return;
      }
      btn.disabled = true;
      btn.innerHTML = 'Odesílám…';
      fetch('https://api.web3forms.com/submit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
        body: JSON.stringify({
          access_key: 'd71af99e-cbe2-4a35-b48f-373962c49253',
          subject: 'Nová registrace',
          from_name: 'Správa BOZP – Web',
          replyto: email,
          message: 'Nová registrace z webu spravabozp.cz\n\nE-mail: ' + email
        })
      }).finally(function () {
        formState.style.display = 'none';
        successState.style.display = 'flex';
      });
    });

    // Enter key in input
    input.addEventListener('keydown', function (e) {
      if (e.key === 'Enter') btn.click();
    });

    // Trap focus inside modal
    modal.addEventListener('keydown', function (e) {
      if (e.key !== 'Tab') return;
      var focusable = modal.querySelectorAll('button,input,a,[tabindex]');
      var arr = Array.prototype.slice.call(focusable);
      var first = arr[0], last = arr[arr.length - 1];
      if (e.shiftKey && document.activeElement === first) {
        e.preventDefault(); last.focus();
      } else if (!e.shiftKey && document.activeElement === last) {
        e.preventDefault(); first.focus();
      }
    });

    // Focus input after animation
    setTimeout(function () { if (input) input.focus(); }, 400);
  }

})();
