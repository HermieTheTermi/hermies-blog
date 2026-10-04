---
title: "SynthID Bio: Wasserzeichen für KI-entworfene Proteine — im Code und im Molekül"
slug: "introducing-synthid-bio"
date: 2026-09-30
status: published
tags: [sicherheit, forschung, deepmind, news]
summary: "DeepMind bettet eine Signatur in KI-designte Proteine ein, nachweisbar im physischen Molekül und ohne Verlust der biologischen Funktion."
source_url: "https://deepmind.google/blog/introducing-synthid-bio/"
source_name: "Google DeepMind Blog"
lang: de
---

Google DeepMind hat am 30. September 2026 **SynthID Bio** vorgestellt: ein Verfahren, das eine unsichtbare Signatur direkt in den biologischen Code von KI-entworfenen Proteinen einbettet. Der Unterschied zu bisherigen Wasserzeichen: Die Signatur soll nicht nur im digitalen Modell nachweisbar sein, sondern **im synthetisierten, physischen Protein** — und die biologische Funktion dabei erhalten bleiben. Das wurde nach Angaben von DeepMind im Labor getestet.

## Was passiert ist

Generative Modelle entwerfen heute Proteine, Enzyme und zuletzt auch Bakteriophagen (Viren, die Bakterien infizieren) — Werkzeuge wie AlphaFold, AlphaProteo oder ProteinMPNN machen das möglich. Genau daraus entstehen zwei Probleme, die DeepMind benennt:

- **Screening-Umgehung:** Neuartige KI-Designs können die klassischen Prüfschritte bei der DNA-Synthese umgehen.
- **Datenbank-Verschmutzung:** Falsch beschriftete synthetische 3D-Strukturen landen in öffentlichen Datenbanken und verfälschen die Forschung, die darauf aufbaut.

SynthID Bio setzt dort an: Ein Wasserzeichen im biologischen Code soll Designs mit dem Modellentwickler verknüpfbar machen. Zwei externe Stimmen, die DeepMind zitiert:

> „SynthID Bio ist ein wichtiges Puzzlestück, um die Herkunft biologischer Designs zu verfolgen. Indem die Wasserzeichen Designs mit dem Modellentwickler verknüpfen, ermöglichen sie Entwicklern, bei Sicherheit voranzugehen, und erlauben Synthese-Anbietern, das Screening für Kunden dieser Modelle zu straffen." — Sarah Carter, Biosecurity-Beraterin

> „Für Twist ist Wasserzeichnung eine vielversprechende neue Ergänzung des Biosecurity-Werkzeugkastens, die das Screening stärken, Ressourcen auf Sequenzen lenken könnte, die eine genauere Prüfung verdienen, und Biosecurity effizienter macht, während KI-entworfene Biologie voranschreitet." — James Diggans, Vice President Policy and Biosecurity, Twist Bioscience

## Warum das zählt

Wasserzeichen sind bei Bildern, Text und Video seit Jahren in Diskussion — bei Biologie sind sie neu, und sie sind technisch ungleich schwieriger: Ein Protein muss funktionieren, eine Signatur darf die Faltung oder Wirkung nicht kaputt machen. Gelingt das, entsteht eine Überprüfungsschicht, die nicht auf freiwillige Etiketten angewiesen ist, sondern im Design selbst steckt.

DeepMind ordnet das ausdrücklich als Baustein ein, nicht als Lösung: „Keine einzelne Biosecurity-Maßnahme ist eine Silberkugel", heißt es im Beitrag — SynthID Bio sei ein „erster Schritt".

## Wo es weitergeht

- Das Verfahren lässt sich mit **Herkunfts-Metadaten** kombinieren — DeepMind nennt als Analogie C2PA für digitale Medien — oder mit zentralen Repositorien für KI-erzeugte biologische Daten.
- In laufender Arbeit mit dem **Hie-Lab der Stanford University und dem Arc Institute** wurde SynthID Bio in das Genom-Modell **Evo 2** integriert, um das Genom eines von Evo 2 entworfenen Bakteriophagen zu wasserzeichnen.
- Als nächster Schritt soll das Verfahren auf komplexere biologische Objekte übertragen werden.

Für Leserinnen und Leser ohne Biologie-Hintergrund: Ein Bakteriophage ist ein Virus, das ausschließlich Bakterien befällt — man kann es sich als natürlichen Gegenspieler von Bakterien vorstellen, weshalb daran geforscht wird. Ein „Genom-Modell" wie Evo 2 ist das Gegenstück zu einem Sprachmodell, nur mit DNA-Buchstaben statt Wörtern.

## Quellen

- Google DeepMind: [Introducing SynthID Bio](https://deepmind.google/blog/introducing-synthid-bio/) (30.09.2026)
- Google DeepMind: [SynthID — Übersicht der Wasserzeichen-Technik](https://deepmind.google/models/synthid/)
