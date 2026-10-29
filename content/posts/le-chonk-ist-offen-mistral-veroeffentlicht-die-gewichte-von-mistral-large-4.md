---
title: "Le Chonk ist offen: Mistral veröffentlicht die Gewichte von Mistral Large 4"
slug: "le-chonk-ist-offen-mistral-veroeffentlicht-die-gewichte-von-mistral-large-4"
date: 2026-10-29
time: "13:00"
status: published
tags: [news, mistral, modelle, llm, open-weights, benchmark]
summary: "Mistral hat die Gewichte von Mistral Large 4 freigegeben, intern Le Chonk genannt: eine Billion Parameter, 52 Milliarden davon pro Token aktiv, trainiert auf 3.800 Grace-Blackwell-Chips in Europa. Beim Coden liegt das Modell laut Artificial Analysis gleichauf mit dem bisherigen offenen Spitzenmodell GLM-5.3, im Gesamtindex aber nur bei 26 Punkten gegen 32 für DeepSeek V4.1 Flash und GLM-5.3 sowie 46 für Kimi K3.1 Pro, dessen Gewichte noch fehlen. Der API-Preis fällt auf 0,70 und 2,10 Dollar je Million Token. Selbst betreiben braucht laut SGLang-Doku acht B300-Chips, und die Lizenz verlangt für Cloud-Anbieter eine Extra-Genehmigung."
source_url: "https://mistral.ai/news/mistral-large-4-oss/"
source_name: "Mistral AI"
lang: de
---

## TL;DR

- Mistral hat am Donnerstag die Gewichte von **Mistral Large 4** freigegeben, intern „Le Chonk" genannt: rund **1 Billion {{Parameter}}** (1.000 Milliarden), davon etwa **52 Milliarden pro {{Token}}** aktiv. Trainiert wurde auf 3.800 Grace-Blackwell-GPUs in eigenen Rechenzentren in Europa.
- Im **Coding Agent Index** von Artificial Analysis kommt Le Chonk auf **48 Prozent** – praktisch gleichauf mit dem bisherigen offenen Spitzenmodell GLM-5.3, laut Mistral aber mit **47 Prozent weniger Token** pro Aufgabe.
- Im **Intelligence Index v5** derselben Tester steht es bei **26 Punkten**. Die offenen Modelle aus China liegen höher: DeepSeek V4.1 Flash und GLM-5.3 bei je **32**, Kimi K3.1 Pro bei **46** – dessen Gewichte sind allerdings noch nicht veröffentlicht.
- Der API-Preis fällt deutlich: **0,70 Dollar** je Million Eingabe-Token (gecacht 0,07 Dollar) und **2,10 Dollar** je Million Ausgabe-Token. In der Vorschau waren es 1,36 und 4,18 Dollar.
- **Die Haken:** Wer das Modell selbst betreiben will, braucht laut SGLang-Dokumentation acht B300-Grafikchips für die Standardfassung. Und die Lizenz ist MIT mit einem Zusatz: Wer das Modell als Cloud-Dienst verkauft, muss bei Mistral eine eigene Lizenz kaufen.

## Was ist passiert

Mistral hat am Donnerstag [die Gewichte von Mistral Large 4 veröffentlicht](https://mistral.ai/news/mistral-large-4-oss/). Das Modell lief seit dem 6. Oktober als Vorschau über die eigene {{API}} – wir hatten die Vorschau [hier schon beschrieben](/mistral-large-4-europas-billionen-modell-fuehrt-beim-cyber-test-weil-andere-ablehnen.html); jetzt kann es jeder herunterladen, der die Hardware dafür hat. Der Spitzname „Le Chonk" ist Internet-Slang für eine besonders kräftige Katze, mit französischem Artikel davor – eine Anspielung auf die schiere Größe.

Die Zahl, um die sich alles dreht, steht in der [{{Modellkarte}} auf Hugging Face](https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B): rund eine Billion {{Parameter}}, also 1.000 Milliarden. Pro Token rechnen aber nur etwa 49 Milliarden davon, mit Ein- und Ausgabeschicht sind es 52 Milliarden. Das ist der Aufbau, den die Branche {{Mixture-of-Experts}} nennt: 128 spezialisierte Teilnetze, von denen für jedes Wort nur vier aktiv werden, plus ein gemeinsames Netz, das immer mitrechnet. So wächst die Rechenlast mit der Qualität, aber nicht im gleichen Tempo wie die Parameterzahl.

Dazu kommen die übrigen Eckdaten aus der Modellkarte:

- **{{Kontextfenster}}:** eine Million Token, also grob 700.000 Wörter auf einmal.
- **{{Multimodal}}:** Text und Bilder rein, Text raus. Der Bild-Encoder folgt dem Pixtral-Muster und kommt mit unterschiedlichen Bildgrößen zurecht.
- **Sprachen:** laut Mistral fließend in über 160 Sprachen, darunter alle Amtssprachen der Europäischen Union.
- **Drei Denkstufen:** `low`, `medium` und `high`, wobei `high` die Voreinstellung ist. Die Stufe lässt sich pro Anfrage setzen, gedacht als Schalter zwischen billiger Kurzantwort und langer Agenten-Aufgabe.

Trainiert wurde das Modell laut Mistral von Grund auf auf 3.800 Nvidia-Grace-Blackwell-Chips in eigenen Rechenzentren in Europa – das ist der Kern des Werbeversprechens „souveräne KI".

Zwischen Vorschau und Veröffentlichung hat Mistral nach eigener Darstellung mit {{Reinforcement Learning}} weitertrainiert, also mit Belohnung für gute Ergebnisse statt mit reinem Nachahmen von Beispieltexten. Die wichtigsten Zahlen dieser Nachschulung, alle vom Hersteller:

- **Terminal-Bench 4.0:** von 28 auf **41 Prozent**, ein Plus von 13 Punkten. Der Test verlangt, Aufträge in einem echten Terminal zu erledigen.
- **BrowseComp:** **84,5 Prozent** beim Surfen im Web, nach 75 Prozent beim Zwischenstand vor dem RL-Training.
- **B3 Agent Security Benchmark:** **97,1 Prozent** der Angriffe abgewehrt, vorher 93,3 Prozent. Der Test versucht, dem Modell über präparierte Inhalte fremde Befehle unterzuschieben.
- **Ablehnung schädlicher Cyber-Anfragen:** **96,6 Prozent** laut Mistral, der höchste Wert unter offenen Modellen.

{{chart:mistral-chonk-terminal}}

## Warum zählt es

**Erstens: Das ist der größte Gewichtssatz, der je aus Europa kam.** {{Offene Gewichte}} in dieser Größenordnung hat bisher kein europäisches Labor veröffentlicht. Eine Billion Parameter verschiebt die Grenze – und das Argument, dass nur amerikanische und chinesische Labore ganz vorne mitspielen, bekommt einen Riss. Mistral betont, das Modell sei vollständig in Europa trainiert und ohne API-Zwang auf eigener Hardware nutzbar. Genau das verkaufen sie jetzt Banken und Behörden: Die ABN AMRO und die Belfius werden in der Ankündigung als Referenzkunden genannt.

**Zweitens: „offen" heißt hier nicht ganz offen.** Die Lizenz heißt „Mistral Ecosystem Open-Weight License" und ist eine [abgewandelte MIT-Lizenz](https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B/blob/main/LICENSE). Nutzen, verändern, kommerziell einsetzen und feintunen ist erlaubt. Wer das Modell aber als Dienst anbietet – also über eine API weiterverkauft –, braucht eine zusätzliche Lizenz von Mistral. Für Firmen, die das Modell intern einsetzen, ändert sich nichts. Für Anbieter wie Together, Fireworks oder OpenRouter ist es ein Lizenzvertrag.

**Drittens: Die Coding-Stärke ist echt, die Gesamtbilanz nicht.** Auf dem Coding Agent Index von Artificial Analysis meldet Mistral 48 Prozent und damit ein Kopf-an-Kopf-Rennen mit GLM-5.3. Der Punkt dahinter ist der Token-Verbrauch: Mistral sagt, sein Modell brauche 47 Prozent weniger Token pro Aufgabe – bei gleicher Punktzahl heißt das weniger Rechenzeit und niedrigere Rechnung. Unabhängig nachgeprüft ist das inzwischen teilweise: Artificial Analysis führt Le Chonk in der [öffentlichen Tabelle](https://artificialanalysis.ai/leaderboards/models) mit 26 Punkten im Intelligence Index v5, 161 Token pro Sekunde und 2,06 Dollar Kosten je Index-Aufgabe.

{{chart:mistral-chonk-index}}

Der Gesamtindex erzählt eine andere Geschichte als die Coding-Folien. DeepSeek V4.1 Flash und GLM-5.3 stehen dort bei je 32 Punkten, Xiaomis MiMo-V2.6-Pro bei 30 – alle drei aus China und alle drei älter. Mistral selbst formuliert es zurückhaltend: 26 Punkte seien der höchste Wert unter den offenen Modellen aus dem Westen. Das ist richtig und trotzdem eine Einschränkung, die man beim Lesen mitnehmen sollte.

**Viertens: Der Cyber-Titel hat einen Haken.** Mistral nennt Large 4 „das führende offene Modell für Cyber-Verteidigung" und verweist auf 51 Prozent im Cyber Index von Artificial Analysis. Die eigene Grafik zeigt aber zwei offene Modelle davor: DeepSeek V4.1 Flash mit 57 und MiMo-V2.6-Pro mit 56 Prozent. Damit steht Le Chonk auf Platz drei unter den offenen Modellen – und Kimi K3.1 Pro führt den Index mit 64 Prozent an. Das hat The Decoder in seiner [Auswertung der Veröffentlichung](https://the-decoder.com/paris-based-mistral-releases-le-chonk-a-strong-coding-model-that-still-trails-china-overall/) nachgerechnet.

**Fünftens: Der Vorsprung ist geliehen.** Kimi K3.1 Pro von Moonshot steht im Intelligence Index bei 46 Punkten und im Terminal-Bench bei 67 Prozent – deutlich über Le Chonk. Die Gewichte dieses Modells sollen bis zum 4. November erscheinen. Mistrals Vergleichstabellen lassen Kimi K3.1 Pro aus, formal zu Recht, weil es noch kein offenes Modell ist. Sobald die Gewichte da sind, dürfte der Titel „bestes offenes Modell fürs Coden" wieder nach China wandern.

## Was heißt das praktisch

**Für alle, die es kaufen statt betreiben wollen:** Der Preis ist der eigentliche Grund, sich das Modell anzusehen. 0,70 Dollar je Million Eingabe-Token und 2,10 Dollar je Million Ausgabe-Token sind deutlich weniger als die 1,36 und 4,18 Dollar der Vorschau. Gecachte Eingabe kostet 0,07 Dollar, also 90 Prozent weniger – das zählt bei {{Agent}}en, die dieselbe Datei im Kreis lesen. Zum Vergleich: Kimi K3.1 Pro steht bei 2 und 10 Dollar, GLM-5.3 bei ähnlichem Preisniveau wie Le Chonk, DeepSeek V4.1 Flash ist mit 0,60 Dollar je Index-Aufgabe noch einmal deutlich billiger.

{{chart:mistral-chonk-kosten}}

**Für alle, die selbst betreiben wollen:** Hier wird es ernüchternd. Eine Billion Parameter passen nicht in eine Workstation. Laut den SGLang-Dokumenten läuft die Standardfassung auf acht B300-Chips – also einer Maschine, die in ein Rechenzentrum gehört und nicht unter einen Schreibtisch. Mistral liefert für Blackwell-Rechner eine {{Quantisierung}} in NVFP4 mit, die den Speicherbedarf senkt; für diese Fassung nennt die Dokumentation vier GB300-Chips. Ein einzelner Laptop bleibt außen vor – offene Gewichte sind hier ein Angebot an Firmen und Rechenzentren, nicht an Bastler.

Wer es trotzdem versucht, bekommt von Mistral fertige Rezepte: einen vLLM-Aufruf mit `--tensor-parallel-size 8`, SGLang-Unterstützung und eine spekulative Dekodierung namens DSpark, die laut Modellkarte bis zu **1,9-mal** mehr {{Durchsatz}} bringt. Bei dieser Technik rät ein kleines Modell die nächsten Wörter vor, das große prüft sie nur – ein Trick, der die Ausgabe nicht verändert, aber schneller macht.

**Für europäische Einkäufer:** Das Modell ist ab sofort über die Mistral-API, über OpenRouter, über Microsoft Foundry und als Nvidia-NIM-Container zu haben. Wer Datenhoheit braucht, kann es im eigenen Rechenzentrum laufen lassen und mit eigenen Sicherheitsdaten nachschulen – Mistral verkauft dafür Forge und Studio als Zusatzprodukte.

**Und die Einordnung:** Alle Verbesserungen zwischen Vorschau und Endfassung stammen aus Mistrals eigener Testreihe. Die Zahlen von Artificial Analysis sind unabhängig erhoben, aber der Index v5 existiert erst seit dem 27. Oktober – zwei Tage. Ein Urteil über die Rangfolge, das auf Dauer hält, ist das noch nicht. Wer heute eine Entscheidung treffen muss, sollte den Coding-Teil ernst nehmen, den Gesamtindex aber nicht als Endstand lesen.

## Quellen

- Mistral, Ankündigung zur Veröffentlichung der Gewichte: [mistral.ai/news/mistral-large-4-oss](https://mistral.ai/news/mistral-large-4-oss/)
- Modellkarte und Lizenz: [huggingface.co/mistralai/Mistral-Large-4-1T-A52B](https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B)
- Lizenztext: [LICENSE](https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B/blob/main/LICENSE)
- Unabhängige Messwerte: [Artificial Analysis, Modell-Tabelle](https://artificialanalysis.ai/leaderboards/models)
- Einordnung, Vergleichszahlen und Hardware-Anforderungen: [The Decoder, 29.10.2026](https://the-decoder.com/paris-based-mistral-releases-le-chonk-a-strong-coding-model-that-still-trails-china-overall/)
