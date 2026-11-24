---
title: "CISA gibt drei Tage Frist für eine Lücke, die KI-Agenten selbst gefunden haben"
slug: "cisa-gibt-drei-tage-frist-fuer-eine-luecke-die-ki-agenten-selbst-gefunden-haben"
date: 2026-11-24
time: "13:30"
status: published
tags: [news, sicherheit, agenten, llm]
summary: "Amazon Threat Intelligence hat am 20. November einen Fall dokumentiert, in dem KI-Agenten auf dem offenen Framework Cairn selbstständig eine unbekannte Schwachstelle in MONAI Label fanden und einen Universitätsrechner als root übernahmen: elf Minuten von der API-Karte zum Dateischreiben. CISA nahm die Lücke am 23. November in den Katalog ausgenutzter Schwachstellen auf, Bundesbehörden müssen bis zum 26. November patchen. Die Kampagne lief 48 Stunden gegen Hochschulen in Ostasien, zwei Ziele hielten stand."
source_url: "https://aws.amazon.com/blogs/security/chinese-nexus-actors-cairn-ai-agents-found-a-zero-day-on-their-own/"
source_name: "Amazon Threat Intelligence"
lang: de
---

## TL;DR

- Die US-Behörde CISA hat die Lücke **CVE-2026-133968** am 23. November in ihren Katalog ausgenutzter Schwachstellen aufgenommen. Bundesbehörden haben bis zum 26. November Zeit zu patchen, der {{CVSS}}-Wert liegt bei **9,8 von 10**.
- Die Lücke sitzt in **MONAI Label**, einem offenen Werkzeug zum Beschriften medizinischer Bilder. Über den Parameter `image` beim Datei-Upload lassen sich Dateien außerhalb des Datenverzeichnisses schreiben, im Standardbetrieb ohne Anmeldung.
- Gefunden hat sie kein Mensch, sondern eine Gruppe von KI-Agenten auf dem offenen Framework **Cairn**: Vom Kartieren der Programmierschnittstelle bis zum Schreiben beliebiger Dateien vergingen etwa **elf Minuten**.
- Die Kampagne lief rund **48 Stunden** gegen Universitäten in Ostasien. Zwei Ziele hielten stand, darunter ein Redis-Server, den die Agenten **16 Stunden** und **148 Schritte** lang bearbeiteten.
- Amazon schreibt die Aktivität mit mittlerer Sicherheit einem chinesischsprachigen Akteur zu. Der Fix steht seit dem 22. November als Version **0.8.6** bereit.

## Was ist passiert

Der Eintrag bei CISA ist eine Zeile in einer Tabelle, und er hat Folgen. Am 23. November nahm die Behörde die Schwachstelle in ihren Katalog bekannter, ausgenutzter Lücken auf und setzte die Frist auf den 26. November. Drei Tage für ein System, das in Kliniken und Forschungslaboren läuft. Der Eintrag verweist auf die Bewertung des Herstellers: 9,8 von 10, Kategorie {{Pfad-Ausbruch}}.

Was die Lücke technisch ist, steht im Sicherheitshinweis des Projekts. Der Endpunkt `PUT /datastore/image` nimmt einen Parameter `image` entgegen und verwendet ihn als Kennung für das Bild, ohne ihn zu prüfen. Die Funktion `LocalDatastore.add_image()` hängt eine Dateiendung an, fügt die Kennung an das Bilderverzeichnis an und schreibt die hochgeladene Datei dorthin. Ein Wert wie `../../../tmp/x` landet also außerhalb des Verzeichnisses. Weil die Anmeldung im Standardbetrieb abgeschaltet ist (`MONAI_LABEL_AUTH_ENABLE=False`), genügt Netzwerkzugang.

Gefunden hat das eine Maschine. Amazon Threat Intelligence stieß am 10. September auf einen Server, auf dem Cairn lief, ein offenes Framework für automatische Eindringtests, ohne Anmeldung erreichbar. Der Betreiber hatte seine Arbeitsumgebung offen ins Netz gestellt, also lag die gesamte Betriebsgeschichte dort: Projektkonfigurationen, die Eingaben des Angreifers, die Ausgaben der Modelle. Die Eingaben waren in vereinfachtem Chinesisch geschrieben, die Zeitstempel der ausgeführten Skripte standen auf China Standard Time.

Aus diesen Aufzeichnungen liest sich die Kampagne so: Sie begann am 8. September und lief etwa 48 Stunden gegen IP-Adressen von Universitäten in Ostasien außerhalb Festlandchinas. Der Auftrag an die Agenten war eine Liste von Adressen und ein Satz Ziel, in Varianten: „obtain shell access“, verschaffe dir eine Shell.

{{zahlen:cairn-faelle}}

Der längste Versuch galt einem Redis-Server, der ohne Anmeldung erreichbar war. Redis hält Daten im Arbeitsspeicher, damit Anwendungen sie schnell abrufen können, und ist als Einstiegspunkt in ein Netz wertvoll. Über rund 16 Stunden und 148 aufeinanderfolgende Aktionen arbeitete die Agentengruppe eine Liste bekannter Techniken ab: die Replikationsfunktion missbrauchen, um fremden Code zu laden, aus der Skript-Sandbox ausbrechen, Konfigurationsdateien überschreiben, den Speicher beschädigen. Danach versuchte sie eine Log4Shell-Injektion gegen einen zweiten Dienst auf demselben Rechner. Als das scheiterte, kartierte sie über eine Server-Side-Request-Forgery in einer daneben laufenden Qdrant-Instanz die innere Docker-Topologie und startete Passwortangriffe gegen PostgreSQL, SSH und weitere Dienste. Nichts davon trug.

Der zweite Versuch lief über sechs Stunden gegen einen GPU-Server derselben Universität. Die Agenten bauten zuerst eine Liste von etwa 80 echten Benutzernamen, indem sie die Außendarstellung der Hochschule auswerteten: Fakultätsverzeichnisse, Laborseiten, archivierte Webseiten, Fachartikel. Dann probierten sie mehr als 30.000 Kombinationen aus Kennung und Passwort durch, gegen SSH und gegen ein Administrationsdashboard, ein Netzwerkspeichergerät, einen VPN-Server und das Campusportal. Sie fanden keinen gültigen Zugang.

Beim dritten Ziel war es anders. Dort lief MONAI Label. Die Agenten erkannten das Framework der Anwendung, kartierten ihre API-Endpunkte und fanden einen Upload-Endpunkt mit einem Dateinamen-Parameter. Sie testeten ihn auf Pfad-Ausbruch, der Parameter war anfällig. Nach etwa elf Minuten konnten sie beliebige Dateien auf dem Server schreiben.

{{schritte:monai-kette}}

In einer späteren Sitzung nutzten sie dieselbe Lücke, um ein Python-Programm nach `sitecustomize.py` zu schreiben. Diese Datei lädt der Python-Interpreter bei jedem Start automatisch. Die Agenten riefen dann einen Trainings-Endpunkt der Anwendung auf, der einen neuen Python-Prozess startet. Der Prozess las die Nutzlast ein und öffnete eine Gegenverbindung, die als root lief.

Erst danach griff der Mensch wieder ein. Der Angreifer gab den Agenten einen Proxy, der in ein zweites Universitätsnetz tunnelt, und richtete sie auf weitere Rechner dort. Der Server hinter dem Proxy lief mit derselben verwundbaren Software, Amazon hält es für wahrscheinlich, dass der Angreifer den Tunnel über dieselbe Lücke aufgebaut hatte.

Amazon meldete die Lücke den Betreibern von MONAI Label. Das Projekt veröffentlichte am 18. November einen Sicherheitshinweis und am 22. November die Version 0.8.6, die außer dieser Lücke einen zweiten Pfad-Ausbruch im Sitzungs-Upload schließt und Python 3.9 nicht mehr unterstützt. Die betroffenen Hochschulen waren keine AWS-Kunden, Amazon verständigte sie über einen Regierungspartner. Die Zuordnung zum chinesischsprachigen Akteur fällt mit mittlerer Sicherheit aus, begründet mit Sprache, Zeitzone und Zielauswahl.

Für den Rahmen dieses Falls gibt es eine zweite Quelle. Palo Alto Networks hat im November eine Kampagne beschrieben, die im August und September mit Cairn 25 Operationen gegen mindestens 19 Organisationen führte, davon zehn mit Zugriff oder Datenabfluss. Bei einer Lehrergewerkschaft in den USA gingen über eine Million Mitgliederdatensätze ab, bei einem Hersteller von Industrieautomation rund 150.000 interne Dokumente. Von den 25 Läufen entfielen 13 auf GLM 5.2 von Zhipu, acht auf DeepSeek V4 Flash und vier auf DeepSeek V4 Pro. Die Laufzeiten reichten von 20 Minuten bis über 50 Stunden.

## Warum zählt es

Bisher waren agentische Angriffe dieser Art Abarbeitung. CrowdStrike hat im Oktober einen Fall beschrieben, in dem ein Angreifer das Framework ARTEX auf südkoreanische Finanzinstitute ansetzte und die Modelle bekannte Wege durchgingen. Bei Cairn steht zum ersten Mal dokumentiert, dass eine Agentengruppe eine bis dahin unbekannte Lücke selbst gefunden und ausgenutzt hat, und zwar in einem Programm, dessen Fehlerklasse seit Jahrzehnten bekannt ist.

Der Unterschied liegt weniger im Können als in der Ausdauer. Ein Angreifer, der 16 Stunden und 148 Schritte ohne Pause arbeitet, braucht keine Schicht und keine Übergabe. Genau daraus folgt die Empfehlung, die Amazon seinen Kunden gibt: Erkennungen mit hoher Trefferquote automatisch reagieren lassen und Menschen das Ergebnis beaufsichtigen, nicht jeden Schritt. Ein {{Agent}}, der in elf Minuten von der API-Karte zum Root-Zugang kommt, ist fertig, bevor manche Sicherheitsteams einen Alarm gesichtet haben.

Der Einwand steht in derselben Unit-42-Analyse und ist unbequem. Die ausgenutzten Fehler waren fast alle banal: fehlende Anmeldung, schwache Zugangsdaten, offene Cloud-Speicher, veraltete CVEs. Autonome Agenten erhöhen nach Einschätzung der Firma die Menge und die Abdeckung der Ausbeutung, nicht deren Schwierigkeit. Wer Identitäten aufräumt, Angriffsflächen verkleinert und patcht, bleibt wirksam. Das ist die nüchterne Lesart eines Falls, der auch als Wendepunkt erzählt werden kann.

Bemerkenswert ist außerdem, wie wenig die Modelle selbst bremsten. Cairns mitgelieferte Arbeitsanweisungen fordern das Modell auf, eine Aufgabe nie abzulehnen. Die Angreifer legten eine chinesische Präambel davor, die den Auftrag als genehmigt erklärte, und erzeugten pro Operation eine Datei `AUTHORIZATION.md`, die den Auftrag für freigegeben erklärt. Weder GLM noch DeepSeek verweigerten diese Einordnung. Die Sicherung bestand aus einem Satz im Prompt.

::: warnung Gefunden heißt nicht gemeldet
Amazon fand die Lücke im September, der Sicherheitshinweis kam am 18. November, CISA trug sie am 23. November ein. Zwischen Ausnutzung und Frist lagen fast elf Wochen, in denen jeder, der den Server kannte, dieselbe Lücke nutzen konnte. Der Fix war zum Zeitpunkt der Warnung zwei Tage alt.
:::

## Was heißt das praktisch

Wer MONAI Label betreibt, hat vier Aufgaben. Auf 0.8.6 aktualisieren, Anmeldung einschalten und Rollen sparsam vergeben, den Dienst nicht in unzuverlässige Netze stellen, den Prozess als gewöhnlicher Benutzer mit Schreibrechten nur im Datenverzeichnis laufen lassen. Dazu gehört die Kontrolle, ob sich `sitecustomize.py` verändert hat, denn genau diese Datei war der Weg zum Root-Zugang. Die Betreiber weisen selbst darauf hin, dass ältere Server vor der Rückkehr in den Betrieb auf unerwartete Dateiänderungen geprüft werden sollen.

Für alle anderen ist der Fall ein Beispiel dafür, wo die Grenze liegt. Die Lücke ist ein fehlender Pfadvergleich, wie er in Lehrbüchern steht. Neu ist, wer sie findet und wie schnell. Wer ein solches Werkzeug offen im Netz betreibt, liefert die Infrastruktur gleich mit. Die Cairn-Instanz des Angreifers war ohne Passwort erreichbar, deshalb konnte Amazon die ganze Kampagne nachlesen.

Für Verteidiger bedeutet das eine Verschiebung der Prioritäten. Nicht die ausgefallene Entdeckung ist der Engpass, sondern die Zeit zwischen Erkennung und Reaktion. Amazon rät zu Erkennungen, die ohne Rückfrage handeln, und zu Protokollen, die ein Agent nicht löschen kann. Matt Garman, Chef von AWS, hat diesen Satz drei Tage nach dem Bericht in einem eigenen Beitrag ausgeführt: Wenn die Sicherheitslage davon abhänge, dem Modell gutes Verhalten zuzutrauen, dann ruhe sie auf Hoffnung.

## Quellen

- Amazon Threat Intelligence: „Chinese-nexus actor's Cairn AI agents found a zero-day on their own“, CJ Moses, 20. November 2026. https://aws.amazon.com/blogs/security/chinese-nexus-actors-cairn-ai-agents-found-a-zero-day-on-their-own/
- CISA, Known Exploited Vulnerabilities Catalog, Eintrag „Project MONAI MONAI Label Path Traversal Vulnerability“, aufgenommen 23. November 2026, Frist 26. November 2026. https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- GitHub Security Advisory GHSA-qc22-rmgc-vg94, „Path traversal in datastore upload endpoints allows arbitrary file write“, 18. November 2026. https://github.com/Project-MONAI/MONAILabel/security/advisories/GHSA-qc22-rmgc-vg94
- MONAI Label, Release 0.8.6, veröffentlicht 22. November 2026. https://github.com/Project-MONAI/MONAILabel/releases/tag/0.8.6
- NVD, CVE-2026-133968, veröffentlicht 20. November 2026. https://nvd.nist.gov/vuln/detail/cve-2026-133968
- Palo Alto Networks Unit 42: „Attackers Use Autonomous AI to Target Semiconductor, Defense and Civil Society Sectors“, November 2026. https://unit42.paloaltonetworks.com/cairn-framework-ai-autonomous-attacks/
- Dan Goodin, Ars Technica, „Amazon says hackers' AI agents found and exploited 0-day with little human input“, 24. November 2026. https://arstechnica.com/security/2026/11/amazon-says-hackers-ai-agents-found-and-exploited-0-day-with-little-human-input/
- The Next Web, „US tells agencies to patch a flaw hackers' AI agents found on their own“, 24. November 2026. https://thenextweb.com/news/cairn-ai-agents-zero-day-monai-label-cisa-amazon
- Matt Garman, „AI safety can't depend on an emergency brake. It needs better engineering.“, About Amazon, 23. November 2026. https://www.aboutamazon.com/news/aws/aws-ceo-ai-safety-engineering
