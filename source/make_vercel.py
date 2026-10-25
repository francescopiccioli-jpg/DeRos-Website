"""Turns out/ into out-vercel/: a light copy for the Vercel preview.
Photos load from Unsplash's CDN, the logo from one shared SVG file, and search engines are kept out."""
import os, re, json, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC, DST = os.path.join(ROOT, "out"), os.path.join(ROOT, "out-vercel")
UNSPLASH = {
    "hero": "photo-1776993298453-b4d53a7a040f?w=1600&h=1000&fit=crop",
    "rawbar": "photo-1633321094192-388268512e0f?w=1400&h=800&fit=crop",
    "dish-lobster": "photo-1498603273107-62080b9e4963?w=720&h=960&fit=crop",
    "dish-tuna": "photo-1777897371931-af00228044d9?w=720&h=960&fit=crop",
    "dish-risotto": "photo-1778104682785-b4447364e25a?w=720&h=960&fit=crop",
    "catch": "photo-1615141982883-c7ad0e69fd62?w=880&h=1100&fit=crop",
    "chef-pass": "photo-1775513153018-0c7ac7899751?w=880&h=1100&fit=crop",
    "chef-portrait": "photo-1775498053538-ec293e32b963?w=880&h=1100&fit=crop",
    "private": "photo-1776848517525-ccc3a43bfcfb?w=1600&h=900&fit=crop",
    "restaurant-head": "photo-1776993298422-5b7df704c2c1?w=1600&h=800&fit=crop",
    "visit-head": "photo-1654373728532-612d2042b6f9?w=1600&h=800&fit=crop",
    "events-head": "photo-1761116189895-9fa9541520d7?w=1600&h=800&fit=crop",
}
shutil.rmtree(DST, ignore_errors=True)
os.makedirs(os.path.join(DST, "assets"))
logo = None
for name in ["index.html", "menu.html", "restaurant.html", "private-dining.html", "visit.html"]:
    s = open(os.path.join(SRC, name)).read()
    m = re.search(r'<svg width="0" height="0" style="position:absolute" aria-hidden="true">(.*?)</svg>', s, re.S)
    if m and logo is None:
        logo = m.group(1)
    s = s.replace(m.group(0), "") if m else s
    s = s.replace('<use href="#logo"/>', '<use href="assets/logo.svg#logo"/>')
    s = s.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '')
    s = s.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n<meta name="robots" content="noindex, nofollow">', 1)
    s = re.sub(r'assets/img/([a-z-]+)\.webp', lambda k: "https://images.unsplash.com/" + UNSPLASH[k.group(1)] + "&q=70&auto=format", s)
    open(os.path.join(DST, name), "w").write(s)
open(os.path.join(DST, "assets", "logo.svg"), "w").write('<svg xmlns="http://www.w3.org/2000/svg">' + logo + '</svg>')
for f in ["site.css", "site.js"]:
    shutil.copy(os.path.join(SRC, "assets", f), os.path.join(DST, "assets", f))
open(os.path.join(DST, "robots.txt"), "w").write("User-agent: *\nDisallow: /\n")
open(os.path.join(DST, "vercel.json"), "w").write(json.dumps({"headers": [{"source": "/(.*)", "headers": [{"key": "X-Robots-Tag", "value": "noindex, nofollow"}]}]}, indent=2) + "\n")
for root, _, files in os.walk(DST):
    for f in files:
        p = os.path.join(root, f)
        print(os.path.relpath(p, DST), os.path.getsize(p))
