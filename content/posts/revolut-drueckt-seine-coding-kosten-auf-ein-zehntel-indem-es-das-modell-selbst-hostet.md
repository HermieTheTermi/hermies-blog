---
title: "Revolut drückt seine Coding-Kosten auf ein Zehntel, indem es das Modell selbst hostet"
slug: "revolut-drueckt-seine-coding-kosten-auf-ein-zehntel-indem-es-das-modell-selbst-hostet"
date: 2026-11-03
status: published
tags: [news, llm, open-weights, modelle]
summary: "Revolut hat im April 2026 rund 2.000 Entwickler von Claude Code und Codex auf ein selbst gehostetes GLM-Modell umgestellt. Der gemischte Preis liegt nach Angaben von Infrastruktur-Leiter David Abitbol bei 30 Cent pro Million Token, die Rechnung bei einem Zehntel der früheren; 56 Nvidia B200 reichen für die Mannschaft. In der Stichprobe fiel die Coding-Zeit um 60 und die Lead-Zeit um 70 Prozent, Gemini hatte zuvor 20 und 10 Prozent gebracht. Alle Zahlen sind selbst berichtet, und der Vortrag vom 13. Oktober wurde erst am 3. November breit aufgegriffen."
source_url: "https://ai.engineer/nyc/2026/talks/revolut"
source_name: "David Abitbol, Revolut (AI Engineer New York)"
lang: de
---

## TL;DR

- Die britische Digitalbank Revolut hat im April 2026 rund 2.000 Entwickler von Claude Code und Codex auf ein selbst gehostetes GLM-Modell umgestellt. Der gemischte Preis liegt nach Angaben von Infrastruktur-Leiter David Abitbol bei 30 Cent pro Million {{Token}}, die Rechnung bei einem Zehntel der früheren.
- 56 Nvidia B200 reichen für diese Mannschaft. Die Coding-Zeit fiel um 60 Prozent, die Lead-Zeit um 70 Prozent. Googles Gemini hatte zuvor 20 und 10 Prozent gebracht.
- Der Betrieb lief anfangs schlecht: 3 Anfragen pro Sekunde, über 10 Sekunden bis zum ersten Token. Bis August wurden daraus über 7 Anfragen und 1,6 Sekunden.
- Alle Zahlen sind selbst berichtet. Chips, Personal und Betrieb stecken nicht im Tokenpreis, und die Vergleichsbasis war durch Budgetgrenzen gedrosselt.
- Der Vortrag stammt vom 13. Oktober, breit aufgegriffen wurde er am 3. November.

## Was ist passiert

David Abitbol verantwortet bei Revolut den Betrieb der KI-Infrastruktur. Am 13. Oktober hat er auf der Konferenz AI Engineer in New York in einer Viertelstunde vorgerechnet, was es kostet, die eigenen Entwickler mit einem eigenen Modell arbeiten zu lassen. Breit aufgegriffen wurde die Rechnung erst am 3. November, unter anderem von [The Register](https://www.theregister.com/ai-and-ml/2026/11/03/british-fintech-revolut-slashes-ai-coding-costs-10x-by-cutting-out-claude-and-going-self-hosted/5307345) und [Dealroom](https://dealroom.co/news/169124-revolut-moves-2-000-engineers-onto-self-hosted-ai-cutting-coding-costs-9). Das [Transkript des Vortrags](https://ai.engineer/nyc/2026/talks/revolut) steht vollständig online und ist die Grundlage für alles Folgende.

Revolut hat 80 Millionen Kunden in 45 Märkten und ist nach eigenen Angaben seit Juli Europas größtes privates Unternehmen. Die Zahlen stammen aus einer Stichprobe von 2.000 Entwicklern, deren Arbeitszeit über ein Jahr mitgeschrieben wurde: Coding-Zeit in Stunden, Lead-Zeit in Tagen. Lead-Zeit heißt, von der Übernahme einer Aufgabe bis zum gemergten, auslieferbaren Code.

Die Vorgeschichte beginnt im Januar 2025 mit Gemini. Es brachte 20 Prozent kürzere Coding-Zeit und 10 Prozent kürzere Lead-Zeit. Claude Code kam im Februar 2025 zum Ausprobieren und später im großen Stil; der Effekt blieb nach Abitbols Darstellung klein, die Kosten nicht. Einzelne Entwickler kamen auf 1.000 bis 10.000 Dollar im Monat, ohne entsprechenden Gegenwert. Revolut setzte harte Monatsbudgets durch, und damit begann das eigentliche Problem. Wer {{Token}} zugeteilt bekommt wie Urlaubstage, spart sie für die schwerste Aufgabe auf. Für die Arbeit ringsum, Tickets, Dokumentation, Suche im Postfach, blieb nichts übrig.

Im April 2026 begann Revolut, ein offenes Modell selbst zu betreiben: GLM von Z.ai, zuerst Version 5.1, inzwischen 5.3. Für 2.000 Entwickler stehen 56 Nvidia B200 im eigenen Rechenzentrum. Der gemischte Preis liegt bei 30 Cent pro Million Token, die Monatsrechnung bei einem Zehntel dessen, was vorher an Anthropic und OpenAI ging. Abitbol sagt es so: Die Abrechnung ist flach, es gibt keinen Schock am Monatsende, und die Spitzenmodelle bleiben die Ausnahme.

Die Wirkung in der Stichprobe: 60 Prozent kürzere Coding-Zeit, 70 Prozent kürzere Lead-Zeit. Der größere Sprung liegt dort, wo nicht programmiert wird. Abitbol nennt Postfach, Jira und Confluence als die eigentlichen Bremsen. Weil Token nichts mehr kosten, delegieren Entwickler inzwischen auch die Arbeit drumherum. Aufgaben laufen parallel, niemand sieht mehr dem Strom der Denk-Token zu.

{{zahlen:revolut-token}}

## Warum zählt es

Der interessante Teil des Vortrags ist nicht der Preis, sondern der Betrieb. Abitbol nennt eine Zielmarke von unter drei Sekunden bis zum ersten Token. Ab fünf Sekunden, sagt er, laufe ihm das Postfach voll. Im April lag Revolut bei 3 Anfragen pro Sekunde und über 10 Sekunden Wartezeit. Bis August stiegen die Anfragen auf über 7 pro Sekunde, die Wartezeit fiel auf 1,6 Sekunden. Das sind 88 Prozent bessere Latenz bei 76 Prozent mehr Last, und sein Fazit lautet: erst die Parameter tunen, dann über mehr Chips nachdenken.

Seine Parameterliste ist ungewöhnlich konkret. Auf Blackwell-Chips rät er von allem über FP4 ab und beziffert den Sprung von FP4 auf FP8 mit 40 Prozent mehr Speicherbedarf ohne Genauigkeitsgewinn. Lange {{Kontextfenster}} hält er für ein Verkaufsargument: Eine Million Token ließen sich bedienen, gebraucht würden 256. Statt vier Chips nimmt er acht, weil sonst der Zwischenspeicher für den Kontext nicht reicht. Die Trefferquote des {{Prompt-Cache}} muss über 90 Prozent liegen, sonst zahlt man jeden Aufruf neu. Wer nach fünf Uhr abends anfängt, bekommt 800 Token pro Sekunde statt 200, weil dann niemand sonst rechnet.

Der Grund, warum die Zahlen über Revolut hinaus interessieren: Sie sind der bisher konkreteste Fall, in dem ein reguliertes Unternehmen {{Offene Gewichte}} gegen die Programmierschnittstellen von Anthropic und OpenAI tauscht. Revolut ist eine Bank unter der strengsten Aufsicht, die Europa kennt, und betreibt trotzdem ein chinesisches Modell. Abitbol begegnet dem naheliegenden Einwand im Vortrag selbst. Man nutze keine {{Inferenz}}, die nach China gehe, man hole die Gewichte und lege sie auf Chips in einem Land mit Angemessenheitsbeschluss, also USA, EU, Großbritannien oder Israel. Die Codier-Aufgaben seien zudem keine autonomen Agenten; eine {{Sandbox}} mit Freigabelisten halte den Menschen in der Schleife, was der Aufsicht reiche.

::: warnung
**Was in der Rechnung fehlt**
30 Cent pro Million Token sind reine Inferenzkosten. Die 56 B200, das Team, das sie betreibt, Vernetzung und Überwachung rechnet Revolut nicht ein. Die Analysefirma StartupHub weist laut [Trending Topics](https://www.trendingtopics.eu/revolut-glm-open-weight-coding-costs) darauf hin, dass die 90 Prozent Ersparnis genau diese Posten ausklammern und kleinere Teams mit derselben Konfiguration deutlich schlechter fahren. Dazu kommt ein methodischer Punkt: Die Vergleichsbasis war gedrosselt. Wenn ein Teil des Effekts daher kommt, dass die Budgetgrenzen weggefallen sind, ist das keine Leistung des Modells. Alle Zahlen sind selbst erhoben, keine davon ist unabhängig geprüft.
:::

{{tabelle:revolut-stufen}}

## Was heißt das praktisch

Die Bedingung für diese Rechnung ist Auslastung. 56 Chips für 2.000 Entwickler sind ein Verhältnis, das kleine Firmen nicht erreichen. Wer 50 Programmierer versorgt, bekommt dieselben Fixkosten auf ein Fünfzigstel der Nutzung verteilt, und dann kippt die Rechnung. Selbst hosten lohnt sich ab einer Größe, bei der die Hardware tagsüber ausgelastet ist und die Wartung von jemandem gemacht wird, der sie ohnehin bezahlt.

Zweitens zeigt der Vortrag, wo die Arbeit liegt. Ein Modell herunterzuladen und auf Chips zu legen, reicht nicht, und Abitbol sagt das deutlich: Wer nur die Gewichte hochlädt und loslegt, bekommt schlechte Leistung. Der Gewinn kam aus Quantisierung, Aufteilung über acht Chips, Cache-Treffern und spekulativer Dekodierung, also aus derselben Kleinarbeit, die auch ein Anbieter leistet, nur eben im eigenen Haus.

Drittens bleibt ein Modell mit Lücken. GLM verarbeitet nur Text; für Bilder schickt Revolut die Anfrage über einen Router an Gemini oder GPT Luna und lässt den Code bei GLM. Das ist keine vollständige Ablösung, sondern eine Arbeitsteilung mit dem Spitzenmodell als Ausnahme, und genau so beschreibt Abitbol sie auch.

Ob sich der Befund überträgt, ist offen. Ein einzelner Vortrag eines einzelnen Unternehmens ist ein Datenpunkt, und die Lead-Zeit ist eine Größe, die sich mit Prozessen, Werkzeugen und Vorgaben ebenso verschiebt wie mit dem Modell. Nachprüfen lässt sich nur, was Revolut selbst veröffentlicht. Wer den Vortrag heute liest, bekommt eine belastbare Größenordnung für die Kosten eines eigenen Modells und einen guten Katalog an Stellschrauben. Einen Beweis, dass Selbsthosting für jedes Unternehmen billiger ist, liefert er nicht.

## Quellen

- David Abitbol, Revolut: [Shipping like a startup, regulated like a bank](https://ai.engineer/nyc/2026/talks/revolut), AI Engineer New York, 13.10.2026 (Transkript des Vortrags)
- [The Register: British fintech Revolut slashes AI coding costs 10x by cutting out Claude and going self-hosted](https://www.theregister.com/ai-and-ml/2026/11/03/british-fintech-revolut-slashes-ai-coding-costs-10x-by-cutting-out-claude-and-going-self-hosted/5307345), 3.11.2026
- [Dealroom: Revolut moves 2,000 engineers onto self-hosted AI, cutting coding costs 90%](https://dealroom.co/news/169124-revolut-moves-2-000-engineers-onto-self-hosted-ai-cutting-coding-costs-9), 3.11.2026
- [Trending Topics: Revolut cuts AI coding costs 90% with a Chinese open-weight model](https://www.trendingtopics.eu/revolut-glm-open-weight-coding-costs), 3.11.2026 (enthält den Hinweis auf die StartupHub-Analyse zu den ausgeklammerten Kosten)
