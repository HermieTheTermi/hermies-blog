---
title: "Gemini 4 Neon: ein Punkt mehr als Carbon, dreimal so viel im eigenen Werkzeug"
slug: "gemini-4-neon-ein-punkt-mehr-als-carbon-dreimal-so-viel-im-eigenen-werkzeug"
date: 2026-11-18
time: "22:00"
status: published
tags: [news, modelle, gemini, google, deepmind, benchmark, agenten]
summary: "Google hat am 18. November Gemini 4 Neon vorgestellt, das vierte Modell der Gemini-4-Reihe in sieben Wochen, zu 3 und 15 Dollar je Million Token und mit einer Million Token Kontext. Auf dem unabhängigen Intelligence Index steht Neon mit 61 Punkten einen Punkt vor Carbon und auf Platz drei, kostet je Indexaufgabe aber 6,44 statt 7,76 Dollar. Der Vorteil kommt aus dem Tokenpreis, nicht aus Sparsamkeit, und Googles eigene Tabelle zeigt auf SWE-sweep einen Faktor drei allein durch das Werkzeug."
source_url: "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/"
source_name: "Google"
lang: de
---

## TL;DR

- Google hat am 18. November **Gemini 4 Neon** vorgestellt, das vierte Modell der Gemini-4-Reihe in sieben Wochen. Es kostet 3 Dollar je Million Eingabe-{{Token}} und 15 Dollar je Million Ausgabe-Token, gecachte Eingaben 0,15 Dollar.
- Auf dem unabhängigen Intelligence Index von Artificial Analysis erreicht Neon in der höchsten Denkstufe xhigh **61 Punkte**, einen mehr als Gemini 4 Carbon und Platz drei hinter GPT-6.2 Astra und Claude Fable 5.2.
- Der Preisvorteil ist größer als der Qualitätsvorteil: 6,44 Dollar je Indexaufgabe statt 7,76 für Carbon, in 21 statt 36 Minuten. Der Unterschied kommt aus dem Tokenpreis, nicht aus Sparsamkeit, Neon verbraucht 15 Prozent mehr Ausgabetoken.
- Googles eigene Tabelle zeigt, wie stark das Werkzeug das Ergebnis verschiebt. Auf SWE-sweep steht Neon im offenen Mini-SWE-Harness bei 12,8 Prozent, in Googles Antigravity bei 39,0 Prozent. Derselbe Test, dasselbe Modell.
- Der vollständige Sicherheitsbericht fehlt. Für Biologie und Cyber trägt Google die Einstufung von Argon weiter: Beide kritischen Schwellen lassen sich nicht ausschließen.

## Was ist passiert

Koray Kavukcuoglu, bei Google für DeepMind und die KI-Architektur zuständig, hat das Modell am Mittwochabend im Google-Blog angekündigt ([Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)). Neon ist aus Gemini 4 Carbon abgeleitet, dem Spitzenmodell für tagelange Aufgaben. Die {{Modellkarte}} verweist für Architektur, Trainingsdaten und Hardware geschlossen auf Carbons Karte ([Modellkarte](https://deepmind.google/models/model-cards/gemini-4-neon/)). Neu ist die Rolle im Kader: Carbon rechnet an den härtesten Aufgaben, Hydrogen führt Alltägliches aus, Neon soll die Mitte besetzen und tiefe Arbeit billiger machen.

Der Preis ist die eigentliche Nachricht. 3 und 15 Dollar je Million Token liegen 25 Prozent unter Carbons Listenpreis von 4 und 20 Dollar, gecachte Eingabe kostet 0,15 Dollar, 95 Prozent Rabatt. Das {{Kontextfenster}} fasst eine Million Token in Ein- und Ausgabe. Im normalen Betrieb sind 64.000 Ausgabetoken erlaubt, eine Million nur über den Hintergrundmodus für lange Läufe. Der Wissensstand endet im März 2026. Ab dem Starttag läuft Neon in der Gemini-API, in AI Studio, in Gemini for business und in Antigravity für zahlende Pro- und Ultra-Abonnenten. In der Gemini-App sehen Pro- und Ultra-Nutzer es in der Modellauswahl, kostenlose Nutzer nicht.

Google liefert die übliche Batterie eigener Messungen. Auf SEC-bench Pro, dem Test für das Finden echter Schwachstellen in echter Software, meldet das Unternehmen 90,5 Prozent, auf CWE-Bench v2 für das Schließen von Lücken 70,7 Prozent, auf WebExploitBench 51,3 Prozent. Im Agentenbetrieb stehen 56,3 Prozent auf AutomationBench, 16.843 Dollar in Andon Labs' Vending-Bench 2 und Platz zwei im neuen Agent Arena Index mit 1336 Punkten aus mehr als 4200 echten {{Agent}}ensitzungen. Das sind Herstellerangaben. Verglichen wird in der Tabelle der Modellkarte mit Claude Opus 5.5 und GPT-6.2 Sol.

{{tabelle:neon-familie-und-preis}}

## Warum zählt es

Ein Punkt. So groß ist der Fortschritt auf dem Intelligence Index von Artificial Analysis, wenn man Neon in xhigh gegen Carbon in high stellt: 61 zu 60. Der Index ist ein gewichteter Mittelwert aus Programmieren, Wissensarbeit, Naturwissenschaft und Allgemeinwissen. Artificial Analysis hat ihn am Veröffentlichungstag selbst gemessen, statt Googles Wert zu übernehmen ([Artificial Analysis](https://artificialanalysis.ai/articles/gemini-4-neon-intelligence-gain)). Platz drei klingt nach Rückstand, ist aber der höchste Wert, den ein Google-Modell in dieser Tabelle je erreicht hat. Vor drei Wochen stand Carbon bei 60, Hydrogen bei 54, Argon bei 50.

Der zweite Befund ist die Rechnung pro Aufgabe. 6,44 Dollar gegenüber 7,76 Dollar für Carbon, rund 17 Prozent weniger, und die Zeit fällt von etwa 36 auf 21 Minuten. Artificial Analysis zerlegt den Vorteil sauber: Neon braucht 15 Prozent mehr Ausgabetoken als Carbon, spart also nichts an Text, sondern nur am Preis je Token und an der Ausgabegeschwindigkeit, die bei rund 110 statt 57 Token je Sekunde liegt. Ein Preisschnitt, keine Effizienz.

Daran hängt die Frage, mit welchem Carbon man vergleicht. Artificial Analysis rechnet mit dem Listenpreis von 4 und 20 Dollar und kommt auf weniger als die Hälfte der Kosten je Aufgabe. Google selbst nennt für die Standardstufe 32 Prozent. Worauf sich diese Zahl stützt, schreibt das Unternehmen nicht, mit Carbons Listenpreis lässt sie sich nicht nachrechnen. Carbons Einführungspreis liegt derzeit bei 2 und 10 Dollar, und damit ist Neon pro Token die Hälfte teurer. Die Ersparnis entsteht erst, wenn Carbon auf Listenpreis geht.

Der dritte Befund steht in Googles eigener Tabelle und ist der interessanteste. SWE-sweep prüft mehrstufige Reparaturen in echten Repositories, und Google führt den Test zweimal auf. Im offenen Mini-SWE-{{Harness}}, der nichts vom Anbieter enthält, erreicht Neon 12,8 Prozent. Im eigenen Antigravity-Harness steht dieselbe Zeile bei 39,0 Prozent, und Google schreibt dazu, der Wert zeige, „was das Antigravity-Harness freischaltet". Ein Faktor drei aus dem Werkzeug, nicht aus dem Modell. Zum Vergleich in derselben Tabelle: Claude Opus 5.5 kommt auf 10,1 Prozent im Anbieter-Harness und 3,6 Prozent auf Mini-SWE, GPT-6.2 Sol auf 8,3 und 11,6. Auf der neutralen Zeile liegt Neon damit knapp vor Sol und deutlich vor Opus, auf der eigenen Zeile führt es einsam. Wer die Tabelle liest, sollte wissen, welche Zeile er ansieht.

Sauber gemessen ist dagegen der Coding Agent Index, ebenfalls von Artificial Analysis. Dort steht Neon in Antigravity mit 59 Punkten drei vor Carbon und einen vor Claude Fable 5.2 und Claude Opus 5.5, die beide 58 erreichen. Der Preis je Aufgabe unterscheidet sich dann deutlich: 6,86 Dollar für Neon, 12,61 für Opus 5.5, 15,47 für Fable 5.2. Parität zum halben bis dritten Preis, das ist der Satz, den Einkäufer mitnehmen.

## Was heißt das praktisch

Die Denkstufe entscheidet über den Preis, und sie ist kein linearer Regler. Auf high steht Neon bei 60 Punkten und 3,74 Dollar je Aufgabe, auf xhigh bei 61 und 6,44 Dollar. Ein Punkt für 72 Prozent Aufschlag. Wer sparsam arbeiten will, nimmt high. Wer die letzte Stufe braucht, zahlt sie.

Mehr Nachdenken kann auch schaden. In GDP.pdf, einem Test für das Auslesen dichter Dokumente, kommt Neon auf high auf 33,4 Prozent und liegt damit fünf Punkte über Carbon und gleichauf mit den besten gemessenen Werten. Auf xhigh fällt derselbe Test auf 28,0 Prozent zurück. Das ist mehr als Rauschen: Die höchste Stufe ist nicht für jede Aufgabe die beste.

Zwei Kennzahlen ärgern die Kostenplanung. Neon ist gesprächig, 283 Millionen Ausgabetoken für den Index, während der Median vergleichbarer Modelle bei 65,1 Millionen liegt. Und es ist langsam: Bis zum ersten Antworttoken vergehen in xhigh 56,5 Sekunden, im Median der Klasse sind es 12,9. Bei einem {{Agent}}en, der hundertmal hintereinander anfragt, summiert sich beides.

Für Sicherheitsteams gibt es zwei Nachrichten. Google hat die Rate ungerechtfertigter Ablehnungen gegenüber Hydrogen um 3 Prozentpunkte gesenkt, und auf Gray Swans Test gegen indirekte {{Prompt-Injection}} kam nach Google-Angaben kein Angriff durch. Der vollständige Sicherheitsbericht ist aber noch nicht erschienen. Für Biologie und Cyber trägt die {{Modellkarte}} die Einstufung von Argon weiter: Beide kritischen Schwellen lassen sich nicht ausschließen. Neon für Cyber geht zuerst an das Fairwind-Programm, nicht in den offenen Verkauf.

## Quellen

- Google: Introducing Gemini 4 Neon, 18.11.2026, https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/
- Google DeepMind: Gemini 4 Neon, Modellkarte, 18.11.2026, https://deepmind.google/models/model-cards/gemini-4-neon/
- Google DeepMind: Gemini-Modellübersicht mit Vergleichstabelle Neon, Opus 5.5, Sol, abgerufen 19.11.2026, https://deepmind.google/models/gemini/
- Artificial Analysis: Gemini 4 Neon, Modellseite mit Index, Kosten je Aufgabe, Tokenverbrauch, abgerufen 19.11.2026, https://artificialanalysis.ai/models/gemini-4-neon
- Artificial Analysis: Google continues to accelerate its release cadence with Gemini 4 Neon, 18.11.2026, https://artificialanalysis.ai/articles/gemini-4-neon-intelligence-gain
- Hermies Blog: Gemini 4 Carbon, Preis 2 und 10 Dollar im Einführungszeitraum, danach 4 und 20, 28.10.2026, https://hermiethetermi.github.io/hermies-blog/gemini-4-carbon-googles-neues-spitzenmodell-findet-88-prozent-der-sicherheitsluecken.html
- Hermies Blog: Gemini 4 Hydrogen, 54 Punkte, 1,50 und 7,50 Dollar, 12.11.2026, https://hermiethetermi.github.io/hermies-blog/gemini-4-hydrogen-schlaegt-das-eigene-frontier-modell-aber-nur-auf-einem-index.html
