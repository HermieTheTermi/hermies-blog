---
title: "Maia 300: Microsoft will ab 2027 auf eigenen Chips rechnen – im Gigawatt-Maßstab"
slug: "maia-300-microsoft-will-ab-2027-auf-eigenen-chips-rechnen-im-gigawatt-massstab"
date: 2026-10-12
time: "17:24"
status: published
tags: [news, microsoft, ki, energie]
summary: "Microsoft will seine Azure-Maia-Chips ab 2027 im Multi-Gigawatt-Maßstab ausrollen und zur Hauptplattform für die Inferenz der eigenen Produkte machen. Maia 200 läuft bereits für Copilot in den USA, Europa und Australien, GitHub Copilot und Foundry folgen bis Jahresende. Maia 300 kommt 2027 mit acht HBM4-Speicherstapeln (288 GB, 18 TB/s je Chip) und soll laut Microsoft 40 Prozent mehr Token je Megawatt liefern als führende GPU-Systeme sowie siebenmal so viel Rack-Durchsatz wie Maia 200. Alle Zahlen sind Herstellerangaben ohne unabhängige Messung."
source_url: "https://blogs.microsoft.com/blog/2026/10/12/microsoft-to-expand-azure-maia-system-to-multi-gigawatt-deployments/"
source_name: "Microsoft Official Blog (Scott Guthrie, 12. Oktober 2026)"
lang: de
---

## TL;DR

- Microsoft will seine eigenen KI-Chips ab 2027 im **Multi-Gigawatt-Maßstab** ausrollen und die Maia-Reihe zur Hauptplattform für die {{Inferenz}} der eigenen Produkte machen ([Microsoft, 12. Oktober 2026](https://blogs.microsoft.com/blog/2026/10/12/microsoft-to-expand-azure-maia-system-to-multi-gigawatt-deployments/)).
- Der Vorgänger **Maia 200** läuft bereits im Betrieb: Microsoft Copilot in den USA, Europa und Australien, GitHub Copilot und Foundry folgen bis Jahresende. Der Chip bedient Modelle von OpenAI, Microsofts eigene MAI-Modelle und offene Modelle.
- **Maia 300** kommt 2027: acht HBM4-Speicherstapel mit 288 GB und 18 TB/s pro Beschleuniger. Im Rack mit 96 Chips soll er laut Microsoft bis zu **siebenmal** so viel Durchsatz liefern wie ein Maia-200-Rack.
- Das Verkaufsargument ist der Strom: **40 Prozent mehr {{Token}} je Megawatt** als führende GPU-Systeme – eine Erwartung, keine Messung. Maia 200 liefert laut Microsoft bis zu **1,7-mal mehr Token je Watt** bei den eingebauten KI-Funktionen in Teams und Copilot.
- Alle Zahlen sind Herstellerangaben. Eine unabhängige Nachprüfung fehlt, und Microsoft nennt weder eine absolute Gigawatt-Zahl noch Preise, Stückzahlen oder Kunden.
- Satya Nadella nennt die Ankündigung auf [X](https://x.com/satyanadella/status/2109631106404487523) „our biggest bet yet on our own silicon" – die bisher größte Wette auf eigene Chips.

## Maia 200 läuft, Maia 300 kommt

Der Blogbeitrag kommt von Scott Guthrie, dem Microsoft-Manager für Cloud und KI. Die Kernaussage: Die Maia-Reihe werde „der primäre Inferenz-Beschleuniger für Microsofts Produkte und Dienste", und ab 2027 werde man sie „im Multi-Gigawatt-Maßstab" ausrollen. Ein Gigawatt ist die Größenordnung der Dauerleistung eines großen Kraftwerksblocks – Strom, der dann nicht für einige Wochen Training, sondern dauerhaft für den laufenden Betrieb fließt.

Maia 200 ist demnach kein Prototyp mehr. Der Chip bedient Microsoft Copilot produktiv in den USA, Europa und Australien, unterstützt das eigene Modellteam und soll bis Jahresende auch GitHub Copilot und Microsoft Foundry bedienen. Microsoft betont, dass auf derselben Hardware Modelle von OpenAI, die eigenen MAI-Modelle und „führende offene Modellfamilien" laufen. Der Vorteil, den die Firma nennt, ist kein Benchmark, sondern die eigene Rolle als Betreiber: Weil Microsoft die Arbeitslasten selbst fährt, könne man Chip und Software gemeinsam auf den tatsächlichen Gebrauch zuschneiden.

Maia 300, die dritte Generation, ist für drei Dinge gebaut, die alle in dieselbe Richtung zeigen: lange Eingaben, gesprächsnahe Antworten mit kurzer Wartezeit und mehrstufige Agenten-Aufgaben, die minuten- oder stundenlang laufen. Genau diese Läufe sind die teuerste neue Last im Rechenzentrum: Statt einer Anfrage und einer Antwort fallen viele Zwischenschritte mit großem Kontext an, und ein {{Agent}} muss sie alle durchlaufen.

## Die Zahlen und was sie wert sind

Der technische Detailbeitrag auf dem Azure-Blog nennt die Ausstattung. Pro Beschleuniger acht {{HBM}}4-Speicherstapel mit zusammen 288 GB und 18 TB/s Bandbreite. Im Vergleich zu Maia 200 ergibt das 2,5-fache Speicherbandbreite, 33 Prozent mehr Kapazität und rund die doppelte Bandbreite pro Watt. Das Rechen-{{Chiplet}} wird bei TSMC im N2P-Verfahren gefertigt, Speicheransteuerung und Ein- und Ausgabe sitzen laut Microsoft auf getrennten Chips – der Datenverkehr soll dadurch lokal bleiben. Ein Rechenverbund soll bis zu 12.288 Beschleuniger umfassen.

{{chart:maia-300-gegen-maia-200}}

Für das Rack verspricht Microsoft bis zu 2,5-fach mehr Leistung pro Watt gegenüber Maia 200, und mit 96 Beschleunigern bis zu siebenfach mehr Token-Durchsatz. Beide Angaben beziehen sich auf das eigene Vormodell. Die Schlagzeilen-Zahlen dagegen vergleichen mit dem Wettbewerb: 40 Prozent mehr Token je Megawatt gegenüber „führenden GPU-Systemen" – ausdrücklich als Erwartung formuliert („we expect"). Für Maia 200 nennt Microsoft bereits gemessene bis zu 1,7-fach mehr Token je Watt bei den eingebauten KI-Funktionen in Teams, Copilot und Cowork, wiederum gegenüber „führender GPU-Infrastruktur".

Genau hier liegt die Einschränkung. Microsoft schreibt nicht, welche GPUs die Vergleichsbasis sind, welche Aufgabe gemessen wurde und unter welchen Bedingungen. „Token je Watt" ist eine Kennzahl, die stark von Modell, Kontextlänge, Stapelverarbeitung und Auslastung abhängt. Ohne unabhängige Messung bleibt es eine Herstellerangabe – wie bei allen Chip-Ankündigungen dieses Jahres. Mehr Details will Microsoft im November auf der eigenen Konferenz Ignite nachliefern.

## Warum das zählt

Zum Ersten verschiebt sich das Geschäft. Training ist ein Projekt, Inferenz ist Dauerbetrieb. Wer den Betrieb auf eigener Hardware fährt, muss den Chip nicht mit Marge einkaufen, sondern nur bauen. Microsoft nennt keine Einsparungen und keinen Anteil, den Maia am Ende abdecken soll – aber dass NVIDIA-Karten im Dauerbetrieb das größte Kostenstück sind, ist der Grund, weshalb Microsoft, Google und Amazon alle an eigenen Beschleunigern arbeiten.

Zum Zweiten geht es um Strom. Rechenzentren werden heute nicht mehr von der Zahl der Chips begrenzt, sondern von Anschlussleistung und Kühlung. Ein [IEA-Bericht](https://www.iea.org/reports/energy-and-ai/executive-summary) von 2025 rechnet damit, dass der Stromverbrauch der Rechenzentren von rund 415 Terawattstunden im Jahr 2024 auf etwa 945 Terawattstunden im Jahr 2030 steigt; wie sich das gegen die Effizienzgewinne verhält, haben wir [an anderer Stelle ausgerechnet](wo-soll-die-ki-skalierung-enden-ueber-kraftwerke-datenmauern-und-kluegere-rechenwege.html). Ein Zuwachs von 40 Prozent beim Wirkungsgrad hilft nur, wenn die Nachfrage nicht schneller wächst – der alte {{Rebound-Effekt}}: Was billiger wird, wird häufiger genutzt.

Zum Dritten signalisiert der Zeitplan, wie lang das dauert. Microsoft schreibt selbst, Silizium-Entwicklung brauche Jahre. Wer 2027 Gigawatt-Mengen eigenes Silizium hochzieht, hat diese Entscheidung lange vor der aktuellen Debatte getroffen. Der Microsoft-Chef fordert in derselben Woche eine „Notbremse" für KI-Systeme, also die Möglichkeit, ein Modell mitten in der Aufgabe zu stoppen ([heise](https://www.heise.de/news/Microsoft-Chef-will-Notbremse-fuer-kuenstliche-Intelligenz-11483617.html)). Die Botschaft ist dieselbe: Kontrolle über die eigene Infrastruktur.

## Was heißt das praktisch

- **Für Azure-Kunden:** Wer Copilot, GitHub Copilot oder Foundry nutzt, rechnet künftig teilweise auf Maia-Hardware – ohne dass Microsoft Preise oder Leistungsversprechen dazu nennt. Was das für Abrechnung und Verfügbarkeit bedeutet, bleibt offen.
- **Für Effizienzversprechen:** Aussagen wie „40 Prozent mehr Token je Megawatt" sind ohne genannte Vergleichsbasis nicht nachprüfbar. Wer solche Zahlen weiterverwenden will, sollte sie als Herstellerangaben kennzeichnen und die fehlende Messung dazusagen.
- **Für den Energie-Diskurs:** Wichtiger als der Wirkungsgrad einzelner Chips ist die Gesamtmenge. Ein Rechenzentrumsverbund, der um 40 Prozent sparsamer rechnet, aber dreimal so viel Arbeit verrichtet, verbraucht mehr Strom als vorher.
- **Für den Markt:** Eigene Chips für die Inferenz sind das Mittel, mit dem die großen Cloud-Anbieter ihre Kosten senken und ihre Abhängigkeit vom Zulieferer verringern. Ob Microsoft das gelingt, entscheidet sich 2027 im Betrieb – nicht in einer Folie.

## Quellen

- [Microsoft: Microsoft to expand Azure Maia system to multi-gigawatt deployments](https://blogs.microsoft.com/blog/2026/10/12/microsoft-to-expand-azure-maia-system-to-multi-gigawatt-deployments/) (Scott Guthrie, 12. Oktober 2026)
- [Azure Blog: Deep dive into Azure Maia 300 architecture](https://azure.microsoft.com/en-us/blog/deep-dive-into-azure-maia-300-architecture/) (12. Oktober 2026)
- [Microsoft News: Maia 300 – Bilder und Videos zur Ankündigung](https://news.microsoft.com/maia-2026/) (12. Oktober 2026)
- [Satya Nadella auf X zur Maia-300-Ankündigung](https://x.com/satyanadella/status/2109631106404487523) (12. Oktober 2026)
- [The Decoder: Microsoft plans to scale its own Maia AI chips to gigawatt levels by 2027](https://the-decoder.com/microsoft-plans-to-scale-its-own-maia-ai-chips-to-gigawatt-levels-by-2027/) (12. Oktober 2026)
- [heise: Microsoft-Chef will „Notbremse" für künstliche Intelligenz](https://www.heise.de/news/Microsoft-Chef-will-Notbremse-fuer-kuenstliche-Intelligenz-11483617.html) (12. Oktober 2026)
