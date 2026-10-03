---
title: "Gemini 4 Argon: Googles neues Frontier-Modell startet zuerst bei Cyber-Verteidigern"
slug: "gemini-4-argon-our-next-era-of-frontier-intelligence"
date: 2026-09-30
status: published
tags: [modelle, google, benchmarks]
summary: "DeepMind stellt Gemini 4 Argon vor: Frontier-Leistung, gestaffelter Zugang ab Cyber-Verteidigern, 2/10 Dollar pro Million Tokens und interne Agenten-Ergebnisse mit Zahlen."
source_url: "https://deepmind.google/blog/gemini-4-argon-our-next-era-of-frontier-intelligence/"
source_name: "Google DeepMind Blog"
lang: de
---

Google DeepMind hat am 30. September 2026 **Gemini 4 Argon** vorgestellt, sein neues Frontier-Modell. Es soll tiefes Reasoning über lange Aufgabenketten halten — laut Ankündigung für Software-Engineering im echten Betrieb, Wissensarbeit in Recht und Finanzen sowie für die Verteidigung gegen Cyberangriffe.

## Was passiert ist

Argon startet nicht offen. Google rollt das Modell zunächst an ausgewählte Cyber-Verteidiger aus, über das hauseigene „Fairwind Program". Man beteiligt sich nach eigenen Angaben am freiwilligen US-Vorabprüfungsprozess für Modelle und will den Zugang schrittweise erweitern — Entwickler, Unternehmen und Verbraucher sollen „so schnell wie möglich" folgen.

Der Einstiegspreis liegt bei **2 US-Dollar pro Million Input-Tokens** und **10 US-Dollar pro Million Output-Tokens**. Tokens, die aus dem Zwischenspeicher kommen, kosten laut Ankündigung 95 % weniger als normale Input-Tokens.

## Warum das zählt

Drei Dinge sind bemerkenswert.

**Der Preis.** Zwei Dollar pro Million Input-Tokens ist die günstigste Frontier-Ankündigung, die Google bisher für ein Modell dieser Klasse genannt hat — ob das im Betrieb hält, muss man abwarten, aber es setzt eine Marke.

**Die Zahlen, die Google selbst nennt.** Vier Beispiele aus dem eigenen Haus:

- **Quanten-Subroutinen:** Argon half Forschern, die Spacetime-Ressourcen (Qubits × Gatter) von Subroutinen zu optimieren, die wichtige Anwendungen ausbremsen. In einem Beispiel schlug es die veröffentlichte Vergleichsbasis um **40 %** — laut Blogbeitrag „in wenigen Minuten".
- **Speicheroptimierung:** Eine Gruppe von Argon-Agenten analysierte flottenweite Profiling-Telemetrie und identifizierte und setzte Speicheroptimierungen in Googles Rechenzentren autonom um. Nach dem Rollout sind das **über 300 TiB** freigegebener Speicher, mit geschätzt 500 TiB bis 1 PiB Gesamteinsparung.
- **Code-Migration:** Argon-Agenten migrieren C/C++-Codebasen zu Rust — von Zehntausenden Zeilen in Kernbibliotheken wie `re2` und `libgav1` bis zu **über 800.000 Zeilen** für den Fuchsia-Kernel Zircon. Bei `libgav1` haben die Agenten eigenen Angaben zufolge 32.000 Zeilen SIMD-Code ersetzt, indem sie viele Runden profilgesteuerter Experimente gefahren und die Compiler-Ausgabe studiert haben.
- **Qualität:** Tausende Googler nutzen Argon intern für spezialisierte Coding-Aufgaben, Recherche und Texte.

**Die Veröffentlichungsstrategie.** Statt eines offenen API-Drops bekommt zuerst eine geschlossene Gruppe Zugang, parallel läuft ein Regierungsverfahren. Das ist der neue Normalzustand bei Frontier-Modellen: Fähigkeiten und Zugangskontrolle werden zusammen ausgeliefert.

Der Vollständigkeit halber: Google nennt in der Ankündigung nicht, wie Argon auf öffentlichen Benchmarks abschneidet. Die genannten Zahlen sind interne Fallbeispiele, keine unabhängig nachprüfbaren Messwerte.

## Was heißt das praktisch

Wer heute mit Argon arbeiten will, kommt nicht ohne Weiteres dran — der Zugang ist gestaffelt und beginnt bei Cyber-Verteidigern. Interessant ist für die meisten deshalb weniger das Modell selbst als das Muster dahinter: **Agenten, die über Stunden an einer Codebasis arbeiten und ihre Ergebnisse selbst gegen Profiler-Daten prüfen**, sind bei Google offenbar kein Demo-Stand mehr, sondern laufender Betrieb. Und der genannte Preis deutet an, wohin die Frontier-Klasse wirtschaftlich geht.

## Quellen

- Google DeepMind: [Gemini 4 Argon: our next era of frontier intelligence](https://deepmind.google/blog/gemini-4-argon-our-next-era-of-frontier-intelligence/) (30.09.2026)
- Google: [The latest AI news we announced in September 2026](https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-september-2026/)
