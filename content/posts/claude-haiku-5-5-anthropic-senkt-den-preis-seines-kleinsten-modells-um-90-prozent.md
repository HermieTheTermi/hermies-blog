---
title: "Claude Haiku 5.5: Anthropic senkt den Preis seines kleinsten Modells um 90 Prozent"
slug: "claude-haiku-5-5-anthropic-senkt-den-preis-seines-kleinsten-modells-um-90-prozent"
date: 2026-10-07
status: published
tags: [news, modelle, llm, benchmark, anthropic]
summary: "Anthropic hat am 7. Oktober 2026 Claude Haiku 5.5 veröffentlicht, das kleinste und schnellste Modell der 5.5-Reihe. Für Anfragen bis 100.000 Token kostet es 0,10 Dollar pro Million Eingabe- und 0,50 Dollar pro Million Ausgabe-Token, 90 Prozent weniger als der Vorgänger. In den eigenen Tests steigt der Wert beim Bedienen eines Computers von 15,7 auf 72,4 Prozent und beim Kommandozeilen-Test von 0 auf 39,2 Prozent; das größere Sonnet 5.5 bleibt bei schwerer Programmierung vorn. Alle Leistungswerte sind Herstellerangaben."
source_url: "https://www.anthropic.com/claude-haiku-5-5"
source_name: "Anthropic"
lang: de
---

## TL;DR

- Anthropic hat am 7. Oktober 2026 **Claude Haiku 5.5** veröffentlicht: das kleinste, schnellste und günstigste Modell der 5.5-Reihe ([Ankündigung](https://www.anthropic.com/claude-haiku-5-5), [Modelldaten](https://platform.claude.com/docs/en/models/haiku-5-5/overview)).
- Der Preis fällt deutlich: **0,10 Dollar pro Million Eingabe-Token** und **0,50 Dollar pro Million Ausgabe-Token** bei Anfragen bis 100.000 Token. Haiku 4.5 kostete 1 und 5 Dollar – das sind 90 Prozent weniger.
- Oberhalb von 100.000 Token gelten 0,50 und 2,50 Dollar, immer noch halb so viel wie beim Vorgänger. Im Schnitt rechnet Anthropic mit rund 75 Prozent weniger Kosten – der neue Tokenizer zerlegt denselben Text aber in etwa 30 Prozent mehr {{Token}}.
- In den eigenen Tests legt das Modell überall zu: Computerbedienung (OSWorld 2.1) **72,4 statt 15,7 Prozent**, Kommandozeilen-Aufgaben (Terminal-Bench 4.0) **39,2 statt 0 Prozent**, Wissensarbeit (GDPval-AA) **1.620 statt 735 Punkte**. Gegen das gleich teure GPT-6 Luna gewinnt es in allen genannten Tests, gegen das größere Sonnet 5.5 verliert es beim schweren Programmieren deutlich.
- Erstmals bei Haiku gibt es eine einstellbare Denk-Stufe, dazu ein {{Kontextfenster}} von einer Million Token und bis zu 128.000 Token Ausgabe.
- Nebenbei senkt Anthropic den Cache-Preis von Sonnet 5.5 um die Hälfte und führt monatliche API-Guthaben für Max- und Team-Abos ein. Alle Leistungswerte sind Herstellerangaben aus der eigenen Testreihe; unabhängig geprüft hat sie niemand.

## Was passiert ist

Anthropic hat am 7. Oktober 2026 Claude Haiku 5.5 vorgestellt. Es ist der dritte und letzte Teil der 5.5-Reihe: Opus 5.5 kam am 22. September, Sonnet 5.5 am 28. September, Haiku ist die kleine, schnelle und günstige Variante für viel Routinearbeit ([Ankündigung](https://www.anthropic.com/claude-haiku-5-5)).

Die Reihe ist damit komplett – und der Preis ist die eigentliche Nachricht. Für Anfragen bis 100.000 Token kostet Haiku 5.5 jetzt 0,10 Dollar pro Million Eingabe-Token und 0,50 Dollar pro Million Ausgabe-Token. Beim Vorgänger Haiku 4.5 waren es 1 und 5 Dollar ([Preisliste](https://platform.claude.com/docs/en/about-claude/pricing)). Nach Anthropics eigener Rechnung sind das 90 Prozent weniger; für Anfragen über 100.000 Token halbiert sich der Preis. Diese kurzen Anfragen machen laut Anthropic rund 90 Prozent der Aufrufe des Vorgängermodells aus.

Ein Detail verhindert, dass die Ersparnis eine Milchmädchenrechnung wird. Haiku 5.5 nutzt denselben neuen Tokenizer wie die größeren Modelle, und der zerlegt denselben Text in etwa 30 Prozent mehr Token ([Migrationsleitfaden](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide)). Wer seine Kosten anhand alter Token-Zahlen schätzt, landet zu niedrig. Anthropic rechnet deshalb mit rund 75 Prozent Ersparnis im Schnitt, nicht mit 90.

Auch die Größe des Modells ist neu für diese Klasse: {{Kontextfenster}} von einer Million Token, bis zu 128.000 Token Ausgabe, und zum ersten Mal bei einem Haiku eine einstellbare Denk-Stufe. Bisher gab es diesen Regler nur bei den größeren Modellen – damit lässt sich pro Anfrage entscheiden, ob das Modell mehr rechnen (und kosten) soll oder schneller antwortet. Die Standardstufe ist „medium". Das Modell läuft auf der Claude-API und am ersten Tag auch bei Amazon Bedrock, Google Cloud und Microsoft Foundry.

## Was die Zahlen zeigen

Anthropic vergleicht Haiku 5.5 mit dem Vorgänger, mit OpenAIs GPT-6 Luna und zur Einordnung mit dem eigenen Sonnet 5.5. Der auffälligste Sprung liegt beim Bedienen eines echten Rechners.

{{chart:haiku55-osworld}}

Im Test OSWorld 2.1, der zusammenhängende Klickfolgen und Teilpunkte bewertet, steigt der Wert von 15,7 auf 72,4 Prozent. Das ist mehr als das Vierfache und liegt 23,5 Punkte vor GPT-6 Luna. Bemerkenswert ist, dass Anthropic gleichzeitig die Computer- und Browser-Steuerung in den eigenen Entwicklerbibliotheken freigegeben hat – für die schnelle, günstige Variante gedacht.

{{chart:haiku55-gdpval}}

Bei Aufgaben aus 44 Berufen (GDPval-AA v2.1) kommt Haiku 5.5 auf 1.620 Punkte, der Vorgänger auf 735, GPT-6 Luna auf 1.437. Beim anderen Wissensarbeitstest AA-Briefcase sind es 1.578 statt 614 Punkte. In beiden Fällen bleibt Sonnet 5.5 vorn – beim GDPval-Test mit 1.840 Punkten –, kostet dafür aber das Zwanzigfache pro Token.

Der zweite auffällige Wert ist Terminal-Bench 4.0, ein Test für mehrschrittige Profiaufgaben in der Kommandozeile: 39,2 Prozent, nach 0,0 Prozent beim Vorgänger. Genau hier zeigt sich aber die Grenze: Sonnet 5.5 erreicht im gleichen Test 70,6 Prozent. Für schwere Programmierarbeit bleibt also das größere Modell die richtige Wahl; Haiku 5.5 ist für eng umrissene Aufgaben gedacht.

{{chart:haiku55-preis}}

Bei den übrigen Werten nennt Anthropic 46,4 Prozent beim eigenen Programmiertest FrontierCode 1.1 (GPT-6 Luna: 42,4), 46,4 Prozent beim Diagramm-Test Chartography (GPT-6 Luna: 29,1) und 45,9 beziehungsweise 57,4 Prozent im Wissensquiz Humanity's Last Exam ohne und mit Hilfsmitteln. Das sind allesamt Werte aus der eigenen Testreihe des Herstellers, mit dem Vergleichsmodell in derselben Tabelle.

## Warum das zählt

Kleine Modelle sind die Arbeitstiere der Praxis: Sie sortieren E-Mails, fassen Dokumente zusammen, klassifizieren Anfragen und arbeiten als Unteragenten für die großen Modelle. Wenn dieses Segment im Preis fällt und gleichzeitig deutlich besser wird, sinkt die Schwelle, ab der sich {{Agent}}-Anwendungen überhaupt rechnen. Ein Modell, das einen Rechner bedienen kann, für 0,10 Dollar pro Million Eingabe-Token, verändert die Kalkulation für Anwendungen, die bisher zu teuer waren.

Bemerkenswert ist auch das Tempo: Opus 5.5, Sonnet 5.5 und Haiku 5.5 kamen innerhalb von gut zwei Wochen. Der Preis von 0,10 und 0,50 Dollar ist derselbe, den OpenAI im September für sein kleines Modell GPT-6 Luna aufgerufen hat ([Bericht](https://decrypt.co/380351/anthropic-launches-haiku-5-5-cheapest-fastest-claude-model)). Die günstigste Klasse ist also der Ort, an dem sich die Anbieter derzeit direkt unterbieten.

Und schließlich verschiebt sich das Verhältnis zwischen den Größenklassen. Wer vor einem Jahr zwischen Haiku und Sonnet wählen musste, wählte zwischen „kann das nicht" und „kann das" – heute liegt Haiku beim Bedienen von Computern nur noch rund elf Punkte hinter dem größeren Modell, beim schweren Programmieren aber gut 30 Punkte. Die Entscheidung wird also nicht einfacher, sondern feiner.

## Was heißt das praktisch

Wer Kosten senken will, sollte drei Dinge prüfen. Erstens: Wie lang sind die Anfragen wirklich? Unter 100.000 Token gilt der günstige Tarif, darüber verdoppelt sich der Preis fast. Zweitens: Wie viele Token fallen mit dem neuen Tokenizer an? Ein Test mit echten Daten ist sicherer als eine Rechnung nach alter Gewohnheit. Drittens: Lohnt sich Zwischenspeichern? Das Lesen aus dem Cache kostet bei Haiku 5.5 nur 0,01 Dollar pro Million Token, also ein Zehntel der Eingabe.

Für Agenten mit vielen Schritten kommt ein zweiter Hebel dazu: Die einstellbare Denk-Stufe erlaubt, einfache Schritte billig und schwierige Schritte gründlich zu fahren, ohne das Modell zu wechseln. Dazu kommen monatliche Guthaben für Abos, die Anthropic diese Woche einführt: 100 Dollar im Monat beim kleinen Max-Abo, 200 beim großen und bis zu 500 Dollar für Team-Kunden, die gemeinsam verbraucht werden können ([Ankündigung](https://www.anthropic.com/claude-haiku-5-5)). Dass Anthropic gleichzeitig den Cache-Preis des größeren Sonnet 5.5 halbiert hat – von 0,20 auf 0,10 Dollar, laut Anthropic rund 20 Prozent weniger Kosten bei typischer Agentenarbeit – zeigt, wo die Rechnung im Alltag wirklich auffällt: nicht beim Text hineinschreiben, sondern beim wiederholten Lesen desselben Kontexts.

Bleibt die Einschränkung: Alle Leistungswerte stammen aus Anthropics eigener Messung, die Preise gelten ohne Mengenrabatt und ohne die Aufschläge regionaler Endpunkte bei den Cloud-Anbietern. Wer umstellt, sollte mit einer Handvoll eigener Aufgaben nachmessen.

## Quellen

- [Anthropic: Introducing Claude Haiku 5.5](https://www.anthropic.com/claude-haiku-5-5) (7. Oktober 2026) – Preise, Benchmark-Tabelle, Sicherheitsangaben, Cache-Preis für Sonnet 5.5 und die monatlichen API-Guthaben
- [Claude Haiku 5.5 – Modelldaten](https://platform.claude.com/docs/en/models/haiku-5-5/overview) (Plattform-Dokumentation) – Kontextfenster von 1 Million Token, 128.000 Token Ausgabe, Denk-Stufe, Tokenizer
- [Preisliste von Anthropic](https://platform.claude.com/docs/en/about-claude/pricing) – Vergleichspreise von Haiku 4.5, Sonnet 5.5 und den Cloud-Plattformen
- [Migrationsleitfaden zu Haiku 5.5](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide) – rund 30 Prozent mehr Token für denselben Text
- [Claude Haiku 5.5 – System Card](https://www.anthropic.com/document/claude-haiku-5-5-system-card) – Sicherheitsbewertungen und Einsatzentscheidungen
- [Decrypt: Anthropic Launches Haiku 5.5](https://decrypt.co/380351/anthropic-launches-haiku-5-5-cheapest-fastest-claude-model) – zum Preis von GPT-6 Luna (Sekundärquelle zur Einordnung)
