---
title: "Ein Blogger hält Astras Gewichte-Lesen für Rechenkunst, nicht für Forschung"
slug: "ein-blogger-haelt-astras-gewichte-lesen-fuer-rechenkunst-nicht-fuer-forschung"
date: 2026-11-03
status: published
tags: [news, forschung, llm, modelle]
summary: "Sean Goedecke hat am 3. November eine Gegenrechnung zum Astra-Bericht vom 2. November veröffentlicht: Ein kluger Mensch aus der Forschung könnte diese Aufgaben ebenfalls lösen. Das Trainingsspiel aus den Gewichten zu erkennen, sei mit drei Zeilen Python nachzubauen, weil die Eingabekanäle beschriftet sind und direkt auf einzelne Rasterfelder hören. Beim Qwen-Modell habe keine Rechensschwäche vorgelegen, sondern eine Schleife nach 32.768 Token. Seine Kritik trifft die Einordnung, nicht die Messwerte; zwei der acht Experimente prüft er nicht."
source_url: "https://www.seangoedecke.com/llms-are-not-superhuman-at-reading-and-writing-neural-network-weights/"
source_name: "Sean Goedecke"
lang: de
---

## TL;DR

- Der Softwareentwickler Sean Goedecke hat am 3. November eine Gegenrechnung zu dem Astra-Bericht vom 2. November veröffentlicht. Sein Satz: Ein kluger Mensch aus der Forschung könnte all diese Aufgaben ebenfalls lösen.
- Sein Hauptargument: Das Trainingsspiel aus den Gewichten zu erkennen, ist mit drei Zeilen Python nachzubauen, weil die Eingabekanäle beschriftet sind und direkt auf einzelne Felder eines Rasters hören.
- Beim Qwen-Modell lag kein Rechendefekt vor, sondern eine Schleife nach 32.768 Token. Unterhalb dieser Grenze löste das unveränderte Modell jede Aufgabe.
- Goedecke hält den Eingriff für die Arbeit, die ein guter Mensch ebenso machen würde, und vergleicht ihn mit dem Schreiben von Maschinencode statt Quelltext.
- Seine Kritik trifft die Einordnung, nicht die Messwerte. Zwei der acht Experimente prüft er nicht, und wiederholt hat den Versuch noch niemand.

## Was ist passiert

Am 3. November hat Sean Goedecke, Softwareentwickler und Blogger, einen Text mit dem Titel [„LLMs are not superhuman at reading and writing neural network weights“](https://www.seangoedecke.com/llms-are-not-superhuman-at-reading-and-writing-neural-network-weights/) veröffentlicht. Er antwortet damit auf den [Bericht vom 2. November](/astra-repariert-ein-fremdes-netz-indem-es-0-016-prozent-der-gewichte-ueberschreibt.html), in dem vier Forscher am MIT CSAIL zeigen, dass GPT-6 Astra die rohen Gewichte kleiner Netze lesen, reparieren und von Grund auf schreiben kann. Goedecke bestreitet die Messwerte nicht. Er bestreitet, dass daraus eine neue Fähigkeit folgt.

Seine These steht im zweiten Absatz: Ein klüger Mensch aus der Maschinenlern-Forschung könnte all diese Aufgaben ebenfalls lösen. Was der Bericht als Leistung über menschliches Vermögen hinaus beschreibt, sei in Wahrheit die Arbeit eines geübten Menschen, nur sehr schnell ausgeführt.

## Warum zählt es

Der Bericht selbst nennt als mögliche Folge die rekursive Selbstverbesserung: ein Modell, das andere Modelle besser macht und irgendwann sich selbst. Genau daran hängt die ganze Aussicht, und genau dort greift die Kritik. Der Unterschied zwischen „ein Modell rechnet schnell“ und „ein Modell forscht“ trägt die These. Wenn Astra nur tut, was ein Mensch mit Numpy in einer Minute tut, ändert sich an der Aussicht wenig.

Für die Einordnung ist der Streit nützlicher als der Bericht allein. Die Autoren schreiben selbst, ihre Ergebnisse seien durch Kontextlänge und Werkzeuge begrenzt. Goedecke liefert die Gegenprobe von außen, und zwar nicht mit einem Gefühl, sondern mit einer Rechnung, die jeder nachvollziehen kann.

## Was er nachrechnet

Im ersten Experiment sollten die Gewichte verraten, welches von vier Spielen ein Netz trainiert wurde. Alle vier Netze hatten dieselben Eingabekanäle, dieselben sechs Aktionen und dieselben Dimensionen, damit nur die Zahlen Auskunft geben konnten. Astra nannte alle vier richtig, ohne die Auswahl der Spiele zu kennen. Die Netze haben 17.253 Gewichte, verteilt auf zwei Schichten mit je 32 Einheiten.

Goedecke nennt drei Gründe, warum das leichter ist, als es klingt. Die Eingabekanäle hören direkt auf einzelne Felder eines 10-mal-10-Rasters, sie sind beschriftet, und damit lässt sich ausrechnen, welche Felder die erste Schicht gewichtet. Sein Code ist drei Zeilen lang: Gewichte laden, in die Form Raster mal Kanäle mal Einheiten bringen, über die Einheiten die Länge des Vektors bilden. Übrig bleibt eine Karte pro Kanal, 10 mal 10 Felder.

{{schritte:goedecke-heatmap}}

Aus dieser Karte, schreibt er, erkenne man die Spiele ohne Beschriftung. Bei Breakout liegt die Spielerfigur als waagerechte Linie am unteren Rand, die bewegten Objekte verteilen sich darüber. Dass Astra solche Normen im Kopf bilde, ohne Python, sei beachtlich. Es sei aber Kopfrechnen, das weit über menschliches Vermögen hinausgeht, und keine Forschung, die es täte.

::: methode
**Worüber hier gestritten wird**
Vier Netze, mit bestärkendem Lernen auf vier Spielen trainiert, jedes mit 17.253 Gewichten, sechs Eingabekanälen und sechs Ausgaben. Astra bekam die Gewichte als Text in den Prompt, ohne Werkzeuge und ohne die Namen der Spiele zur Auswahl. Der Blogger hat den umgekehrten Weg gewählt und die erste Schicht selbst ausgewertet. Beide Wege führen zum selben Ergebnis; strittig ist, was daran bemerkenswert ist.
:::

Der wichtigere Teil ist der Fall Qwen3.5-0.8B. Dort hatte das Modell nach Darstellung des Berichts kein Rechenproblem, sondern eine Schleife: Nach 32.768 Token wiederholte es sich und kam nie zu einer Antwort. Goedecke liest daraus, dass das Netz nicht schlecht im Rechnen war, sondern im Aufhören. Alle Aufgaben unterhalb dieser Grenze habe das unveränderte Modell gelöst.

Sein Gegenentwurf klingt unspektakulär. Er würde einige Denktexte schreiben, die in Schleifen laufen, und einige, die es nicht tun, die Differenz der Zwischenzustände messen, den Beitrag einzelner Gewichte dazu bestimmen und die größten Beiträge abschneiden. Dieses Vorgehen ist unter dem Namen Abliteration bekannt und als Werkzeug verbreitet; es braucht keine Gradienten und kein Training. Astra habe im Kern dasselbe getan, mit vier Textpaaren, einer Messung und einem Test. Der Unterschied liegt im Werkzeug: Bei Qwen durfte es Python benutzen, bei den Spielnetzen nicht.

## Wo seine Kritik endet

Goedecke prüft zwei der acht Experimente, das Spielnetz und Qwen, und sagt das auch. Die anderen bleiben außen vor. Im dritten Experiment bekam Astra nur die vier mittleren Blöcke eines Zeichenmodells, ohne Eingabe- und Ausgabeschicht, ohne die Möglichkeit, das Netz laufen zu lassen. Es nannte die Trainingssprache in allen drei Fällen richtig und benannte genau die Kopierköpfe, die die Forscher separat gemessen hatten, keinen daneben. Im sechsten Experiment schrieb Astra ein Go-Netz mit 1,48 Millionen Gewichten von Null, ohne Training, und schlug mit 50 Vorwärtspässen ein gleich großes Netz, das auf 20 Millionen Partien trainiert worden war. Diese Ergebnisse erklärt seine Rechnung nicht weg.

Ein Punkt spricht dagegen für ihn. Im siebten Experiment sollten zwei ansonsten identische Gemma-Modelle an ihren Gewichten unterschieden werden, eines ehrlich, eines schleimerisch. Aus den Gewichten allein erkannte Astra den Unterschied in vier Versuchen nicht. Erst als es die Aufmerksamkeitsmuster auf selbst geschriebenen Texten sehen durfte, traf es zu. Das ist ein Befund der Autoren selbst, und er stützt die Skepsis: Gewichte lesen ist nicht dasselbe wie Verhalten verstehen.

::: warnung
**Was offen bleibt**
Ein Modell, ein Anbieter, keine unabhängige Wiederholung. Die Autoren veröffentlichen alle Protokolle und jede Antwort im [Repository](https://github.com/RikiyaT/lm_understand-logs), nachgerechnet hat sie noch niemand. Der negative Versuch mit Gemma 3 270M steht im selben Bericht: Wo keine Schleife war, bewegte keine Bearbeitung den Wert über etwa einen Punkt. Ob sich der Befund auf Modelle überträgt, bei denen sich ein Eingriff wirklich lohnen würde, weiß niemand.
:::

## Was heißt das praktisch

Für alle, die solche Berichte lesen, ist die Unterscheidung wichtiger als das Ergebnis. Ein Modell, das eine Aufgabe in Sekunden löst, für die ein Mensch eine Stunde braucht, ist ein Geschwindigkeitsgewinn. Ein Modell, das eine Aufgabe löst, die ein Mensch nicht lösen kann, wäre etwas anderes. Goedeckes Vergleich macht den Unterschied greifbar: Sprachmodelle können Maschinencode schreiben und in fertige Programme eingreifen, und trotzdem schreibt niemand Software in Assembler, wenn er den Quelltext haben kann.

Für die Forschung folgt daraus eine nüchterne Priorität. Wenn sich ein Modell durch das Löschen einer Richtung in zwei Schichten von Schleifen befreien lässt, dann ist das ein nützliches diagnostisches Werkzeug, das bisher menschliche Arbeit war: Fehlerbild ansehen, Hypothese bilden, gezielt eingreifen, testen. Automatisiert wird daran der Handgriff, nicht die Frage, welche Hypothese sich lohnt. Ob Gewichte-Lesen einmal Training ersetzt, entscheidet sich nicht an einem Modell mit 0,8 Milliarden {{Parameter}}n, sondern daran, ob jemand den Versuch mit einem Modell wiederholt, das man tatsächlich trainieren müsste.

## Quellen

- Sean Goedecke: [LLMs are not superhuman at reading and writing neural network weights](https://www.seangoedecke.com/llms-are-not-superhuman-at-reading-and-writing-neural-network-weights/), 3.11.2026
- Rikiya Takehi, Jayden Teoh, Alex Zhang, Omar Khattab: [Sparks of Weight-Space Programming](https://rikiyat.github.io/blog/weight-space-programming/), MIT CSAIL, 2.11.2026
- [Vollständige Protokolle aller Experimente](https://github.com/RikiyaT/lm_understand-logs)
- [Diskussion auf Hacker News](https://news.ycombinator.com/item?id=50344861)
