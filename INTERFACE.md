# blog-system — Vertrag zwischen Blog und Agent

Dieses Repo **ist** das CMS. Es gibt genau ein Interface für Mensch und Agent: das CLI `./blogctl`.
Alles, was automatisch passieren soll — Artikel anlegen, News scrapen, veröffentlichen, bauen,
deployen — läuft über diese Befehle. Kein Admin-Panel, keine versteckte Logik.

## Grundregeln

- **Statische Site.** `blogctl build` erzeugt `dist/` (HTML + `feed.xml` + `sitemap.xml`). Keine Server-Runtime, kein Cloud-Dienst zum Bauen.
- **Inhalt ist Wahrheit.** Markdown-Dateien unter `content/`. Jede Zustandsänderung muss als Git-Diff sichtbar sein.
- **Ordner = Status.** `content/drafts/` = Entwurf (nicht live), `content/posts/` = veröffentlicht. Veröffentlichen heißt: Datei verschieben.
- **id == slug** (Dateiname ohne `.md`). Stabil, wird nie automatisch geändert.
- **Exit-Code 0 = ok, 1 = Fehler.** Fehler nach stderr. Mit `--json` kommt ein maschinenlesbares Objekt nach stdout.
- **Läuft offline und ohne Zusatzpakete.** Nur Python-Stdlib, Ziel ist der macOS-System-`python3` (3.9) **und** 3.14 → keine 3.10+-Syntax (`match`, `X | Y` in Annotationen sind tabu). PyYAML darf genutzt werden, wenn vorhanden, ist aber optional.
- **Deutsch**, Zeitzone Europe/Berlin, Datum ISO (`YYYY-MM-DD`), optionale Uhrzeit `HH:MM`.

## Dateien

```
blogctl                 # das Interface (ausführbar)
INTERFACE.md            # dieser Vertrag (+ Betriebsregeln)
content/posts/          # veröffentlichte Artikel
content/drafts/         # Entwürfe
content/lexikon.json    # Datendatei für Fachbegriffe und Tooltips
content/sources.json    # Quellen für `blogctl scrape`
content/templates/      # Layout der Site (Chunk 2)
assets/                 # Bilder und Dateien
tests/                  # Regressionstests (python3 tests/test_time.py, tests/test_lexikon.py)
dist/                   # Build-Ausgabe (nicht committen)
```

`BLOGCTL_ROOT` überschreibt die Repo-Wurzel — nur für Tests gedacht, im Normalbetrieb nicht setzen.

## CLI

| Befehl | Wirkung | `--json` Rückgabe |
|---|---|---|
| `new --title T [--slug S] [--tags a,b] [--summary S] [--source-url U] [--source-name N] [--date D] [--time T] [--body-file F]` | legt Entwurf an (Body aus Datei oder stdin, sonst Platzhalter) | `{ok,id,path,status}` |
| `list [--drafts\|--posts] [--limit N]` | Artikel auflisten | `{posts:[{id,title,date,time,tags,status,summary,source_url}]}` |
| `show ID` | Frontmatter + Body ausgeben | `{ok,id,frontmatter,body}` |
| `edit ID [--title T] [--tags a,b] [--summary S] [--time T] [--body-file F]` | Felder/Body ändern | `{ok,id,path}` |
| `publish ID [ID…]` | Entwurf → `content/posts/`, `status: published` | `{ok,published:[ids]}` |
| `unpublish ID [ID…]` | zurück nach `content/drafts/` | `{ok,drafts:[ids]}` |
| `rm ID --yes` | löscht Artikel (ohne `--yes`: Abbruch) | `{ok,removed:[]}` |
| `check` | Frontmatter, Pflichtfelder, Duplikate, interne Links, Lexikon-Marker | `{ok,errors:[],warnings:[]}` |
| `lexikon [--json]` | Begriffe auflisten (Klartext oder JSON) | `{terms:[{term,slug,text}]}` |
| `build [--out dist]` | statische Site bauen | `{ok,out,pages}` |
| `serve [--port 8080]` | Vorschau lokal | – |
| `scrape [--source NAME] [--per-source N] [--limit N] [--since-days D] [--dry-run]` | neue Items aus `content/sources.json` → Entwürfe (N je Quelle, Gesamtdeckel über `--limit`) | `{ok,created:[],skipped:N,errors:[]}` |
| `deploy` | `build` + git commit + push (nur wenn Remote existiert) | `{ok,commit,pushed}` |

## Frontmatter

```yaml
---
title: "Titel des Artikels"
slug: "titel-des-artikels"
date: 2026-10-03
time: "09:15"            # optional, HH:MM in Europe/Berlin
status: draft            # draft | published
tags: [news, ki]
summary: "Ein Satz für Startseite, RSS und Vorschau."
cover: "assets/bild.jpg" # optional
source_url: "https://…"  # optional, bei gescrapten Artikeln Pflicht
source_name: "Beispiel"  # optional
lang: de
---
```

## Datierung, Anzeige und Sortierung

Artikel werden mit Datum und Uhrzeit des Quell-Zeitpunkts datiert (Aktualität), nicht mit dem Zeitpunkt des Schreibens; ohne Uhrzeitangabe in der Quelle bleibt es beim Tagesdatum.

- **Frontmatter-Feld `time`**: Optionales Feld im Format `HH:MM` (24 h, Europe/Berlin), platziert direkt nach `date`.
- **Anzeige**: Datum wird deutsch gerendert (`04.10.2026` bzw. `04.10.2026, 09:15`). Das Attribut `datetime` im `<time>`-Element bleibt maschinenlesbar (`2026-10-04` bzw. `2026-10-04T09:15+02:00` mit dem Berliner Zeitzonen-Offset).
- **Sortierung**: Startseite, Tag-Seiten, Feed und Sitemap sortieren absteigend nach `(date, time, id)`. Fehlt `time`, sortiert der Artikel wie `00:00`.
- **Feed**: `<pubDate>` im RSS-Feed enthält die Uhrzeit mit korrektem Berliner Zeitzonen-Offset nach RFC 822 (z. B. `Sun, 04 Oct 2026 09:15:00 +0200` im Sommer bzw. `+0100` im Winter; ohne Uhrzeit `00:00:00`).

## Lexikon, Popover und Fachbegriffe

Fachbegriffe können in Artikeln und Seiten mit dem Marker `{{Begriff}}` referenziert werden. Die Erklärungen liegen zentral in `content/lexikon.json`.

- **Markup & Popover-API**: Beim Build erzeugt jedes Vorkommen einen semantischen Button und ein natives Popover-Element:
  ```html
  <button type="button" class="lex" popovertarget="lex-<slug>" data-tip="…">Begriff</button>
  <span class="lex-pop" popover id="lex-<slug>"><strong>Begriff</strong> Erklärung … <a href="lexikon.html#<slug>">Im Lexikon</a></span>
  ```
- **Kein JavaScript, Popover-API**: Vollständig nativ ohne `<script>` und ohne externe Ressourcen. Das Attribut `popover` bietet automatisches Light-Dismiss (Klick daneben oder Escape schließt; nur ein Popup gleichzeitig).
- **Eindeutige IDs**: Pro Dokument werden IDs deterministisch gezählt (`lex-<slug>`, `lex-<slug>-2`, `lex-<slug>-3` …). `popovertarget` verweist exakt auf die ID des zugehörigen Popovers.
- **Anzeige & Responsivität**: Auf Desktop zeigt Überfahren einen Tooltip (`data-tip`), solange das Popover geschlossen ist (`.lex:has(+ .lex-pop:popover-open)::after { display: none; }`). Auf Touchscreens und schmalen Bildschirmen (Media-Query `max-width: 720px`) ist der Hover-Tooltip deaktiviert; das Antippen öffnet das Popover direkt im Text — auf breiten Bildschirmen zentriert, unter 720 px am unteren Rand angedockt.
- **Fallback**: Browser ohne Popover-Unterstützung blenden `.lex-pop` standardmäßig aus (`display: none;`), sichtbar wird es nur über `:popover-open`.
- **Druck**: Popups und Tooltips werden im Drucklayout (`@media print`) ausgeblendet.
- **Navigation**: Header- und Footer-Navigation enthalten Links auf `lexikon.html` sowie `tag/news.html` und `tag/brainstorming.html` (im Header direkt nach „Start").
- **Validierung**: `blogctl check` verifiziert, dass jeder verwendete Marker in `content/lexikon.json` definiert ist (Marker in Backtick-Code wie `{{Begriff}}` werden ignoriert).

## Quellen (`content/sources.json`)

```json
{
  "settings": { "max_items_per_run": 10, "auto_publish": false },
  "sources": [
    { "name": "Beispiel", "type": "rss", "url": "https://example.com/feed.xml",
      "tags": ["news"], "auto_publish": false, "enabled": false }
  ]
}
```

`type`: `rss` (verarbeitet RSS 2.0 **und** Atom — auch bei Atom-Feeds `rss` eintragen, `atom` ist kein gültiger Wert) oder `html` (Seite ohne Feed, Links werden extrahiert). `auto_publish: true` nur für Quellen, denen der Nutzer ausdrücklich vertraut.

## Ablauf für den Agenten (Hermes)

1. `blogctl scrape --json` → neue Entwürfe in `content/drafts/`
2. Entwürfe prüfen: kürzen, einordnen, Tags setzen, Dubletten gegen bestehende Posts abgleichen (`list --json`)
3. `blogctl check`, dann Telegram: kurzer Digest + Vorschläge
4. Auf Freigabe: `blogctl publish <ids>` → `blogctl build` → `blogctl deploy`
5. Nie ohne Freigabe veröffentlichen (Ausnahme: Quelle mit `auto_publish: true`)

## Betriebsregeln (verbindlich)

**Ohne Rückfrage erlaubt:** `new`, `edit`, `check`, `list`, `show`, `build`, `serve`, `lexikon` auf Entwürfen; `scrape` auswerten, Entwürfe anlegen, Tags/Summary setzen, Titel kürzen, Fakten prüfen.

**Nur mit ausdrücklicher Freigabe:** `publish` und `unpublish`, `rm`, `deploy` in ein öffentliches Remote, neue Quellen in `content/sources.json`, `auto_publish: true` setzen, Änderungen an bereits veröffentlichten Artikeln über Tippfehler/Format hinaus.

1. Vor jedem `publish` muss `blogctl check` fehlerfrei sein.
2. Jeder gescrapte Artikel braucht `source_url` und `source_name` — keine Quelle, kein Artikel.
3. Keine erfundenen Fakten: was nicht in der Quelle steht, wird nicht behauptet. Unsicher → Entwurf, kein Freigabevorschlag.
4. Vor dem Anlegen Dubletten prüfen (`list --json` gegen Titel und `source_url`).
5. Nur über `blogctl` am Inhalt arbeiten — Dateien nicht direkt umbenennen oder verschieben, sonst driftet der Zustand.
6. `dist/` nicht committen. Commit-Nachricht deutsch, Imperativ, mit Artikel-id.
