---
title: "Nemotron holt Gold bei IOI und IMO: zwei Medaillen, ein Rezept"
slug: "nemotron-holt-gold-bei-ioi-und-imo-zwei-medaillen-ein-rezept"
date: 2026-10-07
status: published
tags: [news, modelle, benchmark, open-weights, forschung]
summary: "NVIDIA meldet am 7. Oktober 2026, dass feinjustierte Fassungen der offenen Nemotron-3-Reihe bei zwei Olympiaden Gold-Niveau erreicht haben: 30 von 42 Punkten bei der Mathematik-Olympiade IMO 2026 (Gold-Schwelle 29) und 535,4 von 600 Punkten beim Informatik-Wettbewerb IOI 2026 (Schwelle 361,12, bestes menschliches Ergebnis 498,27). Der IOI-Lauf war laut Team inoffiziell und unbeaufsichtigt, die IMO-Beweise wurden dagegen von offiziellen Prüfern benotet. Modell, Prüfpunkte, Trainingsdaten und Code sind veröffentlicht; alle Zahlen sind Herstellerangaben."
source_url: "https://huggingface.co/blog/nvidia/nemotron-ioi-and-imo-2026"
source_name: "NVIDIA"
lang: de
---

## TL;DR

- NVIDIA meldet in einem [Blogbeitrag vom 7. Oktober 2026](https://huggingface.co/blog/nvidia/nemotron-ioi-and-imo-2026), dass zwei feinjustierte Fassungen der offenen Nemotron-3-Reihe **Gold-Niveau bei zwei Olympiaden** erreicht haben: **30 von 42 Punkten** bei der Mathematik-Olympiade IMO 2026 (Gold-Schwelle 29) und **535,4 von 600 Punkten** beim Informatik-Wettbewerb IOI 2026 (Schwelle 361,12).
- Der Unterschied zwischen beiden Ergebnissen zählt: Die IMO-Beweise wurden laut Team **von offiziellen IMO-Prüfern benotet**, der IOI-Lauf war ausdrücklich **inoffiziell und unbeaufsichtigt** – die Punktzahl steht nicht in der offiziellen Rangliste.
- Die IOI-Punktzahl liegt über dem besten menschlichen Ergebnis (498,27). Der Vergleich hinkt trotzdem: Es gab kein Duell, sondern einen nachgestellten Test unter Wettkampfbedingungen.
- Statt eines neuen Riesenmodells beschreibt das Team ein **Rezept**: 22.000 Programmieraufgaben, für Mathematik 414.890 gefilterte Trainingsbeispiele aus 15.818 Beweisaufgaben, dazu eine Suchschleife, die Antworten erzeugt, prüft und nachbessert.
- Modell, Prüfpunkte, Trainingsdaten, Code und ein neuer Test mit 200 Olympiade-Aufgaben sind veröffentlicht – {{Offene Gewichte}}, nachbaubar für jeden mit genug Rechenleistung.
- Alle Zahlen sind Herstellerangaben aus NVIDIAs eigener Messung; unabhängig nachgerechnet hat sie niemand.

## Was passiert ist

Jugendliche, die bei der Internationalen Informatik-Olympiade (IOI) antreten, schreiben Programme, die versteckte Tests bestehen müssen – unter Zeitdruck und mit begrenztem Internet. Bei der Internationalen Mathematik-Olympiade (IMO) schreiben sie Beweise in normaler Sprache, Schritt für Schritt. Beides zusammen zu schaffen gilt als schwer, weil die Fähigkeiten kaum überlappen.

NVIDIA beschreibt in einem [Blogbeitrag vom 7. Oktober 2026](https://huggingface.co/blog/nvidia/nemotron-ioi-and-imo-2026), wie sein Team beide Ziele erreicht hat. Zwei Fachartikel liegen schon seit September auf arXiv, einer [zur Mathematik](https://arxiv.org/abs/2609.10712), einer [zum Programmieren](https://arxiv.org/abs/2609.02849).

Der wichtigste Unterschied steckt im Kleingedruckten. Bei der **IMO 2026** nahm das System offiziell teil, die eingesandten Beweise wurden nach Angaben des Teams von offiziellen IMO-Prüfern benotet: 30 von 42 Punkten, bei vier der sechs Aufgaben die volle Punktzahl, die Gold-Schwelle lag bei 29. Beim **IOI 2026** war es anders. Dort schreibt das Team selbst, sein System sei kein offizieller Teilnehmer gewesen, der Lauf sei nicht von der IOI beaufsichtigt worden, und die Punktzahl sei deshalb nicht in die offizielle Rangliste eingegangen. Die 535,4 von 600 sind ein nachgestellter Test unter Wettkampfbedingungen – kein Wettkampfsieg.

## Das Rezept: Feintuning plus Suchschleife

Nemotron 3 ist eine Familie offener Modelle. Die größte Fassung hat laut Blog 550 Milliarden {{Parameter}}, von denen pro Wortschritt 55 Milliarden aktiv werden – das ist ein {{Mixture-of-Experts}}, bei dem nur ein Teil des Netzes rechnet.

Für den Programmierwettbewerb sammelte das Team 22.000 Aufgaben und ließ dazu Erklärwege erzeugen. Daraus entstanden zwei Spezialfassungen: Nano-CC mit 30 Milliarden Parametern (3 Milliarden aktiv) und Ultra-CC in der Riesengröße. Nano bekam {{Fine-Tuning}} und {{Reinforcement Learning}} – beim Reinforcement Learning lernt ein Modell aus Belohnungen für gute Lösungen –, Ultra nur Feintuning.

{{chart:nemotron-ioi-2025-stufen}}

Die Stufen am Aufgabensatz der IOI 2025 zeigen, woher die Punkte kommen. Nano startete vor dem Nachtraining bei 130 Punkten, das Feintuning brachte es auf 280, Reinforcement Learning auf 291. Erst die Suchschleife mit dem Namen GenCorrect hob es auf 468 Punkte – über die Gold-Schwelle von 438,3. Die große Fassung Ultra-CC kam mit derselben Schleife auf 502 Punkte.

Das ist der Kern der Sache: Der größte Sprung kommt nicht aus einem größeren Modell, sondern aus einer Schleife, die mehrere Antworten erzeugt, sie bewertet und die besten nachbessert. Fachleute nennen das {{Testzeit-Compute}} – Rechenzeit im Moment der Anfrage statt im Training. Bemerkenswert ist außerdem, dass bei der großen Fassung eine einzige Trainingsrunde genügte, um die voll durchtrainierte kleine Fassung bei Aufgaben aus IOI, ICPC und LiveCodeBench Pro zu überholen.

Für Mathematik dreht sich dasselbe Vorgehen um das Prüfen. Der Trainingsdatensatz enthält 414.890 gefilterte Beispiele aus 15.818 verschiedenen Beweisaufgaben – nicht nur fertige Lösungen, sondern auch Kritik, das Finden von Lücken und die Frage, ob ein Beweis überhaupt vollständig ist. Ein zweiter Durchgang mit Reinforcement Learning lief auf 9.597 Aufgaben.

Im Einsatz arbeiten drei Fassungen zusammen: das allgemeine Modell, die feinjustierte und die mit Reinforcement Learning trainierte. Für jede Aufgabe entwerfen sie Beweise, bewerten sie, kritisieren sie und verbessern die aussichtsreichsten Entwürfe. Eine separate Rechenstufe wählt am Ende aus, was eingereicht wird. Das System arbeitete ausschließlich in normaler Sprache, ohne formales Beweissystem, ohne Werkzeuge und ohne Internet.

## Was die Zahlen zeigen

{{chart:nemotron-imo-2026}}

Die 30 von 42 Punkten sind die belastbarere der beiden Zahlen, weil hier offizielle Prüfer benotet haben. Sie sind knapp: vier Punkte über der Gold-Schwelle, und bei zwei der sechs Aufgaben blieb Punktverlust. Es bleibt der Stand eines einzelnen Wettbewerbs, nicht der Beweis, dass ein Modell Mathematik beherrscht. Die bisherige Erfahrung mit solchen Systemen zeigt auch, dass die Prüfung der schwierigere Teil ist – bei OpenAIs Mathematik-Veröffentlichung Anfang Oktober war genau das der Streitpunkt: wie viele der eingesandten Manuskripte tatsächlich maschinell nachgeprüft werden können ([Artikel dazu](openai-veroeffentlicht-722-mathematik-manuskripte-maschinell-geprueft-ist-ein-fuenftel.html)).

{{chart:nemotron-ioi-2026}}

Bei der IOI liegen 535,4 Punkte deutlich über der Gold-Schwelle von 361,12 und über dem besten menschlichen Ergebnis von 498,27. Ein direkter Vergleich ist das nicht: Der Lauf fand zwar unter denselben Zeit-, Internet- und Abgaberegeln statt wie bei menschlichen Teilnehmern, aber ohne Aufsicht und außerhalb der Wertung. Der Blog nennt auch keine Zahl, wie oft das System bei diesem Lauf danebenlag – nur das Endergebnis.

Veröffentlicht ist trotzdem alles: Das [Modell Ultra-CC](https://huggingface.co/nvidia/NVIDIA-Nemotron-Labs-3-Competitive-Coding-550B-A55B-NVFP4), eine [Sammlung mit beiden Prüfpunkten, Trainingsdaten und dem neuen Test Nemotron-IMO-Bench](https://huggingface.co/collections/nvidia/nemotron-labs-imo-2026) mit 200 Aufgaben auf Olympiadeniveau, dazu die Abläufe und Prompts im [NeMo-Skills-Repository](https://github.com/NVIDIA-NeMo/Skills). Wer die Rechenleistung hat, kann die Messung mit demselben Material wiederholen.

## Warum das zählt

Erstens wandert die Botschaft: Fortschritt bei schwierigen Aufgaben entsteht nicht nur dadurch, dass ein Grundmodell immer größer wird. NVIDIA beschreibt den Erfolg ausdrücklich als Zusammenarbeit von Modell, Daten und der Schleife, die am Ende die Antwort auswählt. Ein {{Reasoning}}-Sprung kann also auch aus der Verpackung kommen – und diese Verpackung ist hier kein Geheimnis.

Zweitens zeigt der Fall, wie unterschiedlich streng „Gold" sein kann. Bei der Mathematik sagen offizielle Prüfer ja, bei der Informatik sagt es das Team selbst. Diese Unterscheidung nachvollziehbar zu dokumentieren, statt sie zu verwischen, ist ungewöhnlich – die meisten Ankündigungen in diesem Feld machen es andersherum.

Drittens steht die Frage im Raum, was ein solcher Spezialist für normale Arbeit bedeutet. Ein System, das pro Aufgabe mehrere Beweise schreibt, kritisiert und verbessert, verbraucht ein Vielfaches an Rechenzeit. Die Methode ist also nicht der billige Weg zu einem besseren Assistenten, sondern der teure Weg zu einem sehr guten Spezialisten.

## Was heißt das praktisch

Wer ein offenes Modell für eine enge Fachaufgabe braucht, findet hier ein Vorgehen zum Nachbauen: ein starkes Grundmodell nehmen, Aufgaben mit guten Lösungswegen sammeln, feinjustieren, und die Ausgabe mit einer Bewertungs- und Verbesserungsschleife nachschärfen. Das funktioniert nicht nur für Beweise, sondern überall dort, wo sich ein Ergebnis automatisch prüfen lässt – Code, Rechenwege, strukturierte Daten.

Die Einschränkungen gehören dazu. Alle Werte sind Herstellerangaben aus NVIDIAs eigener Messung, nachgemessen hat sie niemand. Der IOI-Lauf war nicht beaufsichtigt, und wie die Ergebnisse mit einem anderen Aufgabensatz oder anderem Zeitlimit aussehen würden, steht nirgends. Für den eigenen Einsatz heißt das: nicht die Olympiade-Punkte zählen, sondern ein eigener Test mit eigenen Aufgaben.

## Quellen

- [NVIDIA: One Model Family, Two Gold-Level Results – Fine-Tuning Nemotron for IOI and IMO](https://huggingface.co/blog/nvidia/nemotron-ioi-and-imo-2026) (Hugging Face Blog, 7. Oktober 2026) – alle genannten Zahlen, Trainingsmengen und die Einschränkung zum IOI-Lauf
- [An Open Recipe for IMO Gold: Training Nemotron for Olympiad Mathematics](https://arxiv.org/abs/2609.10712) (arXiv, 9. September 2026) – IMO-System, 30 von 42 Punkten, freigegebene Prüfpunkte und Daten
- [IOI-Papier: Nemotron für Wettbewerbsprogrammierung](https://arxiv.org/abs/2609.02849) (arXiv, September 2026) – GenCorrect und die IOI-Ergebnisse
- [Modellkarte Nemotron-3-Ultra-CC](https://huggingface.co/nvidia/NVIDIA-Nemotron-Labs-3-Competitive-Coding-550B-A55B-NVFP4) – 550 Milliarden Parameter, davon 55 Milliarden aktiv
- [Sammlung Nemotron Labs IMO 2026](https://huggingface.co/collections/nvidia/nemotron-labs-imo-2026) – Prüfpunkte, Trainingsdaten, Nemotron-IMO-Bench mit 200 Aufgaben
- [NeMo-Skills-Repository](https://github.com/NVIDIA-NeMo/Skills) – Abläufe, Prompts und eingereichte Lösungen
