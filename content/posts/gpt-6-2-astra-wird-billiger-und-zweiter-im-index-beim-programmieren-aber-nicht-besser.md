---
title: "GPT-6.2 Astra wird billiger und Zweiter im Index, beim Programmieren aber nicht besser"
slug: "gpt-6-2-astra-wird-billiger-und-zweiter-im-index-beim-programmieren-aber-nicht-besser"
date: 2026-11-17
status: published
tags: [news, modelle, llm, benchmark, openai]
summary: "OpenAI senkt die Preise für sein Flaggschiff um 20 Prozent, beim gecachten Input um 60 Prozent, und landet im unabhängigen Intelligence Index auf Platz zwei hinter Claude Fable 5.2. Derselbe Index zeigt beim Programmieren keinen Fortschritt, für Sol sogar drei Punkte Verlust, und Halluzinationsraten von 59 und 55 Prozent. Astra ist zudem das erste extern veröffentlichte OpenAI-Modell mit der Stufe High für KI-Selbstverbesserung."
source_url: "https://openai.com/index/introducing-gpt-6-2-astra-sol"
source_name: "OpenAI"
lang: de
---

## TL;DR

- OpenAI hat am 17. November **GPT-6.2 Astra** und **GPT-6.2 Sol** veröffentlicht, beide über ChatGPT Work, Codex und die API als `gpt-6.2-astra` und `gpt-6.2-sol`.
- Astra kostet 8 Dollar je Million Eingabe-Token, 0,40 Dollar für zwischengespeicherte Eingabe und 40 Dollar je Million Ausgabe-Token. Das sind 20 Prozent weniger als bei GPT-6 Astra, beim {{Prompt-Cache}} sogar 60 Prozent.
- Im unabhängigen Intelligence Index von Artificial Analysis erreicht Astra 62 Punkte und Platz zwei hinter Claude Fable 5.2. Sol kommt auf 57 Punkte, zwei mehr als der Vorgänger.
- Beim Programmieren bringt die neue Version nichts: Im Coding Agent Index von Artificial Analysis liegt Astra gleichauf mit GPT-6 Astra, Sol verliert drei Punkte.
- Laut derselben Auswertung halluzinieren Astra und Sol in 59 und 55 Prozent der Fälle, in denen sie die Antwort nicht wissen. Die Anbieterzahlen zeigen stattdessen Gewinne von 5 bis 9 Punkten auf ihren eigenen {{Benchmark}}s.
- Astra ist das erste extern veröffentlichte OpenAI-Modell, das die Stufe „High" für KI-Selbstverbesserung erreicht. Diese Einstufung steht im hinteren Teil der Ankündigung.

## Was passiert ist

Die Ankündigung ist eine Preismeldung mit Modellen drumherum. GPT-6.2 Astra kostet je Million {{Token}} 8 Dollar für Eingabe, 0,40 Dollar für gecachte Eingabe und 40 Dollar für Ausgabe ([OpenAI](https://openai.com/index/introducing-gpt-6-2-astra-sol/), 17. November 2026). Beim Vorgänger GPT-6 Astra waren es 10, 1 und 50 Dollar. Sol bleibt bei den 2, 0,10 und 10 Dollar, die schon GPT-6.1 Sol verlangte. Beide Modelle fassen eine Million {{Token}} Kontext.

Auf den hauseigenen Prüfungen sieht der Sprung groß aus. Auf Agents' Last Exam, das mehrstufige Berufsarbeit testet, liegt Astra 5,2 Punkte über GPT-6 Astra und braucht dafür weniger als ein Drittel der Rechenkosten je Aufgabe. Gegen Claude Fable 5.2 meldet OpenAI 5,5 Punkte Vorsprung bei rund 5 Prozent der Kosten. Auf Terminal-Bench-Science 0.1 sind es 9 Punkte mehr als beim Vorgänger, in Harvey LAB-AA mehr als das Doppelte der Durchlassquote von Fable 5.2 bei einem Sechstel der Kosten.

Sol tritt als Arbeitstier an. In FrontierCode 2.0 von Cognition bleibt es 0,5 Punkte unter Astra, zu etwa einem Fünftel der Kosten. Auf dem internen GDPval v2 legt Astra 6,2 Punkte zu und schreibt dabei 22 Prozent weniger Ausgabe-Token.

{{tabelle:gpt62-preis-und-index}}

Solche Zahlen sind Anbieterzahlen. Der Fußnotentext der Ankündigung räumt eine ein: Die Ergebnisse von Fable 5.2 auf Agents' Last Exam lassen neun Aufgaben aus, bei denen ein Ersatzmodell einspringen musste. Wer die Punktedifferenz liest, liest sie gegen eine verkürzte Vergleichsreihe.

## Warum zählt es

Der unabhängige Blick fällt gemischter aus, und er kommt von derselben Institution, die OpenAI in der Ankündigung zitiert. Artificial Analysis setzt Astra mit 62 Punkten auf Platz zwei des Intelligence Index v5, fünf Punkte über GPT-6 Astra und vor Gemini 4 Carbon (60) und Claude Opus 5.5 (59) ([AA](https://artificialanalysis.ai/articles/openai-has-the-2-model-in-the-intelligence-index-with-the-release-of-gpt-6-2-astra-and-gpt-6-2-sol), 17. November 2026). Nur Claude Fable 5.2 liegt darüber.

In derselben Auswertung steht der Haken. Im Coding Agent Index, gemessen im Codex-{{Harness}} bei maximalem Aufwand, liegt Astra genau auf dem Niveau von GPT-6 Astra. Sol verliert drei Punkte gegenüber GPT-6.1 Sol, getrieben von einem Rückgang um 14 Punkte in SWE-Atlas-QnA-AA, wo das neue Modell häufiger wichtige Fakten weglässt. Ein Punkt mehr auf einem Sammelindex, null Punkte beim Programmieren: Für die Berufsgruppe, die diese Modelle am meisten benutzt, ist das die eigentliche Nachricht des Tages.

Dazu kommen die Fehlerquoten. Artificial Analysis misst für Astra 59 und für Sol 55 Prozent {{Halluzination}}srate bei maximalem Aufwand, also den Anteil der Fragen, bei denen das Modell rät, obwohl es die Antwort nicht kennt. Die Kosten je Indexaufgabe liegen bei 4,00 Dollar für Astra und 1,01 Dollar für Sol. Der Preis pro Token sinkt, der Preis pro erledigter Aufgabe bleibt für Astra im oberen Bereich: Die Auswertung nennt das Modell ausdrücklich teuer im Vergleich zu anderen Modellen derselben Preisklasse.

::: warnung Der Satz, der fehlt
In der Ankündigung steht kein Wort über Programmierleistung im Vergleich zum direkten Vorgänger. Der Abschnitt zu Code spricht von saubererem Stil, fokussierteren Tests und weniger Überarbeitungsrunden, ohne Zahl zum Coding-Index. Auf Terminal-Bench-Science und in FrontierCode gewinnt Astra, im Coding Agent Index steht es still. Beides kann stimmen, weil die Prüfungen unterschiedliche Dinge messen. Nur eine der beiden Aussagen steht im Werbetext.
:::

Die dritte Einstufung betrifft die Sicherheit und geht in der Preisberichterstattung unter. Astra ist laut OpenAI das erste extern veröffentlichte Modell des Hauses, das die Stufe „High" im Bereich KI-Selbstverbesserung erreicht. High heißt in der Sprache des Preparedness Framework: Der Effekt entspricht einem zusätzlichen, sehr fähigen Forschungsingenieur für jeden OpenAI-Forscher, gemessen gegen den Stand von 2024. Beide Modelle erreichen zudem die Stufe „Critical" bei Cyberfähigkeiten, weshalb OpenAI die Schutzmaßnahmen für Angriffsaufgaben verschärft hat, was laut Ankündigung auch legitime Arbeiten zur Suche nach Sicherheitslücken erschwert.

Unabhängige Prüfer bestätigen die Richtung. Epoch AI hat sieben Lösungen von 68 FrontierMath-Aufgaben im {{Beweisassistent}} Lean verifiziert, der bisherige Bestwert lag bei drei ([Epoch AI](https://x.com/EpochAIResearch/status/2122762423501467663), 17. November 2026). Vals AI meldet für seinen Index zur Selbstverbesserung einen Anstieg von 27,07 auf 29,01 Prozent, wobei 50 Prozent den menschlichen Referenzwert markiert. Mercor misst Astra auf OpenWorldEngineer mit 67,2 Prozent, Fable 5.2 mit 54,6 und GPT-6 Astra mit 44,2.

Und die Praktiker? Die Urteile gehen weit auseinander. Matt Shumer nennt die Modelle nach Wochen im Test „im Wesentlichen unbrauchbar" und berichtet, seine Opus- und Fable-Agenten hätten die Arbeit von Astra-{{Subagent}}en oft zurückgewiesen. Simon Willison hat denselben Drei-JS-Prompt durch mehrere Modelle laufen lassen und schreibt, weder Astra noch Sol hätten die Verwandlung in einen Mecha so gut hinbekommen wie Claude Fable 5.2 und Gemini 4 Carbon ([Willison](https://simonwillison.net/2026/Nov/17/), 17. November 2026). Im Hacker-News-Thread zur Ankündigung, 1.326 Punkte und 834 Kommentare, halten mehrere Kommentatoren die mitgelieferten Foliensatz-Beispiele für schlechter als die von GPT-6 Astra. Latent Space fasst die Lage so zusammen: ungewöhnlich stark negatives Echo von Testern, teils überzogen, teils berechtigt.

## Was heißt das praktisch

Für die Modellwahl zählt der Preis je Aufgabe, nicht je Token. Sol trägt den Alltag: 57 Indexpunkte, gut eine Minute bis zum ersten Antwort-Token gegenüber 171 Sekunden bei Astra, und 1,01 statt 4,00 Dollar je Indexaufgabe. Wer Astra für eine schwierige Analyse bucht, sollte die Latenz mitplanen. 12,9 Minuten je Indexaufgabe sind kein Chat-Tempo.

Wer lange Agentenläufe fährt, profitiert vom Cache-Rabatt stärker als vom Tokenpreis. 0,40 statt 1,00 Dollar je Million gecachte Eingabe-Token senken die Kosten genau dort, wo Agenten ihr Geld verbrennen: im wiederholten Lesen desselben Kontexts. OpenAI empfiehlt in der Ankündigung ausdrücklich, den Prompt-Anfang unverändert zu lassen und neue Anweisungen hinten anzuhängen. Das ist keine Stilfrage, sondern die Bedingung dafür, dass der Cache greift.

Für alles, was Code ist, lohnt der Blick auf die Alternative. Drei Punkte Verlust bei Sol im Coding Agent Index und ein unverändertes Astra bedeuten, dass der Vorgänger nicht schlechter ist. Wer mit GPT-6.1 Sol zufrieden war, hat keinen Grund zu wechseln, außer er braucht die bessere Wissenschafts- und 3D-Leistung: In AA-3D führt Astra mit 1.318 Elo vor Fable 5.2 (1.271) und Sol (1.259), in der Robotik-Vorschau von Artificial Analysis steht es 79 zu 75 gegen Fable 5.2.

Die Selbstverbesserungs-Einstufung ist der Punkt, an dem sich in den nächsten Monaten zeigt, ob die Aufsicht mithält. OpenAI beschreibt Control-Room-Systeme, die Forschungs-Workloads überwachen und Ausgaben anhalten können. Ob solche Systeme greifen, prüft niemand von außen. Bis dahin bleibt die Einstufung eine Selbstauskunft mit Systemkarte.

## Quellen

- OpenAI: [Introducing GPT-6.2 Astra and Sol](https://openai.com/index/introducing-gpt-6-2-astra-sol/), 17. November 2026 (Preise, Benchmarkangaben, Preparedness-Einstufungen, Alignment)
- OpenAI: [Systemkarte GPT-6.2 Astra und Sol](https://deploymentsafety.openai.com/gpt-6-2-astra-sol), 17. November 2026
- Artificial Analysis: [OpenAI has the #2 model in the Intelligence Index](https://artificialanalysis.ai/articles/openai-has-the-2-model-in-the-intelligence-index-with-the-release-of-gpt-6-2-astra-and-gpt-6-2-sol), 17. November 2026 (Indexwerte, Coding Agent Index, Halluzinationsraten, Kosten je Aufgabe)
- Artificial Analysis: [Modellseite GPT-6.2 Astra](https://artificialanalysis.ai/models/gpt-6-2-astra) und [GPT-6.2 Sol](https://artificialanalysis.ai/models/gpt-6-2-sol), abgerufen 18. November 2026 (Latenz, Kontextfenster, Kosten je Indexaufgabe)
- Latent Space: [AINews zu GPT-6.2 Astra](https://latent.space/p/ainews-gpt-6-2-astra-the-2-frontier-model-is-better-and-20-600-cheaper-but-has-mixed-reviews-6-2-sol), 18. November 2026 (Testerstimmen, Mercor, Epoch, Vals, Perplexity)
- Simon Willison: [Archiv 17. November 2026](https://simonwillison.net/2026/Nov/17/), 17. November 2026 (eigener Vergleichstest, Preisrechnung)
- Hacker News: [GPT-6.2 Astra and Sol](https://news.ycombinator.com/item?id=50535230), 1.326 Punkte, abgerufen 18. November 2026
- Mercor: [OpenWorldEngineer-Ergebnisse](https://x.com/mercor/status/2122754439094354101), 17. November 2026
- Epoch AI: [FrontierMath-Erdős-Ergebnisse](https://x.com/EpochAIResearch/status/2122762423501467663), 17. November 2026
- Vals AI: [RSI-Index](https://x.com/ValsAI/status/2122751897434309101), 17. November 2026
- Matt Shumer: [Einschätzung nach Wochen im Test](https://x.com/mattshumer_/status/2122752192226406421), 17. November 2026
