---
title: "ThinkingBox: Wenn der Agent fertig sagt und die Datenbank widerspricht"
slug: "thinkingbox-wenn-der-agent-fertig-sagt-und-die-datenbank-widerspricht"
date: 2026-10-04
status: published
tags: [benchmark, agenten, microsoft, llm, news]
summary: "Microsoft und Hugging Face prüfen Agenten nicht an ihrem Text, sondern am Zustand, den sie in der Datenbank hinterlassen: 507 Geschäftsabläufe, je 20 Wiederholungen. Von 121.680 Versuchen scheiterten 79.853 an der Zustandsprüfung – 67 Prozent davon ohne jede Fehlermeldung. Neue Modelle helfen nicht: Claude Opus 5.5 besteht exakt dieselben 241 Aufgaben in allen 20 Läufen wie Opus 5."
source_url: "https://huggingface.co/blog/microsoft/thinkingbox"
source_name: "Microsoft / Hugging Face"
lang: de
---

## TL;DR

- Microsoft und Hugging Face haben mit **ThinkingBox** einen Prüfstand für Agenten veröffentlicht, der nicht bewertet, was ein Agent *sagt*, sondern was er in der Datenbank *hinterlässt*. Veröffentlicht am [3. Oktober 2026](https://huggingface.co/blog/microsoft/thinkingbox), Paper unter [arXiv:2608.19741](https://arxiv.org/abs/2608.19741).
- Grundlage sind **507 Geschäftsabläufe** aus fünf Bereichen (Handel, Kfz-Versicherung, Reisen, Neobank, Beratung). Jede Aufgabe läuft **20-mal** gegen eine frisch zurückgesetzte Datenbank.
- Von **121.680 gültigen Versuchen** über zwölf Modelle scheiterten **79.853** an den Prüfungen des Endzustands. **67,24 Prozent** dieser Fehlversuche liefen trotzdem „sauber" durch: kein Werkzeugfehler, ein datenverändernder Aufruf — und am Ende ein falscher Wert.
- **Claude Opus 5.5** führt die Einzelversuchs-Wertung mit **67,16 Prozent** an. Aber: Ein neueres Modell bringt hier **keine** höhere Zuverlässigkeit — Opus 5.5 besteht exakt dieselben **241 Aufgaben** in allen 20 Versuchen wie Opus 5.
- Die breiteste Abdeckung hat das offene **Kimi-K3** (93,89 Prozent mindestens einmal gelöst), die niedrigste Verlässlichkeit dagegen fast im selben Atemzug: nur **13,41 Prozent** aller Aufgaben bestehen alle 20 Läufe.
- Rund **vier Fünftel aller Fehler** sind Werkzeugfehler, nicht Denkfehler — die Autoren verschieben damit den Schwerpunkt von „klügeres Modell" zu „bessere Fehlerbehandlung".

## Die Kernaussage

Ein Kunde schreibt, ihr Küchengerät für 745 Dollar hänge seit 15 Tagen bei einer Versandausnahme fest. Der Agent arbeitet sorgfältig: neun Werkzeugaufrufe, Bestellung geholt, Sendungsverfolgung geprüft, Kundenprofil gelesen, die Erstattungsrichtlinie zweimal durchsucht, korrekt festgestellt, dass der Kundenstatus keinen Anspruch auf Ausgleich wegen verspäteter Lieferung hat, ein Ticket geöffnet, den Verlauf dokumentiert. Dann schließt er das Ticket als **„gelöst"** und antwortet: „Da Ihr Anliegen geklärt ist, kann ich sonst etwas für Sie tun?"

Zwei Dinge sind falsch. Der Versandfall ist weiter offen — der verlangte Endzustand war **„auf Eis"**. Und die Kundin hat auf ihre Frage keine Antwort bekommen. Genau diese Lücke vermisst ThinkingBox.

Der Einzelversuch, den die Autoren beschreiben, stammt aus einem Datensatz von 507 Aufgaben aus fünf Geschäftsbereichen. Jede Aufgabe definiert einen Startzustand, ein Kundenziel, die verfügbaren Werkzeuge, die Fachrichtlinie und ausführbare Prüfungen über den Endzustand. Am Ende vergleichen feste, nicht-sprachliche Prüfprogramme, was sich tatsächlich geändert hat, mit dem geforderten Ergebnis. Jeder Versuch bekommt eine eigene Datenbanksitzung — zwei Läufe derselben Aufgabe teilen nie eine Zeile. Das ist die Voraussetzung dafür, denselben Ablauf zwanzigmal vergleichen zu können.

Zwei von drei Ergebnissen sind ungewöhnlich für Benchmark-Berichte und darum den Aufwand wert:

**Erstens: Der Zustand zählt, nicht der Text.** 477 der 507 Aufgaben werden allein an der Datenbank bewertet, nur 30 zusätzlich an einer inhaltlichen Ja/Nein-Frage (etwa: „Hat der Agent gesagt, dass dies nicht garantiert ist?"). Ein bestandener Prüftext überzeugt hier niemanden.

**Zweitens: Ein Erfolg ist kein Nachweis.** Die Autoren zählen Aufgaben nicht als gelöst, wenn sie *einmal* geklappt haben, sondern berichten drei Zahlen: **pass@1** (Anteil aller erfolgreichen Versuche), **pass@20** (Aufgaben, die mindestens einmal geklappt haben) und **20/20** (Aufgaben, die in allen 20 Läufen durchgingen). Eine Agentur, die eine Rückerstattung einmal korrekt bearbeitet und danach viermal falsch, ist kein funktionierender Erstattungsagent.

## Was die Zahlen zeigen

Der auffälligste Befund steht in der ersten Auswertung. Über **121.680 gültige Versuche** mit zwölf Modellen scheiterten **79.853** an den Zustandsprüfungen. Von diesen Fehlversuchen endeten **67,24 Prozent** trotzdem ordentlich: kein Fehler am Ende, ein datenveränderndes Werkzeug aufgerufen, keine Fehlermeldung. Die Prüfung fand dann **falsche Feldwerte in 77,61 Prozent**, ungewollte Nebeneffekte in **43,30 Prozent** und fehlende Pflichtänderungen in **25,36 Prozent** dieser Fälle (die Kategorien überschneiden sich).

Anders gesagt: Der Agent meldete Erfolg, das Protokoll sah sauber aus — und in der Datenbank stand das Falsche.

Bei der Einzelversuchs-Wertung (pass@1 über alle 507 Aufgaben):

- **Claude Opus 5.5** — 67,16 Prozent (Bestwert)
- Claude Opus 5 — 66,50
- GPT-5.4 — 65,36
- GPT-5.6 Sol — 61,91
- Claude Sonnet 4.6 — 59,19
- GPT-6 Astra — 58,31
- **Kimi-K3** — 57,37 (bestes offenes Modell, nur ein Punkt hinter GPT-6 Astra)
- Qwen3.8-27B — 51,70
- GPT-5.2 — 46,28
- DeepSeek-V4-Pro — 43,26
- Claude Opus 4.6 — 32,09
- o3-pro — 19,31
- Grok-4.3 — 14,38
- Mistral-Large-3 — 4,66

Zwei Dinge fallen daran auf. Erstens die Streuung nach Bereich: Dasselbe Modell, das im Handel 68,62 Prozent schafft (Claude Opus 4.6), kommt in der Kfz-Versicherung auf **8,30 Prozent**. Im Durchschnitt über alle Modelle liegt der Handel bei 59,52 Prozent, die Kfz-Versicherung bei 33,83. Ein Benchmark-Durchschnitt über alles verdeckt das.

Zweitens, und das ist der eigentliche Befund der Arbeit: **Genauigkeit und Verlässlichkeit fallen auseinander.**

Nur drei Modelle halten den größten Teil ihrer Leistung über 20 Wiederholungen: **GPT-6 Astra** behält 78 Prozent seines Einzelversuchswerts, **Claude Opus 5.5** und **Claude Opus 5** je 71 Prozent. Am anderen Ende behalten **GLM-5.1, Kimi-K2.6 und DeepSeek-V4-Pro** jeweils nur rund **8 Prozent**.

Am deutlichsten wird es bei Kimi-K3: Es löst **93,89 Prozent** der Aufgaben mindestens einmal (476 von 507 — Bestwert im Feld, im Handel mit 82,24 Prozent vor allen kommerziellen Modellen). In allen 20 Läufen besteht es aber nur **13,41 Prozent** (68 von 507). Claude Opus 5 ist das genaue Gegenteil: Es löst weniger Aufgaben überhaupt (79,09 Prozent, 106 Aufgaben widerstehen ihm vollständig), besteht aber **47,53 Prozent** in jedem einzelnen Versuch.

Und ein neueres Modell hilft dabei nicht. Claude Opus 5.5 liegt bei der Durchschnittsleistung über alle Läufe vor Opus 5 (67,16 gegen 66,50 Prozent) und löst mehr Aufgaben mindestens einmal. In allen 20 Versuchen bestehen aber **exakt dieselben 241 Aufgaben**. Ein halber Prozentpunkt mehr Kopfzahl brachte null zusätzliche Verlässlichkeit.

## Was das praktisch heißt

Die Autoren haben noch nachgerechnet, was Verlässlichkeit kostet — und zwar pro **zuverlässig erledigter Aufgabe**, also Kosten für den kompletten 20-Lauf-Durchgang geteilt durch die Zahl der Aufgaben, die alle 20 Läufe bestanden haben:

- **GPT-5.4** — 6,80 Dollar (128 Aufgaben bestehen 20/20)
- GPT-6 Astra — 7,45 Dollar (231)
- Claude Opus 5.5 — 7,80 Dollar (241)
- GPT-5.6 Sol — 9,76 Dollar (82)
- Claude Opus 5 — 13,30 Dollar (241)
- Kimi-K3 — 20,68 Dollar (68)

Die Preise sind aus Token-Verbräuchen zu Listenpreisen hochgerechnet, keine echten Rechnungen — die Autoren sagen das ausdrücklich. Der Kern bleibt: Das billigste Modell pro *richtiger* Antwort ist nicht das billigste pro *verlässlicher* Antwort. GPT-5.6 Sol hat mit 0,127 Dollar die niedrigsten Kosten pro erfolgreichem Versuch, landet bei den verlässlich erledigten Aufgaben aber bei 9,76 Dollar.

Die Fehleranalyse ist dabei der brauchbarste Teil für alle, die selbst Agenten bauen. Die Autoren ordnen jedem gescheiterten Versuch eine feste Signatur zu:

- **Werkzeugnutzung — 79,9 Prozent** der Fehler
- Falsche Zustandsänderungen — 10,3 Prozent
- Unvollständige Kundenlösungen — 7,0 Prozent
- Keine datenverändernde Aktion — 2,9 Prozent

Vier von fünf Fehlern sind also keine Denkfehler, sondern ein Problem mit Werkzeugen: Der Agent kommt weit genug, um den Ablauf zu versuchen, und scheitert dann daran, einen Werkzeugfehler aufzufangen, eine Vorbedingung zu erkennen oder mit einem leeren Suchergebnis umzugehen. Das ist ein Problem der Wiederholungs- und Fehlerbehandlung, bevor es ein Modellproblem ist.

Praktisch raten die Autoren zu drei Dingen: den Endzustand prüfen, bevor etwas festgeschrieben wird — nicht die Zusammenfassung des Modells darüber; Werkzeug- und Systemfehler so klassifizieren, dass Wiederholungen die tatsächlich behebbaren treffen; und die Zahl der Werkzeuge auf das zu kürzen, was der Ablauf wirklich braucht. Ob das die Trefferquote hebt, haben sie **nicht** gemessen — es sei genau die Art Frage, die der Prüfstand nun testbar mache.

## Was noch zu sagen ist

Der Maßstab ist offen zugänglich: Der Code ist MIT-lizenziert, die Benchmark-Daten stehen unter CDLA-Permissive-2.0, die Umgebung läuft über die OpenEnv-Schnittstelle, und der Datensatz liegt auf Hugging Face. Man kann die Aufgaben also selbst gegen ein eigenes Modell laufen lassen.

Zwei Einschränkungen gehören dazu. **Alle Aufgaben sind synthetisch** — nachgebaut nach echten Agentenmustern aus Unternehmen, nicht echte Kundenvorgänge; die Kunden sind erfunden, und die Autoren schreiben das selbst als Hinweis unter den Beitrag. Und die Auswertung stammt vom Hersteller der geprüften Werkzeugumgebung (Microsofts Copilot-Studio-Team zusammen mit Toloka und Hugging Face) — die Zahlen sind also nicht unabhängig nachgeprüft.

Bemerkenswert bleibt der Kern: Dass ein Agent ohne Fehlermeldung durchläuft, sagt nichts darüber, ob er die Aufgabe erledigt hat. Genau dieses Auseinanderfallen messbar zu machen, ist der Beitrag dieser Arbeit.

## Quellen

- Microsoft & Hugging Face, „The Agent Said It Was Done. The Database Disagreed.", 3. Oktober 2026: https://huggingface.co/blog/microsoft/thinkingbox
- Paper: „ThinkingBox" — https://arxiv.org/abs/2608.19741
- Datensatz: ThinkingBox-Bench — https://huggingface.co/datasets/microsoft/ThinkingBox-Bench
- OpenEnv-Umgebung: https://huggingface.co/docs/openenv/environments/thinkingbox
- Code (MIT): https://github.com/microsoft/thinkingbox
