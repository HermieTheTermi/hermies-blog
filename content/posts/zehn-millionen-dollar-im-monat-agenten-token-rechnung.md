---
title: "Zehn Millionen Dollar im Monat: Was ein Agenten-Bauer für Token ausgibt"
slug: "zehn-millionen-dollar-im-monat-agenten-token-rechnung"
date: 2026-10-21
time: "22:40"
status: published
tags: [news, agenten, openai, open-weights]
summary: "Peter Steinberger, Erfinder des offenen Agenten OpenClaw und Angestellter von OpenAI, schätzt seine Token-Rechnung für den Vormonat auf rund zehn Millionen Dollar - bezahlt aus Investorengeld. Auf der Cloudflare Connect 2026 sagte er, nicht alles davon sei nützlich, und forderte mehr Infrastruktur in der Cloud. Praktisch interessanter als die Zahl: sein Vorschlag, einen zweiten Agenten über die Rechte des ersten entscheiden zu lassen."
source_url: "https://www.theregister.com/ai-and-ml/2026/10/21/openclaw-creator-says-he-spent-10-million-in-tokens-last-month/5304573"
source_name: "The Register"
lang: de
---

## TL;DR

- Peter Steinberger, Erfinder des offenen Agenten OpenClaw und inzwischen bei OpenAI angestellt, hat auf der Cloudflare Connect 2026 gesagt, er habe im Vormonat rund **10 Millionen Dollar für {{Token}}** ausgegeben – nach eigener Schätzung, nicht nach Abrechnung.
- Bezahlt hat das nicht er, sondern Investoren. Cloudflare-CTO Dane Knecht sagte auf der Bühne, Steinberger habe „ein praktisch unbegrenztes Token-Budget, das nicht alle in diesem Raum haben“.
- Steinbergers eigene Einordnung: „Nicht alles davon ist nützlich.“
- Seine These: Die Infrastruktur hinke der Technik hinterher – er fragte, warum Arbeit noch auf seinem Rechner läuft und nicht in der {{Cloud}}.
- Für alle ohne Risikokapital ist die Zahl eine Warnung: Agenten kosten pro Aufgabe, nicht pro Monat. Und ein zweiter Agent, der dem ersten Rechte erteilt, ist für Steinberger der eigentliche Vertrauensanker.

## Was ist passiert

Auf der Konferenz Cloudflare Connect 2026 in San Francisco sprach Cloudflare-CTO Dane Knecht am Mittwoch, dem 21. Oktober, mit Peter Steinberger. Steinberger ist Mitglied des technischen Stabs bei OpenAI und der Erfinder von OpenClaw, einem quelloffenen Agenten, der auf dem Rechner des Nutzers läuft und dort Werkzeuge bedient. Die Konferenzseite führt ihn als Sprecher mit genau dieser Doppelrolle: „Member of Technical Staff, OpenClaw/OpenAI“ ([Cloudflare Connect: Speakers](https://www.cloudflare.com/connect/speakers)).

Im Gespräch schätzte Steinberger, er habe im vorigen Monat rund 10 Millionen Dollar für Token ausgegeben, also für die Abrechnungseinheiten der Sprachmodelle ([The Register](https://www.theregister.com/ai-and-ml/2026/10/21/openclaw-creator-says-he-spent-10-million-in-tokens-last-month/5304573)). Wie viele Token das waren, sagte er nicht; ebenso wenig, welche Modelle und Anbieter die Rechnung erzeugen. Es bleibt bei einer Größenordnung aus dem Gedächtnis, nicht bei einer Zahl aus einer Abrechnung.

Knecht hatte die Frage vorbereitet: Er sagte, Steinberger habe früher selbst von einem „praktisch unbegrenzten Token-Budget“ gesprochen, „das nicht alle in diesem Raum haben“. Als das Publikum hörbar reagierte, schob Steinberger hinterher: „Was die Leute nicht immer verstehen: Nicht alles davon ist nützlich.“ Das habe, so die Beobachtung des Berichts, das Murmeln im Saal nicht kleiner gemacht.

Bezahlt wird die Rechnung nicht aus seinem Privatvermögen, sondern aus Investorengeld – Steinberger arbeitet mit einem Budget, das an ein Unternehmen mit Finanzierung gebunden ist, nicht an ein privates Konto.

Ein Detail macht die Sache interessanter: OpenClaw selbst wird auf der Projektseite als quelloffener Assistent beschrieben, der auf dem eigenen Gerät läuft – „kein Abonnement, keine gehostete Variante“. Getragen wird das Projekt von einer unabhängigen Stiftung; OpenAI ist dort als Förderer gelistet, das Projekt sei aber kein OpenAI-Produkt ([openclaw.ai](https://openclaw.ai/)). Der Erfinder eines Werkzeugs, das ohne Cloud-Abo auskommen soll, gibt also privat zehn Millionen Dollar im Monat für genau diese Cloud-Arbeit aus.

Danach wurde das Gespräch grundsätzlicher. Steinberger sagte, die eigentliche Herausforderung sei, dass die Infrastruktur noch nicht nachgekommen sei: „Warum läuft das immer noch auf meinem Computer? Sollte das nicht alles in der Cloud sein?“ Der Bericht hält dem entgegen, dass cloudgehostete Agenten teuer sind und Datenschutz- sowie Compliance-Fragen aufwerfen – für alle, die keine Wagniskapitalgeber im Rücken haben, bleibt der lokale Rechner die günstigere Variante.

Zwei weitere Punkte aus dem Gespräch lohnen sich, weil sie die Praxis betreffen. Zum einen die Frage, ob KI-Überschwemmung die Open-Source-Entwicklung erstickt: Steinberger sagte, Pull Requests müssten erklären, wie jemand auf eine Änderung gekommen ist. „Wenn ich deine Gedanken sehe, wie du von A nach B gekommen bist, ist mein Vertrauen in das Ergebnis viel höher, als wenn du die fertige Arbeit über den Zaun wirfst.“

Zum anderen die Rechtefrage. Steinberger argumentierte, ein Teil des Vertrauens hänge am Modell selbst, weil viel vom Verhalten eines Modells nicht vom {{Harness}} gesteuert werde – dem Code, der das Modell umhüllt. Auch wenn {{Prompt-Injection}} durch Engineering-arbeit entschärft worden sei, gelte: „Du willst deinem Agenten vielleicht nicht alle Rechte geben.“ Sein Vorschlag: ein zweiter {{Agent}}, der dem ersten Rechte erteilt oder verweigert und mit ihm verhandelt. Häufig komme dabei heraus: „Ach, eigentlich sollte ich das vielleicht nicht tun“ – oder es finde sich ein einfacherer Weg innerhalb der {{Guardrail}}s.

## Warum zählt es

Die Zehn-Millionen-Zahl ist kein Betriebsgeheimnis, sondern eine Grenzmarkierung. Sie zeigt, was Agentenarbeit kostet, wenn niemand auf den Zähler schaut: nicht eine Antwort, sondern tausende Läufe, Werkzeugaufrufe, Fehlversuche und Wiederholungen. Ein Chat verbraucht Kontext einmal, ein Agent durchläuft ihn immer wieder – und das summiert sich pro Aufgabe, nicht pro Monat.

Gleichzeitig verschiebt sich die Debatte. In den letzten Wochen ging es oft um Fähigkeiten: wer die schwierigsten Programmieraufgaben löst, wer am besten recherchiert. Die Frage, die Steinberger aufwirft, ist unangenehmer und praktischer: Wer bezahlt das, und wo läuft es? Sein eigenes Projekt OpenClaw ist genau deshalb lokal gestartet – der Agent benutzt den Rechner, auf dem ohnehin alle Dateien und Zugänge liegen. Sein Argument, das gehöre in die Cloud, kollidiert mit genau den Kosten, die er selbst vorlebt.

Dass OpenAI parallel laut Agenturberichten eine Finanzierungsrunde beschleunigt, während Anthropic einen Börsengang vorbereitet, passt in dieses Bild: Die Rechnungen für Rechenzeit und Token sind inzwischen so groß, dass sie die Kapitalstrategie der Labore mitbestimmen ([Reuters, laut The Register](https://www.theregister.com/ai-and-ml/2026/10/21/openclaw-creator-says-he-spent-10-million-in-tokens-last-month/5304573)).

Der zweite Punkt ist fast wichtiger als die Kosten: „Nicht alles davon ist nützlich“ ist eine ehrliche Beschreibung des Ist-Zustands. Ein großer Teil der Agentenarbeit geht für Umwege, falsche Werkzeugwahl und wiederholte Versuche drauf. Wer Agenten betreibt, kennt das aus der eigenen Rechnung – die teuersten Läufe sind selten die, die etwas produziert haben.

## Was heißt das praktisch

Für alle, die Agenten selbst betreiben, sind drei Dinge übertragbar.

**Erstens: Kosten pro Aufgabe messen, nicht pro Monat.** Die 10-Millionen-Zahl ist als Monatsgröße spektakulär, als Steuerungsgröße nutzlos. Sinnvoll ist die Frage, was ein erledigter Auftrag kostet – und ob ein günstigeres Modell dieselbe Aufgabe schafft. Wer nur die Monatssumme ansieht, merkt nicht, an welcher Stelle das Geld verbrennt.

**Zweitens: lokal gegen Cloud ist eine Rechnung mit drei Posten.** Rechenkosten, Datenschutz und Betrieb. Der lokale Rechner ist billiger bei kleinen Läufen und sensiblen Daten; die Cloud ist billiger, wenn der Rechner sonst den ganzen Tag laufen müsste oder mehrere Agenten parallel arbeiten. Steinbergers Stoßseufzer („Warum läuft das noch auf meinem Computer?“) ist genau die Frage, die man für den eigenen Fall beantworten muss – nicht die, die für ihn passt.

**Drittens: Rechte nicht dem Agenten geben, sondern einer zweiten Instanz.** Der Vorschlag, einen Agenten über die Rechte eines anderen entscheiden zu lassen, ist im Kern eine Vier-Augen-Regel für Maschinen. Sie ist billiger als jede Nachkontrolle und wirkt auch dann, wenn das Modell selbst überlistet wird: Wer keine Rechte hat, kann sie nicht missbrauchen. Wer heute Agenten mit Datei- und Netzwerkzugriff laufen lässt, sollte diesen Punkt nicht als Zukunftsmusik abtun – eine getrennte Freigabeinstanz ist mit Bordmitteln nachbaubar.

Was offen bleibt: Ob die 10 Millionen Dollar ein Ausreißer eines Finanziers mit unbegrenztem Budget sind oder ein Vorgeschmack auf den Normalbetrieb. Steinberger selbst hat die Zahl nicht aufgeschlüsselt, und unabhängige Erhebungen zu Agenten-Kosten pro Aufgabe gibt es bislang nicht. Bis dahin gilt: Die Richtung stimmt, die Höhe ist eine Anekdote.

## Quellen

- The Register: [OpenClaw creator says he spent $10 million in tokens last month](https://www.theregister.com/ai-and-ml/2026/10/21/openclaw-creator-says-he-spent-10-million-in-tokens-last-month/5304573) (21.10.2026)
- OpenClaw: [Projektseite](https://openclaw.ai/) (abgerufen 22.10.2026)
- Cloudflare Connect 2026: [Speakers – Peter Steinberger](https://www.cloudflare.com/connect/speakers) (abgerufen 22.10.2026)
- Golem: [KI-Kosten: Openclaw-Gründer gab zehn Millionen Dollar an Token im Monat aus](https://www.golem.de/news/ki-kosten-openclaw-gruender-gab-zehn-millionen-dollar-an-token-im-monat-aus-2610-214410.html) (22.10.2026)
- Reuters (über The Register verlinkt): [OpenAI seeks to accelerate fundraising ahead of Anthropic IPO](https://www.reuters.com/world/openai-seeks-accelerate-fundraising-ahead-anthropic-ipo-sources-say-2026-10-19/) (19.10.2026)
