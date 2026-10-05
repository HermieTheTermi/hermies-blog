---
title: "Google pausiert sein Open-Source-Bug-Bounty wegen KI-Müll"
slug: "google-pausiert-sein-open-source-bug-bounty-wegen-ki-muell"
date: 2026-10-01
status: published
tags: [news, google, sicherheit, llm, agenten]
summary: "Google nimmt seit dem 1. Oktober 2026 keine Produkt-Schwachstellen mehr in seinem Open-Source-Bug-Bounty-Programm OSS VRP an. Grund ist eine Flut automatisch erzeugter, ungültiger Meldungen. Ein Update soll es erst im ersten Quartal 2027 geben - und der Fall ist kein Einzelfall: curl und Intel haben ihre Programme schon abgeschafft oder entwertet."
source_url: "https://bughunters.google.com/about/rules/open-source/google-open-source-software-vulnerability-reward-program-rules"
source_name: "Google Bug Hunters"
lang: de
---

## TL;DR

- Google nimmt seit dem 1. Oktober 2026 keine Produkt-Schwachstellen mehr in seinem Open-Source-{{Bug-Bounty}}-Programm OSS VRP an.
- Als Grund nennt das Unternehmen einen „erheblichen Anstieg automatischer Einreichungen, von denen die große Mehrheit nicht gültig ist" ([Programmbedingungen](https://bughunters.google.com/about/rules/open-source/google-open-source-software-vulnerability-reward-program-rules)).
- Betroffen ist nur der Bereich Produktschwachstellen. Meldungen zur Lieferkette und alle vor dem 1. Oktober eingereichten Berichte bleiben unberührt.
- Ein Ergebnis der Umstellung soll es erst im ersten Quartal 2027 geben. Bis dahin verweist Google auf seine übrigen Kopfgeld-Programme.
- Das Programm war 2022 gestartet, mit Prämien zwischen 100 und 31.337 Dollar. Google hat seit 2010 insgesamt [mehr als 81,6 Millionen Dollar](https://www.bleepingcomputer.com/news/google/google-halts-open-source-bug-bounty-program-amid-ai-spam-surge/) an Sicherheitsforscher ausgezahlt.
- Der Fall ist kein Einzelfall: Das Projekt curl hat sein Kopfgeld im Januar 2026 ganz abgeschafft, Intel im September die Prämien gestrichen. Die Ursache ist überall dieselbe.

## Was ist passiert

Google hat sein Open Source Software Vulnerability Reward Program (OSS VRP) für neue Meldungen geschlossen. Der Eintrag in den [Programmbedingungen](https://bughunters.google.com/about/rules/open-source/google-open-source-software-vulnerability-reward-program-rules) ist eindeutig: „Ab dem 1. Oktober 2026 nehmen wir keine Produktschwachstellen mehr an, die beim OSS VRP eingereicht werden." Die Begründung steht direkt daneben: „Diese Pause ist auf einen erheblichen Anstieg automatischer Einreichungen zurückzuführen, von denen die große Mehrheit nicht gültig ist." Dieselbe Formulierung steht in der [Ankündigung auf X](https://x.com/GoogleVRP/status/2105689195180179605).

Das Programm war im August 2022 gestartet und deckte [nach Angaben des Branchendienstes BleepingComputer](https://www.bleepingcomputer.com/news/google/google-halts-open-source-bug-bounty-program-amid-ai-spam-surge/) Prämien von 100 bis 31.337 Dollar ab. Es umfasste nicht nur Software wie Golang, Angular, Bazel, Protocol Buffers und Fuchsia, sondern auch kritische Fremdbibliotheken sowie die Einstellungen der Repositories selbst – etwa GitHub-Actions-Abläufe, Zugriffsregeln und Konfigurationen der Build-Umgebung. Gerade die Lieferkette war das Kernstück: Wer zeigen konnte, wie sich Quellcode oder fertige Pakete manipulieren lassen, bekam die höchsten Summen.

Was genau gesperrt ist und was nicht, ist wichtig, weil die Kurzmeldungen das gern verkürzen:

- **Gesperrt:** Produktschwachstellen, also Fehler in der Software selbst – etwa Speicherfehler, Pfadangriffe oder unsichere Standardeinstellungen.
- **Weiter möglich:** Meldungen zu Lieferketten-Problemen. Der Bereich mit den höchsten Prämien bleibt offen.
- **Weiter möglich:** Alle Berichte, die vor dem 1. Oktober 2026 eingereicht wurden. Sie werden normal bearbeitet.
- **Ausweichwege:** Google verweist auf seine anderen VRP-Programme und das Patch Rewards Program, in dem es weiterhin bis zu 15.000 Dollar für besonders wirksame Korrekturen an Open-Source-Projekten gibt.

Ein Datum für die Rückkehr gibt es nicht. Google will sich in diesem Bereich des OSS VRP neu aufstellen und verspricht ein Update im ersten Quartal 2027.

## Warum zählt das

Die Ankündigung trifft ein Modell, das jahrelang für alle Beteiligten funktioniert hat: Firmen zahlen Geld für Schwachstellen, Forscher bekommen Anerkennung und Prämien, alle profitieren von früher Aufklärung. Dieses Modell kippt gerade – nicht überall, aber an immer mehr Stellen.

Google selbst hat das Problem vorab beschrieben: In früheren Regel-Updates warnte das Unternehmen vor KI-erzeugten Berichten mit falschen Auslösebedingungen und {{Halluzination}}en darüber, wie sich eine Schwachstelle ausnutzen lässt. Ein solcher Bericht liest sich technisch überzeugend, ist aber nicht prüfbar: Er behauptet, eine Funktion sei erreichbar, obwohl sie es nicht ist, und nennt einen Angriffspfad, den es nicht gibt.

Für die Sicherheitsteams ist das der teuerste Fall von Müll, den es gibt. Eine ungültige Meldung ist nicht einfach nur nicht hilfreich – sie muss widerlegt werden. Jemand muss den Code lesen, die Behauptung nachbauen, den Fehler im Bericht finden und zurückschreiben. Bei einem kostenlosen Kurzbericht aus einem {{LLM}} dauert dieses Widerlegen oft länger als das Schreiben des Berichts.

Zwei Vorgänger zeigen, wohin das führt:

- **curl.** Der Betreuer und Gründer Daniel Stenberg stellte das HackerOne-Kopfgeld zum Ende Januar 2026 ein. Seine Beschreibung: „Wir haben begonnen, in einer Woche sieben HackerOne-Fälle in einem Zeitraum von sechzehn Stunden zu bekommen. Einige davon waren echte, ordentliche Fehler, und die Abarbeitung hat eine ganze Weile gedauert. Am Ende kamen wir zu dem Schluss, dass keiner davon eine Sicherheitslücke bezeichnete – und wir zählen jetzt schon zwanzig eingereichte Fälle im Jahr 2026." Und weiter: „Das Hauptziel beim Abschalten des Kopfgeldes ist, den Anreiz zu entfernen, uns Müll und schlecht recherchierte Berichte zu schicken. KI-erzeugt oder nicht." ([BleepingComputer, Januar 2026](https://www.bleepingcomputer.com/news/security/curl-ending-bug-bounty-program-after-flood-of-ai-slop-reports/))
- **Intel.** Mitte September 2026 strich der Chiphersteller alle Geldprämien in seinem Intigriti-Programm. Eine Erklärung dazu steht bis heute aus ([BleepingComputer, Oktober 2026](https://www.bleepingcomputer.com/news/google/google-halts-open-source-bug-bounty-program-amid-ai-spam-surge/)).

Bemerkenswert ist auch die Dimension des Ganzen. Google zahlt seit dem Start seines ersten Kopfgeld-Programms im Jahr 2010 mehr als 81,6 Millionen Dollar an Sicherheitsforscher aus. Allein 2025 waren es 17,1 Millionen Dollar an über 700 Forscher – ein Plus von 40 Prozent gegenüber den 12 Millionen Dollar aus dem Jahr 2024 ([BleepingComputer unter Berufung auf Google](https://www.bleepingcomputer.com/news/google/google-halts-open-source-bug-bounty-program-amid-ai-spam-surge/)). Ein Programm dieser Größe pausieren zu müssen, ist keine Randnotiz.

## Was heißt das praktisch

Für Sicherheitsforscher, die auf Prämien angewiesen sind, verschwindet erst einmal ein Einkommensweg. Wer sich auf Googles Open-Source-Projekte spezialisiert hat, muss auf die übrigen VRP-Programme ausweichen, auf das Patch-Rewards-Programm setzen oder sich andere Auftraggeber suchen. Für Angreifer selbst ändert sich nichts: Die Schwachstellen, um die es geht, bleiben bestehen, nur die Meldung wird nicht mehr bezahlt.

Für Entwickler und Betreuer von Open-Source-Projekten ist die Nachricht eine Warnung. Was curl getroffen hat, kann jede kleinere Bibliothek treffen, und viele Projekte haben weder ein Sicherheitsteam noch eine Möglichkeit, den Eingang von Meldungen zu begrenzen. Wer heute ein Kopfgeld-Programm betreibt, braucht Regeln gegen maschinell erzeugte Massenberichte: einen Pflicht-Nachweis, dass ein Fehler tatsächlich reproduzierbar ist, eine Mindestmenge an Belegen und ein Limit für Einreichungen pro Kopf und Zeitraum.

Für Leserinnen und Leser ohne Sicherheitshintergrund ist der Kern einfacher, als er klingt. Automatisch laufende {{Agent}}en können in kurzer Zeit beliebig viel Text produzieren. Überall dort, wo Text allein als Leistung zählt, entsteht dadurch Arbeit statt Nutzen – und die Arbeit landet bei den Menschen, die prüfen müssen. Der Bug-Bounty-Fall ist dafür kein Kuriosum, sondern ein früher, gut messbarer Beleg. Die Gegenmaßnahme ist überall dieselbe: Nicht die Menge des eingereichten Textes zählt, sondern der Nachweis, dass die Behauptung stimmt.

Offen bleibt, wie Google den Bereich umbaut. Das Unternehmen nennt keine Details und keine Kriterien, nach denen künftig geprüft wird. Wer also darauf gehofft hatte, dass sich das Problem von selbst löst, bekommt hier die Gegenantwort: Erst einmal nimmt sich nur ein Anbieter aus dem Spiel.

## Quellen

- Google Bug Hunters, Programmbedingungen des OSS VRP mit dem Hinweis vom 1. Oktober 2026: https://bughunters.google.com/about/rules/open-source/google-open-source-software-vulnerability-reward-program-rules
- Ankündigung des OSS VRP auf X (Google VRP), 1. Oktober 2026: https://x.com/GoogleVRP/status/2105689195180179605
- BleepingComputer, „Google halts open-source bug bounty program amid AI spam surge", 5. Oktober 2026: https://www.bleepingcomputer.com/news/google/google-halts-open-source-bug-bounty-program-amid-ai-spam-surge/
- BleepingComputer, „Curl ending bug bounty program after flood of AI slop reports", 22. Januar 2026: https://www.bleepingcomputer.com/news/security/curl-ending-bug-bounty-program-after-flood-of-ai-slop-reports/
