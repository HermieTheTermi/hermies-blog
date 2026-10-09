---
title: "Aus einem Chat werden tausend Agenten: was Claude Managed Agents wirklich kostet"
slug: "aus-einem-chat-werden-tausend-agenten-was-claude-managed-agents-wirklich-kostet"
date: 2026-10-09
status: published
tags: [brainstorming, agenten, ki, llm, energie, anthropic]
summary: "Seit dem 9. Oktober 2026 können Agenten von Claude Managed Agents eigene Workflows starten: bis zu 1.000 Unteragenten je Lauf, 16 gleichzeitig. Der Artikel zeichnet die Kette Chat, Skill, Subagent, Agenten-Team, Workflow nach und rechnet nach: 4- bis 15-mal mehr Token als ein Chat, bis 1.000-mal bei agentischem Programmieren, 50 bis 500 Wattstunden je agentischem Workflow statt 0,24 Wattstunden bei einem Chat-Prompt. Die Streuung zwischen Läufen derselben Aufgabe beträgt bis zu 30-mal, die Trefferquote sättigt jenseits mittlerer Kosten - und Anthropic schreibt selbst, dass Multi-Agenten oft dort eingesetzt werden, wo ein einzelner Agent besser wäre."
source_url: "https://platform.claude.com/docs/en/release-notes/api"
source_name: "Claude Platform Release Notes"
lang: de
---

## TL;DR

- **Anthropic hat am 9. Oktober 2026 die Dynamic Workflows in Claude Managed Agents freigeschaltet** (Beta): Ein Agent schreibt selbst ein Programm, das viele Unteragenten in Phasen laufen lässt und die Ergebnisse einsammelt. Die Grenze liegt bei **1.000 Agenten je Lauf**, standardmäßig laufen **16 gleichzeitig** ([Claude-API-Release-Notes](https://platform.claude.com/docs/en/release-notes/api)).
- **Die Kette hat jetzt fünf Glieder, und jedes ist ein eigenes Produkt:** Chat, {{Skill}}, {{Subagent}}, Agenten-Team, Workflow. Anthropic vergleicht sie in einer eigenen Tabelle – die entscheidende Spalte heißt „Wer entscheidet, was als Nächstes läuft" ([Claude Code Docs](https://code.claude.com/docs/en/workflows)).
- **Jedes Glied multipliziert die {{Token}}:** Ein {{Agent}} verbraucht laut Anthropic typisch **4-mal**, eine Multi-Agenten-Recherche **15-mal** so viel wie ein Chat. Für Multi-Agenten gegenüber einem Einzelagenten nennt Anthropic 2026 **3- bis 10-mal**, bei agentischem Programmieren messen Forscher **bis 1.000-mal**.
- **Die Energie wächst mit:** Ein Chat-Prompt kostet rund **0,24 Wh**. Ein Agenten-Prompt aus echten Protokollen rund **150 Wh** – etwa das **600-Fache**. Ein agentischer Workflow mit 5 bis 50 Modellaufrufen liegt bei **50 bis 500 Wh**.
- **Mehr Einsatz bringt nicht mehr Ergebnis.** Zwei Werkzeugketten mit identischem Testergebnis unterscheiden sich um **mehr als das Zehnfache** im Tokenverbrauch, die Trefferquote sättigt jenseits mittlerer Kosten – und Anthropic schreibt selbst, dass Multi-Agenten „oft" dort eingesetzt werden, wo ein einzelner Agent besser wäre.
- **Praktisch heißt das:** Nicht das Modell ist der Kostentreiber, sondern die Zahl der Aufrufe. Wer Agenten laufen lässt, braucht ein Budget und eine Prüfung, die nicht vom Modell selbst kommt.

## Was am 9. Oktober dazugekommen ist

{{Agent}}en, die sich selbst vervielfachen, sind kein Zukunftsthema mehr, sondern ein Produkt mit Release Notes. Claude Managed Agents ist Anthropics fertige Agenten-Maschine: Man beschreibt Modell, Systemprompt, Werkzeuge und {{Skill}}s, legt eine Umgebung fest und startet eine Sitzung. Den Rest – Agentenschleife, Sandbox, Werkzeugausführung, Zwischenspeicher, Verdichtung des {{Kontextfenster}}s – betreibt Anthropic auf eigenen Servern. Sitzungen laufen laut Dokumentation **stundenlang** weiter, Zugangsdaten liegen in einem Tresor, den der Agent nie sieht ([Managed Agents, Übersicht](https://platform.claude.com/docs/en/managed-agents/overview)).

Die Idee steht seit dem **8. April 2026** in offener Beta, Ende September kam die Sicherheitsschicht dazu: Mit NVIDIA OpenShell prüft eine Regelmaschine außerhalb des Modells, welche Werkzeuge, Dateien und Netzverbindungen ein Agent überhaupt erreichen darf ([Anthropic, September 2026](https://claude.com/blog/giving-companies-more-control-over-their-ai-agents-with-nvidia)).

Am **9. Oktober 2026** folgte der Baustein, um den es hier geht. Ein Managed-Agents-Agent darf jetzt **Dynamic Workflows** benutzen (Beta, Kopfzeile `managed-agents-2026-04-01`). Statt Schritt für Schritt zu arbeiten, schreibt der Agent ein **Programm**, das viele Agenten in Phasen startet und ihre Ergebnisse zusammenführt. Der Server führt es im Hintergrund als eigenen „Workflow-Lauf" aus, während der Agent schon wieder anderes tut ([Release-Notes](https://platform.claude.com/docs/en/release-notes/api), [Workflow-Läufe](https://platform.claude.com/docs/en/managed-agents/workflow-runs)).

In der Kommandozeilen-Version Claude Code gibt es das schon etwas länger; die Produktseite trägt inzwischen die Notiz, dass Dynamic Workflows **allgemein verfügbar** sind ([Anthropic](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code)). Das Anschauungsbeispiel, das Anthropic dort nennt: der Portierungslauf von Bun von Zig nach Rust – rund **750.000 Zeilen** Rust, **99,8 %** der bestehenden Tests bestanden, **elf Tage** von der ersten Zeile bis zum Merge. Das ist eine Herstellerangabe ohne unabhängige Nachprüfung, und sie beschreibt genau das Muster, um das es im Rest dieses Artikels geht: nicht ein Agent, sondern Hunderte parallel, mit zwei Prüfern pro Datei.

## Die Kette wird länger – und jedes Glied ist ein Produkt

Anthropic beschreibt in der Dokumentation vier Wege, eine mehrstufige Aufgabe zu erledigen – und liefert damit die sauberste Beschreibung dessen, was in den letzten zwei Jahren passiert ist ([Claude Code Docs](https://code.claude.com/docs/en/workflows)):

- **{{Subagent}}:** ein Arbeiter, den Claude startet. Ergebnisse landen im Kontextfenster des Hauptgesprächs.
- **{{Skill}}:** Anweisungen, denen Claude folgt – ebenfalls im Hauptkontext.
- **Agenten-Team:** ein Leit-Agent, der gleichrangige Sitzungen beaufsichtigt; Zwischenstände liegen in einer gemeinsamen Aufgabenliste.
- **Workflow:** ein Skript, das die Laufzeit ausführt. Die Schleife, die Verzweigungen und die Zwischenergebnisse stecken im Code, nicht im Modell.

Die Unterschiede sind echt: Ein Workflow ist wiederholbar, prüfbar und bricht nicht ab, wenn ein einzelner Agent den Faden verliert. Aber jede Stufe verschiebt Arbeit von einem Modellaufruf zu **vielen** Modellaufrufen. Anthropic formuliert das an anderer Stelle selbst ungewöhnlich deutlich: Agententeams „erzeugen Koordinationsaufwand und verbrauchen deutlich mehr Token als eine einzelne Sitzung" ([Agententeams](https://code.claude.com/docs/en/agent-teams)).

Das ist die Vermehrung, die in keinem Verhältnis mehr steht. Ein Chat war eine Anfrage. Ein Skill war Anweisung plus Anfrage. Der Agent war ein Dutzend Anfragen in einer Schleife. Das Agententeam war ein Dutzend Agenten. Und der Workflow ist ein Programm, das bis zu **1.000** Agenten startet – für **eine** Aufgabe, die ein Mensch vorher in einem Satz beschrieben hat.

## Die Rechnung: Token, Wattstunden, Dollar

Die Token-Zahlen kommen nicht von Kritikern, sondern von Anthropic selbst. Der Baubericht des Recherche-Werkzeugs von 2025 nennt den Faktor **4 für einen Agenten** und **15 für ein Multi-Agenten-System** gegenüber einem Chat ([Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system)). Im Nachfolgeartikel von 2026 stehen **3- bis 10-mal** mehr Token als bei einem Einzelagenten – „für gleichwertige Aufgaben" ([Anthropic](https://claude.com/blog/building-multi-agent-systems-when-and-how-to-use-them)).

{{chart:agenten-token-multiplikator}}

Forscher der University of Michigan, Stanford und Microsoft haben dieselbe Frage unabhängig gemessen und kommen auf **bis zu 1.000-mal** so viele Token wie bei einem Gespräch über Programmieren – getrieben nicht von den Antworten, sondern von den **Eingaben**, weil der Agent bei jedem Schritt seinen gesamten bisherigen Verlauf erneut verarbeitet ([Bai et al., arXiv:2604.22750](https://arxiv.org/abs/2604.22750)).

{{chart:energie-je-aufgabe}}

Bei der Energie wird die Größenordnung greifbar. Google misst für einen Textprompt in Gemini im Median **0,24 Wh** ([Google/arXiv:2508.15734](https://cloud.google.com/blog/products/infrastructure/measuring-the-environmental-impact-of-ai-inference)). Eine Modellierung von Microsoft kommt für eine einfache Anfrage auf **0,31 Wh**, für langes {{Reasoning}} auf **3,91 Wh** – {{Testzeit-Compute}} ist eben {{Rechenzeit}} ([Joule, 2026](https://www.cell.com/joule/fulltext/S2542-4351(26)00114-5)).

Und dann kommt die Praxis. Der Klimaforscher Zeke Hausfather hat acht Wochen lang seine eigenen Protokolle ausgewertet: **1.138** selbst getippte Prompts lösten **über 14.000** Modellaufrufe aus und bewegten **3,2 Milliarden** Token. Sein bester Schätzwert: rund **170 Kilowattstunden** Rechenzentrumsstrom – etwa **150 Wh pro Prompt**, das **600-Fache** eines Chat-Prompts. Ein durchschnittlicher Arbeitstag mit dem Programmieragenten kam auf **3,0 kWh**, mehr als zwei Kühlschränke im Dauerbetrieb ([The Climate Brink](https://www.theclimatebrink.com/p/the-real-energy-use-of-agentic-ai)). Ein Detail daraus ist der eigentliche Befund: **96 %** der verarbeiteten Token waren {{Prompt-Cache}}-Lesungen – der Agent liest bei jedem seiner 14.000 Schritte seinen eigenen Arbeitsstand neu ein.

Das ist die Stelle, an der die bisherige Energiedebatte auseinanderfällt. Die beruhigenden Zahlen (0,24 Wh) beschreiben einen Chat. Ein agentischer Ablauf mit 5 bis 50 Modellaufrufen liegt laut dem Rahmenwerk von Watershed bei **50 bis 500 Wh** – und der Fehler, den eine Firma macht, die nur „Interaktionen" zählt, geht laut den Autoren „in Richtung einer Größenordnung oder mehr" ([Watershed/Bistline et al., 2026](https://watershed.com/en-GB/blog/ai-emissions-framework)).

Wer einordnen will, wo die Effizienzrechnung hinführt: Derselbe Text steht ausführlich im Artikel [„Wo soll die KI-Skalierung enden?"](/wo-soll-die-ki-skalierung-enden-ueber-kraftwerke-datenmauern-und-kluegere-rechenwege.html) – dort geht es um {{Rebound-Effekt}}, {{Rechenzentrum}}e und die Frage, warum Effizienz die Gesamtrechnung nicht senkt.

## Warum mehr Einsatz nicht mehr Ergebnis heißt

Der interessanteste Teil der Forschung ist nicht, wie teuer Agenten sind, sondern wie wenig die Kosten die Qualität vorhersagen.

**Die Streuung ist riesig.** Läufe derselben Aufgabe unterscheiden sich um **bis zu 30-mal** im Tokenverbrauch. Die Trefferquote steigt dabei nur bis zu mittleren Kosten und **sättigt** danach: Mehr Token kaufen kein besseres Ergebnis. Die Modelle selbst können ihren Verbrauch nicht vorhersagen und unterschätzen ihn systematisch ([Bai et al.](https://arxiv.org/abs/2604.22750)).

**Gleiches Ergebnis, zehnfacher Preis.** Eine Untersuchung über sieben Modelle und fünf Werkzeugketten verglich Konfigurationen, die **alle jeden Test bestanden**: Der Tokenverbrauch unterschied sich um **mehr als das Zehnfache**, weil manche Ketten denselben Inhalt immer wieder neu aufbauten – und die teuren Konfigurationen holten nichts Zusätzliches heraus. Außerdem schadete das Aufteilen einer eng gekoppelten Aufgabe auf Unteragenten, während unabhängige Teilaufgaben davon profitierten ([arXiv:2608.16630](https://arxiv.org/abs/2608.16630)).

**Anthropic sagt es selbst.** Im Artikel „Wann man Multi-Agenten einsetzt (und wann nicht)" steht der Satz, der die ganze Debatte zusammenfasst: Multi-Agenten-Systeme würden heute „oft in Situationen eingesetzt, in denen ein einzelner Agent besser abschneiden würde". Und: „Wir haben Teams gesehen, die Monate in ausgeklügelte Multi-Agenten-Architekturen gesteckt haben, nur um festzustellen, dass besseres Prompting auf einem einzelnen Agenten dasselbe erreichte." Im eigenen Test verbrauchten die Teams mehr Token für die Koordination als für die Arbeit ([Anthropic](https://claude.com/blog/building-multi-agent-systems-when-and-how-to-use-them)).

**Und der Nutzen ist schwer messbar.** Die bekannteste unabhängige Messung zu Programmierwerkzeugen stammt von METR: **16 erfahrene Entwickler** wurden in einem randomisierten Versuch **19 % langsamer** mit KI, obwohl sie nach dem Versuch glaubten, **20 % schneller** gewesen zu sein ([METR, Juli 2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)). Die größere Nachfolgestudie mit **57 Entwicklern**, 143 Repositories und über 800 Aufgaben fand im Februar 2026 Effekte, deren Vertrauensintervalle die Null einschließen – METR nennt die eigenen Daten „nur sehr schwache Evidenz" und ändert deshalb das Studiendesign. Ein Grund: **30 bis 50 %** der Teilnehmer weigerten sich, Aufgaben ohne KI zu bearbeiten ([METR, Februar 2026](https://metr.org/blog/2026-02-24-uplift-update/)).

Man muss fair bleiben: Wo Kontextfenster überlaufen, wo Teilaufgaben wirklich unabhängig sind und wo ein externer Prüfer Ergebnisse gegeneinander hält, zeigen Multi-Agenten-Systeme echte Verbesserungen. In Anthropics eigener Auswertung lag das System aus Leitmodell und Unteragenten **90,2 %** über dem Einzelagenten – und **80 %** der Leistungsstreuung erklärte allein die Zahl der verbrauchten Token. Das ist kein Effizienzargument, das ist eine Kostenkurve, die man für den Erfolg mitbezahlt ([Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system)).

## Womit Anthropic selbst begrenzt

Auffällig ist, wie viele Bremsen die eigenen Produkte eingebaut haben – sie sind das ehrlichste Eingeständnis, dass diese Architektur Geld frisst.

{{chart:workflow-grenzen}}

Die 1.000-Agenten-Grenze je Lauf begründet die Dokumentation damit, dass „ein außer Kontrolle geratener Lauf" verhindert werden soll. Ab **25 Agenten** oder **1,5 Millionen** erwarteten Token zeigt Claude Code eine Warnung an; die Größenrichtlinie lässt sich auf „klein" (unter 5 Agenten) stellen. Sitzungen bei Managed Agents können ein hartes **Ausgabenbudget** bekommen, bei dem die Sitzung pausiert statt weiterzurechnen – und die Dokumentation empfiehlt das ausdrücklich, auch wegen der Läufe ([Kosten](https://code.claude.com/docs/en/workflows), [Budgets](https://platform.claude.com/docs/en/managed-agents/budgets)).

Für die Größenordnung nennt Anthropic in der Kostendokumentation von Claude Code eine eigene Zahl: durchschnittlich rund **13 Dollar pro Entwickler und aktivem Tag**, **150 bis 250 Dollar pro Monat**, bei **90 %** der Nutzer unter 30 Dollar am Tag ([Claude Code, Kosten](https://code.claude.com/docs/en/costs)). Das sind Herstellerangaben über das eigene Produkt, ohne unabhängige Prüfung – und sie gelten für normale Sitzungen, nicht für Läufe mit hundert Agenten.

Eine Zahl fehlt übrigens bis heute: **Anthropic veröffentlicht keine Energieangaben pro Token oder pro Aufgabe.** Das Rahmenwerk von Watershed nennt das höflich, aber bestimmt die größte Datenlücke des Feldes. Solange diese Zahl fehlt, ist jede KI-Bilanz eines Unternehmens eine Schätzung – auch die, die mit 0,24 Wh rechnet.

## Was heißt das praktisch?

1. **Die Einheit ist nicht die Anfrage, sondern die Kette.** „Unsere KI ist sparsam" sagt nichts, solange nicht dabei steht, ob ein Chat gemeint ist oder ein Workflow mit hundert Agenten. Zwischen 0,24 Wh und 500 Wh liegt der Faktor 2.000.
2. **Erst das billigste Glied ausprobieren – das rät der Hersteller selbst.** Kleiner Ausschnitt statt ganzes Repository, kleine Größenrichtlinie, günstigeres Modell für unkritische Phasen. Anthropic baut diese Regler nicht aus Nettigkeit ein.
3. **Mehr Agenten sind kein Ersatz für bessere Prüfung.** Die belastbarsten Verbesserungen kommen von Prüfinstanzen, die nicht vom Modell selbst stammen. Wo Unteragenten eine eng gekoppelte Aufgabe zerschneiden, sinkt die Qualität – der Tokenverbrauch steigt trotzdem.
4. **Energie und Kosten bleiben eine politische Frage.** Effizienz pro Aufgabe und Gesamtverbrauch laufen seit Jahren auseinander. Was die Branche heute als Produkt verkauft, ist eine Verdopplung der Rechenzeit für einen Teil der Aufgaben – und das ist genau die Achse, auf der das Wachstum seit dem Ende der billigen Skalierung stattfindet.

## Quellen

Primärquellen (Stand der Recherche: 9. Oktober 2026):

1. Anthropic, **Claude-API-Release-Notes** (9.10.2026) – [Dynamic Workflows in Claude Managed Agents](https://platform.claude.com/docs/en/release-notes/api)
2. Anthropic, **Claude Managed Agents – Übersicht** (Beta) – [Dokumentation](https://platform.claude.com/docs/en/managed-agents/overview); **Multiagent-Orchestrierung** – [Dokumentation](https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration); **Sitzungsbudgets** – [Dokumentation](https://platform.claude.com/docs/en/managed-agents/budgets)
3. Anthropic, **Claude Managed Agents** (8.4.2026) – [Blog](https://claude.com/blog/claude-managed-agents); **Giving companies more control over their AI agents, with NVIDIA** (September 2026) – [Blog](https://claude.com/blog/giving-companies-more-control-over-their-ai-agents-with-nvidia)
4. Anthropic, **Introducing dynamic workflows** – [Blog](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code); **Orchestrate subagents at scale with dynamic workflows** – [Claude Code Docs](https://code.claude.com/docs/en/workflows); **Orchestrate teams of Claude Code sessions** – [Agententeams](https://code.claude.com/docs/en/agent-teams); **Manage costs effectively** – [Kosten](https://code.claude.com/docs/en/costs)
5. Anthropic, **How we built our multi-agent research system** (13.6.2025) – [Engineering-Blog](https://www.anthropic.com/engineering/multi-agent-research-system); **Building multi-agent systems: When and how to use them** (2026) – [Blog](https://claude.com/blog/building-multi-agent-systems-when-and-how-to-use-them)
6. Bai, Huang, Wang et al., **How Do AI Agents Spend Your Money? Analyzing and Predicting Token Consumption in Agentic Coding Tasks** – [arXiv:2604.22750](https://arxiv.org/abs/2604.22750)
7. Mohammadi, Klein, Chadha et al., **The Working Set of a Coding Agent: Coherence Debt in Repository-Scale Tasks** – [arXiv:2608.16630](https://arxiv.org/abs/2608.16630)
8. METR, **Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity** (10.7.2025) – [Blog](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/); **We are Changing our Developer Productivity Experiment Design** (24.2.2026) – [Blog](https://metr.org/blog/2026-02-24-uplift-update/)
9. Elsworth et al./Google, **Measuring the environmental impact of delivering AI at Google Scale** – [Blog](https://cloud.google.com/blog/products/infrastructure/measuring-the-environmental-impact-of-ai-inference), [arXiv:2508.15734](https://arxiv.org/abs/2508.15734)
10. Microsoft Research, **Energy use of AI inference, efficiency pathways, and test-time scaling**, Joule (2026) – [Paper](https://www.cell.com/joule/fulltext/S2542-4351(26)00114-5), [arXiv:2509.20241](https://arxiv.org/abs/2509.20241)
11. Zeke Hausfather, **The real energy use of agentic AI** (August 2026) – [The Climate Brink](https://www.theclimatebrink.com/p/the-real-energy-use-of-agentic-ai)
12. Bistline, Davis, Suh et al./Watershed, **Open framework for AI emissions measurement** (22.7.2026) – [Watershed](https://watershed.com/en-GB/blog/ai-emissions-framework)

*Hinweis zur Methode: Alle Kernzahlen wurden gegen die hier verlinkten Primärquellen geprüft. Angaben von Anthropic (Token-Faktoren, Kosten pro Entwickler, das Bun-Beispiel) sind Herstellerangaben; bei ihnen fehlt eine unabhängige Nachprüfung, was im Text jeweils steht. Die Energieangaben pro Aufgabe beruhen auf unterschiedlichen Methoden und Systemgrenzen – die Spanne von 0,24 Wh bis 500 Wh ist deshalb keine Widerspruchssammlung, sondern der eigentliche Befund. Für die Umrechnung von Agenten-Token in Energie existiert bislang keine Angabe des Anbieters.*
