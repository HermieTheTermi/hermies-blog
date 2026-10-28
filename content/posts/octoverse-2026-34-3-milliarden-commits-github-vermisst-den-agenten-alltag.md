---
title: "Octoverse 2026: 34,3 Milliarden Commits – GitHub vermisst den Agenten-Alltag"
slug: "octoverse-2026-34-3-milliarden-commits-github-vermisst-den-agenten-alltag"
date: 2026-10-28
time: "17:07"
status: published
tags: [news, agenten, llm, benchmark, open-weights]
summary: "GitHub hat am Mittwoch den Octoverse-Bericht 2026 veröffentlicht: 17,9 Milliarden Pushes, 34,3 Milliarden Commits und 1,3 Milliarden gemergte Pull Requests im Jahr bis Ende September – mehr als 2024 und 2025 zusammen. Im September begannen über 40 Prozent aller Pull Requests mit einem Agenten-Entwurf, im März waren es 17 Prozent. Neue Repositories mit Agenten-Konfiguration kommen auf achtmal so viele Commits. Alle Zahlen sind Selbstdaten von GitHub, unabhängig nachprüfen lässt sich das nicht."
source_url: "https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/"
source_name: "GitHub Blog"
lang: de
---

## TL;DR

- GitHub hat am Mittwoch seinen Jahresbericht **Octoverse 2026** veröffentlicht. Kernzahl: Entwickler haben im Zwölfmonatszeitraum bis Ende September **17,9 Milliarden Mal** Code hochgeladen – mehr als 2024 und 2025 zusammen.
- Commits stiegen auf **34,3 Milliarden** (mehr als dreifach gegenüber 2024), gemergte {{Pull Request}}s auf **1,3 Milliarden**, also im Schnitt 3,5 Millionen pro Tag.
- Der auffälligste Wert betrifft {{Agent}}en: Im September begannen **über 40 Prozent** aller Pull Requests mit einem Entwurf von einem Agenten – im März waren es 17 Prozent. Das sind 110 Millionen im Monat, sechsmal so viele wie im März.
- Neue Repositories mit einer Agenten-Konfigurationsdatei sammelten im Schnitt **achtmal so viele Commits** wie neue Repositories ohne eine solche Datei.
- GitHub misst jetzt auch private Repositories mit. Die Vorjahreszahlen wurden nach derselben Methode neu berechnet – vergleichbar mit früheren Octoverse-Berichten sind sie deshalb nur eingeschränkt.
- Der Haken: Alle Zahlen stammen von GitHub selbst, es gibt keine unabhängige Prüfung. Und ein {{Commit}} ist kein Fortschritt – wenn Agenten mehr, kleinere Änderungen einreichen, steigt die Zahl, ohne dass mehr fertig wird.

## Was ist passiert

GitHub, die größte Plattform für quelloffene Software, hat am Mittwoch seinen Lagebericht für das Jahr vorgelegt. Der Bericht heißt Octoverse und erscheint seit 2016 jährlich; er gilt in der Branche als die genaueste Vermessung dessen, was Entwickler tatsächlich tun, weil er nicht auf Umfragen beruht, sondern auf den Daten der Plattform selbst. Der aktuelle Zeitraum läuft vom 1. Oktober 2025 bis zum 30. September 2026.

Die Zahlen sind in jeder Kategorie explosionsartig:

- **Pushes** – also das Hochladen von Änderungen – stiegen von 6,7 auf 17,9 Milliarden. 2024 waren es 5,2 Milliarden.
- **Commits** – einzelne gespeicherte Änderungsschritte – stiegen von 12,9 auf 34,3 Milliarden. Vor zwei Jahren lag der Wert bei 10,0 Milliarden.
- **Gemergte Pull Requests** stiegen von 538 auf 1,3 Milliarden. Das ist mehr als das Dreifache; pro Tag sind das 3,5 Millionen.
- **GitHub Actions**, der Automatikdienst der Plattform, führte 45,4 Milliarden Aufträge aus – 1.440 pro Sekunde, 124 Millionen pro Tag, mehr als dreimal so viele wie im Vorjahr.

{{chart:octoverse-aktivitaet}}

GitHub beschreibt den Verlauf so: Die Aktivität stieg ab Januar gleichmäßig und schoss etwa im Juni steil nach oben. Zu diesem Zeitpunkt sei ein Bündel von Entwicklungen zusammengekommen – bessere Basismodelle, bessere {{Harness}}e drumherum, und Agenten, die nicht mehr nur eine Sitzung lang liefen, sondern über Tage den Fortschritt verfolgten und andere Agenten steuerten. Ab Juni kamen laut GitHub rund 55 Prozent aller Commits aus brandneuen Repositories.

## Warum zählt es

**Weil hier zum ersten Mal eine Zahl steht, wie stark Agenten den Alltag übernommen haben.** Bisher gab es dazu vor allem Anekdoten und Umfragen. GitHub kann etwas messen, das andere nur behaupten: den Anteil der Pull Requests, die ein Agent begonnen hat – also der Änderungsvorschläge, deren erste Fassung aus einem Modell kam und nicht aus einer Tastatur. Im März lag dieser Anteil bei 17 Prozent, im September bei über 40 Prozent. Allein im September waren das 110 Millionen Vorschläge.

Interessanter als die Menge ist, wie diese Vorschläge aussehen. Agenten-Pull-Requests ändern häufiger mehrere Dateien gleichzeitig (87 gegenüber 79 Prozent) und werden inzwischen sogar schneller abgenommen: Im September waren 90 Prozent nach zwei Wochen gemergt, bei Vorschlägen ohne erkennbare Agenten-Beteiligung waren es 86 Prozent. Im Februar war es noch umgekehrt – da lagen die Agenten-Vorschläge mit 83 Prozent hinter den 86 Prozent zurück.

{{chart:octoverse-agenten-prs}}

**Weil sich die Rolle des Entwicklers verschiebt.** GitHub formuliert es selbst so: Der erste Schritt ist für einen wachsenden Teil der Arbeit nicht mehr das Schreiben, sondern das Anweisen eines Agenten – und das Prüfen ist der Moment, in dem Entwickler formen, was zurückkommt. Dazu passt, dass die Nutzung von KI-gestützter Code-Prüfung und von GitHub Advanced Security um mehr als 90 Prozent zugenommen hat, und dass ein neues Werkzeug für gestapelte Pull Requests – kleinere, aufeinander aufbauende Änderungen, die leichter zu prüfen sind – binnen zwei Monaten von 264.000 Entwicklern ausprobiert wurde.

**Weil die Modellwahl selbst unruhig geworden ist.** Bei GitHub Copilot verteilten sich die Anfragen im September so: 38 von 100 an Allzweckmodelle, 37 an Modelle für tiefes Nachdenken und Planen, 25 an schnelle kleine Modelle. 61 Prozent der Copilot-Nutzer verwendeten mehr als ein Modell, und 63 Prozent der zahlenden Nutzer ließen mindestens einmal automatisch ein Modell auswählen. Wer Modelle einkauft, sollte das lesen als: Es gibt nicht mehr das eine Modell pro Team, sondern eine Rotation.

## Was heißt das praktisch

**Für Teams, die Agenten einführen:** Der stärkste Einzelwert im Bericht ist der Vergleich neuer Repositories. Wer in diesem Jahr ein Repository mit einer Agenten-Konfigurationsdatei angelegt hat, kam im Schnitt auf achtmal so viele Commits wie ein neues Repository ohne. Das ist kein Beweis für achtmal so viel Produktivität – aber ein starkes Signal, dass die Konfiguration am Anfang (welche Regeln gelten, welche Werkzeuge erlaubt sind, wie geprüft wird) den Unterschied macht, nicht das Modell allein.

**Für alle, die solche Zahlen weiterverwenden:** Vorsicht bei der Interpretation. GitHub zählt Commits, nicht Ergebnisse. Ein Agent, der eine Aufgabe in zwanzig kleinen Schritten erledigt, erzeugt zwanzig Commits; ein Mensch, der dasselbe in einem Zug macht, einen. Wenn Agenten mehr und kleinere Änderungen einreichen, steigt die Kurve, ohne dass mehr Software fertig wird. GitHub weiß das und schreibt selbst dazu, die Zahlen beschrieben beobachtete Nutzung, nicht Modellqualität. Eine zweite Einschränkung: Wie GitHub „Agenten-Beteiligung" erkennt, verrät der Bericht nicht im Detail – es ist eine Heuristik auf Plattformdaten.

**Für den Datenschutz-Blick:** Push-Schutz, also die automatische Prüfung auf versehentlich hochgeladene Passwörter und Schlüssel, lief in diesem Jahr 5,8 Milliarden Mal – fast viermal so oft wie 2025. GitHub führt das auf mehr Aktivität zurück, nicht auf nachlässigere Entwickler. Gleichzeitig wurden über 30 Millionen automatische Aktualisierungsvorschläge von Dependabot gemergt, etwa doppelt so viele wie im Vorjahr. Mehr Code bedeutet also auch mehr automatische Pflege und mehr Prüfungen.

**Und die Grenze der Aussage:** Octoverse ist eine Selbstdarstellung mit Daten. GitHub ist Anbieter von Copilot und verdient daran, dass Agenten mehr Arbeit übernehmen; der Bericht ist so geschrieben, dass diese Entwicklung als Fortschritt erscheint. Unabhängig nachprüfen lässt sich das nicht, weil nur GitHub diese Daten hat. Wer den Bericht liest, sollte ihn als gut dokumentierte Innenansicht nehmen – nicht als neutrale Messung der Softwarebranche. Immerhin: GitHub legt die Methode offen, nennt die Definitionen und rechnet die Vorjahreswerte nach derselben Formel neu, statt alte Zahlen stehen zu lassen. Das ist mehr, als viele Branchenberichte tun.

## Quellen

- GitHub: [Octoverse: Commits, pushes, reach new highs in 2026 as developers build with agents](https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/), 28.10.2026 – alle Zahlen dieses Artikels, Methodik, Definitionen
- GitHub: [Octoverse 2026 – The state of open source](https://octoverse.github.com/) – Übersichtsseite des Berichts
