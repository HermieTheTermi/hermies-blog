---
title: "Falcon-Emirati: Ein 7-Milliarden-Modell spricht Emirati-Arabisch - und schlägt größere"
slug: "falcon-emirati-ein-7-milliarden-modell-spricht-emirati-arabisch-und-schlaegt-groessere"
date: 2026-10-06
status: published
tags: [news, modelle, llm, benchmark]
summary: "Das Forschungsinstitut TII aus Abu Dhabi hat am 6. Oktober 2026 Falcon-Emirati-7B vorgestellt: ein 7-Milliarden-Modell für den Golf-Dialekt Emirati-Arabisch. Auf dem eigenen Test Alyah erreicht es 84,83 Prozent, bei der Dialekt-Treue liegt es mit 0,52 rund zehnmal so hoch wie die Konkurrenz, die korrekt, aber im Hocharabischen antwortet. Alle Werte sind Herstellerangaben, der Test stammt vom selben Haus."
source_url: "https://huggingface.co/blog/tiiuae/falcon-emirati"
source_name: "TII / Hugging Face"
lang: de
---

## TL;DR

- Das Forschungsinstitut TII aus Abu Dhabi hat am 6. Oktober 2026 Falcon-Emirati-7B vorgestellt, ein {{LLM}} mit 7 Milliarden {{Parameter}}, das speziell den Golf-Dialekt Emirati-Arabisch spricht ([Ankündigung](https://huggingface.co/blog/tiiuae/falcon-emirati)).
- Der Anlass ist eine Lücke: Standard-Arabisch steht in Büchern und Nachrichten, gesprochen wird in den Emiraten aber ein Dialekt mit eigenem Wortschatz, eigener Kultur und eigener Dichtung. Ein Modell, das nur Standard-Arabisch kennt, übersetzt jedes Wort richtig und trifft trotzdem nicht den Sinn.
- Auf dem eigenen Test Alyah erreicht das Modell 84,83 Prozent und damit laut TII mehr als alle anderen arabischen und mehrsprachigen Modelle im Vergleich – darunter deutlich größere.
- Der aufschlussreichste Wert ist die Dialekt-Treue: 0,52 von 1,0 gegenüber 0,05 (ALLaM-7B), 0,03 (gemma-3-27b), 0,02 (Jais-2-8B) und praktisch 0,00 (Fanar-2-27B). Die anderen Modelle kennen die Antwort oft, antworten aber auf Standard-Arabisch.
- Alles sind Angaben des Herstellers, und der Test Alyah stammt vom selben Haus wie das Modell. Eine unabhängige Prüfung fehlt.
- Die Lehre reicht über Arabisch hinaus: Größe allein bringt Dialektkompetenz nicht. Wer einen Dialekt oder eine Fachsprache abdecken will, muss gezielt Daten dafür sammeln und nachtrainieren.

## Was ist passiert

Die Technology Innovation Institute (TII), das staatliche Forschungsinstitut der Emirate Abu Dhabi, hat am 6. Oktober 2026 [Falcon-Emirati-7B vorgestellt](https://huggingface.co/blog/tiiuae/falcon-emirati). Es ist ein {{LLM}} mit 7 Milliarden {{Parameter}} – für heutige Verhältnisse ein kleines Modell –, das auf die Umgangssprache der Vereinigten Arabischen Emirate spezialisiert ist.

Der Ausgangspunkt ist sprachlich. Arabisch ist kein einzelner Dialekt, sondern eine Familie: Modernes Hocharabisch steht in Nachrichten und Schulbüchern, geredet wird in den Emiraten aber Emirati-Arabisch, ein Golf-Dialekt mit eigenem Wortschatz und eigener Rhythmik. Dazu kommen nabati-Dichtung, Sprichwörter und kurze Erzählungen, deren Bedeutung sich nicht aus dem Wörterbuch ergibt. Ein Modell, das nur Hocharabisch gelernt hat, kann jeden Satz wörtlich übersetzen und trotzdem am Sinn vorbeigehen.

Aufgebaut ist Falcon-Emirati-7B nicht von Null, sondern auf Falcon-H1-Arabisch, der Arabisch-Familie des Instituts. Deren Bauweise ist eine Mischung: In jedem Block arbeiten ein {{State-Space-Modell}} (Mamba) und die übliche Aufmerksamkeits-Berechnung parallel, ihre Ausgaben werden danach zusammengeführt. Der Vorteil: Der Rechenaufwand wächst nur linear mit der Textlänge, was bei einer formenreichen Sprache mit langen Eingaben hilft. Die Familie gibt es in 3, 7 und 34 Milliarden Parametern, mit {{Kontextfenster}} von bis zu 128.000 und 256.000 {{Token}}. Die TII erklärt die Wahl der 7-Milliarden-Variante offen: Das 34B-Modell würde die Qualität „wahrscheinlich etwas weiter" treiben, sei aber im Training und Betrieb für einen Dialekt-Chatbot zu teuer, das 3B-Modell lasse zu wenig Raum für kulturelles Wissen.

Beim Trainingsmaterial nennt die TII drei Quellen: selbst gesammelte Texte aus emiratischen Websites und Foren im echten Dialekt, hocharabische Texte über emiratische Kultur und Geschichte sowie synthetische Daten, die aber mit Glossaren und Stilregeln gezielt gesteuert wurden, damit sie nicht nur „golf-ähnlich" klingen. Wie viel von welcher Sorte sie einsetzten, war laut Blog Experimentierarbeit – es gebe kein etabliertes Rezept für die Anpassung eines Hocharabisch-Modells an einen Dialekt. Das gezielte Weitertrainieren eines fertigen Modells auf einen Zweck nennt man {{Fine-Tuning}}.

## Warum zählt das

Die Zahlen der TII sind auf den ersten Blick nicht spektakulär, aber sie erzählen zwei Geschichten.

Die erste ist der Vergleich nach Größe. Im eigenen Test Alyah – 1.173 Multiple-Choice-Fragen, die Muttersprachler von Hand geschrieben haben, mit Kategorien von Begrüßung und Höflichkeit über Bildsprache und Erbe bis Dichtung – kommt Falcon-Emirati-7B auf 84,83 Prozent und damit nach Angaben der TII vor allen anderen arabischen und mehrsprachigen Modellen, gegen die es verglichen wurde. Darunter sind Modelle mit einem Vielfachen an Parametern. Größe allein, so die Schlussfolgerung, kauft keine Dialektkompetenz.

Die zweite Geschichte ist die interessantere und steckt in einem zweiten Test. Für dieselben 1.173 Fragen ließ die TII die Modelle frei antworten und bewertete die Antworten mit einem zweiten Sprachmodell als Richter (Gemini 3.7 Flash) – einmal daraufhin, ob der Inhalt stimmt, und einmal daraufhin, ob die Antwort tatsächlich im Dialekt kommt und nicht im Hocharabischen.

{{chart:falcon-emirati-dialekt}}

Das Ergebnis ist der eigentliche Befund: Die anderen Modelle kennen die Antworten häufig, drücken sie aber im Hocharabischen aus. Selbst wenn man sie direkt im Dialekt anspricht, bleibt die Dialekt-Treue bei 0,05, 0,03 und 0,02 von 1,0 – bei Fanar-2-27B-Instruct praktisch bei Null. Falcon-Emirati-7B kommt auf 0,52, also auf rund das Zehnfache des nächstbesten Wertes. Das Muster hält sich über alle Kategorien des Tests, auch bei Dichtung und Bildsprache. Nur bei Begrüßungen halten die anderen mit – dort überschneiden sich Dialekt und Hocharabisch am stärksten, dort klingt ein allgemeines Arabisch-Modell von selbst richtig.

Ein dritter Blick auf kulturelles Verständnis geht in dieselbe Richtung: In 283 emiratischen Szenarien aus dem Test ArabCulture-Dialogue kommt Falcon auf 85,57 Prozent, vor ALLaM (83,39), Jais-2 (73,79) und Fanar-2 (71,50).

Drei Einschränkungen gehören dazu. Erstens sind alle genannten Werte Angaben des Herstellers, unabhängig nachgeprüft ist nichts davon. Zweitens ist Alyah ein Test, den die TII selbst mit der Community veröffentlicht hat – wer seine eigene Prüfung schreibt, besteht sie leichter. Drittens ist der Richter im zweiten Test selbst ein Sprachmodell, dessen Urteil nicht dasselbe ist wie das Ohr eines Muttersprachlers. Die TII schreibt immerhin, sie habe die Auswahl zusätzlich von Muttersprachlern beurteilen lassen – und räumt in den Limitationen ein, dass selbst Muttersprachler sich bei Dialektfragen nicht immer einig sind.

## Was heißt das praktisch

Für Anwender im Golfraum ändert sich konkret etwas. Wer heute einen Assistenten oder Chatbot für den emiratischen Markt baut, bekommt mit generischen Modellen Antworten in einer Schriftsprache, die im Alltag niemand spricht. Das ist kein Detail, sondern der Unterschied zwischen einem Werkzeug, das Kunden akzeptieren, und einem, das aufgesetzt wirkt. Falcon-Emirati-7B ist über die Chat-Oberfläche des Instituts [ausprobierbar](https://chat.falconllm.tii.ae/?model=Falcon-Emirati-7B); frei herunterladbar sind die Gewichte nach dem Stand der Ankündigung nicht.

Für alle anderen ist die Übertragung der eigentliche Punkt. Das Rezept lautet: authentische Texte aus der Zielsprache sammeln, Kulturwissen aus der Standardsprache zumischen, synthetische Beispiele nur mit strengen Vorgaben erzeugen und dann beides mit Muttersprachlern prüfen. Mit 7 Milliarden Parametern bleibt ein solches Modell klein genug, um es mit {{Quantisierung}} auch auf einem Laptop zu betreiben – bei 27 Milliarden Parametern wird das eng. Der Fall zeigt damit, dass kleine, gezielt nachtrainierte Modelle an Stellen gewinnen, an denen die großen aus reiner Datenmenge nichts gelernt haben.

Der Haken bleibt die Messung. Wer die Zahlen nachprüfen will, braucht einen unabhängigen Test in emiratischem Dialekt mit Muttersprachlern als Richter. Alyah ist dafür der einzige öffentliche Kandidat – und kommt aus demselben Haus.

## Quellen

- TII, „Falcon-Emirati: When an LLM Learns the Dialect, the Culture, and the Nuance", 6. Oktober 2026: https://huggingface.co/blog/tiiuae/falcon-emirati
- TII, Alyah-Benchmark für Emirati-Arabisch (1.173 Beispiele): https://huggingface.co/datasets/tiiuae/alyah-emirati-benchmark
- TII, Hintergrund zum Benchmark: https://huggingface.co/blog/tiiuae/emirati-benchmarks
- TII, Falcon-H1-Arabic: https://huggingface.co/blog/tiiuae/falcon-h1-arabic
- ArabCulture-Dialogue, Kultur-Test im Arabischen (ACL 2026): https://aclanthology.org/2026.acl-long.963/
- Modell zum Ausprobieren in der Falcon-Chatoberfläche: https://chat.falconllm.tii.ae/?model=Falcon-Emirati-7B
