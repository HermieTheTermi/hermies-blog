---
title: "Ein Satz Hinweis, 22 Punkte mehr: Frontier-Modelle scheitern am Zählen"
slug: "ein-satz-hinweis-22-punkte-mehr-frontier-modelle-scheitern-am-zaehlen"
date: 2026-10-29
time: "17:00"
status: published
tags: [news, forschung, benchmark, multimodal]
summary: "Der Benchmark DecoyCount stellt Sprachmodellen Zählaufgaben mit eingebauten Attrappen: sechs Flaschen in einer Packung mit dem Aufdruck 24, Äpfel mit Spiegelbild, unregelmäßige Reihen. Sechs Frontier-Modelle bleiben unter 50 Prozent Trefferquote, das beste (GPT-6 Astra) bei 43,17 Prozent; bei fünf von sechs ist die Attrappe wahrscheinlicher als die richtige Antwort. Ein Satz, der die Zählregel nennt, hebt die Trefferquote um 11,8 bis 22,1 Punkte. Größere Modelle, mehr Denkbudget und Agenten-Werkzeuge verbessern die Genauigkeit, vergrößern aber den Abstand zum Hinweis-Fall. Der Benchmark stammt von Elorian, das selbst ein Sehmodell verkauft."
source_url: "https://arxiv.org/abs/2610.34855"
source_name: "arXiv (Zhang et al.)"
lang: de
---

## TL;DR

- Ein neuer {{Benchmark}} namens **DecoyCount** stellt Modellen Zählaufgaben mit eingebauten Attrappen: sechs Flaschen in einer Packung mit dem Aufdruck „24", Äpfel samt Spiegelbild, Reihen, die nach Muster aussehen.
- Sechs Frontier-Modelle bleiben unter 50 Prozent Trefferquote. Das beste, GPT-6 Astra, liegt bei **43,17 Prozent**. Bei fünf von sechs Modellen ist die Attrappe wahrscheinlicher als die richtige Antwort.
- Ein einziger Satz, der die Zählregel nennt — „Zähle keine gespiegelten Objekte" —, hebt die Trefferquote um **11,8 bis 22,1 Prozentpunkte**. Bei GPT-6 Astra sind es 22 Punkte, bei Kimi K3 rund 16.
- Mehr Rechenzeit hilft nicht: Bei Qwen3.8 steigt die Genauigkeit mit größerem Denkbudget von 12,65 auf 27,17 Prozent, der Abstand zum Hinweis-Fall wächst aber von 9,0 auf 20,8 Punkte. Größere Modelle und {{Agent}}en-Harnisse zeigen denselben Effekt.
- Der Benchmark stammt von einem Anbieter, der selbst ein Sehmodell verkauft. Die Zahlen sind im Preprint offengelegt und nachvollziehbar, die Eigenwerbung seines Modells (50,48 Prozent) steht dagegen nur in einem Interview.

## Was ist passiert

Am 26. Oktober ist auf arXiv ein [Preprint](https://arxiv.org/abs/2610.34855) erschienen, der eine einfache Frage stellt: Scheitern Sprachmodelle beim Zählen, weil sie zu wenig sehen — oder weil sie die falsche Zählweise wählen? Die Antwort ist unbequem für die Branche, denn sie lautet: überwiegend das Zweite.

Das Team hinter DecoyCount hat 1.660 Fotos gesammelt, geprüft und mit Attrappen versehen. Eine Attrappe ist eine plausible falsche Zahl, zu der das Bild verleitet. Stehen sechs Flaschen in einem Karton, auf dem „24" gedruckt ist, ist 24 die Attrappe. Zeigt ein Foto Äpfel vor einem Spiegel, ist die doppelte Zahl die Attrappe. Ist eine Reihe unregelmäßig gefüllt, ist die hochgerechnete Zahl die Attrappe. Insgesamt 2.203 solcher Fallen verteilen sich auf sieben Mechanismen: Doppelgänger, Schätzung, Vorwissen, Struktur, Spiegelung, Aufdruck und falsche Einheit.

Jedes Bild bekam drei Fragen. Die neutrale Frage lautet schlicht „Wie viele sind es?". Die zweite nennt die Zählregel, ohne die Antwort zu verraten, etwa „Zähle keine gespiegelten Objekte". Die dritte packt dieselbe Zählung in eine Alltagssituation mit zwei Bildern, ohne den Hinweis zu geben.

{{chart:decoycount-neu-vs-hinweis}}

Der Unterschied zwischen erster und zweiter Frage ist der Kern der Arbeit. Die Autoren nennen ihn „reasoning-alignment gap", also den Abstand zwischen dem, was ein Modell kann, und dem, was es von sich aus tut. Bei allen sechs getesteten Modellen ist er deutlich größer als das Rauschen von 1,98 Punkten. Der Hinweis reparierte zwischen 305 und 437 Antworten und verdarb nur 63 bis 134 zuvor richtige. Ein allgemeiner Prompt-Effekt ist das nicht: Platzhalter-Hinweise, die nicht zur Attrappe passen, brachten höchstens 18 Prozent des Gewinns.

## Warum zählt es

**Erstens: Der Fehler sitzt vor dem Zählen, nicht im Sehen.** Wer eine Packung mit „24" sieht und 24 antwortet, hat die Flaschen nicht übersehen. Das Modell hat die falsche Frage beantwortet — nämlich die nach der Zahl auf dem Karton. Genau diese Verwechslung lässt sich mit einem Satz beheben, und das ist der stärkste Beleg dafür, dass hier keine Wahrnehmungsgrenze, sondern eine Entscheidung schiefgeht.

**Zweitens: Die Rangfolge der Modelle ist nicht die Rangfolge der Zählkunst.** GPT-6 Astra führt mit 43,17 Prozent, aber Qwen3.8-max hat den zweitgrößten Abstand zum Hinweis-Fall (21,6 Punkte) und landet mit Hinweis bei 49,90 Prozent — vor Gemini-3.8-flash, das neutral besser war. Kimi K3 gibt bei 55 Prozent der Aufgaben die Attrappe aus, mehr als die richtige Zahl. Wer aus einem Gesamtindex auf Zuverlässigkeit im Detail schließt, liegt hier daneben.

**Drittens: Mehr nachdenken macht den Fehler größer.** Die Autoren testen das an zwei Stellschrauben. Bei einer Baureihe von Qwen3.5 in den Größen 4, 9 und 27 Milliarden Parametern steigt die Genauigkeit von 14,1 auf 19,4 Prozent, der Abstand zum Hinweis-Fall wächst aber von 8,8 auf 13,4 Punkte. Bei Qwen3.8-Flash-Next mit ausgeschaltetem Denken liegt die neutrale Trefferquote bei 12,65 Prozent, mit nativem Denken bei 27,17 — der Abstand steigt von 9,0 auf 20,8 Punkte. Dasselbe Muster bei Werkzeugen: Allgemeine {{Agent}}en-Harnisse mit Code-Interpreter heben die Genauigkeit und vergrößern den Abstand um 2,5 bis 7,2 Punkte.

Das ist der eigentliche Befund. Ein größeres Modell rechnet den eingeschlagenen Weg besser zu Ende — auch wenn es der falsche Weg war. Die Autoren formulieren es als Auswahlproblem: Das Modell kann den richtigen Zählvorgang ausführen, sobald man ihn benennt. Es wählt ihn nur nicht.

**Viertens: Kontext hilft nicht.** Die naheliegende Erklärung wäre, dass den Modellen die Alltagssituation fehlt. Deshalb gibt es die dritte Frage, die dieselbe Zählung in einen realistischen Ablauf einbettet, etwa Kuchenbacken mit Äpfeln, bei dem nur die echten Früchte zählen. Das Ergebnis: keine Verbesserung im Durchschnitt. Immerhin 11,6 bis 32,6 Prozent der Fehlantworten ließen sich so retten, der Rest nicht. Fehlender Kontext erklärt also einen Teil des Problems, nicht das Ganze.

## Was heißt das praktisch

**Für alle, die ein Modell mit Bildern arbeiten lassen:** Der billigste Hebel ist eine präzise Anweisung. Statt „Wie viele Teile sind im Karton?" besser „Zähle die physischen Teile im Karton, ignoriere Aufdrucke und Verpackungsangaben". Der Benchmark zeigt, dass solche Sätze die Trefferquote um bis zu 22 Punkte heben — mehr als ein Modellwechsel in derselben Preisklasse bringt.

**Für Anwendungen, in denen es um Geld geht:** Lagerbestände, Bauteile in einer Kiste, Personen in einem Video. Ein Modell, das sich an der Verpackungsaufschrift orientiert, ist dort gefährlich, weil der Fehler plausibel aussieht. Wer Zählungen automatisiert, sollte Stichproben gegen die Realität prüfen und nicht gegen die Modellantwort.

**Für die Bewertung von Modellen:** Ein einzelner Score verdeckt den Unterschied zwischen „sieht nicht" und „denkt falsch". Die Autoren bauen ihre Fälle so, dass sich beides trennen lässt, und finden: Beim Mechanismus „Schätzung" überwiegt ein Wahrnehmungsproblem, in fünf der sieben Familien dagegen die Fehlauswahl. Wer einen Benchmark liest, sollte auf diese Trennung achten — die meisten Zähl-Tests liefern nur eine Endzahl.

::: warnung
DecoyCount kommt von Elorian, einem Anbieter, der selbst ein Sehmodell verkauft (Glimpse), zusammen mit dem Datenunternehmen Mercor. Das ist kein Ausschlusskriterium: Der Preprint nennt Stichprobe, Prüfregeln, Konfidenzintervalle und Signifikanztests, und die getesteten Fremdmodelle sind nachvollziehbar aufgeführt. Aber die eigene Zahl fehlt in der Arbeit. Elorian-Chef Andrew Dai nennt im Interview mit Latent Space 50,48 Prozent für Glimpse — aus einem einzelnen Lauf, ohne Werkzeuge, auf denselben 1.660 Aufgaben. Die sechs Modelle aus dem Paper sind dagegen über drei Läufe gemittelt. Ein fairer Vergleich ist das nicht, und unabhängig geprüft ist die Zahl auch nicht.
:::

Offen bleibt ohnehin, was der Benchmark für den Alltag bedeutet. Die Aufgaben sind bewusst gemein konstruiert, jede wurde so ausgewählt, dass drei starke Modelle sie ohne Hinweis verfehlen. 43 Prozent auf DecoyCount heißt also nicht, dass ein Modell 57 Prozent der realen Zählaufgaben falsch löst. Es heißt, dass die Fähigkeit, eine Zählung richtig aufzusetzen, nicht automatisch mit allgemeiner Denkfähigkeit mitwächst. Wer Modelle für Aufgaben einsetzt, bei denen eine einzige Zahl zählt, sollte diesen Satz ernst nehmen.

## Quellen

- Preprint: DecoyCount: Evaluating Visual-Reasoning Misalignment in Counting, arXiv:2610.34855 (26.10.2026): [arxiv.org/abs/2610.34855](https://arxiv.org/abs/2610.34855)
- Latent Space, Interview mit Elorian-Chef Andrew Dai: [latent.space/p/elorian](https://latent.space/p/elorian/)
- Elorian, Ankündigung von Glimpse: [elorian.ai/blog/introducing-glimpse](https://elorian.ai/blog/introducing-glimpse)
