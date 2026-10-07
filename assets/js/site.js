/* Shine of Fort Lauderdale prototype: menu, reveal, lights, Gravity-style forms. No dependencies. */
(function () {
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Overlay menu (core navigation overlay behaviour)
  var menu = $('#menu'), toggle = $('.menu-toggle');
  function setMenu(open) { if (!menu) return; menu.hidden = !open; toggle.setAttribute('aria-expanded', open); document.body.style.overflow = open ? 'hidden' : ''; if (open) $('.menu-close').focus(); }
  if (toggle) toggle.addEventListener('click', function () { setMenu(true); });
  if (menu) { $('.menu-close').addEventListener('click', function () { setMenu(false); }); $$('a', menu).forEach(function (a) { a.addEventListener('click', function () { setMenu(false); }); }); }
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setMenu(false); });

  // Fade-ins and the lights band
  var io = 'IntersectionObserver' in window ? new IntersectionObserver(function (es) {
    es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add(e.target.hasAttribute('data-lights') ? 'is-lit' : 'is-in'); io.unobserve(e.target); } });
  }, { threshold: .18 }) : null;
  $$('.wp-reveal, [data-lights]').forEach(function (el) { if (io && !reduce) io.observe(el); else el.classList.add(el.hasAttribute('data-lights') ? 'is-lit' : 'is-in'); });
  var sw = $('[data-switch]');
  if (sw) sw.addEventListener('click', function () { var b = $('[data-lights]'); var on = b.classList.toggle('is-lit'); sw.textContent = on ? 'Turn them off' : 'Turn them back on'; });

  // Mobile action bar appears once the hero form scrolls away
  var bar = $('.action-bar'), anchor = $('.hero .gform_wrapper') || $('.page-banner');
  if (bar && anchor && io) new IntersectionObserver(function (es) { bar.classList.toggle('is-visible', !es[0].isIntersecting && es[0].boundingClientRect.top < 0); }).observe(anchor);

  // Gravity-style validation
  function validate(scope) {
    var ok = true;
    $$('.gfield_error', scope).forEach(function (f) { f.classList.remove('gfield_error'); var m = $('.validation_message', f); if (m) m.remove(); });
    $$('.gfield', scope).forEach(function (f) {
      var bad = false;
      if (f.hasAttribute('data-group') && f.classList.contains('gfield_contains_required')) bad = !$('input:checked', f);
      else { var i = $('input[required], select[required], textarea[required]', f); if (i) { bad = !i.value.trim() || (i.name === 'zip' && !/^\d{5}$/.test(i.value.trim())) || (i.type === 'tel' && i.value.replace(/\D/g, '').length < 10); } }
      if (bad) { ok = false; f.classList.add('gfield_error'); var m = document.createElement('div'); m.className = 'validation_message'; m.textContent = f.hasAttribute('data-group') ? 'Please choose at least one.' : 'This field is required.'; f.appendChild(m); }
    });
    return ok;
  }
  function confirm(wrap, name) {
    // Prototype only: the form service (e.g. Gravity Forms or a webhook) gets wired in here.
    wrap.innerHTML = '<div class="gform_confirmation_message" role="status"><h3>Thanks' + (name ? ', ' + name.split(' ')[0] : '') + '.</h3><p>Your request is in. The Fort Lauderdale team will call you shortly to talk through your estimate.</p></div>';
  }
  $$('[data-form]').forEach(function (wrap) {
    var form = $('form', wrap), err = $('.gform_validation_errors', wrap);
    var q = new URLSearchParams(location.search).get('service');
    if (q) { var c = $('input[value="' + q + '"]', form); if (c) c.checked = true; }
    var pages = $$('.gform_page', form), cur = 0;
    function show(n) { pages.forEach(function (p, i) { p.hidden = i !== n; }); cur = n; $('[data-step]', form).textContent = n + 1; $('.gf_progressbar_percentage', form).style.width = Math.round((n + 1) / pages.length * 100) + '%'; err.hidden = true; wrap.scrollIntoView({ block: 'start', behavior: reduce ? 'auto' : 'smooth' }); }
    $$('[data-next]', form).forEach(function (b) { b.addEventListener('click', function () { if (validate(pages[cur])) show(cur + 1); else err.hidden = false; }); });
    $$('[data-prev]', form).forEach(function (b) { b.addEventListener('click', function () { show(cur - 1); }); });
    form.addEventListener('submit', function (e) { e.preventDefault(); if (validate(pages.length ? pages[cur] : form)) confirm(wrap, (form.elements.name || {}).value); else err.hidden = false; });
  });

  // Easter egg: type "shine" or tap the logo five times and the header gets its holiday lights
  var typed = '', taps = 0, tapT;
  function festive() { document.body.classList.toggle('is-festive'); }
  document.addEventListener('keydown', function (e) { if (e.target.matches('input, textarea')) return; typed = (typed + e.key.toLowerCase()).slice(-5); if (typed === 'shine') festive(); });
  var logo = $('[data-logo]');
  if (logo) logo.addEventListener('click', function (e) { taps++; clearTimeout(tapT); tapT = setTimeout(function () { taps = 0; }, 1500); var same = logo.href.split('#')[0] === location.href.split('#')[0]; if (same) { e.preventDefault(); window.scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' }); } if (taps >= 5) { taps = 0; festive(); } });

  console.log('%cShine of Fort Lauderdale', 'font:600 16px Georgia;color:#c8102e', '\nPrototype by White Phoenix. Try typing "shine".');
})();
