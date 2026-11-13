---
title: "Gemini 4 Hydrogen schlägt das eigene Frontier-Modell, aber nur auf einem Index"
slug: "gemini-4-hydrogen-schlaegt-das-eigene-frontier-modell-aber-nur-auf-einem-index"
date: 2026-11-12
time: "19:00"
status: published
tags: [news, modelle, gemini, google, deepmind, agenten, benchmark]
summary: "Google hat am 12. November Gemini 4 Hydrogen vorgestellt, ein aus Gemini 4 Carbon abgeleitetes Modell für schnelle Agentenarbeit, das ab sofort auch Google Search für alle Nutzer antreibt. Der Preis liegt flach bei 1,50 und 7,50 Dollar je Million Token über eine Million Token Kontext. Auf dem unabhängigen Index von Artificial Analysis erreicht Hydrogen 54 Punkte bei 3,16 Dollar je Aufgabe, während GPT-6.1 Sol 55 Punkte für 1,27 Dollar schafft. Googles eigener Vergleich mit dem Frontier-Modell Argon hält nur auf einem Konglomerat-Index, und bei Terminal- und Computer-Use-Tests liegt die Konkurrenz vorn."
source_url: "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/"
source_name: "Google"
lang: de
---

## TL;DR

- Google hat am 12. November Gemini 4 Hydrogen vorgestellt, ein aus Gemini 4 Carbon abgeleitetes Modell für schnelle Agentenarbeit. Es läuft in der Gemini-API, in AI Studio, in der Gemini-App, in Google Search und für zahlende Abonnenten in Antigravity.
- Der Preis liegt bei 1,50 Dollar je Million Eingabetoken und 7,50 Dollar je Million Ausgabetoken, flach über das ganze {{Kontextfenster}} von einer Million {{Token}}. Zwischengespeicherte Eingaben kosten 0,075 Dollar.
- Auf dem Artificial Analysis Intelligence Index erreicht Hydrogen in der höchsten Denkstufe xhigh 54 Punkte, in der Standardstufe high 51. Google vergleicht das mit dem eigenen Frontier-Modell Argon, das bei 50 steht, und mit Carbon, das 59 bis 60 erreicht.
- Unabhängig gemessen ist der Vorsprung schmal und der Preis pro Aufgabe hoch: 3,16 Dollar je Indexaufgabe bei xhigh, GPT-6.1 Sol kommt auf 55 Punkte für 1,27 Dollar. Bis zum ersten Antworttoken dauert es bei xhigh 40,55 Sekunden, der Median der Preisklasse liegt bei 13,61 Sekunden.
- Die {{Modellkarte}} nennt 64.000 Ausgabetoken im normalen Betrieb, eine Million nur im Hintergrundmodus, Wissensstand März 2026 und mehr ungerechtfertigte Ablehnungen als beim Vorgänger.

## Was ist passiert

Koray Kavukcuoglu, Senior Vice President bei Google DeepMind, hat das Modell am 12. November im Google-Blog angekündigt ([Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/)). Hydrogen ist laut Modellkarte aus Gemini 4 Carbon abgeleitet, dem Spitzenmodell, das Google Anfang November für zahlende Entwickler freigegeben hat ([unser Artikel zu Carbon](https://hermiethetermi.github.io/hermies-blog/gemini-4-carbon-googles-neues-spitzenmodell-findet-88-prozent-der-sicherheitsluecken.html)). Neu ist die Rolle: Hydrogen soll nicht die schwierigsten Aufgaben lösen, sondern schnell und diszipliniert ausführen, was Carbon und Argon geplant haben.

Vier Denkstufen sind einstellbar: low, medium, high und das neue xhigh. high ist die Voreinstellung. Der Preis ist der eigentliche Bruch mit dem Vorgänger. Er gilt flach über das gesamte Fenster von einer Million Token, ohne Aufschlag für lange Eingaben, und Ausgabetoken werden mitgezählt, auch die, die das Modell zum Nachdenken verbraucht.

Google liefert die übliche Batterie eigener Messungen mit. Auf Terminal-Bench 4.1 kommt Hydrogen auf 57,0 Prozent, der Vorgänger 3.8 Flash auf 18,2 Prozent, bei 2,5-facher Geschwindigkeit und nach Google-Angaben fünfmal weniger erfundenen Behauptungen. In der eigenen Vergleichstabelle gewinnt Hydrogen sieben von zehn Zeilen gegen Claude Sonnet 5.5 und GPT-6.1 Terra ([zusammengefasst bei NeuralTrust](https://neuraltrust.ai/blog/gemini-4-hydrogen)). Es verliert die drei Terminal- und Computer-Use-Tests: 57,0 gegen 63,9 Prozent auf Terminal-Bench 4.1, 77,6 gegen 83,9 Prozent auf OSWorld-2.1, 51,4 gegen 59,9 Prozent auf Terminal-Bench-Science.

{{tabelle:hydrogen-vergleich}}

## Warum zählt es

Die Ankündigung enthält einen Satz, der in der Modelllandschaft neu ist: Hydrogen übertrifft Argon auf dem Intelligence Index, in der Standardstufe mit 51 gegen 50 Punkte. Ein günstigeres Modell schlägt also das eigene Flaggschiff. Der Satz hält nur, weil Argon ein anderes Ziel hat. Argon ist auf lange Ausgaben und mehrstündige Aufgaben ausgelegt, mit bis zu einer Million Ausgabetoken, und erreicht auf dem Konglomerat-Index von Artificial Analysis nur 50 Punkte. Carbon, im September noch als zweite Frontier-Stufe positioniert, liegt bei 59 bis 60 ([The Decoder](https://the-decoder.com/googles-gemini-4-hydrogen-outscores-the-bigger-argon-just-four-weeks-after-its-launch/)). Googles Modellreihe ist damit schwer zu lesen: Das mittlere Modell führt den Index an, das große führt die Ausgabelänge an, und das neueste liegt dazwischen.

Wichtiger als der interne Vergleich ist der Verteilkanal. Hydrogen läuft ab sofort in Google Search für alle Nutzer, weltweit, ohne Anmeldung und ohne Wahlmöglichkeit. Bisher war dort ein Flash-Modell der 3er-Reihe im Einsatz. Diese Reichweite hat kein anderes Modell der Branche, und sie verändert, was ein guter Prozentpunkt auf einem Benchmark bedeutet: Die Antworten, die billionenfach ausgeliefert werden, kommen künftig aus einem Modell, dessen Fehlerquote auf Terminal-Bench 4.1 bei 43 Prozent liegt.

Der dritte Punkt ist die Rechnung pro Aufgabe. Ein {{Reasoning}}-Modell verbraucht Ausgabetoken zum Denken, und Hydrogen denkt viel. Artificial Analysis hat auf seinem Index 304 Millionen Ausgabetoken gemessen, der Median vergleichbarer Modelle liegt bei 72,8 Millionen. Bei 7,50 Dollar je Million Ausgabetoken ist das der Grund, warum eine Indexaufgabe 3,16 Dollar kostet und nicht 1,50. Zum Vergleich: Claude Sonnet 5.5 kostet bei ähnlichem Ergebnis 10,04 Dollar, GPT-6.1 Sol 1,27 Dollar bei 55 Punkten. Hydrogen sitzt in der Mitte, ist aber nicht das Schnäppchen, das der Tokenpreis vermuten lässt.

## Was heißt das praktisch

Wer von 3.8 Flash kommt, zahlt künftig doppelt so viel pro Token. Der alte Flash kostet bis zum 31. Dezember 2026 noch 0,75 und 3,75 Dollar, danach denselben Preis wie Hydrogen. Die Migration ist damit keine Ersparnis, sondern ein Qualitätssprung zum gleichen Preis: 51 gegen 31 Punkte auf dem Index und 57 gegen 18,2 Prozent auf Terminal-Bench 4.1.

Für Agenten, die Terminals und Bildschirme bedienen, bleibt die Konkurrenz vorn. Sonnet 5.5 gewinnt die drei einschlägigen Tests in Googles eigener Tabelle, und das ist die Tabelle des Anbieters. Wer einen Computer-Use-Agenten baut, sollte beide Modelle auf den eigenen Aufgaben messen, bevor er wechselt.

Bei der Geschwindigkeit ist die Denkstufe entscheidend. Auf high antwortet Hydrogen nach 16,7 Sekunden, eine Indexaufgabe dauert 7,9 Minuten und kostet 1,87 Dollar. Auf xhigh sind es 40,55 Sekunden bis zum ersten Token und 13,7 Minuten, während der Median der Preisklasse bei 13,61 Sekunden liegt. Artificial Analysis stuft das Modell deshalb als langsamer ein als vergleichbare Modelle. Wer xhigh einschaltet, zahlt diese Zeit bei jeder Anfrage.

Ein Tarifdetail lohnt die Prüfung vor der Planung. Hydrogen ist in AI Studio für alle Stufen verfügbar und im bezahlten Google-AI-Pro und Ultra auch in Antigravity. Kostenlose Nutzer der Gemini-App bekommen es nur über die automatische Modellauswahl, nicht als feste Wahl. Wer einen Agenten auf Antigravity stützen will, braucht das Abonnement.

::: aufklappen Was die Modellkarte einräumt

Die Modellkarte ist bei Google traditionell der ehrlichste Teil der Veröffentlichung, weil sie Dinge nennt, die im Blog fehlen.

- Das Ausgabelimit liegt im normalen Betrieb bei 64.000 Token. Eine Million sind nur über den Hintergrundmodus für lange Ausgaben erreichbar.
- Der Wissensstand endet im März 2026.
- Die Rate ungerechtfertigter Ablehnungen steigt gegenüber 3.8 Flash um 5,57 Prozentpunkte, besonders bei multimodalen Anfragen.
- Hydrogen erreicht nach Googles eigener Frontier-Safety-Prüfung keine kritische Schwelle bei biologischen und Cyber-Risiken, aber die Warnschwellen in beiden Bereichen. Der vollständige Sicherheitsbericht steht noch aus.

:::

Für Aufgaben, bei denen Fehler teuer sind, bleibt die Belastbarkeit der Zahlen offen. Alle Genauigkeitswerte in Googles Tabelle stammen aus Googles Suite. Der unabhängige Index von Artificial Analysis bestätigt die Größenordnung, nicht die Rangfolge: Dort liegt Hydrogen bei xhigh gleichauf mit Sonnet 5.5 und GPT-6.1 Sol, nicht davor.

## Quellen

- Google DeepMind, Koray Kavukcuoglu: *Introducing Gemini 4 Hydrogen*, 12.11.2026. https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/
- Google DeepMind: *Gemini 4 Hydrogen Model Card*, November 2026. https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-4-Hydrogen-Model-Card.pdf
- Google: *Gemini 4 Hydrogen: everyday coding and agentic workflows for developers*, 12.11.2026. https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-4-hydrogen/
- Artificial Analysis: *Gemini 4 Hydrogen (xhigh), Intelligence, Performance and Price Analysis*, abgerufen 13.11.2026. https://artificialanalysis.ai/models/gemini-4-hydrogen
- The Decoder: *Google's Gemini 4 Hydrogen outscores the bigger Argon just four weeks after its launch*, 12.11.2026. https://the-decoder.com/googles-gemini-4-hydrogen-outscores-the-bigger-argon-just-four-weeks-after-its-launch/
- NeuralTrust: *Gemini 4 Hydrogen: Benchmarks and Security*, 12.11.2026 (Googles Vergleichstabelle und Preise des Vorgängers). https://neuraltrust.ai/blog/gemini-4-hydrogen
- heise online: *Gemini 4 Hydrogen: Google's efficient alternative to Argon and Carbon*, 12.11.2026 (Kosten je Aufgabe nach Denkstufe). https://www.heise.de/en/news/Gemini-4-Hydrogen-Google-s-efficient-alternative-to-Argon-and-Carbon-11523905.html
