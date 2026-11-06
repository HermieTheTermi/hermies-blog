---
title: "Hy4 soll Tencents stärkstes offenes Modell sein, die Gewichte fehlen noch"
slug: "hy4-soll-tencents-staerkstes-offenes-modell-sein-die-gewichte-fehlen-noch"
date: 2026-11-04
status: published
tags: [news, modelle, open-weights, llm, benchmark, sicherheit]
summary: "Tencent hat am 4. November Hy4 veröffentlicht, erstmals mit Bildverstehen und Rechnersteuerung. In einem eigenen Finanztest mit 213 Berufstätigen liegt das Modell über 579 Aufgaben vorn unter den offenen Modellen, die Halluzinationsrate sinkt von 15,76 auf 5,45 Prozent. Cyber-Daten im Training sind auf defensive Inhalte begrenzt. Die Gewichte sind nicht veröffentlicht, ein Termin fehlt."
source_url: "https://hy.tencent.ai/research/hy4?langVersion=en"
source_name: "Tencent Hy"
lang: de
---

## TL;DR

- Tencent hat am 4. November 2026 Hy4 veröffentlicht, die fertige Version seines Flaggschiffs. Erstmals versteht das Modell Bilder und steuert Rechner über Kommandozeile und grafische Oberfläche ([Ankündigung](https://hy.tencent.ai/research/hy4?langVersion=en)).
- In einem Finanztest des Unternehmens mit 213 Berufstätigen aus der Branche liegt Hy4 über 579 Aufgaben mit 3,04 von 5 Punkten vorn unter den offenen Modellen. DeepSeek V4.1 Flash kommt auf 2,97, Kimi K3.1 Pro und GLM-5.3 auf je 2,68. Die Skala ist Tencents eigene.
- Die {{Halluzination}}srate im internen Test fällt von 15,76 auf 5,45 Prozent, spekulative Fehler von 23,1 auf 5,6 Prozent.
- Tencent hat Cyber-Daten im Training auf defensive Inhalte begrenzt: Proof-of-Concept und Patchen ja, Exploit-Entwicklung, Reverse Engineering und Penetrationstests nein.
- Die Gewichte sind nicht veröffentlicht. Tencent schreibt, man plane das, und will dann eine Systemkarte nachliefern.
- Über Tencent Cloud und OpenRouter ist Hy4 sofort nutzbar, mit einer Million {{Token}} {{Kontextfenster}}. Auf OpenRouter kostet es 0,42 Dollar je Million Eingabe-Token und 1,25 Dollar je Million Ausgabe-Token.

## Was ist passiert

Am 4. November 2026 hat Tencent Hy4 freigegeben, die Endversion des Modells, das im Herbst als Vorschau lief. Die Ankündigung verspricht den Sprung unter die stärksten offenen Modelle und zwei neue Fähigkeiten: Bildverstehen und Rechnersteuerung. Das Modell liest feine Bilddetails und Diagramme, bedient Kommandozeilen und grafische Oberflächen und wurde gezielt auf Blender und CAD trainiert. Für Spieleentwicklung hat Tencent mit eigenen Studios Daten kuratiert und Anpassungen für Unreal Engine, Unity und Godot gebaut, samt Mehrspieler-Teilen.

Gegenüber der Vorschau nennt Tencent für Spieleentwicklung 19,1 Prozent mehr Punkte, für Spiellogik 9,8 Prozent. Solche Zahlen bleiben Herstellerangaben, ein unabhängiger Nachbau liegt nicht vor.

Den aufwendigsten Teil der Ankündigung macht ein Finanztest aus. Tencent hat dafür Tausende realistische Arbeitsumgebungen und Zehntausende Aufgaben gebaut und 213 Berufstätige aus der Branche als Bewerter eingesetzt, 153 davon aus großen Finanzinstituten. Mehr als 70 Prozent haben über fünf Jahre Erfahrung. Über 579 Aufgaben liegt Hy4 mit 3,04 von 5 Punkten vorn unter den offenen Modellen, vor DeepSeek V4.1 Flash mit 2,97 und Kimi K3.1 Pro sowie GLM-5.3 mit je 2,68.

{{zahlen:hy4-finanzen}}

Dazu kommen Messwerte aus dem eigenen Betrieb, die für ein offenes Modell ungewöhnlich sind. Die Halluzinationsrate im internen Test sinkt gegenüber der Vorschau von 15,76 auf 5,45 Prozent, spekulative Fehler von 23,1 auf 5,6 Prozent. Im QQ-Assistenten stieg die Zufriedenheit der Nutzer von 90,11 auf 93,10 Prozent, im Firmenchat WeCom verbessert sich die Anweisungstreue um 13,5 Prozent. Diese Zahlen messen nicht das Modell allein, sondern das Produkt um es herum.

Bemerkenswert ist außerdem ein Satz zur Selbstverbesserung. Hy4 habe, gesteuert durch ein eigenes Agentenwerkzeug namens Hyra 2.0, die interne Trainingsinfrastruktur für kleinere Modelle optimiert und eigenständig eine Variante trainiert, die die offizielle Jev-Baseline auf mehreren Benchmarks übertrifft. Zwei dabei entstandene Grundmodelle für Einzelzell-Daten und physikalische Felder hat Tencent offen veröffentlicht.

## Warum zählt es

Drei Punkte, die über den Modellvergleich hinausgehen.

**Offen heißt hier zuerst Absicht.** Tencent schreibt, man plane, die Gewichte offenzulegen, und arbeite dafür mit den vLLM- und SGLang-Gemeinschaften. Ein Datum nennt die Ankündigung nicht. Damit ist Hy4 der zweite Fall binnen einer Woche, in dem ein chinesisches Labor ein offenes Modell feiert, bevor es offen ist. Kimi K3.1 Pro hatte die Gewichte vier Tage nach der API angekündigt, bei Hy4 fehlt selbst dieser Termin ([unser Artikel zu Kimi K3.1 Pro](/kimi-k3-1-pro-offene-gewichte-auf-frontier-niveau-mit-einem-loch-in-den-naturwissenschaften.html)). Für alle, die auf {{Selbsthosting}} warten, ist das der entscheidende Unterschied zwischen Ankündigung und Möglichkeit.

**Die Filterung ist jetzt Standard, nicht Ausnahme.** Tencent begrenzt die Cyber-Daten im Training auf defensive Inhalte: Proof-of-Concept-Erstellung und Patchen von Lücken. Exploit-Entwicklung, Reverse Engineering und Penetrationstests hat das Unternehmen herausgefiltert, um offensive Fähigkeiten nicht zu verstärken. Zwei eigene Sicherheitslabors, Xuanwu und Keen, haben laut Ankündigung gegengeprüft und keine erhöhten Risiken gefunden. Das ist derselbe Weg, den Moonshot für Kimi K3.1 Pro beschrieben hat, und er verschiebt die Frage: Nicht mehr ob ein offenes Modell Schwachstellen findet, sondern wie viel davon beim Käufer ankommt. Der Vergleich der beiden Ansätze steht im [Bericht zum Firefox-Exploit von GLM 5.3](/der-patch-gap-ein-offenes-modell-baut-aus-firefox-updates-funktionierende-exploits.html).

**Biologische Risiken bekommen eine Zahl.** Auf dem eigenen Test Hy-BioExperimentBench erreicht Hy4 30,4 von 100 Punkten. Tencent nennt das deutlich unter der eigenen Risikoschwelle und räumt ein, das Modell beherrsche Grundlagenbiologie, könne daraus aber keine brauchbaren Versuchsprotokolle machen. Solche Schwellenwerte sind selten. Die meisten Anbieter schreiben nur, ein Test sei bestanden.

## Was heißt das praktisch

Hy4 ist ab sofort über Tencent Cloud, OpenRouter und die eigenen Produkte CodeBuddy, WorkBuddy, Yuanbao und ima erreichbar. Eine Million Token Kontext, Bilder als Eingabe, Preise auf OpenRouter bei 0,42 Dollar je Million Eingabe-Token und 1,25 Dollar je Million Ausgabe-Token. Wer heute eine Agentenschleife für Dokumente, Tabellen oder Oberflächen baut, kann das Modell also testen, ohne auf die Gewichte zu warten.

Wer selbst hosten will, wartet. Wichtig wird dann die Systemkarte: Sie soll mit den Gewichten erscheinen und die Sicherheitstests offenlegen. Erst dort zeigt sich, ob die gefilterten Cyber-Daten das Modell auch bei legitimer Fehlersuche bremsen, und ob die Biowerte belastbar sind. Bis dahin bleiben die Fähigkeitszahlen das, was Tencent selbst schreibt: eigene Tests, eigene Bewerter, eigene Maßstäbe.

Für europäische Firmen kommt eine zweite Frage dazu, die nichts mit Technik zu tun hat. Ein Modell, das auf Tencent-Infrastruktur läuft und dessen Gewichte noch ausstehen, lässt sich schlecht auf Datenschutz prüfen. Bis die Gewichte da sind, bleibt Hy4 ein starkes Angebot für alle, die über eine API testen wollen, und eine Absichtserklärung für alle anderen.

## Quellen

- Tencent Hy, „Introducing Hy4", 4. November 2026: https://hy.tencent.ai/research/hy4?langVersion=en
- Channel News Asia, „Tencent rolls out AI model trained with limited cybersecurity data amid hacking fears", 4. November 2026: https://www.channelnewsasia.com/business/tencent-rolls-out-ai-model-trained-limited-cybersecurity-data-amid-hacking-fears-6523736
- OpenRouter, Modellseite Tencent Hy4 (Preise, Kontextfenster), abgerufen am 6. November 2026: https://openrouter.ai/tencent/hy4
- Kimi K3.1 Pro, Tech Blog zur Datenfilterung im Training: https://www.kimi.com/en/blog/kimi-k3-1-pro
