---
title: "Gemini 4 Carbon: Googles neues Spitzenmodell findet 88 Prozent der Sicherheitslücken"
slug: "gemini-4-carbon-googles-neues-spitzenmodell-findet-88-prozent-der-sicherheitsluecken"
date: 2026-10-28
time: "18:00"
status: published
tags: [news, google, deepmind, modelle, llm, sicherheit, benchmark]
summary: "Google DeepMind hat Gemini 4 Carbon vorgestellt: laut Unternehmen das stärkste eigene Modell, gebaut für tagelange Programmieraufgaben und Cyber-Verteidigung. Google meldet 88,2 Prozent auf SEC-bench Pro, 54,8 auf ExploitGym und 71,0 auf CWE-bench und Platz 1 im Intelligence Index v5.0 mit 59 Punkten – unabhängig geprüft ist davon nichts, Carbon fehlt in der Tabelle von Artificial Analysis noch. Preis wie beim Vorgänger Argon: 2 und 10 Dollar je Million Token, danach 4 und 20. Zugang bekommen zuerst nur ausgewählte Cyber-Verteidiger."
source_url: "https://deepmind.google/blog/gemini-4-carbon-our-next-frontier-model/"
source_name: "Google DeepMind"
lang: de
---

## TL;DR

- Google DeepMind hat am Mittwoch **Gemini 4 Carbon** vorgestellt – laut Unternehmen sein stärkstes Modell, gebaut für zwei Dinge: sehr lange Aufgaben und Cyber-Verteidigung.
- Google nennt drei Zahlen als Bestwerte: **88,2 Prozent** auf SEC-bench Pro (Sicherheitslücken finden), **54,8 Prozent** auf ExploitGym (Lücken ausnutzen) und **71,0 Prozent** auf CWE-bench (Lücken schließen). Das sind Herstellerangaben, unabhängig nachgeprüft sind sie nicht.
- Auf dem Intelligence Index v5.0 von Artificial Analysis steht Carbon laut Google bei **59 Punkten und damit auf Platz 1**. Der Wert ist neu: Anbieter Anthropic führt die veröffentlichte Tabelle derzeit mit 58 Punkten an, Carbon ist dort noch nicht eingetragen.
- Der Preis bleibt im Einführungszeitraum wie beim Vorgänger: **2 Dollar** je Million Eingabe-{{Token}} und **10 Dollar** je Million Ausgabe-Token. Danach gelten 4 und 20 Dollar – ein Enddatum nennt Google diesmal nicht.
- **Die Haken:** Carbon bekommt zunächst nur ausgewählte Cyber-Verteidiger, kein normaler Kunde kann es kaufen. Zum {{Kontextfenster}} sagt die Ankündigung nichts, eine eigene {{Modellkarte}} veröffentlicht Google nicht.

## Was ist passiert

Koray Kavukcuoglu, bei Google für DeepMind und die KI-Architektur zuständig, hat Gemini 4 Carbon am Mittwochabend im Google-Blog vorgestellt. Der Zeitpunkt ist bemerkenswert: Der Vorgänger Gemini 4 Argon ist erst zwei Wochen zu haben – seit dem 13. Oktober für alle zahlenden Kunden. Carbon setzt direkt darauf.

Der Zuschnitt ist eng und erkennbar politisch. Carbon ist kein Allzweckmodell für den Chat, sondern ein Werkzeug für zwei Aufgaben, die Google als strategisch ansieht: Programmierarbeit, die über Stunden oder Tage läuft, und Abwehrarbeit in der IT-Sicherheit. Google schreibt, eigene Teams hätten Carbon „tagelang" laufen lassen, um Fehler in großen Codebasen und in systemnaher Software zu finden und zu beheben.

Die Zahlen, die Google nennt, kommen aus drei Tests der Kategorie {{Benchmark}} und einer Web-Arena:

- **SEC-bench Pro: 88,2 Prozent.** Der Test misst, ob ein Modell echte Schwachstellen in echter Software findet.
- **ExploitGym: 54,8 Prozent.** Hier geht es darum, eine gefundene Lücke tatsächlich auszunutzen – also den Angriff zu bauen, nicht nur das Loch zu sehen.
- **CWE-bench: 71,0 Prozent.** Dieser Test prüft das Gegenteil: ob das Modell eine Lücke korrekt schließt, ohne den Code zu zerstören. Argon kam bei der Vorgängerversion CWE-bench v1 auf 68 Prozent, wie Google in der Argon-Ankündigung schrieb.
- **WebDev Arena: plus 89 Punkte, Platz 4 mit 1769 Elo.** Die Arena lässt Menschen zwei Webseiten vergleichen, die zwei Modelle aus derselben Vorgabe gebaut haben; Elo ist die Punktezahl, mit der solche Duelle ausgewertet werden.

{{chart:gemini-carbon-index}}

Diese Werte stammen ausnahmslos von Google selbst. Für ExploitGym und SEC-bench Pro nennt die Ankündigung keine Vergleichszahlen anderer Anbieter, ein unabhängiger Nachbau fehlt bislang.

## Warum zählt es

**Erstens: Der Sicherheitstest ist der eigentliche Markttest.** Google positioniert Carbon nicht gegen Googles eigenes Vorjahresmodell, sondern gegen Anthropics Claude Opus 5.5 und OpenAIs GPT-6-Familie. Der Punkt, an dem sich das entscheidet, ist der Intelligence Index von Artificial Analysis – ein gewichteter Mittelwert aus neun Prüfungen, den viele Einkaufsabteilungen als erste Orientierung nehmen. Diesen Index hat Artificial Analysis erst am 27. Oktober auf Version 5.0 umgestellt. Auf der neuen Skala führt Claude Opus 5.5 mit 58 Punkten, dahinter GPT-6 Astra mit 57 und GPT-6.1 Sol mit 55; Gemini 4 Argon steht bei 50.

Google meldet für Carbon 59 – einen Punkt vor dem bisherigen Spitzenreiter. Das ist ein knapper Vorsprung und ein geschickt gewählter Moment: Die neue Skala ist zwei Tage alt, die Zahlen sind also frisch und für Leser noch nicht einordbar. In der öffentlich abrufbaren Tabelle von Artificial Analysis ist Carbon derzeit nicht eingetragen; dort steht als Spitze weiterhin Opus 5.5. Ob der Wert 59 nach derselben Prüfroutine entstanden ist, lässt sich von außen nicht kontrollieren.

**Zweitens: Google traut sich etwas bei der Freigabe.** Carbon geht zuerst an eine kleine Gruppe von Verteidigern in Unternehmen und Behörden, danach schrittweise an weitere Partner im eigenen Programm „Fairwind". Google schreibt ausdrücklich, man beteilige sich am freiwilligen Vorab-Testverfahren der US-Regierung. Für Entwickler, Firmen und Privatkunden gibt es keinen Termin – nur ein „so bald wie möglich". Das ist derselbe Weg, den Google bei Argon gegangen ist, und es ist der Grund, warum Carbon für die meisten Leser vorerst Theorie bleibt.

**Drittens: Die Fähigkeit ist doppelt verwendbar.** Ein Modell, das Lücken findet und ausnutzt, kann auch angegriffen werden. Google reagiert darauf mit zwei Schichten: Der Zugang ist begrenzt, und das Modell läuft bei Kunden mit Verteidigungsauftrag ohne die üblichen Cyber-{{Guardrail}}s, damit es überhaupt wirken kann. Das ist ein bewusstes Risiko, das Google mit der Prüfung durch Dritte abfedern will. Wie real die Gefahr ist, zeigte in dieser Woche ein anderer Fall: Ein Sicherheitsstartup drang nach eigener Darstellung mit KI-Agenten in Anthropics interne Systeme ein – über externe Geschäftssoftware und im Rahmen von Anthropics eigenem {{Bug-Bounty}}-Programm. Diese Darstellung stammt aus einem Bericht der Washington Post, den The Decoder zusammengefasst hat; Anthropic bestätigt den Zugriff, bestreitet aber Umfang und Dauer.

## Was heißt das praktisch

**Für Sicherheitsteams:** Carbon ist derzeit kein Produkt, das man kaufen kann, sondern ein Bewerbungsverfahren. Wer im Fairwind-Programm ist, bekommt Zugang ohne Cyber-Guardrails. Für alle anderen bleibt Argon die verfügbare Spitze – mit 1 Million Token gemeinsames Ein- und Ausgabefenster und 68 Prozent auf CWE-bench v1.

**Für Einkäufer:** Der Preis ist der interessanteste Teil. Carbon startet bei 2 und 10 Dollar je Million Token, also auf dem Niveau von Argon und deutlich unter GPT-6 Astra, das bei Artificial Analysis mit 10 und 50 Dollar je Million Token geführt wird. Nach dem Einführungszeitraum gelten 4 und 20 Dollar – dasselbe Niveau wie Claude Opus 5.5. Bei Argon endet der Einführungszeitraum am 30. November 2026; für Carbon nennt die Ankündigung kein Datum. Gecachte Eingabe kostet 95 Prozent weniger, was bei Agenten zählt, die dieselbe Datei hundertmal lesen.

{{chart:gemini-carbon-preis}}

**Für alle, die wissen wollen, ob es stimmt:** Abwarten. Google hat für Carbon weder ein Kontextfenster noch eine eigene Modellkarte veröffentlicht; die Ankündigung verweist für die Sicherheitsprüfung auf den Bericht zu Argon. Wer heute einen Vergleich braucht, hat nur Googles eigene Zahlen und muss ihnen glauben. Ein unabhängiger Test von Carbon durch Artificial Analysis oder eine Universität steht aus.

**Und die Sicherheitsseite in Zahlen:** Google meldet, Carbon habe bei einer internen Prüfung 26 Prozent weniger Übergriffigkeit gezeigt (das Modell hält sich also besser an den Auftrag, statt eigenmächtig mehr zu tun) und 29 Prozent weniger Untererfüllung (es lässt Aufgaben seltener liegen). Beim Test gegen {{Prompt-Injection}}, also dem Versuch, dem Modell über versteckte Anweisungen in Dokumenten oder Webseiten fremde Befehle unterzuschieben, lag Argon bei 0,7 Prozent erfolgreichen Angriffen auf dem Benchmark von Gray Swan. Carbon gibt Google mit 0,0 Prozent an – kein einziger der getesteten Angriffe sei durchgekommen.

Das ist eine starke Zahl und eine, die man mit Vorsicht lesen sollte: Ein Benchmark ist eine feste Sammlung von Angriffen. Wer sie kennt, kann sie trainieren. Die {{Attack Success Rate}} von null sagt deshalb, dass Carbon die bekannten Muster abwehrt – nicht, dass es gegen neue immun ist.

## Quellen

- Google DeepMind: [Gemini 4 Carbon: our next frontier model](https://deepmind.google/blog/gemini-4-carbon-our-next-frontier-model/), 28.10.2026 – Ankündigung, Benchmark-Werte, Preis, Freigabeweg, Sicherheitsangaben
- Google: [Gemini 4 Argon: Built to solve your hardest problems](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/), 13.10.2026 – 1 Million Token, Kontextfenster, Ende des Einführungspreises am 30.11.2026
- Google: [Gemini 4 Argon: our next era of frontier intelligence](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/), 30.09.2026 – CWE-bench v1 mit 68 Prozent
- Artificial Analysis: [Announcing Artificial Analysis Intelligence Index v5](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5), 27.10.2026 – Index-Skala, Spitzenwerte 58/57/55/50, Abstand zu offenen Gewichten
- Artificial Analysis: [Model Comparison](https://artificialanalysis.ai/models/comparisons) – Preise je Million Token für Claude Opus 5.5 und GPT-6 Astra
- The Decoder: [AI agents hacked Anthropic](https://the-decoder.com/ai-agents-hacked-anthropic-maker-of-arguably-the-most-capable-ai-models-for-cyberdefense/), 28.10.2026 – Bericht über den Zugriff auf Anthropics Systeme (Sekundärquelle, beruht auf Washington Post)
