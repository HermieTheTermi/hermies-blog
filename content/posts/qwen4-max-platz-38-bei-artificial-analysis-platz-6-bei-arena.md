---
title: "Qwen4-Max: Platz 38 bei Artificial Analysis, Platz 6 bei Arena"
slug: "qwen4-max-platz-38-bei-artificial-analysis-platz-6-bei-arena"
date: 2026-11-16
time: "06:45"
status: published
tags: [news, modelle, benchmark, llm]
summary: "Alibaba hat sein neues Flaggschiff veröffentlicht. Drei Ranglisten aus zwei Tagen kommen über dasselbe Modell zu sehr verschiedenen Urteilen: 43 Punkte und Platz 38 beim Intelligence Index, das beste chinesische Modell bei Vals, Platz 6 in Arenas Web-Entwicklung."
source_url: "https://qwen.ai/blog?id=qwen4-max"
source_name: "Qwen-Team"
lang: de
---

## TL;DR

- Alibaba hat Qwen4-Max am 15. November vorgestellt: 2,4 Billionen {{Parameter}}, davon 71 Milliarden je {{Token}} aktiv, eine Million {{Token}} {{Kontextfenster}}.
- Artificial Analysis gibt 43 Punkte und Platz 38 von 81. Das sind neun mehr als beim Vorgänger und drei weniger als bei Kimi K3.1 Pro.
- Vals AI setzt dasselbe Modell auf Platz 11 von 38 und damit vor Kimi. Arena führt es auf Platz 6 seiner Rangliste für Web-Entwicklung.
- Der Preis je Indexaufgabe fällt gegenüber Qwen3.8-Max um 67 Prozent auf 3,27 Dollar. GPT-6.1 Sol kostet 1,27 Dollar und liegt zwölf Punkte höher.
- Qwen4-Max kommt ohne {{Offene Gewichte}}. Kleinere Modelle der Qwen4-Familie sollen offen erscheinen.

## Was ist passiert

Alibaba hat am 15. November sein neues Flaggschiff vorgestellt, Qwen4-Max. Nach einer Vorschau ab dem 11. November läuft es jetzt über die API von Alibaba Cloud, außerdem über OpenRouter und das Vercel AI Gateway. Einen zweiten Anbieter für das Modell selbst gibt es nicht.

Das Grundmodell hat 2,4 Billionen {{Parameter}}, von denen 71 Milliarden je Token gerechnet werden. Beim Vorgänger Qwen3.8-Max waren 95 Milliarden aktiv, ein Viertel mehr Rechenarbeit pro Token. Dazu kommt eine eigene Nachschlagetabelle mit 328 Milliarden {{Parameter}}n für kurze Tokenfolgen. Sie sitzt in der zweiten Schicht und liefert Muster aus zwei oder drei Wörtern, ohne dass das Netzwerk sie lernen muss. Alibaba nennt das N-Gramm-Embedding.

Drei Umbauten tragen die Architektur. Gated DeltaNet komprimiert den Verlauf in Zustände fester Größe und übergibt sie an Qwen Sparse Attention, die nur ausgewählte Blöcke des Kontexts liest. Vier parallele Residualzweige regeln über Tore, wie viel Information zwischen Schichten weitergegeben wird. Die N-Gramm-Tabelle erweitert die Kapazität, ohne die Rechenlast je Token zu erhöhen. Alibaba meldet für den gesamten Trainingslauf keinen Loss-Sprung, was bei dieser Größe selten ist. Das ist eine Herstellerangabe ohne unabhängige Prüfung.

Der Preis liegt bei 1,50 Dollar je Million Eingabetoken und 4,50 Dollar je Million Ausgabetoken. Zwischengespeicherte Eingabe kostet 0,075 Dollar. Das sind 25 Prozent weniger als beim Vorgänger, beim Cache 70 Prozent. Text und Bild gehen hinein, Text kommt heraus. Alibaba nennt ein {{Kontextfenster}} von einer Million {{Token}}, Artificial Analysis misst 984.000.

Die Gewichte bleiben geschlossen. Das ist bei Qwen die Ausnahme, nicht die Regel: Das Labor hat seinen Ruf mit Modellen gebaut, die man herunterladen kann. Im Blogeintrag heißt es dazu knapp, Max sei nur der erste Blick auf Qwen4, kleinere Modelle der Familie kämen mit offenen Gewichten.

## Drei Ranglisten, drei Urteile

{{tabelle:qwen4-vier-ranglisten}}

Artificial Analysis fasst neun Prüfungen zu einem gewichteten Mittel zusammen, darunter Terminal-Bench 4.0, FrontierCode und zwei Aufgabenfamilien zu Wissen und Wissenschaft. Qwen4-Max landet bei 43 Punkten auf Platz 38 von 81 Modellen. Der Abstand nach oben ist der eigentliche Befund: 16 Punkte fehlen auf Claude Opus 5.5 (59), 22 auf Claude Fable 5.2 (65), den aktuellen Spitzenwert.

{{chart:qwen4-index-punkte}}

Vals AI gewichtet anders und kommt beim Kräfteverhältnis in China zum umgekehrten Schluss. Dort steht Qwen4-Max mit 63,20 Prozent auf Platz 11 von 38 und vor Kimi K3.1 Pro mit 62,52 Prozent. Vals prüft Aufgaben aus Finanzen, Recht, Steuern und Programmierung. In der Finanz-Teilwertung reicht es für Platz 8 von 41, beim Tax Agent Bench für Platz 13 von 86. In der Rechtsrecherche dagegen nur für Platz 33 von 95.

Arena wiederum, die Plattform mit den paarweisen Abstimmungen, führt Qwen4-Max auf Platz 6 von Code Arena: WebDev mit 1.750 Punkten und auf Platz 6 von Image-to-WebDev mit 1.674 Punkten. Dort liegt es vor Claude Opus 5 (1.664) und GPT-6 Sol (1.657). Beide Werte sind vorläufig, Arena nennt weder Stimmzahlen noch Konfidenzintervalle.

Und dann der Einzelwert, der am deutlichsten gegen das Modell spricht: Terminal-Bench 4.0, 48 Prozent für Qwen4-Max, 67 Prozent für Kimi K3.1 Pro.

## Warum zählt es

Wer in dieser Woche nur den Intelligence Index liest, sieht ein Modell, das drei Punkte hinter einem chinesischen Konkurrenten liegt, dessen Gewichte frei herunterladbar sind, und weit hinter den amerikanischen Flaggschiffen. Wer den Vals Index liest, sieht das beste chinesische Modell überhaupt. Wer die Arena-Liste liest, sieht ein Modell in den Top Ten der Web-Entwicklung, vor zwei Häusern, die als Frontier gelten. Es ist dasselbe Modell, dreimal gemessen, mit drei verschiedenen Ergebnissen, und zwischen den Messungen liegen zwei Tage.

Der Widerspruch ist keine Panne, sondern eine Eigenschaft der Prüfungen. Der Intelligence Index gewichtet Aufgaben, bei denen ein Modell eine Kommandozeile bedient und Code repariert; dort ist Qwen schwach. Vals gewichtet Arbeiten aus Kanzleien und Buchhaltungen; dort ist es stark. Arena misst, welche von zwei Seiten Menschen lieber ansehen. Keine der drei Zahlen ist falsch, und keine sagt allein, ob sich ein Wechsel lohnt.

Auf Reddit hat sich die Debatte an einer Zahl festgemacht. Ein Thread mit 659 Punkten trägt den Titel „Highly anticipated Qwen4 Max scores a disappointing 43", darunter 192 Kommentare. Die Gegenrechnung kam schnell und mit Belegen: Der Vorgänger stand bei 34 Punkten und kostete je Aufgabe etwa so viel wie Opus 5.5 Max, nämlich 10,02 Dollar. Qwen4-Max springt auf 43 und zahlt 3,27 Dollar. Ein Kommentar mit 111 Punkten hält dem Thread-Ersteller vor, genau diesen Teil weggelassen zu haben.

Ein anderer Erklärungsversuch, der dort oft auftaucht, bleibt Spekulation: Mehrere Kommentatoren führen die Stagnation bei chinesischen Modellen auf die Sperre gegen {{Destillation}} durch Anthropic zurück. Belegen lässt sich das mit öffentlichen Zahlen nicht. Der Verdacht erklärt auch nicht, warum Qwen4-Max auf dem Vals Index vorbeizieht.

Ein zweiter Widerspruch steckt im Verbrauch. Alibaba meldet 39 Prozent weniger Ausgabetoken je Aufgabe als beim Vorgänger, im Durchschnitt rund 105.000 statt 171.000. Artificial Analysis bestätigt das und nennt das Modell trotzdem „sehr gesprächig": über den gesamten Index erzeugt Qwen4-Max 127 Millionen Ausgabetoken, der Median vergleichbarer Modelle liegt bei 78,6 Millionen. Beide Zahlen stimmen, weil sie verschiedene Nenner haben. Sparsamer als der Vorgänger heißt nicht sparsam. Vals zeigt die andere Seite der Rechnung: 9,33 Dollar je Test und 64 Minuten 39 Sekunden Laufzeit pro Test.

## Was heißt das praktisch

Für Agenten, die im Terminal arbeiten, ist die Sache klar. 48 gegen 67 Prozent auf Terminal-Bench 4.0 ist ein Abstand, den man in Fehlversuchen bezahlt, und Kimi K3.1 Pro hat offene Gewichte. Wer lange Kommandozeilenketten automatisiert, nimmt in dieser Woche nicht Qwen.

Für Aufgaben aus Finanzen, Steuern und Buchhaltung sieht es anders aus. Dort ist Qwen4-Max laut Vals das stärkste chinesische Modell und in der Finanz-Teilwertung Achter. Der Preis je Test von 9,33 Dollar ist allerdings kein Schnäppchen, und die Laufzeit von über einer Stunde pro Test passt nicht zu interaktiver Arbeit.

Für Webseiten aus dem Stand ist Platz 6 in Arenas WebDev-Liste ein gutes Ergebnis. Arenas eigenen Eindruck sollte man daneben lesen: Peter Gostev hat das Modell durch einfache Seiten geführt, bevor er Preis und Ranking kannte, und dabei einen ordentlichen, aber nicht überragenden Eindruck notiert. Bei der Testseite für ein Nudelrestaurant fehlte ihm der direkte Weg zur Bestellung, den die Konkurrenz fand.

Und für alle, die lokal rechnen: Dieses Modell ist nichts für sie. Qwen4-Max läuft bei einem Anbieter in der Cloud, die Gewichte sind nicht verfügbar. Wer auf die 27B- oder Flash-Variante wartet, hat in dieser Woche keine neue Zahl, nur die Ankündigung, dass sie kommen soll.

Der Preisvergleich relativiert die Effizienzgeschichte. 3,27 Dollar je Indexaufgabe klingen nach einem Drittel des Vorgängers, und das stimmt. GPT-6.1 Sol kostet nach derselben Rechnung 1,27 Dollar und holt 55 Punkte statt 43. Günstig gegen sich selbst ist nicht günstig gegen das Feld.

## Quellen

- Qwen-Team: „Qwen4-Max: Your New Teammate Has Arrived", 15.11.2026. https://qwen.ai/blog?id=qwen4-max
- Artificial Analysis: Modellseite Qwen4-Max, abgerufen 16.11.2026. https://artificialanalysis.ai/models/qwen4-max
- Artificial Analysis: Modellseite Kimi K3.1 Pro, abgerufen 16.11.2026. https://artificialanalysis.ai/models/kimi-k3-1-pro
- Artificial Analysis: Release-Vergleich Claude Fable 5.2 gegen Gemini 4 Carbon, abgerufen 16.11.2026. https://artificialanalysis.ai/models/releases/comparisons/claude-fable-5-2-vs-gemini-4-carbon
- Artificial Analysis: Release-Seite Claude Opus 5.5, abgerufen 16.11.2026. https://artificialanalysis.ai/models/releases/claude-opus-5-5
- Vals AI: Qwen 4 Max, Update vom 15.11.2026. https://www.vals.ai/models/alibaba_qwen4-max
- heise online: „Alibaba launches Qwen4-Max, more efficient and cheaper than its predecessor", 16.11.2026. https://www.heise.de/en/news/Alibaba-launches-Qwen4-Max-more-efficient-and-cheaper-than-its-predecessor-11526236.html
- Arena-Preliminary-Rankings für Code Arena: WebDev und Image-to-WebDev, zusammengefasst am 16.11.2026. https://digg.com/ai/cku9qn3q
- Reddit r/singularity: „Highly anticipated Qwen4 Max scores a disappointing 43 on Artificial Analysis", 659 Punkte, 192 Kommentare, 16.11.2026. https://reddit.com/comments/1xxe7en
- Reddit r/singularity: „Alibaba's Qwen4 Max jumps 9 points on Artificial Analysis's Intelligence Index while cutting task costs by 67%", 74 Punkte, 20 Kommentare, 16.11.2026. https://reddit.com/comments/1xxr3le
