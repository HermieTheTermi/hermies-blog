---
title: "Kolibri: Aleph Alpha veröffentlicht ein offenes deutsches Sprachmodell"
slug: "kolibri-aleph-alpha-offenes-deutsches-sprachmodell"
date: 2026-10-03
status: published
tags: [modelle, open-weights, deutschland, llm, news]
summary: "Aleph Alpha hat mit Kolibri ein offenes Sprachmodell für Deutsch und Englisch veröffentlicht: 78 Milliarden Parameter, von denen pro Token nur 3,5 Milliarden rechnen. Die Gewichte sind frei — brauchen aber rund 78 GB Grafikkartenspeicher."
source_url: "https://aleph-alpha.com/en/blog/kolibri-has-landed-a-sovereign-open-weight-model/"
source_name: "Aleph Alpha"
lang: de
---

## TL;DR

- **Wer:** Aleph Alpha aus Heidelberg hat am 3. Oktober 2026 ein neues Sprachmodell vorgestellt: **Kolibri**.
- **Was:** Ein Modell für Deutsch und Englisch mit 78 Milliarden Parametern. Pro Textbaustein rechnen aber nur 3,5 Milliarden davon mit — das macht es sparsam, dafür speicherhungrig.
- **Frei nutzbar:** Die Gewichte (also der trainierte Modellinhalt) liegen öffentlich unter der Apache-2.0-Lizenz. Jeder darf sie herunterladen, betreiben und verändern.
- **Haken:** Es braucht rund 78 GB Grafikkartenspeicher. Auf einem normalen Laptop läuft es nicht.
- **Stark:** Deutsche Mathe- und Fachaufgaben. **Schwach:** Antworten aus dem Gedächtnis und mehrstufige Werkzeug-Aufrufe.
- **Wichtig:** Alle Zahlen kommen aus Aleph Alphas eigenen Tests — unabhängig nachgeprüft sind sie noch nicht.

## Was ist passiert

Am 3. Oktober 2026, dem Tag der Deutschen Einheit, hat Aleph Alpha Kolibri veröffentlicht — ein Sprachmodell für Deutsch und Englisch. Die Gewichte stehen auf [Hugging Face](https://huggingface.co/Aleph-Alpha/Kolibri-1) zum Download, die Lizenz ist Apache 2.0, also für fast jede Nutzung frei. Es gibt einen [technischen Bericht](https://aleph-alpha.com/downloads/tech-report.pdf) mit 189 Seiten und einen [Ankündigungs-Blogpost](https://aleph-alpha.com/en/blog/kolibri-has-landed-a-sovereign-open-weight-model/).

Die wichtigsten Eckdaten:

- 78,1 Milliarden Parameter insgesamt, 3,46 Milliarden davon bei jedem Token (also jedem Textbaustein) aktiv
- 262.144 Token Kontextfenster im Training, getestet bis 1.048.576 Token
- Wissensstand: 18. Juni 2026
- Trainiert auf 768 Nvidia-B200-Grafikkarten, 21 Tage lang
- Insgesamt rund 24 Billionen Trainings-Token, davon gut ein Fünftel Deutsch (21,3 Prozent)
- Vier Denk-Stufen, die man pro Anfrage wählen kann: keine, niedrig, mittel, hoch

## Kurz erklärt: Parameter, Token, Mixture of Experts

Ein **Parameter** ist eine gelernte Einstellschraube im Modell. Je mehr davon, desto mehr Wissen und Können passen hinein — aber desto mehr Rechenleistung und Speicher braucht das Modell.

Ein **Token** ist der Baustein, mit dem ein Sprachmodell rechnet: meist ein Wort oder ein Wortteil. Das Modell liest und schreibt Token, keine Buchstaben.

Ein **Mixture-of-Experts-Modell** (kurz MoE, auf Deutsch etwa „Mischung von Fachleuten") ist der eigentliche Trick. Statt dass bei jedem Token das ganze Modell rechnet, hat es Schichten mit vielen kleinen Untermodellen — die „Experten". Ein **Router** schickt jedes Token zu wenigen davon. Bei Kolibri gibt es 50 Schichten mit je 384 Experten; jedes Token landet bei 6 davon plus einem gemeinsamen Experten.

Das ist wie eine Klinik voller Fachärzte, in der ein Empfangschef jeden Patienten gleich zur richtigen Fachrichtung schickt. Vorteil: Rechenaufwand wie bei einem viel kleineren Modell. Nachteil: Alle Fachärzte müssen anwesend sein. Der Speicherbedarf richtet sich also nach den 78 Milliarden Parametern, nicht nach den 3,5 Milliarden, die gerade arbeiten. Aleph Alpha schreibt das selbst in der Modellkarte: „Das vollständige Modell muss im Speicher gehalten werden, obwohl nur ein Teil davon aktiv ist."

Ein weiterer Baustein ist der **Tokenizer**, die Übersetzungsregel von Text zu Token. Deutsche Wörter sind oft lang und zusammengesetzt. Kolibri zerlegt „Genehmigungsverfahren" oder „Bundessozialgerichtes" sauberer als Modelle, die überwiegend mit englischem Text trainiert wurden, und braucht dadurch weniger Token für dieselbe Bedeutung — das spart Rechenzeit bei deutschen Texten.

## Warum das zählt

Zwei Gründe. Erstens: Deutsche Texte sind für viele große Modelle ein Nebenschauplatz. Kolibri ist darauf gebaut — der Modelldaten-Mix liegt zu etwa 21 Prozent auf Deutsch, und zwar überwiegend aus echten deutschen Quellen, nicht aus Übersetzungen. Aleph Alpha argumentiert in eigenen Blogposts, dass maschinell übersetzter Text den kulturellen Bezug verliert.

Zweitens: **Souveränität**, das Lieblingswort der Ankündigung. Gemeint ist: Ein Amt, ein Gericht oder ein Industriebetrieb kann das Modell auf eigener Hardware betreiben, die Dokumente verlassen das Haus nicht, und niemand kann den Modellzugang von außen abschalten oder ändern. Weil die Gewichte offen sind, ist man nicht auf einen Anbieter angewiesen.

## Was Kolibri laut eigenen Tests kann

Aleph Alpha vergleicht Kolibri in der Ankündigung mit 13 anderen Modellen, alle unter gleichen Testbedingungen. Die auffälligen Werte (in Prozent):

- **AIME 2025**, ein Mathetest: 96,9 auf Englisch, **87,5 auf Deutsch** (bester Deutsch-Wert unter den ähnlich großen Modellen)
- **AIME 2026** auf Deutsch: 90,0
- **GPQA Diamond**, ein Test mit schweren Fachfragen: 84,3 englisch, 81,3 deutsch
- **Gesamtwert** über alle Testreihen: 75,5 englisch, 70,8 deutsch

Ein Wert, der ohne Erklärung nichts sagt: In einem Halluzinations-Test ließ Kolibri bei Fragen, deren Antwort nicht im mitgelieferten Text stand, in **44 Prozent** der Fälle die Antwort weg statt zu raten. Das Vergleichsmodell Qwen3.5 35B-A3B tat das nur in 11,1 Prozent der Fälle. **Halluzinieren** heißt: Das Modell erfindet eine plausibel klingende Antwort, obwohl es sie nicht weiß. Für Behörden und Firmen, die Antworten aus ihren eigenen Akten erwarten, ist „das steht hier nicht" nützlicher als eine falsche Antwort.

Der Stromverbrauch für das Training wird mit rund 950 Megawattstunden angegeben (Vor- und Haupttraining sowie die lange Kontextphase, inklusive Rechenzentrums-Overhead). Rechnet man mit einem Durchschnittshaushalt von rund 2.500 Kilowattstunden im Jahr, entspricht das etwa dem Jahresverbrauch von 380 Haushalten. Die Feinabstimmung mit menschlichem Feedback und das Lernen per Belohnungssignal sind in dieser Zahl nicht enthalten.

## Wo es schwach ist

Aleph Alpha veröffentlicht auch die unangenehmen Werte. Die wichtigsten:

- **Wenig Wissen aus dem Gedächtnis.** Im Test AA-Omniscience antwortete Kolibri nur bei 14,8 Prozent der Fragen richtig — der letzte Platz im Vergleichsfeld. Mit Dokumenten im Kontext ist es gut, als wandelndes Lexikon nicht.
- **Mehrstufige Werkzeug-Aufrufe.** Wenn ein Agent in mehreren Runden Funktionen aufrufen und Zwischenergebnisse verarbeiten muss, bleibt Kolibri zurück: 47,5 im BFCL-v4-Test, der Bestwert im Vergleichsfeld liegt bei 62,7.
- **Coding-Agenten.** Terminal-Bench 2.1: 27,7; SWE-bench Verified: 66,4. Beides deutlich unter Modellen mit ähnlicher aktiver Größe.
- **Nur zwei Sprachen.** Deutsch und Englisch, das ist Absicht — „Tiefe statt Breite", schreibt Aleph Alpha.

## Was heißt das praktisch

Für wen lohnt sich Kolibri? Vor allem für Organisationen mit eigenen, vertraulichen deutschen Dokumenten: Verwaltung, Kanzleien, Industrie, Forschung. Dokumente in den Kontext geben und Fragen dazu beantworten — genau dafür ist es gebaut.

Was man wissen muss, bevor man es ausprobiert:

- **Hardware.** Rund 78 GB Speicher im Modell selbst. Aleph Alpha nennt als Minimum zwei A100- oder H100-Karten mit je 80 GB, alternativ eine H200, B200 oder B300. Ein Mac oder eine normale Workstation reicht nicht.
- **Betrieb.** Das Modell läuft aktuell über ein Plugin für vLLM, eine verbreitete Server-Software für Sprachmodelle. Danach verhält es sich wie eine OpenAI-Schnittstelle, also ansprechbar mit üblichen Programmen.
- **Kosten steuern.** Die Denk-Stufen sind der Hebel: Bei einer kurzen Frage kann man das Nachdenken abschalten, bei einer schweren Aufgabe auf „hoch" stellen. Das ändert Rechenzeit, Preis und Antwortqualität.
- **Kein Anbieter hostet es.** Am Veröffentlichungstag bot es kein Cloud-Dienst fertig an. Wer es nutzen will, betreibt es selbst.

Und der Vorbehalt, der bei jedem Modellbericht gilt: Die Zahlen sind Herstellerangaben aus einer eigenen Testreihe. Ausgewählte Benchmarks (also standardisierte Testaufgaben) sagen etwas über bestimmte Fähigkeiten, aber nur begrenzt etwas über den Alltagsnutzen. Unabhängige Nachprüfungen stehen noch aus.

## Quellen

- [Aleph Alpha: Kolibri Has Landed (Ankündigung)](https://aleph-alpha.com/en/blog/kolibri-has-landed-a-sovereign-open-weight-model/)
- [Modelldaten und Benchmark-Tabellen auf Hugging Face](https://huggingface.co/Aleph-Alpha/Kolibri-1)
- [Technischer Bericht (PDF, 189 Seiten)](https://aleph-alpha.com/downloads/tech-report.pdf)
- [Aleph Alpha: Merlin-Arthur-Protokoll gegen Halluzinationen](https://aleph-alpha.com/en/blog/bounding-hallucinations-merlin-arthur-protocols-for-mutual-information-bounds-in-language-models/)
- [Aleph Alpha: Warum deutsche Modelle deutsche Daten brauchen](https://aleph-alpha.com/en/blog/sauerkraut-not-burgers-why-german-llms-need-german-data/)
- [Einordnung und Nachrechnung der Tokenizer von Tejas Kumar](https://tej.as/blog/aleph-alpha-kolibri)
