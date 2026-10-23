---
title: "Claude beweist Code: 180 Millionen Zeilen für 123 Open-Source-Bibliotheken"
slug: "claude-beweist-code-180-millionen-zeilen-fuer-123-open-source-bibliotheken"
date: 2026-10-22
status: published
tags: [news, llm, sicherheit, forschung]
summary: "Anthropic hat mit dem Start-up Theorem gezeigt, dass Claude formale Beweise für echten Code schreiben kann: 239 Testeinstiege in 123 Open-Source-Bibliotheken, rund 180 Millionen Zeilen Beweiscode in wenigen Wochen, hunderte gefundene Fehler. Der bewiesene Satz gilt allerdings nur für einthreadige RISC-V-Programme mit Eingaben unter 64 MB, und ein einzelner Beweis kostet hunderte Millionen Token."
source_url: "https://www.anthropic.com/research/formal-verification"
source_name: "Anthropic"
lang: de
---

## TL;DR

- Anthropic hat zusammen mit dem Start-up Theorem gezeigt, dass Claude {{Formale Verifikation}} für echten Code übernehmen kann: In wenigen Wochen entstanden rund **180 Millionen Zeilen Beweiscode** für **239 Testeinstiege in 123 Open-Source-Bibliotheken** aus Googles OSS-Fuzz-Programm.
- Der bewiesene Satz ist eng, aber stark: Diese Programme stürzen bei **keiner Eingabe unter 64 MB** ab – allerdings nur als einthreadige, statisch gelinkte RISC-V-Binärdatei mit festem Speicherbudget unter Linux.
- Unterwegs fand Claude hunderte Fehler und durfte sie selbst reparieren, darunter einen Pufferüberlauf, der nur bei rund 20 MB großen Eingaben mit seltenem Aufbau auftritt, und eine Logiklücke, die über zehn Jahre unentdeckt blieb.
- Geprüft wird nicht von Menschen, sondern von einem Beweisprüfer: Vertrauen muss man nur den Maschinenmodellen, den bewiesenen Aussagen und dem Prüfer selbst.
- Der Haken sind die Kosten: Ein einzelner Beweis verschlingt laut Anthropic hunderte Millionen {{Token}}, eine Gesamtrechnung für das Projekt nennt das Unternehmen nicht.

## Was ist passiert

Anthropic hat am 22. Oktober 2026 einen Forschungsbericht veröffentlicht, der die Grenze dessen verschiebt, was automatisierte Softwareprüfung leisten kann. Das Frontier Red Team des Unternehmens hat zusammen mit dem Start-up [Theorem](https://theorem.dev/) Claude dazu gebracht, nicht neuen Code zu schreiben, sondern **bestehenden Code mathematisch zu beweisen** ([Anthropic: LLMs are making formal software verification feasible at a much larger scale](https://www.anthropic.com/research/formal-verification)).

Der Ausgangspunkt ist ein alter Ärger: Beweisen, dass Software unter allen Umständen tut, was sie soll, war bisher so teuer, dass es nur für Extremfälle infrage kam. Der Mikrokernel seL4 brauchte zwei Personenjahre zum Bau – und zwanzig Personenjahre, um ihn zu beweisen ([seL4-Papier](https://sel4.systems/Research/pdfs/comprehensive-formal-verification-os-microkernel.pdf)). Airbus ließ Avionik-Code auf diesem Weg prüfen, weil ein Absturz Menschenleben kostet. Für eine PDF-Bibliothek oder einen Dekompressor hat das niemand bezahlt.

Anthropic und Theorem drehen den Ansatz um: Statt eine Spezifikation von Hand zu schreiben und dann mühsam zu beweisen, nehmen sie die **Fuzz-Tests**, die Entwickler ohnehin geschrieben haben. {{Fuzzing}} heißt: Ein Testprogramm wirft Millionen zufälliger, absichtlich kaputter Eingaben auf eine Funktion und schaut, ob sie abstürzt. Die Forscher übersetzen diese Tests in eine {{Spezifikation}} über die kompilierten RISC-V-Befehle. Der Satz lautet dann: „Dieser Test stürzt bei keiner Eingabe unter 64 MB ab.“ Kann Claude das beweisen, ist der Fuzz-Test an dieser Stelle überflüssig – nicht „wahrscheinlich sauber“, sondern garantiert.

Claude schreibt dafür Beweise in Rocq, einem {{Beweisassistent}}en. Ein eigenes Prüfprogramm rechnet jeden Beweis nach. Ergebnis: **239 Einstiegspunkte in 123 Bibliotheken**, zusammen rund **180 Millionen Zeilen Rocq**. Ein typischer Beweis umfasst nach Angaben der Forscher etwa 600.000 Zeilen und sichert damit eine Binärdatei mit im Median 18.000 RISC-V-Befehlen ab.

Weil das praktisch niemand Zeile für Zeile lesen kann, ändert sich, wem man vertrauen muss. Übrig bleiben drei Dinge: die Modelle von RISC-V und des Linux-Prozesses, die genaue Formulierung der bewiesenen Sätze und der Prüfer Rocq selbst. Beweise für einen Teil der Bibliotheken hat Anthropic [auf GitHub veröffentlicht](https://github.com/theorem-labs/oss-verify-proofs), dazu die [Semantik von RISC-V und Linux-Prozessen](https://github.com/theorem-labs/rocq-linux-process-semantics). Theorem bietet an, dieselbe Pipeline für weitere Open-Source-Projekte laufen zu lassen, und liefert einen Claude-Skill, mit dem Entwickler eigene Projekte anmelden können.

## Warum zählt es

Formale Verifikation hatte bisher ein Personalproblem, kein Prinzipienproblem: Die Arbeit war richtig, aber niemand konnte sie bezahlen. Wenn ein Modell Beweise schreibt, die ein Prüfprogramm abnimmt, fällt dieser Engpass weg – und das trifft genau die Schwachstelle der aktuellen KI-Codewerkzeuge. Agenten produzieren inzwischen Code in Mengen, die kein Review-Prozess mehr abdeckt. Tests finden nur, was jemand vorher als Testfall aufgeschrieben hat. Ein Beweis deckt alle Eingaben ab, die in der Spezifikation beschrieben sind.

Wie viel dabei herauskommt, zeigt die Fehlerliste. Beim Beweisen eines Dekompressors stieß Claude auf einen Unterlauf im Zähler, der zu einem Schreibzugriff außerhalb des Puffers führt – auslösbar nur durch Eingaben von rund 20 MB mit einem seltenen, speziellen Aufbau. Ein Bilddecoder hatte einen Lesefehler außerhalb des Puffers, der eine 64-MB-Eingabe und über 2 GB Arbeitsspeicher braucht. In einer anderen Bibliothek reichte eine bestimmte Reihenfolge von Aufrufen über zwei Handles auf dieselbe Datei. In libexpat fand Claude CVE-2026-56132 erneut, diesmal über tief verschachtelte Eingaben. Und ein Logikfehler ohne Absturz: Eine Funktion, die festlegen soll, welche Dateien eine Anwendung laden darf, wird nicht in jedem Fall durchgesetzt.

Die Funde sind kein Zufall der Auswahl. Der Grund ist strukturell: Fuzzer probieren kleine Eingaben aus, typischerweise bis 1 MB, und brauchen Glück, um seltene Pfade zu treffen. Ein Beweis muss dagegen jeden Pfad abdecken, also stolpert das Modell über genau die Ecken, die im Testbetrieb nie erreicht werden. Bei der Prüfung eines verbreiteten PDF-Lesers fand das Team in einer Woche so viele Sicherheitsfehler, wie für diese Software sonst in einem Jahr gemeldet werden. In einer weiteren Anwendung kam ein Logikfehler zum Vorschein, der über ein Jahrzehnt unbemerkt geblieben war.

Dass das kein Nischenproblem ist, zeigt der Linux-Kernel: Kürzlich wurden dort über 1.000 Schwachstellen offengelegt ([LWN](https://lwn.net/Articles/1097401/)) – in Software, die auf Milliarden Geräten läuft und jahrelang intensiv getestet wurde.

## Was heißt das praktisch

Zuerst die Einschränkung, die Anthropic selbst deutlich macht: **„formal verifiziert“ heißt nicht „fehlerfrei“**. Die Beweise gelten für einthreadige, statisch gelinkte RISC-V-Programme mit musl libc. In der Praxis laufen dieselben Bibliotheken auf x86 oder ARM, dynamisch gelinkt gegen glibc – der bewiesene Satz beschreibt also eine Maschine, die so gut wie niemand benutzt. Dazu kommt: AdressSanitizer, das die Abstürze erkennt, übersieht manche Speicherfehler; nicht jeder Einstiegspunkt jeder Bibliothek wurde geprüft; und wer eine Bibliothek falsch aufruft, kann im eigenen Code weiterhin Speicher zerstören. Der Beweis sagt nichts über den Aufrufer. Wer die Grenzen kennt, weiß immerhin, wo die restlichen Fehler stecken können – in den Modellen, der Spezifikation oder außerhalb ihres Bereichs.

Der zweite praktische Punkt ist der Preis. Ein einzelner Beweis kann hunderte Millionen Token verschlingen; Anthropic nennt für das Gesamtprojekt keine Kosten. Theorem hat für den Nix-Paketbestand durchgerechnet, was eine flächendeckende Verifikation kosten würde: 123.471 Binärdateien mit 153,7 GB Maschinencode, bei geschätzten 0,5 KB Beweisfortschritt pro Stunde und 40 Dollar pro KB ([Theorem: Bootstrapping the Verified Software Stack](https://theorem.dev/blog/verified-software-stack/)). Mit 100 Millionen Dollar Jahresbudget wäre der letzte Paketstand nach rund fünf Jahren fertig, für insgesamt etwa 404 Millionen Dollar. Wachsen die Fähigkeiten viermal schneller als allgemein erwartet, wären 95 Prozent des Maschinencodes bis Ende 2027 für rund 134 Millionen Dollar bewiesen. Ein OpenSSL-Beweis käme auf etwa 220.000 Dollar, also rund 14 Dollar pro Paket, das ihn wiederverwendet.

Wiederverwendung ist überhaupt der Hebel. Beweise bauen aufeinander auf wie Software: Wenn Agenten die Beweise der anderen lesen durften, brauchten sie 17 Prozent weniger Token, und manche schafften Aufgaben, an denen sie allein gescheitert waren. Bei 36 kleinen Testaufgaben zeigte sich außerdem, dass das neuere Modell sparsamer arbeitet: **Claude Opus 5.5 beweist die Hälfte davon mit rund 40 Prozent weniger Token als Opus 5**.

Für Teams, die Agenten programmieren lassen, ergibt sich daraus eine konkrete Reihenfolge. Nicht jede Zeile beweisen, sondern die Abhängigkeiten, auf denen alles steht – glibc, OpenSSL, curl stehen genau deshalb auf der Roadmap. Und Beweise als Prüfschritt dort einsetzen, wo ein Fehler teuer wird, statt sie als allgemeine Qualitätsversicherung zu verkaufen. Der Satz, den man mitnehmen sollte: Ein Beweis verschiebt die Frage von „Ist dieser Code richtig?“ zu „Ist diese Annahme richtig?“ – und die zweite Frage kann ein Mensch beantworten.

## Quellen

- Anthropic: [LLMs are making formal software verification feasible at a much larger scale](https://www.anthropic.com/research/formal-verification) (22.10.2026)
- Anthropic: [Appendix mit Details zu den Beweisen (PDF)](https://www-cdn.anthropic.com/files/4zrzovbb/website/6867eadf760258fa8b42a504600cd3c036d16358.pdf)
- Theorem: [Bootstrapping the Verified Software Stack](https://theorem.dev/blog/verified-software-stack/) (29.09.2026)
- GitHub: [Veröffentlichte Rocq-Beweise](https://github.com/theorem-labs/oss-verify-proofs), [RISC-V- und Linux-Semantik](https://github.com/theorem-labs/rocq-linux-process-semantics)
- seL4: [Comprehensive formal verification of an OS microkernel (PDF)](https://sel4.systems/Research/pdfs/comprehensive-formal-verification-os-microkernel.pdf)
- LWN: [Über 1.000 offengelegte Schwachstellen im Linux-Kernel](https://lwn.net/Articles/1097401/)
- The Decoder: [Anthropic's Claude now writes code and proves it safe automatically](https://the-decoder.com/anthropics-claude-now-writes-code-and-proves-it-safe-automatically/) (23.10.2026)
