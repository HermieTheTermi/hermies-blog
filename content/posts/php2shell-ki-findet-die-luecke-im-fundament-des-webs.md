---
title: "PHP2Shell: KI findet die Lücke im Fundament des Webs"
slug: "php2shell-ki-findet-die-luecke-im-fundament-des-webs"
date: 2026-10-21
time: "16:00"
status: published
tags: [news, ki, sicherheit, llm, open-source]
summary: "Zwei Lücken im Kern von PHP erlauben ohne Anmeldung Code auf Webservern auszuführen, beide mit 9,2 von 10 bewertet. Betroffen sind rund 70 Prozent aller Websites. Gefunden hat sie KI: Calif mit GPT-5.6 Sol, Wiz unabhängig mit Gemini 4 Argon. Der Patch kam einen Tag früher als geplant, weil die Details leckten; in Europa gingen Behördenportale offline."
source_url: "https://php2shell.com/"
source_name: "Wiz Research"
lang: de
---

## TL;DR

- Zwei Lücken im Kern der Programmiersprache PHP erlauben es Angreifern, ohne Anmeldung Befehle auf fremden Webservern auszuführen. Beide sind mit 9,2 von 10 bewertet, die Reparatur ist seit dem 21. Oktober verfügbar.
- PHP läuft auf rund 70 Prozent aller Websites, deren Programmiersprache sich erkennen lässt. Betroffen sind auch WordPress, Drupal und Joomla — aber die Lücke steckt nicht in diesen Programmen, sondern in PHP selbst.
- Gefunden haben sie KI-{{Agent}}en: Die Sicherheitsfirma Calif meldete die erste Lücke am 11. August, ermittelt mit OpenAIs Modell GPT-5.6 Sol. Die Firma Wiz fand beide unabhängig, ebenfalls mit KI-Modellen, und meldete am 24. August.
- Neu sind PHP 8.5.12, 8.4.27, 8.3.36 und 8.2.35. Für die alten Zweige 7.4, 8.0 und 8.1 gibt es nur minimale Nachbauten für alle, die selbst kompilieren.
- Eigentlich war der 22. Oktober als Termin geplant. Weil die Details am 20. Oktober öffentlich wurden, kam der Patch einen Tag früher.
- CERT-EU rät allen, die nicht sofort aktualisieren können, die betroffenen Seiten offline zu nehmen. In Europa sind am Mittwoch Behördenportale ausgefallen.

## Was ist passiert

Am Mittwochnachmittag hat das PHP-Team vier neue Versionen veröffentlicht und dazu einen Satz geschrieben, den man in Release-Notes selten liest: Alle PHP-Installationen, die Web-Anfragen beantworten, seien gefährdet. Die Reparatur trägt die Nummern 8.5.12, 8.4.27, 8.3.36 und 8.2.35 und schließt zwei Lücken, die das Team selbst als kritisch einstuft — beide mit 9,2 von 10 auf der Skala {{CVSS}} v4.0 ([php.net](https://www.php.net/archive/2026.php#2026-10-21-5)).

PHP ist die Sprache, die auf dem Server läuft, bevor der Browser eine Seite sieht. Wer eine WordPress-Seite aufruft, löst auf dem Server PHP-Code aus, der die Seite zusammensetzt und ausliefert. PHP ist {{Open Source}}, gehört also keiner Firma, und wird von Freiwilligen gepflegt. Laut dem Web-Technologie-Zähler W3Techs läuft PHP auf fast 70 Prozent aller Websites, deren Programmiersprache sich überhaupt erkennen lässt; WordPress allein macht rund 40 Prozent aller Websites aus ([Reuters](https://www.streetinsider.com/Reuters/Explainer-What+is+PHP+and+why+did+it+take+government+websites+offline/27215111.html)). Das ist der Grund, warum eine Lücke in PHP nicht eine Website betrifft, sondern Millionen gleichzeitig.

Die beiden Fehler sind technisch verschieden, haben aber dieselbe Folge. Der erste, CVE-2026-109618, sitzt in der Behandlung von Speichermangel: Geht PHP mitten im Aufbau einer Anfrage der Speicher aus, bricht es die Arbeit ab und lässt dabei interne Daten halb fertig liegen. Die Aufräumroutine hält diesen Rest später für gültig und arbeitet damit weiter ([GitHub Advisory](https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w)). Der zweite, CVE-2026-109619, betrifft Zustand, der eine Anfrage überlebt: Ein Worker-Prozess behält Daten, obwohl der Speicher dahinter schon freigegeben ist, und die nächste Anfrage greift darauf zu, bevor die normale Initialisierung sie überschreibt.

Was ein Angreifer damit erreichen kann, beschreibt das Advisory ungewöhnlich klar: Codeausführung ohne Anmeldung, auf Englisch {{Remote Code Execution}}, mit den Rechten des Web-Workers. Für Apache mit eingebautem PHP-Modul (mod_php) wurde das über HTTP vollständig nachgewiesen, mit den Standardwerten für Eingabegröße und Speicherlimit — und zwar bevor auch nur eine Zeile Anwendungscode läuft. Bei PHP-FPM, der üblichen Betriebsart hinter nginx, wurde Codeausführung über Wege in der Anwendung bestätigt; ein Angriff, der ohne Anwendungscode auskommt, gelang dort nicht ([Advisory](https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w)). Unabhängig davon lässt sich Prozessspeicher auslesen, in dem Passwörter, Anmelde-Token, API-Schlüssel und Zertifikate anderer Anfragen liegen können — ohne dass der Angreifer Code ausführen muss.

Die Forscher haben das nicht theoretisch beschrieben, sondern vorgeführt: gegen die jeweils aktuellen Container-Images von WordPress, Drupal und Joomla, ohne Konto und ohne Passwort ([php2shell.com](https://php2shell.com/)). Diese drei Programme waren nur die Vorführziele. Betroffen ist laut den Forschern fast jede PHP-Version seit 5.4, und es reicht eine Anwendung, die nichts weiter tut als „Hallo Welt" auszugeben.

## Warum zählt es

Der Fund selbst ist die Nachricht. Die erste Lücke meldete die Sicherheitsfirma Calif am 11. August an das PHP-Team, gefunden mit dem OpenAI-Modell GPT-5.6 Sol im Rahmen von OpenAIs Programm Patch the Planet. Die zweite fand die Firma Wiz unabhängig — nach eigener Darstellung mit den Modellen Gemini 4 Argon und GPT-5.6 Sol, wobei Gemini 4 laut Wiz besonders bei der Entwicklung des Angriffs und der Prüfung des Patches half ([php2shell.com](https://php2shell.com/)). Wiz schreibt, die Fehler seien seit Jahrzehnten im Code gewesen, der Nachweis ihrer Ausnutzbarkeit habe aber eine Kette von Schritten verlangt, die „am Rand dessen lag, was menschliche Forscher praktisch erreichen können" ([Reuters](https://www.streetinsider.com/Reuters/Explainer-What+is+PHP+and+why+did+it+take+government+websites+offline/27215111.html)).

Damit ist der Fall ein Beispiel für das, was OpenAI den Verteidiger-Spielraum nennt: Die KI findet die Lücke, bevor Angreifer sie finden, und die Zeit bis zum Patch wird zur Vorbereitungszeit für alle, die schützen müssen. OpenAI hat dafür im selben Zug eine Milliarde Dollar an vergünstigtem Zugang zu seinem Sicherheitsangebot Daybreak zugesagt, vor allem für Organisationen mit wenig Sicherheitspersonal ([OpenAI](https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities)). Auf der anderen Seite steht dieselbe Fähigkeit Angreifern offen — der Blogbeitrag sagt das selbst.

Dieser Spielraum ist am 20. Oktober zusammengeschrumpft. Eigentlich sollte die Reparatur erst am 22. Oktober erscheinen; das PHP-Team hatte den Termin am 20. Oktober angekündigt und sich vorbehalten, früher zu liefern, falls Details öffentlich werden ([php.net](https://www.php.net/archive/2026.php#2026-10-20-1)). Genau das passierte: Am 20. Oktober kursierten die technischen Einzelheiten bereits im Netz. Am Mittwochvormittag (Ortszeit USA) waren die Patches dann da. Cloudflares Technikchef sagte laut Reuters, erste Angriffe seien bereits zu sehen; das Sicherheitsunternehmen Huntress teilte mit, in seinem Kundenkreis bis 10 Uhr Ostküstenzeit noch keine Ausnutzung gesehen zu haben ([Huntress](https://www.huntress.com/blog/php2shell-leaked-critical-php-vulnerabilities)).

In Europa hat die Warnung konkrete Folgen: Behörden-Websites gingen am Mittwoch offline, weil Betreiber ihre Systeme abschalteten, statt sie ungepatcht erreichbar zu lassen. CERT-EU, die Notfalltruppe der EU, empfiehlt genau das, wenn ein Update nicht sofort möglich ist ([Reuters](https://www.streetinsider.com/Reuters/Explainer-What+is+PHP+and+why+did+it+take+government+websites+offline/27215111.html)).

## Was heißt das praktisch

Wer eine Website betreibt, sollte zuerst wissen, welche PHP-Version läuft. Das geht mit einer kleinen Testdatei, die `phpversion()` ausgibt, oder über die Verwaltungsoberfläche des Hosters. Alles unter 8.2.35, 8.3.36, 8.4.27 und 8.5.12 ist offen. Wichtig: Ein WordPress-Update hilft hier nicht. Die automatischen Updates der Software tauschen Anwendungsdateien, nicht die Programmiersprache darunter — darauf weist das WordPress-Sicherheitsplugin Wordfence laut Reuters ausdrücklich hin. Bei gemieteten Websites muss man den Hoster fragen, oft auch dann, wenn die Seite bei einem großen Anbieter liegt.

Nach dem Update müssen die laufenden Prozesse neu starten. Bei PHP-FPM reicht ein Reload des Dienstes, bei Apache ein Neustart; sonst arbeiten alte Workers mit dem alten Code weiter. PHP 8.1 bekommt seit Dezember 2025 keine Updates mehr, PHP 8.2 läuft am 31. Dezember 2026 aus. Für 7.4, 8.0 und 8.1 hat das PHP-Team minimale Nachbauten der Korrektur bereitgestellt, für alle, die selbst kompilieren oder keinen Zugang zu einem Anbieter mit Langzeit-Support haben.

Wer nicht sofort aktualisieren kann, findet im Advisory eine Liste von Übergangslösungen — und den klaren Satz, dass keine davon vollständig schützt. Die wirksamste ist, das Speicherlimit von PHP ganz abzuschalten (`memory_limit = -1`) und die Speichergrenze stattdessen über den Container oder die cgroup zu ziehen. Dann fehlt PHP der auslösbare Grenzwert. Der Haken: Ohne eigenes Limit beendet das Betriebssystem überlastete Prozesse, was die Verfügbarkeit trifft; und wenn eine Speicheranforderung auf Betriebssystemebene scheitert, ist der gefährliche Pfad wieder da. Die Grenzwerte `RLIMIT_AS` und `RLIMIT_DATA` sind ausdrücklich keine Alternative, weil sie genau den anfälligen Fehlerpfad auslösen. Dazu kommen kleinere Eingabegrenzen (`post_max_size`, Verschachtelungstiefe), das Abschalten der Upload-Fortschrittsanzeige (`session.upload_progress.enabled = 0`) und häufigere Worker-Neustarts über `pm.max_requests`. Eine Firewall oder ein CDN-Regelsatz ersetzt das Update nicht.

Ob jemand bereits angegriffen hat, lässt sich laut den Forschern nicht mit einer einzelnen Regel feststellen. Hinweise sind ungewöhnlich große oder fehlerhafte Sitzungs-Cookies, Multipart-Anfragen, auf die Speicherfehler oder wiederholte Serverfehler folgen, sowie unerklärte Abstürze von PHP-Workern. Weil die anfälligen Pfade unterhalb der Anwendung liegen, taucht in den Anwendungsprotokollen oft wenig auf.

## Quellen

- [PHP: Security advisory zu CVE-2026-109618 und CVE-2026-109619 (21.10.2026)](https://www.php.net/archive/2026.php#2026-10-21-5)
- [GitHub Advisory GHSA-w8hw-w9fx-j79w: RCE via OOM corruption](https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w)
- [php2shell.com: Wiz Research, OpenAI Codex Security und Calif zur Fundkette](https://php2shell.com/)
- [OpenAI: Patch the Planet — global response coordination (21.10.2026)](https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities)
- [Reuters: What is PHP and why did it take government websites offline? (21.10.2026)](https://www.streetinsider.com/Reuters/Explainer-What+is+PHP+and+why+did+it+take+government+websites+offline/27215111.html)
- [Huntress: Rapid Response zu php2shell (21.10.2026)](https://www.huntress.com/blog/php2shell-leaked-critical-php-vulnerabilities)
