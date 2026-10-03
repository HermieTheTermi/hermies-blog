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
- **Deutsch**, Zeitzone Europe/Berlin, Datum ISO (`YYYY-MM-DD`).

## Dateien

```
blogctl                 # das Interface (ausführbar)
INTERFACE.md            # dieser Vertrag (+ Betriebsregeln)
content/posts/          # veröffentlichte Artikel
content/drafts/         # Entwürfe
content/sources.json    # Quellen für `blogctl scrape`
content/templates/      # Layout der Site (Chunk 2)
assets/                 # Bilder und Dateien
dist/                   # Build-Ausgabe (nicht committen)
```

## CLI

| Befehl | Wirkung | `--json` Rückgabe |
|---|---|---|
| `new --title T [--slug S] [--tags a,b] [--summary S] [--source-url U] [--source-name N] [--date D] [--body-file F]` | legt Entwurf an (Body aus Datei oder stdin, sonst Platzhalter) | `{ok,id,path,status}` |
| `list [--drafts\|--posts] [--limit N]` | Artikel auflisten | `{posts:[{id,title,date,tags,status,summary,source_url}]}` |
| `show ID` | Frontmatter + Body ausgeben | `{ok,id,frontmatter,body}` |
| `edit ID [--title T] [--tags a,b] [--summary S] [--body-file F]` | Felder/Body ändern | `{ok,id,path}` |
| `publish ID [ID…]` | Entwurf → `content/posts/`, `status: published` | `{ok,published:[ids]}` |
| `unpublish ID [ID…]` | zurück nach `content/drafts/` | `{ok,drafts:[ids]}` |
| `rm ID --yes` | löscht Artikel (ohne `--yes`: Abbruch) | `{ok,removed:[]}` |
| `check` | Frontmatter, Pflichtfelder, Duplikate, interne Links | `{ok,errors:[],warnings:[]}` |
| `build [--out dist]` | statische Site bauen | `{ok,out,pages}` |
| `serve [--port 8080]` | Vorschau lokal | – |
| `scrape [--source NAME]` | neue Items aus `content/sources.json` → Entwürfe | `{ok,created:[],skipped:N}` |
| `deploy` | `build` + git commit + push (nur wenn Remote existiert) | `{ok,commit,pushed}` |

## Frontmatter

```yaml
---
title: "Titel des Artikels"
slug: "titel-des-artikels"
date: 2026-10-03
status: draft            # draft | published
tags: [news, ki]
summary: "Ein Satz für Startseite, RSS und Vorschau."
cover: "assets/bild.jpg" # optional
source_url: "https://…"  # optional, bei gescrapten Artikeln Pflicht
source_name: "Beispiel"  # optional
lang: de
---
```

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

`type`: `rss` (Atom/Feed) oder `html` (Seite mit Links). `auto_publish: true` nur für Quellen, denen der Nutzer ausdrücklich vertraut.

## Ablauf für den Agenten (Hermes)

1. `blogctl scrape --json` → neue Entwürfe in `content/drafts/`
2. Entwürfe prüfen: kürzen, einordnen, Tags setzen, Dubletten gegen bestehende Posts abgleichen (`list --json`)
3. `blogctl check`, dann Telegram: kurzer Digest + Vorschläge
4. Auf Freigabe: `blogctl publish <ids>` → `blogctl build` → `blogctl deploy`
5. Nie ohne Freigabe veröffentlichen (Ausnahme: Quelle mit `auto_publish: true`)

## Betriebsregeln (verbindlich)

**Ohne Rückfrage erlaubt:** `new`, `edit`, `check`, `list`, `show`, `build`, `serve` auf Entwürfen; `scrape` auswerten, Entwürfe anlegen, Tags/Summary setzen, Titel kürzen, Fakten prüfen.

**Nur mit ausdrücklicher Freigabe:** `publish` und `unpublish`, `rm`, `deploy` in ein öffentliches Remote, neue Quellen in `content/sources.json`, `auto_publish: true` setzen, Änderungen an bereits veröffentlichten Artikeln über Tippfehler/Format hinaus.

1. Vor jedem `publish` muss `blogctl check` fehlerfrei sein.
2. Jeder gescrapte Artikel braucht `source_url` und `source_name` — keine Quelle, kein Artikel.
3. Keine erfundenen Fakten: was nicht in der Quelle steht, wird nicht behauptet. Unsicher → Entwurf, kein Freigabevorschlag.
4. Vor dem Anlegen Dubletten prüfen (`list --json` gegen Titel und `source_url`).
5. Nur über `blogctl` am Inhalt arbeiten — Dateien nicht direkt umbenennen oder verschieben, sonst driftet der Zustand.
6. `dist/` nicht committen. Commit-Nachricht deutsch, Imperativ, mit Artikel-id.
