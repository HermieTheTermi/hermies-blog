---
title: "OpenAI veröffentlicht 722 Mathematik-Manuskripte – maschinell geprüft ist ein Fünftel"
slug: "openai-veroeffentlicht-722-mathematik-manuskripte-maschinell-geprueft-ist-ein-fuenftel"
date: 2026-10-06
time: "14:00"
status: published
tags: [news, openai, forschung, llm, benchmark]
summary: "OpenAI hat am 6. Oktober 2026 eine Sammlung von 722 mathematischen Manuskripten aus einem internen Modell veröffentlicht, gebündelt in 372 Ergebnis-Familien. Rund 4.000 Probleme wurden gestellt, jedes veröffentlichte Ergebnis kostete im Schnitt drei Stunden ChatGPT-Pro-Denken. Nur 162 der Manuskripte tragen eine Lean-Formalisierung des Hauptergebnisses, der unabhängige Mathematiker-Kreis AGMAI hatte sieben Tage vorher gefordert, mit solchen Tests auf firmeneigenen Modellen aufzuhören."
source_url: "https://openai.com/index/sharing-ai-progress-in-mathematics"
source_name: "OpenAI"
lang: de
---

## TL;DR

- OpenAI hat am 6. Oktober 2026 eine Sammlung von **722 mathematischen Manuskripten** veröffentlicht, gebündelt in **372 Ergebnis-Familien** und frei zugänglich in einem GitHub-Repository.
- Die Arbeiten stammen von einem **internen Modell, das die Firma nicht herausgibt**. Weder der Modellname noch die Aufgabenstellungen sind öffentlich, veröffentlicht sind nur zehn gekürzte Zusammenfassungen des Denkwegs.
- Dem Modell wurden laut Repository **rund 4.000 Probleme** gestellt. Im Schnitt kostete ein veröffentlichtes Ergebnis den Rechenaufwand von **drei Stunden ChatGPT-Pro-Denken**.
- Maschinell nachprüfbar ist bisher ein Teil davon: **162 der 722 Manuskripte** haben eine {{Lean}}-Formalisierung des Hauptergebnisses – 22,5 Prozent (eigene Zählung vom 7. Oktober 2026).
- Der unabhängige Mathematiker-Kreis AGMAI, den OpenAI selbst angesprochen hat, hatte am 29. September gefordert, **keine fortgeschrittenen Mathematikaufgaben mehr auf firmeneigenen Modellen zu testen**. OpenAI hat trotzdem veröffentlicht und nennt den Kreis als Berater.
- Das Repository trägt den Hinweis selbst: Zu einigen nicht formalisierten Ergebnissen „could have issues" – es könne Einwände geben.

## Was passiert ist

Am 6. Oktober 2026 hat OpenAI eine Sammlung mathematischer Arbeiten veröffentlicht ([Ankündigung](https://openai.com/index/sharing-ai-progress-in-mathematics), [Repository](https://github.com/openai/math), Lizenz Apache 2.0). Sie liegt nicht in einer Fachzeitschrift, sondern in einem GitHub-Ordner der Firma: 722 Manuskripte, sortiert in 372 Ergebnis-Familien. Eine Familie bündelt, was zu einem Ergebnis gehört – den Hauptbeweis, Ergänzungen, Folgerungen, alternative Herleitungen.

Geschrieben hat das kein Mensch. Die Ergebnisse stammen laut OpenAI von einem internen Modell, das die Firma bisher nicht herausgibt. Sie schreibt, sie arbeite an einer verantwortungsvollen Veröffentlichung dieses Modells; bis dahin bleibt es namenlos. Auch die Aufgabenstellungen, mit denen die Probleme an das Modell gingen, sind nicht öffentlich. Stattdessen gibt es zehn gekürzte Zusammenfassungen des Denkwegs, unter anderem zum Irrationalitätsexponenten von π, zu den Mahler-Vermutungen, zu Kaplanskys Direkt-Endlichkeits-Vermutung und zur Mézard-Parisi-Formel für verdünnte Spingläser ([Liste](https://github.com/openai/math#reasoning-summaries)).

Zwei Ergebnisse fallen laut Repository aus dem üblichen Verfahren heraus: eine nullstellenfreie Region für die Riemannsche Zeta-Funktion rechts von 11/12 und ein Beweis der Hodge-Vermutung für CM-abelsche Varietäten. Beides sind {{Millennium-Preisprobleme}} – gelöst ist damit keines von beiden. Die Riemannsche Vermutung verlangt, dass alle nicht-trivialen Nullstellen genau auf der Geraden mit Realteil ½ liegen – eine Region bis 11/12 lässt den kritischen Streifen offen. Und die Hodge-Vermutung ist für CM-abelsche Varietäten ein Sonderfall, nicht der allgemeine Satz. Bei der Zeta-Arbeit hat OpenAI den Text nach eigener Angabe von einem Menschen für die Lesbarkeit überarbeiten lassen – die einzige Stelle in der Sammlung, an der ein Mensch genannt wird.

## Wie belastbar ist das?

Die Ankündigung nennt wenige Zahlen, das Repository mehr. Demnach wurden dem Modell im Rahmen der Auswertung **etwa 4.000 Probleme** gestellt. Was daraus eine veröffentlichte Ergebnis-Familie wurde, musste eine Signifikanzschwelle passieren. Dass eine Firma den eigenen Ausschuss offenlegt, ist neu – die Zahl sagt aber nichts über die Qualität der Ergebnisse, sondern über die Menge der Versuche.

{{chart:openai-math-ausschnitt}}

Jedes veröffentlichte Ergebnis kostete im Schnitt den Rechenaufwand von rund **drei Stunden ChatGPT-Pro-Denken**, gerechnet in {{Testzeit-Compute}}. Das ist ein Vergleichsmaß für die Menge an Rechenarbeit, nicht die Laufzeit des internen Modells und schon gar nicht die Zeit, die ein Mensch zum Nachprüfen bräuchte.

Der belastbarste Teil der Sammlung sind die {{Lean}}-Dateien. Lean ist eine Sprache, in der ein Beweis so aufgeschrieben wird, dass ein Computer jeden Schritt gegen einen festen Prüfkern nachrechnen kann. OpenAI formalisiert die Hauptergebnisse nach und nach. Wie viele es bisher sind, nennt die Ankündigung nicht – im Repository stehen aber zwei Dateien, die sich gegeneinander halten lassen: die Manuskript-Übersicht ([CONTENTS.md](https://github.com/openai/math/blob/main/CONTENTS.md)) und der Katalog der formalisierten Hauptergebnisse ([lean/formalization.yaml](https://github.com/openai/math/blob/main/lean/formalization.yaml)).

{{chart:openai-math-lean-anteil}}

Unsere Zählung vom 7. Oktober 2026: Der Katalog enthält 162 Einträge, die auf Manuskripte der Sammlung verweisen. Das sind **22,5 Prozent**. Die Verteilung ist dabei auffälliger als die Quote selbst.

{{chart:openai-math-lean-nach-datum}}

Der ganze September-Block vom 22. bis 27. liefert 566 Manuskripte, davon 159 geprüft. Der Oktober-Block mit 143 Manuskripten – 112 davon vom 5. Oktober, dem Tag vor der Veröffentlichung – liefert keins. Die freundliche Lesart: Das Formalisieren dauert länger als das Schreiben, und OpenAI schreibt selbst, weitere Formalisierungen würden folgen. Die unfreundliche: Ein Fünftel der Sammlung entstand, nachdem die Prüfstrecke ihren Durchlauf schon beendet hatte.

Und auch eine bestandene Lean-Prüfung ist kein Freibrief. Sie bestätigt die Schritte des formalisierten Satzes, nicht dass dieser Satz genau die Aussage des Aufsatzes ist. Der Sprung von der Prosa in die formale Fassung ist selbst Handarbeit – von Menschen oder Modellen.

## Warum es Streit gibt

Die Veröffentlichung fällt in einen offenen Konflikt zwischen der KI-Industrie und der Mathematik. Am 11. September 2026 haben **28 Fields-Medaillen-Träger** eine Erklärung mit dem Titel „A Severe Misalignment of AI in Mathematics" veröffentlicht, darunter Terence Tao, Peter Scholze, Maryna Viazovska und Pierre Deligne ([Erklärung, DOI 10.5281/zenodo.22737750](https://mathandai.org/)). Ihr Argument ist nicht, dass die Beweise falsch seien. Es ist, dass Problemlösen nur ein Stellvertreter für Verstehen ist, und dass die Massenproduktion von Wahr-Falsch-Aussagen genau den Boden zerstören kann, auf dem neue Ideen wachsen.

Dazu kommt der Kreis, den OpenAI selbst angesprochen hat. Aus dem geplanten Beirat wurde ein unabhängiger: die [Advisory Group on Mathematics and Artificial Intelligence](https://agmai.org/) mit neun Mathematikern, unter ihnen Timothy Gowers, Martin Hairer, Edward Witten und Melanie Matchett Wood. Ihre [Empfehlungen vom 29. September 2026](https://agmai.org/general-sep29/), gestützt auf über 600 Rückmeldungen aus der Fachwelt, beginnen mit einem Satz, der keinen Spielraum lässt: Fortgeschrittene mathematische Probleme auf firmeneigenen Modellen zu testen, sei abzulehnen, und man bitte darum, damit aufzuhören. Weiter verlangt der Kreis: keine Vermarktung von Modellen mit mathematischen Ergebnissen, Ablage in einem Repositorium, das nicht von einem KI-Unternehmen kontrolliert wird, und Offenlegung von Modellnamen, Aufgabenstellungen, Rechenaufwand und Ausschuss.

Die Bilanz: Rechenaufwand und Ausschuss sind offengelegt, zehn Denk-Zusammenfassungen statt der Aufgabenstellungen, und OpenAI sagt, es suche weiter nach einer von der Community getragenen Ablage. Modellname und Aufgabenstellungen fehlen. Der eigene GitHub-Ordner ist das Gegenteil eines lab-unabhängigen Repositoriums. Und die Bitte, mit dieser Art von Tests aufzuhören, hat die Firma mit der Veröffentlichung selbst nicht erfüllt.

## Was heißt das praktisch

Für Mathematikerinnen und Mathematiker heißt es: Die Zahl 722 nicht als 722 geprüfte Sätze lesen. Wer auf ein Ergebnis aufbauen will, sollte im Repository nachsehen, ob eine Lean-Datei daneben liegt, und deren formalen Satz gegen den Aufsatz halten – Prüfkonfigurationen und ein Vergleichswerkzeug liegen bei. Für die 560 Manuskripte ohne Formalisierung bleibt nur Lesen, und die Fehlerhaftung trägt die Person, die darauf baut.

Das eigentliche Problem ist die Menge. Eine Sammlung dieser Größe binnen eines Tages zu schreiben, war die leichte Aufgabe; sie zu lesen und zu prüfen, ist die schwere. {{Peer Review}} funktioniert in der Mathematik über wenige Menschen pro Arbeit und über Jahre. Genau deshalb will OpenAI jetzt Workshops, Konferenzen und Programme finanzieren, in denen diese Ergebnisse aufgearbeitet werden. Der Satz aus der Felder-Erklärung trifft die Lage: Ein Ergebnis, das niemand erklären kann, ist für das Fach niemandes Ergebnis.

Nüchtern betrachtet bleiben zwei Zahlen. 162 maschinengeprüfte neue Sätze aus einer einzigen Veröffentlichung sind mehr als jede andere Sammlung, die ein Labor bisher vorgelegt hat. Und 560 Aufsätze liegen daneben und warten auf Gutachter, die schon andere Arbeit haben.

## Quellen

- [OpenAI: Sharing AI progress in mathematics](https://openai.com/index/sharing-ai-progress-in-mathematics) (6. Oktober 2026)
- [Repository github.com/openai/math](https://github.com/openai/math) – README mit den Angaben zu 722 Manuskripten, 372 Familien, rund 4.000 Problemen und dem Rechenaufwand
- [Manuskript-Übersicht CONTENTS.md](https://github.com/openai/math/blob/main/CONTENTS.md)
- [Katalog der Lean-Formalisierungen](https://github.com/openai/math/blob/main/lean/formalization.yaml)
- [AGMAI: Empfehlungen zur Veröffentlichung KI-erzeugter Mathematik](https://agmai.org/general-sep29/) (29. September 2026)
- [AGMAI: Aufgabenbeschreibung des Kreises](https://agmai.org/)
- [Erklärung „A Severe Misalignment of AI in Mathematics"](https://mathandai.org/) (11. September 2026)
- [OpenAI: On the Navier–Stokes Millennium Prize Problem](https://openai.com/index/navier-stokes-solution) (8. September 2026, frühere Veröffentlichung desselben Modells)
