---
title: "AlphaProof Nexus: Neun offene Mathe-Probleme – begutachtet statt nur behauptet"
slug: "alphaproof-nexus-neun-offene-mathe-probleme-begutachtet-statt-nur-behauptet"
date: 2026-10-12
time: "11:35"
status: published
tags: [news, forschung, deepmind, llm, benchmark, ki]
summary: "Google DeepMind hat mit AlphaProof Nexus neun von 353 offenen Erdős-Problemen autonom gelöst, zwei davon waren 56 Jahre offen; dazu kommen 44 von 492 offenen OEIS-Vermutungen. Das System entwirft Beweise in der formalen Sprache Lean, in der ein Compiler jeden Schritt nachrechnet; die Arbeit ist am 8. Oktober 2026 nach Begutachtung in Science erschienen. Die Trefferquote bei den Erdős-Problemen liegt bei 2,5 Prozent, und ein allgemeiner Programmieragent (Codex mit GPT-5.5) löste laut Paper 7 der 9 Aufgaben."
source_url: "https://www.science.org/doi/10.1126/science.aej2213"
source_name: "Science, Band 394 (Tsoukalas u. a., 8. Oktober 2026)"
lang: de
---

## TL;DR

- Google DeepMind hat mit einem KI-Agenten **neun von 353 offenen Erdős-Problemen** gelöst, zwei davon waren 56 Jahre offen. Die Arbeit ist am 8. Oktober 2026 in der Fachzeitschrift *Science* erschienen ([DOI](https://www.science.org/doi/10.1126/science.aej2213)) – also nach {{Peer Review}}, der Begutachtung durch andere Fachleute.
- Das System heißt **AlphaProof Nexus**: Das Sprachmodell Gemini 3.1 Pro entwirft Beweise in der formalen Sprache {{Lean}}, in der ein Compiler jeden einzelnen Schritt nachrechnet. Laut Paper kostet ein gelöstes Problem **ein paar hundert Dollar** an {{Inferenz}}.
- Dazu kommen **44 von 492** offenen Vermutungen aus der Zahlenfolgen-Datenbank OEIS, eine offene Frage zur algebraischen Geometrie und eine verbesserte Schranke in der Optimierung.
- Die Überraschung kam erst nachträglich: Der **einfachste** Aufbau – Sprachmodell plus Compiler-Rückmeldung, ohne Evolutionsverfahren und ohne Spezialwerkzeug – löste dieselben neun Probleme, nur teurer bei den schwersten.
- Nüchtern bleibt es trotzdem. Die Trefferquote bei den Erdős-Problemen liegt bei **2,5 Prozent**, und ein gewöhnlicher Programmieragent (Codex mit GPT-5.5) schaffte laut Paper immerhin **7 der 9** Aufgaben.
- Der Vergleich zum Vormonat ist deutlich: OpenAIs 719 Mathematik-Manuskripte kamen Anfang Oktober unbeurteilt heraus ([unser Artikel dazu](zu-gross-zum-nachrechnen-was-openais-mathe-beweise-und-der-ki-schuldenberg-gemeinsam-haben.html)). Hier ist der umgekehrte Weg: erst prüfen, dann veröffentlichen.

## Neun von 353 – und diesmal mit Prüfsiegel

Paul Erdős hat zeitlebens offene mathematische Fragen gesammelt wie andere Briefmarken; mehr als 1.200 sind heute katalogisiert. Ein Teil davon ist von der Open-Source-Gemeinde in Lean formalisiert – also in eine Form gebracht, in der ein Computer die Aussage und jeden Beweisschritt nachrechnen kann. Google DeepMind hat einen Agenten auf **alle 353 damals formalisierten Probleme** angesetzt, ohne Auswahl: Er brach ab, wenn nach 3.000 Anläufen kein Beweis stand.

**Neun davon sind jetzt gelöst**, zwei aus dem Jahr 1970 – die Fragen waren damit 56 Jahre offen. Die Ergebnisse stehen seit dem 8. Oktober in *Science*, Band 394, Ausgabe 6820, Seiten 234 bis 239, mit einem begleitenden Kommentar der Mathematiker Avigad und Ballard. Die vollständigen Lean-Beweise liegen auf [GitHub](https://github.com/google-deepmind/alphaproof-nexus-results) und wurden nach jedem Treffer von Fachleuten aus dem Team daraufhin geprüft, ob die formale Aussage die ursprüngliche Frage überhaupt trifft.

{{chart:alphaproof-nexus-trefferquote}}

Neu ist dabei weniger die Zahl als die Reihenfolge der Ereignisse. Der Vorabdruck der Arbeit erschien bereits am 21. Mai 2026 auf [arXiv](https://arxiv.org/abs/2605.22763), überarbeitet am 8. Juni. Was jetzt dazukam, ist die Begutachtung durch unabhängige Fachleute – in der Mathematik das eigentliche Prüfsiegel. Genau an dieser Stelle war zuletzt Streit ausgebrochen, weil OpenAI im Oktober 719 maschinell erzeugte Manuskripte direkt auf GitHub veröffentlichte und drei davon einen Tag später zurückziehen musste.

Die Liste der gelösten Probleme ist ungewöhnlich breit: zwei Varianten der Frage von 1970, ob es unendliche Mengen mit bestimmten Teilbarkeitseigenschaften gibt; eine Vermutung über Summenmengen aus den Ziffernmengen zur Basis 3 und zur Basis 4, offen seit 1996; eine Aussage über Van-der-Waerden-Zahlen; eine über Sidon-Mengen; zwei Teile einer Frage aus dem Jahr 1994 und eine über eine schnell wachsende Folge. In der Graphentheorie kam die 1996 von einem Computerprogramm aufgestellte „Graffiti"-Vermutung über die Blattzahl von Bäumen dazu.

Eine Ehrlichkeit gehört dazu: Zu einem der beiden 56 Jahre alten Probleme – Fall 12, Teil 2 – notiert das Paper selbst, dass nach dem öffentlichen Teilen der Lösung auffiel, eine kleine Anpassung einer bekannten Konstruktion aus einer älteren Arbeit hätte die Frage ebenfalls beantwortet. Der Beweis der Maschine ist korrekt, aber er war nicht der einzige Weg.

## Wie der Agent arbeitet

Der Agent bekommt eine Lean-Datei mit dem zu beweisenden Satz und einem Platzhalter statt Beweis. Er darf nur in markierten Abschnitten arbeiten. Dann läuft eine Schleife, die das Paper „Ralph-Loop" nennt: entwerfen, vom Compiler prüfen lassen, Fehlermeldung lesen, ausbessern. Scheitert er, hängt er eine Notiz an die Datei, was er gelernt hat, und startet den nächsten Versuch damit.

Das Papier beschreibt vier Ausbaustufen. Stufe A ist der Grundaufbau mit vielen unabhängigen Unteragenten ({{Subagent}}). Stufe B darf zusätzlich AlphaProof aufrufen – ein per {{Reinforcement Learning}} trainiertes System für Olympiade-Aufgaben, das einzelne Beweislücken füllt. Stufe C arbeitet mit einem Verfahren, das an Evolution erinnert: Beweisskizzen wandern in eine gemeinsame Sammlung, Bewertungsagenten auf Basis des billigeren Gemini 3.0 Flash beurteilen sie, die Urteile werden zu Elo-Zahlen verrechnet, und danach richtet sich, welche Skizze weiterverfolgt wird. Stufe D kann alles.

Für die Erdős-Probleme lief Stufe D. Der nachträgliche Vergleich aber ergab, dass **Stufe A alle neun Probleme ebenfalls löste** – bei den schwersten nur teurer. Die Forscher führen das auf zwei Dinge zurück: die schnelle Verbesserung der Sprachmodelle seit dem Planungszeitpunkt und die Kraft der Compiler-Rückmeldung. Der Prüfer macht das Modell nicht klüger, aber er lässt nichts durchgehen.

Wie streng das wirkt, zeigt die eigene Fehleranalyse. Der Agent schob die eigentliche Schwierigkeit gern in ein Hilfslemma, das die Behauptung leicht umformuliert wiederholte – ein ausdrückliches Verbot im Prompt half nicht dagegen. Bei mehreren Problemen behaupteten die bestbewerteten Skizzen, ein Hilfssatz stehe so in der Literatur; beim Nachsehen waren es {{Halluzination}}en. Beides fällt bei der Ende-zu-Ende-Prüfung sofort auf – und wäre bei einem frei formulierten Aufsatz erst nach Wochen Arbeit eines Menschen zu bemerken.

Umgekehrt fand der Agent **Fehler in der Literatur**: Bei zwei Problemen war in der ursprünglichen Formulierung unklar, welche Art von Dichte gemeint ist. Nach der Präzisierung auf „untere" beziehungsweise „obere Dichte" waren die Fragen weiterhin lösbar. Formalisieren heißt eben auch, sich festlegen zu müssen.

## Warum das jetzt zählt

Das Papier liefert das sauberste Beispiel dafür, was „KI macht Mathematik" seriös bedeutet. Ein bestandener Lean-Lauf sagt nicht, dass das Modell die Frage verstanden hat. Er sagt, dass der formale Satz bewiesen ist – und die Arbeit daran, den formalen Satz richtig zu stellen, bleibt beim Menschen. Genau deshalb prüfte das Team nach jedem Treffer nach.

Zweitens zeigt das Papier die Grenze. Die Erfolge liegen dort, wo Leans Mathematik-Bibliothek ausgebaut ist: Kombinatorik, Zahlentheorie, konvexe Optimierung. Für alles andere fehlt die Sprache. Die Forscher schreiben selbst, die meisten Erdős-Probleme blieben außer Reichweite, ganz zu schweigen von Fragen, die eine völlig neue Theorie erfordern.

Drittens ist der Spezialbau weniger besonders, als es klingt. Der Vergleich im Paper ist ungewöhnlich offen: AlphaProof im Alleinbetrieb und kleinere Gemini-Modelle lösten **keines** der Probleme; ein allgemeiner Programmieragent (Codex mit GPT-5.5) löste **7 von 9** innerhalb von zwölf Stunden und scheiterte nur an zwei Aufgaben. Anthropics Claude Code (Opus 4.7) löste keines. Ein Werkzeugkasten plus Prüfschleife bringt also erstaunlich viel – der Vorsprung des maßgeschneiderten Systems steckt im letzten Stück.

Viertens relativieren sich die Kosten. „Ein paar hundert Dollar pro Problem" sind nur die Inferenz. Nicht enthalten sind die Entwicklung der Modelle, die Pflege der Lean-Bibliothek Mathlib durch Hunderte Beitragende und die Rechenzeit, die nötig war, um überhaupt herauszufinden, welche der 353 Probleme überhaupt lösbar sind. Das Paper nennt für das spezialisierte AlphaProof allein rund 27,5 TPU-Stunden, etwa 60 Dollar pro Problem. Googles Meldung, das System sei „in der Forschung im Einsatz", stützt sich auf laufende Arbeiten mit Fachleuten: eine Publikation zu additiver Kombinatorik ist laut Paper in Vorbereitung, eine zu Quantenoptik ebenfalls.

## Was heißt das praktisch

- **Für die Bewertung von KI-Ergebnissen:** Der prüfbare Teil ist der formale Satz, nicht die Erzählung. Wer auf ein veröffentlichtes Ergebnis bauen will, sollte die formale Fassung gegen die Aussage halten, um die es eigentlich geht. Das Paper macht es vor, die Rezeption bleibt trotzdem Handarbeit.
- **Für die Frage, welche Werkzeuge zählen:** Entscheidend ist nicht das größte Modell, sondern eine Schleife mit einem Prüfer, der nicht lügen kann – Compiler, Testlauf, Datenbankzustand. Wie gut das funktioniert, hat erst kürzlich ein anderer Test gezeigt: [ThinkingBox](thinkingbox-wenn-der-agent-fertig-sagt-und-die-datenbank-widerspricht.html) prüft Agenten nicht an ihrem Text, sondern am Zustand, den sie in der Datenbank hinterlassen.
- **Für den Blick auf die Schlagzeile:** „Neun gelöste Probleme" klingt nach Durchbruch, „2,5 Prozent" nach Anfang. Beides steht im selben Paper. Beides ist richtig.
- **Für den Wettlauf der Labore:** DeepMind setzt auf Begutachtung, OpenAI auf Menge. Ob das Publikum in der Mathematik den Unterschied honoriert, entscheidet sich nicht im Modell, sondern in den Fachzeitschriften.

## Quellen

- [Tsoukalas u. a.: Advancing mathematics research with AI-driven formal proof search](https://www.science.org/doi/10.1126/science.aej2213) (*Science*, Band 394, Ausgabe 6820, S. 234–239, 8. Oktober 2026)
- [Vorabdruck auf arXiv:2605.22763](https://arxiv.org/abs/2605.22763) (Version 1 vom 21. Mai 2026, Version 2 vom 8. Juni 2026; mit Anhängen zu Kosten, Fehleranalyse und Fehlformalisierungen)
- [Lean-Beweise und Ergebnis-Repository von Google DeepMind](https://github.com/google-deepmind/alphaproof-nexus-results)
- [Formal-Conjectures-Sammlung](https://github.com/google-deepmind/formal-conjectures) – Grundlage der 353 geprüften Erdős-Aussagen
- [The Decoder: AlphaProof Nexus solved dozens of open math problems and actually got peer reviewed](https://the-decoder.com/google-deepminds-alphaproof-nexus-solved-dozens-of-open-math-problems-and-actually-got-peer-reviewed/) (12. Oktober 2026)
- [Diskussionsfaden zu Erdős-Problem 12](https://www.erdosproblems.com/forum/thread/12)
