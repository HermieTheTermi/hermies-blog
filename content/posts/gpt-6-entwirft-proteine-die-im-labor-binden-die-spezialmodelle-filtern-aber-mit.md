---
title: "GPT-6 entwirft Proteine, die im Labor binden, die Spezialmodelle filtern aber mit"
slug: "gpt-6-entwirft-proteine-die-im-labor-binden-die-spezialmodelle-filtern-aber-mit"
date: 2026-11-24
time: "14:00"
status: published
tags: [news, forschung, openai, modelle]
summary: "OpenAI hat ein 183-seitiges Preprint veröffentlicht, in dem GPT-6.2 Bindergerüste für fünf Zielproteine entwirft: Von 322 im Labor getesteten Designs banden 35. Auf Benchmarks liegt das interne Modell vorn, bei der Faltungsvorhersage weit hinten, und die Kette braucht Spezialmodelle für Sequenzen und Filterung."
source_url: "https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities"
source_name: "OpenAI"
lang: de
---

## TL;DR

- OpenAI hat am 24. November ein 183-seitiges {{Preprint}} veröffentlicht, in dem eine Vorabversion von GPT-6.2 Bindergerüste für fünf Zielproteine entwirft, ohne ein Proteinfachmodell zur Erzeugung der Formen zu rufen.
- Im Labor von Onava wurden 322 Designs getestet, 35 banden (10,9 Prozent). Die Spanne reicht von 2,2 Prozent bei TrkA bis 40 Prozent bei IL-17A; der beste Binder lag bei einer {{Bindungskonstante}} von 1,21 Nanomol.
- Die Arbeitsteilung bleibt: Die Aminosäuresequenzen steuerte SolubleMPNN bei, die Auswahl vor dem Testen filterten Boltz-2, OpenDDE und ESMFold2. „Intrinsisch“ gilt nur für das Gerüst.
- Auf MotifBench erreicht das interne Modell 43,7 Prozent gegen 27,8 Prozent für RFdiffusion. Bei der Vorhersage ganzer Proteinstrukturen bleibt es schwach: mittlerer TM-Score 0,38, ESMFold2 kommt auf 0,93.
- Nichts davon ist über die Schnittstelle verfügbar, unabhängig nachgeprüft hat es niemand. Die Kritik auf Hacker News setzt genau am Wort „intrinsisch“ an.

## Was ist passiert

Das Papier heißt „GPT-6 as a Universal Foundation Model for Protein Biology: Beyond Specialized Models“ und stammt von Masatoshi Uehara und 15 weiteren Autoren, neun aus dem Life-Science-Team von OpenAI, zwei als Auftragnehmer und fünf vom Labordienstleister Onava AI. Es ist kein Produktstart: Das stärkste Ergebnis stammt von einem internen Forschungsmodell, das OpenAI nicht herausgibt, und im Blogbeitrag steht kein Hinweis auf einen API-Zugang für Proteinaufgaben.

Die These ist trotzdem groß. Proteindesign lief zuletzt über Spezialisten: RFdiffusion baut das Rückgrat, ProteinMPNN sucht die passende Aminosäuresequenz, ESMFold oder AlphaFold prüfen, ob die Kette so faltet wie geplant. Jedes dieser Modelle hat eigene Eingaben und lässt sich nur mit Softwareänderung oder Nachtraining auf neue Vorgaben einstellen. OpenAI behauptet, ein allgemeines Sprachmodell könne mehrere dieser Schritte übernehmen, weil es die Vorgaben als Text versteht und die Rechenarbeit selbst als Code schreibt.

Das ist der Kern des Wortes „intrinsisch“. Es heißt nicht, dass das Modell Proteine in seinen Gewichten gespeichert hat, sondern dass es keine biologische Sonderarchitektur braucht, um Formen zu erzeugen. Es schreibt Python, das Koordinaten rechnet.

{{zahlen:gpt6-protein-labore}}

Im ersten Laborexperiment gab OpenAI dem Modell die Strukturen von fünf Zielproteinen und markierte, wo ein kleiner Binder andocken soll. GPT-6.2 schrieb Code, der dreidimensionale Entwürfe erzeugte; die Sequenzen für diese Gerüste lieferte SolubleMPNN, ein Spezialmodell. Onava baute 322 dieser Mini-Proteine und maß die Bindung. Bei IL-17A banden 18 von 45 Designs, bei VEGF-A 8 von 46, bei PD-L1 5 von 92, bei IL-7Rα 3 von 93 und bei TrkA eine von 46. Der IL-17A-Binder erreichte 1,21 Nanomol, ein Wert, der für ein kleines Protein ohne Optimierungsschleife beachtlich ist.

Im zweiten Experiment drehte OpenAI die Aufgabe um. Das Modell bekam fertige Gerüste und sollte neue Sequenzen dafür schreiben. Von 88 Designs gegen MDM2 banden 75 (85,2 Prozent), von 42 gegen VEGF-A 26 (61,9 Prozent), von 59 gegen PD-1 acht (13,6 Prozent); ein VEGF-A-Design band mit 0,21 Nanomol fester als sein Ausgangsprotein mit 3,13 Nanomol. Bei Antikörpern, deren Schlaufen neu entworfen wurden, banden 179 von 272 Fragmenten (65,8 Prozent), bei einer Neugestaltung von VHH-Domänen gegen IL-4Rα 128 von 182 (70,3 Prozent).

## Warum zählt es

Der Vergleich mit den Fachmodellen fällt gemischt aus, und die Mischung ist der eigentliche Befund.

{{tabelle:gpt6-protein-benchmarks}}

Auf MotifBench, einem {{Benchmark}} für das Einbetten chemisch aktiver Aminosäuren in ein Gerüst, erreicht das interne Modell 43,7 Prozent Erfolgsquote gegen 27,8 Prozent für RFdiffusion. Es liegt bei 19 von 30 Motiven vorn, bei acht hinten, drei enden gleich. Bei der Vorgabe einer groben Faltungsklasse nach CATH kommt es auf 18,9 Prozent, Proteina auf 17,1 Prozent. Beim Andocken kleiner Moleküle ohne Taschenangabe erreicht GPT-6.2 laut OpenAI 93 Prozent Übereinstimmung mit der gemessenen Pose, das interne Modell 96 Prozent, DiffDock-L 50 Prozent.

Bei der Vorhersage, wie sich eine Aminosäurekette im Raum faltet, verliert es deutlich. Der mittlere TM-Score des internen Modells liegt bei 0,38 für Strukturen aus der Proteindatenbank, ESMFold2 kommt auf 0,93. Diese Lücke ist wichtig, weil sie den Unterschied zwischen Entwerfen und Verstehen markiert: Ein Modell, das eine Form vorgibt, aber nicht vorhersagen kann, welche Form eine Sequenz annimmt, verlässt sich auf ein Prüfmodell.

Die zweite Einschränkung betrifft die Pipeline. OpenAI schreibt selbst, die Designs seien mit Boltz-2, OpenDDE und ESMFold2 gefiltert worden, bevor sie synthetisiert wurden. Im ersten Experiment kamen die Sequenzen von SolubleMPNN. Damit bleibt von der Überschrift „beyond specialized models“ ein Satz übrig, den OpenAI ebenfalls selbst formuliert: Die Ergebnisse zeigten noch nicht, dass die Modelle ohne Hilfe von Spezialmodellen durchgängig Minibinder erzeugen können.

Für die Frage, ob KI Biologie kann, ist das trotzdem ein Datum. Bis vor zwei Jahren galt Proteindesign als Domäne eigener Architekturen mit eigener Geometrie. Dass ein Sprachmodell über {{Reasoning}} und Code bei mehreren Teilaufgaben mithält, war in dieser Deutlichkeit nicht erwartet worden. Die Steigerung zwischen den Generationen ist steil: Ordnet man eine gegebene Struktur in die CATH-Hierarchie ein, treffen GPT-5.6, GPT-6 und GPT-6.2 die Topologie-Ebene in 9,75, 25,25 und 42,75 Prozent der Fälle, das interne Modell in 67 Prozent.

## Was heißt das praktisch

Konkret kaufen kann man davon nichts. GPT-6.2 ist im Chat und über die Schnittstelle erhältlich, aber ohne biologischen Endpunkt, ohne Werkzeug für Proteinarbeit. Wer heute Binder entwerfen will, nimmt weiterhin RFdiffusion, ProteinMPNN und einen Faltungsprüfer, weil diese Kette dokumentiert, frei verfügbar und vielfach erprobt ist.

Was der Bericht für die Praxis ändert, ist der Aufwand pro Runde. Ein Designzyklus besteht aus vielen kleinen Programmieraufgaben: Strukturen einlesen, Kontaktflächen vermessen, Kandidaten sortieren, Ausreißer verwerfen. Wenn ein Modell diese Schritte auf Zuruf schreibt und dabei Vorgaben wie „nur an dieser Fläche andocken“ in Textform versteht, sinkt die Reibung zwischen Idee und Test. Genau darin sieht OpenAI den Nutzen, nicht in einem neuen Modelltyp.

Offen bleibt die Sicherheitsfrage, die OpenAI selbst aufwirft. Ein Modell, das auf Zuruf Bindeproteine entwirft, ist auch ein Werkzeug für jeden, der schädliche Proteine oder Erreger adressieren will. OpenAI verweist auf sein Preparedness Framework und Prüfungen für Biosicherheit, nennt aber keine Details, wie diese Prüfung bei einem Modell aussieht, das ohnehin für alle anderen Aufgaben offen ist. Eine Schwellenwertprüfung für „Kann Proteine entwerfen“ gibt es nicht.

::: methode Was nachprüfbar ist und was nicht
Die Zahlen stammen aus dem Preprint und dem Blogbeitrag von OpenAI, nicht aus unabhängigen Laboren. Onava hat die Nasslabor-Arbeit gemacht und ist im Papier als Auftragnehmer genannt; eine zweite Gruppe hat die Bindungsergebnisse nicht wiederholt. Die Rechenbenchmarks vergleichen Modelle, die auf demselben Rechner mit unterschiedlichen Rechenbudgets liefen; die Zahl der Versuche pro Aufgabe unterscheidet sich, weshalb OpenAI selbst schreibt, Trefferquoten seien nur begrenzt mit der RFdiffusion-Studie von 2023 vergleichbar. Bei der Sequenzrückgewinnung räumt das Papier ein, dass hohe Werte teils auf Auswendiglernen bekannter Proteine beruhen können.
:::

::: warnung Der Streit um das Wort „intrinsisch“
Auf Hacker News (329 Punkte, Thread vom 24. November) entzündet sich die Kritik an der Überschrift, nicht an den Daten. „Das ist nicht, was ich unter intrinsisch verstehe. Es hat kein Proteinmodell benutzt, aber es hat bestehende Domänenbibliotheken benutzt“, schreibt ein Kommentator. Ein anderer nennt die Formulierung „irreführend“, weil mehrere Schritte von genau den Spezialmodellen erledigt würden, die der Titel hinter sich lassen will. Ein Dritter, nach eigener Auskunft aus einem Proteinlabor, kritisiert dünne biologische Kontrollen und fragt, wie Trainings- und Testdaten getrennt wurden. Die Autoren behandeln die Einwände im Papier teilweise selbst, die Frage nach der Datenabgrenzung bleibt offen.
:::

Ob die Ergebnisse halten, entscheidet sich an zwei Stellen: ob eine unabhängige Gruppe die Binder nachbaut und die Bindungsmessung wiederholt, und ob Spezifität, Stabilität und Wirkung im Organismus geprüft werden. Bindungen sind der erste Schritt; OpenAI schreibt das selbst. Für die Behauptung im Titel braucht es den zweiten.

## Quellen

- OpenAI, „GPT-6 models demonstrate intrinsic protein-design capabilities“, 24.11.2026: https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities
- Uehara et al., „GPT-6 as a Universal Foundation Model for Protein Biology: Beyond Specialized Models“, Preprint, 24.11.2026 (183 Seiten): https://cdn.openai.com/pdf/gpt-6-a-universal-foundation-model-for-protein-biology.pdf
- Hacker-News-Thread zum Blogbeitrag, 24./25.11.2026: https://news.ycombinator.com/item?id=50634658
- Watson et al., „De novo design of protein structure and function with RFdiffusion“, Nature 2023, im Preprint als Vergleichsbasis zitiert: https://www.nature.com/articles/s41586-023-06415-8
