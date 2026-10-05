---
title: "OpenAI versteckt Wasserzeichen in KI-Texten: textGrain und seine Grenzen"
slug: "openai-versteckt-wasserzeichen-in-ki-texten-textgrain-und-seine-grenzen"
date: 2026-10-05
time: "17:00"
status: published
tags: [news, openai, llm, sicherheit, ki]
summary: "OpenAI führt Textwasserzeichen ein: In der EU bekommen ChatGPT und Codex in den nächsten Wochen unsichtbare Markierungen, API-Kunden können freiwillig zuschalten. Grund ist Artikel 50 des EU AI Act. Die eigenen Zahlen zeigen die Grenzen der Technik."
source_url: "https://openai.com/index/eu-text-provenance"
source_name: "OpenAI"
lang: de
---

## TL;DR

- Ab dem 5. Oktober 2026 können API-Kunden von OpenAI {{Wasserzeichen}} für Textausgaben zuschalten – freiwillig, standardmäßig bleibt die Funktion aus.
- In der Europäischen Union bekommen ChatGPT und Codex in den kommenden Wochen eine unsichtbare Markierung automatisch. Außerhalb der EU ändert sich am Standard nichts.
- Der Anlass ist [Artikel 50 des EU AI Act](https://artificialintelligenceact.eu/article/50/): Wer KI-Texte erzeugt, muss sie maschinenlesbar als KI-erzeugt kennzeichnen. Die Pflicht gilt seit dem [2. August 2026](https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content).
- Das Verfahren heißt textGrain und verändert beim Schreiben die Wortwahl minimal. Ein Detektor sucht danach.
- Nach [OpenAIs eigener Auswertung](https://openai.com/index/eu-text-provenance) – Herstellerangabe, unabhängig nicht nachgeprüft – erkennt der Detektor bei 1 Prozent Falsch-Positiv-Rate rund 95 Prozent der 400-{{Token}}-Passagen, aber nur etwa 80 Prozent der 200-Token-Passagen.
- Wer 10 Prozent der Wörter durch Synonyme ersetzt, fällt von 92 auf 66 Prozent Erkennung, bei 25 Prozent Ersatz bleiben 17 Prozent. Detektor-Zugang gibt es zunächst nur für geprüfte Forscher.

## Was ist passiert

OpenAI hat am 5. Oktober 2026 [seinen Umgang mit den Transparenzregeln der EU beschrieben](https://openai.com/index/eu-text-provenance) und dazu ein neues {{Wasserzeichen}} für Text vorgestellt. Bis heute gibt es von OpenAI nur Prüfwerkzeuge für Bilder und Audio: die Web-Seite [openai.com/verify](https://openai.com/verify) und eine Programmierschnittstelle, mit der sich feststellen lässt, ob eine Bild- oder Tondatei aus einem OpenAI-System stammt.

Text war bisher außen vor – und das aus gutem Grund. Text lässt sich leicht umschreiben, kürzen oder in eine andere Sprache übersetzen, und jede dieser Änderungen zerstört eine Markierung, die in der Wortwahl steckt.

Die Neuerung besteht aus drei Teilen:

- **Freiwillig in der API:** Ab sofort können Entwickler, die Modelle über die API nutzen, Wasserzeichen für ausgewählte Modelle aktivieren. Standardmäßig bleibt die Funktion aus.
- **In der EU automatisch:** In den kommenden Wochen bekommen ChatGPT und Codex in der EU eine unsichtbare Markierung, auf allen Abo-Stufen. Global will OpenAI das zunächst nicht zum Standard machen.
- **Detektor für Forscher:** Ab jetzt können sich Forscher und Expertengruppen [für den Zugang zu einem Wasserzeichen-Detektor bewerben](https://openai.com/form/content-provenance-api/). Zugelassen wird zunächst nur, wer bei der Bewertung hilft.

Das Verfahren selbst heißt textGrain und ist in einem [technischen Bericht](https://cdn.openai.com/pdf/e9508624-d767-41b6-a26d-e34ca798ada6/textgrain-entropy-calibrated-watermarking-for-language-model-text.pdf) beschrieben, an dem neben OpenAI-Mitarbeitern auch Forscher der University of Pennsylvania und der Yale University beteiligt sind. Der Trick, vereinfacht gesagt: Beim Schreiben wählt das Modell aus mehreren ähnlich passenden Wörtern. textGrain greift in diese Auswahl mit einem geheimen Schlüssel ein – nicht so stark, dass der Text schlechter wird, aber so, dass die getroffene Wahl nicht mehr rein zufällig ist. Der Detektor kennt den Schlüssel und prüft, ob die Wörter zu den erwarteten Mustern passen.

{{chart:textgrain-erkennung-laenge}}

## Warum zählt das

Für Anbieter von KI-Systemen ist die Pflicht nicht freiwillig. [Artikel 50 Absatz 2 des EU AI Act](https://artificialintelligenceact.eu/article/50/) verlangt, dass Ausgaben, die Text, Bild, Ton oder Video erzeugen, „in einem maschinenlesbaren Format markiert und als künstlich erzeugt oder manipuliert erkennbar" sind. Laut EU-Kommission gilt die Anforderung [seit dem 2. August 2026](https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content).

Der Gesetzestext hat eine eingebaute Einschränkung, die in der Praxis alles entscheidet: Die technischen Lösungen sollen wirksam, interoperabel, robust und zuverlässig sein, „soweit dies technisch machbar ist" – unter Berücksichtigung der Eigenheiten verschiedener Inhaltsarten, der Umsetzungskosten und des Stands der Technik. Genau in diesem Vorbehalt argumentiert OpenAI.

Ergänzt wird der Gesetzestext durch einen freiwilligen Verhaltenskodex zur Transparenz KI-erzeugter Inhalte. Bis Ende Juli 2026 haben ihn [nach Angaben der EU-Kommission](https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content) rund 190 Unternehmen und Organisationen unterzeichnet. Ein Kodex, der das Problem löst, ist er nicht – es gibt bis heute keinen allgemein anerkannten Standard, mit dem sich KI-Text zuverlässig als solcher erkennen lässt.

## Wie gut das Wasserzeichen wirklich ist

Interessant ist der Abschnitt, in dem OpenAI selbst aufzählt, wo das Verfahren schwächelt. Die Zahlen stammen aus [OpenAIs eigener Auswertung](https://openai.com/index/eu-text-provenance) – {{Benchmark}}-Werte unabhängiger Labore gibt es dazu bisher nicht.

- **Kurzer Text ist schwer zu erkennen.** Bei einer Zielrate von 1 Prozent falsch-positiver Treffer erkannte der Detektor etwa 80 Prozent der 200-Token-Passagen, aber etwa 95 Prozent der 400-Token-Passagen – getestet an Texten aus dem Bereich Psychologie.
- **Wenig Spielraum, wenig Signal.** In Fächern wie Mathematik, wo die Wortwahl kaum variiert, sinken die Erkennungsraten deutlich.
- **Umschreiben wirkt.** Bei 400-Token-Passagen fiel die Erkennung von rund 92 Prozent auf 66 Prozent, sobald 10 Prozent der Wörter durch Synonyme ersetzt wurden. Bei 25 Prozent Ersatz sank sie auf 17 Prozent.

{{chart:textgrain-editierbestaendigkeit}}

Die Rate falsch-positiver Treffer ist dabei der kritische Wert. Sie sagt, wie oft der Detektor ein Wasserzeichen meldet, obwohl keines da ist. Deshalb gibt es den Detektor nur für geprüfte Forscher: Ein öffentlich zugängliches Werkzeug, das bei 1 Prozent der geprüften Texte einen falschen Verdacht ausspricht, wäre eine Denunziationsmaschine.

OpenAI formuliert außerdem ausdrücklich, was ein Treffer **nicht** bedeutet:

- Ein Wasserzeichen misst nicht den menschlichen Anteil am Text.
- Es klärt keine Urheberschaft und keine Verantwortung – nicht, wem der Text gehört, ob die Nutzung rechtmäßig ist oder wer haftet.
- Es identifiziert keinen Nutzer, kein Konto und keine Konversation.
- Es sagt nichts über die Richtigkeit des Textes aus.
- Und das Fehlen eines Treffers beweist keine menschliche Urheberschaft: Der Text kann zu kurz, zu stark bearbeitet, übersetzt, älter als die Markierung oder von einem anderen Anbieter erzeugt sein.

Ein weiterer Haken liegt im Vergleich mit anderen Verfahren. Laut OpenAI schneide textGrain in den eigenen Tests besser ab als andere geprüfte Ansätze, „einschließlich SynthID für Text". Man kann nicht stark genug betonen: Das ist eine Eigenaussage des Anbieters, unabhängige Vergleiche fehlen. OpenAI schreibt selbst, gute Werte unter idealen Bedingungen garantierten keine verlässliche Erkennung im Alltag.

## Was heißt das praktisch

Für Entwickler, die über die API Texte erzeugen, ändert sich nichts, solange sie nicht bewusst einschalten. Wer Wasserzeichen aktiviert, sollte wissen, dass die Erkennung statistisch bleibt: kein Beweis, sondern eine Wahrscheinlichkeit. Für Unternehmen, die Aufsichtspflichten erfüllen müssen, ist die Opt-in-Möglichkeit trotzdem nützlich – sie erlaubt, Transparenzpflichten sichtbar zu erfüllen, ohne die Ausgabe umzustellen.

Für Leserinnen und Leser in der EU ist der zweite Teil relevant: Wer ChatGPT oder Codex nutzt, bekommt in den kommenden Wochen markierte Ausgaben, ohne es zu merken. Nach OpenAIs Darstellung ändert sich für die Nutzer nichts – bei den Benchmarks für das aktuelle Frontier-Modell Astra sieht der Anbieter „keine bedeutenden Leistungsunterschiede" mit und ohne Wasserzeichen. Auch das ist eine Anbieteraussage.

Für alle, die Texte prüfen wollen, bleibt der wichtigste Punkt: Das Werkzeug dazu wird nicht öffentlich. Es bleibt bei einer Bewerbung, einer Prüfung und einem Zugang auf Zeit. Bis sich das ändert, ist die Erkennung KI-erzeugter Texte genau das, was sie schon vorher war – ein statistischer Hinweis, kein Beleg.

Offen bleibt eine Frage, die OpenAI selbst aufwirft: Wie lässt sich KI-Unterstützung von vollständiger KI-Autorschaft unterscheiden? Das Wasserzeichen markiert Wörter, nicht Arbeitsanteile. Wer einen Text selbst schreibt und nur einzelne Sätze glätten lässt, kann am Ende einen Text haben, der als „von KI bearbeitet" markiert ist – und das Wasserzeichen sagt nichts darüber, wie groß der eigene Anteil war.

## Quellen

- OpenAI, „Our approach to EU text provenance rules", 5. Oktober 2026: https://openai.com/index/eu-text-provenance
- Technischer Bericht „textGrain: Entropy-Calibrated Watermarking for Language Model Text", 5. Oktober 2026 (PDF): https://cdn.openai.com/pdf/e9508624-d767-41b6-a26d-e34ca798ada6/textgrain-entropy-calibrated-watermarking-for-language-model-text.pdf
- Artikel 50 des EU AI Act, Transparenzpflichten: https://artificialintelligenceact.eu/article/50/
- EU-Kommission, „Code of Practice on Transparency of AI-generated Content": https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content
