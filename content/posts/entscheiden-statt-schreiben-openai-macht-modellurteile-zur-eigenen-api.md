---
title: "Entscheiden statt schreiben: OpenAI macht Modellurteile zur eigenen API"
slug: "entscheiden-statt-schreiben-openai-macht-modellurteile-zur-eigenen-api"
date: 2026-10-22
time: "21:00"
status: published
tags: [news, modelle, agenten, openai]
summary: "OpenAI hat die Decisions API allgemein verfügbar gemacht: Das Modell antwortet nicht mit Text, sondern mit einer Wahrscheinlichkeit, einer Auswahl aus vorgegebenen Optionen oder einem Punktwert. Basis ist GPT-6 Luna, laut OpenAI bis zu zehnmal schneller als über die normale API; 0,10 Dollar pro Million Eingabe-Token, gecacht 0,01 Dollar. Die Kundenzahlen zu Tempo und Kosten sind Herstellerangaben, unabhängig nachgeprüft ist nichts."
source_url: "https://openai.com/index/decisions-api"
source_name: "OpenAI"
lang: de
---

## TL;DR

- OpenAI hat die **Decisions API** allgemein verfügbar gemacht (22.10.2026): Das Modell antwortet nicht mit Text, sondern mit einer **Wahrscheinlichkeit, einer Auswahl aus vorgegebenen Optionen oder einem Punktwert**.
- Grundlage ist **GPT-6 Luna**; laut OpenAI bis zu **zehnmal schneller** als dasselbe Modell über die normale Responses-API. Pro Anfrage sind bis zu **400 Fragen** möglich, mit Text, Bildern und JSON als Eingabe.
- Der Preis: **0,10 Dollar pro Million {{Token}}** an Eingabe, gecacht 0,01 Dollar. Ausgabe-Token kosten nichts, weil es keine Ausgabe im Textsinne gibt.
- Kunden nennen eigene Zahlen: Datadog **40-mal schneller** bei den langsamsten fünf Prozent der Antworten, Sierra unter **280 Millisekunden** bei drei Mal schneller und 90 Prozent geringeren Kosten pro Aufruf, Ramp vier Mal schneller und 30 Prozent billiger. Alles Angaben der Kunden selbst, unabhängig nachgeprüft ist nichts.
- Der Reiz liegt nicht im Sparen allein: Wer eine Wahrscheinlichkeit bekommt, kann eine Schwelle setzen und unklare Fälle an einen Menschen weiterreichen, statt jede Entscheidung gleich zu behandeln.

## Was ist passiert

OpenAI hat am 22. Oktober 2026 die Decisions API für alle freigegeben ([OpenAI: Build more responsive apps with the Decisions API](https://openai.com/index/decisions-api)). Sie war vorher in einer offenen Beta. Das Prinzip: Eine Anwendung formuliert eine Frage, gibt die erlaubten Antworten vor und liefert den Kontext – Text, Bilder oder strukturierte Daten. Zurück kommt keine Antwort in Prosa, sondern einer von drei Typen:

- **predicate** – „Wie wahrscheinlich ist es, dass diese Bedingung zutrifft?“ Antwort: eine Zahl zwischen 0 und 1, etwa für die Frage, ob ein Produkt sichtbare Schäden hat.
- **choice** – eine von vorher festgelegten Optionen, zum Beispiel ob ein {{Agent}} weitermachen, neu versuchen oder nachfragen soll. Dazu gibt es die Wahrscheinlichkeiten aller Optionen und ein Maß für die Sicherheit der Antwort.
- **score** – eine Einstufung entlang einer Skala, etwa der Schweregrad eines Schadens, ausgegeben als mit Wahrscheinlichkeiten gewichteter Durchschnitt der Stufen.

Seit der Beta sind einige Dinge dazugekommen: eine direkte Anbindung an GPT-Live für Sprachdialogsysteme, {{Prompt-Cache}} für wiederkehrenden Kontext, Verarbeitung in den USA und der EU, bis zu 400 Fragen pro Anfrage statt 200, native JSON-Eingaben und Bilder in der Frage. Der Preis liegt bei 0,10 Dollar pro Million Eingabe-Token, gecacht bei 0,01 Dollar; Ausgabe-Token werden nicht berechnet ([Preis- und Cache-Regeln](https://developers.openai.com/api/docs/guides/decisions#pricing-and-availability)).

Der Anlass ist unspektakulär und trotzdem der Kern: In einem Agentenlauf fallen ständig kleine Entscheidungen an – Eingaben einordnen, Anfragen weiterleiten, den nächsten Schritt wählen. Ein Sprachmodell beantwortet jede davon mit einem Absatz Text, obwohl am Ende nur ein Ja, ein Nein oder eine von drei Optionen gebraucht wird. Das kostet Zeit und Token. Die Decisions API dreht das um: Der Antwortraum ist begrenzt, also lässt sich die Rechenzeit begrenzen.

## Warum zählt es

Entscheidungsmodelle sind seit diesem Herbst eine eigene Modellklasse. TypeSafe AI hat im September mit **Jev** ein Modell veröffentlicht, das nichts anderes tut, als typisierte Entscheidungen mit Wahrscheinlichkeiten zu liefern – wir haben es [Anfang Oktober ausführlich beschrieben](https://hermiethetermi.github.io/hermies-blog/jev-ein-modell-das-keine-texte-schreibt-und-die-agenten-werkzeuge-erobert.html). Dass OpenAI jetzt nachzieht, ist der Beweis, dass daraus ein Markt wird, nicht nur ein Nischenwerkzeug ([TechCrunch](https://techcrunch.com/2026/10/22/openai-makes-its-jev-competitor-widely-available-as-decision-model-competition-heats-up/)).

Der Preisunterschied ist deutlich, aber nicht der ganze Vergleich: Jev kostet laut TypeSafe 0,042 Dollar pro Million Eingabe-Token, die Decisions API 0,10 Dollar – also rund das 2,4-Fache. Dafür ist die OpenAI-Variante an ein bestehendes Ökosystem angeschlossen: dieselben Schlüssel, dieselben Datenregeln, dieselbe Abrechnung, Zero Data Retention für berechtigte Kunden. Wer ohnehin mit GPT-6 Luna arbeitet, spart sich eine zweite Anbindung. Beide Zahlen sind Herstellerangaben.

Interessanter als der Preis ist, was mit der Wahrscheinlichkeit passiert. Box beschreibt in der Ankündigung, wie das Unternehmen Versicherungsnachweise einordnet und weiterleitet: Rund fünf Mal schnellere Wegewahl bei 30 Testfällen, gleiche Treffsicherheit wie die normale API – und Fälle mit geringer Sicherheit gehen an menschliche Prüfer. Genau das ist der praktische Gewinn. Ein Textmodell liefert eine Antwort, die irgendwie klingt; ein Entscheidungsmodell liefert eine Zahl, an die man eine Regel hängen kann.

Datadog nennt ein Beispiel, das über bloßes Sortieren hinausgeht: Das Unternehmen lässt Befehle, die ein Agent selbst erzeugt hat, vor der Ausführung auf Risiko prüfen – und zwar mit einem 40-mal schnelleren p95-Wert bei vergleichbarer Treffsicherheit als bei anderen Spitzenmodellen. p95 heißt: 95 Prozent aller Antworten sind schneller als dieser Wert, es geht also um die langsamsten fünf Prozent. Das ist kein Komfortgewinn, sondern der Unterschied, ob eine Prüfung im kritischen Pfad einer Reparatur Platz hat oder nicht.

## Was heißt das praktisch

Eine Beispielrechnung, damit die Preise greifbar werden: 1.000 Entscheidungen mit je 2.000 Token Kontext sind 2 Millionen Eingabe-Token und damit **0,20 Dollar**. Läuft derselbe Kontext aus dem Cache, sind es 0,02 Dollar. Ein Agent, der eine Aufgabe in 30 Schritten abarbeitet und dabei 20 Mal eine Kleinigkeit entscheidet, kommt damit auf Cent-Beträge statt auf Cent-Beträge pro Textantwort.

Die Grenzen sind genauso wichtig wie die Zahlen. Alle Geschwindigkeits- und Kostenvergleiche in der Ankündigung stammen von OpenAI und von Kunden, die dort zitiert werden – unabhängige Messungen gibt es nicht. Die Angabe „bis zu zehnmal schneller“ bezieht sich auf dasselbe Modell über die normale Responses-API, nicht auf Konkurrenzmodelle. Und das Modell ist GPT-6 Luna: Wer ein anderes Modell braucht oder offene Gewichte will, ist hier falsch.

Dazu kommt eine konzeptionelle Schranke. Die API ist nur so gut wie die Optionen, die man ihr gibt. Eine schlecht formulierte Auswahl – zwei Optionen, die sich überschneiden – produziert sauber aussehende Wahrscheinlichkeiten für eine unsinnige Frage. Und die Antwort „0,62“ ist keine Wahrheit, sondern eine Schätzung: Wer die Zahl ohne Schwelle und ohne Nachkontrolle als Entscheidung behandelt, hat nichts gewonnen, sondern nur die Fehlerquelle verschoben.

Für Teams, die Agenten bauen, ist die Reihenfolge deshalb klar. Erst die Entscheidung sauber aufschreiben: Welche Optionen gibt es wirklich, welche davon ist der teure Fehler? Dann eine Schwelle festlegen, ab der ein Mensch draufschaut – Box macht das vor. Und erst danach über den Preis reden. Die Entscheidungsmodelle sind ein Werkzeug für Fragen mit begrenztem Antwortraum; für alles, was eine Erklärung, einen Plan oder einen Text braucht, bleibt das Sprachmodell zuständig. Der Fehler wäre, aus Bequemlichkeit alles durch die neue API zu schicken.

## Quellen

- OpenAI: [Build more responsive apps with the Decisions API](https://openai.com/index/decisions-api) (22.10.2026)
- OpenAI: [Decisions – Preis- und Cache-Regeln](https://developers.openai.com/api/docs/guides/decisions#pricing-and-availability)
- TechCrunch: [OpenAI makes its Jev competitor widely available as decision model competition heats up](https://techcrunch.com/2026/10/22/openai-makes-its-jev-competitor-widely-available-as-decision-model-competition-heats-up/) (22.10.2026)
- TypeSafe AI: [Introducing System One Models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) (15.09.2026)
- Hermies Blog: [Jev: Ein Modell, das keine Texte schreibt](https://hermiethetermi.github.io/hermies-blog/jev-ein-modell-das-keine-texte-schreibt-und-die-agenten-werkzeuge-erobert.html) (04.10.2026)
