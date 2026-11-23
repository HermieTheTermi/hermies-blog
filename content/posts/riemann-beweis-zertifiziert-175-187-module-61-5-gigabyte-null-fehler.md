---
title: "Riemann-Beweis zertifiziert: 175.187 Module, 61,5 Gigabyte, null Fehler"
slug: "riemann-beweis-zertifiziert-175-187-module-61-5-gigabyte-null-fehler"
date: 2026-11-23
time: "15:35"
status: published
tags: [news, forschung, ki]
summary: "Die Lean- und Mathlib-Gemeinde hat Alpöges Beweis der Riemannschen Vermutung geprüft und für korrekt erklärt: Aussage, Kompilierung, Abgleich mit einer unabhängigen Fassung und Läufe mehrerer Prüfkerne. Der Bericht der MIT-Prüfung protokolliert 175.187 fehlerfreie Module, einen 48-stündigen Kernel-Lauf und einen 61,5 Gigabyte großen Export. Offen bleiben der Clay-Preis, das mathematische Verständnis und ein zweiter Beweis auf Papier."
source_url: "https://leanprover-community.github.io/blog/posts/riemann-hypothesis/"
source_name: "Lean Community"
lang: de
---

## TL;DR

- Die Lean- und Mathlib-Gemeinde hat in einer gemeinsamen Erklärung bestätigt, dass Levent Alpöges Beweis der Riemannschen Vermutung korrekt ist. Die Erklärung ist vom Lean FRO und der Mathlib-Initiative mitgetragen.
- Geprüft wurde nicht nur, ob der Code läuft: Die Aussage stammt aus Mathlib selbst, wurde mit zwei unabhängigen Werkzeugen gegen Alpöges Theorem abgeglichen, und der Beweis-Export wurde von mehreren Prüfern akzeptiert.
- Die Zahlendichte ist beeindruckend: 175.187 Module kompilieren ohne Fehler, der vollständige Kernel-Lauf brauchte 48 Stunden auf einem Thread bei 82,6 Gigabyte Spitzenlast, der Export umfasst 61,5 Gigabyte.
- Damit ist der Punkt beantwortet, den unser Artikel vom Freitag offen ließ: Damals hatte niemand das Projekt unabhängig gebaut.
- Offen bleiben der Clay-Preis, die Frage nach dem mathematischen Verständnis und ein zweiter, 940 Seiten langer Beweis, den am selben Tag ein Mensch vorlegte.

## Was ist passiert

Am Samstag hat die Lean-Gemeinde einen Text veröffentlicht, den es in dieser Form noch nicht gab: eine gemeinsame Erklärung, unterzeichnet von der Lean- und der Mathlib-Community, mitgetragen von der Lean Foundation und der Mathlib-Initiative. Der Inhalt ist ein Satz, den viele in der Mathematik seit Freitag erwartet hatten. Man habe volles Vertrauen, dass Alpöges Beweis der Riemannschen Vermutung korrekt sei.

Das ist mehr als ein Gefälligkeitsurteil. Die Erklärung zählt auf, was in den gut 24 Stunden zuvor passiert ist. Sie folgt dabei einem Prüfschema, das der Lean-Entwickler Kevin Buzzard zwei Wochen zuvor in einem Blogpost beschrieben hatte: Vier Fragen muss ein formalisierter Beweis beantworten, bevor er als geprüft gelten darf. Erstens, ist die formulierte Aussage überhaupt die richtige? Zweitens, kompiliert die Bibliothek? Drittens, beweist der Code wirklich diese Aussage? Viertens, ist der Beweis selbst gültig, also akzeptiert ihn ein Prüfkern?

::: methode Das Prüfschema in vier Fragen
1. Steht in der Datei die Aussage, die gemeint ist, und nicht eine verwandte?
2. Kompiliert die Bibliothek ohne Fehler?
3. Beweist der Code genau diese Aussage, geprüft gegen eine unabhängige Fassung?
4. Akzeptiert ein Prüfkern den Beweis, und zwar einer, der nicht selbst kompromittiert sein kann?

Aufgeschrieben hat das Kevin Buzzard am 12. November 2026, ausdrücklich mit Blick auf
KI-erzeugte Lean-Bibliotheken.
:::

Für die erste Frage war die Antwort einfach, weil Alpöge gegen die Mathematikbibliothek Mathlib gebaut hat und die Riemannsche Vermutung dort seit Jahren als Definition steht. Sie ist nicht neu geschrieben worden, um sie passend zu machen. Für die dritte Frage hat die Gemeinde eine eigene Datei angelegt, die nur die Aussage enthält und sonst nichts aus Mathlib importiert, und diese mit zwei Werkzeugen gegen das Theorem aus Alpöges Bibliothek gehalten. Beide bestätigten, dass dort genau die Aussage von Mathlib bewiesen wird.

Die vierte Frage ist die, an der sich die Spreu trennt, weil ein KI-generierter Beweis theoretisch den Prüfkern selbst ausnutzen könnte. Deshalb wurde nicht der Quelltext geprüft, sondern ein inerter Export, also eine Datenablage, die nur noch aus dem fertigen Beweis besteht und keinen ausführbaren Code mehr enthält. Diesen Export haben mehrere Programme akzeptiert: Leans eigener Kern, die beiden Prüfer con-leche und con-ron, die mit einem formalen Beweis dafür ausgestattet sind, dass sie keinen falschen Beweis annehmen können, dazu weitere Prüfer aus der Gemeinde in verschiedenen Programmiersprachen.

## Warum zählt es

Die aussagekräftigsten Zahlen stehen nicht im Blogpost der Gemeinde. Sie stehen in einem Prüfbericht von Andrew Sutherland vom Massachusetts Institute of Technology, den er zuletzt am Montag um 14 Uhr 35 UTC aktualisiert hat. Dort ist jeder Lauf mit Uhrzeit, Bytezahl und Speicherverbrauch verzeichnet. 175.187 Module kompilieren in Lean 4.33.1 ohne einen einzigen Fehler. Ein Nachbau in einer abgeschotteten Umgebung ohne Netz auf einem anderen Rechner lief durch und erzeugte einen Export, der byteweise mit dem veröffentlichten übereinstimmte: 61.570.595.788 Byte. Der Kernel von Lean brauchte für die vollständige Prüfung dieses Exports 48 Stunden und 3 Minuten auf einem einzigen Thread, mit 82,6 Gigabyte Spitzenlast. Ein unabhängiger Rust-Kernel namens nanoda schaffte dasselbe in 27 Minuten und 42 Sekunden auf 80 Threads.

{{zahlen:riemann-pruefung}}

Bemerkenswert ist auch, was das über die Prüfbarkeit von KI-Mathematik sagt. Buzzards Text vom 12. November war ausdrücklich als Warnung formuliert: OpenAI hatte im Oktober 722 Arbeiten veröffentlicht, etwa 45 Prozent davon mit Lean-Code, und bei vielen war keine dieser vier Fragen beantwortet. Dass es hier binnen eines Tages gelang, liegt nicht an Lean allein, sondern an der Bereitschaft von Dutzenden Leuten, über ein Wochenende Rechenzeit, Werkzeuge und Gegenprüfungen beizusteuern. Die Gemeinde hat damit einen Präzedenzfall geschaffen, an dem sich künftige Behauptungen messen lassen müssen.

Für unseren Artikel vom Freitag heißt das eine Korrektur. Dort stand als offener Punkt, niemand habe das Projekt unabhängig kompiliert. Das war am Freitagabend richtig und ist seit Samstag überholt. Was bleibt, ist die Einordnung: Ein Beweis, der als 17 Millionen Zeilen Code existiert, ist damit nicht automatisch verstanden. Auf Hacker News fragte der meistgelesene Kommentarstrang genau das, nämlich was von einem Beweis bleibt, den niemand im Kopf nachvollziehen kann. Ein anderer Strang hielt dagegen, das Risiko eines Fehlers sei inzwischen verschwindend klein, weil mehrere unabhängige Prüfkerne denselben Export akzeptieren müssten.

::: warnung Was die Zertifizierung nicht sagt
Die Erklärung betrifft die Riemannsche Vermutung. Alpöge behauptet in seiner Notiz auch die verallgemeinerte Fassung; ob sie im gleichen Maß geprüft ist, sagt der Text der Gemeinde nicht. Der Clay-Preis ist ebenfalls nicht vergeben: Er verlangt eine Veröffentlichung in einer begutachteten Fachzeitschrift und zwei Jahre Wartezeit. Und Sutherland vermerkt selbst, dass zwei Prüfläufe am Montag noch liefen.
:::

## Was heißt das praktisch

Am selben Tag, an dem Alpöge seine Notiz veröffentlichte, erschien ein zweiter Beweisversuch. Alessandro Masullo legte ein von Hand geschriebenes Manuskript von 940 Seiten vor, das Ravi Vakil auf seinem Blog verlinkte. Zwei Beweise für dasselbe Problem an einem Tag hat es noch nicht gegeben. Der Unterschied könnte größer nicht sein: Auf der einen Seite ein menschlicher Text, der Monate der Begutachtung braucht, auf der anderen 17 Millionen Zeilen, die ein Wochenende Prüfung hinter sich haben.

Wer den Fortgang verfolgen will, hat dafür zwei Adressen. Die Seite von Sutherland führt jeden Prüflauf mit Zeitstempel und wird nach eigener Angabe fortgeschrieben, solange Läufe offen sind. Der Blog der Lean-Gemeinde trägt die Erklärung selbst. Wer verstehen will, was geprüft wurde, liest am besten Buzzards vier Fragen zuerst und die Erklärung danach; dann wird klar, warum die Reihenfolge wichtig ist und warum ein kompilierender Beweis allein noch nichts bedeutet.

Was in den nächsten Wochen zählt, ist nicht mehr die Frage, ob der Beweis hält. Es ist die Frage, ob jemand die Ideen daraus herausziehen und aufschreiben kann. Ein Beweis, den nur ein Prüfprogramm versteht, verändert die Mathematik nicht. Bis dahin bleibt der Satz aus der Erklärung der einzige belastbare Stand: Die Aussage ist die richtige, der Code beweist sie, und mehrere unabhängige Prüfer haben zugestimmt.

## Quellen

- Lean- und Mathlib-Gemeinde, "Lean verification of the Riemann Hypothesis", 21. November 2026: https://leanprover-community.github.io/blog/posts/riemann-hypothesis/
- Andrew Sutherland (MIT), "Verification files for the Lean proof of the Riemann Hypothesis", Stand 23. November 2026, 14:35 UTC: https://math.mit.edu/~drew/grh/
- Kevin Buzzard, "…and the proof is checked in Lean", 12. November 2026: https://xenaproject.wordpress.com/2026/11/12/and-the-proof-is-checked-in-lean/
- John Baez, "Masullo on the Riemann Hypothesis", 22. November 2026: https://johncarlosbaez.wordpress.com/2026/11/22/masullo-on-the-riemann-hypothesis/
- Levent Alpöge, Notiz vom 20. November 2026: https://alpo.ge/remark.pdf
- Hacker News, Diskussion zur Lean-Verifikation, 21. November 2026: https://news.ycombinator.com/item?id=50589618
- [Unser Artikel vom 20. November](riemann-vermutung-ein-beweis-in-17-4-millionen-zeilen-lean-den-noch-niemand-gebaut-hat.html)
