---
title: "Google stellt zwei neue TPU-Systeme vor und baut dafür keinen neuen Chip"
slug: "google-stellt-zwei-neue-tpu-systeme-vor-und-baut-dafuer-keinen-neuen-chip"
date: 2026-11-09
status: published
tags: [news, google, modelle, benchmark, energie]
summary: "Google hat am 9. November TPU 8tx und TPU 8i Max vorgestellt, das dritte und vierte System der achten Generation in einem Jahr. Beide bauen auf vorhandenen Chips: 8tx schützt Daten auch während der Verarbeitung, 8i Max packt zwei Chips in ein Package für lange Kontexte. Preise und Termine fehlen, die Leistungsangaben sind Herstellerangaben."
source_url: "https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/tpu-8i-max-and-8tx/"
source_name: "Google"
lang: de
---

## TL;DR

- Google hat am 9. November zwei weitere Systeme seiner achten {{TPU}}-Generation vorgestellt: TPU 8tx für vertrauliche Berechnung und TPU 8i Max für sehr lange Kontexte ([Ankündigung](https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/tpu-8i-max-and-8tx/)).
- Vier Systeme in einem Jahr, so viele wie nie zuvor innerhalb einer Generation. Neu sind dabei die Gehäuse, der Speicher und die Netze, nicht die Chips selbst.
- TPU 8i Max verdoppelt Rechenleistung, SRAM und HBM-Bandbreite gegenüber dem 8i und bringt doppelt so viel Silizium im gleichen Rack unter.
- TPU 8tx hält Daten und Modellgewichte auch während der Verarbeitung verschlüsselt und erreicht laut Google bis zu doppelt so niedrige Latenz wie der 8t.
- Fast 100 externe Kunden nennt Google inzwischen. Preise und Termine für die beiden neuen Systeme stehen nicht in der Ankündigung.

## Was ist passiert

Am 9. November hat Google zwei weitere Systeme seiner achten TPU-Generation angekündigt. Der TPU 8tx ist für vertrauliche Berechnung gebaut, der TPU 8i Max für sehr lange Kontexte und hohe Rechendichte. Beide ergänzen den TPU 8t fürs Training und den TPU 8i für {{Inferenz}} mit niedriger Latenz, die Google im April auf dem Cloud Next gezeigt hat. Vier Systeme in einem Jahr, das ist laut Ankündigung die bisher höchste Zahl innerhalb einer Generation.

Bemerkenswert ist, was Google nicht angekündigt hat: keinen neuen Chip. Beide Neuvorstellungen bauen auf vorhandenem Silizium. Der 8tx nutzt die Chips des 8t und kombiniert sie mit Hauptprozessoren vom Typ AMD EPYC der fünften Generation. Der 8i Max packt zwei 8i-Chips auf ein einziges Package.

Amin Vahdat, bei Google für Technologie und Infrastruktur zuständig, begründet den Weg mit dem Tempo der Software. Ein neuer Chip brauche Jahre, ein neues System um einen vorhandenen Chip herum Monate. Hinter dem Satz steckt eine Vertriebsstrategie: Google kann Varianten nachliefern, wenn Kunden danach fragen, ohne eine ganze Fertigungslinie neu aufzusetzen.

{{zahlen:tpu-zahlen}}

Die Nachfrage kommt inzwischen von außen. Fast 100 Kunden zählt Google, darunter Frontier-Labore, Handelsfirmen, Händler und Universitäten. Ein Teil von ihnen betreibt TPUs im eigenen Rechenzentrum, andere mieten sie in Google Cloud. Bis vor wenigen Jahren waren TPUs ein internes Werkzeug für Gemini und die eigenen Dienste.

## Warum zählt es

Zwei technische Entscheidungen sagen mehr über den Markt als die Zahl der Systeme.

Die erste betrifft den Speicher. Wenn Dutzende Agenten gleichzeitig eine Codebasis durchsuchen oder stundenlanges Video auswerten, wird die Bandbreite zum Arbeitsspeicher zum Engpass. Der Chip wartet auf Daten. Google antwortet mit einem Package, in dem zwei 8i-Chips sitzen: doppelte Rechenleistung, doppelter SRAM, doppelte HBM-Bandbreite, doppelt so viel Silizium im gleichen Rack. Das zielt auf die Grenze, an der Modelle mit langem {{Kontextfenster}} langsamer werden, weil jede Schicht Daten nachladen muss.

Die zweite betrifft die Vertraulichkeit. Normalerweise sind Daten auf der Platte und im Netz verschlüsselt, im Arbeitsspeicher liegen sie im Klartext, sonst kann der Prozessor nicht rechnen. Der 8tx schützt Daten und Modellgewichte auch während der Verarbeitung, in einer abgeschotteten Zone direkt in der Hardware. Für Banken, Behörden und Firmen, die ein eigenes Modell mit eigenen Daten nachtrainieren wollen, ist das der Unterschied zwischen dürfen wir nicht und dürfen wir.

{{tabelle:tpu-portfolio}}

Beide Systeme zahlen auf eine Verschiebung ein, die nicht von Google ausgeht. Der Aufwand verlagert sich vom Training auf den Betrieb. Trainingsläufe sind groß, aber selten. Der Betrieb läuft rund um die Uhr. Wer dort Kosten senkt, gewinnt Kunden, und deshalb bauen auch Amazon, Microsoft und OpenAI eigene Beschleuniger. Google tritt in diesem Wettbewerb mit der Breite an, nicht mit dem schnellsten einzelnen Chip: für jede Phase der Agentenkette ein eigenes System.

Der zweite Hebel ist die Software. Google hat im Oktober TorchTPU als Open Source veröffentlicht, damit PyTorch-Code ohne Umschreiben auf TPUs läuft, und liefert Backends für vLLM und SGLang. Dazu kommt ein Werkzeugpaket, das sich laut Ankündigung in Claude Code, Cursor und Google Antigravity einklinkt und Kernel in natürlicher Sprache abstimmt, sowie eine offene Serving-Engine für eine C++-Laufzeit. Das ist der unspektakulärere Teil der Ankündigung und wahrscheinlich der wichtigere: Ein Chip, für den niemand Code umbauen muss, wird eher gekauft.

## Was heißt das praktisch

Für Teams, die ohnehin auf Google Cloud arbeiten, ändert sich am ersten Tag wenig. Sie können den 8i Max für lange Kontexte einplanen und den 8tx für Daten, die das Haus nicht verlassen dürfen. Beides sind Systeme, keine neuen Chips, also bleibt die Werkzeugkette dieselbe. Interessant sind die Software-Änderungen: TPU Sync, jetzt offen, verschiebt {{KV-Cache}}s zwischen Chip, Host-Speicher und Netz und verspricht mehr als 90 Prozent weniger Übertragungslatenz bis zum ersten Token. Wer Agenten in langen Sitzungen betreibt, merkt das direkter als jede Chip-Spezifikation. Der Agent Compute Engine genannte Teil schaltet wartende Sitzungen ab und schiebt deren Arbeitsspeicher in Millisekunden vom Chip, damit Leerlauf nicht die volle Leistungsaufnahme kostet.

Was fehlt, sind die Zahlen, die eine Kaufentscheidung tragen. Google nennt weder Preise noch Termine für den 8tx und den 8i Max. Die Leistungsangaben, also 2,7-fache Trainingsleistung für den 8t und 80 Prozent bessere Inferenz-Preis-Leistung für den 8i, vergleichen mit der eigenen siebten Generation, nicht mit Nvidias aktuellen Beschleunigern. Die Spitzenwerte auf den Benchmarks InferenceX und AgentX stammen aus Messungen, auf die Google selbst verlinkt; ein unabhängiger Nachbau mit identischem Software-Stack liegt nicht vor. Auch zur Aufteilung des Geschäfts sagt die Ankündigung nichts: wie viel davon Miete in Google Cloud ist und wie viel Verkauf von Systemen in fremde Rechenzentren, bleibt offen.

Bemerkenswert ist zum Schluss ein Satz über den Bau der Chips selbst. Google setzt AlphaChip ein, ein Verfahren aus dem eigenen Forschungslabor, das Chip-Layouts mit bestärkendem Lernen entwirft, und Gemini für Layouts, die früher Wochen brauchten und jetzt in Stunden entstehen. Die Infrastruktur für KI wird also mit KI gebaut. Ob das die Lieferzeiten verkürzt, lässt sich an der Zahl der Systeme messen, die Google im kommenden Jahr vorstellt. Vier in einem Jahr sind die Messlatte, die das Unternehmen sich selbst gesetzt hat.

## Quellen

- Google, „Our newest TPUs: 8tx and 8i Max, built for the agentic era", 9. November 2026: https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/tpu-8i-max-and-8tx/
- Google Cloud Blog, „Introducing TPU 8tx and TPU 8i Max", 9. November 2026: https://cloud.google.com/blog/topics/ai-infrastructure/tpu-8tx-and-tpu-8i-max
- Google, „Our eighth generation TPUs: two chips for the agentic era" (TPU 8t und 8i, April 2026): https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/
- The Decoder, „Google ships four TPU variants in one year as it ramps up competition with Nvidia", 9. November 2026: https://the-decoder.com/google-ships-four-tpu-variants-in-one-year-as-it-ramps-up-competition-with-nvidia/
- SiliconANGLE, „Google advances agentic AI custom silicon expanding TPU family with 8tx and 8i Max", 9. November 2026: https://siliconangle.com/2026/11/09/google-advances-agentic-ai-custom-silicon-expanding-tpu-family-with-8tx-and-8i-max/
- Google Cloud, „TorchTPU is now open source" (Oktober 2026): https://cloud.google.com/blog/topics/ai-infrastructure/torchtpu-is-now-open-source-run-native-pytorch-on-tpus
- Google Open Source Blog, „Supercharging XLA inference" (XLA Serving Engine), November 2026: https://opensource.googleblog.com/2026/11/supercharging-xla-inference-xla-serving-engine.html
