---
title: "Claude Duet: Anthropic schickt einen Agenten, der von selbst anklopft"
slug: "claude-duet-anthropics-agent-klopft-von-selbst-an"
date: 2026-10-22
status: published
tags: [news, agenten, labs, sicherheit]
summary: "Anthropic öffnet eine Forschungsvorschau von Claude Duet: ein Agent auf Claude Opus 5.5, der auf einer eigenen Cloud-Maschine arbeitet, morgens eine Übersicht schickt und vor Zahlungen, Nachrichten oder Unterschriften um Erlaubnis bittet. Start nur in den USA, per Warteliste, für Pro und Max; Hintergrundprüfungen zählen gegen dasselbe Nutzungslimit wie normale Chats."
source_url: "https://claude.com/resources/articles/claude-duet"
source_name: "Anthropic"
lang: de
---

## TL;DR

- Anthropic startet **Claude Duet** als Forschungsvorschau: eine eigene App, in der ein {{Agent}} im Hintergrund arbeitet und sich von selbst meldet, wenn etwas Wichtiges ansteht.
- Duet läuft auf **Claude Opus 5.5**, arbeitet auf einem eigenen Cloud-Rechner mit Browser und greift über **mehr als 6.000 Konnektoren und Plugins** aus dem Claude Marketplace auf Dienste wie Gmail, Slack, Stripe, DocuSign und Shopify zu.
- Alles, was nach außen wirkt – Nachricht senden, zahlen, unterschreiben, löschen –, zeigt Duet vorher an und wartet auf ein Ja. Wertpapierhandel und Umbuchungen zwischen Konten sind auch mit Erlaubnis gesperrt.
- Zugang gibt es zunächst nur in den **USA** für Abonnenten von Pro und Max, per Warteliste. Team- und Enterprise-Kunden sind noch außen vor.
- Der Haken steht im Kleingedruckten: Die Hintergrundprüfungen zählen gegen dasselbe Nutzungslimit wie normale Chats. Anthropic räumt außerdem ein, dass die frühe Version Threads falsch liest und Dringlichkeit falsch einschätzt.

## Was ist passiert

Anthropic hat am 22. Oktober 2026 eine Forschungsvorschau von Claude Duet geöffnet – als eigenständige App für iOS und Android sowie im Web unter claude.ai. Das Unternehmen richtet sich laut eigener Ankündigung an „Profis und kleine Unternehmen, die mehr auf dem Tisch haben, als sie überblicken können“. Zugang bekommen zunächst Pro- und Max-Abonnenten in den USA über eine Warteliste; im Rahmen der Vorschau ist Duet in diesen Plänen enthalten und teilt sich die Nutzungslimits mit dem Rest von Claude ([Anthropic: Introducing Claude Duet](https://claude.com/resources/articles/claude-duet)).

Der Unterschied zur normalen Claude-App liegt in der Richtung, in der die Kommunikation läuft. Dort öffnet man einen Chat und fragt. Duet kommt von selbst: Jeden Morgen schickt es eine kurze Übersicht der wichtigsten Punkte aus den verbundenen Apps, danach meldet es sich nur, wenn etwas Aufmerksamkeit braucht. Aufgaben nimmt es als Text- oder Sprachnachricht in einem durchlaufenden Thread entgegen – von der Terminplanung über Dashboards und Finanzprognosen bis zu Prototypen und kleinen Web-Apps.

Dafür bekommt der Agent eine virtuelle Maschine mit eigenem Browser. Laptop oder Handy müssen also nicht laufen, während Duet arbeitet. Die Verbindung zur Außenwelt läuft über mehr als 6.000 Konnektoren und Plugins aus dem Claude Marketplace. Konkret genannt werden Gmail, Slack, Stripe, DocuSign und Shopify: Duet kann offene Rechnungen aufspüren und Zahlungserinnerungen entwerfen, eine Lohnabrechnung vorbereiten oder einen Shop einrichten. Einkäufe laufen über Stripes digitale Geldbörse Link mit einer virtuellen Kartennummer, die echte Kartennummer wird nicht weitergegeben; bei Shopify kommt Shop Pay dazu ([Anthropic](https://claude.com/resources/articles/claude-duet), [TechCrunch](https://techcrunch.com/2026/10/22/claude-duet-app-is-anthropics-bet-on-agents/)).

Gedächtnis, Skills und verbundene Apps übernimmt Duet aus dem bestehenden Claude-Konto. Wer schon länger mit Claude arbeitet, muss also wenig einrichten – und nimmt dafür mit, was das Konto über ihn weiß.

## Warum zählt es

Duet ist kein Alleingang, sondern der Einstieg in einen Wettlauf, der seit dem Sommer läuft. SpaceXAI hat im August die Beta von Grok Bot geöffnet, Meta brachte im September Muse, OpenAI kurz darauf seine Dots – alle mit demselben Versprechen: ein Assistent, der Aufgaben selbstständig erledigt und von sich aus aktiv wird ([The Decoder](https://the-decoder.com/anthropic-takes-on-grok-bot-metas-muse-and-openais-dots-with-its-always-on-agent-claude-duet/)).

Meta hat für Muse inzwischen Zahlen vorgelegt: mehr als 10 Millionen Nutzer, etwa ein Viertel davon täglich, und ein Viertel der einkaufenden Nutzer mit einem durchschnittlichen Einkaufswert über 200 Dollar ([TechCrunch](https://techcrunch.com/2026/10/21/meta-says-muse-has-over-10m-users-with-shopping-a-top-activity/)). Das sind Herstellerangaben aus der Quartalsbilanz, unabhängig nachgeprüft sind sie nicht – aber es zeigt, worum es in diesem Markt geht: nicht um bessere Antworten, sondern um Gewohnheiten.

Bemerkenswert ist, wo Anthropic die Grenze zieht. Duet darf lesen, entwerfen und vorbereiten. Sobald eine Nachricht rausgeht, Geld fließt, ein Dokument unterschrieben oder etwas gelöscht wird, hält es an und zeigt den Plan. Einige Dinge bleiben auch mit Zustimmung tabu: mit Wertpapieren handeln und Geld zwischen Konten verschieben. Das ist eine bewusst engere Auslegung als bei Wettbewerbern, die den Agenten stärker als Einkaufs- und Buchungshelfer positionieren – Anthropic sagt selbst, für persönliche Besorgungen wie Kinokarten sei Duet schwächer, der Kern sei Arbeit.

Dazu kommt eine zweite Absicherung, die technisch interessant ist: ein eigener Klassifikator plus besondere Sicherheitsanweisungen im System-Prompt, die jede Nachricht prüfen. Anfragen nach Kreditkartennummern oder Ausweisdaten soll Duet grundsätzlich ablehnen; Gesundheits- und Finanzdaten gehen nur raus, wenn der Nutzer es ausdrücklich verlangt. Gegen versteckte Anweisungen in fremden Inhalten – {{Prompt-Injection}} – setzt Anthropic Abwehrmaßnahmen aus seiner Browser-Forschung ein, außerdem haben interne {{Red-Teaming}}-Teams und eine externe Firma das System angegriffen, und es fällt unter das öffentliche {{Bug-Bounty}}-Programm ([Anthropic](https://claude.com/resources/articles/claude-duet)).

## Was heißt das praktisch

Für Anwender außerhalb der USA heißt es erst einmal warten: Die Vorschau startet dort, eine Zeitleiste für Europa nennt Anthropic nicht. Wer in den Genuss kommt, sollte zwei Dinge im Kopf behalten.

Erstens: Hintergrundarbeit ist nicht gratis. Duet prüft verbundene Konten in Abständen, und diese Prüfungen zählen auf dasselbe Limit wie alle anderen Claude-Nutzungen. Größere Aufgaben – ein Finanzmodell, eine Präsentation – brauchen viele Modellschritte und damit viel Budget. Anthropic begründet die seltenen Prüfintervalle ausdrücklich damit, dass häufigeres Nachsehen die Limits schneller verbrennen würde. Wer den Agenten dauerhaft laufen lässt, arbeitet also am Rand des Abos.

Zweitens: Die Fehler sind eingestanden. Die frühe Version kann einen Nachrichten-Thread falsch verstehen, Dringlichkeit falsch bewerten und Dinge übersehen, die zwischen zwei Prüfungen eintreffen. Sie kann ihren Browser noch nicht zeigen, während sie arbeitet – man sieht also nicht mit, sondern nur das Ergebnis. Und sie lebt in einer eigenen App neben der normalen Claude-App; wie beide zusammenwachsen, ist offen.

Spannend ist der Sicherheitsentwurf auch jenseits von Anthropic. Duet bekommt keine Passwörter und Anmelde-Token zu sehen, sondern arbeitet über eine Vermittlungsschicht, die Anthropic schon für Claude Managed Agents gebaut hat. Das Muster – der Agent sieht Zugangsdaten nie direkt – dürfte zum Standard für alle werden, die Agenten an fremde Konten lassen. Wer selbst Agenten baut, kann sich daran orientieren: nicht Rechte großzügig vergeben und hinterher filtern, sondern Rechte gar nicht erst in den Kontext des Modells legen.

Ob das reicht, entscheidet sich an der Frage, die Anthropic offenlässt: wie oft ein Agent nachfragen darf, bevor er nervt. Die Vorschau ist genau dafür da – Rückmeldungen sollen kalibrieren, wann Duet sich meldet und wann es still bleibt.

## Quellen

- Anthropic: [Introducing Claude Duet](https://claude.com/resources/articles/claude-duet) (22.10.2026)
- TechCrunch: [Claude Duet app is Anthropic's bet on agents](https://techcrunch.com/2026/10/22/claude-duet-app-is-anthropics-bet-on-agents/) (22.10.2026)
- The Decoder: [Anthropic takes on Grok Bot, Meta's Muse, and OpenAI's Dots with its always-on agent Claude Duet](https://the-decoder.com/anthropic-takes-on-grok-bot-metas-muse-and-openais-dots-with-its-always-on-agent-claude-duet/) (22.10.2026)
- TechCrunch: [Meta says Muse has over 10M users](https://techcrunch.com/2026/10/21/meta-says-muse-has-over-10m-users-with-shopping-a-top-activity/) (21.10.2026)
- Anthropic: [Claude Opus 5.5](https://www.anthropic.com/claude-opus-5-5) (22.09.2026)
