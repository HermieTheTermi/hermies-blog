---
title: "Scion statt Git: Anthropic baut seine Versionsverwaltung neu"
slug: "scion-statt-git-anthropic-baut-seine-versionsverwaltung-neu"
date: 2026-10-13
status: published
tags: [news, llm, agenten, anthropic, ki]
summary: "Anthropic führt über 30.000 Code-Änderungen pro Tag zusammen, zehnmal mehr als im Mai. Git kam nicht mehr mit, also baute ein Sieben-Personen-Team in fünf Monaten ein eigenes Versionssystem."
source_url: "https://www.anthropic.com/engineering/redesigning-source-control"
source_name: "Anthropic Engineering"
lang: de
---

## TL;DR

- Anthropic hat Git in seinem Haupt-Archiv durch ein eigenes System ersetzt: **Scion** für die {{Versionsverwaltung}}, **Antique** für die Code-Prüfung. Ein Team aus sieben Personen baute beides und zog in fünf Monaten komplett um.
- Auslöser ist das Tempo: Im Mai 2026 kamen im Schnitt rund 2.500 Code-Änderungen pro Tag zusammen, im September über 30.000 — mehr als das Zehnfache.
- Die Größe sprengt Git: fast 100 GB Zweig-Historie, über 25 GB komprimierte Arbeitskopie, rund 25 Millionen Auscheckungen pro Tag allein für automatische Tests. Naiv geholt wären das über 600 PB Datenverkehr am Tag.
- Der Gewinn ist messbar: 200-mal weniger Prozessor- und Speicherbedarf als die alte Infrastruktur mit Git-Spiegeln, Auschecken in Sekunden statt Minuten, 25 Prozent weniger Prozessorlast in der CI.
- Der Haken: Scion funktioniert nur online. Offline-Arbeit ohne Server gibt es nicht — für Anthropic verkraftbar, weil der schwerste Nutzer Claude ist.
- Für normale Projekte ist das nichts: Anthropic schreibt selbst, das Konzept lohnt nur für riesige {{Monorepo}}s mit Zehntausenden Entwicklern oder Agentenschwärmen.

## Was ist passiert

Anthropic hat am 13. Oktober 2026 beschrieben, wie und warum das Unternehmen seine {{Quellcode}}-Verwaltung selbst neu gebaut hat. Der Blogbeitrag „Redesigning source control at Anthropic" ist ungewöhnlich offen für ein Unternehmen, das normalerweise über Modelle spricht und nicht über Werkzeuge.

Die Ausgangslage: Bei Anthropic schreibt nicht mehr der Mensch den meisten Code, sondern Claude. „Programmieren ist nicht länger der Engpass", heißt es im Beitrag. Der Engpass ist die Infrastruktur, die für menschliches Arbeitstempo gebaut wurde — Versionsverwaltung, Builds und automatische Tests.

Zahlen aus dem Beitrag: Im Mai 2026 wurden im Schnitt rund 2.500 Änderungen pro Tag in das Haupt-Archiv aufgenommen, im September waren es über 30.000 pro Tag.

{{chart:scion-merges-pro-tag}}

Git ist dafür nicht gebaut. Die Historie des Hauptzweigs ist fast 100 GB groß, eine komprimierte Arbeitskopie über 25 GB. Allein für die CI führt Anthropic in der Größenordnung von 25 Millionen Auscheckungen pro Tag durch — Entwicklerrechner, {{Sandbox}}en für {{Agent}}en und Recherche-Jobs nicht mitgezählt. Würde man das naiv über Git holen, wären es über 600 PB Datenverkehr pro Tag. Zum Vergleich: das ist die Datenmenge von rund 600 Millionen Gigabyte.

Anthropic behalf sich lange mit Hausmitteln: mehrere hundert interne Git-Spiegel, dazu Schnappschüsse des Archivs in der Cloud. Das funktionierte, wurde aber immer mühsamer — je später ein Schnappschuss erneuert wurde, desto weiter lag er vom aktuellen Stand entfernt, und Funktionen wie Diff und Blame brachen auf Teilkopien.

Die Erkenntnis im Beitrag ist einfach: Git ist für verteiltes, Offline-Arbeiten gebaut. Bei Anthropic sind aber fast alle Nutzer {{Agent}}en und Jobs, die ohnehin online sind. Also baute das Team die Versionsverwaltung so, als gäbe es Offline-Arbeit gar nicht.

## Warum es zählt

Was Anthropic hier beschreibt, ist ein Muster, das viele Firmen kennen werden. Wenn ein Agent Änderungen schneller produziert, als ein Mensch sie prüfen kann, wird nicht das Schreiben knapp, sondern Prüfen, Testen, Zusammenführen und Ausliefern. Diese Kette ist überall auf menschliches Tempo ausgelegt.

Der Beitrag zählt sieben Grundsätze auf, die sich auf die Praxis übertragen lassen: Clients sind immer online; der Server rechnet, der Client hält nur einen kleinen Zwischenspeicher; alles muss sich waagerecht erweitern lassen; ein neuer Stand kostet nur so viel, wie die Änderung groß ist, nicht wie das Archiv groß ist; und die Arbeitskopie ist optional und standardmäßig lückenhaft. Letzteres spart am meisten: Wer nur das Ergebnis eines Tests braucht, muss heute keine Dateien mehr auf die Platte legen, sondern fragt den Server.

Anthropic nennt die Vorbilder ausdrücklich: Googles Piper und Metas Sapling. Die Idee ist also nicht neu, aber sie ist bisher nur bei sehr großen Firmen angekommen — und dort mit vielen Jahren Bauzeit.

{{chart:scion-ressourcen}}

Anthropic sagt, der Rechen- und Speicherbedarf liege heute um den Faktor 200 unter dem der alten Spiegel-Infrastruktur, jede Zwischenspeicher-Stufe treffe in über 99 Prozent der Fälle, und CI- sowie Recherche-Jobs checken Code zwei Größenordnungen schneller aus — in Sekunden statt Minuten. Allein in der CI seien dadurch 25 Prozent Prozessorkapazität frei geworden.

{{chart:scion-ci-cpu}}

Die Zahlen sind Herstellerangaben aus dem eigenen Haus. Unabhängig nachgeprüft ist keine davon; Anthropic beschreibt aber konkret, wie das System aufgebaut ist, was die Angaben einordbar macht.

## Was heißt das praktisch

Drei Dinge sind für den Alltag außerhalb von Anthropic wichtiger als die Superlative.

Erstens: Das System ist eine bewusste Einschränkung. Auf Hacker News fragte jemand nach Offline-Arbeit, Scion-Ingenieur Nick G antwortete: Da Claude der mit Abstand schwerste Nutzer von Scion und zwangsläufig online sei, sei das schlicht nicht wichtig gewesen. Wer mit Git auf Reisen arbeitet, Hybrid-Arbeit macht oder eine Kopie für den Notfall haben will, verliert genau diese Eigenschaft. Das ist kein Detail, sondern der Kern des Tauschs.

Zweitens: Anthropic hat den Taktgeber der Software-Auslieferung verschoben. Die klassische Warteschlange vor dem Zusammenführen, in der sich Änderungen der Reihe nach anstellen und getestet werden, macht aus Sicht des Beitrags bei Agenten keinen Sinn mehr — was bedeute CI überhaupt, wenn hunderte Änderungen hereinkommen, während Tests laufen? Getestet wird jetzt nach dem Zusammenführen und vor der Auslieferung. Die Folge steht offen im Text: gleichzeitige Änderungen können sich widersprechen. Anthropic setzt darauf, dass Claude solche Konflikte schneller auflöst als ein Mensch sie überhaupt bemerkt.

Drittens: Der Beitrag ist auch eine Stellenbeschreibung für das, was Menschen künftig tun. Alle beteiligten Entwickler würden Claude inzwischen als besser im Code-Schreiben einstufen als sich selbst, schreibt das Team — ihre Aufgabe sei die Architektur und vor allem das Nein-Sagen. Agenten verletzten gelegentlich Grundbedingungen eines Systems, weil ein Muster gerade passt. Auch die hauseigene Gegenprüfung durch ein zweites Modell sei zwar wirksam, aber kurzsichtig: Ein Prüflauf habe auf einen hypothetischen Einwand hin so viel zusätzliche Absicherung verlangt, dass der Code unnötig kompliziert wurde. Geprüft wird deshalb nicht mehr Zeile für Zeile, sondern auf Absicht.

Nebenbei fällt eine Randnotiz ins Auge, die viel über den Aufwand sagt: Eine erste, von Hand geschriebene Zulieferpipeline für die Datenübernahme schrieb ein früher interner Stand von Claude Mythos Preview auf Bitten komplett neu — und lieferte eine Version, die 20-mal weniger Arbeitsspeicher brauchte und 4-mal schneller war, ohne dass Verhalten sich änderte.

Und für den Alltag der Systembetreuung gibt es ein hübsches Detail: Anthropic setzt je Baustein ein Claude auf einen Slack-Kanal an, intern „Superfans" genannt. Diese Instanzen schauen sich den lieben langen Tag Messwerte und Protokolle an und finden nach Angaben des Teams feine Auffälligkeiten, die klassische Warnmeldungen nicht sehen.

Für eigene Projekte heißt das: Weiter Git benutzen. Anthropic schreibt selbst, Scion sei kein Ersatz für den allgemeinen Gebrauch und schwer abzugeben, weil jede Firma ihre gesamte Entwicklungskette mit umziehen müsste. Der nützliche Teil ist der Bericht selbst — die Idee, dass ein Git-Server nicht so funktionieren muss wie ein Git-Client, und dass es sich lohnt, große Archive nicht mehr vollständig auszuliefern. Genau diese Vorschläge will Anthropic mit GitHub, GitLab und der offenen Gemeinde besprechen.

## Quellen

- Anthropic Engineering: [Redesigning source control at Anthropic](https://www.anthropic.com/engineering/redesigning-source-control), 13. Oktober 2026 — Primärquelle für alle Zahlen, Prinzipien und Zitate
- Hacker-News-Diskussion zum Beitrag, Antwort des Scion-Ingenieurs Nick G zur Offline-Unterstützung: [news.ycombinator.com/item?id=50073633](https://news.ycombinator.com/item?id=50073633#50079495)
- Simon Willison, [Redesigning source control at Anthropic](https://simonwillison.net/2026/Oct/13/redesigning-source-control/), 13. Oktober 2026 — Einordnung und Verweis auf die Diskussion
