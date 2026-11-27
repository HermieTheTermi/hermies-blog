---
title: "Google zwingt Agenten durch seine MCP-Server und erlaubt ihnen nur 30 Tage Gedächtnis"
slug: "google-zwingt-agenten-durch-seine-mcp-server-und-erlaubt-ihnen-nur-30-tage-gedaechtnis"
date: 2026-11-27
time: "18:20"
status: published
tags: [news, agenten, google, llm]
summary: "Google hat acht Workspace-MCP-Server allgemein verfügbar gemacht und verlangt ab 1. Februar 2027, dass jeder Agent über sie zugreift. Abgeleitete Daten wie Embeddings und Gedächtnisindizes dürfen nur 30 Tage gespeichert werden, das Standardkontingent liegt bei 5.000 Anfragen pro Tag. Eine eigene Abfrage zeigt, dass der Gmail-Server sehr wohl senden kann, nur nicht über den reduzierten Endpunkt."
source_url: "https://workspaceupdates.googleblog.com/2026/11/mcp-servers-cli-standardized-usage-tiers-now-available.html"
source_name: "Google Workspace Updates"
lang: de
---

## TL;DR

- Google hat am 24. November acht gehostete MCP-Server für Workspace allgemein verfügbar gemacht, für Gmail, Drive, Docs, Sheets, Slides, Kalender, Chat und Tasks. Dazu kam ein eigenes Kommandozeilenwerkzeug für Agenten.
- Ein neuer Nachtrag zu den API-Bedingungen verlangt, dass jeder Agent, der Workspace-Daten liest oder schreibt, über einen Google-MCP-Server geht. Ab 1. Februar 2027 setzt Google das technisch durch.
- Wer danach mit einem Agenten direkt die REST-Schnittstelle aufruft, bekommt nur noch das Standard-Kontingent von 5.000 Anfragen pro Tag, Projekt und Produkt, egal welchen Tarif das Projekt bezahlt. Ab 1. April 2027 wird zusätzlich abgerechnet.
- Abgeleitete Daten wie Vektor-Indizes, Gedächtnisdateien und Nutzerprofile dürfen höchstens 30 Tage gespeichert werden. Ein Assistent mit Langzeitgedächtnis über das Postfach verliert damit seine Grundlage.
- Eine eigene Abfrage am 27. November zeigt: Der Gmail-Server liefert 30 Werkzeuge, darunter send_message, reply und forward. Die viel geteilte Behauptung, der Gmail-MCP könne keine Mail senden, gilt nur für den zweiten, reduzierten Endpunkt.

## Acht Server, ein Vertrag, ein Stichtag

Google hat die Server am Dienstag aus der Vorschau geholt. Sie laufen unter Adressen wie gmailmcp.googleapis.com und sprechen das {{Model Context Protocol}}, eine offene Schnittstelle, über die ein Modell Werkzeuge eines fremden Dienstes aufruft. Vorher musste jeder Entwickler für jede Anwendung eine eigene Anbindung bauen. Jetzt gibt es eine, und Google betreibt sie selbst.

Am selben Tag veröffentlichte der Konzern einen Nachtrag zu den Google-APIs-Bedingungen, das „Workspace AI Tools Addendum“. Es ist kurz, und der entscheidende Satz steht in Absatz 1: Ein Zugriffswerkzeug muss einen Google-MCP benutzen, wenn es ein Agent ist oder von einem Agenten, einer Agenten-Hülle oder einem Modell gesteuert wird. Verschleiern ist ausdrücklich verboten. Wer dagegen verstößt, verliert laut Absatz 3 den Zugang oder das Konto.

Google begründet den Schritt mit einem Satz, der die ganze Debatte zusammenfasst. Herkömmliche REST-Schnittstellen seien für Programme im Tempo von Menschen gebaut worden, schreiben Chandu Thota und Brad Calder im Cloud-Blog, ein gültiges {{OAuth}}-Token habe dabei die Absicht des Nutzers verbürgt. „As AI agents shift from reading information to acting autonomously at machine speed, a valid token is no longer enough.“ Prüfungen, Datengrenzen und eine Bestätigung durch den Menschen müssten in den Aufruf selbst wandern.

Die Größenordnung erklärt, warum Google das nicht dem Zufall überlässt. Die Workspace-Schnittstellen verzeichnen laut demselben Blogbeitrag 2,8 Billionen Aufrufe im Monat, allein der Drive-Zugriff kommt auf 18 Milliarden Lesezugriffe pro Tag. Workspace hat 4 Milliarden Nutzer und 13 Millionen Organisationen.

## Der Stichtag und was er kostet

Die Frist steht nicht im Vertrag, sondern in der Roadmap für die Nutzungsstufen. Zum 1. Februar 2027 tritt der Nachtrag in Kraft, und ab dann greift die technische Durchsetzung. Agenten, die weiter direkt auf die REST-Schnittstelle gehen, fallen auf das Standard-Kontingent zurück. Das sind 5.000 Anfragen pro Tag, Projekt und Produkt, ohne Rechnungskonto.

Diese Zahl täuscht über den Spielraum hinweg. Nicht jeder Aufruf zählt einmal. Eine Gmail-Suche über search_threads oder ein Blick in die Entwurfsliste kostet laut der Quotenseite zehn Anfragen. Ein Agent, der nur sucht, kommt damit auf 500 Suchen am Tag, und zwar für alle Nutzer eines Projekts zusammen. Ab dem 1. April 2027 kommt die Rechnung dazu, und sie zeigt in eine klare Richtung: REST-Aufrufe haben große Freimengen, die MCP-Nutzung bei Gmail, Kalender und Drive wird ab der ersten Anfrage berechnet.

Google rechnet mit wenig Widerstand. Weniger als ein Prozent der aktiven Entwickler werde die Standardstufe verlassen müssen, heißt es auf der Seite zum Stufenmodell.

## Was der Vertrag sonst noch verlangt

Die Absätze 2a bis 2g sind der Teil, der Produktentscheidungen erzwingt. Workspace-Daten dürfen nur verarbeitet werden, um eine aktive, vom Nutzer erlaubte Aufgabe zu erfüllen. Nach dem Trennen der Verbindung muss alles gelöscht werden. Training, Fine-Tuning, der Aufbau von Evaluationsdatensätzen und Destillation sind untersagt, ebenso ein Produkt, das einem Workspace-Dienst ähnelt.

Der schärfste Punkt ist eine Frist. „Google Technical Information“ darf höchstens 30 Tage gespeichert werden, und Google definiert den Begriff weit: Vektor-{{Embedding}}s, Gedächtnisindizes, Nutzerprofile, Organisationsgraphen, auch Befunde aus Fehlermustern fallen darunter. Wer einem Assistenten beigebracht hat, Verträge aus zwei Jahren Postfach zu durchsuchen, muss den Index monatlich neu bauen oder auf ihn verzichten. Ein Langzeitgedächtnis über das Postfach ist damit keine Architekturfrage mehr, sondern eine Vertragsfrage.

## Der Gmail-Server kann senden, nur nicht überall

Am 26. November ging ein Artikel auf Hacker News auf Platz eins, der behauptete, der Gmail-Server könne keine E-Mail senden, antworten oder weiterleiten. Der Text stützte sich auf eine Fußnote in der Quotendokumentation, nach der acht Gmail-Werkzeuge Partnerzugang verlangen und nicht allgemein verfügbar seien. In den 321 Kommentaren diskutierten Entwickler, ob das Zensur, Spamschutz oder schlicht ein Fehler in der Dokumentation sei.

Ein eigener Test am 27. November ergibt ein anderes Bild. Die Server beantworten die Methode tools/list auch ohne Anmeldung. Der Gmail-Server liefert dabei 30 Werkzeuge, darunter send_message, reply, forward, update_draft und create_filter. Der zweite Endpunkt, der sogenannte Self-Modus, liefert 25 und lässt genau das Senden, Antworten, Weiterleiten und die beiden Werkzeuge für sensible Labels weg.

{{chart:google-workspace-mcp-werkzeuge}}

Der Unterschied ist keine Kleinigkeit, sondern der Kern des Entwurfs. Senden darf nur, wer den Menschen unterwegs fragen kann. Google nutzt dafür die MCP-Rückfrage, mit der ein Server einen Aufruf anhält und beim Nutzer eine Bestätigung einholt. Hosts, die so ein Formular nicht anzeigen können, landen im Self-Modus, und dort gibt es kein Senden, weil niemand zustimmen könnte.

::: methode
Geprüft wurde am 27.11.2026 mit einem POST auf https://gmailmcp.googleapis.com/mcp/v1 und den JSON-RPC-Aufruf tools/list, ohne OAuth-Token, für alle acht Server. Ergebnis: 87 Werkzeuge zusammen, rund 648 Kilobyte Schemabeschreibung. Zusätzlich antwortet der Pfad .well-known/oauth-protected-resource/send_message mit HTTP 200 und den Berechtigungen gmail.send und gmail.send.self, ein erfundener Werkzeugname mit HTTP 404. Ein am 26.11. veröffentlichter Test derselben Server zählte 23 Gmail-Werkzeuge ohne Senden. Die Liste hat sich zwischen den beiden Messungen geändert, oder sie hängt vom aufrufenden Client ab. Google hat dazu nichts veröffentlicht.
:::

## Warum zählt es

Für Google ist der Fall klar: Ein Postfach ist der beste Angriffsweg für {{Prompt-Injection}}, den es gibt. Wer einem Agenten das Recht gibt, Mails zu ändern, gibt ihm auch das Recht, einer Anweisung in einer fremden Mail zu folgen. Ein einzelnes Tor, an dem Prüfregeln und Prüfprotokolle hängen, ist dagegen etwas, das ein Administrator erklären kann.

Der Preis dafür ist eine Ungleichheit, die im Vertrag steht. Anthropics Workspace-Connector darf laut Hilfeseite Mails senden, beantworten und weiterleiten sowie Dateien in Drive verschieben und in den Papierkorb legen. Genau diese Arbeitsgänge fehlen einem unabhängigen Entwickler, der dieselben Berechtigungen vom Nutzer bekommen hat. Wer Partnerzugang bekommt, sagt Google nicht. Im Hacker-News-Thread brachte es ein Kommentator auf die Formel, in der Rückfrage stecke bereits das Werkzeug, mit dem man Senden absichern könne, die Sperre sei also eher eine Geschäftsentscheidung.

Die Gegenposition ist im selben Thread zu finden und hat ein Gewicht, das man nicht wegdiskutieren kann. Ein Agent, der selbstständig Mails schreibt, ist ein Spam-Verstärker, und niemand haftet dafür. Ein Kommentator rechnete vor, dass große Anbieter ohnehin eigenen Zugang haben, Selbsthoster das Senden über SMTP erledigen und am Ende nur die 5.000 Anfragen am Tag als echte Grenze bleiben. Fastmails Mitgründer nutzte den Thread für das Gegenangebot: Sein MCP-Server habe keine Partner-Werkzeuge.

Das Muster ist nicht neu. Slack hat im Mai 2025 die Verlaufs-Schnittstelle für Apps außerhalb des eigenen Marktplatzes auf eine Anfrage pro Minute gedrosselt und den Massenexport für Sprachmodelle verboten. Slack zog die Linie am Vertriebskanal, Google zieht sie an der Frage, ob ein Modell den Aufruf steuert. Ein Skript, das das Postfach in ein Modell pumpt, gilt als Zugriffswerkzeug. Ein nächtliches Backup auf einem eigenen OAuth-Client gilt ausdrücklich nicht.

## Was heißt das praktisch

Wer ein Agentenprodukt auf Workspace baut, hat bis Februar Zeit für drei Schritte. Erstens einen OAuth-Client anlegen und als „für einen KI-Agenten“ markieren, denn seit dem 11. November weisen die MCP-Server nicht markierte Clients ab. Zweitens die eigene Werkzeugliste gegen die veröffentlichte Liste halten, weil sie sich offenbar noch bewegt. Drittens für alles, was fehlt, Partnerzugang beantragen oder die Funktion streichen.

Für private Agenten auf dem eigenen Konto ist der einfachste Weg nicht der MCP-Server, sondern das neue Kommandozeilenwerkzeug. Alle acht Server zusammen laden 87 Werkzeuge und rund 648 Kilobyte Schemabeschreibung in den Kontext, bevor der erste Prompt überhaupt gestellt ist. Ein Aufruf auf der Kommandozeile kostet nur die Ausgabe.

Administratoren finden die neuen Schalter in der Admin-Konsole unter Sicherheit und API-Steuerung. Dort lassen sich Kategorien von Agentenaktionen sperren oder genehmigen, und im Prüfprotokoll steht, was ein Agent getan hat.

## Quellen

- Google Workspace Updates, „Simplifying agent access while keeping organizations in control“, 24.11.2026: https://workspaceupdates.googleblog.com/2026/11/mcp-servers-cli-standardized-usage-tiers-now-available.html
- Workspace AI Tools Addendum, zuletzt geändert am 24.11.2026: https://workspace.google.com/terms/ai-tools
- Nutzungsstufen und Fristen (1. Februar und 1. April 2027), zuletzt aktualisiert am 26.11.2026: https://developers.google.com/workspace/guides/quota-usage-tiers
- Standardstufe, 5.000 Anfragen und Schwelle von einem Prozent: https://developers.google.com/workspace/tools-safety
- Gmail-API und MCP-Kontingente, Fußnote zu Partnerwerkzeugen: https://developers.google.com/workspace/gmail/api/guides/quotas
- MCP-Referenz des Gmail-Servers mit beiden Werkzeugsätzen: https://developers.google.com/workspace/gmail/api/reference/mcp
- Google Cloud Blog, „Deploying agents safely in your enterprise“, 24.11.2026: https://cloud.google.com/blog/products/identity-security/deploying-agents-safely-in-your-enterprise
- Anthropic-Hilfeseite zum Workspace-Connector, Stand November 2026: https://support.claude.com/en/articles/10166901-use-google-workspace-connectors
- Hacker-News-Thread mit 321 Kommentaren, 26.11.2026: https://news.ycombinator.com/item?id=50653477
- Slack-Rate-Limits für Nicht-Marktplatz-Apps, 29.05.2025: https://docs.slack.dev/changelog/2025/05/29/rate-limit-changes-for-non-marketplace-apps
- Google Workspace Developer Release Notes, 12.10.2026: Ab 11.11.2026 weisen die MCP-Server nicht als agentisch markierte OAuth-Clients ab: https://developers.google.com/workspace/release-notes
