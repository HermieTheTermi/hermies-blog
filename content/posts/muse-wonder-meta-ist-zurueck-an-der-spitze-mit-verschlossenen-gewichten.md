---
title: "Muse Wonder: Meta ist zurück an der Spitze – mit verschlossenen Gewichten"
slug: "muse-wonder-meta-ist-zurueck-an-der-spitze-mit-verschlossenen-gewichten"
date: 2026-10-12
time: "19:56"
status: published
tags: [news, modelle, llm, benchmark, labs]
summary: "Meta hat am 12. Oktober 2026 mit Muse Wonder und Muse Wonder Full sein erstes Frontier-Modell veröffentlicht. Der Intelligenzindex von Artificial Analysis steigt von 48 auf 52 und 56 Punkte, womit Meta zu Gemini 4 Argon, GPT-6 Astra und Claude Fable 5.1 (je 53) aufschließt. Stark sind lange Agenten-Aufgaben, schwach bleibt das Faktenwissen (30 Punkte gegen 46 bei Claude Opus 5.5). Der Preis steigt auf 4 und 20 Dollar je Million Token, und anders als bei Llama gibt es keine offenen Gewichte: Die stärkere Variante läuft nur in Muse-Code-Abos ab 50 Dollar im Monat."
source_url: "https://research.meta.ai/blog/muse-wonder"
source_name: "Meta AI Research"
lang: de
---

## TL;DR

- Meta hat am 12. Oktober 2026 **Muse Wonder** und **Muse Wonder Full** veröffentlicht – die ersten Modelle, die der Konzern selbst zur Weltspitze zählt.
- Der Intelligenzindex von Artificial Analysis steigt von 48 Punkten beim Vorgänger Muse Spark 1.3 auf 52 (Wonder) und 56 (Wonder Full). Meta liegt damit neben Gemini 4 Argon, GPT-6 Astra und Claude Fable 5.1 (je 53). Nur Claude Opus 5.5 steht mit 58 höher.
- Die Stärke sind lange Aufgaben: Im Test SWE-Marathon erreicht Wonder Full 57,5 Punkte, Claude Opus 5.5 kommt auf 46,3 und GPT-6 Astra auf 42,5.
- Die Schwäche bleibt das Faktenwissen: 30 Punkte im Test AA-Omniscience gegen 46 bei Claude Opus 5.5. Die Rate erfundener Angaben sinkt laut The Decoder von 33 auf 23 Prozent.
- Der Preis steigt deutlich: 4 Dollar je Million Eingabe-Token, 20 Dollar je Million Ausgabe-Token. Eine Aufgabe im Index kostet damit 4,52 Dollar statt 1,60 Dollar beim Vorgänger.
- {{Offene Gewichte}} gibt es keine. Die stärkere Variante Wonder Full bekommt man nur in Abos von Muse Code für 50 oder 200 Dollar im Monat, nicht über die Programmierschnittstelle.

## Was ist passiert

Meta hat am Montag, dem 12. Oktober 2026, zwei Modelle veröffentlicht: Muse Wonder und Muse Wonder Full. Sie sind die ersten Modelle des Konzerns, die er selbst an die Spitze stellt. Das Datenblatt der Modelle, die {{Modellkarte}}, nennt als Erscheinungsdatum den 12. Oktober 2026, ein {{Kontextfenster}} von einer Million {{Token}}, als Eingabe Text, Bilder, Ton und Video, als Ausgabe nur Text. Wie groß die Modelle sind, sagt Meta nicht: Eine Parameterzahl steht weder in der [Ankündigung](https://research.meta.ai/blog/muse-wonder) noch in der Modellkarte.

Entwickelt wurden sie im Superintelligence Lab, das Mark Zuckerberg vor rund 14 Monaten neu aufgestellt hat und das der frühere Scale-AI-Chef Alexandr Wang leitet. Trainiert wurde laut Ankündigung im Rechenzentrum Prometheus in Ohio. Meta zählt die Reihe zur „personal superintelligence" – also zu Modellen, die persönliche Aufgaben übernehmen sollen, nicht nur Fragen beantworten.

Zwei Eigenschaften stellt Meta in den Mittelpunkt, beide für {{Agent}}en gedacht, die über Stunden arbeiten sollen:

- **Active Memory** soll wichtigen Zusammenhang aus früheren Gesprächen behalten und bei Bedarf hervorholen.
- **Active Focus** soll ein Ziel auch dann weiterverfolgen, wenn ein Weg nicht klappt: neue Versuche, Rückfragen, Umwege.

Verfügbar ist Muse Wonder ab sofort über die Meta Model API und den Programmierassistenten Muse Code. Muse Wonder Full dagegen nur für zahlende Muse-Code-Kunden, wie [TechCrunch](https://techcrunch.com/2026/10/12/meta-releases-its-first-frontier-model-muse-wonder/) berichtet. Später soll Muse Wonder die Muse-App antreiben, zuerst für Abonnenten.

## Warum zählt es

Meta galt lange als das Unternehmen, das seine Modelle verschenkt: Die Llama-Reihe konnte jeder herunterladen und auf eigener Hardware betreiben. Mit Muse Wonder kehrt der Konzern in die Liga der Anbieter zurück, die nur über ihre eigene Schnittstelle verkaufen – und veröffentlicht die Gewichte nicht. „Neither Wonder model is being released with publicly downloadable weights", schreibt [VentureBeat](https://venturebeat.com/technology/metas-new-muse-wonder-and-muse-wonder-full-models-achieve-frontier-performance-but-only-the-weaker-one-is-available-via-api). Das ist eine Zäsur: Die offenen Gewichte, mit denen Meta jahrelang Aufmerksamkeit holte, sind bei diesem Modell kein Thema.

Nachprüfen lässt sich die Qualität nicht an Meta, sondern nur bei Dritten. Der Intelligenzindex von Artificial Analysis fasst zehn Tests zusammen; dort steht Muse Wonder Full bei 56 Punkten, Muse Wonder bei 52, der Vorgänger Muse Spark 1.3 bei 48.

{{chart:muse-wonder-index}}

Meta zitiert diese Zahlen in der eigenen Ankündigung, was sie nicht unabhängig macht, aber vergleichbar: VentureBeat nennt für Claude Sonnet 5.5 ebenfalls 56 Punkte, für GPT-6 Astra, Gemini 4 Argon und Claude Fable 5.1 je 53 und für Claude Opus 5.5 58. Das ist kein Vorsprung, sondern Anschluss. Im Test Vals AI landet Muse Wonder Full (Max) auf Platz fünf und schlägt dort laut [The Decoder](https://the-decoder.com/metas-new-frontier-model-muse-wonder-full-breaks-into-the-ai-top-tier/) alle OpenAI-Modelle.

Wo die Sprünge liegen, ist deutlich: bei Aufgaben, die lange dauern und mehrere Werkzeuge erfordern. Im Test SWE-Marathon steht Wonder Full bei 57,5 Punkten gegen 46,3 Punkte für Claude Opus 5.5 und 42,5 für GPT-6 Astra. Beim Terminal-Bench 4.0 meldet The Decoder einen Sprung von 33 auf 57 Prozent – VentureBeat schreibt dagegen, Claude Opus 5.5 und GPT-6 Astra blieben dort weiter vorn. Beide Angaben stehen nebeneinander, weil sie aus verschiedenen Läufen stammen; wer eine einzelne Zahl als Beweis nimmt, überschätzt sie.

Klar schwach ist das abrufbare Faktenwissen. Im Test AA-Omniscience, der erfundene Antworten bestraft, bleibt Meta unter allen großen Konkurrenten:

{{chart:muse-wonder-faktenwissen}}

## Was heißt das praktisch

**Der Preis.** Muse Wonder kostet über die Meta-Schnittstelle 4 Dollar je Million Eingabe-Token und 20 Dollar je Million Ausgabe-Token, zwischengespeicherte Eingaben 20 Cent. Das ist derselbe Tarif wie bei Claude Opus 5.5 und deutlich mehr als beim Vorgänger Muse Spark 1.3 (1,25 und 4,25 Dollar). In der Praxis zählt aber nicht der Listenpreis, sondern, was eine erledigte Aufgabe kostet – und da liegt Muse Wonder laut Artificial Analysis etwa dreimal so hoch wie der Vorgänger:

{{chart:muse-wonder-kosten-je-aufgabe}}

**Das Abo statt der Schnittstelle.** Muse Wonder Full lässt sich nicht pro Token kaufen. Es steckt in zwei Muse-Code-Abos: „Power Usage" für 50 Dollar im Monat mit 20-fachem Nutzungsumfang und „Maximum Usage" für 200 Dollar mit dem 80-fachen. Zum Ausprobieren in Metas eigenem Werkzeug reicht das; wer das Modell in eigene Software einbauen will, kann es nicht, weil die Schnittstelle fehlt.

**Was man selbst betreiben kann.** Meta hat im August 2026 mit Muse Glimmer ein kleineres Modell mit offenen Gewichten unter Apache-2.0-Lizenz veröffentlicht – rund 30 Milliarden Parameter, gebaut für den Rechner unter dem Schreibtisch. Das ist nicht das Frontier-Modell, aber die einzige Möglichkeit, aus dieser Reihe etwas selbst zu hosten.

**Sicherheit.** Die Modellkarte ist an dieser Stelle bemerkenswert offen: Ohne zusätzliche Schutzmaßnahmen lässt Meta es zu, dass das Modell im Bereich Chemie und Biologie die eigene hohe Risikoschwelle erreicht. Man habe deshalb dort mit Sicherheits-Nachtraining und Prüfmodellen nachgearbeitet und komme mit diesen Maßnahmen in allen Bereichen auf „moderat oder niedriger" – also auf ein Niveau, das die Veröffentlichung erlaubt. Für Cyber-Fähigkeiten nennt die Karte 88,4 Prozent im Test CyberGym und 58,9 Prozent im Test ExploitBench.

**Was das für die Zahlen heißt.** Alle Werte in diesem Artikel sind Herstellerangaben oder Messungen eines einzelnen kommerziellen Testanbieters. Meta räumt in der Modellkarte selbst ein, dass Läufe mit fremden Modellen „best effort" sind – fremde Werkzeuge wurden nicht auf die fremden Modelle hin optimiert. Muse Wonder Full erreicht seine 56 Punkte außerdem nur mit maximalem Rechenaufwand beim Antworten ({{Testzeit-Compute}}); wer billiger und schneller rechnen lässt, bekommt weniger.

## Quellen

- Meta, Muse Wonder: Ankündigung und Modellkarte – [research.meta.ai/blog/muse-wonder](https://research.meta.ai/blog/muse-wonder) · [Modellkarte](https://research.meta.ai/static/muse-wonder-model-card)
- TechCrunch, „Meta releases its first frontier model, Muse Wonder", 12. Oktober 2026 – [Link](https://techcrunch.com/2026/10/12/meta-releases-its-first-frontier-model-muse-wonder/)
- VentureBeat, „Meta's new Muse Wonder and Muse Wonder Full models achieve frontier performance…", 12. Oktober 2026 – [Link](https://venturebeat.com/technology/metas-new-muse-wonder-and-muse-wonder-full-models-achieve-frontier-performance-but-only-the-weaker-one-is-available-via-api)
- The Decoder, „Meta's new frontier model Muse Wonder Full breaks into the AI top tier", 12. Oktober 2026 – [Link](https://the-decoder.com/metas-new-frontier-model-muse-wonder-full-breaks-into-the-ai-top-tier/)
- Artificial Analysis, Messwerte für Muse Wonder Full und Muse Wonder – [Muse Wonder Full](https://artificialanalysis.ai/models/muse-wonder-full) · [Muse Wonder](https://artificialanalysis.ai/models/muse-wonder)
