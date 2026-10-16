---
title: "Beam: Reflection veröffentlicht ein offenes 501-Milliarden-Modell"
slug: "beam-reflection-veroeffentlicht-ein-offenes-501-milliarden-modell"
date: 2026-10-16
status: published
tags: [news, modelle, open-weights, llm, agenten, benchmark]
summary: "Reflection, ein US-Labor aus zwei ehemaligen DeepMind-Forschern, veröffentlicht mit Beam sein erstes Modell unter Apache 2.0: 501 Milliarden Parameter, davon 23 Milliarden pro Wort aktiv, eine Million Token Kontext. Zum Selbstbetreiben braucht es vier B200-Grafikchips. In der Vergleichstabelle von Reflection selbst liegt Beam hinter chinesischen Modellen; alle Werte sind Herstellerangaben."
source_url: "https://reflection.ai/blog/beam-is-available"
source_name: "Reflection"
lang: de
---

## TL;DR

- Das US-Labor **Reflection** hat am 16. Oktober sein erstes eigenes Modell veröffentlicht: **Beam** steht als Download bereit — ein Modell mit {{Offene Gewichte}}n unter der Lizenz Apache 2.0, also kommerziell frei nutzbar.
- Beam ist ein {{Mixture-of-Experts}}-Modell mit 501 Milliarden {{Parameter}}n, von denen pro Wort nur 23 Milliarden rechnen. Es verarbeitet bis zu eine Million {{Token}} auf einmal.
- Auf eigenen Rechnern betreiben kann es trotzdem fast niemand: Die Gewichte sind in voller Genauigkeit rund ein Terabyte groß, in der 4-Bit-Fassung noch etwa 280 Gigabyte. Reflection empfiehlt vier B200-Grafikchips.
- Der Vorteil liegt laut Reflection nicht in roher Leistung, sondern im Rechenaufwand. Auf acht B300-Chips liefert Beam 708 Token pro Sekunde für eine einzelne Anfrage; der Zwischenspeicher für eine Million Token Kontext ist rund sechsmal kleiner als bei üblicher Bauweise.
- In der Vergleichstabelle von Reflection selbst liegt Beam hinter chinesischen Modellen: Terminal Bench 2.1 — Beam 80,1 Prozent, DeepSeek V4.1 Flash 90,6 Prozent.
- Alle Leistungszahlen stammen von Reflection. Eine unabhängige Nachprüfung fehlt noch.

## Was ist passiert

Reflection ist ein US-amerikanisches KI-Labor, das im März 2024 von zwei ehemaligen Google-DeepMind-Forschern gegründet wurde: Misha Laskin und Ioannis Antonoglou, der an AlphaGo mitgebaut hat ([TechCrunch](https://techcrunch.com/2025/10/09/reflection-raises-2b-to-be-americas-open-frontier-ai-lab-challenging-deepseek/)). Das Unternehmen positioniert sich ausdrücklich als offenes Gegenstück zu den geschlossenen Labors in den USA und zu den chinesischen Anbietern.

Am 16. Oktober hat Reflection sein erstes Modell freigegeben. **Beam** steht jetzt auf [Hugging Face](https://huggingface.co/reflection) zum Herunterladen, unter Apache 2.0. Das ist die Lizenz, die kommerzielle Nutzung, Veränderung und Weitergabe ohne Auflagen erlaubt — bei KI-Modellen ist das die offenste gängige Variante.

Zum Aufbau nennt die [Modellkarte](https://reflection.ai/beam-model-card) konkrete Werte: 501,3 Milliarden Parameter insgesamt, 23,4 Milliarden davon aktiv, 52 Schichten, davon drei herkömmlich und 49 als Experten-Schichten mit je 256 Experten. Pro Wort rechnen nur acht dieser Experten. Das {{Kontextfenster}} reicht über eine Million Token, das Wissen endet am 30. Juni 2026, und das Modell versteht ausschließlich Text.

Interessant ist, wie Beam mit langen Eingaben umgeht. Von den 52 Schichten schauen 43 nur auf die letzten 512 Token und merken sich den Rest nicht; nur die anderen neun betrachten den gesamten Text. Dadurch wächst der Zwischenspeicher, den das Modell für eine Anfrage braucht, deutlich langsamer.

{{chart:beam-kontext-cache}}

Bei einer Million Token Kontext sind das laut Hugging Face 36,08 GiB statt 208 GiB. In 8-Bit-Genauigkeit halbiert sich der Wert noch einmal. Das ist der Grund, warum ein Kontextfenster dieser Größe überhaupt bezahlbar wird.

## Warum es zählt

Offene Modelle an der Spitze kamen bisher fast immer aus China: Kimi, Qwen, GLM, DeepSeek. Reflection behauptet in der [Ankündigung vom 5. Oktober](https://reflection.ai/blog/introducing-beam), Beam schiebe die „westliche Grenze offener Gewichte" nach vorn. Das ist ein Labor, das für sich in Anspruch nimmt, mit dem eigenen Modell die Lücke zu den chinesischen Anbietern zu schließen — und die eigene Vergleichstabelle zeigt, dass es nur teilweise gelingt.

Der Trainingsaufwand gibt eine Vorstellung davon, was in dieser Größenklasse inzwischen üblich ist. Reflection nennt 23,8 Billionen Token für das Vortraining und über 100 Millionen Durchläufe im {{Reinforcement Learning}} auf 10.500 NVIDIA-GB300-Chips in vier Wochen. Für die Lernumgebungen liefen rund 1,3 Milliarden {{Sandbox}}en; die Rechnerflotte erreichte nach Angaben des Labors 883.006 virtuelle Prozessorkerne über 23 Cluster bei Google Cloud und Amazon Web Services.

Zweitens der praktische Teil: Releasing bedeutet bei dieser Größe etwas anderes als bei einem 8-Milliarden-Modell. Die vollständige Fassung in 16-Bit-Genauigkeit ist rund ein Terabyte groß. Die 4-Bit-Variante schrumpft sie auf etwa 280 Gigabyte, passt aber nur auf Blackwell-Chips von NVIDIA. Ältere Beschleuniger brauchen die 8-Bit-Variante. Reflection empfiehlt vier B200, alternativ zwei B300 oder acht RTX Pro 6000.

Drittens die Rechenzeit im Betrieb. Auf acht B300-Chips erreicht Beam 708 Token pro Sekunde bei einer einzelnen Anfrage, mit einer Trefferquote von 3,7 Token pro Prüfschritt. Diese Zahlen stammen aus dem [vLLM-Blogpost zum Starttag](https://vllm-project.github.io/2026/10/16/reflection-beam.html) und aus der [Hugging-Face-Vorstellung](https://huggingface.co/blog/reflection-beam). Bemerkenswert daran ist, wie die Verbesserung entstand: Das vLLM-Team hat eine erste, kaum optimierte Fassung von Programmier-{{Agent}}en beschleunigen lassen. Die haben das Modell vermessen, eigene Rechenkerne geschrieben und jede Änderung nachgemessen. Ergebnis: 8,95 Millisekunden je Schritt wurden zu 3,30 — Faktor 2,7.

## Was heißt das praktisch

Für Anwender in Deutschland ändert sich durch die Lizenz nichts Nachteiliges: Apache 2.0 erlaubt kommerzielle Nutzung ohne Einschränkung. Der Knackpunkt ist die Hardware. Ein Modell dieser Größe läuft nicht auf einem Arbeitsplatzrechner und auch nicht auf einer einzelnen Grafikarte. Wer Beam selbst betreiben will, braucht ein Rechenzentrum oder einen Anbieter.

Der Ausprobier-Weg ist deshalb ein anderer: [Ollama](https://ollama.com/blog/reflection-beam) gibt Beam befristet kostenlos über die eigene Cloud aus, mit der Zusage, keine Daten zu speichern. Reflection selbst betreibt eine Programmierschnittstelle in einer offenen Beta, und rund 40 Anbieter und Projekte nennen den Starttag — darunter Amazon Web Services, Microsoft Azure, Google Cloud, Cloudflare, CoreWeave, Together AI und OpenRouter.

Eine Einschränkung ist im Modell selbst angelegt: Es wurde laut Modellkarte überwiegend auf Englisch entwickelt. Für deutschsprachige Texte gibt es keine Angaben.

Und der ehrlichste Teil steht in der Ankündigung von Reflection selbst. Das Labor schreibt, wo andere offene Modelle wie Kimi K3 bei der reinen Fähigkeit vorn bleiben, liege Beams Vorteil in der Effizienz zur Laufzeit. Zwei Vergleichstabellen zeigen genau das.

{{chart:beam-terminal-bench}}

Beim {{Benchmark}} Terminal Bench 2.1 liegt Beam mit 80,1 Prozent hinter DeepSeek V4.1 Flash (90,6), Kimi K3 (88,3), GLM 5.3 (88,2), Qwen 3.8 Max (86,6) und GLM 5.2 (81,0). Bei den schweren Wissensfragen sieht es ähnlich aus.

{{chart:beam-hle}}

Solche Herstellerangaben sind mit Vorsicht zu lesen: Reflection hat die Werte für die Konkurrenzmodelle der Tabelle selbst zusammengestellt, und wo für ein Modell kein Wert veröffentlicht war, steht in der Tabelle „NR". Ob die Zahlen einem unabhängigen Nachbau standhalten, ist offen. Ein erster Anhaltspunkt ist, dass Reflection die eigenen Schwächen benennt, statt sie wegzulassen.

## Quellen

- [Beam ist verfügbar — Reflection (16.10.2026)](https://reflection.ai/blog/beam-is-available)
- [Introducing Beam — Reflection (05.10.2026), mit Vergleichstabelle](https://reflection.ai/blog/introducing-beam)
- [Beam-Modellkarte — Reflection](https://reflection.ai/beam-model-card)
- [Beam 1.0 501B A23B — Hugging Face, Modellkarte mit Testwerten](https://huggingface.co/reflection/Beam-1.0-501B-A23B)
- [Welcome Beam: a 501B open model — Hugging Face Blog (16.10.2026)](https://huggingface.co/blog/reflection-beam)
- [Serving Reflection Beam on vLLM from Day 0 (16.10.2026)](https://vllm-project.github.io/2026/10/16/reflection-beam.html)
- [Reflection's Beam is freely available on Ollama](https://ollama.com/blog/reflection-beam)
- [Reflection AI raises $2B — TechCrunch](https://techcrunch.com/2025/10/09/reflection-raises-2b-to-be-americas-open-frontier-ai-lab-challenging-deepseek/)
