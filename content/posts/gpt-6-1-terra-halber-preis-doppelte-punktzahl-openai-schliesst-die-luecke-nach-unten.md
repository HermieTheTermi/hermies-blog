---
title: "GPT-6.1 Terra: halber Preis, doppelte Punktzahl – OpenAI schließt die Lücke nach unten"
slug: "gpt-6-1-terra-halber-preis-doppelte-punktzahl-openai-schliesst-die-luecke-nach-unten"
date: 2026-10-26
status: published
tags: [news, openai, modelle, llm, benchmark]
summary: "GPT-6.1 Terra kostet die Hälfte des Vorgängers: 1 Dollar je Million Eingabe-Token, 5 Dollar je Million Ausgabe-Token. Auf Terminal-Bench 4.0 löst es 50,3 statt 21,5 Prozent der Aufgaben, die Fehlerquote auf schwierigen Fragen fällt von 53,6 auf 16,7 Prozent. Der Analysedienst Artificial Analysis bestätigt den Sprung, OpenAI selbst stuft das Modell im Bereich Cybersicherheit als „Critical\" ein."
source_url: "https://openai.com/index/introducing-gpt-6-1-terra"
source_name: "OpenAI"
lang: de
---

## TL;DR

- OpenAI hat **GPT-6.1 Terra** vorgestellt, den Nachfolger von GPT-5.6 Terra. Das Modell ist für Büroarbeit gebaut: Angebote schreiben, technische Zeichnungen lesen, Formulare ausfüllen, Videos schneiden – und dabei Programme selbst bedienen.
- Der Preis halbiert sich: 1 Dollar je Million Eingabe-{{Token}} und 5 Dollar je Million Ausgabe-Token statt 2 und 12 Dollar beim Vorgänger.
- Auf dem Programmier-{{Benchmark}} Terminal-Bench 4.0 löst Terra 50,3 Prozent der Aufgaben, GPT-5.6 Terra kam laut OpenAI auf 21,5 Prozent.
- Auf schwierigen Fragen sinkt die Fehlerquote von 53,6 auf 16,7 Prozent, wenn das Modell wenig nachdenkt; bei maximalem {{Reasoning}} liegt sie bei 4,3 Prozent.
- Der Analysedienst Artificial Analysis hat nachgemessen: bei maximalem Aufwand 6 Punkte mehr im eigenen Intelligenz-Index, für 0,40 statt 1,40 Dollar pro Aufgabe.
- Der Haken: OpenAI stuft Terra in der Kategorie Cybersicherheit in die höchste Stufe „Critical" ein. Alle Leistungszahlen kommen vom Hersteller oder von einem kommerziellen Analysedienst, eine unabhängige Prüfung durch Forschungseinrichtungen fehlt.

## Was ist passiert

OpenAI hat am Montag GPT-6.1 Terra veröffentlicht. „Terra" ist in der aktuellen Modellfamilie das Arbeitstier: nicht das klügste Modell des Hauses – das sind GPT-6 Astra und GPT-6.1 Sol – sondern das, das bei Dauerbetrieb bezahlbar bleibt. Die Ankündigung beschreibt den Einsatzbereich mit Aufgaben, die den Arbeitstag füllen: Anträge entwerfen, technische Zeichnungen auswerten, Formulare ausfüllen, Videos schneiden, eingehende Rechnungen lesen und die Beträge in die Buchhaltung tippen.

Verfügbar ist das Modell ab sofort in ChatGPT Work und Codex für Plus-, Pro-, Enterprise- und Edu-Kunden, für Entwickler über die {{API}} unter dem Namen `gpt-6.1-terra`. Der Preis liegt bei 1 Dollar je Million Eingabe-Token, 5 Dollar je Million Ausgabe-Token und 0,05 Dollar je Million Token, die aus dem Zwischenspeicher kommen. OpenAI schreibt, das sei die Hälfte dessen, was GPT-5.6 Terra und GPT-6.1 Sol kosten.

Wer das einordnen will, braucht eine Relation: Eine Million Token sind grob Dreiviertel einer Million Wörter, also mehrere Romane Text. Ein Dauerbetrieb, in dem eine Firma jeden Tag tausende Rechnungen einlesen lässt, kostet mit dem neuen Modell also die Hälfte von vorher – bei besserer Trefferquote.

## Warum zählt es

**Erstens der Preis pro erledigter Aufgabe, nicht der Preis pro Token.** OpenAI rechnet in der Ankündigung durch, was eine Aufgabe tatsächlich kostet. Auf einem internen Test für Profiaufgaben – „Agents' Last Exam", bei dem ein Modell aus einer Architekturzeichnung ein 3D-Modell bauen oder einen Animationsfilm Bild für Bild protokollieren soll – liegt Terra bei mittlerem Aufwand 15 Prozentpunkte über GPT-5.6 Terra und kostet dabei etwa ein Drittel. Beim höchsten Aufwand rechnet OpenAI vor, dass Terra dreimal sparsamer mit Token umgeht als Claude Opus 5.5 und ein Viertel des Tokenpreises kostet; unterm Strich seien das rund neunmal geringere Kosten pro Aufgabe. Außerdem sei es mehr als dreimal schneller als GPT-6 Astra und GPT-6.1 Sol.

**Zweitens Programmierarbeit auf der Kommandozeile.** {{chart:gpt-terra-terminal-bench}}

Das ist mehr als eine Verdopplung gegenüber dem Vorgänger. Wichtig bleibt die Einschränkung, die OpenAI selbst macht: Für die schwersten Programmieraufgaben sind Sol und Astra weiter die bessere Wahl. Terra schließt die Lücke nach unten, nicht nach oben.

**Drittens die Fehlerquote.** OpenAI hat in diesem Jahr viel Aufwand in die Reduktion von {{Halluzination}}en gesteckt, und bei Terra zeigt sich das in Zahlen: Auf einem internen Satz besonders fehleranfälliger Fragen fiel die Fehlerquote bei geringem Rechenaufwand von 53,6 auf 16,7 Prozent – ein Rückgang um fast 37 Prozentpunkte. Bei maximalem Aufwand sank sie um 18 Punkte auf 4,3 Prozent und liegt damit fast auf dem Niveau der großen Modelle.

**Viertens der Preisvergleich.** {{chart:gpt-terra-preis}}

Für die Einordnung: The Decoder nennt für Anthropics Claude Sonnet 5.5 in derselben Preisklasse 2 Dollar Eingabe und 10 Dollar Ausgabe je Million Token. Terra liegt also beim Output bei der Hälfte.

## Eine zweite Meinung, die es wert ist

OpenAI-Benchmarks sind Herstellerangaben, und die Aufgabensätze wählt die Firma selbst. Deshalb ist wichtig, dass Artificial Analysis – ein kommerzieller Analysedienst, der Modelle mit eigenen, nicht veröffentlichten Tests vermisst – unabhängig nachgemessen hat. Das Ergebnis stützt die Ankündigung in den wichtigsten Punkten:

- Im Intelligence Index gewinnt Terra bei maximalem Aufwand 6 Punkte gegenüber GPT-5.6 Terra und kostet pro Aufgabe 0,40 statt 1,40 Dollar. Bei niedrigeren Aufwandstufen sind die Zugewinne größer: 7 bis 13 Punkte.
- Im neuen Coding Agent Index v2.0 erreicht Terra 48 Punkte. GPT-6.1 Sol kommt auf 54, GPT-6 Luna auf 31.
- Beim Halluzinieren ist der Unterschied am deutlichsten: Auf dem eigenen Wissens-Test AA-Omniscience rät Terra in 38 Prozent der Fälle, in denen es die Antwort nicht weiß – GPT-5.6 Terra riet in 88 Prozent. Gleichzeitig stieg die Trefferquote um 2 Punkte.
- Bei Terminal-Bench 4.0 bestätigt Artificial Analysis den Sprung von rund 20 Punkten; in den meisten anderen Tests sind die Fortschritte kleiner, etwa 5 Punkte in GDP.pdf.

Damit ist die Aussage „halber Preis, mehr Leistung" nicht nur eine Werbebotschaft. Sie ist von zwei Seiten belegt – bleibt aber innerhalb derselben zwei Quellenarten, denn auch Artificial Analysis verkauft seine Auswertungen.

## Was heißt das praktisch

**Für Firmen, die Routinearbeit automatisieren:** Der Preis pro Aufgabe ist die Zahl, mit der man rechnet, und die ist deutlich gefallen. Terra ist damit für Aufgaben interessant, die vorher zu teuer waren – Rechnungen, Formulare, Protokolle, Bildschirmarbeit in Altsystemen ohne Schnittstelle. Das Modell bedient Programme wie ein Mensch: Es sieht den Bildschirm und klickt. Auf dem Desktop-Test OSWorld 2.1 schlägt es laut OpenAI die Bestwerte des Vorgängers schon bei mittlerem Aufwand.

**Für Agenten, die fremde Inhalte lesen:** Terra erreicht laut {{Modellkarte}} 98,8 Prozent Abwehraquote gegen indirekte {{Prompt-Injection}}, bei der schädliche Anweisungen in Webseiten oder Dokumenten versteckt sind – vorher 96,2 Prozent. Bei direkten Angriffen auf die Anweisungshierarchie liegen Astra, Sol und Terra bei 99,99 Prozent. Ganz dicht ist das nicht: Von 1.000 versteckten Angriffen kommen im Schnitt noch rund zwölf durch. Wer einem {{Agent}} Schreibrechte gibt, sollte das wissen.

**Für alle anderen:** In ChatGPT Work und Codex merkt man den Wechsel vor allem daran, dass das Nutzungskontingent weiter reicht. OpenAI schreibt, dieselbe Freigabe decke mehr Aufgaben ab als bei GPT-5.6 Terra und deutlich mehr als bei Sol oder Astra.

**Was in der Ankündigung fehlt:** OpenAI nennt kein {{Kontextfenster}}, also nicht, wie viel Text und Bild das Modell auf einmal verarbeiten kann. Auch Angaben zur Geschwindigkeit in Token pro Sekunde fehlen; „dreimal schneller" bezieht sich auf die Dauer ganzer Aufgaben, nicht auf die Ausgaberate. Und die Einstufung „Critical" im Bereich Cybersicherheit bleibt unkommentiert – die Ankündigung verweist nur darauf, dass die Schutzmaßnahmen von GPT-6 Astra übernommen wurden.

## Quellen

- OpenAI: [Introducing GPT-6.1 Terra](https://openai.com/index/introducing-gpt-6-1-terra), 26.10.2026 – Preise, Benchmarks, Verfügbarkeit (Herstellerangaben)
- OpenAI: [System Card GPT-6.1 Terra](https://deploymentsafety.openai.com/gpt-6-1-terra) – Sicherheitsprüfungen, Prompt-Injection-Werte
- Artificial Analysis: [GPT-6.1 Terra pushes the cost efficiency frontier](https://artificialanalysis.ai/articles/gpt-6-1-terra-pushes-the-cost-efficiency-frontier), 26.10.2026 – unabhängige Nachmessung
- The Decoder: [GPT-6.1 Terra halves OpenAI's API prices](https://the-decoder.com/gpt-6-1-terra-halves-openais-api-prices-and-still-gains-ground-on-its-larger-models/), 26.10.2026 – Vergleichspreise und Einordnung
