---
title: "EmbeddingGemma 2: Ein 740-Millionen-Modell bringt Text, Bild, Ton und Video in eine Zahlenreihe"
slug: "embeddinggemma-2-ein-740-millionen-modell-bringt-text-bild-ton-und-video-in-eine-zahlenreihe"
date: 2026-10-06
status: published
tags: [news, google, modelle, open-weights, multimodal]
summary: "Google hat am 6. Oktober 2026 EmbeddingGemma 2 veröffentlicht: ein offenes Suchmodell mit 740 Millionen Parametern, das Text, Bilder, Ton und Video in denselben Zahlenraum legt. Die Gewichte stehen unter Apache 2.0, der Text-Teil braucht rund 191 MB Arbeitsspeicher. Der größte Fortschritt liegt bei der Codesuche, beim allgemeinen Text-Test ist der Unterschied zum Vorgänger praktisch null; alle Werte sind Herstellerangaben."
source_url: "https://huggingface.co/google/embeddinggemma-2"
source_name: "Google"
lang: de
---

## TL;DR

- Google hat am 6. Oktober 2026 **EmbeddingGemma 2** veröffentlicht: ein offenes Suchmodell mit **740 Millionen {{Parameter}}**, das Text, Bilder, Ton und Video in dieselbe Zahlenreihe übersetzt.
- Die Lizenz ist **Apache 2.0**, die Gewichte liegen auf Hugging Face und Kaggle – das Modell darf jeder selbst betreiben und verändern.
- Gebaut ist es für den {{On-Device}}-Betrieb: Der Text-Teil belegt laut Google rund **191 MB** Arbeitsspeicher, mit Bild- und Ton-Teil rund **567 MB** auf einem Pixel 11 Pro.
- Der größte Sprung liegt bei Programmcode: **78,68 statt 68,76 Punkte** im Test MTEB Code. Beim allgemeinen mehrsprachigen Text-Test ist der Unterschied mit 61,36 zu 61,15 praktisch null.
- Neu ist das Kürzen: Ein Vektor lässt sich von 768 auf 256 Dimensionen schrumpfen – ein Drittel des Speichers bei fast gleicher Qualität. Bei 128 Dimensionen sinkt die Qualität deutlicher.
- Alle Werte sind Herstellerangaben aus der eigenen Testreihe. Eine unabhängige Nachprüfung fehlt.

## Was passiert ist

Ein {{Embedding}} ist eine Zahlenliste, die die Bedeutung eines Inhalts als Punkt in einem großen Raum beschreibt. Texte mit ähnlichem Sinn landen nah beieinander – deshalb findet eine Suchmaschine damit Dokumente, ohne dass irgendwo das gesuchte Wort stehen muss. Genau diese Zwischenschicht hängen sich Programme ein, die mit eigenen Dokumenten arbeiten: Suche, Empfehlungen oder {{RAG}}, bei dem ein Sprachmodell vor dem Antworten die passenden Textstellen nachgeschlagen bekommt.

Google hat dafür am 6. Oktober 2026 ein neues Modell veröffentlicht ([Ankündigung](https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2/), [Modellkarte](https://huggingface.co/google/embeddinggemma-2)): EmbeddingGemma 2, Lizenz Apache 2.0. Das Modell ist damit {{Multimodal}}: Text, Bilder, Video und Ton landen in einem gemeinsamen Zahlenraum von 768 Dimensionen. Die Suche nach einer Textzeile kann damit einen Videoausschnitt finden, und die Suche nach einer kurzen Frage eine Tonspur – ohne dass für jede Eingabeart ein eigenes Modell nötig wäre.

Wichtig für ein solches Modell ist die Größe. 740 Millionen Parameter sind für heutige Verhältnisse klein, und Google hat sie aufgeteilt: 130 Millionen stecken im Grundgerüst, 140 Millionen in der Ausgabeschicht für Text, 170 Millionen im {{Encoder}} für Bilder und 300 Millionen im Encoder für Ton. Die beiden Zusatz-Teile lassen sich einzeln dazuladen. Wer nur Text sucht, betreibt nach Google-Angaben rund 191 MB Arbeitsspeicher; mit allen Teilen sind es auf einem Pixel 11 Pro rund 567 MB, jeweils mit {{Quantisierung}}. Das {{Kontextfenster}} liegt bei 8.192 {{Token}} – viermal so groß wie beim Vorgänger, genug für bis zu 5,5 Minuten Ton, 29 Bilder oder 58 Videobilder am Stück.

## Was die Zahlen zeigen

EmbeddingGemma 2 tritt die Nachfolge von EmbeddingGemma an, das Google zufolge auf über 20 Millionen Downloads kam. Beim allgemeinen mehrsprachigen Text-Test MTEB steht das neue Modell bei 61,36 Punkten, der Vorgänger bei 61,15 – der Unterschied ist praktisch null. Der Fortschritt steckt woanders.

{{chart:eg2-code}}

Beim Suchen in Programmcode sind es 9,92 Punkte mehr, und das ist der Wert, der für Entwicklerwerkzeuge zählt: ein Verzeichnis mit Quellcode lokal durchsuchbar zu machen, ohne jedes Mal eine Anfrage an einen fremden Server zu schicken. Bei den multimodalen Tests, für die es keinen Vorgängerwert gibt, nennt Google 64,64 Punkte im Bild-Test MIEB lite, 57,28 im Bild-Test MMEB v2, 67,84 bei gescannten Dokumenten, 50,67 bei Video sowie 69,54 und 49,39 in zwei Tontests. Für sich genommen sagen diese Zahlen wenig – ohne Vergleichsmodelle im gleichen Test bleiben es Selbstauskünfte.

Die interessantere Neuerung ist das Kürzen. Ein Vektor aus 768 Zahlen kostet Speicher, und bei Millionen von Dokumenten wird die Datenbank schnell groß. EmbeddingGemma 2 ist so trainiert, dass sich der Vektor nachträglich abschneiden lässt – auf 512, 256 oder 128 Dimensionen.

{{chart:eg2-kuerzen}}

Bis 256 Dimensionen kostet das laut Modellkarte fast nichts: 60,41 statt 61,36 Punkte bei einem Drittel des Speichers. Bei 128 Dimensionen wird der Verlust deutlich, und beim Bild-Video-Test bricht der Wert von 59,01 auf 45,65 ein – dort rät Google selbst, die kurze Fassung nur für Text zu verwenden.

{{chart:eg2-bausteine}}

## Warum das zählt

Bei Sprachanfragen an große Modelle ist lokal gegen zentral längst entschieden: Die guten Modelle laufen auf Servern. Bei der Suche ist das anders. Ein Suchindex über eigene Dateien verrät mehr über eine Person oder eine Firma als fast alles andere, und genau dafür ist eine Zwischenschicht gedacht, die auf dem Gerät bleibt. Das ist der eigentliche Punkt hinter den 191 MB: nicht Rechenzeit, sondern dass die Daten das Gerät nicht verlassen.

Der zweite Punkt sind die {{Offene Gewichte}}: Apache 2.0 erlaubt auch kommerzielle Nutzung und Veränderung – ein Modell, das man herunterladen, selbst feinjustieren und in ein eigenes Produkt einbauen darf. Google liefert dafür gleich die Anbindungen mit: Der Eintrag liegt bei Hugging Face und Kaggle, es gibt Wege über die üblichen Bibliotheken und Werkzeuge ([Modellkarte](https://huggingface.co/google/embeddinggemma-2)), und die kurze Fassung lässt sich auch im Browser betreiben.

Und schließlich zeigt der Fall, wie sich der Wettbewerb verschiebt. Google baut EmbeddingGemma 2 nach eigener Angabe mit derselben Technik wie seine Gemini-Einbettungsmodelle, gibt die kleine Ausgabe aber frei. Wer keine Daten an einen Anbieter geben will, bekommt damit eine Fassung, die auf einem Handy läuft. Genau diesen Weg sind zuletzt auch Mistral mit Large 4 und Aleph Alpha mit Kolibri gegangen.

## Was heißt das praktisch

Wer eine eigene Suche über Dokumente, Bilder, Tonaufnahmen oder Code baut, hat jetzt eine Option, die ohne Netz und ohne laufende Kosten arbeitet. Der Einstieg ist unspektakulär: Modell laden, Texte und Medien durchrechnen lassen, die Zahlenreihen in einer Vektordatenbank ablegen, Anfragen auf dieselbe Weise durchrechnen und die nächsten Nachbarn ausgeben. Für Text allein genügt der kleine Teil des Modells; Bild und Ton werden nur dazugeladen, wenn sie gebraucht werden.

Zwei Einschränkungen gehören dazu. Erstens sind alle Genauigkeitswerte Google-Angaben, gemessen in Googles eigener Testreihe – wer das Modell für einen bestimmten Anwendungsfall braucht, muss ihn mit eigenen Daten messen. Zweitens hat das Kürzen einen Preis, der je nach Aufgabe unterschiedlich ausfällt: Für Textsuche auf einem Handy sind 256 Dimensionen ein guter Handel, für Bild- und Videosuche nicht.

Bleibt die Einordnung: EmbeddingGemma 2 ist ein Zwischenstück, kein Sprachmodell. Es antwortet nicht und schreibt nicht, es ordnet nur ein. Für Anwendungen, in denen genau das gebraucht wird, ist das die schnellere und günstigere Wahl – und eine, bei der die Daten auf dem Gerät bleiben.

## Quellen

- [Google: EmbeddingGemma 2 — Ankündigung](https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2/) (6. Oktober 2026)
- [Modellkarte EmbeddingGemma 2](https://huggingface.co/google/embeddinggemma-2) – Parameteraufteilung, Benchmark-Tabellen, Werte zum Kürzen der Vektoren
- [Google DeepMind: EmbeddingGemma 2, an open, lightweight multimodal embedding model](https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model/) (6. Oktober 2026)
- [Google AI Edge: EmbeddingGemma 2 für LiteRT](https://developers.googleblog.com/google-ai-edge-with-embeddinggemma-2) – Betrieb auf Geräten ohne Netz
