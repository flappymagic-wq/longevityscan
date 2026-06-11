# Cover-Snippet System — Anleitung für neue Artikel

Ab sofort gehört zu jedem neuen Artikel ein SVG-Cover. Das ist ein Inline-SVG
(keine Bilddatei, kein zusätzlicher Request, keine Ladezeit) und wird in die
Artikelkarte auf `index.html` und `blog.html` eingesetzt — genau dort, wo bisher
das Emoji stand.

Damit erweitert sich das bekannte Vier-Dateien-Deployment NICHT um eine neue Datei,
aber um einen neuen Schritt: **Cover-Motiv wählen + Karte mit Cover bauen.**

---

## 1. Motiv wählen

Jede Kategorie hat ein festes Motiv und eine feste Akzentfarbe. Nimm das passende:

| Thema des Artikels            | Motiv (`motif`) | Farbe (`accent`) | Grund-Look          |
|-------------------------------|-----------------|------------------|---------------------|
| Supplement / Wirkstoff / NMN  | `molecule`      | `g` (grün)       | Molekül-Netz        |
| Studie / Daten / Meta-Analyse | `chart`         | `g` (grün)       | Balken + Kurve      |
| Epigenetik / Gen-Uhr / DNA    | `helix`         | `g` (grün)       | DNA-Doppelhelix     |
| Schlaf / HRV                  | `waves`         | `b` (blau)       | Schlafwellen        |
| Wearable / Ring / Tracker     | `ring`          | `b` oder `g`     | Ring-Form           |
| Biohacking / Training / Zone 2| `pulse`         | `o` (orange)     | Pulslinie / EKG     |
| Routine / Schritt-für-Schritt | `pulse`         | `o` (orange)     | Pulslinie           |
| Protokoll / Blueprint / Liste | `checklist`     | `b` (blau)       | Checkliste          |
| Ernährung / Fasten            | `plate`         | `p` (pink)       | Teller / Uhr        |
| Medikament / GLP-1 / Pille    | `capsule`       | `r` (rot)        | Kapsel              |

Farb-Codes: `g`=grün, `o`=orange, `b`=blau, `p`=pink, `r`=rot.
Die Farbe muss zur `pill-`Klasse und zum bisherigen `acc-`Streifen passen
(grün→pill-g, orange→pill-o, blau→pill-b, pink→pill-p, rot→pill-r).

---

## 2. Cover-SVG erzeugen

Im Projektordner liegt `covers.py`. Erzeugen so:

```bash
python3 -c "import covers; print(covers.cover('molecule','g',label='KREATIN · 1000+ STUDIEN'))"
```

- **erstes Argument** = Motiv aus der Tabelle
- **zweites Argument** = Farb-Code
- **label** = kurzer Text unten links im Cover (Großbuchstaben, knapp, z. B. Keyword + Kennzahl)

Ausgabe ist ein einzeiliger `<svg…>…</svg>`-String. Den kopierst du in die Karte.

---

## 3. Karte bauen

### Für `blog.html` (Artikel-Grid):

```html
<a href="artikel-DEIN-SLUG.html" class="article-card" data-cat="KATEGORIE">
  <div class="card-cover">HIER_DAS_SVG</div>
  <div class="card-inner">
    <div class="card-pill pill-X">Pill-Text ohne Emoji</div>
    <h3 class="card-title">Artikel-Titel</h3>
    <div class="card-excerpt">Kurzbeschreibung.</div>
    <div class="card-meta">DATUM · X Min.</div>
  </div>
</a>
```

### Für `index.html` (Startseiten-Grid):

```html
<a href="artikel-DEIN-SLUG.html" class="card">
  <div class="card-cover">HIER_DAS_SVG</div>
  <div class="card-body">
    <div class="pill pill-X">Pill-Text ohne Emoji</div>
    <h3 class="card-title">Artikel-Titel</h3>
    <div class="card-exc">Kurzbeschreibung.</div>
    <div class="card-meta">DATUM · X Min.</div>
  </div>
</a>
```

`data-cat` (nur blog.html) muss einer der gültigen Werte sein:
`studien, supplements, biohacking, ernaehrung, schlaf, protokoll, epigenetik`.

---

## 4. Pflicht-Regeln (sonst bricht etwas)

1. **Keine Emojis** mehr in Pills oder Titeln — das Cover ist der visuelle Anker.
2. **Titel = `<h3>`** in Karten, **`<h2>`** im Featured-Bereich. Niemals `<div>`.
3. **`data-cat` muss eindeutig pro Kategorie sein** — der alte Bug (alle Buttons
   gleicher data-cat) hat die Counts zerschossen. Bei neuem Artikel prüfen, ob die
   Kategorie-Zählung in Sidebar UND Burger-Menü auf beiden Seiten noch stimmt.
4. **Kategorie-Counts aktualisieren** an vier Stellen, wenn ein Artikel dazukommt:
   - `blog.html` Sidebar `.cat-count`
   - `blog.html` Burger-Menü `.mc-count`
   - `index.html` Sidebar `.cat-row` count
   - `index.html` Burger-Menü `.mc-count`
   - sowie die Artikel-Gesamtzahl in `blog.html` (`.blog-stat-num`)
5. **ItemList-Schema**: neuen Artikel in den `ItemList`-JSON-LD-Block beider Seiten
   mit nächster `position` und voller URL eintragen.
6. **Featured/Spotlight**: Das kommerziell relevanteste oder neueste Stück bleibt
   der Featured-Artikel oben.

---

## 5. Vor dem Deploy testen

- Beide Seiten lokal im Browser öffnen (echtes Chrome/Firefox, nicht nur Preview).
- Desktop: 2-Spalten-Grid sichtbar? Sidebar + Spotlight rechts?
- Mobile (Fenster < 640px): Burger-Menü öffnet Overlay? Filter-Pills umbrechen,
  alle 8 auf einen Blick? Spotlight inline sichtbar?
- Blog-Filter: jede Kategorie anklicken — Counts korrekt, richtige Karten sichtbar?

---

## 6. Produkt-Spotlight wechseln

Das Spotlight-Widget (rechts in Sidebar + inline auf Mobile) ist an EINER Stelle
pro Datei definiert. Zum Wechseln:

1. Neues Produktbild als quadratisches/portrait WebP ~15–25 KB nach
   `spotlight-PRODUKT.webp` exportieren (weißer Hintergrund, Produkt freigestellt).
2. Im Spotlight-Block ersetzen: `src`, `alt`, `sp-name`, `sp-rating`, `sp-desc`
   und den Amazon-Link (`rel="noopener sponsored nofollow"`).
3. Beide Vorkommen pro Datei (Sidebar-Version + Mobile-Version) angleichen.

Aktuelles Spotlight: **Vitamin D3 + K2 MK7 5000 I.E.** (Sunday Natural),
Bild `spotlight-vitamin-d3-k2.webp`, Link `https://amzn.to/49XmiMO`.

---

## Verfügbare Motive (Referenz)

`molecule` · `waves` · `pulse` · `helix` · `checklist` · `chart` · `plate` · `ring` · `capsule`

Alle in `covers.py`. Neue Motive bei Bedarf dort als Funktion ergänzen und in
`MOTIFS` registrieren — gleiche Signatur `def name(accent_code)`, gibt SVG-Body
(ohne `<svg>`-Wrapper) zurück.
