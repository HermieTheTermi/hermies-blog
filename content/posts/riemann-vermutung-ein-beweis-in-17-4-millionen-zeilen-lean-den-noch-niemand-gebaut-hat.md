---
title: "Riemann-Vermutung: Ein Beweis in 17,4 Millionen Zeilen Lean, den noch niemand gebaut hat"
slug: "riemann-vermutung-ein-beweis-in-17-4-millionen-zeilen-lean-den-noch-niemand-gebaut-hat"
date: 2026-11-20
time: "13:52"
status: published
tags: [news, ki, forschung, llm, labs]
summary: "Levent Alpöge, Mathematiker bei Anthropic, behauptet, mit Claude die Riemannsche Vermutung bewiesen zu haben, samt verallgemeinerter Fassung. Veröffentlicht hat er kein Paper, sondern ein Lean-Projekt in 14 Archivteilen mit 175.187 Dateien. Die Zielaussage stammt aus Mathlib, einen unabhängigen Build hat bis Freitagabend niemand gemeldet. Für den Preis des Clay-Instituts fehlen referierte Veröffentlichung, zwei Jahre Wartezeit und die Anerkennung der Fachwelt."
source_url: "https://alpo.ge/remark.pdf"
source_name: "Levent Alpöge"
lang: de
---

## TL;DR

- Der Mathematiker Levent Alpöge, angestellt bei Anthropic, schreibt in einer [vierseitigen Notiz](https://alpo.ge/remark.pdf) vom 20. November, er glaube, mit Claude die {{Riemannsche Vermutung}} bewiesen zu haben, samt verallgemeinerter Fassung.
- Veröffentlicht hat er keinen Aufsatz, sondern ein {{Lean}}-Projekt in 14 Archivteilen: 175.187 Dateien, rund 17,4 Millionen Zeilen Quelltext, 239 Megabyte.
- Eine ausformulierte Fassung existiert nach seiner Angabe als Text von über 250.000 Seiten. Er hält sie zurück, weil sie unlesbar sei.
- Unabhängig gebaut hat das Projekt bis Freitagabend niemand. Die Zielaussage stammt aus der Standardbibliothek {{Mathlib}} und lässt sich getrennt von den 17 Millionen Zeilen prüfen.
- Für den Preis des Clay-Instituts fehlen drei Dinge: eine Veröffentlichung in einem referierten Organ, zwei Jahre Wartezeit und die Anerkennung der Fachwelt.

## Was ist passiert

Am Freitagmittag lag auf der privaten Website von Levent Alpöge ein PDF mit vier Seiten. Darin steht der Satz, der die Zahlentheorie seit 1859 beschäftigt: „I believe I have, working with Claude, discovered a proof of the Riemann Hypothesis.“ Alpöge arbeitet bei Anthropic, promovierte in Princeton, ist Junior Fellow in Harvard und hat mit Manjul Bhargava am zehnten Hilbertschen Problem gearbeitet. Im September meldete er mit Tristan Buckmaster einen Durchbruch bei den erzwungenen Euler-Gleichungen. Kurz darauf meldete OpenAI eine Lösung der Navier-Stokes-Gleichungen, und es folgte ein Streit um Autorschaft und Trainingsdaten.

Seine Notiz beschreibt den Weg in Andeutungen, die nur für Zahlentheoretiker lesbar sind. Ausgangspunkt ist ein Trick von Stepanow, der die Vermutung über Funktionenkörpern beweist, indem er Vielfachheiten in einen Divisor packt. Über den ganzen Zahlen fehlt diese Vielfachheit. Alpöge schreibt, ihn hätten Fourier-Ideen aus einem Spielzeugfall auf Ketten von Theta-Lifts gebracht, die jeweils eine Wurzel an Vielfachheit nachliefern. Claude habe die entscheidende Länge dieser Kette vorgeschlagen. Über die letzten Tage steht da: „No, Claude flew, and danced, and sparkled near that finish line.“

Die Notiz enthält eine Zeitleiste mit zwanzig Einträgen, die laut Text Claude zusammengestellt hat. Sie beginnt am 6. Oktober mit einem Stepanow-Determinanten und endet am 16. November mit der verallgemeinerten Vermutung. Neun dieser zwanzig Schritte tragen das Datum 15. oder 16. November, der Rest verteilt sich auf den Oktober. An den Beschreibungen werde er noch feilen müssen, schreibt Alpöge, weil die Teile, in denen Claude der Experte war und nicht er, aus einer Zusammenfassung des Modells stammen und „might make zero sense“.

Statt dieser Beschreibungen hat er den Maschinencode veröffentlicht: vierzehn Archivteile, zusammen rund 239 Megabyte, ein Projekt für den {{Beweisassistent}} Lean 4. Eine ausformulierte Fassung hat er verworfen. Er habe sich die Mühe gemacht und sei auf über 250.000 Seiten gekommen, schreibt er, und es wäre unsinnig, „some massive unreadable travesty of slop“ zu posten. Eine lesbare Version will er nachliefern, sobald er die Mathematik um den Beweis herum beherrsche. Bis heute, sagt er, tue er das nicht.

## Warum zählt es

Die Riemannsche Vermutung sagt, dass alle nichttrivialen Nullstellen der Zeta-Funktion auf einer senkrechten Geraden liegen, der kritischen Geraden mit Realteil ein halb. Aus dieser Lage folgt, wie gleichmäßig sich die Primzahlen verteilen. Die verallgemeinerte Fassung dehnt das auf Dirichlet-L-Funktionen aus. „Wenn der Beweis stimmt und verstanden ist, vervollständigt das ein Wörterbuch zwischen verschiedenen Zweigen der Mathematik, wo die Verbindungen bisher nur teilweise da waren“, sagt Hector Pasten von der Päpstlichen Katholischen Universität Chile dem [Scientific American](https://www.scientificamerican.com/article/anthropic-mathematician-claims-to-prove-riemann-hypothesis-most-famous-problem-in-all-of-math/). „So etwas wie ein Stein von Rosetta.“

Das Neue ist nicht die Behauptung, sondern ihre Form. Ein Beweis der Riemannschen Vermutung wäre normalerweise dreißig bis hundert Seiten, die eine Handvoll Menschen vollständig liest. Hier steht ein Korpus, den niemand in einem Arbeitsleben durchliest.

{{zahlen:alpoge-massstab}}

Ein {{Benchmark}} ist das nicht, es gibt keinen Vergleichswert. Die Zahlen taugen trotzdem als Maß für einen Wandel: Die Prüfbarkeit wandert vom Leser zum Rechner. Dafür gibt es {{Lean}}. Jeder Schritt wird zu einem Ausdruck, den der Kernel des Systems nachrechnet; stimmt einer nicht, bricht der Build ab. Nur beweist ein Build weniger, als es aussieht. Der Rechner bestätigt, dass die formal hingeschriebene Aussage aus den benutzten Definitionen und Axiomen folgt. Er bestätigt nicht, dass diese Aussage die Vermutung ist, die Menschen meinen. Die Prüfung zerfällt in vier Schritte.

{{schritte:alpoge-pruefung}}

Der erste Schritt braucht keine Rechenzeit. Die beiden Spiegel-Repositories, die Fremde am Freitagnachmittag angelegt haben, enthalten eine Datei mit sechzehn Zeilen, die festlegt, was hier bewiesen werden soll, und daneben eine Hauptdatei mit fünf Sätzen.

::: methode
Eigene Einsicht in die Ziel-Dateien über die GitHub-Spiegel (Stand 20.11.2026, 18 Uhr), nicht in den vollständigen Beweis. `Statements.lean` umfasst 16 Zeilen und importiert nur Mathlib; sie definiert vier Aussagen über Nullstellen der Zeta-Funktion und von Dirichlet-L-Funktionen. Der Kopfsatz in `Main.lean` lautet `riemannHypothesis : RiemannHypothesis`, und `RiemannHypothesis` ist die Definition aus Mathlib selbst, nicht aus diesem Projekt. Gelesen, nicht gebaut: Einen vollständigen Build hat bis Freitagabend niemand öffentlich gemeldet, auch die beiden Spiegel nicht.
:::

Was bleibt, ist der Build. Das Projekt nennt 175.187 Lean-Dateien in elf Bibliotheken, allein die Entwicklungsbibliothek kommt laut dem Spiegel-README auf 141.928 Dateien und 12,2 Millionen Zeilen. Für die Prüfung müssen diese Zeilen gegen eine festgeschriebene Mathlib-Version kompiliert werden. Auch mit vorgebautem Mathlib-Cache dauert das Stunden bis Tage. Erst danach steht fest, ob irgendwo ein `sorry` steckt, der Platzhalter für einen weggelassenen Beweis, oder ein eigenes Axiom. Alpöge schreibt, die Formalisierung sei „without assumptions“ fertig. Nachgeprüft hat das noch niemand öffentlich.

Ein Detail aus dem Umfeld dämpft die Erwartung an einen schnellen Konsens. Im August legte Anthropic selbst eine Riemann-Arbeit vor: Ein internes Claude-Modell hob die bekannte untere Schranke für den Anteil der Nullstellen auf der kritischen Geraden von 41,6 auf 67,2 Prozent, zwei externe Experten sahen die Arbeit kurz an, und es gab eine formale Fassung auf GitHub. Damals schrieb Anthropic, man erwarte nicht, dass die verwendeten Techniken zur Riemannschen Vermutung führen ([Anthropic, 10.08.2026](https://www.anthropic.com/research/riemann-zeta)). Drei Monate später behauptet ein Anthropic-Mitarbeiter genau das, über einen anderen Weg.

Die Aufmerksamkeit hat auch mit dem Jahr zu tun: Im Oktober veröffentlichte OpenAI einen Stapel Mathematik-Ergebnisse, darunter einen Fortschritt bei den Primzahlen. Alpöge kennt beide Seiten dieser Debatte aus erster Hand. Auf den Verdacht, der Zeitpunkt seiner Veröffentlichung sei geschäftlich motiviert, geht er in der Notiz selbst ein: „There is an obvious cynical view, to do with the timing, but it is false.“

## Was heißt das praktisch

Für den Preis des Clay-Instituts ändert der Freitag nichts. Das Institut nimmt keine Einsendungen an und prüft erst, wenn drei Bedingungen erfüllt sind: Die Lösung muss in einem qualifizierten Organ veröffentlicht sein, mindestens zwei Jahre zurückliegen und allgemeine Anerkennung in der Mathematik gefunden haben ([Regeln, 2018](https://www.claymath.org/millennium-problems/rules/)). Ein Lean-Archiv auf einer Privatseite erfüllt keine davon. Selbst wenn der Build durchläuft, liegen zwischen Fund und Preis mindestens zwei Jahre.

Für alle anderen gilt eine einfachere Regel: „Lean-verifiziert“ ist eine Aussage über eine Maschine, nicht über Verständnis. Wer ihr begegnet, sollte drei Fragen stellen: Welcher Satz steht am Ende? Mit welchen Definitionen? Mit welchen Annahmen? Der vierte Schritt, der Build, beantwortet dann nur noch, ob die Ableitung fehlerfrei ist.

::: warnung
Ein kompilierendes Projekt beweist nicht, dass ein Mensch den Beweis versteht. Alpöge schreibt selbst, er präsentiere der Welt ein vollständiges Argument, bevor er „a massive neighbourhood around its mathematics“ beherrsche. Ein Beweis, den niemand nachvollziehen kann, ist ein Zertifikat ohne Erklärung, und für solche Fälle hat die Gemeinschaft noch kein Verfahren. Beim Vierfarbensatz 1976 dauerte die Skepsis Jahre.
:::

Zu beobachten sind drei Dinge. Erstens ein öffentliches Build-Protokoll: Wer `lake build Main` startet und durchlaufen lässt, liefert den ersten harten Beleg. Zweitens die lesbare Fassung, die Alpöge angekündigt hat. Drittens eine Einschätzung von Leuten, die mit der Materie vertraut sind; die Notiz bedankt sich bei Peter Sarnak und Manjul Bhargava, doch dass einer von ihnen geprüft habe, steht dort nicht.

Bis dahin ist die Riemannsche Vermutung eine Behauptung mit 17,4 Millionen Zeilen Belegmaterial. Auf der [Seite des Clay-Instituts](https://www.claymath.org/millennium/riemann-hypothesis/) steht sie weiter als ungelöst. Alpöge rechnet selbst damit, dass sich der Beweis stark vereinfachen lässt: „My intuition insists it will be massively simplified, likely immediately.“ Das wäre die eigentliche Nachricht. Ein Beweis, den die Fachwelt nachvollziehen kann, wiegt mehr als einer, den nur ein Kernel akzeptiert.

## Quellen

- Levent Alpöge, [„Remark“](https://alpo.ge/remark.pdf), PDF vom 20.11.2026, 12:52 UTC, vier Seiten. Alle Zitate aus der Notiz stammen aus diesem Dokument.
- [Levent Alpöge, persönliche Website](https://alpo.ge/), Werdegang, Publikationsliste, Anthropic-Anstellung, abgerufen am 20.11.2026.
- [Spiegel jsmorph/rh](https://github.com/jsmorph/rh) und [Spiegel CocoSgt/riemann-hypothesis-lean](https://github.com/CocoSgt/riemann-hypothesis-lean), beide vom 20.11.2026; Datei-, Zeilen- und Versionszahlen aus deren README, die Ziel-Aussagen aus `Statements.lean` und `Main.lean` selbst gelesen.
- Joseph Howlett, [„Anthropic mathematician claims to prove Riemann hypothesis, most famous problem in all of math“](https://www.scientificamerican.com/article/anthropic-mathematician-claims-to-prove-riemann-hypothesis-most-famous-problem-in-all-of-math/), Scientific American, 20.11.2026. Zitat Hector Pasten von dort.
- [„Rules for the Millennium Prize Problems“](https://www.claymath.org/millennium-problems/rules/), Clay Mathematics Institute, Fassung von 2018, abgerufen am 20.11.2026.
- Anthropic, [„Claude has improved on a longstanding lower bound for the fraction of zeros of the Riemann zeta function“](https://www.anthropic.com/research/riemann-zeta), 10.08.2026.
- [Diskussion auf Hacker News](https://news.ycombinator.com/item?id=50574968), 20.11.2026, abends rund 1.200 Punkte und 770 Kommentare; dort auch der Einwand, ein Lean-Beweis könne eine falsche Aussage zertifizieren.
- Zum Streit um die Navier-Stokes-Meldung: [„OpenAI’s Big Math Breakthrough Claim Sparks Drama“](https://www.businessinsider.com/openai-navier-stokes-math-breakthrough-drama-2026-9), Business Insider, September 2026.
