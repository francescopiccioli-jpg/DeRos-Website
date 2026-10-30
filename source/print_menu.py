"""Printable DeRos menus, one PDF per language (A4, logo on every page)."""
import os, re, sys, html, asyncio
from menu_data import *

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "print")
FONTS = os.path.abspath(os.path.join(HERE, "..", "..", "fonts"))
os.makedirs(OUT, exist_ok=True)

logo_src = open(os.path.join(HERE, "..", "out-vercel", "assets", "logo.svg")).read()
inner = re.search(r'<symbol id="logo" viewBox="([^"]+)">(.*?)</symbol>', logo_src, re.S)
LOGO = f'<svg class="logo" viewBox="{inner.group(1)}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="DeRos">{inner.group(2)}</svg>'

FONT_CSS = ""
for fam, pkg, ws in [("Spectral", "fontsource-spectral-5.1.1", [300, 400]), ("Manrope", "fontsource-manrope-5.1.1", [400, 500, 600])]:
    for w in ws:
        for sub, rng in [("latin", "U+0000-00FF,U+0131,U+0152-0153,U+02C6,U+02DA,U+02DC,U+2000-206F,U+20AC,U+2122,U+2212"),
                         ("latin-ext", "U+0100-02AF,U+0304,U+0308,U+0329,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF"),
                         ("cyrillic", "U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116")]:
            f = f"{FONTS}/{pkg}/files/{fam.lower()}-{sub}-{w}-normal.woff2"
            if os.path.exists(f):
                FONT_CSS += f"@font-face{{font-family:'{fam}';font-weight:{w};src:url('file://{f}') format('woff2');unicode-range:{rng}}}\n"

CSS = FONT_CSS + """
@page { size: A4; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: 'Manrope', sans-serif; color: #1D1A52; background: #fff; }
.page { width: 210mm; height: 297mm; padding: 16mm 22mm 14mm; position: relative; display: flex; flex-direction: column; page-break-after: always; overflow: hidden; }
.page:last-child { page-break-after: auto; }
.page::before { content: ""; position: absolute; inset: 7mm; border: 0.4pt solid rgba(29,26,82,.28); pointer-events: none; }
.top { display: flex; justify-content: center; margin-bottom: 9mm; }
.top .logo { width: 30mm; height: auto; color: #1D1A52; }
.body { flex: 1; }
h1 { font-family: 'Spectral', serif; font-weight: 300; font-size: 32pt; letter-spacing: .01em; text-align: center; }
.rule { width: 18mm; height: 0.6pt; background: #2C5A70; margin: 4mm auto 10mm; }
.item { display: grid; grid-template-columns: 1fr auto; column-gap: 8mm; margin-bottom: 8.5mm; break-inside: avoid; }
.item h3 { font-family: 'Spectral', serif; font-weight: 400; font-size: 15pt; line-height: 1.25; }
.item .price { font-family: 'Spectral', serif; font-size: 14pt; white-space: nowrap; }
.item p { grid-column: 1 / 2; font-size: 10pt; line-height: 1.55; color: #5B5978; margin-top: 1.6mm; max-width: 125mm; }
.item .al { font-size: 8pt; letter-spacing: .04em; color: #2C5A70; margin-left: 1.5mm; white-space: nowrap; }
.dessert { margin-bottom: 12mm; break-inside: avoid; }
.dessert > .item { margin-bottom: 3.5mm; }
.pair-label { font-size: 7.4pt; letter-spacing: .2em; text-transform: uppercase; color: #2C5A70; margin: 0 0 3mm; padding-top: 2.5mm; border-top: 0.4pt solid rgba(44,90,112,.45); }
.pair .item { margin-bottom: 3.5mm; padding-left: 5mm; }
.pair .item h3 { font-size: 12.5pt; } .pair .item .price { font-size: 12pt; } .pair .item p { font-size: 9.2pt; }
.foot { display: flex; justify-content: space-between; font-size: 7pt; letter-spacing: .18em; text-transform: uppercase; color: #5B5978; }
/* cover */
.cover .top { display: none; }
.cover .body { display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; gap: 7mm; }
.cover .logo { width: 82mm; height: auto; color: #1D1A52; }
.cover .kicker { font-size: 8.5pt; letter-spacing: .32em; text-transform: uppercase; color: #2C5A70; }
.cover h1 { font-size: 24pt; margin-top: 8mm; }
.cover .intro { font-family: 'Spectral', serif; font-weight: 300; font-size: 13pt; line-height: 1.55; max-width: 120mm; }
.cover .tag { font-size: 8pt; letter-spacing: .28em; text-transform: uppercase; color: #2C5A70; margin-top: 4mm; }
/* allergens */
.allergens .note { text-align: center; font-weight: 600; font-size: 9.5pt; margin-bottom: 4mm; }
.allergens .legal, .allergens .ask { font-size: 9pt; line-height: 1.5; color: #5B5978; margin-bottom: 4mm; }
.allergens ol { list-style: none; columns: 2; column-gap: 9mm; margin: 2mm 0 5mm; }
.allergens li { display: grid; grid-template-columns: 7mm 1fr; font-size: 9pt; line-height: 1.45; margin-bottom: 2.2mm; break-inside: avoid; }
.allergens li b { color: #2C5A70; font-weight: 600; }
.allergens .thanks { text-align: center; font-family: 'Spectral', serif; font-size: 11pt; margin-top: 6mm; }
"""

def e(s): return html.escape(s)

def item_html(it, lang):
    name, desc = it[lang], it["d" + lang]
    al = f'<span class="al">({it["al"]})</span>' if it["al"] else ""
    p = f"<p>{e(desc)}</p>" if desc else ""
    return f'<div class="item"><h3>{e(name)}{al}</h3><span class="price">{price(it["price"], lang, it["unit"])}</span>{p}</div>'

def page(lang, n, total, title, inner, cls=""):
    foot = f'<div class="foot"><span>DeRos · Via Romagnosi 4, Milano</span><span>{n} / {total}</span></div>'
    head = f'<h1>{e(title)}</h1><div class="rule"></div>' if title else ""
    return f'<section class="page {cls}"><div class="top">{LOGO}</div><div class="body">{head}{inner}</div>{foot}</section>'

def build(lang):
    pages = []
    cover = f'''{LOGO}<p class="kicker">Seafood restaurant · Milano</p><h1>{e(OUR_MENU[lang])}</h1><div class="rule" style="margin:0 auto"></div>
      <p class="intro">{e(INTRO[lang])}</p><p class="tag">{e(TAGLINE[lang])}</p>'''
    pages.append(("", cover, "cover"))
    for key, title, items in FOOD:
        pages.append((title[lang], "".join(item_html(i, lang) for i in items), ""))
    for chunk in (DESSERTS[:2], DESSERTS[2:]):
        inner = ""
        for d, pairs in chunk:
            inner += f'<div class="dessert">{item_html(d, lang)}<p class="pair-label">{e(PAIRINGS[lang])}</p><div class="pair">{"".join(item_html(p, lang) for p in pairs)}</div></div>'
        pages.append((DESSERT_TITLE[lang], inner, ""))
    pages.append((DRINKS[1][lang], "".join(item_html(i, lang) for i in DRINKS[2]), ""))
    li = "".join(f"<li><b>{k}</b><span>{e(a[{'it':0,'en':1,'ru':2}[lang]])}</span></li>" for k, a in enumerate(ALLERGENS, 1))
    alg = f'''<p class="note">{e(ALLERGEN_NOTE[lang])}</p><p class="legal">{e(ALLERGEN_LEGAL[lang])}</p><ol>{li}</ol>
      <p class="ask">{e(ALLERGEN_ASK[lang])}</p><p class="thanks">{e(THANKS[lang])}</p>'''
    pages.append((ALLERGEN_TITLE[lang], alg, "allergens"))
    total = len(pages)
    body = "".join(page(lang, i + 1, total, t, inner, c) for i, (t, inner, c) in enumerate(pages))
    return f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'

async def render():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for lang in ("it", "en", "ru"):
            path = os.path.join(OUT, f"menu-deros-{lang}.html")
            open(path, "w").write(build(lang))
            pg = await b.new_page()
            await pg.goto("file://" + path); await pg.evaluate("document.fonts.ready")
            over = await pg.evaluate("""[...document.querySelectorAll('.page')].map((p,i)=>{const b=p.querySelector('.body');return b.scrollHeight>b.clientHeight+1?i+1:null}).filter(Boolean)""")
            await pg.pdf(path=os.path.join(OUT, f"menu-deros-{lang}.pdf"), format="A4", print_background=True, prefer_css_page_size=True)
            print(lang, "overflow pages:", over)
            await pg.close()
        await b.close()

asyncio.run(render())
