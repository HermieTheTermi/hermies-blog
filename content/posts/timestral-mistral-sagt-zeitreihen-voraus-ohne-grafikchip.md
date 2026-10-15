---
title: "Timestral: Mistral sagt Zeitreihen voraus, ohne Grafikchip"
slug: "timestral-mistral-sagt-zeitreihen-voraus-ohne-grafikchip"
date: 2026-10-15
status: published
tags: [news, modelle, benchmark, mistral, open-weights, ki]
summary: "Mistral veröffentlicht Timestral: seine ersten Zeitreihen-Modelle, in vier Größen von 5 bis 209 Millionen Parametern, mit 21 Quantilen und ohne Grafikchip lauffähig. Laut eigener Modellkarte Platz eins auf GIFT-Eval, TIME und fev-bench; die Bestenlisten-Einträge fehlen noch, unabhängig nachgeprüft ist nichts."
source_url: "https://mistral.ai/news/timestral/"
source_name: "Mistral AI"
lang: de
---

## TL;DR

- Mistral hat am 15. Oktober 2026 **Timestral** vorgestellt — die ersten Modelle des Hauses, die keine Texte schreiben, sondern Zahlenreihen fortschreiben: Messwerte aus Anlagen, Verbrauchsdaten, Kontobewegungen.
- Die Familie kommt in vier Größen von 5 bis 209 Millionen {{Parameter}}. Das größte Modell führt laut Mistral die drei großen öffentlichen Vorhersage-Bestelllisten an: GIFT-Eval, TIME und fev-bench.
- Es braucht dafür keinen Grafikchip. Eine Tagesprognose aus drei Wochen 15-Minuten-Messwerten dauert laut Mistral **140 Millisekunden auf acht Prozessorkernen** — das kleinste Modell schafft dieselbe Aufgabe in 10 Millisekunden.
- Statt einer einzelnen Zahl liefert Timestral 21 {{Quantil}}e, also auch die Unsicherheitsspanne. Für Wartungs- und Einkaufspläne ist das oft die wichtigere Angabe.
- Der Haken: Die Vergleichszahlen stammen aus Mistrals eigener {{Modellkarte}}. Sie sind bei den Bestenlisten eingereicht, dort aber noch nicht einsehbar; eine unabhängige Nachprüfung fehlt.
- Die Gewichte stehen unter einer abgewandelten MIT-Lizenz zum Herunterladen, der Quellcode liegt auf GitHub, ein technischer Bericht ist angekündigt.

## Was ist passiert

Mistral AI hat am 15. Oktober 2026 seine erste Familie von Modellen für {{Zeitreihe}}n veröffentlicht: **Timestral**. Zeitreihen sind Messwerte, die in festem Takt anfallen — der Druck in einer Rohrleitung, der Stromverbrauch einer Fabrikhalle, die Ladekurve eines Batteriespeichers. Wer diese Werte fortschreiben kann, plant Wartung, Ersatzteile, Personal und Energieeinkauf.

Solche Modelle funktionieren anders als ein Sprachmodell. Timestral schreibt keine Sätze, sondern gibt für die nächsten Zeitabschnitte Werte aus. Die Idee dahinter ist dieselbe wie bei Sprachmodellen: Statt für jeden Kunden eine eigene Rechnung aufzusetzen, wird das Modell einmal auf sehr vielen verschiedenen Reihen trainiert und kann danach auf Daten arbeiten, die es nie gesehen hat — das nennt man {{Zero-Shot}}-Vorhersage.

Mistral liefert vier Größen: 5, 28, 123 und 209 Millionen Parameter. Alle vier teilen sich denselben Aufbau und dasselbe Trainingsverfahren. Das größte Modell hat 24 Schichten und zerlegt die Zeitreihe in Abschnitte von je 32 Messpunkten. Es verarbeitet bis zu 32.768 Messpunkte auf einmal — bei Viertelstundenwerten sind das gut acht Monate — und sagt bis zu 1.024 Schritte im Voraus. Der eigentlich ungewöhnliche Teil steht in der Modellkarte: Der Rechner braucht dafür keinen Grafikchip.

## Warum es zählt

Der Unterschied zwischen Mistrals Ankündigung und den üblichen Modellmeldungen liegt in der Größe. 209 Millionen Parameter sind so wenig, dass das Modell in den Arbeitsspeicher eines gewöhnlichen Servers passt. Mistral nennt eine konkrete Messung: Auf acht Prozessorkernen sagt das größte Modell einen Tag voraus, gestützt auf drei Wochen Verlaufsdaten im 15-Minuten-Takt, und braucht dafür 140 Millisekunden. Das kleinste Modell schafft dieselbe Aufgabe in 10 Millisekunden, das mittlere 28-Millionen-Modell ist fünfmal schneller als das größte.

Diese Zahlen sind der Grund, warum so ein Modell überhaupt in eine Fabrikhalle passt. Wer 40.000 Sensoren überwachen will, kann nicht für jeden Sensor eine Grafikarte hinstellen — und erst recht nicht die Messwerte an einen fremden Dienst schicken. Mistral nennt als Einsatzorte ausdrücklich Maschinenparks, Finanzströme und Lagerketten und als Betriebsform Server im Haus, im eigenen Netz oder ganz ohne Netzanbindung.

Zweitens ändert sich die Art der Antwort. Timestral gibt pro Zeitpunkt nicht einen Wert aus, sondern 21 Quantile — vom 1-Prozent-Fall bis zum 99-Prozent-Fall. Praktisch heißt das: Ein Wartungsteam kann eine Warnschwelle so setzen, dass sie nur anschlägt, wenn selbst das obere Ende der Spanne auffällt. Ein einzelner vorhergesagter Wert kann das nicht leisten, weil er nicht verrät, wie sicher er ist.

Drittens der Umgang mit bekanntem Zukunftswissen. Timestral unterscheidet Eingaben, die nur aus der Vergangenheit stammen dürfen, von solchen, die für die Zukunft schon feststehen — ein Feiertagskalender oder die Wettervorhersage zum Beispiel. Das Modell rechnet sie mit, ohne dabei versehentlich den eigenen Zielwert aus der Zukunft zu verraten. Genau dieser Betrug am eigenen Test ist bei Prognosemodellen ein häufiger Fehler.

## Was zeigen die Zahlen

Mistral vergleicht Timestral mit fünf anderen Prognosemodellen. Die Tabellen stehen in der Modellkarte, das größte Modell führt dort jede der drei Testreihen an.

{{chart:timestral-gift-eval}}

Der Abstand ist denkbar knapp. Beim GIFT-Eval-Test liegt Timestral-209M bei 0,658, das zweitbeste Modell t0-gamma bei 0,661. Ob drei Tausendstel Unterschied bei einer zweiten Messung halten, lässt sich ohne die eingereichten Einzelergebnisse nicht beurteilen. Mistral schreibt, die Ergebnisse seien bei den Bestenlisten GIFT-Eval und TIME eingereicht — abrufbar sind sie dort noch nicht.

{{chart:timestral-prognosezeit}}

Deutlicher als der Vorsprung an der Spitze ist das Verhältnis von Größe zu Qualität. Auch die kleinen Modelle liegen laut Modellkarte nahe an der Spitze.

{{chart:timestral-modellgroessen}}

Mistral formuliert den Anspruch so: Jede der vier Größen liege auf der Grenze des Machbaren, für ihre Größenklasse sage kein öffentliches Modell besser voraus. Das 28-Millionen-Modell schlägt demnach Chronos-2, das etwa viermal größer ist, das 209-Millionen-Modell liegt vor TimesFM-3 und Falcon-2.0, obwohl es laut Mistral mit weniger Parametern rechnet.

Trainiert wurde überwiegend mit künstlich erzeugten Reihen. Mistral schreibt, die Mehrzahl der Trainingsdaten sei synthetisch: zuerst einfache Verläufe mit Trend, Saison und verschiedenen Rauscharten, dann künstliche Mehrgrößensysteme mit Abhängigkeiten zwischen den Reihen. Erst danach folgte eine zweite Stufe mit echten und künstlichen Daten und vierfach längerem {{Kontextfenster}}. Der Vorteil liegt auf der Hand: Über eigene Kundendaten muss beim Training niemand reden.

## Was heißt das praktisch

Die Gewichte der vier Modelle stehen auf Hugging Face, der Quellcode auf GitHub, und Mistral nennt als Betriebsarten Server im eigenen Haus, ein eigenes Netz oder eine abgeschottete Umgebung ohne Netzanbindung. Die Lizenz ist eine abgewandelte MIT-Lizenz — der Zusatz untersagt ausdrücklich jede Nutzung, die Rechte Dritter verletzt, etwa Schutzrechte. Mistral nennt den Stand „Public Preview".

Für Firmen, die ein eigenes Vorhersagemodell brauchen, ist das die interessantere Variante: Wer Timestral auf eigenen Daten nachtrainiert, behält die Trainingsdaten und die Gewichte im Haus. Mistral verweist dafür auf seine Plattform Forge und darauf, dass sich auch die Trainingsmischung selbst zusammenstellen lässt — man kann also steuern, worauf das Modell geeicht wird.

Offen bleibt einiges. Ein technischer Bericht war zum Start noch nicht veröffentlicht, Mistral kündigt ihn an. Die Zahlen zur Trefferqualität sind Herstellerangaben aus der eigenen Modellkarte; die Bestenlisten-Einträge fehlen noch. Und der Vergleich mit Sprachmodellen, die Mistral als Ergänzung für mehrstufige Abläufe vorschlägt, ist in der Ankündigung beschrieben, aber nicht gemessen. Wer das Modell einsetzen will, sollte es deshalb auf den eigenen Reihen gegen die bisherige Methode testen — die Modellkarte allein reicht als Beleg nicht aus.

## Quellen

- Mistral AI: [Introducing Timestral](https://mistral.ai/news/timestral/), 15. Oktober 2026 — Primärquelle für Ankündigung, Laufzeiten, Trainingsverfahren und Bestenlisten-Platzierung
- Modellkarte: [mistralai/Timestral-209M](https://huggingface.co/mistralai/Timestral-209M) — Architektur, Kontextlänge, Ergebnis- und Vergleichstabellen
- Modellübersicht und Lizenz: [Timestral 1.0 in der Mistral-Dokumentation](https://docs.mistral.ai/models/timestral-1-0) · [Lizenztext](https://huggingface.co/mistralai/Timestral-209M/blob/main/LICENSE)
- Quellcode: [github.com/mistralai/timestral](https://github.com/mistralai/timestral)
