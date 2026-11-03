---
title: "Astra repariert ein fremdes Netz, indem es 0,016 Prozent der Gewichte überschreibt"
slug: "astra-repariert-ein-fremdes-netz-indem-es-0-016-prozent-der-gewichte-ueberschreibt"
date: 2026-11-02
status: published
tags: [news, forschung, llm, modelle]
summary: "Vier Forscher am MIT CSAIL haben GPT-6 Astra die rohen Gewichte kleiner Netze vorgelegt und es gebeten, sie zu lesen, zu reparieren und neu zu schreiben, ohne Training und ohne Gradienten. Bei Qwen3.5-0.8B löschte Astra eine Richtung in den Schichten 15 und 19, die für Denkschleifen verantwortlich war, in 131.072 von 800 Millionen Gewichten; MATH-500 stieg von 7,9 auf 48,1 Prozent, die Instruktionsbefolgung von 21,0 auf 62,3 Prozent. Bei Gemma 3 270M, das nicht schleift, blieb jede Bearbeitung wirkungslos: Ein Hindernis lässt sich wegschneiden, eine fehlende Fähigkeit nicht hinzufügen."
source_url: "https://rikiyat.github.io/blog/weight-space-programming/"
source_name: "MIT CSAIL (Takehi et al.)"
lang: de
---

## TL;DR

- Vier Forscher am MIT CSAIL haben GPT-6 Astra die rohen Gewichte kleiner Netze vorgelegt und es gebeten, sie zu lesen, zu reparieren und von Grund auf zu schreiben. Trainieren, Verlustfunktion und Gradienten waren nicht erlaubt.
- In acht Experimenten erkannte Astra aus den Gewichten allein, welches Spiel ein Netz gelernt hatte, welche Form ein Diffusionsmodell zeichnet und auf welcher Sprache ein Sprachmodell trainiert war. Die Kopierköpfe, die es benannte, stimmten mit den gemessenen überein.
- Bei Qwen3.5-0.8B fand es eine Richtung in den Gewichten der Schichten 15 und 19, die für die Denkschleifen verantwortlich war, und löschte sie in 131.072 von 800 Millionen Gewichten, also 0,016 Prozent. MATH-500 stieg von 7,9 auf 48,1 Prozent.
- Die Grenze steht im selben Bericht: Bei Gemma 3 270M, das nicht schleift, blieb jede Bearbeitung wirkungslos. Ein Hindernis lässt sich wegschneiden, eine fehlende Fähigkeit nicht hinzufügen.
- Getestet wurde ein einziges Modell, ohne unabhängige Wiederholung; einen Benchmark für die Fähigkeit bauen die Autoren erst noch.

## Was ist passiert

Am 2. November haben Rikiya Takehi, Jayden Teoh, Alex Zhang und Omar Khattab vom MIT CSAIL einen [Bericht](https://rikiyat.github.io/blog/weight-space-programming/) veröffentlicht, der eine ungewöhnliche Frage stellt: Kann ein Sprachmodell die Zahlen in einem fremden neuronalen Netz lesen wie Quelltext? Ihre Antwort ist ein vorsichtiges Ja, und sie haben der Methode einen Namen gegeben: Weight-Space Programming.

Gewichte sind die Zahlen, die ein Netz beim Training lernt. Bei einem Modell mit 800 Millionen {{Parameter}}n sind das 800 Millionen einzelne Werte, verteilt über 24 Schichten. Normalerweise schreibt sie ein Optimierer wie Adam, der aus Fehlern ableitet, wohin jede Zahl wandern soll. Die vier Forscher haben stattdessen die rohen Werte als Text in das {{Kontextfenster}} von Astra gelegt und ihm Python gegeben. Eine Trainingsschleife durfte es nicht schreiben, Gradienten nicht sehen und das Netz in den meisten Experimenten nicht einmal ausführen.

In acht Experimenten kommen drei Fähigkeiten zusammen: lesen, reparieren, schreiben.

## Lesen

Das erste Experiment ist das schönste. Vier Netze wurden mit demselben Verfahren (PPO) auf vier verschiedene Spiele trainiert: Breakout, Pong, Pac-Man und Freeway, jeweils eine eigene 10×10-Version. Alle vier haben dieselbe Bauform, 500 Eingaben, zwei versteckte Schichten mit 32 Einheiten, fünf Ausgaben, zusammen 17.253 Gewichte. Von außen ist kein Unterschied zu sehen.

Astra nannte trotzdem alle vier richtig, ohne die Liste der Spiele zu kennen. Die Begründung im Bericht ist konkret: Beim Breakout liegen die Gewichte des Agenten-Kanals in der unteren Zeile, weil dort der Schläger sitzt. Astra hatte die Geometrie des Spiels aus den Zahlen gelesen.

Im zweiten Experiment ging es um Diffusionsmodelle, die 12×12-Bilder erzeugen, je 23.824 Gewichte für Kreise, Quadrate und Dreiecke. Astra erkannte alle drei. Interessanter als die Trefferquote ist ein Fehler: Es zeichnete die Formen als Umriss, obwohl die Modelle gefüllte Flächen erzeugen. Wer einen Vorwärtspass rechnet, macht diesen Fehler nicht.

Das dritte Experiment ist das strengste. Drei Zeichenmodelle mit 7,16 Millionen Gewichten wurden auf Python-Code, englischer Wikipedia und japanischer Literatur in Lateinschrift trainiert. Die Forscher entfernten die Eingabe- und die Ausgabeschicht und gaben Astra nur die vier {{Transformer}}-Blöcke dazwischen. Ohne diese beiden Schichten sagt keine Zahl im Netz, welches Zeichen welches ist, und das Modell lässt sich auf keinem Text ausführen.

Astra traf die Sprache in beiden Versuchen und benannte in allen drei Modellen genau die Kopierköpfe, die eine spätere Messung bestätigte: Schicht 2.1, 3.1 und 3.5 im Python-Modell, 3.3 im Japanischen, 3.1 im Englischen. Keinen anderen Kopf meldete es als Kopierkopf. Den Weg dorthin hat es sich selbst hergeleitet, mit einer veröffentlichten Methode von Elhage und Kollegen aus der Mechanistischen Interpretierbarkeit: ein Kopf, der ein Zeichen zurückschaut, dann Gewichtsmatrizen multiplizieren, um spätere Köpfe zu finden, die damit weiterarbeiten. Astra hatte diese Methode nicht genannt bekommen.

Das siebte Experiment zeigt die Grenze desselben Ansatzes. Zwei Kopien von Gemma 3 270M wurden gleich feinjustiert, eine antwortet korrekt, die andere gibt immer die vom Nutzer vorgeschlagene Antwort. Aus den Gewichten allein fand Astra den Speichellecker nicht, in vier Versuchen nicht. Erst als es die Aufmerksamkeitsmuster auf selbst geschriebenen Texten sehen durfte, traf es alle drei Paare: In der ehrlichen Kopie schaut Kopf 10.2 zu 94,3 Prozent auf die Zahlen der Frage, in der speichelleckerischen zu 85,7 Prozent auf die Antwort des Nutzers.

## Reparieren und schreiben

Im vierten Experiment ging es um ein Auto in einer Physiksimulation, das eine Rampe überspringen soll. Dafür muss es erst zurücksetzen, um Anlauf zu nehmen. Das mit PPO trainierte Netz fuhr stattdessen gerade auf die Rampe zu und blieb hängen, in 256 von 256 Läufen. Astra bekam die Gewichte, eine Beschreibung der Szene und eine aufgezeichnete Episode. Es änderte 3,5 Prozent der Gewichte und löste die Aufgabe in 1.024 von 1.024 Läufen. Der Bericht zeigt auch, wie: ein kleiner zusätzlicher Pfad durch wenige Einheiten pro Schicht, der Position und Geschwindigkeit liest und sich abschaltet, sobald das Rad den roten Streifen passiert hat.

Noch einen Schritt weiter geht das fünfte Experiment. Drei MinAtar-Spiele, Netz mit 600 Eingaben und 32 Einheiten pro Schicht, alle Gewichte starten bei null. Keine Daten, keine Verlustfunktion, keine Gradienten, keine Werkzeuge, kein Ausprobieren im Spiel. Astra schrieb die Gewichte als Text in einer Antwort, und die Netze schlugen das mit PPO trainierte Vergleichsnetz in allen drei Spielen: Breakout 517,4 Punkte gegen 15,8 nach 100 Millionen Trainingsschritten, Seaquest 53,1 gegen 5,6, Asterix 53,2 gegen 25,8. Gegen die 500-Millionen-Version steht es 20-fach in Breakout, knapp in Asterix und bei 60 Prozent in Seaquest.

Im sechsten Experiment ging es um Go auf 9×9 Feldern, 1,48 Millionen Gewichte. Die passen nicht in einen Prompt, deshalb bekam Astra eine Python-Sandbox ohne Go-Bibliothek und 50 Vorwärtspässe. Damit schlug sein Netz ein gleich großes PPO-Netz, das auf 20 Millionen Partien trainiert war.

## Die 0,016 Prozent

Das achte Experiment ist das, über das gerade geredet wird. Qwen3.5-0.8B ist ein offenes Modell mit 800 Millionen {{Parameter}}n, das vor dem Antworten nachdenkt. Seine {{Modellkarte}} warnt vor Denkschleifen, in denen das Modell denselben Text wiederholt, bis das {{Token}}-Limit greift. In der Praxis betraf das fast jede Antwort: 85 der ersten 96 Übungsantworten liefen bis an die Grenze von 32.768 Token.

Astra bekam die Gewichte in einer Python-Sitzung, 14.744 Übungsaufgaben aus GSM8K und MATH und ein Budget an Vorwärtspässen, also Läufen des Netzes ohne Gradienten. Es verfolgte die Schleife bis zu einer Richtung, die die MLPs der Schichten 15 und 19 schreiben, und zog diese Richtung von je 64 Ausgabespalten ab. 131.072 von 800 Millionen Gewichten, 0,016 Prozent.

{{tabelle:wsp-qwen}}

Der Sprung kommt nicht von mehr Rechenzeit allein: Mit 10 und mit 25 Vorwärtspässen blieb MATH-500 bei 12,3 und 14,1 Prozent, der Anteil der Antworten am Token-Limit fiel kaum. Erst mit 50 Pässen brach die Schleife, und dann verbesserte sich auch die Instruktionsbefolgung von 21,0 auf 62,3 Prozent. Das passt zur Diagnose: Die Schleife war kein Mathematikproblem, sie traf jede Aufgabe.

::: warnung Der Gegenversuch
Die Autoren haben den wichtigsten Einwand selbst geprüft. Gemma 3 270M, ein instruct-feinjustiertes Modell ohne Schleifenproblem (8,5 Prozent der Antworten am Token-Limit), ließ sich nicht verbessern: MATH-500 blieb bei 6,8 Prozent, nach Bearbeitungen bei 7,0, 7,6, 7,7 und wieder 7,0. Astra fand hier gewöhnliche Rechenfehler ohne eine einzelne Ursache. Ihr Fazit: Ein Eingriff in die Gewichte kann ein Hindernis entfernen, das eine Fähigkeit verdeckt. Er kann keine Fähigkeit hinzufügen, die nicht da ist.
:::

## Warum zählt es

Zwei Dinge sind neu. Bisher haben Modelle entweder Werkzeuge bedient, die für sie gebaut wurden, oder sie wurden eigens dafür trainiert, Gewichte zu lesen. Hier liest ein Allzweckmodell die Zahlen selbst, so gut, dass es die veröffentlichte Kopierkopf-Analyse ohne Anleitung nachvollzieht.

Der zweite Punkt ist die Sparsamkeit des Eingriffs. 0,016 Prozent der Gewichte zu ändern lässt den Rest unangetastet. {{Fine-Tuning}} auf neue Aufgaben verändert dagegen alle Gewichte und riskiert, dass das Modell Altes verlernt.

Der Titel heißt „Sparks", Funken, und die Autoren meinen das so. Getestet wurde ein Modell eines Anbieters, auf Netzen bis 1,5 Millionen und einmal 800 Millionen Gewichte. Die Zahlen hängen am {{Harness}}: Bei Qwen springt MATH-500 je nach Zahl der erlaubten Vorwärtspässe von 12,3 auf 48,1 Prozent. Kontextlänge und Harness nennen die Autoren selbst als Engstelle. Einen standardisierten Test, der Modelle vergleichbar macht, gibt es noch nicht.

## Was heißt das praktisch

Für die Sicherheitsprüfung ist der Leseteil der interessantere. Wer ein Modell bekommt, ohne zu wissen, was beim Training hineingeraten ist, kann bisher nur auf Eingaben warten, die eine Hintertür auslösen. Gewichte lesen wäre der direkte Weg, vorausgesetzt, es klappt auch bei Milliarden {{Parameter}}n.

Für die Reparatur ist die Grenze aus dem Gegenversuch die eigentliche Nachricht. Was ein Modell schon kann und nur nicht zeigt, lässt sich freilegen. Was es nicht kann, bleibt außer Reichweite.

Eine Frage stellt der Bericht nicht: Dieselbe Fähigkeit, eine Schleife zu löschen, kann auch eine Sicherheitsschwelle verschieben. Bei offenen Gewichten ist ein Modell, das sich mit ein paar Zahlen umschreiben lässt, leichter zu verändern als eines, das neu trainiert werden muss.

## Quellen

- Rikiya Takehi, Jayden Teoh, Alex Zhang, Omar Khattab: Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights, MIT CSAIL, 2.11.2026: [rikiyat.github.io/blog/weight-space-programming](https://rikiyat.github.io/blog/weight-space-programming/)
- Vollständige Protokolle aller acht Experimente: [github.com/RikiyaT/lm_understand-logs](https://github.com/RikiyaT/lm_understand-logs)
- Bearbeitetes Qwen3.5-0.8B, von Hugging Face aus den Protokollen nachgebaut und neu bewertet: [huggingface.co/JonathanColetti/Qwen3.5-0.8B-Astra-WeightEdit](https://huggingface.co/JonathanColetti/Qwen3.5-0.8B-Astra-WeightEdit)
- Methode der Kopierköpfe, die Astra ohne Anleitung nachvollzog: Elhage et al., A Mathematical Framework for Transformer Circuits: [transformer-circuits.pub/2021/framework](https://transformer-circuits.pub/2021/framework/index.html)
