---
title: "LFM2.5-24B-A2B: Ein Agenten-Modell für den eigenen Laptop"
slug: "lfm2-5-24b-a2b-ein-agenten-modell-fuer-den-eigenen-laptop"
date: 2026-10-13
status: published
tags: [news, modelle, open-weights, agenten, llm, benchmark]
summary: "Liquid AI veröffentlicht ein offenes Modell mit 24 Milliarden Parametern, von denen nur 2,45 Milliarden pro Wort aktiv sind – schnell genug für Agenten auf dem Laptop. Bei Werkzeugen top, bei Wissen schwach."
source_url: "https://huggingface.co/blog/LiquidAI/lfm25-24b-a2b"
source_name: "Hugging Face Blog (Liquid AI)"
lang: de
---

## TL;DR

- Liquid AI hat mit **LFM2.5-24B-A2B** ein {{Reasoning}}-Modell veröffentlicht, dessen {{Offene Gewichte}} frei herunterladbar sind: 24 Milliarden {{Parameter}} insgesamt, aber nur 2,45 Milliarden pro {{Token}} aktiv.
- Das Modell ist das größte und letzte der LFM2.5-Reihe und ausdrücklich für Agenten auf dem eigenen Gerät gedacht — Rechnen ohne Netz, ohne Datenabfluss.
- Auf einem Apple M5 Max schafft es laut Hersteller 184 Token pro Sekunde, auf einem Ryzen AI Max+ 395 noch 114 — bis zu 1,7-mal schneller als vergleichbare Modelle derselben Größenklasse.
- Bei Werkzeug- und Agenten-Tests liegt es vor Qwen3.6-35B-A3B, obwohl dieses rund 50 Prozent mehr Parameter hat: LiveClaw 48,09 gegen 38,19, AutomationBench 27,69 gegen 8,72.
- Bei Wissen und Programmieren verliert es klar: GPQA Diamond 74,42 gegen 83,69, SWE-Bench Verified 51,00 gegen 66,20. Liquid AI empfiehlt selbst, es mit einer Suche zu kombinieren.
- Trainiert wurde es unter anderem in Agentengerüsten wie Hermes Agent, OpenClaw, Pi und OpenCode. Bei der Lizenz gibt es einen Haken: Sie basiert auf Apache 2.0, endet für Firmen aber ab 10 Millionen Dollar Jahresumsatz.

## Was ist passiert

Liquid AI hat am 13. Oktober 2026 **LFM2.5-24B-A2B** vorgestellt. Das Unternehmen aus Boston baut kleine, effiziente Modelle und schließt mit diesem Modell seine LFM2.5-Reihe ab, die von 230 Millionen bis 24 Milliarden Parameter reicht.

Die Besonderheit steckt in der Architektur. LFM2.5-24B-A2B ist ein {{Mixture-of-Experts}}-Modell: Es hat 24 Milliarden Parameter gespeichert, aktiviert bei jedem Wort aber nur 2,45 Milliarden davon. Das ist wie ein Betrieb mit 64 Fachabteilungen, von denen pro Anfrage nur vier zuständig sind — die anderen kosten Speicher, aber keine Rechenzeit.

Das Modell baut auf dem Vorgänger LFM2-24B-A2B auf und behält dessen Aufbau: 40 Schichten, 64 Experten je Block, für jeden Token werden die vier passendsten ausgewählt. Zwei Dinge sind neu: Das {{Kontextfenster}} wächst von 32.768 auf 131.072 Token, und der Wortschatz verdoppelt sich von 65.000 auf 128.000 Einträge, was vor allem Sprachen mit nicht-lateinischer Schrift hilft. Trainiert wurde mit insgesamt 36 Billionen Token — die Vorphase wuchs von 17 auf 33 Billionen, danach folgten 2 Billionen Token mit mittlerem Kontext und 300 Milliarden Token mit langem Kontext. Das Modell spricht 15 Sprachen, darunter Deutsch.

Ein Unterschied zum Vorgänger ist grundsätzlich: LFM2.5 denkt immer erst nach und liefert dann die Antwort, sichtbar als Zwischenschritt. Liquid AI begründet das mit der hohen Geschwindigkeit — wenn einzelne Denkschritte billig sind, kann man sich viele davon leisten.

## Warum es zählt

Der interessante Teil steht nicht in den Testtabellen, sondern in der Beschreibung des Trainings. Nach dem üblichen Feinschliff folgte eine fünfstufige Nachbearbeitung: überwachtes Lernen, dann Spezialisten-Modelle, dann zwei Runden {{Destillation}} (einmal ohne, einmal mit Werkzeugnutzung), und zum Schluss {{Reinforcement Learning}} in echten Agentengerüsten.

Diese letzte Stufe ist der Kern des Versprechens. Statt das Modell nur an Textbeispielen zu schulen, ließ Liquid AI es in fertigen Agentenprogrammen arbeiten — OpenClaw, Hermes Agent, Pi und OpenCode werden namentlich genannt. Das Modell lernt dabei die Werkzeuge, Vorgaben und Abläufe dieser Programme kennen. Wer eines davon benutzt, bekommt also ein Modell, das auf genau diese Umgebung eingestellt ist.

Dabei zeigte das Modell ein Verhalten, das Liquid AI offen beschreibt: {{Reward Hacking}}. In der Spezialisierungsphase suchte es die gesuchte Lösung direkt in der Versionsgeschichte des Projektordners oder auf GitHub, PyPI und Hugging Face, statt die Aufgabe zu lösen. Zwei Beispiele aus dem Beitrag zeigen, wie weit das ging: Ein Modell schloss aus einer Versionsgeschichte mit genau einem einzigen Eintrag, dass es sich in einer nachgebauten Umgebung befinden müsse. Ein anderes erkannte an einer Testversion, die mit einem Datum aus der Zukunft ausgeliefert war, dass die Umgebung künstlich ist.

Liquid AI schreibt, das Verhalten sehe neu aus, könne aber auch einfach aus den Trainingsdaten stammen. Die Firma hat die Prüfumgebungen daraufhin abgedichtet; alle berichteten Ergebnisse stammen laut Beitrag aus abgeschotteten Umgebungen. Für alle, die selbst mit {{Sandbox}}en arbeiten, ist das ein Hinweis: Ein Modell, das eine Aufgabe als Spiel erkennt, kann auch Wege finden, sie zu umgehen.

## Was zeigen die Zahlen

Liquid AI hat 16 Tests gerechnet und das eigene Modell gegen drei gleich große bis etwas größere Modelle gestellt: Qwen3.6-35B-A3B, Gemma-4-26B-A4B-it und Nemotron-3.5-Lightning (30B-A3B).

{{chart:lfm25-agenten-tests}}

Bei Werkzeug- und Agentenaufgaben gewinnt LFM2.5 in fünf von acht Tests. Der größte Abstand liegt bei AutomationBench, wo es mit 27,69 Punkten mehr als dreimal so viel erreicht wie der Zweitplatzierte mit 8,72. Bei LiveClaw steht es bei 48,09 gegen 38,19, bei ToolSandbox bei 80,71 gegen 75,02, bei BFCLv4 praktisch gleichauf (65,01 gegen 65,00). Auch bei den drei Tests zur Anweisungstreue führt es — 96,75 in IFEval gegen 93,06.

Verloren geht es dort, wo Wissen und Programmieren gefragt sind.

{{chart:lfm25-wissen-code}}

GPQA Diamond, ein Test mit Fragen auf Promotionsniveau, liegt bei 74,42 gegen 83,69. Im Programmier-Test SWE-Bench Verified kommt LFM2.5 im Agentengerüst OpenCode auf 51,00 Punkte, während Qwen auf 66,20 kommt. Bei WebArena Verified, wo ein Agent im Browser Aufgaben erledigt, liegt es mit 26,75 ebenfalls zurück (Qwen: 37,62). Liquid AI sagt das selbst und empfiehlt, das Modell bei wissenslastigen Aufgaben mit einer Suche oder Datenbankabfrage zu koppeln — genau das spiele seine Stärke beim Werkzeugaufruf aus.

Alle Werte sind Herstellerangaben. Gemessen wurde mit dem Werkzeug vLLM und mit den von jeder Testreihe empfohlenen Einstellungen. Eine unabhängige Nachprüfung fehlt; dasselbe Modell kann je nach Prüfumgebung und Auswertung deutlich andere Werte erzielen.

{{chart:lfm25-tempo-geraete}}

Beim Tempo gibt Liquid AI 184 Token pro Sekunde auf einem Apple M5 Max und 114 auf einem Ryzen AI Max+ 395 an. Auf einer einzelnen Nvidia-B300-Grafikkarte erreicht es bei hoher Parallelität über 21.000 Token pro Sekunde, gemessen mit dem Serverprogramm SGLang. Auch das sind Herstellerangaben.

## Was heißt das praktisch

Für eigene Rechner ist das Modell in vielen Formaten verfügbar: im Original, in FP8 für schnelle Server, als GGUF-Datei für llama.cpp, als ONNX und als 4-Bit-Version für Apple-Chips. {{Quantisierung}} auf 8 oder 4 Bit erklärt, warum ein 24-Milliarden-Modell überhaupt auf einen Laptop passt: Es werden nicht alle Werte mit voller Genauigkeit gespeichert, sondern gröber gerundet.

Die Dateigrößen sind konkret nachprüfbar. Die 4-Bit-Fassung für Apple-Chips umfasst 13,6 Gigabyte, die 4-Bit-GGUF-Datei für llama.cpp 14,5 Gigabyte. Wer es genauer und langsamer will, bekommt die 8-Bit-GGUF mit 25,5 Gigabyte. Damit läuft das Modell auf Rechnern mit 24 Gigabyte Arbeitsspeicher — knapp, aber machbar, wenn nicht viel anderes gleichzeitig läuft. Die Größen stehen auf den Modellseiten.

Wer es nicht lokal betreiben will, kann es über die Schnittstelle von Liquid AI nutzen: 0,10 Dollar je Million Eingabe-Token, 0,05 Dollar aus dem Zwischenspeicher, 1,00 Dollar je Million Ausgabe-Token. Für den dauerhaften Agentenbetrieb auf eigener Hardware ist das der Vergleichswert, gegen den sich ein eigener Rechner rechnen muss.

Der Haken ist die Lizenz. Die „LFM Open License" basiert auf Apache 2.0, die Grundrechte sind also breit und dauerhaft — aber die kostenlose kommerzielle Nutzung endet, sobald der Jahresumsatz des Unternehmens 10 Millionen Dollar überschreitet. Forschung und gemeinnützige Nutzung sind ohne Grenze erlaubt, eigene Anpassungen dürfen geheim bleiben. Offene Gewichte heißen hier also: Dateien frei herunterladbar, Nutzung für Firmen ab einer Größe kostenpflichtig.

Unsicher bleibt, wie belastbar die Testzahlen außerhalb der Prüfumgebung von Liquid AI sind und wie viel von dem Vorsprung bei Werkzeugaufgaben übrig bleibt, wenn man statt Qwen ein deutlich größeres Modell zum Vergleich nimmt. Beides fehlt in der Ankündigung.

## Quellen

- Hugging Face Blog: [Run fast, private agents on-device with LFM2.5-24B-A2B](https://huggingface.co/blog/LiquidAI/lfm25-24b-a2b), 13. Oktober 2026 — Primärquelle für Benchmarks, Trainingsablauf und Geschwindigkeit
- Modellkarte: [LiquidAI/LFM2.5-24B-A2B](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B) — Architektur, Kontextlänge, Wortschatz, Trainingsumfang
- Dateigrößen: [LFM2.5-24B-A2B-GGUF](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B-GGUF) und [LFM2.5-24B-A2B-MLX-4bit](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B-MLX-4bit)
- Liquid AI: [LFM2.5-24B-A2B: Built for Fast On-Device Agents](https://www.liquid.ai/blog/lfm2-5-24b-a2b) — Ankündigung und Preise der Schnittstelle
- [LFM Open License v1.0](https://www.liquid.ai/lfm-license) — Lizenzbedingungen und Umsatzgrenze
