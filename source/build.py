"""Builds the DeRos static site: one shared header/footer, five pages.
Output: out/ (deploy version, every page a full document) and out/artifact-index.html
(the home page without the document skeleton, for the claude.ai artifact)."""
import html, os, sys

SRC = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(SRC), "out")

def t(en, it, tag="span", cls="", extra=""):
    c = f' class="{cls}"' if cls else ""
    return f'<{tag}{c}{extra} data-it="{html.escape(it, quote=True)}">{html.escape(en)}</{tag}>'

paths = open(os.path.join(SRC, "paths.txt")).read().split("\n")
LOGO = '<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs><symbol id="logo" viewBox="30 38 377 208">' + \
    "".join(f'<path fill="currentColor" d="{d.strip()}"/>' for d in paths) + "</symbol></defs></svg>"

NAV = [("menu.html", "Menu", "Menu"), ("restaurant.html", "Restaurant", "Ristorante"),
       ("private-dining.html", "Private dining", "Eventi privati")]

def head(title, desc):
    return f"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="claude:viewport-fit-sides" content="cover">
<title>{title}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="restaurant">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600&family=Spectral:wght@300;400&display=swap">
<link rel="stylesheet" href="assets/site.css">"""

def lang_group():
    return f"""<div class="lang" role="group" aria-label="Language">
        <button type="button" data-lang="en" lang="en" aria-pressed="true" aria-label="English" title="English">EN</button>
        <button type="button" data-lang="it" lang="it" aria-pressed="false" aria-label="Italiano" title="Italiano">IT</button>
        <button type="button" data-lang="ru" lang="ru" aria-pressed="false" aria-label="Русский" title="Русский">RU</button>
      </div>"""

NAV_RU = {"Private dining": ' data-ru="Мероприятия"'}

def header(current):
    left = "".join(
        f'<a class="desk" href="{h}"{" aria-current=page" if h == current else ""} data-it="{it}"{NAV_RU.get(en, "")}>{en}</a>' for h, en, it in NAV)
    visit_cur = ' aria-current="page"' if current == "visit.html" else ""
    drawer_links = "".join(f'<a href="{h}" data-it="{it}">{en}</a>' for h, en, it in NAV)
    return f"""{LOGO}
<div class="draft"><div class="wrap">{t("Preview for the partners — photos of the restaurant, plus a few illustrative ones; details in [brackets] to complete.", "Anteprima per i soci — foto del ristorante e alcune indicative; dati tra [parentesi quadre] da completare.")}</div></div>
<header class="top">
  <div class="wrap">
    <div class="nav-left">
      <button class="menu-toggle" type="button" id="open-menu" aria-expanded="false" aria-controls="drawer"><span class="bars" aria-hidden="true"></span>{t("Menu", "Menu")}</button>
      {left}
    </div>
    <a class="mark" href="./" aria-label="DeRos, home"><svg role="img" aria-label="DeRos Restaurant"><use href="#logo"/></svg></a>
    <div class="nav-right">
      <a class="desk plain" href="visit.html"{visit_cur} data-it="Dove siamo" data-ru="Контакты">Visit</a>
      {lang_group()}
      <a class="btn btn-light" href="visit.html#book" data-it="Prenota" data-ru="Забронировать">Book a table</a>
    </div>
  </div>
</header>
<div class="drawer" id="drawer" hidden>
  <div class="bar">{lang_group()}<button class="close" type="button" id="close-menu" data-it="Chiudi">Close</button></div>
  <nav aria-label="Main">{drawer_links}<a href="visit.html#book" data-it="Prenota un tavolo">Book a table</a><a href="visit.html" data-it="Dove siamo">Visit</a></nav>
  <div class="facts"><span>Via Romagnosi 4, Milano · {t("Next to La Scala", "Accanto alla Scala")}</span><span>+39 02 3651 7680</span></div>
</div>"""

FOOTER = f"""<footer>
  <div class="wrap">
    <div class="cols">
      <div style="display:grid;gap:16px;align-content:start">
        <span class="mark"><svg role="img" aria-label="DeRos Restaurant"><use href="#logo"/></svg></span>
        {t("Seafood restaurant next to La Scala, a few minutes from Via Montenapoleone.", "Ristorante di pesce accanto alla Scala, a pochi minuti da via Montenapoleone.")}
      </div>
      <div><h4 data-it="Indirizzo">Address</h4>Via Romagnosi 4, 20121 Milano<br>{t("Metro M3 Montenapoleone, 250 m", "Metro M3 Montenapoleone, 250 m")}<br>{t("Parking: Autosilo San Fedele", "Parcheggio: Autosilo San Fedele")}</div>
      <div><h4 data-it="Orari">Opening hours</h4><div class="hours">{t("Every day", "Tutti i giorni")}<span></span>{t("Lunch", "Pranzo")}<span>12:00 – 15:00</span>{t("Dinner", "Cena")}<span>19:00 – 23:00</span></div></div>
      <div><h4 data-it="Contatti">Contact</h4>+39 02 3651 7680<br>[info@derosmilano.it]<br><a href="https://www.instagram.com/deros.ristorantemilano/" target="_blank" rel="noopener">Instagram</a> · <a href="https://www.facebook.com/deros.ristorante/" target="_blank" rel="noopener">Facebook</a> · <a href="https://www.tiktok.com/@derosristorante" target="_blank" rel="noopener">TikTok</a></div>
    </div>
    <div class="legal">{t("[Company name] · VAT [number]", "[Ragione sociale] · P.IVA [numero]")}<a href="#" data-it="Privacy">Privacy policy</a><a href="#" data-it="Cookie">Cookie policy</a><span>© 2026 DeRos</span></div>
  </div>
</footer>
<div class="bookbar"><a class="btn btn-light" href="visit.html#book" data-it="Prenota un tavolo">Book a table</a></div>
<script src="assets/site.js"></script>"""

# Restaurant photos from the previous site (rights to confirm before launch); chef, catch and street are still Unsplash.
IMG = {"The dining room at night": ("hero", "The DeRos dining room with blue velvet banquettes"),
       "Private room": ("private", "A blue velvet booth set for dinner"),
       "Raw bar": ("rawbar", "Bluefin tuna, sliced raw"),
       "The dining room": ("restaurant-head", "The DeRos dining room"),
       "Private room set for dinner": ("events-head", "A velvet cushion embroidered with the DeRos logo"),
       "Street entrance": ("visit-head", "Piazza della Scala, Milan"),
       "Chef at the pass": ("chef-pass", "Chef plating a dish"),
       "The morning delivery": ("catch", "Fresh fish and shellfish on ice"),
       "Chef portrait": ("chef-portrait", "Chef finishing a fish dish")}

def _img(name, alt, eager=False):
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return f'<img src="assets/img/{name}.webp" alt="{html.escape(alt)}" {load} decoding="async">'

def photo(en, it, ratio, img=None, alt=None):
    if img is None and en in IMG:
        img, alt = IMG[en]
    if img:
        return f'<div class="photo {ratio}">{_img(img, alt or en)}</div>'
    return f'<div class="photo {ratio}">{t("Photo · " + en, "Foto · " + it)}</div>'

def band(cls, ph_en, ph_it, inner, heading_id):
    if ph_en in IMG:
        name, alt = IMG[ph_en]
        shot = _img(name, alt, eager=("hero" in cls))
    else:
        shot = t("Photo · " + ph_en, "Foto · " + ph_it, cls="ph-tag")
    return f"""<section class="band-photo {cls}" aria-labelledby="{heading_id}">
  <div class="shot">{shot}</div>
  <div class="copy"><div class="wrap">{inner}</div></div>
</section>"""

def m(en, it, price="€ —"):
    return f'<li>{t(en, it, cls="name")}<span class="price">{price}</span></li>'

def dish(name_en, name_it, desc_en, desc_it, confirm=False, price="€ —"):
    tag = f'<div class="tags">{t("To confirm with the kitchen", "Da confermare con la cucina", cls="tag confirm")}</div>' if confirm else ""
    return f'<li>{t(name_en, name_it, cls="name")}<span class="price">{price}</span>{t(desc_en, desc_it, cls="desc")}{tag}</li>'

CATCH_TABLE = f"""<div class="table-scroll">
  <table class="catch">
    <thead><tr><th data-it="Pesce">Fish</th><th data-it="Provenienza">From</th><th data-it="All'etto">Per 100 g</th></tr></thead>
    <tbody>
      <tr><td data-it="Gambero rosso">Red prawn</td><td class="origin">[Mazara del Vallo]</td><td>€ —</td></tr>
      <tr><td data-it="Scampi">Langoustine</td><td class="origin">[porto]</td><td>€ —</td></tr>
      <tr><td data-it="Ricciola">Amberjack</td><td class="origin">[porto]</td><td>€ —</td></tr>
      <tr><td data-it="Tonno rosso">Bluefin tuna</td><td class="origin">[porto]</td><td>€ —</td></tr>
      <tr><td data-it="Ostriche">Oysters</td><td class="origin">[origine]</td><td data-it="€ — cad.">€ — each</td></tr>
    </tbody>
  </table>
  <p class="note" data-it="Righe di esempio: la lista reale va aggiornata ogni giorno dallo staff.">Example rows: the real list is updated daily by the staff.</p>
</div>"""

# ---------- Pages ----------
from scala import P as SCALA
import json, datetime as _dt
SLOT = {"14:30": ("Lunch before the matinée, from 12:00", "Pranzo prima della pomeridiana, dalle 12:00"),
        "18:00": ("Dinner after the show", "Cena dopo lo spettacolo"),
        "20:00": ("Pre-theatre dinner at 19:00", "Cena pre-teatro alle 19:00")}
KIND = {"opera": ("Opera", "Opera"), "ballet": ("Ballet", "Balletto"), "concert": ("Concert", "Concerto")}
NOTES = {"2026-12-07": "Season opening", "2026-12-31": "New Year's Eve"}

def shows_block():
    today = _dt.date(2026, 10, 25).isoformat()
    nxt = [p for p in SCALA if p["date"] >= today][:4]
    lis = []
    for p in nxt:
        when = _dt.date.fromisoformat(p["date"]).strftime("%d/%m")
        tm = p["time"]
        ken, kit = KIND[p["kind"]]
        sen, sit = SLOT[tm]
        lis.append('<li><time>' + when + '</time><div><strong>' + html.escape(p["title"]) + '</strong>'
                   + t(ken + " · " + tm + " — " + sen, kit + " · " + tm + " — " + sit) + '</div></li>')
    data = json.dumps([dict(p, note=NOTES.get(p["date"], "")) for p in SCALA], ensure_ascii=False)
    return f"""<div class="shows">
      {t("Next at La Scala", "Prossimamente alla Scala", tag="p", cls="label")}
      <ol class="timeline" id="shows">{"".join(lis)}</ol>
      <p class="note"><a href="https://www.teatroallascala.org/en/calendar.html" target="_blank" rel="noopener" data-it="Calendario ufficiale del Teatro alla Scala, stagione 2026/27">Teatro alla Scala official calendar, season 2026/27</a></p>
      <a class="btn btn-solid" href="visit.html#book" data-it="Prenota prima dello spettacolo">Book before the show</a>
    </div>
    <script type="application/json" id="shows-data">{data}</script>"""

SHOWS_BLOCK = shows_block()

HOME = band("hero", "The dining room at night", "La sala di sera", f"""
  {t("Seafood · Milan · Next to La Scala", "Pesce · Milano · Accanto alla Scala", tag="p", cls="label")}
  <h1 id="hero-title" data-it="Il meglio dei mari italiani.">The finest catch of the Italian coasts.</h1>
  <div class="actions"><a class="btn btn-light" href="visit.html#book" data-it="Prenota un tavolo">Book a table</a><a class="btn btn-line" href="menu.html" data-it="Vedi il menu">See the menu</a></div>""", "hero-title") + f"""
<section class="pad statement">
  <div class="wrap">
    <blockquote data-it="Pesce scelto ogni mattina e servito la sera stessa, a due passi dal Teatro alla Scala.">Fish chosen every morning and served the same evening, two minutes from La Scala.</blockquote>
    <div class="pillars">
      <div>{t("Daily catch", "Pescato del giorno", tag="strong")}{t("From [ports / suppliers], priced by weight.", "Da [porti / fornitori], a peso.")}</div>
      <div>{t("Raw bar", "Crudi", tag="strong")}{t("Oysters, crudo and tartare, made to order.", "Ostriche, crudo e tartare, preparati al momento.")}</div>
      <div>{t("Lunch and dinner", "Pranzo e cena", tag="strong")}{t("Open every day, 12:00 – 15:00 and 19:00 – 23:00.", "Aperti tutti i giorni, 12:00 – 15:00 e 19:00 – 23:00.")}</div>
      <div>{t("Italian cellar", "Cantina", tag="strong")}{t("69 labels, from Franciacorta to Champagne.", "69 etichette, dal Franciacorta allo Champagne.")}</div>
    </div>
  </div>
</section>
<p class="wrap rating"><a href="https://www.tripadvisor.com/Restaurant_Review-g187849-d11951685-Reviews-DeRos-Milan_Lombardy.html" target="_blank" rel="noopener">{t("4.4 out of 5 on Tripadvisor · 256 reviews", "4,4 su 5 su Tripadvisor · 256 recensioni")}</a></p>
<section class="pad on-surface" aria-labelledby="scala-title">
  <div class="wrap scala">
    <div class="text">
      {t("Before and after the opera", "Prima e dopo l'opera", tag="p", cls="label")}
      <h2 id="scala-title" data-it="La tavola che segue il calendario della Scala.">A table timed to La Scala's calendar.</h2>
      <p class="lead" data-it="Il teatro è a due minuti a piedi. Pranzo prima delle pomeridiane, cena prima degli spettacoli serali, cena dopo quelli che iniziano alle 18:00.">The theatre is a two-minute walk away. Lunch before matinées, dinner before evening performances, supper after the 18:00 shows.</p>
      <p data-it="In carta c'è anche il Franciacorta Bellavista Teatro alla Scala 2020.">The list even includes Bellavista's Franciacorta Teatro alla Scala 2020.</p>
      <a class="text-link" href="menu.html#theatre" data-it="Il menu pre-teatro">The pre-theatre menu</a>
      {t("Proposal: to confirm with the restaurant", "Proposta: da confermare con il ristorante", tag="p", cls="ex")}
    </div>
    {SHOWS_BLOCK}
  </div>
</section>
<section class="pad" aria-labelledby="dishes-title">
  <div class="wrap">
    <div class="sec-head"><h2 id="dishes-title" data-it="I piatti firma">Signature dishes</h2><a class="text-link" href="menu.html" data-it="Il menu completo">The full menu</a></div>
    <div class="plates">
      <article>{photo("Dish", "Piatto", "r-3-4", img="dish-tuna", alt="Bluefin tuna carpaccio")}<div class="row-price">{t("Bluefin tuna carpaccio, fresh wasabi", "Carpaccio di tonno rosso con wasabi fresco", tag="h3")}<span class="price">€ —</span></div></article>
      <article>{photo("Dish", "Piatto", "r-3-4", img="dish-spaghetti", alt="Smoked spaghetti with clams")}<div class="row-price">{t("Smoked spaghetti, clams, grilled datterini tomatoes", "Spaghetti affumicati alle vongole e datterini grigliati", tag="h3")}<span class="price">€ —</span></div></article>
      <article>{photo("Dish", "Piatto", "r-3-4", img="dish-triglia", alt="Red mullet tempura with artichokes")}<div class="row-price">{t("Red mullet tempura, Sardinian artichokes", "Triglia in tempura con carciofi sardi", tag="h3")}<span class="price">€ —</span></div></article>
    </div>
  </div>
</section>
<section class="pad on-surface" aria-labelledby="catch-title">
  <div class="wrap slate">
    <div class="intro">
      {t("Today's catch", "Il pescato del giorno", tag="p", cls="label")}
      <h2 id="catch-title" data-it="A peso, scelto al tavolo.">Priced by weight, chosen at the table.</h2>
      <p data-it="Chiedete di vedere il pesce prima della cottura. Prezzi all'etto.">Ask to see the fish before it is cooked. Prices per 100 g.</p>
    </div>
    {CATCH_TABLE}
  </div>
</section>
""" + band("side plate", "Private room", "Sala privata", f"""
  {t("Private dining", "Eventi privati", tag="p", cls="label")}
  <h2 id="priv-title" data-it="La sala in esclusiva, fino a [N] ospiti.">The whole room, for up to [N] guests.</h2>
  <p data-it="Compleanni, cene di lavoro, gruppi dopo la Scala. Rispondiamo entro 24 ore.">Birthdays, business dinners, groups after La Scala. We reply within 24 hours.</p>
  <a class="btn btn-line" href="private-dining.html" data-it="Organizza un evento">Plan an event</a>""", "priv-title") + f"""
<section class="pad" aria-labelledby="chef-title">
  <div class="wrap split">
    {photo("Chef at the pass", "Lo chef al passe", "r-4-5")}
    <div class="text">
      {t("The chef", "Lo chef", tag="p", cls="label")}
      <h2 id="chef-title" data-it="Lo chef Davide">Chef Davide</h2>
      <p data-it="[X] anni in [ristoranti / esperienze], oggi in cucina con un menu che cambia con quello che portano le barche.">[X] years in [restaurants / experiences], now cooking a menu that changes with what the boats bring in.</p>
      <a class="text-link" href="restaurant.html" data-it="La nostra storia">Our story</a>
    </div>
  </div>
</section>"""

from wines import WINES
def _price(v):
    return "€ " + f"{v:,}".replace(",", ".") if v is not None else None
def wine_section():
    groups = []
    for (en, it, ru), rows in WINES:
        items = []
        for name, prod, price in rows:
            pr = _price(price)
            ptxt = f'<span class="price">{pr}</span>' if pr else t("On request", "Su richiesta", cls="price")
            sub = f'<span class="desc">{html.escape(prod)}</span>' if prod else ""
            items.append(f'<li><span class="name">{html.escape(name)}</span>{ptxt}{sub}</li>')
        RU_EXTRA[en] = ru
        groups.append(f'<div class="wine-group"><h3 data-it="{html.escape(it)}">{html.escape(en)}</h3><ul class="dish-list">{"".join(items)}</ul></div>')
    n = sum(len(r) for _, r in WINES)
    return f"""<section class="course" id="wine"><div class="intro"><h2 data-it="Carta dei vini">Wine list</h2>
    {t(f"{n} labels. Prices per bottle.", f"{n} etichette. Prezzi a bottiglia.", tag="p")}
    {t("Ask the staff for tasting notes and wines by the glass.", "Chiedete al personale note di degustazione e vini al calice.", tag="p")}</div>
    <div class="wine-groups">{"".join(groups)}</div></section>"""
RU_EXTRA = {}
WINE_SECTION = wine_section()

MENU = band("page-head", "Raw bar", "Banco dei crudi", f"""
  {t("Menu", "Menu", tag="p", cls="label")}
  <h1 id="menu-title" data-it="Il menu">The menu</h1>
  <p data-it="Cambia con il pescato. Prezzi in euro, servizio incluso.">It changes with the catch. Prices in euros, service included.</p>""", "menu-title") + f"""
<nav class="menu-nav" aria-label="Menu sections"><div class="wrap">
  <a href="#starters" data-it="Antipasti">Starters</a><a href="#raw" data-it="Crudi">Raw bar</a><a href="#pasta" data-it="Primi">Pasta &amp; risotto</a><a href="#mains" data-it="Secondi">Mains</a><a href="#catch" data-it="Pescato">Daily catch</a><a href="#theatre" data-it="Pre-teatro">Pre-theatre</a><a href="#desserts" data-it="Dolci">Desserts</a><a href="#wine" data-it="Carta dei vini">Wine list</a>
</div></nav>
<div class="wrap">
  <section class="course" id="starters"><div class="intro"><h2 data-it="Antipasti">Starters</h2></div><ul class="dish-list">
    {m("Artichoke salad, celery, 36-month Parmigiano Reggiano", "Insalatina di carciofi sardi con sedano e parmigiano reggiano 36 mesi")}
    {m("Creamed salt cod on Jerusalem artichoke cream", "Baccalà mantecato su crema di topinambur")}
    {m("Warm seafood salad", "Tiepido di mare")}
    {m("Fried baby squid", "Frittino di calamaretti spillo")}
    {m("Seared octopus, vegetables and aioli", "Polpo scottato con verdure e aiolì")}
    {m("Cantabrian anchovies, San Filippo reserve", "Acciughe del Mar Cantabrico riserva “San Filippo”")}
    {m("Bluefin tuna carpaccio, fresh wasabi", "Carpaccio di tonno rosso con wasabi fresco")}
    {m("Amberjack carpaccio, candied lemon, wasabi and yukari", "Carpaccio di ricciola con limone candito, wasabi e yukari")}
  </ul></section>
  <section class="course" id="raw"><div class="intro"><h2 data-it="Crudi">Raw bar</h2><p data-it="Preparati al momento, mai in anticipo.">Prepared to order, never in advance.</p></div><ul class="dish-list">
    {m("Langoustines", "Scampi")}
    {m("Prawns", "Gamberi")}
    {m("Oysters", "Ostriche")}
    {m("Sea urchins", "Ricci di mare")}
  </ul></section>
  <section class="course" id="pasta"><div class="intro"><h2 data-it="Primi">Pasta &amp; risotto</h2></div><ul class="dish-list">
    {m("King crab tortello, greens and mascarpone", "Tortello al king crab, erbette e mascarpone")}
    {m("Risotto with spinach, grilled scallops and lemon zest", "Risotto con spinaci, capesante grigliate e zeste di limone")}
    {m("Smoked spaghetti, clams, grilled datterini tomatoes", "Spaghetti affumicati alle vongole e pomodorini datterini grigliati")}
    {m("Linguine alla Nerano, grilled baby squid", "Linguine alla Nerano e calamaretti grigliati")}
    {m("Paccheri with lobster, tomato and basil", "Paccheri all'astice, pomodoro e basilico")}
    {m("Calamarata with seafood", "Calamarata ai frutti di mare")}
  </ul></section>
  <section class="course" id="mains"><div class="intro"><h2 data-it="Secondi">Mains</h2></div><ul class="dish-list">
    {m("Catch of the day", "Pescato del giorno", price="€ — / 100 g")}
    {m("Seared bluefin tuna, grilled seasonal vegetables, crusco pepper sauce", "Tonno rosso scottato con verdure di stagione grigliate e salsa di peperone crusco")}
    {m("Red mullet tempura, Sardinian artichoke hearts", "Triglia in tempura con cuore di carciofi sardi di stagione")}
    {m("Turbot, Mediterranean style", "Rombo chiodato alla mediterranea")}
    {m("Black cod and greens", "Black cod ed erbette")}
  </ul></section>
  <section class="course" id="catch"><div class="intro"><h2 data-it="Il pescato del giorno">Daily catch</h2><p data-it="Scegliete il pesce al tavolo. Prezzi all'etto.">Choose your fish at the table. Prices per 100 g.</p></div>{CATCH_TABLE}</section>
  <section class="course" id="theatre"><div class="intro"><h2 data-it="Menu pre-teatro">Pre-theatre menu</h2><p data-it="Dalle 19:00, all'apertura della cena: tre portate in un'ora. Proposta da confermare.">From 19:00, when dinner service opens: three courses within the hour. Proposal to confirm.</p></div><ul class="dish-list">
    {dish("Three courses and a glass of wine", "Tre portate e un calice di vino", "Crudo, a pasta or risotto, dessert, served within the hour.", "Crudo, un primo, un dolce, serviti in un'ora.", price="€ — p.p.")}
  </ul></section>
  <section class="course" id="desserts"><div class="intro"><h2 data-it="Dolci">Desserts</h2></div><ul class="dish-list">
    {m("Tiramisù", "Tiramisù")}
    {m("Seasonal fruit", "Frutta di stagione")}
    {m("Tarte tatin, custard and vanilla ice cream", "Tarte tatin con crema inglese e gelato alla vaniglia")}
    {m("Profiteroles with hot chocolate", "Profiterole con cioccolato caldo")}
    {m("Babà with cream gelato", "Babà con gelato alla crema")}
  </ul></section>
  {WINE_SECTION}
  <div class="allergens">
    <p data-it="Allergeni: chiedete al personale l'elenco completo (Reg. UE 1169/2011). Alcuni prodotti possono essere abbattuti a temperatura negativa per la sicurezza alimentare.">Allergens: ask our staff for the full list (EU Reg. 1169/2011). Some products may be blast-frozen for food safety.</p>
    <p data-it="Piatti dal menu pubblicato sul sito precedente: prezzi da inserire.">Dishes from the menu published on the previous site: prices to be added.</p>
  </div>
</div>"""

RESTAURANT = band("page-head", "The dining room", "La sala", f"""
  {t("The restaurant", "Il ristorante", tag="p", cls="label")}
  <h1 id="rest-title" data-it="Un ristorante di mare nel cuore di Milano.">A seafood restaurant in the heart of Milan.</h1>""", "rest-title") + f"""
<section class="pad statement">
  <div class="wrap">
    {t("Since 2016", "Dal 2016", tag="p", cls="label")}
    <blockquote data-it="Dal 2016 DeRos porta il miglior pesce d'Italia a Milano, accanto al suo teatro più famoso. Autentico, raffinato, italiano.">Since 2016, DeRos has brought the best fish in Italy to Milan, next to its most famous theatre. Authentic, refined, Italian.</blockquote>
  </div>
</section>
<section class="pad on-surface" aria-labelledby="source-title">
  <div class="wrap split">
    {photo("The morning delivery", "L'arrivo del pescato", "r-4-5")}
    <div class="text">
      {t("Sourcing", "La materia prima", tag="p", cls="label")}
      <h2 id="source-title" data-it="Da [porti] alla tavola in meno di 24 ore.">From [ports] to the table in under 24 hours.</h2>
      <p data-it="[Fornitori, porti, frequenza degli arrivi. Solo fatti verificabili.]">[Suppliers, ports, delivery frequency. Verifiable facts only.]</p>
    </div>
  </div>
</section>
<section class="pad" aria-labelledby="chef2-title">
  <div class="wrap split rev">
    {photo("Chef portrait", "Ritratto dello chef", "r-4-5")}
    <div class="text">
      {t("The chef", "Lo chef", tag="p", cls="label")}
      <h2 id="chef2-title" data-it="Lo chef Davide">Chef Davide</h2>
      <p data-it="[Biografia di 80-100 parole: formazione, ristoranti precedenti, idea di cucina.]">[80–100 word biography: training, previous kitchens, approach to cooking.]</p>
    </div>
  </div>
</section>
<section class="pad on-surface" aria-labelledby="room-title">
  <div class="wrap">
    <div class="sec-head"><div>{t("The room", "La sala", tag="p", cls="label")}<h2 id="room-title" data-it="[N] coperti, un servizio caloroso.">[N] seats, warm service.</h2></div></div>
    <div class="facts-grid">
      <div>{t("Seats", "Coperti", tag="p", cls="label")}<p>[N]</p></div>
      <div>{t("Private room", "Sala privata", tag="p", cls="label")}<p data-it="Fino a [N] ospiti">Up to [N] guests</p></div>
      <div>{t("Atmosphere", "Atmosfera", tag="p", cls="label")}<p data-it="Intima e accogliente, senza formalità">Intimate and welcoming, never stiff</p></div>
    </div>
  </div>
</section>"""

EVENTS = band("page-head", "Private room set for dinner", "Sala privata apparecchiata", f"""
  {t("Private dining", "Eventi privati", tag="p", cls="label")}
  <h1 id="ev-title" data-it="Cene private ed eventi aziendali.">Private dinners and corporate events.</h1>
  <p data-it="La sala in esclusiva o un ambiente riservato fino a [N] ospiti.">The whole restaurant or a private room for up to [N] guests.</p>""", "ev-title") + f"""
<section class="pad" aria-labelledby="formats-title">
  <div class="wrap">
    <div class="sec-head"><div>{t("Formats", "Formati", tag="p", cls="label")}<h2 id="formats-title" data-it="Tre formule per i gruppi.">Three options for groups.</h2></div></div>
    <div class="facts-grid">
      <div>{t("Private room", "Sala privata", tag="h3")}<p data-it="Fino a [N] ospiti, menu fisso da € — a persona.">Up to [N] guests, set menu from € — per person.</p></div>
      <div>{t("Exclusive use", "Locale in esclusiva", tag="h3")}<p data-it="L'intero ristorante, fino a [N] ospiti seduti.">The whole restaurant, up to [N] seated guests.</p></div>
      <div>{t("After La Scala", "Dopo la Scala", tag="h3")}<p data-it="Cena per gruppi dopo lo spettacolo, con tavolo pronto all'uscita.">Group supper after the performance, table ready as you leave.</p></div>
    </div>
  </div>
</section>
<section class="pad on-surface" aria-labelledby="enq-title">
  <div class="wrap two">
    <div class="text">
      <h2 id="enq-title" data-it="Richiedi una proposta">Request a proposal</h2>
      <p data-it="Rispondiamo entro 24 ore con menu, abbinamenti e preventivo.">We reply within 24 hours with menu, pairings and a quote.</p>
      <div class="contact-alt"><span><strong>Email</strong> · [events@derosmilano.it]</span><span><strong data-it="Telefono">Phone</strong> · +39 02 3651 7680</span></div>
    </div>
    <form class="form" data-demo="event">
      <div class="fields">
        <label for="e-name"><span data-it="Nome">Name</span><input id="e-name" autocomplete="name"></label>
        <label for="e-email"><span>Email</span><input id="e-email" type="email" autocomplete="email"></label>
        <label for="e-phone"><span data-it="Telefono">Phone</span><input id="e-phone" type="tel" autocomplete="tel"></label>
        <label for="e-date"><span data-it="Data">Date</span><input id="e-date" type="date"></label>
        <label for="e-guests"><span data-it="Ospiti">Guests</span><input id="e-guests" type="number" min="6" inputmode="numeric"></label>
        <label for="e-type"><span data-it="Tipo di evento">Event type</span><select id="e-type"><option data-it="Cena privata">Private dinner</option><option data-it="Evento aziendale">Corporate event</option><option data-it="Dopo la Scala">After La Scala</option><option data-it="Altro">Other</option></select></label>
        <label for="e-notes" class="full"><span data-it="Note">Notes</span><textarea id="e-notes"></textarea></label>
      </div>
      <button class="btn btn-solid" type="submit" data-it="Invia la richiesta">Send request</button>
      <p class="msg" data-it="Bozza: il modulo non invia nulla.">Draft: this form does not send anything.</p>
    </form>
  </div>
</section>"""

VISIT = band("page-head", "Street entrance", "L'ingresso su strada", f"""
  {t("Visit", "Dove siamo", tag="p", cls="label")}
  <h1 id="visit-title" data-it="A pochi passi dal Teatro alla Scala.">A few steps from La Scala.</h1>""", "visit-title") + f"""
<section class="pad" id="book" aria-labelledby="book-title" style="scroll-margin-top:90px">
  <div class="wrap two">
    <div class="text">
      <h2 id="book-title" data-it="Prenota un tavolo">Book a table</h2>
      <p data-it="Disponibilità in tempo reale e conferma immediata via email. Per gruppi oltre [N] persone, contattateci direttamente.">Live availability and instant confirmation by email. For parties larger than [N], contact us directly.</p>
      <div class="contact-alt">
        <span class="copyable"><strong data-it="Telefono">Phone</strong> +39 02 3651 7680 <button class="copy-btn" type="button" data-copy="+39 0236517680" data-it="Copia">Copy</button></span>
        <span class="copyable"><strong>WhatsApp</strong> [+39 …]</span>
        <span class="copyable"><strong>Email</strong> [info@derosmilano.it] <button class="copy-btn" type="button" data-copy="info@derosmilano.it" data-it="Copia">Copy</button></span>
      </div>
    </div>
    <div class="book-cta">
      <a class="btn btn-solid" href="visit.html#book" data-it="Scegli data e orario">Choose date and time</a>
      <p class="note" data-it="La prenotazione si apre su SevenRooms, in una nuova scheda.">Booking opens on SevenRooms, in a new tab.</p>
    </div>
  </div>
</section>
<section class="pad on-surface" aria-labelledby="where-title">
  <div class="wrap">
    <div class="sec-head"><div>{t("Getting here", "Come arrivare", tag="p", cls="label")}<h2 id="where-title" data-it="Via Romagnosi 4, 20121 Milano">Via Romagnosi 4, 20121 Milan</h2></div><a class="text-link" href="https://maps.app.goo.gl/t5BjE6xVXBp1mNLd6" target="_blank" rel="noopener" data-it="Apri in Google Maps">Open in Google Maps</a></div>
    <div class="facts-grid">
      <div>{t("Metro", "Metro", tag="p", cls="label")}<p data-it="M3 Montenapoleone, 250 m a piedi">M3 Montenapoleone, 250 m on foot</p></div>
      <div>{t("Parking", "Parcheggio", tag="p", cls="label")}<p>Autosilo San Fedele</p></div>
      <div>{t("Opening hours", "Orari", tag="p", cls="label")}<div class="hours">{t("Every day", "Tutti i giorni")}<span></span>{t("Lunch", "Pranzo")}<span>12:00 – 15:00</span>{t("Dinner", "Cena")}<span>19:00 – 23:00</span></div></div>
    </div>
  </div>
</section>"""

PAGES = [
    ("index.html", "DeRos Restaurant", "Seafood restaurant in Milan at Via Romagnosi 4, next to La Scala and a few minutes' walk from Via Montenapoleone. Raw bar, daily catch, Italian wines.", HOME),
    ("menu.html", "Menu · DeRos", "The DeRos menu: raw bar, crudo, pasta, daily catch priced by weight, pre-theatre menu. Seafood in central Milan, near La Scala and Via Montenapoleone.", MENU),
    ("restaurant.html", "Restaurant · DeRos", "DeRos, a seafood restaurant between Piazza della Scala and the Montenapoleone fashion district: our story, sourcing and chef.", RESTAURANT),
    ("private-dining.html", "Private dining · DeRos", "Private dinners and corporate events at DeRos, Milan, near La Scala and Via Montenapoleone.", EVENTS),
    ("visit.html", "Visit · DeRos", "Book a table at DeRos, Via Romagnosi 4, Milan: next to La Scala, metro M3 Montenapoleone 250 m.", VISIT),
]

from ru import RU
import re
MISSING = set()
def add_ru(doc):
    def sub(m):
        en = html.unescape(m.group(3))
        ru = RU.get(en) or RU_EXTRA.get(en)
        if 'data-ru=' in m.group(2): return m.group(0)
        if ru is None:
            MISSING.add(en); return m.group(0)
        return f'{m.group(1)} data-ru="{html.escape(ru, quote=True)}"{m.group(2)}>{m.group(3)}<'
    return re.sub(r'(data-it="[^"]*")([^>]*)>([^<]*)<', sub, doc)

os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
for name in ("site.css", "site.js"):
    open(os.path.join(OUT, "assets", name), "w").write(open(os.path.join(SRC, name)).read())
for fname, title, desc, main in PAGES:
    body = header(fname) + f'\n<main id="main">\n{main}\n</main>\n' + FOOTER
    body = add_ru(body).replace('href="visit.html#book"', 'href="https://www.sevenrooms.com/reservations/ristorantederos" target="_blank" rel="noopener"')
    full = f'<!doctype html>\n<html lang="en">\n<head>\n{head(title, desc)}\n</head>\n<body>\n{body}\n</body>\n</html>\n'
    open(os.path.join(OUT, fname), "w").write(full)
    if fname == "index.html":
        open(os.path.join(OUT, "artifact-index.html"), "w").write(head(title, desc) + "\n" + body + "\n")
print("built", [p[0] for p in PAGES]); print("missing RU:", MISSING)
