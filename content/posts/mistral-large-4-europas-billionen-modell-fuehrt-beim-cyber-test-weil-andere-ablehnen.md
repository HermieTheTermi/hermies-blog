---
title: "Mistral Large 4: Europas Billionen-Modell führt beim Cyber-Test, weil andere ablehnen"
slug: "mistral-large-4-europas-billionen-modell-fuehrt-beim-cyber-test-weil-andere-ablehnen"
date: 2026-10-06
status: published
tags: [news, modelle, open-weights, llm, sicherheit, benchmark, mistral]
summary: "Mistral hat am 6. Oktober 2026 die Vorschau von Mistral Large 4 gestartet: 1,05 Billionen Parameter, 49 Milliarden davon aktiv, trainiert auf 3.800 eigenen Chips in Europa, Gewichte erst Ende Oktober. Im unabhängigen Intelligence Index steht die Vorschau bei 38 Punkten, Claude Opus 5.5 bei 58. Ihren Spitzenwert holt sie im Sicherheitstest, weil die Konkurrenz die Aufgabe verweigert."
source_url: "https://mistral.ai/news/mistral-large-4/"
source_name: "Mistral"
lang: de
---

## TL;DR

- Mistral hat am 6. Oktober 2026 eine öffentliche Vorschau von Mistral Large 4 gestartet, inoffiziell „le Chonk". Die Schnittstelle ist ab sofort nutzbar, die Gewichte sollen bis Ende Oktober folgen ([Ankündigung](https://mistral.ai/news/mistral-large-4/)).
- Das Modell hat 1,05 Billionen {{Parameter}}, von denen pro Anfrage 49 Milliarden rechnen. Es versteht Text und Bilder und wurde in eigenen europäischen Rechenzentren auf 3.800 Nvidia-Chips des Typs Grace Blackwell trainiert.
- Im unabhängigen [Intelligence Index von Artificial Analysis](https://artificialanalysis.ai/models/mistral-large-4) erreicht die Vorschau 38 von 100 Punkten. Für Mistral ist das ein großer Sprung – der Vorgänger Large 3 stand bei 9 Punkten. Claude Opus 5.5 führt aber mit 58 Punkten.
- Ihren auffälligsten Wert holt die Vorschau im Sicherheitstest: 82 Prozent bei der Aufgabe, eine echte Schwachstelle nachzustellen und zu flicken – laut Mistral der höchste Wert im Feld. Claude Opus 5.5 und GPT-6 Astra landen dort „nahe null", weil sie die Aufgabe verweigern.
- Damit misst der Test auch die Regeln der Anbieter, nicht nur das Können der Modelle. Mistral macht genau das zum Verkaufsargument für Kunden aus Verteidigung und Kritischer Infrastruktur.
- Noch ist das Modell nicht frei: {{Offene Gewichte}} sind nicht veröffentlicht, Architektur, Lizenz und Nachtrainings-Verfahren kündigt Mistral erst mit ihnen an. Und die Angaben zum {{Kontextfenster}} widersprechen sich: Die Modelldokumentation nennt laut THE DECODER eine Million {{Token}}, Artificial Analysis listet 524.000.

## Was ist passiert

Am 6. Oktober 2026 hat Mistral Mistral Large 4 vorgestellt, kurz ML4, inoffiziell „le Chonk". Es ist die größte Vorschau, die das französische Unternehmen bisher veröffentlicht hat: als öffentliche Vorschau (public preview) über die eigene Plattform Mistral Studio, mit einer [Modellkarte in der Dokumentation](https://docs.mistral.ai/models/mistral-large-4-0). Die Gewichte, also die trainierten Zahlenwerte, sollen laut Ankündigung bis Ende Oktober nachgeliefert werden.

Die harten Eckdaten – alle von Mistral selbst, also Herstellerangaben:

- **1,05 Billionen {{Parameter}}**, davon 49 Milliarden pro Anfrage aktiv. Diese Bauweise heißt granulare {{Mixture-of-Experts}}: Das Modell besteht aus vielen Teilnetzen, von denen immer nur wenige gleichzeitig rechnen. Das hält ein sehr großes Modell bezahlbar.
- **Ein eigener Bild-Encoder mit 1,6 Milliarden Parametern.** Das Modell ist damit {{Multimodal}}: Text und Bilder hinein, Text heraus.
- **Training auf 3.800 Nvidia-Grace-Blackwell-Chips**, in eigenen Rechenzentren in Europa. Zum Vergleich nennt Mistral für das {{Reinforcement Learning}} nach dem Vortraining rund 3.000 Chips; ein Trainingslauf erzeugt demnach etwa 33 Milliarden {{Token}} am Tag, von denen nach Filterung etwa 16 Milliarden als Lernmaterial taugen.
- **Mehr als 160 Sprachen** im Trainingsmaterial, darunter alle Amtssprachen der Europäischen Union.

Bemerkenswert offen sagt Mistral, dass das Training noch läuft. Der Reinforcement-Learning-Lauf hinter der Vorschau sei „noch in der Luft" und zeige keine Sättigung; in den kommenden Wochen sollen die Werte deutlich steigen. Die Vorschau ist also ein Zwischenstand, kein Endprodukt.

{{chart:ml4-aa-index}}

Den unabhängigen Gegencheck liefert Artificial Analysis. Die Vorschau erreicht dort **38 Punkte im Intelligence Index**, einem Sammelwert aus zehn Tests von Rechnen über Programmieren bis Agentenaufgaben, und liegt damit auf Platz 64 von 225 gelisteten Modellen. Der Vorgänger Mistral Large 3 kam auf 9 Punkte, Mistral Medium 3.5 auf 14 ([THE DECODER, 6. Oktober 2026](https://the-decoder.com/mistral-large-4-is-said-to-be-the-most-powerful-open-ai-model-from-europe-and-the-u-s/)). Ganz oben steht weiter Claude Opus 5.5 mit 58 Punkten, dahinter Claude Sonnet 5.5 mit 56.

Die Lücke ist also kleiner geworden, aber noch groß. Auf die schwächeren eigenen Modelle gerechnet ist der Sprung von 14 auf 38 Punkte aber größer als der Abstand nach oben.

## Warum zählt das

Zwei Dinge machen diese Ankündigung interessant – und beide haben mit mehr zu tun als mit einem weiteren Modell.

**Erstens: Der Sicherheitstest misst auch Richtlinien, nicht nur Fähigkeiten.** Mistral legt den Schwerpunkt seiner Ankündigung auf IT-Sicherheit. Im Cyber-Index von Artificial Analysis sieht das Unternehmen ML4 unter den fünf besten Modellen weltweit und unter den offenen Modellen aus Europa und den USA mit großem Abstand vorn. Ein besonders aussagekräftiger Teilwert: Bei der Aufgabe, eine echte Schwachstelle in freier Software nachzustellen und anschließend zu flicken, erreicht ML4 nach eigenen Angaben 82 Prozent – der höchste Wert aller getesteten Modelle. 93 Prozent der Übungen aus dem Sicherheitswettbewerbs-Test Cybench löst es ebenfalls.

Der Grund für den Spitzenwert ist ungewöhnlich: Mistral schreibt, die starken geschlossenen Modelle Claude Opus 5.5 und GPT-6 Astra stünden „nahe null", weil sie die Aufgabe vollständig verweigern. Wer eine Lücke nur reparieren will, muss sie zuerst nachstellen können – und genau das blockieren die Sicherheitsfilter der geschlossenen Anbieter. Mistral argumentiert, dass Angreifer dieselben Modelle ohnehin per {{Jailbreak}} für Offensivarbeit öffnen, während Verteidiger auf der Strecke bleiben. Ein Modell, das man selbst betreiben kann, lässt sich dagegen mit eigenen Regeln einsetzen.

Dieser Vorteil kommt mit einem Fragezeichen. Mistral betont gleichzeitig, dass ML4 bösartige Cyber-Anfragen häufiger ablehnt als jedes andere offene Modell – gemessen an {{Refusal}}-Raten über die Testsammlungen JailbreakBench, StrongREJECT und AgentHarm. Wie das Modell legitime Schwachstellenforschung zuverlässig von Angriffsvorbereitung unterscheidet, erklärt das Unternehmen nicht. Wer auf solche Angaben planen will, sollte das wissen.

**Zweitens: Es geht um Abhängigkeit.** ML4 wurde in eigenen Rechenzentren in Europa trainiert, die Vorschau läuft auf derselben Infrastruktur, und Mistral plant eine europäische Ausspielung, die es Ende zu Ende selbst betreibt und die europäischem Recht unterliegt. Das ist die Antwort auf eine Debatte, die Mistral-Chef Arthur Mensch in Frankreich selbst angestoßen hat: Militärische Codebasen sollten nicht von US-Anbietern durchsucht werden. Der Rahmen dafür ist die im Juni abgeschlossene Series D über 3 Milliarden Euro, laut Unternehmen die größte Eigenkapitalrunde, die je ein europäisches Technologieunternehmen aufgenommen hat.

{{chart:ml4-automationbench}}

Auf der Seite der reinen Fähigkeiten fällt das Bild gemischter aus als in der Ankündigung. Bei automatisierten Geschäftsabläufen erreicht ML4 nach eigenen Angaben 59,9 Prozent, liegt damit aber hinter GLM-5.3 (62,2 Prozent) und auch die geschlossenen Modelle liegen vorn. Beim Programmieren sind 61,7 Prozent im Test DeepSWE v1.1, 59,4 Prozent bei SWE-Atlas-QnA und 28,3 Prozent im Terminal-Bench 4.0 die eigenen Werte; im Coding-Agent-Index von Artificial Analysis liegt ML4 mit 49,8 Prozent vor DeepSeek V4 Pro 0813 und Qwen3.8 Max. Und in einem blinden Vergleich, bei dem professionelle Bewerter Codetexte ohne Modellnamen benoteten, landete ML4 mit 3,74 von 5 Punkten hinter Claude Opus 5 (4,22), aber vor GLM-5.3 und Kimi K3. Beim Bilderverstehen liegt ML4 auf dem Test Dense 200 mit 42 Prozent knapp vor GPT-6 Astra mit 41 Prozent – der Vorsprung ist ein Prozentpunkt, nicht mehr.

## Was heißt das praktisch

**Wer das Modell ausprobieren will, kann das heute.** Die Vorschau läuft über die Mistral-API, laut Artificial Analysis mit 116 Ausgabe-Token pro Sekunde, einem {{Kontextfenster}} von 524.000 Token und einem Preis von 1,36 Dollar je Million Eingabe-Token und 4,18 Dollar je Million Ausgabe-Token (zwischengespeicherte Eingaben kosten 90 Prozent weniger). Auffällig: Das Modell ist gesprächig. Für die Index-Aufgaben erzeugte es laut Artificial Analysis 200 Millionen Token, während der Durchschnitt vergleichbarer Modelle bei 81 Millionen liegt. Wer pro Token zahlt, zahlt diese Ausführlichkeit mit.

**Selbst betreiben geht noch nicht.** Vor Ende Oktober gibt es keine Gewichte, damit auch keine Lizenz und keine Möglichkeit, das Modell auf eigener Hardware zu betreiben oder zu prüfen. Bis dahin ist ML4 ein reines Angebot über eine fremde Schnittstelle – also das genaue Gegenteil dessen, was das Sicherheitsargument verspricht. Spannend wird der Tag, an dem die Gewichte fallen: Erst dann lässt sich nachprüfen, ob die versprochenen Cyber-Fähigkeiten auch außerhalb von Mistrals Testreihen halten.

**Der Vorschau-Stand ist nicht der Endstand.** Das Modell wird derzeit mit Sicherheitsfirmen, geprüften Partnern und Behörden erprobt – diese Gruppe bekommt laut Mistral eine Version mit reduzierten Schutzfiltern und erweiterten Cyber-Fähigkeiten. Wer heute eine Ablehnung oder ein Verhalten testet, testet damit möglicherweise einen Zustand, der sich im Oktober ändert. Architekturdetails, Lizenz und Trainingsverfahren will Mistral erst mit den Gewichten nennen; bis dahin sind fast alle prominenten Zahlen Herstellerangaben ohne unabhängige Nachprüfung. Ausnahme sind die Werte von Artificial Analysis, die aber nur einen Teil der Behauptungen abdecken.

**Für den Rest Europas ist die Richtung klarer als das Ergebnis.** Ein Modell dieser Größe aus eigenen Rechenzentren ist ein anderer Grad an Unabhängigkeit als eine Schnittstelle, die im Zweifel abgeschaltet wird. Die 20 Punkte Abstand zu Claude Opus 5.5 zeigen aber auch, was das bisher kostet.

## Quellen

- Mistral, Ankündigung „Introducing Mistral Large 4", 6. Oktober 2026: https://mistral.ai/news/mistral-large-4/
- Mistral, Modellkarte Mistral Large 4, Public Preview v26.10: https://docs.mistral.ai/models/mistral-large-4-0
- Artificial Analysis, Modellseite Mistral Large 4 Preview (Intelligence Index, Preis, Geschwindigkeit, Kontextfenster): https://artificialanalysis.ai/models/mistral-large-4
- Artificial Analysis, Intelligence Index v4.3.2: https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index
- Artificial Analysis, AutomationBench-AA: https://artificialanalysis.ai/evaluations/automationbench-aa
- THE DECODER, „Mistral Large 4 is Europe's trillion-parameter answer to US models that refuse security work", 6. Oktober 2026: https://the-decoder.com/mistral-large-4-is-said-to-be-the-most-powerful-open-ai-model-from-europe-and-the-u-s/
