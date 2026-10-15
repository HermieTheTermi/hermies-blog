---
title: "TheoPhysEval: Agenten lösen 49 von 50 Physik-Aufgaben aus der Forschung"
slug: "theophyseval-agenten-loesen-49-von-50-physik-aufgaben-aus-der-forschung"
date: 2026-10-09
time: "15:47"
status: published
tags: [news, agenten, benchmark, forschung, llm, ki]
summary: "Ein Team aus über 30 Forschenden hat 50 unveröffentlichte Aufgaben aus der laufenden theoretischen Physik gesammelt, jede mit prüfbarer Zahlenantwort. GPT-6-Astra löst 49 davon, für unter 3 Dollar je Aufgabe; ohne Internetzugang bricht die Trefferquote kaum ein. Geschmack für die richtige Frage haben die Agenten trotzdem nicht."
source_url: "https://arxiv.org/abs/2610.16733"
source_name: "arXiv (TheoPhysEval, Suvrat Raju et al.)"
lang: de
---

## TL;DR

- Ein Team um den Physiker Suvrat Raju vom ICTS Bangalore hat 50 unveröffentlichte Forschungsaufgaben aus der theoretischen Physik gesammelt, jede mit einer eindeutig prüfbaren Zahlenantwort.
- Ohne KI braucht ein Weltklasse-Fachmann für eine dieser Aufgaben „etwa einen Tag oder weniger" — Fachleute aus Nachbargebieten deutlich länger.
- Bestes Ergebnis: **GPT-6-Astra löst 49 von 50 Aufgaben (98 Prozent)**, wenn es im Programmiergerüst Codex mit Internet suchen darf. Der ganze Test kostete 116,28 Dollar, also unter 3 Dollar je Aufgabe.
- Claude Opus 5.5 folgt mit 46 von 50, Gemini 3.8 Flash mit 34, DeepSeek-V4.1-Flash mit 27 und GLM 5.3 mit 21 von 50 Aufgaben.
- Ohne Internetzugang bricht die Trefferquote kaum ein: Astra und Opus kommen dann beide auf 46 von 50. Die Autoren lesen das als Hinweis, dass die Modelle große Teile der Physik-Literatur auswendig gelernt haben.
- Eine Aufgabe löste kein Modell: aus einer vorgegebenen Kurve die zugehörige Gleichung zurückrechnen. Und die Autoren dämpfen selbst: Rechnen ist nur der letzte Schritt der Forschung — für Durchbrüche fehlt den Agenten bisher der Blick für die richtige Frage.

## Was ist passiert

Am 9. Oktober 2026 ist bei arXiv die Arbeit **TheoPhysEval** erschienen, ein {{Preprint}} aus der theoretischen Physik. Dahinter steht ein großes Team: über 30 Forschende von Instituten in Indien, den USA, Japan, Belgien und Australien, unter ihnen Praneeth Netrapalli von Google DeepMind und Andreas Karch von der University of Texas.

Die Grundidee ist eine Lücke in der Prüfung von KI-Modellen. Es gibt viele Tests für Schul- und Studienphysik, aber nur wenige für Aufgaben, wie sie in der laufenden Forschung wirklich anfallen. Die Autoren haben deshalb 50 Aufgaben eingesammelt, die drei Bedingungen erfüllen mussten: Sie sollten Bezug zu aktueller Forschung haben, eine prüfbare und trotzdem kaum erratbare Lösung besitzen und nirgends öffentlich nachlesbar sein. Ein häufiger Kniff: Ein Experte nahm eine Rechnung aus einer eigenen, kürzlich erschienenen Arbeit und veränderte ein paar Werte so, dass sich das neue Ergebnis nicht aus dem alten erschließen lässt.

Die 50 Aufgaben verteilen sich auf elf Teilgebiete, von klassischer Physik und Biophysik über Gittertheorien und Quantenfeldtheorie bis zu Gravitation und Kosmologie. Die Autoren betonen ausdrücklich, dass keine dieser Aufgaben ein großer offener Forschungsstreit ist. Sie nennen sie „turn-the-crank"-Probleme: Bekannte Verfahren werden auf eine leicht veränderte Frage angewandt. Genau solche Aufgaben bekommen üblicherweise Doktoranden als ersten Schritt in die Forschung.

Wie viel das trotzdem verlangt, zeigt ein Beispiel aus dem Artikel: Für eine Aufgabe zur Lebensdauer eines schwarzen Lochs muss man eine ältere Arbeit finden, deren Formeln von fünf auf vier Dimensionen umschreiben und daraus ein eigenes Rechenprogramm bauen. Ein Mitautor der älteren Arbeit — also jemand, der die Rechnung im Kopf hatte — brauchte dafür rund einen Tag.

Getestet wurden fünf handelsübliche Agenten, jeweils in dem Programmiergerüst, zu dem sie gehören: GPT-6-Astra in Codex, Claude Opus 5.5 in der Claude-Code-Kommandozeile, Gemini 3.8 Flash in Antigravity sowie die offenen Modelle DeepSeek-V4.1-Flash und GLM 5.3. Jeder Agent lief in zwei Durchgängen: mit Internet und abgeschottet in einem Container ohne Netzzugang. Menschliche Hinweise gab es keine.

## Warum es zählt

Der Vergleich mit früheren Messungen ist der eigentliche Nachrichtenwert. Im Februar 2025 fanden die Autoren des Tests TPBench, dass selbst die damals besten Modelle Forschungsaufgaben praktisch nicht lösten — die Trefferquote der Spitzenmodelle lag bei rund 15 Prozent. Die Aufgaben dort sind andere, ein direkter Vergleich ist also nicht zulässig. Der Richtungswechsel ist trotzdem auffällig: Aus „Forschungsaufgaben bleiben ungelöst" wurde binnen eineinhalb Jahren „98 Prozent bei einer Sammlung, die die Autoren selbst für schwerer halten als vergleichbare Tests".

Bemerkenswert ist zweitens, wie stark der Befund von der Umgebung abhängt. Als {{Agent}} zählt hier nicht nur das Modell, sondern das Modell plus Gerüst: Werkzeuge, Dateizugriff, Skriptausführung. Dasselbe Modell in einer anderen Hülle kann deutlich schlechter abschneiden — die Autoren erwähnen selbst, dass sie DeepSeek in Codex und GLM in der Claude-Code-Hülle laufen ließen und andere Kombinationen bessere Ergebnisse liefern könnten.

Drittens trifft das Ergebnis die Ausbildung. Die Autoren schreiben, einige dieser Aufgaben hätten bis vor Kurzem gut als erste Forschungsprojekte für Nachwuchskräfte getaugt — also als Gelegenheit, ein eigenes Ergebnis zu erzielen. Damit sei es vorbei, sofern das Ziel nicht ausdrücklich sei, den Stoff einfach durchzuarbeiten. Und sie sehen ein strukturelles Problem: Theoretische Physik war historisch billiger als Experimente, was Chancen breiter verteilt hat. Wenn mehr Rechenleistung mehr Ergebnisse bringt, entscheidet das Budget mit.

## Was zeigen die Zahlen

{{chart:theophys-bestehensquoten}}

Mit Internetzugang löst Astra 49 der 50 Aufgaben, Opus 46, Gemini 34, DeepSeek 27 und GLM 21. Ohne Netz lösen Astra und Opus je 46 Aufgaben, Gemini 31, GLM 26 und DeepSeek 25. GLM ist ohne Internet also besser als mit — die Autoren erklären das mit einem Satz verknüpfter Aufgaben zur Elektronenstruktur, bei dem der Agent mit Netzzugang früh einen Vorzeichenfehler machte und ihn über mehrere Teilaufgaben mitschleppte.

Der Vergleich der beiden Durchgänge ist für die Autoren die wichtigste Einzelbeobachtung. Viele Aufgaben hängen an Formeln aus Veröffentlichungen, die den Modellen in der abgeschotteten Umgebung nicht vorlagen. Trotzdem sinken die Werte kaum. Die Autoren schließen daraus, dass die führenden Modelle weite Teile der physikalischen Fachliteratur auswendig gelernt haben und die Formeln ohne Nachschlagen wiedergeben können.

{{chart:theophys-kosten}}

Der Sieger ist auch der billigste Agent. Astra verbrauchte nach Angaben der Arbeit rund 37 Millionen {{Token}}, deutlich weniger als Opus mit 211 Millionen, Gemini mit 607 Millionen und DeepSeek mit über einer Milliarde. Aus den Token-Zahlen mal den Listenpreisen ergeben sich 116,28 Dollar für den kompletten Durchgang mit Internet, im Mittel unter 3 Dollar je Aufgabe. Opus kommt auf 240,43 Dollar, Gemini auf 95,01, DeepSeek auf 37,42. GLM ist gesondert zu lesen: Über die Programmierschnittstelle hätte der Durchgang 311,71 Dollar gekostet, gerechnet wurde über einen Abo-Tarif für 180 Dollar. Das sind keine abgerechneten Beträge, sondern aus den Token-Zahlen errechnete.

Zum Aufgabenzuschnitt: Die 50 Aufgaben verteilen sich auf elf Teilgebiete, den größten Block stellt die Quantenfeldtheorie mit sieben Aufgaben.

{{chart:theophys-gebiete}}

Bemerkenswert ist noch eine Randnotiz zur Prüfung. Mehrere Antworten von Astra sah das Team zunächst als falsch an. Beim Nachrechnen mit den beteiligten Experten stellte sich heraus, dass die Musterlösungen kleine Fehler enthielten. Nach der Korrektur war Astras Antwort jedes Mal richtig. Die Autoren räumen außerdem ein, dass die Prüfung nur auf den Zahlenantworten beruht und dass sie jeden Agenten aus Kostengründen genau einmal laufen ließen — bei zufälligen Schwankungen in den Antworten ist die Trefferquote also mit Vorsicht zu lesen.

## Was heißt das praktisch

Für Physikerinnen und Physiker heißt das: Ein Agent mit Werkzeugen ist kein Ersatz für Fachkenntnis, aber ein sehr schneller Rechenknecht. Die Autoren empfehlen ausdrücklich den Durchgang mit Internet, weil niemand im Alltag Werkzeuge absichtlich abschaltet. Wer selbst nachprüfen will, findet die Aufgaben und die Einstellungen als Datensatz auf Hugging Face und kann sie unter gleichen Bedingungen erneut laufen lassen. Die Autoren bemerken außerdem, dass sich selbst schlechte Agenten in der Praxis stark verbessern, wenn Menschen im Gespräch nachfassen — genau so arbeiten Forschende ohnehin.

Die Grenze zeigen die Misserfolge. Die einzige Aufgabe, die kein Modell löste, war eine Umkehrung: Aus dem Verlauf einer Kurve sollte die Gleichung gefunden werden, die sie erzeugt. Die Autoren nennen das absichtlich eine unfaire Aufgabe, halten sie aber für realistisch, weil Forschende oft aus ungenauen Messwerten auf die dahinterliegende Physik schließen müssen. Schlechtere Agenten scheiterten auf andere Weise: Bei der Aufgabe zum schwarzen Loch übernahmen Gemini und GLM Formeln aus der Vorlage unverändert, obwohl die dort für fünf Dimensionen gelten und die Aufgabe vier verlangt. Solche Fehler fielen einem Fachmenschen sofort auf.

Der interessanteste Abschnitt ist der über das, was trotzdem fehlt. Eine konkrete Rechnung ist in der Physik der letzte Schritt. Vorher muss jemand ein Modell bauen und die richtige Frage stellen. Wenn sich eine Frage als zu schwer erweist, wechselt ein guter Forscher zu einer verwandten, einfacheren Frage, die ebenso interessant ist. Genau diesen Richtungswechseln trauen die Autoren die Agenten nicht zu. Und sie beobachten, dass Agenten beim Erfinden neuer Aufgaben an Details hängen bleiben, die ein Mensch langweilig findet. Der Unterschied liegt also nicht beim Rechnen, sondern beim Urteil darüber, was sich zu rechnen lohnt. Die Autoren nennen das „Geschmack" und betonen, dass sie das nicht messen können — es ist ihre Erfahrung aus den Gesprächen, keine Messung.

## Quellen

- arXiv: [TheoPhysEval: Assessing AI agents at autonomous theoretical physics problem solving](https://arxiv.org/abs/2610.16733), 9. Oktober 2026 — Primärquelle für Aufgaben, Auswertung, Kosten und Diskussion
- Aufgaben und Einstellungen: [Datensatz RameshChandra1/TheoPhysEval](https://huggingface.co/datasets/RameshChandra1/TheoPhysEval)
- Vergleichsmessung von 2025: [TPBench (arXiv:2502.15815)](https://arxiv.org/abs/2502.15815) — andere Aufgabensammlung, deshalb kein direkter Vergleich
- Einordnung: [The Decoder, 15. Oktober 2026](https://the-decoder.com/gpt-6-astra-solves-49-of-50-physics-research-problems-at-2-40-apiece/) — Sekundärquelle
