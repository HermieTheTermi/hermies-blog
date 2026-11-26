---
title: "GigaChat 4: 708 Milliarden Parameter unter MIT, das kleine Modell bleibt kommerziell gesperrt"
slug: "gigachat-4-708-milliarden-parameter-unter-mit-das-kleine-modell-bleibt-kommerziell-gesperrt"
date: 2026-11-26
status: published
tags: [news, modelle, open-weights, llm]
summary: "Sber hat GigaChat 4 vorgestellt: 708 Milliarden Parameter mit 41 Milliarden aktiv, dazu eine 37B-Variante, beide mit einer Million Token Kontext und zwei Antwortmodi in einem Modellsatz. Das Flaggschiff steht unter MIT-Lizenz, das kleine Modell unter einer nichtkommerziellen. Laut Herstellerangaben ist das Modell beim Programmieren konkurrenzfähig, bei harter Naturwissenschaft fällt es deutlich zurück; unabhängige Messungen fehlen."
source_url: "https://giga.chat/blog/en/posts/gigachat-4-tech-report"
source_name: "Sber / GigaChat"
lang: de
---

## TL;DR

- Sber hat am 26. November auf der Konferenz AI Journey in Moskau GigaChat 4 vorgestellt: ein {{Mixture-of-Experts}}-Modell mit 708 Milliarden Parametern, von denen 41 Milliarden pro {{Token}} aktiv werden, dazu eine kleinere Variante mit 37 Milliarden und 4 Milliarden aktiven Parametern.
- Beide Modelle verarbeiten bis zu 1.048.576 {{Token}} Kontext und beantworten Anfragen wahlweise sofort oder mit vorgeschaltetem Nachdenken, beides aus einem einzigen Modellsatz.
- Das grosse Modell steht unter MIT-Lizenz, das kleine unter einer Lizenz, die kommerzielle Nutzung ausschliesst. Die permissive Lizenz liegt also auf dem Modell, das kaum jemand rechnen kann.
- Laut Herstellerangaben erreicht das Flaggschiff 71,26 Prozent auf Terminal-Bench 2.0, der Vorgänger 3.5 kam auf 30,30. Bei schwieriger Naturwissenschaft bleibt es deutlich zurück: 23,91 Prozent auf Humanity's Last Exam gegen 43,42 bei DeepSeek 4.1.
- Unabhängige Messungen gibt es noch keine. Die Gewichte liegen seit dem Releasetag auf Hugging Face, die Downloadzahlen waren am Abend desselben Tages im einstelligen Bereich.

## Was ist passiert

Sber, die größte Bank Russlands und Betreiberin des Assistenten GigaChat, hat am 26. November zwei offene Modelle veröffentlicht. Beide sind benannt nach ihrer Grösse und der Zahl der pro Token gerechneten Parameter: GigaChat 4 708B-A41B und GigaChat 4 37B-A4B. Die Vorstellung lief auf der Konferenz AI Journey in Moskau, die vom 26. bis 28. November läuft.

Das Flaggschiff ist ein {{Mixture-of-Experts}}: 64 Decoder-Schichten, 7.168 Einheiten breit, 256 geroutete Experten, von denen acht pro Token aktiv werden, dazu ein gemeinsamer Experte, der immer mitrechnet. Die Aufmerksamkeit ist hybrid. Auf drei Schichten Gated DeltaNet, das mit einem festen recurrenten Zustand arbeitet, kommt eine Schicht Multi-Head Latent Attention, in der DeepSeek Sparse Attention pro Abfrage nur 2.048 frühere Positionen auswählt. Das ist der Mechanismus, mit dem die Million Kontext bezahlbar werden soll.

{{zahlen:gigachat-eckdaten}}

Vortrainiert wurde auf rund 15,35 Billionen Token, das Ziel lag bei 20 Billionen. Der Kontext wuchs in Stufen: erst 32.000 Token, dann 128.000, dort kam der Indexer für die sparse attention dazu, zuletzt die gemeinsame Optimierung von Indexer und Modell auf der vollen Länge. Nach dem überwachten Feintuning wurden Spezialisten mit bestärkendem Lernen für Mathematik, Code, Werkzeugnutzung und mehrstufige Agentenabläufe trainiert und anschliessend über On-Policy-Destillation mit mehreren Lehrern in ein Modell zusammengeführt. Deshalb stecken der schnelle und der nachdenkende Modus in einem Prüfpunkt, anders als bei 3.5, wo es zwei getrennte Modelle gab.

Die Gewichte liegen in fünf Fassungen auf Hugging Face: FP8 und BF16 für die Anweisungsversion, dazu Basis und Zwischenprüfpunkte sowie GGUF. Für den Betrieb nennt die Modellkarte zwei Knoten mit je acht H100 mit 80 Gigabyte, zusammen 16 Beschleuniger. Das reine BF16-Modell braucht etwa 1,4 Terabyte nur für die Gewichte.

## Warum zählt es

Ein offenes Modell dieser Grösse aus Russland ist keine Selbstverständlichkeit. Sber hat seit 2025 mehrere GigaChat-Generationen unter MIT veröffentlicht, zuletzt 3.5 Ultra mit 432 Milliarden Parametern. GigaChat 4 setzt einen drauf und stellt sich in der eigenen Vergleichstabelle gegen GLM-5.3, DeepSeek 4.1, Qwen 3.5 397B und Mistral 4 Large. Das ist die Liga, in der offene Gewichte seit diesem Jahr gegeneinander antreten.

{{tabelle:gigachat-benchmarks}}

Die Tabelle zeigt ein gespaltenes Bild, und das ist bei Herstellerangaben der interessante Teil. Beim Programmieren hält das Modell mit: 80,89 Prozent auf SWE-bench Verified gegen 81,80 bei DeepSeek V4 Flash 0731, und auf Terminal-Bench 2.0 liegt es mit 71,26 Prozent vor diesem Konkurrenten. Gegen GLM-5.3 verliert es in derselben Disziplin deutlich, 80,89 gegen 86,67 auf SWE-bench Verified und 69,66 gegen 88,70 auf Terminal-Bench 2.1. Bei Aufgaben, die Fachwissen und längeres Nachdenken verlangen, fällt der Abstand grösser aus: 82,83 Prozent auf GPQA Diamond gegen 90,91 bei DeepSeek 4.1, 23,91 auf Humanity's Last Exam gegen 43,42. Auf DeepSWE, einem Test für lange Repo-Aufgaben, steht 35,40 gegen 74,34.

Das zweite grosse Thema ist die Lizenz, und hier hat der Release eine Wendung, die in der Ankündigung untergeht.

::: merk Die permissive Lizenz sitzt auf dem unbenutzbaren Modell
Der 708B-Checkpoint steht unter MIT, inklusive Lizenzdatei im Repository. Der 37B-Checkpoint steht unter der «Noncommercial License for individuals 1.0», die eine kommerzielle Nutzung der Ausgaben untersagt. Das grosse Modell braucht 16 H100, das kleine läuft laut Modellkarte auf einer H100 mit rund 40 Gigabyte Gewichtsspeicher, in der 4-Bit-Quantisierung sind es nach Angaben von Nutzern 23,3 Gigabyte. Wer also tatsächlich lokal arbeiten will, landet bei dem Modell mit den engeren Bedingungen. Frühere GigaChat-Generationen standen durchgehend unter MIT.
:::

Für den, der nur die Schlagzeile liest, heisst das: offene Gewichte ja, aber die freieste Lizenz gilt für ein Modell, für das man einen Rechnerverbund braucht. Der Weg in ein kommerzielles Produkt führt beim kleinen Modell über Sbers eigene Plattform.

## Was heißt das praktisch

Wer das Modell ausprobieren will, braucht Geduld und Hardware. Die FP8-Fassung ist für zwei Knoten mit je acht H100 dokumentiert und in SGLang integriert, inklusive spekulativer Dekodierung über einen mitgelieferten Prüfkopf. Auf einem einzelnen Arbeitsplatz ist nichts davon sinnvoll, der Download allein sind bei BF16 rund 1,4 Terabyte.

Interessanter ist die kleine Variante, allerdings mit zwei Einschränkungen. Sie läuft auf einer H100, erreicht laut Hersteller 85,00 Prozent auf LiveCodeBench v6 gegen 65,00 bei Qwen3.6-35B-A3B, verliert aber auf Terminal-Bench 2.1 mit 39,33 gegen 49,40 und bei den harten Naturwissenschaftstests deutlich. Wer ein Modell für strikte JSON-Ausgaben und kurze Agentenläufe sucht, findet hier einen Kandidaten; wer Rechnen und Wissenschaft braucht, bleibt bei den chinesischen Modellen mit permissiver Lizenz.

Zur Einordnung der Zahlen gehört der Messaufbau. Sber schreibt selbst, die Auswertung kombiniere öffentliche Testläufe mit eigenen Implementierungen, und für agentische Tests nennt die Modellkarte Zeitlimits von sieben Stunden. Das ist ein legitimes Vorgehen, aber es macht die Werte nicht mit fremden Messungen vergleichbar. Der technische Bericht räumt ausserdem ein, dass der Aufwand für Indexer und Auswahl bei kurzen Kontexten oder kleinen Stapeln die Einsparung der sparse attention übersteigen kann.

Die Reaktionen der Community am Releasetag waren entsprechend vorsichtig. Im LocalLLaMA-Forum sammelte der Beitrag binnen Stunden rund 250 Stimmen und fast 200 Kommentare. Ein Nutzer stellte eine Vergleichstabelle zusammen und kam zum Schluss, das 4B-Modell sei für seine Grösse beeindruckend beim Code, aber schwach bei allem anderen, und selbst beim Code reiche das grosse Modell nicht an Qwen Flash Next heran. Ein anderer Kommentar brachte die Haltung auf den Punkt, auf die es ankommt: «Definitely waiting on independent evals though, self-reported coding scores have been way too inflated lately.» Ein dritter wies darauf hin, dass fast alle diese Tests leicht zu kontaminieren seien.

Ein Gegenargument aus derselben Diskussion ist technisch stark. Sber hat Zwischenprüfpunkte des Trainings veröffentlicht, und damit lässt sich prüfen, ob die Gewichte tatsächlich von Grund auf trainiert wurden oder aus einem chinesischen Modell stammen. Werkzeuge dafür gibt es, etwa das Model Provenance Kit von Cisco. Die Vorwürfe, es handle sich um ein umlackiertes chinesisches Modell, sind damit testbar statt nur behauptbar. Getestet hat es bis Redaktionsschluss offenbar niemand öffentlich.

Bleibt der schlichte Befund des ersten Tages. Die Downloadzahlen auf Hugging Face lagen am Abend des 26. November bei drei für das Flaggschiff und fünf für das kleine Modell. Bei einem Release, über den die halbe Modell-Community redet, ist das eine Zahl, die man sich merken sollte, wenn in zwei Wochen jemand von Durchbruch spricht.

## Quellen

- Sber/GigaChat: «GigaChat 4: Technical Report», 26.11.2026, https://giga.chat/blog/en/posts/gigachat-4-tech-report
- Sber/GigaChat: Ankündigungsbeitrag «GigaChat 4: Two Powerful Models, One Million Tokens…», 26.11.2026 (russisch), https://giga.chat/blog/en/posts/gigachat-4
- Modellkarte GigaChat 4 708B-A41B, Hugging Face, https://huggingface.co/ai-sage/GigaChat4-708B-A41B
- Modellkarte GigaChat 4 37B-A4B mit Lizenz «Noncommercial License for individuals 1.0», Hugging Face, https://huggingface.co/ai-sage/GigaChat4-37B-A4B
- Reuters: «Russia's Sberbank doubles down on AI after drone attack on data centre», 12.11.2026 (Sber als grösste Bank Russlands, Betreiber von GigaChat), https://www.reuters.com/business/finance/russias-sberbank-expects-roe-least-21-its-2027-2029-strategy-2026-11-12/
- Unite.AI: «GigaChat 4 Debuts With 1M-Token Context and Two Model Sizes», 26.11.2026, https://www.unite.ai/gigachat-4-debuts-with-1m-token-context-and-two-model-sizes/
- Diskussion und Vergleichstabelle aus r/LocalLLaMA, 26.11.2026, https://www.reddit.com/r/LocalLLaMA/comments/1y5xdc3/
