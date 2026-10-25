(function () {
  // Language: English text lives in the markup, Italian in data-it, Russian in data-ru.
  var nodes = Array.prototype.slice.call(document.querySelectorAll("[data-it]"));
  nodes.forEach(function (el) { el.dataset.en = el.textContent; });
  var ph = Array.prototype.slice.call(document.querySelectorAll("[data-it-placeholder]"));
  ph.forEach(function (el) { el.dataset.enPlaceholder = el.getAttribute("placeholder") || ""; });

  function setLang(l) {
    nodes.forEach(function (el) { el.textContent = (l !== "en" && el.dataset[l]) || el.dataset.en; });
    ph.forEach(function (el) { el.setAttribute("placeholder", (l === "it" && el.dataset.itPlaceholder) || (l === "ru" && el.dataset.ruPlaceholder) || el.dataset.enPlaceholder); });
    document.documentElement.lang = l;
    document.querySelectorAll(".lang button[data-lang]").forEach(function (b) { b.setAttribute("aria-pressed", String(b.dataset.lang === l)); });
    try { localStorage.setItem("deros-lang", l); } catch (e) {}
    renderShows(l);
  }

  // Next performances at La Scala, with the matching DeRos booking slot
  function renderShows(l) {
    var box = document.getElementById("shows"), src = document.getElementById("shows-data");
    if (!box || !src) return;
    var all; try { all = JSON.parse(src.textContent); } catch (e) { return; }
    var now = new Date();
    var iso = now.getFullYear() + "-" + String(now.getMonth() + 1).padStart(2, "0") + "-" + String(now.getDate()).padStart(2, "0");
    var next = all.filter(function (p) { return p.date >= iso; }).slice(0, 4);
    if (!next.length) return;
    var T = {
      kind: { opera: { en: "Opera", it: "Opera", ru: "Опера" }, ballet: { en: "Ballet", it: "Balletto", ru: "Балет" }, concert: { en: "Concert", it: "Concerto", ru: "Концерт" } },
      slot: { "14:30": { en: "Lunch before the matinée, from 12:00", it: "Pranzo prima della pomeridiana, dalle 12:00", ru: "Обед перед дневным спектаклем, с 12:00" },
              "18:00": { en: "Dinner after the show", it: "Cena dopo lo spettacolo", ru: "Ужин после спектакля" },
              "20:00": { en: "Pre-theatre dinner at 19:00", it: "Cena pre-teatro alle 19:00", ru: "Ужин перед спектаклем в 19:00" } },
      note: { "Season opening": { en: "Season opening", it: "Prima della Scala", ru: "Открытие сезона" }, "New Year's Eve": { en: "New Year's Eve", it: "Capodanno", ru: "Новогодняя ночь" } }
    };
    var fmt = null;
    try { fmt = new Intl.DateTimeFormat(l === "en" ? "en-GB" : l, { weekday: "short", day: "numeric", month: "short" }); } catch (e) {}
    box.innerHTML = "";
    next.forEach(function (p) {
      var d = new Date(p.date + "T12:00:00");
      var li = document.createElement("li");
      var tm = document.createElement("time"); tm.dateTime = p.date;
      tm.textContent = fmt ? fmt.format(d) : p.date.slice(8) + "/" + p.date.slice(5, 7);
      var div = document.createElement("div");
      var st = document.createElement("strong");
      st.textContent = p.title + (p.note ? " · " + ((T.note[p.note] || {})[l] || p.note) : "");
      var sp = document.createElement("span");
      sp.textContent = ((T.kind[p.kind] || {})[l] || p.kind) + " · " + p.time + " — " + ((T.slot[p.time] || {})[l] || "");
      div.appendChild(st); div.appendChild(sp); li.appendChild(tm); li.appendChild(div); box.appendChild(li);
    });
  }
  document.querySelectorAll(".lang button[data-lang]").forEach(function (b) {
    b.addEventListener("click", function () { setLang(b.dataset.lang); });
  });
  var start = "en";
  try { start = localStorage.getItem("deros-lang") || "en"; } catch (e) {}
  setLang(start);

  // Mobile menu
  var drawer = document.getElementById("drawer"), openBtn = document.getElementById("open-menu"), closeBtn = document.getElementById("close-menu");
  function toggle(open) {
    if (!drawer) return;
    drawer.hidden = !open;
    openBtn.setAttribute("aria-expanded", String(open));
    document.body.style.overflow = open ? "hidden" : "";
    (open ? closeBtn : openBtn).focus();
  }
  if (openBtn) openBtn.addEventListener("click", function () { toggle(true); });
  if (closeBtn) closeBtn.addEventListener("click", function () { toggle(false); });
  if (drawer) drawer.querySelectorAll("nav a").forEach(function (a) { a.addEventListener("click", function () { toggle(false); }); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape" && drawer && !drawer.hidden) toggle(false); });

  // Placeholder forms: nothing is sent in the draft
  document.querySelectorAll("form[data-demo]").forEach(function (f) {
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      var m = f.querySelector(".msg");
      if (!m) return;
      var l = document.documentElement.lang;
      var txt = {
        book: { en: "On the live site, available times from the booking platform appear here.", it: "Nel sito reale qui compaiono gli orari disponibili dalla piattaforma di prenotazione.", ru: "На готовом сайте здесь появится свободное время из системы бронирования." },
        event: { en: "Draft: this request is not sent. On the live site it is emailed to the restaurant.", it: "Bozza: la richiesta non viene inviata. Nel sito reale arriva via email al ristorante.", ru: "Черновик: запрос не отправляется. На готовом сайте он придёт ресторану по email." }
      }[f.dataset.demo] || {};
      m.textContent = txt[l] || txt.en || "";
    });
  });

  // Copy buttons for phone and email
  document.querySelectorAll(".copy-btn").forEach(function (b) {
    b.addEventListener("click", function () {
      var t = b.dataset.copy, done = function () { var o = b.textContent; b.textContent = "✓"; setTimeout(function () { b.textContent = o; }, 1400); };
      if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(t).then(done, function () {});
    });
  });
})();
