---
title: "OpenAI zieht zu Google: GPT-6 läuft künftig auch in der Google Cloud"
slug: "openai-modelle-kommen-in-die-google-cloud"
date: 2026-10-21
time: "14:00"
status: published
tags: [news, ki, llm, openai, google, wirtschaft]
summary: "Google Cloud nimmt die drei aktuellen OpenAI-Modelle in seinen Modellkatalog auf: GPT-6 Astra, GPT-6.1 Sol und GPT-6 Luna, zunächst als geschlossene Vorschau. Abgerechnet wird über den Google-Cloud-Marktplatz, die Ausgaben verbrauchen bestehende Cloud-Verpflichtungen. Microsoft bleibt laut OpenAI Hauptpartner, die Exklusivbindung ist aber Geschichte."
source_url: "https://openai.com/index/openai-models-google-cloud"
source_name: "OpenAI"
lang: de
---

## TL;DR

- Google Cloud nimmt die drei aktuellen OpenAI-Modelle in seinen Modellkatalog auf: GPT-6 Astra, GPT-6.1 Sol und GPT-6 Luna. Der Start ist eine geschlossene Vorschau für ausgewählte Firmenkunden.
- Nach Google-Angaben ist Google Cloud damit der einzige große Cloud-Anbieter, der alle drei führenden geschlossenen Modellfamilien im Programm hat: OpenAI, Anthropic und die eigenen Gemini-Modelle.
- Bezahlt wird über den Google-Cloud-Marktplatz: eine Rechnung, und bestehende Cloud-Verpflichtungen lassen sich damit abbuchen.
- Microsoft bleibt laut OpenAI der wichtigste Cloud-Partner. Die Bindung an einen einzigen Anbieter ist damit aber Geschichte.
- Die Modelle sollen bald auch in Googles Programmierumgebung Antigravity und im Gemini-Agenten auftauchen.
- Zwei Datenschutz-Bausteine fehlen noch: Zero Data Retention und Confidential Compute sind angekündigt, aber nicht verfügbar. Preise nennt niemand.

## Was ist passiert

Am 21. Oktober haben OpenAI und Google Cloud gleichzeitig bekannt gegeben, dass die Modelle des einen in der {{Cloud}} des anderen laufen. Konkret wandern GPT-6 Astra, GPT-6.1 Sol und GPT-6 Luna in den Model Garden von Google Cloud — das ist Googles Katalog, in dem Firmenkunden Modelle auswählen und über eine Schnittstelle ansprechen, ohne eigene Infrastruktur zu betreiben ([OpenAI](https://openai.com/index/openai-models-google-cloud), [Google Cloud](https://cloud.google.com/blog/products/ai-machine-learning/google-cloud-brings-openai-models-to-customers)).

Der Start ist klein: Die Modelle laufen zunächst in einer geschlossenen Vorschau für ausgewählte Firmenkunden, Interessenten können über ein Formular Interesse anmelden. Laut OpenAI ist die allgemeine Verfügbarkeit „in den kommenden Wochen" geplant. Schon jetzt sollen Kunden die OpenAI-Modelle über die Schnittstellen von Google Cloud ansprechen und ihre lokalen Codex-Werkzeuge — also OpenAIs Programmierassistenten auf der Kommandozeile oder als Desktop-Programm — mit der Gemini-Plattform verbinden können, die dann die {{Inferenz}} übernimmt.

Der zweite Teil der Ankündigung betrifft das Geld. Wer die OpenAI-Modelle über Google Cloud kauft, kauft sie über den Google-Cloud-Marktplatz. Das heißt: Die Ausgaben stehen auf derselben Rechnung wie Speicher, Datenbanken und Recheninstanzen. Firmen, die sich gegenüber Google zu einem Mindestumsatz verpflichtet haben, können diese Verpflichtung damit abbuchen; die Käufe zählen laut Google auch für die sogenannten Flexible Savings Plans, mit denen Kunden Preisnachlässe für langfristige Nutzung bekommen ([Google Cloud](https://cloud.google.com/blog/products/ai-machine-learning/google-cloud-brings-openai-models-to-customers)).

Der dritte Teil dreht sich um Datenschutz. Google beschreibt mehrere Schutzschichten: Kundenanfragen, Kontext und Antworten bleiben in der vereinbarten Datenzone und werden nicht zum Training von Modellen verwendet; die OpenAI-Modelle laufen auf eigener Google-Infrastruktur, getrennt durch abgeschottete Zugänge; jede Anfrage läuft über eine eigene Identität und taucht im zentralen Audit-Protokoll auf. Zwei der angekündigten Bausteine sind allerdings noch nicht da: Zero Data Retention, also die Zusage, dass Anfragen nach der Antwort überhaupt nicht gespeichert werden, kommt laut Google „bald"; dasselbe gilt für Confidential Compute, bei dem der Speicher auch für den Betreiber nicht lesbar ist.

Bemerkenswert ist der Ton der beiden Stellungnahmen. OpenAIs Präsident Greg Brockman wird mit dem Satz zitiert, die Partnerschaft sei „ein wichtiger Schritt, um unsere leistungsfähigsten Modelle und Codex dort verfügbar zu machen, wo Kunden schon bauen". Googles Cloud-Chef Thomas Kurian sagt, man wolle Kunden „eine breite Auswahl an Modellen, auch von OpenAI" geben, damit sie „das richtige Modell für jede Aufgabe" wählen könnten. Zwei Firmen, die im Modellgeschäft direkte Konkurrenten sind, verkaufen sich gegenseitig als Sortiment.

## Warum zählt es

Für OpenAI ist das eine Vertriebsfrage. Firmenkunden kaufen KI heute selten mit einer neuen Rechnung und einem neuen Vertrag; sie kaufen sie dort, wo sie schon einen Vertrag und ein Budget haben. Wer bei Google Cloud bereits Verpflichtungen eingegangen ist, konnte bisher kein OpenAI-Modell damit bezahlen. Genau diese Lücke schließt die Ankündigung — und sie ist kein Einzelfall: Im Juni 2026 hatten OpenAI und Oracle dasselbe Modell angekündigt, damals für Oracles Cloud-Guthaben ([OpenAI](https://openai.com/index/openai-on-oracle-cloud)).

Für Google ist es eine Positionierung gegen den eigenen Anspruch. Das Unternehmen verkauft seit Jahren das Argument, Gemini sei die günstigste und beste Wahl. Jetzt steht im eigenen Katalog die Konkurrenz, und Google wirbt damit, der einzige große Cloud-Anbieter zu sein, der alle drei führenden geschlossenen Modellfamilien führt: OpenAI, Anthropic und Gemini ([Google Cloud](https://cloud.google.com/blog/products/ai-machine-learning/google-cloud-brings-openai-models-to-customers)). Das ist eine Aussage des Anbieters über sein eigenes Sortiment, keine unabhängig geprüfte Erhebung. Sie passt aber zu dem, was Google parallel tut: Claude-Modelle von Anthropic sind in Googles Programmierumgebung Antigravity verfügbar ([Google Cloud](https://cloud.google.com/blog/products/ai-machine-learning/claude-opus-55-and-claude-sonnet-55-available-in-antigravity)).

Für Microsoft ist die Nachricht der nächste Schritt weg vom Alleinvertrieb. Der OpenAI-Beitrag endet mit dem Satz „Microsoft remains OpenAI's primary cloud partner." Das ist eine Bekräftigung, die man nur schreibt, wenn sie nicht mehr selbstverständlich ist. Die jahrelange Regel, dass OpenAIs Modelle zuerst und exklusiv bei Azure laufen, gilt damit endgültig nicht mehr. Für Kunden heißt das: Der Wettbewerb verschiebt sich von der Frage „Welches Modell?" auf die Frage „Welche Cloud, welche Datenzone, welche Abrechnung?".

Dabei ist offen, wie viel von der Ankündigung Technik und wie viel Marketing ist. Google schreibt selbst, die Modelle liefen „auf dedizierter Google-Cloud-Infrastruktur" und Anfragen gingen durch „gehärtete, isolierte Gateways" — das beschreibt eine Vermittlungsschicht, nicht zwingend eine eigene Modellkopie. Wer genau welche Daten sieht, regelt am Ende der Vertrag zwischen drei Parteien: Kunde, Google und OpenAI. Ein Punkt, den Sicherheitsverantwortliche in regulierten Branchen als erstes fragen werden.

## Was heißt das praktisch

Für Entwicklungsteams, die schon bei Google Cloud sind, wird der Wechsel billiger: Statt einen zweiten Anbietervertrag aufzusetzen, lässt sich ein OpenAI-Modell mit dem vorhandenen Budget testen. Praktisch ist vor allem der Teil mit dem Codex-Werkzeug: Wer den Programmierassistenten lokal nutzt, kann ihn auf die Gemini-Plattform zeigen lassen, ohne die Oberfläche zu wechseln.

Für alle anderen bleibt abzuwarten. Es gibt keine Preise, keine Angaben zu Ratenlimits, keine Regionenliste und keinen festen Termin für die allgemeine Verfügbarkeit. Solange die Vorschau geschlossen ist, hilft nur die Warteliste. Und wer die Modelle heute schon bei Microsoft oder direkt bei OpenAI nutzt, sollte prüfen, ob ein Umzug überhaupt etwas bringt: Rabatte aus bestehenden Azure-Verträgen lassen sich nicht auf Google-Cloud-Guthaben übertragen.

Für regulierte Kunden ist der Zeitpunkt das Problem. Datenzonen, Audit-Protokoll und getrennte Zugänge sind gute Bausteine, aber zwei davon sind noch Ankündigungen. Wer Daten verarbeitet, die nicht gespeichert werden dürfen, muss auf Zero Data Retention warten oder beim bestehenden Anbieter bleiben. Dasselbe gilt für Confidential Compute, das Schutz vor neugierigen Betreibern verspricht — auch das kommt erst „bald".

Was als Nächstes zu beobachten ist: ob Amazon Web Services nachzieht und OpenAI-Modelle in Bedrock aufnimmt, ob Microsoft mit neuen Azure-Konditionen reagiert, und ob Google die Preise für OpenAI-Modelle im eigenen Katalog unter denen von Azure ansetzt. Die Ankündigung selbst ist einen Satz wert, den man in dieser Branche selten hört: Konkurrenten verteilen die Produkte des jeweils anderen, weil Kunden es so wollen.

## Quellen

- [OpenAI: OpenAI models are coming to Google Cloud (21.10.2026)](https://openai.com/index/openai-models-google-cloud)
- [Google Cloud: Google Cloud expands model choice, bringing OpenAI models to customers (21.10.2026)](https://cloud.google.com/blog/products/ai-machine-learning/google-cloud-brings-openai-models-to-customers)
- [OpenAI: Access OpenAI models and Codex through your Oracle cloud commitment (10.06.2026)](https://openai.com/index/openai-on-oracle-cloud)
- [Google Cloud: Claude Opus 5.5 and Claude Sonnet 5.5 are now available in Google Antigravity](https://cloud.google.com/blog/products/ai-machine-learning/claude-opus-55-and-claude-sonnet-55-available-in-antigravity)
