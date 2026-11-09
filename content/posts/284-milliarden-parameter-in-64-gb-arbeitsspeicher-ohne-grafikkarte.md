---
title: "284 Milliarden Parameter in 64 GB Arbeitsspeicher, ohne Grafikkarte"
slug: "284-milliarden-parameter-in-64-gb-arbeitsspeicher-ohne-grafikkarte"
date: 2026-11-08
time: "11:22"
status: published
tags: [news, llm, modelle, open-weights, benchmark]
summary: "llama-modchip quetscht DeepSeek-V4-Flash mit 1,71 Bit pro Gewicht in 56,56 GiB, genug für einen Rechner mit 64 GB Arbeitsspeicher und ohne GPU. Auf einem Ryzen 9 9955HX kommen 43 bis 44 Token pro Sekunde Prompt und 9 bis 10 Token pro Sekunde Ausgabe heraus. Alle Zahlen sind selbst berichtet, ein unabhängiger Nachbau fehlt, und Nachbauer im Hacker-News-Thread melden Startprobleme."
source_url: "https://github.com/synchopate/llama-modchip"
source_name: "llama-modchip (GitHub)"
lang: de
---

## TL;DR

- Ein Projekt namens llama-modchip bringt DeepSeek-V4-Flash mit 284,33 Milliarden {{Parameter}}n in eine Datei von 56,56 GiB, die auf einen Rechner mit 64 GB Arbeitsspeicher und ohne Grafikkarte passt ([Repo](https://github.com/synchopate/llama-modchip)).
- Möglich macht das eine {{Quantisierung}} mit 1,71 Bit pro Gewicht plus selbst geschriebene CPU-Kernel; die Standardfassung derselben Modellfamilie belegt 76,87 GiB.
- Auf einem Ryzen 9 9955HX mit 16 Kernen läuft das Modell mit 43 bis 44 {{Token}} pro Sekunde durch den Prompt und gibt 9 bis 10 Token pro Sekunde aus, mit einem Entwurfsmodell bis 14,7.
- Alle Zahlen stammen vom Autor selbst. Ein Nachbau mit Vergleich gegen die volle Präzision fehlt.
- Im Hacker-News-Thread zum Projekt (469 Punkte, 8. November) melden Nachbauer Startfehler, andere messen ähnliche Werte wie mit unverändertem llama.cpp.

## Was ist passiert

Am 8. November stand ein Repository namens llama-modchip auf der Startseite von Hacker News, mit dem Titel: 284 Milliarden Parameter auf 64 GB Arbeitsspeicher, keine GPU. Seitdem hat es 739 Sterne gesammelt und ein Tempo vorgelegt, das auf eine eilige Woche hindeutet: mehr als 50 Commits, die letzte Änderung am 9. November um 16:57 UTC.

Der Gegenstand ist DeepSeek-V4-Flash, ein {{Mixture-of-Experts}}-Modell mit 284,33 Milliarden {{Parameter}}n, von denen pro Token 13,17 Milliarden aktiv sind. 43 Schichten, 256 geroutete Experten, pro Schicht sechs davon plus ein geteilter. Die verbreitetste kleine Fassung dieses Modells, UD-IQ1_S von Unsloth, belegt 76,87 GiB, also 82,5 GB. Auf einem Linux-Rechner mit 64 GB stehen davon rund 62,5 GiB zur Verfügung, der Rest geht an Kernel, Firmware und laufende Programme. Die Datei passt also nicht, und llama.cpp schiebt bei diesem Betrieb Seiten zwischen Speicher und Platte hin und her, was die Ausgabe auf 5,91 Token pro Sekunde drückt.

Der Autor, ein GitHub-Nutzer namens synchopate, hat zwei Dinge geändert. Erstens ein eigenes Speicherformat. Fractal-64 packt die Gewichte mit 1,71 Bit pro Wert, die gerouteten Experten liegen bei 1,5625 Bit. Einbettungen und dichte Schichten bleiben bei vier bis fünf Bit, die Aufmerksamkeitsprojektionen bei 3,75. Ergebnis: 56,56 GiB statt 76,87, gemessen im Betrieb 57,61 bis 58,9 GiB bei 256.000 {{Token}} {{Kontextfenster}}, ohne Auslagerung auf die Platte.

Zweitens gepatchte Kernel für die CPU. Statt einen Wert nach dem anderen durch die quantisierten Matrizen zu schieben, rechnet der Patch mehrere Spalten gleichzeitig und hält die Zwischenwerte in Registern, im L1-, L2- und L3-Cache. Laut README bringt das 77 Prozent mehr Durchsatz bei der Prompt-Verarbeitung und 53 Prozent bei der Ausgabe. Dazu kommt ein Wörterbuch-Modell von 1,64 MB, das wie ein Schachprogramm aus früheren Stellungen rät, welches Token als nächstes kommt. Ein Zwischenspeicher im Arbeitsspeicher stellt außerdem den Zustand einer Agentensitzung in 13 bis 33 Millisekunden wieder her.

{{vergleich:modchip-vergleich}}

## Warum zählt es

Die Zahlen sind eindrucksvoll und die Einordnung ist trotzdem wichtig, weil hier zwei verschiedene Dinge zusammenfallen: Passen und Laufen.

Was passt, ist die Datei. Der Trick mit 1,71 Bit pro Gewicht ist im Kern eine Kompressionsleistung, und sie ist an eine Eigenschaft von {{Mixture-of-Experts}}-Modellen gebunden: Die meisten Gewichte liegen in Experten, die pro Token nicht gebraucht werden. Wer die nur grob speichert und die aktiven Teile fein, verliert wenig. Genau das ist der Grund, warum ein Modell mit 284 Milliarden Parametern überhaupt in 64 GB passt, und warum dasselbe Vorgehen bei einem dichten Modell derselben Größe scheitern würde.

Was läuft, ist der Betrieb, und hier wird es nüchterner. 9 bis 10 Token pro Sekunde Ausgabe sind ein Tempo, bei dem ein Absatz eine knappe Minute braucht. Für einen Agenten zählt aber zuerst die Verarbeitung des Prompts, also der {{Prefill}}. Ein Kommentator im Hacker-News-Thread berichtet von 116 Sekunden für 43 Eingabetokens und einer einfachen Übersetzung; auf einer RTX 6000 mit GLM-5.3-Flash dauert dieselbe Anfrage dort 1,8 Sekunden. Wer eine Codebasis von 100.000 Token in den Kontext laden will, wartet bei 44 Token pro Sekunde Prompt-Verarbeitung über eine halbe Stunde, bevor das erste Antwortzeichen erscheint. Das ist der Punkt, an dem die Anwendung entschieden wird, nicht die Ausgabegeschwindigkeit.

Dazu kommt die Frage nach der Qualität, und hier ist die Beweislage dünn. Das README nennt für die Standardkonfiguration einen Cosinus von 1,00000 und eine Divergenz von 0,0000 gegenüber der unveränderten Laufzeit. Der Vergleich läuft allerdings gegen dieselbe bereits auf unter zwei Bit komprimierte Datei, nicht gegen das Modell in voller Präzision. Ob Fractal-64 die Fähigkeiten erhält, die DeepSeek-V4-Flash in der Standardfassung schon eingebüßt hat, beantwortet das nicht. Ein Nutzer, der nach eigener Angabe viel mit diesem Modell gearbeitet hat, schreibt im Thread, selbst die 97-GB-Fassung in zwei Bit weiche deutlich von der vollen Präzision ab.

::: warnung
Alle Geschwindigkeits- und Speicherwerte in diesem Artikel stammen aus dem README des Projekts und aus Berichten einzelner Nutzer. Eine unabhängige Messung mit identischem Aufbau und eine Qualitätsprüfung gegen das Ausgangsmodell liegen nicht vor. Wer die Datei herunterlädt, investiert 56 GiB Bandbreite und mehrere Stunden Einrichtung ohne Garantie, dass der Aufbau auf der eigenen Hardware startet.
:::

## Was heißt das praktisch

Wer einen Rechner mit 64 GB Arbeitsspeicher und einer aktuellen AMD- oder Intel-CPU besitzt, kann das ausprobieren. Der Weg ist im README beschrieben: Modell über die Hugging-Face-CLI laden, mitgelieferte Binärdatei starten. Die Binärdateien setzen AVX-512 voraus. Auf einem Haswell-Xeon ohne diese Befehlssätze bricht der Start mit einem Illegal-Instruction-Fehler ab, und eine Anleitung, den eigenen llama.cpp-Zweig neu zu bauen, fehlt; es gibt nur Patch-Dateien. Ein anderer Nutzer bekam beim Laden einen Formfehler auf einem Tensor gemeldet. Beides steht im Thread, nicht im README.

Wichtiger ist eine zweite Einschränkung: Die Dateien nutzen einen eigenen Tensortyp mit der Nummer 40. Unverändertes llama.cpp, Ollama und LM Studio lehnen sie ab. Man ist also auf genau diese Binärdatei angewiesen, und die stammt von einer Person, die in einer Woche mehr als 50 Commits geschrieben hat. Für ein Experiment ist das in Ordnung. Für einen Dienst, der nachts unbeaufsichtigt läuft, ist es ein Risiko, das man kennen sollte.

Und dann ist da noch die Rechnung, die im Thread fast wichtiger war als das Projekt selbst. Eine Grafikkarte für 500 Euro schlägt diesen Aufbau bei der Prompt-Verarbeitung um ein Vielfaches, weil sie Speicherbandbreite und Matrizenmultiplikation zusammenbringt, die eine CPU nicht erreicht. Wer 64 GB Arbeitsspeicher ohnehin hat und kein Geld für eine Karte ausgeben will, für den ist das Projekt ein Gewinn. Wer Rechenzeit kauft, für den bleibt die Rechnung offen: 9 Token pro Sekunde auf eigener Hardware gegen ein Abonnement, das schneller antwortet und mehr kann. Der interessantere Teil der Ankündigung ist deshalb nicht das Tempo, sondern der Speicherbedarf. Zeigt sich, dass sich das Verfahren auf andere offene Modelle übertragen lässt, rückt die Grenze dessen, was ohne Grafikkarte geht, ein Stück nach unten. Das ist der eigentliche Befund dieser Woche.

## Quellen

- llama-modchip, Repository und README v2.4.0 (Apache 2.0), Commit vom 8. November 2026: https://github.com/synchopate/llama-modchip
- Hacker News, „Llama-modchip: 284B DeepSeek on 64GB RAM, no GPU", 8. November 2026, 469 Punkte, 180 Kommentare: https://news.ycombinator.com/item?id=50411961
- Hacker News, Kommentar von aappleby zur Laufzeit auf Ryzen 7945HX: https://news.ycombinator.com/item?id=50416358
- Hacker News, Kommentar von ar-nelson zu Startfehlern auf einem Xeon: https://news.ycombinator.com/item?id=50416444
- Hacker News, Kommentar von kgeist zu 116 Sekunden für 43 Eingabetokens: https://news.ycombinator.com/item?id=50417605
- Hacker News, Kommentar von sparse-Matrix zu 12 bis 14 Token pro Sekunde auf Ryzen 7 5700U: https://news.ycombinator.com/item?id=50416583
- DEV Community, „284B on 64GB RAM: We Read the Small Print Before Downloading 56 GiB", 9. November 2026: https://dev.to/karmabox/284b-on-64gb-ram-we-read-the-small-print-before-downloading-56-gib-37ng
- Hugging Face, Modellgewichte DeepSeek-V4-Flash-0731-Fractal-64GB-CPU-GGUF: https://huggingface.co/Synchopate/DeepSeek-V4-Flash-0731-Fractal-64GB-CPU-GGUF
