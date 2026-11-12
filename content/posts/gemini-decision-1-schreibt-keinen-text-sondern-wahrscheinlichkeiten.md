---
title: "Gemini Decision 1 schreibt keinen Text, sondern Wahrscheinlichkeiten"
slug: "gemini-decision-1-schreibt-keinen-text-sondern-wahrscheinlichkeiten"
date: 2026-11-11
status: published
tags: [news, modelle, deepmind, google, agenten, benchmark]
summary: "Google hat am 11. November die Gemini Decisions API und das Modell Gemini Decision 1 vorgestellt: bis zu 1.000 geschlossene Fragen gegen eine gemeinsame Eingabe aus Text, Bild, Audio, Video und PDF, Antwort als kalibrierte Wahrscheinlichkeit in 150 bis 250 Millisekunden, 0,10 Dollar pro Million Eingabetoken und keine Ausgabetoken. In Googles eigener Vergleichstabelle hat das Modell den niedrigsten Kalibrierungsfehler, Jev von TypeSafe gewinnt dafür die zwei Werkzeug-Benchmarks und kostet 0,042 Dollar. Alle Genauigkeitswerte stammen aus Googles Suite; Entwicklertests auf Hacker News messen bessere Wahrscheinlichkeiten als Jev bei doppeltem Preis."
source_url: "https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/"
source_name: "Google"
lang: de
---

## TL;DR

- Google hat am 11. November die Gemini Decisions API vorgestellt, angetrieben von einem neuen Modell namens Gemini Decision 1. Es schreibt keinen Text. Es bewertet vorgegebene Antwortmöglichkeiten und gibt Wahrscheinlichkeiten zurück.
- Eine Anfrage kann ein gemeinsames Eingabebild aus Text, Bildern, Audio, Video und PDFs tragen, bis 256.000 {{Token}}, dazu bis zu 1.000 Fragen. Die Antwort kommt in 150 bis 250 Millisekunden.
- Der Preis liegt bei 0,10 Dollar pro Million Eingabetoken, Ausgabetoken kosten nichts, weil keine entstehen. Genau so viel verlangt OpenAI für seine Decisions API, Jev von TypeSafe kostet 0,042 Dollar.
- In Googles eigener Vergleichstabelle hat das Modell den niedrigsten Kalibrierungsfehler: 0,0250 gegen 0,0494 bei Jev und 0,0721 bei GPT-6 Luna. Es gewinnt sieben von neun Genauigkeits-{{Benchmark}}s, Jev gewinnt die zwei Aufgaben zur Werkzeugwahl.
- Entwickler auf Hacker News berichten von eigenen Tests mit deutlich besserem Brier-Score als Jev, aber doppeltem Preis. Das Modell läuft bisher nur in AI Studio, nicht in Vertex.

## Was ist passiert

Die Ankündigung steht seit dem 11. November im Google-Blog, geschrieben von Min Choi und Felix Yu, beide bei Google DeepMind ([Google](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/)). Das Muster ist bekannt. TypeSafe hat im Oktober mit Jev vorgelegt, OpenAI kurz darauf mit seiner Decisions API. Google übernimmt es fast unverändert: Statt eine Antwort zu formulieren, bekommt das Modell eine Frage mit erlaubten Antworten und liefert eine Zahl zwischen null und eins.

Technisch ist es ein eigener Endpunkt neben der Gemini-API, den Google `v1beta/decisions` nennt und über Google AI Studio freigibt ([Dokumentation](https://aistudio.google.com/docs/decisions-api)). Der Aufruf besteht aus zwei Teilen: einer gemeinsamen Eingabe, die Text, Bild, Audio, Video und PDF sein kann, und einer Liste von Fragen. Drei Typen sind erlaubt. `noul` schätzt die Wahrscheinlichkeit, dass eine Ja/Nein-Bedingung zutrifft. `choice` wählt aus zwei bis 255 Optionen eine aus und gibt die Wahrscheinlichkeit für jede zurück. `score` bewertet entlang einer geordneten Skala und liefert einen mit Wahrscheinlichkeiten gewichteten Durchschnitt.

Das Modell arbeitet in einem einzigen Vorwärtsdurchlauf, ohne Zwischentext. Deshalb die Zahlen: 50 bis 100 Millisekunden Rechenzeit auf dem Modell, 150 bis 250 Millisekunden von der Anfrage bis zur Antwort, gemessen bis 16.000 Token Kontext. Die Latenz bleibt laut Google fast gleich, ob man eine Frage stellt oder hundert. Bis zu 1.000 Fragen pro Aufruf sind erlaubt, das Eingabefenster liegt bei 262.144 {{Token}}.

## Warum zählt es

Vor sechs Wochen war das eine Nische. Jev war am 4. Oktober das erste Modell, das nichts anderes tat, als typisierte Entscheidungen mit Wahrscheinlichkeiten zu liefern. OpenAI zog am 22. Oktober nach. Jetzt hat die dritte große Firma dasselbe Werkzeug, und damit ist die Frage nicht mehr, ob es diese Modellklasse gibt, sondern wer sie bedient.

Der Grund für das Tempo liegt im Bau von {{Agent}}en. In einem Agentenlauf fallen ständig kleine Entscheidungen an: Ist diese Nachricht ein Ticket oder Spam? Reicht die Antwort, um fortzufahren? Darf dieser Schritt ohne Menschen laufen? Ein Sprachmodell beantwortet jede dieser Fragen mit einem Absatz, obwohl am Ende ein Ja, ein Nein oder eine von fünf Optionen gebraucht wird. Das kostet Zeit und Token. Ein Entscheidungsmodell dreht das um: Der Antwortraum ist begrenzt, also lässt sich die Rechenzeit begrenzen.

Google unterscheidet sich von den beiden Vorläufern an zwei Stellen. Die erste ist das Medium. Gemini Decision 1 liest Audio, Video und PDFs direkt, nicht nur Text, und genau das fehlte Jev und GPT-6 Luna. Wer Anrufmitschnitte gegen Betrugsregeln prüft oder Schadensfotos gegen eine Versicherungspolice, kann beides in einen Aufruf legen. Die zweite ist die {{Kalibrierung}}. Google wirbt nicht mit Trefferquote, sondern damit, dass die angegebene Konfidenz zur tatsächlichen Trefferquote passt. Wenn der Code bei 0,7 eine Entscheidung trifft, soll das in 70 Prozent der Fälle richtig sein. Nur dann lässt sich eine Schwelle setzen, ab der ein Mensch übernimmt.

{{tabelle:entscheidungsmodelle}}

Google setzt das Modell selbst ein, und diese Beispiele sind der ehrlichste Teil der Ankündigung. Die Labs-App CC wählt damit aus über 200 Emoji-Reaktionen in Bruchteilen einer Sekunde. Stitch verarbeitet Sprach- und Tippbefehle auf der Leinwand. Gemini Notebook schickt jede eingehende Anfrage durch das Entscheidungsmodell, um sie der richtigen Modellstufe zuzuordnen, und spart damit nach Google-Angaben bis zu 40 Prozent Latenz bei alltäglichen Fragen ([DataCamp](https://www.datacamp.com/blog/gemini-decision-1)).

## Was heißt das praktisch

Die Preisfrage ist schnell beantwortet und dann kompliziert. 0,10 Dollar pro Million Eingabetoken klingt billig, und weil keine Ausgabetoken anfallen, ist es tatsächlich billiger als jede Variante, die erst einen Satz schreibt und ihn dann auswertet. Google rechnet vor, dass die Decisions API über die gemeinsame Testsuite knapp fünfmal günstiger ist als Gemini 3.5 Flash-Lite über die normale Schnittstelle. Der Vergleich geht gegen das eigene Haus. Jev kostet 0,042 Dollar pro Million Token, also weniger als die Hälfte, und Entwickler auf Hacker News rechnen vor, dass auch Liquid mit 0,02 Dollar pro Million deutlich darunter liegt.

Auf Hacker News hat die Ankündigung 530 Punkte und 152 Kommentare gesammelt ([Diskussion](https://news.ycombinator.com/item?id=50456791)). Darunter sind Messungen, die über die Herstellerangaben hinausgehen. Ein Entwickler berichtet, er habe das Modell gegen Jev laufen lassen und einen vierfach niedrigeren Brier-Score bekommen, je nach Aufgabe zwischen zwei- und sechsfach. Der Brier-Score misst, wie gut eine Wahrscheinlichkeit zur Wirklichkeit passt, kleiner ist besser. Sein p50 lag über 100 Millisekunden niedriger, der Preis über die ganze Testreihe aber doppelt so hoch. Ein anderer nennt die Audio-, Video- und Dateieingabe „sehr attraktiv" und genau den Punkt, an dem er es einsetzen würde.

Die Einwände sind ebenso konkret. Ein Kommentator hält die Kalibrierung für nicht übertragbar: Man könne ein Modell nicht für Aufgaben vorab kalibrieren, die man noch nicht kennt, dafür brauche es pro Aufgabe einen eigenen Kalibrierungssatz. Das trifft den Kern des Werbeversprechens. Ein anderer bekam beim Testen die Meldung, seine Eingabe verstoße gegen Googles Regeln für zulässige Nutzung, was bei einem Entscheidungswerkzeug für Firmendaten ein praktisches Problem ist. Und wer das Modell in Vertex erwartet, also in Googles Enterprise-Plattform, wird vertröstet: Es läuft vorerst in AI Studio.

Zwei Einschränkungen stehen in der Dokumentation und nicht in der Ankündigung. Die Decisions API unterstützt kein Context Caching, wiederkehrender Kontext wird also jedes Mal neu berechnet. Und sie nimmt keine YouTube- oder Cloud-Storage-Links an, Videos müssen als Datei kommen.

::: warnung
Alle Genauigkeits- und Kalibrierungswerte stammen aus Googles eigener Testsuite, die das Unternehmen selbst zusammengestellt hat. Unabhängig nachgemessen hat sie niemand. Die eine Fremdmessung, die es gibt, kommt aus einem Hacker-News-Kommentar ohne veröffentlichten Testaufbau. Wer das Modell produktiv einsetzt, sollte die Konfidenzschwelle an eigenen Daten ziehen, nicht an der Tabelle aus der Ankündigung.
:::

## Quellen

- Google: „Gemini Decisions API: Fast, calibrated multimodal decisions", 11.11.2026, Min Choi und Felix Yu: https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/
- Google AI Studio, Modellkarte Gemini Decision 1, abgerufen 12.11.2026: https://aistudio.google.com/docs/models/gemini-decision-1
- Google AI Studio, Dokumentation Decisions API, abgerufen 12.11.2026: https://aistudio.google.com/docs/decisions-api
- DataCamp: „Gemini Decision 1: Benchmarks, Pricing, and Access", 12.11.2026: https://www.datacamp.com/blog/gemini-decision-1
- Hacker News, Diskussion zur Ankündigung, 11.11.2026 (530 Punkte, 152 Kommentare): https://news.ycombinator.com/item?id=50456791
- TypeSafe AI, Ankündigung Jev, 4.10.2026, Preis 0,042 Dollar pro Million Eingabetoken: https://typesafe.ai/blog/introducing-system-one-models-and-jev
- OpenAI, Decisions API, 22.10.2026, Preis 0,10 Dollar pro Million Eingabetoken: https://openai.com/index/decisions-api
