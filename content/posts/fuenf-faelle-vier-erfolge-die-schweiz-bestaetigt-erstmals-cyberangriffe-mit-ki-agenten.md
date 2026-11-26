---
title: "Fünf Fälle, vier Erfolge: Die Schweiz bestätigt erstmals Cyberangriffe mit KI-Agenten"
slug: "fuenf-faelle-vier-erfolge-die-schweiz-bestaetigt-erstmals-cyberangriffe-mit-ki-agenten"
date: 2026-11-26
time: "06:15"
status: published
tags: [news, sicherheit, agenten]
summary: "Das Bundesamt für Cybersicherheit hat erstmals Angriffe in der Schweiz bestätigt, bei denen KI-Agenten selbstständig nach Lücken suchten: fünf Fälle, vier davon erfolgreich, drei Ziele aus kritischer Infrastruktur. Die eingesetzten Werkzeuge ARTEX und CyberStrikeAI haben sich seit Oktober fast verdoppelt. Die Empfehlungen des Amts sind unspektakulär, und genau darin liegt die Botschaft."
source_url: "https://www.bacs.admin.ch/de/26-ki-agenten-1-de"
source_name: "Bundesamt für Cybersicherheit (BACS)"
lang: de
---

## TL;DR

- Das Bundesamt für Cybersicherheit (BACS) hat am 24. November erstmals Fälle gemeldet, in denen Angreifer in der Schweiz mit KI-Agenten in Firmennetze eingedrungen sind.
- Am Donnerstag nannte BACS-Direktor Florian Schütz gegenüber SRF die Zahl: fünf bestätigte Fälle, in vier davon wurden Systeme kompromittiert.
- Drei der fünf Ziele sind Betreiberinnen kritischer Infrastruktur, betroffen sind mindestens zwei Sektoren. Zu grösseren Ausfällen kam es laut BACS nicht.
- Die eingesetzten Werkzeuge heissen ARTEX und CyberStrikeAI. Ihre Zahl im Netz hat sich seit Oktober 2026 nach Angaben des Amts fast verdoppelt.
- Die Empfehlungen sind unspektakulär: weniger Systeme am offenen Internet, kritische {{Patch}}es binnen 24 Stunden, Mehr-Faktor-Authentisierung ohne Ausnahme.

## Was ist passiert

Die Mitteilung des Bundesamts für Cybersicherheit vom 24. November ist kurz, und sie enthält einen Satz, den es in dieser Form noch nie gab. «Das BACS verfügt erstmals über bestätigte Fälle, in welchen KI-Agenten für Cyberangriffe gegen Unternehmen sowie Betreiberinnen kritischer Infrastrukturen in der Schweiz eingesetzt worden sind.» Betroffen waren verschiedene Firmen und Infrastrukturbetreiber aus mindestens zwei Sektoren.

Zwei Tage später wurde die Zahl konkret. Am Donnerstagmorgen sagte BACS-Direktor Florian Schütz im SRF-Radio: «Wir haben aktuell fünf bestätigte Fälle von Angriffen mit KI-Agenten.» Alle fünf seien in den letzten Tagen gemeldet worden. In vier Fällen drangen die Angreifer erfolgreich in die Systeme ein. Drei der fünf Ziele waren Betreiberinnen kritischer Infrastruktur, nach Angaben von SRF und Reuters unter anderem aus der Strom-, Wasser- und Telekomversorgung. Bei den übrigen handelte es sich um kleinere und mittlere Unternehmen, die die Vorfälle freiwillig meldeten.

{{zahlen:schweiz-ki-faelle}}

Namen nannte das Amt nicht. «Die Betroffenen haben das Recht, selbst zu kommunizieren», sagte Schütz. Auch zur Herkunft der Angreifer machte er keine Angabe. Grössere Ausfälle habe es nicht gegeben.

Technisch beschreibt das BACS den Vorgang als Einsatz von «Agentic Offensive Frameworks». Gemeint sind {{Agent}}en, die selbstständig nach Schwachstellen suchen, passende Angriffswerkzeuge auswählen, die Ausgabe auswerten und daraus die nächsten Schritte planen. Das Amt nennt zwei dieser Werkzeuge beim Namen: ARTEX und CyberStrikeAI. Beide sind im offenen Internet erreichbar, und ihre Zahl hat sich seit Oktober 2026 nach Einschätzung des BACS nahezu verdoppelt.

Der Einstieg lief in den bekannten Fällen über bekannte Muster: Standard- oder leicht erratbare Passwörter, nicht geschlossene Lücken in Software, die direkt am Internet hängt. Neu ist das Tempo. Ein KI-Agent brauche oft nur einen Bruchteil der Zeit, die ein Mensch für dieselbe Suche aufwenden müsste, schreibt das BACS. Und er wechsle die Methode, wenn eine Tür zu ist.

## Warum zählt es

Bisher war die Rede von KI in der Cyberabwehr vor allem Prognose. Branchenfirmen zeigten Laborversuche, Behörden warnten vorsorglich. Jetzt liegt zum ersten Mal eine staatliche Bestätigung aus einem Land vor, dass der Angriff selbst von einem Agenten geführt wurde. Das BACS spricht von einem «Wandel in der Cyberbedrohungslandschaft» und rechnet mit einer Häufung schneller und erfolgreicher Angriffe.

Der Fall reiht sich in eine Entwicklung, die sich diesen Monat schon einmal gezeigt hat. Am 20. November dokumentierte Amazon Threat Intelligence eine Kampagne, in der eine Gruppe von KI-Agenten auf dem offenen Framework Cairn selbstständig eine unbekannte Lücke in einer medizinischen Bildgebungssoftware fand und einen Universitätsrechner als Administrator übernahm. Elf Minuten von der Kartierung der Programmierschnittstelle bis zum Schreiben beliebiger Dateien. Die US-Behörde CISA nahm die Lücke zwei Tage später in ihren Katalog ausgenutzter Schwachstellen auf. ARTEX, eines der beiden in der Schweiz genannten Werkzeuge, tauchte in dieser Berichterstattung ebenfalls auf, damals im Zusammenhang mit Angriffen auf südkoreanische Finanzinstitute. Wer die technischen Details nachlesen will, findet sie im Artikel zu diesem Fall.

Was den Schweizer Vorgang von einem Laborversuch unterscheidet, ist die Zielauswahl. Kritische Infrastruktur ist der Bereich, in dem ein erfolgreicher Eindringling nicht nur Daten verliert, sondern Betrieb. Dass es diesmal bei vier kompromittierten Systemen ohne grösseren Ausfall blieb, ist ein Ergebnis, keine Garantie.

Zwei Einordnungen gehören zur Vollständigkeit. Erstens ist unklar, wie viel Autonomie in den fünf Fällen tatsächlich im Spiel war. Das BACS schreibt von Agenten, die selbstständig suchen und planen; ob ein Mensch die Ziele vorgab und die Funde freigab, steht nicht in der Mitteilung. Sicherheitsforscher unterscheiden genau hier, und die Grenze ist fliessend, weil dieselben Werkzeuge auch für Penetrationstests verkauft werden.

Zweitens weichen Mitteilung und Direktor in einem Punkt voneinander ab.

::: warnung Zwei Formulierungen, ein Unterschied
Die Medienmitteilung vom 24. November schreibt: «In allen dem BACS bekannten Cyberangriffen führte der Einsatz von KI-Agenten zu einer erfolgreichen Kompromittierung der IT-Systeme des Opfers.» Der Direktor sagte am Donnerstag, in vier von fünf Fällen seien Systeme gehackt worden. Entweder ist der fünfte Fall später dazugekommen, oder die Mitteilung fasst enger, als sie klingt. Bis Redaktionsschluss hat das BACS den Widerspruch nicht aufgelöst. Für die Bewertung der Lage ist der Unterschied klein, für die Frage, wie belastbar die Behördenkommunikation ist, nicht.
:::

## Was heißt das praktisch

Die Empfehlungen des BACS sind bewusst banal, und das ist die eigentliche Nachricht. Wer sie umsetzt, nimmt Angriffen dieser Art die Grundlage, weil ein Agent nur dort eindringt, wo eine Tür offen steht. Konkret nennt das Amt sechs Punkte: die Zahl der aus dem Internet erreichbaren Systeme verkleinern, etwa über Geo-Blocking oder Positivlisten für IP-Adressen. Kritische Sicherheitsupdates für erreichbare Systeme binnen 24 Stunden einspielen. Interne Ressourcen wie Webmail und VPN ausnahmslos mit {{Mehr-Faktor-Authentisierung}} oder Passkeys sichern. Rechte nach dem Prinzip der geringsten Rechte vergeben. Abweichungen im Verhalten von Konten, Anwendungen und Datenvolumen erkennen. Und die eigene Infrastruktur regelmässig auf Lücken testen lassen.

Für kleinere Firmen ist vor allem der Patch-Punkt eine Zumutung. Wer keine eigene IT-Abteilung hat, schafft 24 Stunden nicht zuverlässig. Raphael Reischuk vom Nationalen Testinstitut für Cybersicherheit sagt im SRF-Interview, es sei «unrealistisch, dass das Niveau für zigtausend KMU in der Schweiz durch eigene Kraft erhöht wird», und fordert eine gemeinsam finanzierte Unterstützung ähnlich der für Trinkwasser und Strom. Er rechnet mit einer grösseren Angriffswelle und sagt, das Problem werde von den Unternehmen nicht ausreichend ernst genommen.

Rückenwind bekommt die Warnung aus Deutschland. Das dortige Bundesamt für Sicherheit in der Informationstechnik stuft die Lage seit diesem Herbst als «angespannt bis kritisch» ein, unter anderem wegen der schnellen KI-Entwicklung. Beide Behörden raten Unternehmen inzwischen auch, KI selbst für die Verteidigung einzusetzen. Der Satz von Schütz, der die Lage am besten zusammenfasst, ist der nüchternste: «Wenn es keine Schwachstelle gibt, kann auch ein KI-Agent nicht in ein System eindringen.»

## Quellen

- Bundesamt für Cybersicherheit: «Cyberangriffe mit KI-Agenten: Erste bestätigte Fälle in der Schweiz», 24.11.2026, https://www.bacs.admin.ch/de/26-ki-agenten-1-de
- SRF: «Fünf bestätigte Fälle – Erstmals Cyberangriffe mit KI-Agenten in der Schweiz», 26.11.2026, 06:15, https://www.srf.ch/news/schweiz/fuenf-bestaetigte-faelle-erstmals-cyberangriffe-mit-ki-agenten-in-der-schweiz
- Reuters: «AI agents used in five cyber attacks in Switzerland, government says», 26.11.2026, 12:25 UTC, https://www.reuters.com/legal/litigation/ai-agents-used-five-cyber-attacks-switzerland-government-says-2026-11-26/
- Le Temps: «Ein Wendepunkt in der Cyberbedrohungslandschaft», 26.11.2026, https://www.letemps.ch/de/cyber/kuenstliche-intelligenz/ein-wendepunkt-in-der-cyberbedrohungslandschaft-erstmals-haben-ki-agenten-kritische-infrastrukturen-in-der-schweiz-angegriffen
- Blick: «Erstmals Cyberangriffe mit KI-Agenten in der Schweiz gemeldet», 26.11.2026, https://www.blick.ch/life/wissen/technik/erstmals-cyberangriffe-mit-ki-agenten-in-der-schweiz-gemeldet/l9p3q3t
- Amazon Threat Intelligence: «Chinese nexus actors used Cairn AI agents to find a zero-day on their own», 20.11.2026, https://aws.amazon.com/blogs/security/chinese-nexus-actors-cairn-ai-agents-found-a-zero-day-on-their-own/
