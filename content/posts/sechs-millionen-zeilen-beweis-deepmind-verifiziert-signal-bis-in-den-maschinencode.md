---
title: "Sechs Millionen Zeilen Beweis: DeepMind verifiziert Signal bis in den Maschinencode"
slug: "sechs-millionen-zeilen-beweis-deepmind-verifiziert-signal-bis-in-den-maschinencode"
date: 2026-11-10
time: "13:02"
status: published
tags: [news, google, deepmind, forschung, sicherheit, llm]
summary: "Google DeepMind hat am 10. November AlphaProof Code vorgestellt, ein Framework, in dem Agenten formale Beweise über kompilierten Code schreiben. Erster Einsatz ist libsignal, unverändert mit rustc nach AArch64 übersetzt: rund 6,5 Millionen Zeilen Lean-Beweis, geprüft vom Lean-Kernel, für Vorwärtsgeheimhaltung, Authentifizierung und Erholung nach Schlüsseldiebstahl. Ein Team aus fünf Personen brauchte vier Wochen; Krypto-Primitive gelten als sicher, geprüft wurde eine Plattform ohne Gruppenchats, begutachtet ist die Arbeit nicht."
source_url: "https://deepmind.google/blog/introducing-alphaproof-code/"
source_name: "Google DeepMind"
lang: de
---

## TL;DR

- Google DeepMind hat am 10. November ein Framework namens AlphaProof Code vorgestellt, in dem Agenten Beweise über kompilierten Code schreiben ([Ankündigung](https://deepmind.google/blog/introducing-alphaproof-code/)).
- Erster Einsatz ist libsignal, die Referenzimplementierung des Signal-Protokolls, unverändert mit dem Rust-Compiler nach AArch64 übersetzt: rund 6,5 Millionen Zeilen {{Lean}}-Beweis, geprüft vom Lean-Kernel.
- Bewiesen sind Vorwärtsgeheimhaltung, Authentifizierung, Erholung nach Schlüsseldiebstahl und die Geheimheit des Handshakes, sowohl im symbolischen als auch im computationalen Sicherheitsmodell.
- Ein Team aus fünf Personen brauchte vier Wochen. Zum Vergleich: die Verifikation des Mikrokerns seL4 kostete zwanzig Personenjahre.
- Die Grenzen stehen im Papier: Krypto-Primitive gelten als sicher, geprüft wurde eine Plattform und ein Prozess ohne Gruppenchats, und die Sicherheitsschranke wird bei großen Sitzungen leer. Begutachtet ist die Arbeit nicht.

## Was ist passiert

Am 10. November hat Google DeepMind ein Papier veröffentlicht und dazu eine Ankündigung, die den Ton großer Forschungserfolge trägt. Die Autorengruppe um Swarat Chaudhuri und Pushmeet Kohli beschreibt darin einen Beweis, dass der Code hinter dem Signal-Protokoll die versprochenen Sicherheitseigenschaften tatsächlich einhält. Nicht das Design auf Papier, nicht eine eigens für den Beweis umgeschriebene Nachbildung, sondern das kompilierte Programm.

Signal ist der Standard für Ende-zu-Ende-verschlüsselte Nachrichten. Neben der Signal-App stecken Varianten des Protokolls in WhatsApp, im Messenger von Meta und in Google Messages. Was in libsignal falsch läuft, betrifft Milliarden Gespräche.

Die Bibliothek libsignal liegt in Version 0.105.4 vor, dazu die Kryptobibliothek spqr in Version 1.6.0. Das Team hat den unveränderten Rust-{{Quellcode}} mit dem Standard-Compiler rustc auf einem AArch64-Prozessor übersetzt, also auf der Architektur, auf der Mobiltelefone und viele Server laufen. Verifiziert wurden nach Angaben im Papier etwa 140.000 Maschinenbefehle, rund 560 Kilobyte Programm. Wer die Beweise nachlesen will, findet sie unter google-deepmind.github.io/code-verification.

{{zahlen:alphaproof-zahlen}}

## Warum zählt es

{{Formale Verifikation}} galt lange als Handarbeit für Heldenteams. Der verifizierte Mikrokern seL4 verschlang nach Angaben im Papier zwanzig Personenjahre, der verifizierte C-Compiler CompCert sechs. In beiden Fällen war der {{Quellcode}} von Anfang an auf die Verifikation hin geschrieben. Bestehende Industrieprogramme nachträglich zu beweisen ist schwerer, weil der Beweisführer den Code nicht vereinfachen darf.

Genau diese Lücke will das Framework schließen, und der Hebel ist ein anderer als erwartet. In der Analyse der eigenen Arbeit schreiben die Autoren, der größte Teil des Aufwands sei nicht in die Beweise gegangen, sondern in die Frage, was überhaupt bewiesen werden soll. Die {{Spezifikation}} ist der Teil, den ein Mensch verantwortet: die Theoreme, die Annahmen über Umgebung und Angreifer, die Definitionen, von denen die Theoreme abhängen.

Der Beweis selbst darf schludrig sein, solange er falsch ist. Der Lean-Kernel nimmt nur Beweise an, die er Schritt für Schritt nachrechnet, und darum hängt die Zuverlässigkeit des Ergebnisses nicht an der Zuverlässigkeit der Agenten. Das ist der Kern des Verfahrens: Menschen legen fest, was gilt, Maschinen erledigen den Rest.

Sauber wird es dadurch aber nur, wenn die Spezifikation stimmt. Ist sie zu schwach, beweist der Kernel wahrhaftig eine Aussage, die niemanden schützt. Für dieses Problem hat das Team mehrere Gegenmittel eingebaut, und sie sind der interessante Teil des Papiers.

## Wie die Agenten arbeiten

Ein Spezifikations-Agent arbeitet mit dem Menschen aus der Literatur bekannte Sicherheitsmodelle in Lean-Definitionen um. Prüf-Agenten lesen jeden Entwurf mit skeptischem Blick, der Mensch gibt ihn frei, und der freigegebene Stand wird als Git-Commit eingefroren. Damit steht fest, wogegen später geprüft wird.

Die zweite Zutat ist eine Semantik der Architektur. Die Gruppe hat in Lean beschrieben, wie ein AArch64-Prozessor in einem Linux-Prozess Befehle ausführt, 467 Befehle und 31 Systemaufrufe auf 7.532 Zeilen. Diese Beschreibung muss stimmen, sonst beschreibt der Beweis ein anderes Programm als das laufende. Prüfen lässt sich das nicht, also wurde getestet: Befehl für Befehl gegen den Emulator Unicorn und gegen das Sail-Modell der Arm-Architektur, das aus Arms offizieller Spezifikation abgeleitet ist.

Dann beginnt die Beweisarbeit. Ein Orchestrator verteilt Aufgaben an Beweis-Agenten und gruppiert sie unter Teamleiter, ein Architekt legt die Zerlegung fest, ein Integrator führt geprüfte Lemmata in Bibliotheken zusammen. In den Kampagnen arbeiteten laut Papier typischerweise 40 bis 80 Agenten auf einer einzigen Maschine, zwischen 24 und 72 Stunden lang.

Ist ein Beweis fertig, tritt ein Kontrolleur auf den Plan. Er vergleicht mit der eingefrorenen Kopie der Spezifikation, lässt Lean den Kernel rechnen und nimmt den Beweis nur an, wenn das Theoremwortlaut und jede abhängige Definition unverändert ist. Änderungen an der Spezifikation sind erlaubt, aber nur über einen Kritiker-Agenten, der die Beweisansätze nicht sieht und drei Bedingungen prüft: Die Änderung muss durch einen maschinell geprüften Gegenbeweis begründet sein, sie darf die Sicherheit nicht abschwächen, und sie muss klein bleiben.

Ob die Spezifikation echte Fehler fängt, hat das Team an zwei bekannten Fehlern getestet. Beide waren in libsignal gefunden und behoben worden, unter anderem einer, bei dem eine Nachricht nur unter einer archivierten Sitzung entschlüsselt wurde und die Bibliothek trotzdem den Zustand der neuen Sitzung speicherte, samt Kopie des geheimen Signed Prekey. Das Team baute beide Fehler wieder ein und erhielt einen maschinell geprüften Beweis, dass die fehlerhafte Version die Sicherheitssätze verletzt.

## Was der Beweis nicht abdeckt

Das Papier ist in diesem Punkt ungewöhnlich offen, und die Liste ist länger als die Überschrift vermuten lässt. Die Kryptografie selbst wird nicht bewiesen. Diffie-Hellman, Kyber1024, AES, HMAC und die Hashfunktionen gelten als Verträge mit bestimmten Eigenschaften. Wer einen Fehler in diesen Bausteinen findet, hat einen Weg um den Beweis herum.

Die Sicherheit der Maschinensemantik ist getestet, nicht bewiesen. Hardware und Betriebssystem sind keine formalen Objekte. Wer die Aussage über das laufende Programm glauben will, muss der Beschreibung von 467 Befehlen vertrauen, geprüft gegen zwei unabhängige Modelle.

{{vergleich:alphaproof-grenzen}}

Dazu kommen Grenzen des Modells. Die Semantik beschreibt einen einzelnen Thread ohne Signale und ohne dynamisches Linken. Im symbolischen Beweis sind höchstens zwei Teilnehmer erfasst, und die Erholung nach einem Angriff mit gebrochenem Diffie-Hellman ist nicht abgedeckt. Im computationalen Beweis wird die Schranke leer, sobald eine Sitzung etwa 25.000 Nachrichten umfasst oder ein Angreifer über sehr viele Sitzungen rechnet. Gruppenchats hat das Team ausdrücklich auf später verschoben.

Für Kryptografen ist außerdem wichtig, was mit den Ergebnissen älterer Arbeiten passiert: Die computationalen Theoreme von Bhargavan und Kollegen haben hier kein Gegenstück, und die Arbeit zeigt, dass der Triple Ratchet nicht schwächer ist als der Double Ratchet, nicht aber die post-quantum Erholung, die SPQR beisteuert.

::: methode
Gelesen wurden Ankündigung und technisches Papier vom 10. November 2026, rund 220.000 Zeichen, inklusive der Abschnitte zu Grenzen und Vertrauensbasis. Zahlen stammen aus Abschnitt 7 des Papiers, die Einordnung von seL4 und CompCert aus der Einleitung. Ein unabhängiger Nachbau der Beweise liegt nicht vor, das Papier ist nicht begutachtet.
:::

## Was heißt das praktisch

Wer Software prüfen lässt, bekommt mit diesem Verfahren eine andere Rechnung. Bisher war formale Verifikation ein Projekt für Betriebssystemkerne und Chip-Design, weil sie Jahre kostete. Vier Wochen für eine Kryptobibliothek von dieser Bedeutung verschieben die Grenze. DeepMind nennt selbst medizinische Geräte und Stromnetze als nächste Ziele.

Der Aufwand verlagert sich dabei zu den Menschen, die die Spezifikation schreiben. Das Papier nennt das die eigentliche Lektion: Wenn Beweise billig werden, wird die Frage teuer, was zu beweisen ist. Wer eine Sicherheitszusage formuliert, muss entscheiden, gegen welchen Angreifer sie gilt und was sie ausdrücklich nicht umfasst. Genau diese Entscheidung bleibt Handarbeit.

Für Signal-Nutzer ändert sich nichts am Programm, und das ist keine schlechte Nachricht. Der Beweis fand keine neue Lücke, sondern bestätigte, was das Protokoll verspricht. Für alle anderen ist der belastbare Teil des Ergebnisses die Vertrauensbasis: etwa 26.000 Zeilen, die ein Prüfer lesen muss, um den Beweisen zu glauben. Der Rest ist Rechenzeit.

Bemerkenswert ist der Zusammenhang mit der eigenen Modellreihe. Die Beweise schrieben Agenten auf Basis von Gemini Carbon, dem Modell, das Google im Oktober als sein stärkstes vorgestellt hat. DeepMind baut damit die Werkzeuge, mit denen sich die Sicherheit von Software prüfen lässt, aus dem eigenen Modell. Ob das Verfahren auch außerhalb der Kryptografie trägt, entscheidet sich beim nächsten Ziel, das sich das Team vornimmt.

## Quellen

- Google DeepMind, „Introducing AlphaProof Code: a breakthrough in verifying complex software at depth", 10. November 2026: https://deepmind.google/blog/introducing-alphaproof-code/
- Chaudhuri, Ferraiuolo, Kovsharov, Chajed, Schlesinger, Seth, Katz, Sutton, Kohli, „AlphaProof Code: Verifying Signal's Security at the Machine-Code Level", Google DeepMind, 10. November 2026: https://deepmind.google/documents/36/Formal_Verification_of_Signal_4.pdf
- Lean-Entwicklung und Beweise: https://google-deepmind.github.io/code-verification
- The Register, „Google DeepMind melds humans and AI agents to vet Signal's secure messaging techniques", 10. November 2026: https://www.theregister.com/ai-and-ml/2026/11/10/google-deepmind-melds-humans-and-ai-agents-to-vet-signals-secure-messaging-techniques/5308625
- Eigener Artikel zu AlphaProof Nexus, 12. Oktober 2026: /alphaproof-nexus-neun-offene-mathe-probleme-begutachtet-statt-nur-behauptet.html
