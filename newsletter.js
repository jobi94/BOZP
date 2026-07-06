/* ============================================================
   Správa BOZP – Newsletter Bar
   Slides up from the bottom after 40 s on all devices.
   Session-suppressed after first show, dismiss, or submit.
   Defers if the lead-magnet popup is still visible.
   ============================================================ */
(function () {
  'use strict';

  var DELAY            = 20000;
  var SCROLL_THRESHOLD = 0.70;
  var SESSION_KEY      = 'bozp_nl_seen';

  // Session suppression
  try { if (sessionStorage.getItem(SESSION_KEY) === '1') return; } catch (e) {}

  // Excluded paths
  var EXCLUDED = ['/kontakt', '/dekujeme'];
  var path = window.location.pathname.toLowerCase();
  for (var i = 0; i < EXCLUDED.length; i++) {
    if (path.indexOf(EXCLUDED[i]) !== -1) return;
  }

  var shown = false;

  function tryShow() {
    if (shown) return;
    // If the lead-magnet popup is still open, wait 15 s more
    if (document.getElementById('bozp-overlay')) {
      setTimeout(tryShow, 15000);
      return;
    }
    shown = true;
    try { sessionStorage.setItem(SESSION_KEY, '1'); } catch (e) {}
    _inject();
  }

  setTimeout(tryShow, DELAY);

  function onScroll() {
    var scrolled  = window.scrollY || document.documentElement.scrollTop || 0;
    var maxScroll = (document.documentElement.scrollHeight || document.body.scrollHeight) - window.innerHeight;
    if (maxScroll > 0 && scrolled / maxScroll >= SCROLL_THRESHOLD) {
      window.removeEventListener('scroll', onScroll, { passive: true });
      tryShow();
    }
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  function _inject() {

    var style = document.createElement('style');
    style.textContent = [
      '@keyframes nlSlideUp{from{transform:translateY(110%)}to{transform:translateY(0)}}',

      '#nl-bar{',
        'position:fixed;bottom:0;left:0;right:0;z-index:88888;',
        'background:#0B1929;',
        'border-top:3px solid #F5A300;',
        'box-shadow:0 -8px 48px rgba(0,0,0,.4);',
        'padding:20px 24px 22px;',
        'animation:nlSlideUp .5s cubic-bezier(.22,.68,0,1.12);',
        'font-family:inherit;',
      '}',

      '#nl-bar-inner{',
        'max-width:1100px;margin:0 auto;',
        'display:flex;align-items:center;gap:20px;flex-wrap:wrap;',
        'position:relative;',
      '}',

      '#nl-bar-text{flex:1;min-width:190px;}',
      '#nl-bar-title{',
        'color:#fff;font-weight:700;font-size:15px;line-height:1.35;',
        'margin:0 0 4px;',
      '}',
      '#nl-bar-sub{',
        'color:rgba(255,255,255,.48);font-size:11.5px;line-height:1.55;margin:0;',
      '}',

      '#nl-bar-fields{display:flex;gap:0;flex-shrink:0;}',
      '#nl-bar-input{',
        'width:240px;',
        'padding:12px 16px;',
        'border:2px solid rgba(255,255,255,.18);',
        'background:rgba(255,255,255,.07);',
        'color:#fff;',
        'font-size:13px;font-family:inherit;',
        'outline:none;',
        'transition:border-color .2s,background .2s;',
      '}',
      '#nl-bar-input::placeholder{color:rgba(255,255,255,.38);}',
      '#nl-bar-input:focus{border-color:#F5A300;background:rgba(255,255,255,.12);}',
      '#nl-bar-submit{',
        'padding:12px 24px;',
        'background:#F5A300;color:#0B1929;',
        'font-size:11.5px;font-weight:700;letter-spacing:.15em;',
        'text-transform:uppercase;border:none;cursor:pointer;',
        'font-family:inherit;white-space:nowrap;flex-shrink:0;',
        'transition:background .2s;',
        'touch-action:manipulation;',
      '}',
      '#nl-bar-submit:hover{background:#F7B733;}',
      '#nl-bar-submit:disabled{opacity:.65;cursor:default;}',

      '#nl-bar-ok{',
        'display:none;align-items:center;gap:12px;flex-shrink:0;',
      '}',
      '#nl-bar-ok-icon{',
        'width:36px;height:36px;background:#F5A300;',
        'display:flex;align-items:center;justify-content:center;flex-shrink:0;',
      '}',
      '#nl-bar-ok-label{',
        'color:#fff;font-size:13.5px;font-weight:700;',
      '}',
      '#nl-bar-ok-label span{',
        'display:block;color:rgba(255,255,255,.5);font-size:11px;font-weight:400;margin-top:2px;',
      '}',

      '#nl-bar-close{',
        'position:absolute;top:-2px;right:0;',
        'width:32px;height:32px;',
        'display:flex;align-items:center;justify-content:center;',
        'color:rgba(255,255,255,.4);cursor:pointer;',
        'font-size:22px;font-weight:700;line-height:1;',
        'transition:color .15s;',
        'touch-action:manipulation;',
        '-webkit-tap-highlight-color:transparent;',
        'user-select:none;-webkit-user-select:none;',
      '}',
      '#nl-bar-close:hover{color:#fff;}',

      '@media(max-width:600px){',
        '#nl-bar{padding:18px 16px 24px;}',
        '#nl-bar-title{font-size:13.5px;padding-right:28px;}',
        '#nl-bar-fields{flex:0 0 100%;}',
        '#nl-bar-input{flex:1;width:auto;min-width:0;}',
      '}',
    ].join('');
    document.head.appendChild(style);

    var wrap = document.createElement('div');
    wrap.innerHTML =
      '<div id="nl-bar" role="complementary" aria-label="Odběr novinek">' +
        '<div id="nl-bar-inner">' +
          '<button id="nl-bar-close" aria-label="Zavřít">&#215;</button>' +
          '<div id="nl-bar-text">' +
            '<p id="nl-bar-title">Přejete si odbírat novinky ze světa BOZP, PO a EMS?</p>' +
            '<p id="nl-bar-sub">Jednou za čas — žádný spam. Odhlásit se můžete kdykoliv.</p>' +
          '</div>' +
          '<div id="nl-bar-fields">' +
            '<input id="nl-bar-input" type="email" placeholder="Váš e-mail" autocomplete="email" inputmode="email" aria-label="E-mailová adresa">' +
            '<button id="nl-bar-submit" type="button">Odbírat</button>' +
          '</div>' +
          '<div id="nl-bar-ok">' +
            '<div id="nl-bar-ok-icon">' +
              '<svg width="18" height="18" fill="none" stroke="#0B1929" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>' +
            '</div>' +
            '<div id="nl-bar-ok-label">Přihlášení proběhlo<span>Budeme vás informovat o novinkách.</span></div>' +
          '</div>' +
        '</div>' +
      '</div>';
    document.body.appendChild(wrap);

    var nlBar    = document.getElementById('nl-bar');
    var closeBtn = document.getElementById('nl-bar-close');
    var nlInput  = document.getElementById('nl-bar-input');
    var nlSubmit = document.getElementById('nl-bar-submit');
    var nlFields = document.getElementById('nl-bar-fields');
    var nlOk     = document.getElementById('nl-bar-ok');

    function dismissBar(e) {
      if (e) { e.preventDefault(); e.stopPropagation(); }
      if (nlBar._closing) return;
      nlBar._closing = true;
      nlBar.style.transition = 'transform .35s ease, opacity .35s ease';
      nlBar.style.transform  = 'translateY(110%)';
      nlBar.style.opacity    = '0';
      setTimeout(function () { if (nlBar.parentNode) nlBar.parentNode.removeChild(nlBar); }, 370);
    }

    closeBtn.addEventListener('click', dismissBar);
    closeBtn.addEventListener('touchend', dismissBar);

    function submitNewsletter() {
      var email = nlInput.value.trim();
      if (!email || email.indexOf('@') === -1 || email.indexOf('.') === -1) {
        nlInput.style.borderColor = '#E63939';
        nlInput.focus();
        setTimeout(function () { nlInput.style.borderColor = ''; }, 1800);
        return;
      }
      nlSubmit.disabled    = true;
      nlSubmit.textContent = '…';
      fetch('https://api.web3forms.com/submit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
        body: JSON.stringify({
          access_key: '5190cb3f-6bb4-440f-98b5-bccb29ec24fa',
          subject:    'Newsletter – nový odběratel',
          from_name:  'Správa BOZP – Newsletter Bar',
          replyto:    email,
          message:    'Nový odběratel newsletteru (bottom bar)\n\nE-mail: ' + email
        })
      }).finally(function () {
        nlFields.style.display = 'none';
        nlOk.style.display     = 'flex';
        setTimeout(dismissBar, 5000);
      });
    }

    nlSubmit.addEventListener('click', submitNewsletter);
    nlInput.addEventListener('keydown', function (e) {
      if (e.key === 'Enter') submitNewsletter();
    });
  }

})();
