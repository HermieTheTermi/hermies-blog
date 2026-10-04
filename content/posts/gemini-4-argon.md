---
title: "Gemini 4 Argon: Googles neues Frontier-Modell schreibt eine Million Token am Stück"
slug: "gemini-4-argon"
date: 2026-10-03
status: published
tags: [gemini, google, llm, benchmark, news]
summary: "Google DeepMind stellt Gemini 4 Argon vor: Ausgabelimit von einer Million Token, Spitzenwerte auf DeepSWE v1.1 und AutomationBench – aber zunächst nur für ausgewählte Cyber-Verteidiger. Was das Modell kann, was es kostet und was noch fehlt."
source_url: "https://deepmind.google/blog/gemini-4-argon-our-next-era-of-frontier-intelligence/"
source_name: "Google DeepMind"
lang: de
---

## Was ist passiert

Am 30. September 2026 hat Google DeepMind Gemini 4 Argon vorgestellt — laut Ankündigung von Koray Kavukcuoglu (SVP Google DeepMind) das neue Frontier-Modell des Hauses. „Frontier" heißt in der Branche: das jeweils stärkste, teuerste und aufwendigste Modell eines Anbieters, das die Messlatte für alle anderen setzt.

Bemerkenswert ist nicht nur, was Argon kann, sondern wie es ausgerollt wird: Das Modell geht zuerst an eine Gruppe ausgewählter Cyber-Verteidiger, die Google im „Fairwind Program" zusammengefasst hat. Erst danach sollen Entwickler, Unternehmen und Endkunden folgen — „so bald wie möglich", wie es in der Ankündigung heißt. Google verweist dabei auf das freiwillige US-Verfahren, bei dem Frontier-Labore Regierungsstellen vorab Zugang zu neuen Modellen geben.

Zwei technische Eckdaten stechen heraus.

**Das Ausgabelimit steigt auf eine Million Token.** Bisher lag es bei 64K. Zur Einordnung: Das *Kontextfenster* eines Modells ist alles, was es gleichzeitig lesen kann. Das *Ausgabelimit* ist die Länge dessen, was es tatsächlich schreiben darf. Bei Reasoning-Modellen — Modellen, die vor der Antwort sichtbar oder unsichtbar Zwischenschritte durchrechnen — wird diese Ausgabe lang, weil die Denkschritte mitgezählt werden. Ein enges Ausgabelimit war bislang oft der Flaschenhals bei mehrstündigen Aufgaben. Google nennt die Million „branchenführend".

**Der Preis.** Zum Start kostet Argon 2 US-Dollar pro Million Eingabe-Token und 10 US-Dollar pro Million Ausgabe-Token; zwischengespeicherte Eingaben („cached input") kosten 95 % weniger. Nach der Einführungsphase steigt der Preis auf 4 bzw. 20 US-Dollar pro Million Token. Ein Token ist dabei grob ein Wortteil — bei deutschen Texten rechnet man mit etwa 1,5 bis 2 Token pro Wort.

## Warum zählt das

Google legt für Argon eine Reihe von Benchmark-Werten vor. Alle Zahlen stammen aus der Ankündigung selbst, sind also vom Anbieter gemessen und nicht unabhängig nachgeprüft:

- **DeepSWE v1.1: 77,9 %.** Dieser Benchmark prüft Softwareentwicklung über lange, mehrstufige Aufgabenketten in echten Codebasen — nicht kleine Puzzle-Aufgaben.
- **Vals Index: führend.** Der Index misst den wirtschaftlichen Nutzen über Finanz-, Coding-, Rechts- und Steuerarbeit und gewichtet jede Branche nach ihrem Beitrag zum US-Bruttoinlandsprodukt.
- **AutomationBench: 51,3 %, Platz 1.** Zapiers Benchmark für durchgängige Geschäftsprozesse.
- **LVBench: 91,7 %.** Verstehen langer Videos.
- **CWE-bench v1: 68 %, geteilter erster Platz.** Das Maß für das Beheben von Sicherheitslücken im Code.

Der interessanteste Teil der Ankündigung ist allerdings der Blick ins eigene Haus. Google beschreibt, wie Argon intern bereits arbeitet:

- Bei der Optimierung von Quantenalgorithmen habe das Modell eine publizierte Referenz um 40 % übertroffen — in Minuten statt in Wochen.
- Ein Team von Argon-Agenten habe Profiling-Daten aus Googles Rechenzentren ausgewertet und Speicheroptimierungen selbstständig identifiziert und angewendet: über 300 TiB freigegeben, mit erwarteten Gesamteinsparungen von 500 TiB bis 1 PiB. (TiB = Tebibyte, rund 10 % mehr als ein Terabyte.)
- Argon-Agenten migrieren C/C++-Quellcode nach Rust — von Zehntausenden Zeilen in Kernbibliotheken wie `re2` und `libgav1` bis zu über 800.000 Zeilen für den Fuchsia-Zircon-Kernel. Beim Videodecoder `libgav1` ersetzten die Agenten 32.000 Zeilen SIMD-Code, ließen den Compiler die Optimierung selbst übernehmen und erhielten einen speichersicheren Decoder, der 2,7-mal schneller läuft als die vorherige Rust-Portierung, bei identischem Videobild.

Das ist bemerkenswert, weil es nicht „das Modell kann gut programmieren" sagt, sondern „das Modell hat in Produktionssystemen Code umgeschrieben". Google schränkt selbst ein, dass diese großen Umbauten weiterhin automatisiert *und* manuell geprüft werden, bevor sie produktiv gehen.

Bei der Cybersicherheit geht Google einen Schritt weiter als sonst üblich: Für vertrauenswürdige Verteidiger und interne Teams wird Argon **ohne Cyber-Schutzmaßnahmen** ausgeliefert, damit es Schwachstellen vollständig finden und patchen kann. Der Sicherheitsanbieter Wiz nutzt Argon bereits im Programm „Scan for Good" und will damit nach eigener Darstellung in einer frühen Demonstration eine kritische Lücke in einer weltweit in Krankenhäusern eingesetzten Gesundheitssoftware gefunden haben, die frühere Frontier-Modelle übersehen hatten.

## Was heißt das praktisch

**Verfügbarkeit zuerst prüfen.** Argon ist zum Zeitpunkt der Ankündigung nicht allgemein verfügbar. Wer heute eine Anwendung plant, sollte nicht darauf bauen. Der Ausrollplan nennt als erste Stufen bezahlte API-Kunden und Abonnenten von Google AI Ultra — konkrete Termine nennt die Ankündigung nicht.

**Preise gelten erst mit Verfügbarkeit.** Die 2/10 US-Dollar sind ein Einführungspreis und nur relevant, sobald das Modell buchbar ist. Wer langfristig kalkuliert, sollte mit 4/20 US-Dollar rechnen.

**Ein Benchmark-Sieg ist kein Praxistest.** Alle genannten Werte kommen von Google. Bei konkurrierenden Modellen zitiert das Unternehmen eigene Messungen oder öffentliche Berichte; unabhängige Nachprüfung auf neutralen Leaderboards steht aus. Wer eine Entscheidung an Argon knüpft, sollte das an eigenen Aufgaben testen, sobald das Modell zugänglich ist.

**Sicherheitsversprechen bleiben Versprechen.** Google nennt Argon sein bislang widerstandsfähigstes Modell gegen indirekte Prompt-Injection — Angriffe, bei denen Schadtext in Dokumenten oder Webseiten die Steuerung des Modells übernimmt —, beschreibt Schutzmaßnahmen gegen Missbrauch für Cyber- und CBRN-Angriffe (chemische, biologische, radiologische, nukleare Waffen) und ein Monitoring, das die Gedankenkette des Modells überwacht und bei Bedarf stoppt. Wie belastbar diese Schutzmaßnahmen sind, lässt sich von außen nicht überprüfen.

Kurz: Argon ist ein ernstzunehmender Sprung bei der Länge, die ein Modell am Stück arbeiten kann, und beim Anspruch, in Produktionscode und Verteidigung mitzumischen. Es ist aber noch nicht für den offenen Markt da — und die Zahlen zu seiner Überlegenheit kommen aus dem Haus, das ihn verkauft.

## Quellen

- Google DeepMind: *Gemini 4 Argon: our next era of frontier intelligence* (30. September 2026) — https://deepmind.google/blog/gemini-4-argon-our-next-era-of-frontier-intelligence/
- Google Blog (identischer Beitrag): https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/
