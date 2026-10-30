---
title: "EVENET: Ein Grundmodell für Teilchenkollisionen – und es ist offen"
slug: "evenet-ein-grundmodell-fuer-teilchenkollisionen-und-es-ist-offen"
date: 2026-10-29
status: published
tags: [news, forschung, open-weights, physik]
summary: "EVENET ist ein Grundmodell für LHC-Daten: einmal auf 500 Millionen simulierten Kollisionen vortrainiert, danach für einzelne Analysen nachtrainiert. In vier Tests schlägt es Spezialsoftware, bei knappen Daten deutlich. Code und Gewichte sind offen, der Preis sind rund 100.000 GPU-Stunden Vortraining."
source_url: "https://www.nature.com/articles/s42256-026-01322-9"
source_name: "Nature Machine Intelligence"
lang: de
---

## TL;DR

- **EVENET** ist ein {{Foundation Model}} für Teilchenkollisionen: einmal auf 500 Millionen simulierten Ereignissen am Large Hadron Collider (LHC) vortrainiert, danach für einzelne Analysen nachtrainiert.
- Die Arbeit erschien am 29. Oktober 2026 in *Nature Machine Intelligence*, frei zugänglich. Code und trainierte Gewichte sind offen, unter MIT-Lizenz.
- In vier Testaufgaben schlägt das Modell Spezialsoftware. Bei der Suche nach exotischen {{Higgs-Boson}}-Zerfällen erreicht es einen SIC von 4,1 – ohne Vortraining sind es 1,6, der bisherige Spitzenwert liegt bei 1,4.
- Mit 5 Prozent der Trainingsdaten übertrifft es die Vergleichsmodelle, die mit der vollen Datenmenge trainiert wurden.
- In echten CMS-Daten findet es das ϒ-Meson wieder (7,6 σ statt 6,4 σ in der Referenzarbeit) und misst die {{Quantenverschränkung}} von Top-Quark-Paaren auf 3,33 Prozent genau (Referenz: 5,26 Prozent).
- Der Haken: 512 A100-Grafikchips und rund 100.000 GPU-Stunden fürs Vortraining. Und das Modell rechnet Detektor- und Theorieunsicherheiten noch nicht mit.

## Was passiert ist

Am 29. Oktober 2026 hat *Nature Machine Intelligence* eine Arbeit veröffentlicht, die im Maschinenlernen für die Teilchenphysik einen ähnlichen Schnitt verspricht wie Bert oder GPT für die Sprachverarbeitung. Das Team um Ting-Hsiang Hsu (National Taiwan University), Benjamin Nachman (SLAC) und Vinicius Mikuni (Nagoya) stellt darin **EVENET** vor, ein {{Foundation Model}} für Kollisionsdaten. Der Name steht für ein Modell, das nicht ein einzelnes Teilchen oder einen einzelnen Analysegriff lernt, sondern das ganze Ereignis – auf Englisch *event*, also eine Kollision mit allem, was der Detektor davon sieht.

Das Modell ist kein Prototyp auf dem Papier: Der Code liegt auf GitHub, die trainierten Gewichte auf Hugging Face, die Trainingsdaten ebenfalls, alles unter MIT-Lizenz und ohne Zugriffsbeschränkung. Der {{Preprint}} war seit Januar 2026 online; die Veröffentlichung in einer Fachzeitschrift heißt, dass unabhängige Gutachter drübergegangen sind.

Warum das eine Meldung wert ist: Am CERN laufen am LHC pro Jahr Milliarden von Protonenkollisionen durch die Detektoren. Jede davon ist eine Liste von Objekten – {{Jet}}s, Elektronen, Myonen, ihre Energien, Richtungen, Flugbahnen. Aus diesen Listen das Physikalische herauszuholen, ist der eigentliche Engpass.

## Das Problem, das es löst

Bisher läuft jede Analyse gleich ab: Frage stellen, passende Simulation erzeugen, eigenes neuronales Netz von Null trainieren, prüfen, verwerfen, neu bauen. Für eine einzige Suche nach neuen Teilchen können hunderte Hypothesen nötig sein, jede mit eigenem Training. Das kostet Rechenzeit, Expertenzeit und Monate.

Ab etwa 2030 soll der aufgerüstete HL-LHC rund zehnmal so viele Kollisionen liefern. Der CERN hat seit Beginn des LHC etwa ein Exabyte Messdaten gespeichert, eine Million Terabyte. Mit dem Ausbau wächst der Berg weiter. Ein Verfahren, das pro Analyse bei null anfängt, wird da zum Flaschenhals.

Die Idee von EVENET ist die bekannte Grundmodell-Logik: einmal teuer vortrainieren, danach billig anpassen. Man lädt einen fertigen Zwischenstand und trainiert nur noch die Aufgabe nach, die man gerade braucht. {{Fine-Tuning}} statt Neubau.

## Wie das Modell gebaut ist

EVENET nimmt ein Ereignis so, wie es aus der Rekonstruktion kommt: als ungeordnete Wolke aus Objekten mit ihren Eigenschaften. Diese Punktwolke geht in einen {{Encoder}} aus {{Transformer}}-Schichten, der zusätzlich nächste Nachbarn berücksichtigt – so bekommt das Modell sowohl die globale Struktur des Ereignisses als auch lokale Näheverhältnisse mit. Auf diesen gemeinsamen Rumpf setzt das Team fünf austauschbare Köpfe:

- **Klassifikation**: Welcher physikalische Prozess liegt vor?
- **Zuordnung**: Welches Objekt stammt von welchem Mutterteilchen?
- **Segmentierung**: Welche Objekte gehören zusammen, also zu welchem Zerfall?
- **Selbstüberwachte Erzeugung**: fehlende Objekte im Ereignis ergänzen, mit {{Diffusion}}.
- **Überwachte Erzeugung**: unsichtbare Teilchen rekonstruieren, vor allem {{Neutrino}}s.

Der Rumpf hat 18,8 Millionen {{Parameter}}, die Köpfe kommen je nach Aufgabe auf bis zu 8,7 Millionen dazu. Ein Bruchteil dessen, was Sprachmodelle mitbringen.

Vortrainiert wurde in zwei Stufen. Zuerst nur selbstüberwacht: Das Modell musste zufällig maskierte Objekte wiederherstellen, die Maskenquote stieg dabei von 30 auf 100 Prozent. Danach gemeinsam mit Prozessklassifikation und Neutrino-Rekonstruktion. Als Trainingsmaterial dienten rund 3 Milliarden simulierte Ereignisse, von denen nach Vorfilterung etwa 500 Millionen übrig blieben – zehn Prozessklassen von QCD über Top-Quark-Paare bis Higgs-Zerfälle. Aus 4 Terabyte Simulation wurden 180 Gigabyte Trainingsdaten.

Gerechnet wurde auf dem Perlmutter-Supercomputer am NERSC in den USA: 512 Nvidia A100 und 16.384 CPU-Kerne, insgesamt in der Größenordnung von 100.000 GPU-Stunden für beide Vortrainingsstufen. Nachtrainieren kostet dagegen nur wenige bis einige zehn GPU-Stunden pro Aufgabe – das ist der ganze Punkt.

## Was es leistet

Vier Testaufgaben, alle mit Vergleich zu Spezialsoftware:

**Suche nach schweren Resonanzen.** Über ein Raster von 121 Massenpunkten, mit nur 1.000 bis 10.000 Signalereignissen pro Punkt, liegt das vortrainierte Modell im Schnitt 50 Prozent über dem gleichen Modell ohne Vortraining, 20 Prozent über XGBoost und 10 Prozent über TabPFN, einem tabellarischen Grundmodell. Es erreicht sein Optimum außerdem nach rund 1.000 Optimierungsschritten statt nach 3.000.

**Wiederfinden eines bekannten Teilchens in echten Daten.** In offenen CMS-Daten von 2016 sucht EVENET nach dem ϒ-Meson in Myon-Paaren und kommt auf eine lokale {{Signifikanz}} von 7,6 σ; die veröffentlichte Referenzanalyse lag bei 6,4 σ. Ohne Vortraining bleibt es bei 1,5 σ. Auch die Nachkorrektur, die man braucht, damit die künstlich erzeugten Ereignisse physikalisch stimmen, ist viel kleiner: 11,6 Prozent Verschiebung statt 74,4 Prozent.

**Exotischer Higgs-Zerfall.** Hier ist der Abstand am größten, weil dieser Zerfall im Vortraining gar nicht vorkam:

{{chart:evenet-higgs-sic}}

Der SIC ist die Signalausbeute geteilt durch die Wurzel der Untergrundausbeute, höher ist besser. Mit nur 5 Prozent der Trainingsdaten kommt EVENET auf 1,7 und schlägt damit die Vergleichsmodelle, die mit der vollen Datenmenge trainiert wurden. Auch die Zuordnung von Jets zu ihren Mutterteilchen wird deutlich besser, von 58 auf 77 Prozent Trefferquote.

**Quantenverschränkung von Top-Quarks.** Bei dieser Präzisionsmessung sind genug Daten da; der Engpass ist die Rekonstruktion. Das Modell kombiniert zwei seiner Köpfe, um Leptonen richtig zu paaren und die fehlenden Neutrinos zu schätzen, und kommt mit 1,5 Prozent der Referenzdaten auf eine Messgenauigkeit von 3,88 Prozent – ohne Vortraining sind es 5,58 Prozent, mit reinem Selbsttraining 6,20 Prozent. Bei voller Datenmenge sättigt es bei 3,33 Prozent, rund 37 Prozent besser als die 5,26 Prozent der Vergleichsarbeit. Unter variierter Jet-Energieskala bleibt das Ergebnis stabil.

## Warum das zählt

Zwei Dinge sind an dieser Arbeit wichtiger als die Zahlen.

Erstens: Das Modell ist offen. Wer am LHC eine Analyse plant, kann den Rumpf herunterladen und aufsetzen, statt bei null zu beginnen. Genau diese Wiederverwendung ist der Punkt, an dem sich Foundation Models bezahlt machen – nicht das einzelne Ergebnis, sondern der eingesparte Neubau.

Zweitens: Es gibt seit Mitte Oktober eine sehr ähnliche Ankündigung. CERN und Mistral haben am 15. Oktober 2026 eine Absichtserklärung unterschrieben und wollen ein „Large Physics Model" namens Flare bauen, das CERN in seiner Mitteilung „das erste Grundmodell für Kolliderphysik" nennt. Einen Zeitplan, ein Budget oder eine Rechengröße nannten beide nicht. EVENET ist zwei Wochen später genau das, was dieser Ankündigung noch fehlt: ein veröffentlichtes, herunterladbares Modell mit geprüften Ergebnissen. Die beiden Projekte schließen sich nicht aus – das CERN hat einen Exabyte Daten und eine eigene KI-Strategie, die solche Modelle ausdrücklich vorsieht.

## Was es nicht kann

Nüchtern bleiben, auch weil die Autoren selbst nüchtern bleiben.

- **Es ersetzt nicht die Rekonstruktion.** EVENET arbeitet auf bereits rekonstruierten Objekten, nicht auf rohen Detektorsignalen. Die Kette vom Treffer im Siliziumdetektor bis zum fertigen Jet bleibt vor dem Modell.
- **Es rechnet Unsicherheiten nicht mit.** Detektor- und Theoriefehler müssen weiterhin von Hand fortgepflanzt werden. Für eine Publikation in der Physik ist das keine Kleinigkeit.
- **Die Köpfe sind nicht aufeinander abgestimmt.** Klassifikation, Zuordnung und Erzeugung können sich widersprechen; nichts im Training erzwingt Konsistenz.
- **Die Daten stammen aus einer schnellen Simulation.** Vortrainiert wurde mit Delphes, einem vereinfachten Detektormodell, ohne überlagerte Kollisionen. Ein harter Stresstest mit absichtlich falscher Simulation fehlt noch.
- **Es sind Ergebnisse der Autoren.** Unabhängige Nachbauten gibt es noch nicht.

Ein Punkt für die Einordnung: Das Vortrainingsmaterial ist Simulation, nicht Messung. Die Physik, die das Modell lernt, ist damit am Ende so gut wie die Simulationen, mit denen das CERN arbeitet.

## Was heißt das praktisch

Für die Teilchenphysik: Wer eine Suche plant, lädt einen Zwischenstand und trainiert wenige Stunden statt Wochen. Gerade dort, wo nur tausend Signalereignisse pro Massenpunkt verfügbar sind, bringt das Vortraining am meisten – das ist genau die Lage bei exotischen Suchen.

Für alle anderen ist es ein sauberes Beispiel dafür, wie weit man mit wenig Modell und viel Fachdaten kommt. 19 Millionen Parameter, 500 Millionen Beispiele aus einem einzigen Fachgebiet, und ein Ergebnis, das spezialisierte Werkzeuge schlägt. Nicht mehr Rechenleistung hat hier gewonnen, sondern die Entscheidung, das Vorwissen der Physik beim Training mitzugeben – die Simulation liefert Wahrheitslabels, und die wurden genutzt.

## Quellen

- Hsu, T.-H. et al.: *Foundation model for particle collision data analysis*, Nature Machine Intelligence, 29. Oktober 2026 – [nature.com/articles/s42256-026-01322-9](https://www.nature.com/articles/s42256-026-01322-9) (offen zugänglich)
- Preprint: [arXiv:2601.17126](https://arxiv.org/abs/2601.17126)
- Code: [github.com/EveNet-HEP/EveNet-Full](https://github.com/EveNet-HEP/EveNet-Full) · Gewichte: [huggingface.co/Avencast/EveNet](https://huggingface.co/Avencast/EveNet)
- CERN: *CERN and Mistral join forces to accelerate AI for science*, 15. Oktober 2026 – [home.cern](https://home.cern/cern-and-mistral-join-forces-to-accelerate-ai-for-science/)
- Reuters: *CERN and Mistral partner to build Flare, a new AI model for physics*, 15. Oktober 2026 – [channelnewsasia.com](https://www.channelnewsasia.com/business/cern-and-mistral-partner-build-flare-new-ai-model-physics-6462341)
- CMS Open Data (DoubleMuon 2016): [CERN Open Data Portal](https://opendata.cern.ch/)
