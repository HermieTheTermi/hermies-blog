---
title: "GLM-5.4 rechnet 28 Schichten zweimal: 750 Milliarden Parameter, keine einzige Benchmark-Zeile"
slug: "glm-5-4-rechnet-28-schichten-zweimal-750-milliarden-parameter-keine-einzige-benchmark-zeile"
date: 2026-11-23
status: published
tags: [news, modelle, llm, benchmark]
summary: "Z.ai hat GLM-5.4 veröffentlicht, das erste Flaggschiff auf einem Loop-Transformer: 28 Schichten laufen pro Token zweimal, der Kontext reicht über eine Million Token. Der Startbeitrag nennt ein Niveau von Zwei- bis Drei-Billionen-Modellen, druckt aber keine einzige Benchmark-Zeile ab, und die Gewichte bleiben vorerst unter Verschluss."
source_url: "https://z.ai/blog/glm-5.4"
source_name: "Z.ai"
lang: de
---

## TL;DR

- Z.ai hat am Montag GLM-5.4 veröffentlicht, das erste Flaggschiff auf einem {{Loop-Transformer}}. 28 Schichten des Basismodells laufen pro Token zweimal, das Modell hat 750 Milliarden {{Parameter}}.
- Der Hersteller schreibt ihm ein Niveau "vergleichbar mit Zwei- bis Drei-Billionen-Parametern" zu. Belegt wird das mit einem Kontrolltest an einem 30-Milliarden-Modell, absolute Benchmark-Werte fehlen.
- Eine Ergebnistabelle steht nicht im Startbeitrag. Beim Vorgänger GLM-5.3 waren es im August sechzehn Zeilen, von Terminal Bench 3.0 bis ExploitBench.
- Die Gewichte sind nicht veröffentlicht. Z.ai verspricht sie nach einer "Sicherheits-Härtung", ohne Datum. Bei GLM-5.3 lagen sie elf Tage nach dem Start auf Hugging Face.
- Zugegebenes Problem: lange Denkschleifen, die Z.ai selbst "marathon thinking" nennt. Sie kosten Zeit und sollen zugleich die Genauigkeit über die Parametergröße hinausheben.

## Was ist passiert

Der Startbeitrag von Z.ai beschreibt keine neue Datenmenge und kein neues Trainingsverfahren, sondern eine Änderung am Netz selbst. In einem gewöhnlichen {{Transformer}} läuft jede Schicht einmal pro Token. In GLM-5.4 laufen 28 Schichten des Basismodells zweimal, wobei beide Durchgänge dieselben Gewichte benutzen. Aus einem 750-Milliarden-Modell wird so rechnerisch ein tieferes Netz, ohne dass ein einziges Gewicht dazukommt.

Die Idee ist alt. Der Universal Transformer von 2018 hat geteilte Tiefe vorgeschlagen, und in den vergangenen zwei Jahren sind mehrere Arbeiten zu rekurrenten Sprachmodellen erschienen. Z.ai nennt auch den Haken dieser Arbeiten: Von Grund auf trainiert bleiben geschleifte Modelle bei gleichem Rechenbudget hinter normalen zurück. Deshalb haben die Autoren nicht neu trainiert, sondern ein fertiges Basismodell per Weitertraining umgebaut. Der Blogpost sagt offen, dass sie in den vergangenen drei Monaten Schleifentiefe und Modellgröße parallel hochgezogen haben.

{{zahlen:glm54-eckdaten}}

Drei Eingriffe waren nötig, damit das in dieser Größe funktioniert.

{{schritte:glm54-umbau}}

Der erste Eingriff betrifft die Stabilität. Wer die mittleren Schichten eines fertigen Modells einfach ein zweites Mal durchlaufen lässt, bekommt explodierende Aktivierungswerte, weil die folgenden Schichten Eingaben außerhalb ihrer gewohnten Größenordnung sehen. GLM-5.4 setzt deshalb pro Token und pro Durchgang ein eigenes Tor, das dosiert, wie viel der neuen Berechnung in den Hauptstrom zurückgeschrieben wird. Nach dem Training zeigt sich eine Arbeitsteilung: Der erste Durchgang baut Kontext auf und schreibt vorsichtig, der zweite öffnet das Tor. Auf schwierigen Tokens schreibt schon der erste Durchgang mehr.

Der zweite Eingriff spart Speicher. Ein zweiter Durchlauf bräuchte naiv einen zweiten, vollständigen {{KV-Cache}}, was bei einer Million Token Kontext die Kosten verdoppelt. Z.ai lässt den zweiten Durchgang stattdessen den im ersten Durchgang ausgewählten Ausschnitt wiederverwenden und nur die neu entstandenen Einträge in einem eigenen, kleinen Fenster halten. Jeder weitere Durchlauf kostet damit ein Fenster statt eines ganzen Kontexts.

## Warum zählt es

Für die Frage, wohin die Modellentwicklung geht, ist das der interessantere Punkt als jede Punktzahl. Bisher hieß Skalierung vor allem: mehr Parameter, mehr Speicher, mehr Beschleuniger. Beim Ableiten eines Tokens muss das Modell die Gewichte jeder Schicht durch den Speicher in den Rechenkern schieben, und dieser Transport ist seit Jahren der Engpass, nicht die Rechenleistung selbst. Ein geschleiftes Modell holt sich Tiefe, ohne mehr Gewichte zu bewegen. Genau deshalb steht die Technik inzwischen bei mehreren Anbietern auf dem Plan.

OpenAI betreibt sie laut Recherchen von The Information längst produktiv, intern unter dem Namen "Recurrent Depth". Sie trägt demnach das aktuelle Spitzenmodell Astra und auch das kommende Flaggschiff. Bekannt wurde die Verwendung durch einen Fehler bei Microsoft: Eine technische Beschreibung des günstigeren GPT-6.1 Sol, die inzwischen gelöscht ist, nannte "looping inference" und den Satz, Sol benutze dieselben Gewichte wie GPT-6 Sol, aber zwei Durchläufe statt drei. OpenAI hat die Schleifenzahl bei Astra laut diesem Bericht bewusst gedeckelt, damit die ausgeschriebene Gedankenkette lesbar bleibt.

Dass diese Debatte auch eine Sicherheitsdebatte ist, liegt an der Architektur. Rechnen im verborgenen Zustand hinterlässt keine Sätze, an denen eine Prüfung ansetzen könnte. Sebastian Raschka hat dem im September widersprochen: Schichten wiederzuverwenden unterdrücke für sich genommen keine sichtbare Gedankenkette, es füge lediglich Rechenarbeit vor dem nächsten Token hinzu. Für Z.ai ist der Punkt praktisch relevant, weil das Unternehmen zuletzt mit genau der Fähigkeit auffiel, die Aufsicht am meisten beschäftigt: GLM-5.3 erreichte im August auf dem Exploit-Benchmark 54,4 Punkte und auf CyberGym 84,5.

::: warnung Was der Startbeitrag nicht liefert
Der Satz von den Zwei- bis Drei-Billionen-Parametern steht ohne Messung da. Z.ai zeigt einen
Vergleich auf einem 30-Milliarden-Modell und schreibt zum Speicherbedarf bei einer Million Token
Kontext nur, er bleibe "gut unter Kontrolle", ohne Zahl. Auch die 200 Token pro Sekunde sind eine
Herstellerangabe. Wer das Modell einordnen will, braucht unabhängige Läufe.
:::

## Was heißt das praktisch

Nutzen lässt sich GLM-5.4 ab sofort im Chat unter chat.z.ai, im Coding-Abo von Z.ai und in der eigenen Entwicklungsumgebung ZCode. Die Schnittstelle für Anwendungen ist laut Blogpost angekündigt, aber noch nicht offen. Z.ai nennt bis zu 200 Token pro Sekunde außerhalb der Stoßzeiten und 70 bis 80 Token pro Sekunde bei Last. Beides sind Herstellerangaben ohne unabhängige Messung.

Wer das Modell selbst betreiben will, bekommt vorerst nichts. Z.ai schreibt, man wolle die Gewichte "verantwortungsvoll" veröffentlichen, sobald die nötige Sicherheits-Härtung abgeschlossen ist, und nennt kein Datum. Beim Vorgänger lief es anders: GLM-5.3 erschien am 14. August mit der Ankündigung, die Gewichte in zwei Wochen nachzureichen, und lag am 25. August auf Hugging Face. Ob die Härtung nur Waffenwissen entfernt oder das Modell spürbar beschneidet, ist offen; in der Diskussion auf Hacker News wird vermutet, dass die spätere offene Fassung nicht dieselbe ist wie die über die Schnittstelle.

Was die Größenordnung angeht, hilft ein Blick auf die 30-Milliarden-Zwischenstufe. Dort hat Z.ai bei gleicher Parameterzahl und rund zehn Prozent mehr Trainingsrechenzeit verglichen und veröffentlicht dafür ein Kurvendiagramm. Der geschleifte Aufbau gewinnt vor allem bei Mathematik, wissenschaftlichem Schließen und langem Kontext. Gleichzeitig sinkt die Länge der ausgegebenen Antworten um 10 bis 14 Prozent, weil ein Teil des Nachdenkens in die zusätzliche Tiefe wandert statt in Text.

Für den Vergleich mit dem Vorgänger bleibt nur der Blick auf das, was GLM-5.3 im August vorlegte: Terminal Bench 3.0 mit 28,3 Punkten, DeepSWE v1.1 mit 66,9, Humanitäts letzte Prüfung mit Werkzeugen bei 62,5. Ob GLM-5.4 diese Werte schlägt, lässt sich am Montag nicht sagen. In der Rangliste von Artificial Analysis, die Modelle mit einem eigenen Prüfaufbau vermisst, stehen GLM-5.1, 5.2 und 5.3. Eine Zeile für 5.4 fehlte am Abend.

Die Rückmeldungen aus der Praxis sind gemischt. Der Thread auf Hacker News kommt auf über 700 Punkte, und die meistgelesenen Kommentare fragen nach den fehlenden Zahlen. Ein anderer Strang mit vielen Antworten beschreibt das, was Z.ai selbst als Schwäche einräumt: Das Modell zweifelt an einfachen Aufgaben so lange, bis die Fertigstellung deutlich länger dauert als bei Konkurrenzmodellen. Auf Reddit steht neben dem Startfaden ein eigener mit gut 200 Punkten, Titel: hervorragend im Code, unbrauchbar im Schreiben. Die Begründung dort ist strukturell und nicht auf Z.ai gemünzt: Für Code gibt es prüfbare Belohnungen, für Prosa nicht, also optimiert jedes Training mit {{Reinforcement Learning}} in Richtung Code.

::: methode Wie geprüft wurde
Startbeitrag am 23. November vollständig gelesen: keine Ergebnistabelle, keine Modellkarte, kein
Link zu Gewichten. Die sechzehn Zeilen für GLM-5.3 stammen aus dessen Startbeitrag vom 14. August
und wurden einzeln mitgezählt. Auf Hugging Face ist das jüngste Modell der Organisation zai-org
GLM-5.3-BF16 vom 25. August; ein Eintrag zu 5.4 existiert dort nicht. Die Rangliste von Artificial
Analysis führt am Abend des 23. November Zeilen für GLM-5.1, 5.2 und 5.3, keine für 5.4. Die
Reaktionen stammen aus dem Hacker-News-Faden mit über 700 Punkten und zwei Reddit-Fäden in
r/LocalLLaMA.
:::

## Quellen

- Z.ai, "GLM-5.4: Toward Generalized Coding with Our First Loop Transformer", 23. November 2026: https://z.ai/blog/glm-5.4
- Z.ai, "GLM-5.3: Frontier Coding with Emergent Cyber Capabilities", 14. August 2026, mit Ergebnistabelle: https://z.ai/blog/glm-5.3
- Hugging Face, Profil zai-org, neueste Veröffentlichung GLM-5.3-BF16 vom 25. August 2026: https://huggingface.co/zai-org
- Artificial Analysis, Modellrangliste, abgerufen am 23. November 2026: https://artificialanalysis.ai/leaderboards/models
- The Decoder, "OpenAI will reportedly ship at least one model this year but its flagship still needs alignment work", Oktober 2026: https://the-decoder.com/openai-will-reportedly-ship-at-least-one-model-this-year-but-its-flagship-still-needs-alignment-work/
- Sebastian Raschka, "OpenAI Astra and Looped Transformers", September 2026: https://sebastianraschka.com/blog/2026/openai-astra-looped-transformers.html
- Hacker News, Diskussion zu GLM-5.4, 23. November 2026: https://news.ycombinator.com/item?id=50609685
- r/LocalLLaMA, Startfaden zu GLM-5.4: https://reddit.com/comments/1y3enps und Kritikfaden "great at coding, garbage at writing": https://reddit.com/comments/1y3lqu3
