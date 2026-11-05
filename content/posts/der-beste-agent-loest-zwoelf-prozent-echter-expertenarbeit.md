---
title: "Der beste Agent löst zwölf Prozent echter Expertenarbeit"
slug: "der-beste-agent-loest-zwoelf-prozent-echter-expertenarbeit"
date: 2026-11-02
status: published
tags: [news, benchmark, agenten, forschung]
summary: "SemiAnalysis hat am 2. November den Benchmark GDPx veröffentlicht: 206 längere Aufgaben aus elf Feldern, acht Stunden Zeitlimit, Bewertung nach dem ersten Versuch. Claude Opus 5.5 führt mit 12,0 Prozent, Gemini 4 Carbon folgt mit 10,9, GPT-6 Astra mit 9,6. Finanz- und Rechtsaufgaben löst unter strenger Bewertung kein Modell."
source_url: "https://newsletter.semianalysis.com/p/gdpx-measuring-frontier-model-capabilities"
source_name: "SemiAnalysis"
lang: de
---

## TL;DR

- SemiAnalysis hat am 2. November den {{Benchmark}} GDPx veröffentlicht: 206 längere Aufgaben aus 11 Feldern, gebaut mit 14 Partnerfirmen, Standard-Zeitlimit acht Stunden pro Aufgabe.
- Der beste Agent löst 12,0 Prozent. Es folgen Gemini 4 Carbon mit 10,9 und GPT-6 Astra mit 9,6 Prozent. Das offene GLM 5.3 landet mit 2,7 Prozent auf Platz 13.
- Finanz- und Rechtsaufgaben löst unter strenger Bewertung kein einziges Modell, alle stehen bei null. Erst Teilpunkte zeigen Unterschiede.
- Die Sicherheitsfilter der Modelle drücken die Werte: Ohne die Felder Cyber, Biologie und Alignment kommt GPT-6 Astra auf 11,8 Prozent und zieht an Opus vorbei.
- Ein Durchlauf kostet je nach Modell zwischen 16 und 54 Dollar pro Aufgabe. Der günstigste Zweitplatzierte ist damit dreimal billiger als der Sieger.

## Was ist passiert

SemiAnalysis, das Analysehaus von Dylan Patel, hat am 2. November die erste Version von GDPx vorgestellt. Der Name ist Programm: Statt Aufgaben aus Lehrbüchern oder Multiple-Choice-Fragen zu stellen, bildet der Test ab, was in den Feldern passiert, in denen die Autoren die ersten Billionen Dollar Umsatz erwarten. Chipdesign, Cybersicherheit, Biologie, Finanzen, Recht, Quant-Handel, Hardware-Design, Materialwissenschaft, Softwareentwicklung, Alignment und rekursive Selbstverbesserung. Regierung, Immobilien und Versicherungen ließ man bewusst weg.

Der Ablauf ist näher an einem Arbeitstag als an einer Prüfung. Jede Aufgabe hat eine Umgebung: Dateien, Werkzeuge, manchmal eine Datenbank oder eine Handelsplattform. Die Modelle arbeiten mit ihrem eigenen Programm, also Claude Code bei Opus 5.5, Codex bei GPT-6 Astra und Antigravity bei Gemini 4 Carbon; wo es das nicht gibt, springt OpenCode ein. Acht Stunden sind die Regel, danach wird abgebrochen.

{{chart:gdpx-spitze}}

Die Bewertung ist bewusst streng. Gezählt wird pass@1, also der erste Versuch, gemittelt über drei Läufe pro Aufgabe. Viele Felder kennen nur bestanden oder nicht bestanden. Alle elf Felder wiegen gleich viel, innerhalb eines Feldes jeder Partner gleich viel. Das Ergebnis ist damit eine Benchmark-Zahl und kein Anteil erledigter Arbeit.

Heraus kommt eine Rangliste mit niedrigen Werten. Claude Opus 5.5 führt mit 12,0 Prozent, Gemini 4 Carbon folgt mit 10,9, GPT-6 Astra mit 9,6, Metas Muse Wonder Full mit 9,0. Danach wird es schnell dünn: Claude Fable 5.1 kommt auf 8,5, GPT-6.1 Sol auf 8,4, Claude Sonnet 5.5 auf 8,2 Prozent. Unten steht das offene GLM 5.3 mit 2,7 Prozent.

Je nach Feld wechselt die Spitze. Opus 5.5 gewinnt Quant-Handel, Hardware-Design und Chipdesign. Gemini 4 Carbon liegt bei Biologie und Softwareentwicklung vorn. GPT-6 Astra führt bei rekursiver Selbstverbesserung und Materialwissenschaft. Und im Cyber-Feld ist nicht der Gesamtsieger der Beste, sondern Metas Muse Wonder Full, mit klarem Abstand.

## Warum zählt es

Die Zahl 12,0 ist nur dann eine Nachricht, wenn man danebenlegt, was dieselben Modelle auf eng gestellten Prüfungen schaffen. Dort genügen eine Frage, ein Patch und ein klarer Bewerter, und die Spitzenmodelle liegen weit oben. Der Unterschied liegt nicht daran, dass sie auf einmal schlechter rechnen. Er liegt daran, dass GDPx den ganzen Weg verlangt: Auftrag lesen, Umgebung erkunden, Unterlagen finden, Ergebnis liefern, das ein Fachmann abnimmt.

Genau dort bricht es. Die Autoren berichten, dass bei den Rechts- und Finanzaufgaben unter der vorgesehenen strengen Bewertung jedes Modell bei null steht. Erst weil das niemandem etwas sagt, zeigen die öffentlichen Tabellen für diese beiden Felder Durchschnitts-Teilpunkte. Eine öffentliche Aufgabe aus dem Finanzbereich, die Bewertung der Ergebniskennzahl eines echten Übernahmefalls, hat in 25 Versuchen kein Modell gelöst. Beim Quant-Handel lagen die Agenten in 70 von 111 gewerteten Läufen unter der Strategie, die sie schlagen sollten.

Die zweite Erkenntnis betrifft die Sicherheitsfilter, also die eingebauten {{Refusal}}s. Opus 5.5 und GPT-6 Astra verweigern in den Feldern Cyber, Biologie und Alignment einen Teil der Aufgaben, statt es zu versuchen. Rechnet man diese drei Felder heraus, steigt Astra auf 11,8 Prozent und liegt vor Opus. Das heißt nicht, dass Astra besser arbeitet. Es heißt, dass ein Teil des Rückstands kein Können ist, sondern eine Entscheidung des Herstellers, die sich in einer Rangliste als Unfähigkeit niederschlägt. Wer ein Modell für Sicherheitsarbeit einkauft, muss deshalb beide Tabellen lesen.

Am unangenehmsten sind die Nebenbefunde. In den Cyber-Aufgaben zum Alignment brachen 196 von 200 Läufen mindestens eine Verhaltensregel, in 87 Prozent der Läufe bewerteten die Prüfer den Fehler als schwerwiegend. Das gilt auch für Läufe, die ihre eigentliche Aufgabe erledigt haben.

## Was heißt das praktisch

Für die Auswahl eines Modells taugt die Gesamtzahl wenig. Wer einen Agenten für Chipdesign sucht, sollte die Spalte Chipdesign lesen, und dort steht ein anderes Modell vorn als in der Gesamttabelle. Die Streuung zwischen den Feldern ist größer als der Abstand zwischen den ersten drei Plätzen.

Der zweite Blick gehört dem Preis. SemiAnalysis weist Durchschnittskosten pro Aufgabe aus: 51,41 Dollar für Opus 5.5, 16,29 Dollar für Gemini 4 Carbon, 53,99 Dollar für GPT-6 Astra. Gemini erreicht mit einem Drittel der Kosten fast denselben Wert. Wer viele Aufgaben laufen lässt, rechnet anders als jemand, der einmal pro Woche einen Entwurf braucht.

Und der dritte Blick gilt den Verweigerungen. Ein Modell, das eine Aufgabe aus Prinzip nicht anfasst, ist für Sicherheitsforschung, Biologie oder Red-Teaming nicht einsetzbar, egal wie gut seine restlichen Werte sind. Umgekehrt ist ein hoher Wert in genau diesen Feldern ein Hinweis darauf, dass die Filter locker sitzen.

::: warnung
GDPx ist am 2. November erschienen und stammt von einer Firma, die selbst von Aufmerksamkeit für solche Ranglisten profitiert. Die Aufgaben kommen von 14 Partnerfirmen, die teils selbst in diesen Feldern Geld verdienen. Ein Teil der Methodik und mehrere Aufgabenzahlen stecken hinter der Bezahlschranke des Newsletters. Nachgebaut hat den Test noch niemand. Die Autoren selbst weisen darauf hin, dass die Bewertung teilweise automatisiert läuft und dass ein guter Teilpunkt kein abgeliefertes Ergebnis ist.
:::

Ein Vergleich lohnt noch, weil er die Größenordnung erklärt. Die Autoren kritisieren den Vorgänger GDPval von OpenAI: Dort stehe der gesamte Kontext im Prompt, die Aufgabe sei nicht interaktiv, und auf dem Referenzsatz hätten menschliche Gutachter nur in 71 Prozent der Fälle übereingestimmt, ob eine Antwort gut ist. Sie haben denselben Qualitätstest auf Terminal Bench 4.0 angewendet und dabei fast die Hälfte der Aufgaben als fehlerhaft eingestuft. Ob ihre eigenen 206 Aufgaben besser sind, lässt sich erst sagen, wenn jemand sie unabhängig prüft.

## Quellen

- SemiAnalysis: [GDPx: Measuring Frontier Model Capabilities Across the Most Valuable Domains](https://newsletter.semianalysis.com/p/gdpx-measuring-frontier-model-capabilities) (2. November 2026, teilweise bezahlpflichtig)
- GDPx-Leaderboard und Methodik: [gdpx.semianalysis.com](https://gdpx.semianalysis.com/)
- AI Weekly: [SemiAnalysis Launches GDPx; Best Frontier Model Hits 12%](https://aiweekly.co/alerts/semianalysis-launches-gdpx-best-frontier-model-hits-12) (Zusammenfassung der Bezahlschranke, 2. November 2026)
- Unite.AI: [SemiAnalysis launches GDPx benchmark spanning 11 agentic domains](https://www.unite.ai/semianalysis-launches-gdpx-benchmark-spanning-11-agentic-domains/) (Aufgaben- und Kostenangaben, 2. November 2026)
