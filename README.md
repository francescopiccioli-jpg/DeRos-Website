# DeRos Restaurant — anteprima del sito

Anteprima del nuovo sito di DeRos, Via Romagnosi 4, Milano. Sito statico in inglese, italiano e russo.

- Le pagine pubblicate sono nella cartella principale (`index.html`, `menu.html`, `restaurant.html`, `private-dining.html`, `visit.html`, `assets/`).
- Le foto in `assets/img/` sono indicative (licenza Unsplash) e vanno sostituite con quelle del ristorante.
- Il sito è escluso dai motori di ricerca (`robots.txt`, meta `noindex`, intestazione `X-Robots-Tag` in `vercel.json`). Va tolto il blocco al lancio.
- `source/` contiene gli script che generano le pagine (`python3 build.py`); non viene pubblicata.
