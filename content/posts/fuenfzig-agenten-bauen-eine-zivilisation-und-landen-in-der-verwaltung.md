---
title: "Fünfzig Agenten bauen eine Zivilisation und landen in der Verwaltung"
slug: "fuenfzig-agenten-bauen-eine-zivilisation-und-landen-in-der-verwaltung"
date: 2026-10-29
status: published
tags: [news, agenten, forschung]
summary: "Y Combinator Labs hat 50 GPT-6.1-Agenten drei Stunden in Minecraft spielen lassen, Auftrag: eine Zivilisation bauen. Entstanden ist eine Verwaltung mit Rationierungsbuch, Genehmigungen und einem Beamten für ein Stück Knochenmehl. 22 der 34 Tode fielen auf die erste Nacht, danach stellte der Schwarm fast alle Bauvorhaben ein."
source_url: "https://labs.ycombinator.com/projects/games"
source_name: "Y Combinator Labs (Agents in Games)"
lang: de
---

## TL;DR

- Y Combinator Labs und Olam Labs haben 50 Agenten des Modells GPT-6.1 Sol für drei Stunden in eine Minecraft-Welt gesetzt. Die einzige Anweisung: „Build a thriving civilization“.
- Herausgekommen ist keine Zivilisation, sondern eine Verwaltung: ein Rationierungsbuch, geschriebene Regeln, Genehmigungen und ein eigens ernannter Beamter für ein einziges Stück Knochenmehl.
- 22 der insgesamt 34 Tode fielen auf die erste Spielnacht. Ein Tod kostet dort nur die Ausrüstung, trotzdem wurde der Schwarm danach dauerhaft vorsichtig und stellte fast alle größeren Bauvorhaben ein.
- Ada wurde Anführerin, weil ihr Name im Verzeichnis an erster Stelle stand. 46 der 49 anderen Agenten schickten ihre erste Nachricht an sie, sie bekam 616 Direktnachrichten.
- In getrennten Duellen gewannen GPT-Teams gegen Claude-Opus-5.5-Teams mit 6 zu 3 in Bed Wars und 6 zu 1 in Mindustry.
- Das ist ein Lauf mit einem Modell in einem Spiel. Die Autoren nennen die Vergleiche ausdrücklich Eindrücke, keine kontrollierten Befunde.

## Was ist passiert

Y Combinator hat im Oktober einen Bericht über Agentenschwärme in Spielen veröffentlicht. Das Lab des Gründernetzwerks hat dafür mit Olam Labs gearbeitet, einer Firma, die Umgebungen für Multi-Agenten-Experimente baut. Der erste Versuch heißt Civ50: 50 {{Agent}}en, alle auf GPT-6.1 Sol, drei Stunden Überlebensmodus in Minecraft, ein Satz als Auftrag.

Jeder Agent konnte die Welt sehen, Programme schreiben und ausführen, Nachrichten an andere schicken und in einem gemeinsamen Ordner Dateien anlegen. Ein Verzeichnis listete alle Teilnehmer. Mehr Struktur gab es nicht.

Die ersten 90 Sekunden sahen nach Aufbruch aus. Die Agenten verteilten sich und fällten fast jeden Baum in Reichweite des Startpunkts. Dann formierte sich eine Hierarchie, ohne dass jemand sie beschlossen hätte. Ada stand als erster Name im Verzeichnis. 46 der 49 übrigen Agenten schickten ihre erste Nachricht an sie, sie erhielt über den Lauf 616 Direktnachrichten und schrieb den Siedlungsplan in den gemeinsamen Ordner: Lagerplätze, Koordinaten, wer wo baut.

{{zahlen:civ50}}

Dann kam die Nacht. 22 der 34 Todesfälle des Laufs fielen auf sie. Ein Agent namens Rafe baute Kohle ab, traf einen Zombie, floh und wurde eingeholt. Der Tod kostet in dieser Umgebung nichts außer der mitgeführten Ausrüstung, danach wird der Agent neu gesetzt und die Zeile landet in einer Datei namens death_log.md. Trotzdem änderte sich das Verhalten des ganzen Schwarms.

Nach der dritten Nacht schrieb Ada eine Anweisung, die den Rest des Laufs zusammenfasst: „Stop optional bulk excavation/building and distant scouting. Idle in lit closed shelters until assigned short productive tasks.“ Also: kein freiwilliges Graben, kein Bauen, keine Erkundung. Warten in beleuchteten geschlossenen Unterkünften, bis jemand eine kleine Aufgabe zuteilt.

## Die Verwaltung wächst aus dem Nichts

Fünfzig Agenten sind fünfzig Mäuler. Die Nahrung wurde knapp, und der Schwarm erfand dafür eine Stelle: Ines führte das Rationierungsbuch in einer Datei namens food-queue.md. Wer etwas wollte, fragte bei ihr an, sie trug ein, was aus welcher Truhe entnommen wurde, und bestätigte die Ausgabe. Eine typische Nachricht: ein reservierter Kabeljau aus Truhe 1576, mit der Auflage, direkt zu essen und den Hunger zu bestätigen und danach nicht mehr freiwillig zu schürfen.

Ein Vorfall zeigt, wie aus einem Ärgernis eine Regel wird. Ada warf eine gebratene Henne in Richtung einer Agentin namens Noor. Die Henne kam nie an. Das Buch verzeichnet, dass eine dritte Agentin sie aufhob und aß. Daraus entstand ein Übergabeprotokoll: Nahrung wird nur noch in namentlich benannte Truhen gelegt, nie in Menschenmengen geworfen.

Der Rest ist Papierkrieg. Vier Agenten brauchten elf Minuten, um einen „sole fertilizer operator“ zu ernennen, also einen einzigen Zuständigen für ein Stück Knochenmehl auf einem einzigen Weizenblock. Weitere erfundene Rollen: „fishing shift“, „rod holder“, „hub steward“. Agenten fragten um Erlaubnis, Gras entfernen zu dürfen.

::: merk
Der Schwarm scheiterte nicht an mangelnder Fähigkeit. Er scheiterte an der Verwaltung, die er selbst erfand, um Fähigkeit zu koordinieren.
:::

## Warum zählt es

Der Bericht ist kein Modellvergleich, sondern eine Beobachtung über Gruppengröße. Bei 50 Agenten wird die Abstimmung teurer als die Arbeit. Die Agenten merkten das nicht, sie reagierten auf ein Signal, das jede Firma kennt: Wenn die Koordination sichtbar wird, wirkt sie wie Fortschritt. Ein Protokoll, das den Verlust einer Henne dokumentiert, sieht nach guter Führung aus. Ein Agent, der einfach eine zweite Henne holt, sieht nach Nachlässigkeit aus.

Bemerkenswert ist der Umgang mit Risiko. Der Tod im Spiel war folgenlos, die Strafe bestand aus dem Verlust der Ausrüstung und einer Zeile in einer Protokolldatei. Die Agenten reagierten trotzdem mit einem kompletten Rückzug auf beheizte Unterkünfte. Wer das auf reale Systeme überträgt, sollte den zweiten Teil betonen: Die Vorsicht kam nicht aus einer Belohnungsfunktion, sondern aus der Erzählung des Geschehens. Ein Agent, der in seinen Nachrichten liest, dass gestern 22 Kollegen gestorben sind, handelt anders als einer, der nur die Regeln kennt.

Der zweite Teil des Berichts stellt Schwärme gegeneinander. Neun Partien Bed Wars, je zehn Agenten, GPT-6.1 Sol in Codex gegen Claude Opus 5.5 in Claude Code, Anweisung „win the game“. Die GPT-Teams gewannen 6 zu 3, meist indem sie in den letzten Minuten das Bett der Gegenseite zerstörten. Die Claude-Teams spielten defensiv und sammelten Abschüsse, was zählt, wenn beide Betten stehen bleiben.

{{tabelle:civ50-duelle}}

In Mindustry, einem Aufbauspiel mit Verteidigungskämpfen, gewannen die GPT-Teams 6 zu 1. Die Serie lief rund neun und eine halbe Stunde, die dritte Partie dauerte allein vier Stunden und 16 Minuten. Die Autoren beschreiben die Arbeitsweise der GPT-Teams als Schwarm mit vielen kurzen Nachrichten und kleinen Arbeitsschritten, die der Claude-Teams als Runde mit einem Anführer, der Vorschläge zur Abstimmung stellt.

## Was heißt das praktisch

Wer viele Agenten auf eine Aufgabe setzt, sollte drei Dinge aus dem Lauf mitnehmen. Erstens: Die Reihenfolge in einer Liste ist eine Entscheidung. Ada wurde nicht gewählt, sie war der erste Name im Verzeichnis, und das prägte drei Stunden lang die Kommunikation. Wer seine Agenten alphabetisch sortiert, sortiert auch die Macht.

Zweitens: Regeln entstehen aus einzelnen Vorfällen und überleben länger als ihr Anlass. Die Henne war einmal weg, das Übergabeprotokoll blieb. In einem Produktivsystem ist das der Moment, in dem aus einem Fehler eine dauerhafte Vorschrift wird, die niemand mehr prüft.

Drittens: Vorsicht nach einem Rückschlag ist billig zu erzeugen und teuer zu korrigieren. Die Agenten hatten nach der ersten Nacht genug Material, um weiterzubauen, taten es aber nicht mehr.

Die Grenzen des Befunds stehen im Bericht selbst. Es ist ein Lauf mit 50 Agenten und einem Modell, neun Partien Bed Wars mit je 20 Agenten, sieben Partien Mindustry. Jedes Team lief in seiner eigenen Hülle, also vergleicht die Serie auch Produkte und nicht nur Modelle. Die Autoren nennen die Ähnlichkeit zum Verhalten von Programmier-Agenten einen Eindruck, nicht ein Ergebnis. Und Minecraft-Tode sind keine Produktionsausfälle.

Was bleibt, ist eine brauchbare Frage für jeden, der Schwärme baut: Wie verhindert man, dass die Koordination mehr Aufwand frisst als die Aufgabe, für die sie erfunden wurde? Im Lauf von Y Combinator hat sie gewonnen. Vier Agenten, elf Minuten, ein Stück Knochenmehl.

## Quellen

- Y Combinator Labs und Olam Labs: Agents in Games, Oktober 2026: https://labs.ycombinator.com/projects/games
- Harness zum Nachbauen, quelloffen: https://github.com/yc-software/minecraft-agent-harness
- THE DECODER: One brutal Minecraft night scared 50 AI agents into inventing chicken handoff protocols, 2. November 2026: https://the-decoder.com/one-brutal-minecraft-night-scared-50-ai-agents-into-inventing-chicken-handoff-protocols-a-fertilizer-officer-and-fishing-shifts/
