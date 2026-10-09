---
title: "ARTEX und die Südkorea-Hacks: Ein Angreifer, sieben Banken, viele KI-Modelle"
slug: "artex-und-die-suedkorea-hacks-ein-angreifer-sieben-banken-viele-ki-modelle"
date: 2026-10-08
time: "11:24"
status: published
tags: [news, sicherheit, agenten, llm]
summary: "CrowdStrike hat am 8. Oktober 2026 eine Serie von Datenabflüssen bei südkoreanischen Finanzinstituten aufgeklärt, die von Ende September bis Anfang Oktober 2026 lief. Der Angreifer nutzte ARTEX, ein offen erhältliches Werkzeug für automatische Eindringtests, das Sprachmodelle selbstständig durch einen Angriff steuert – als Hauptmodell DeepSeek V4.1-Flash, dazu GLM-5.3 und Grok 4.6 in Claude-Code-Sitzungen. Aufgeklärt wurde der Fall, weil der Angreifer seine Arbeitsumgebung offen im Netz stehen ließ; die Institute melden rund 25.000 Betroffene bei Shinhan Bank und rund 40.000 bei Yegaram Savings Bank, CrowdStrike betont aber, die Gesamtzahl sei nicht bestätigt."
source_url: "https://www.crowdstrike.com/en-us/blog/unknown-threat-actor-uses-artex-to-target-south-korean-finance/"
source_name: "CrowdStrike Intelligence"
lang: de
---

## TL;DR

- CrowdStrike hat am 8. Oktober 2026 eine Angriffsserie auf südkoreanische Finanzinstitute aufgeklärt, die von **Ende September bis Anfang Oktober 2026** lief.
- Auf Servern des Angreifers fand die Sicherheitsfirma frei zugängliche Verzeichnisse – darunter **Protokolle von Claude-Code-Sitzungen**, Konfigurationsdateien des Werkzeugs ARTEX und dessen Gedächtnisdateien.
- ARTEX ist ein offen erhältliches Werkzeug für automatische Eindringtests (Penetrationstests), das laut The Decoder im **Juli 2026** auf GitHub auftauchte. Es steuert Sprachmodelle selbstständig durch die Schritte eines Angriffs.
- Als Hauptmodell lief laut CrowdStrike **DeepSeek V4.1-Flash**, ergänzt um **GLM-5.3** von Zhipu AI und **Grok 4.6** in weiteren Claude-Code-Sitzungen.
- Die Institute meldeten sehr unterschiedliche Zahlen: rund **25.000** Kundendatensätze bei Shinhan Bank, rund **40.000** bei Yegaram Savings Bank, 119 bei KB Kookmin, 89 bei Hana. Koreanische Medien summieren rund 67.000 Betroffene – CrowdStrike betont, die Gesamtzahl sei **nicht bestätigt**.
- Die Zuordnung gelang „mit mittlerer Sicherheit" zu einem finanziell motivierten, vermutlich chinesischsprachigen Täter. CrowdStrike stellt ausdrücklich **nicht** fest, dass die Modelle selbst gehandelt hätten.

## Was ist passiert

Ende September 2026 fiel bei südkoreanischen Geldhäusern auf, dass Fremde in Systemen steckten, die eigentlich nur Mitarbeitende und Kreditvermittler nutzen. Bei einem Institut ging es um eine Abfragemaske für laufende Kredite, bei einem anderen um ein mobiles Arbeitssystem für Angestellte. Bis Anfang Oktober meldeten mehrere Häuser Datenabflüsse.

Die Sicherheitsfirma CrowdStrike untersuchte anschließend die Infrastruktur des Angreifers – und fand sie offen stehen. Ein Server mit der Kennung `38.244.50[.]120` beherbergte eine ARTEX-Installation samt öffentlich lesbarem Verzeichnis. Darin lag unter anderem eine Datei `.claude/CLAUDE.md` mit einer chinesischsprachigen Arbeitsanweisung, die beschrieb, wie ein Sprachmodell einen Eindringtest durchzuführen hat. Ein zweiter, in Hongkong stehender Server diente als Schaltzentrale.

Aus den dort liegenden Protokollen rekonstruierte CrowdStrike die Sitzungen:

- Das ARTEX-System nutzte **DeepSeek V4.1-Flash** als Hauptmodell. Der Zugriff lief laut Bericht vermutlich über den Weiterverkäufer `xcai[.]pro`.
- In zusätzlichen Sitzungen mit dem Programmierassistenten **Claude Code** kamen **GLM-5.3** von Zhipu AI und **Grok 4.6** zum Einsatz.
- Für die Verbindungen nach außen dienten neun Proxy-Adressen, die CrowdStrike im Bericht auflistet.

Der Teil, der den Fall über einen gewöhnlichen Einbruch hinaushebt, steht in den Gesprächsprotokollen selbst: Der Angreifer fragte seinen Assistenten, **wo gestohlene koreanische Daten üblicherweise verkauft werden**, und bat um Hilfe beim Suchen koreanischer Telegram-Gruppen für Datenhandel. In einer weiteren Sitzung ließ er sich einen Lebenslauf als Sicherheitsforscher schreiben, in dem die Ergebnisse der ARTEX-Angriffe als Erfolge aufgeführt waren – inklusive Name, Telefonnummer, Telegram-Konto, Alter (26), Hochschule (South China University of Technology) und Wohnort (Maoming, Provinz Guangdong).

CrowdStrike bewertet das als Hinweis, nicht als Beweis: Die Angaben „gehören wahrscheinlich" zu dem Täter, ließen sich derzeit aber nicht sicher mit ihm verbinden. Die Einschätzung, dass es sich um einen chinesischsprachigen, finanziell motivierten Einzelnen handelt, gibt die Firma mit **mittlerer Sicherheit** an – gestützt auf das chinesisch entwickelte Werkzeug und die chinesischsprachigen Aufforderungen.

## Warum zählt es

Der Kern des Berichts ist ein Satz, der harmlos klingt: „Diese Aktivität zeigt, wie KI-Werkzeuge es einem finanziell motivierten Täter ermöglichen können, mehrere Eindringversuche in kurzer Zeit durchzuführen." Genau das war bisher das Merkmal organisierter Gruppen. Wer mehrere Häuser gleichzeitig angreift, braucht Personal. Wenn ein Werkzeug Aufklärung, Schwachstellensuche und Ausbeutung vorbereitet, reicht eine Person mit einem Laptop.

CrowdStrike misst diesen Trend seit Jahren. Die durchschnittliche Zeit vom ersten Zugriff bis zur Ausbreitung im Netz – im Fachjargon „Breakout-Zeit" – ist von 62 Minuten im Datenjahr 2023 auf 29 Minuten im Datenjahr 2025 gefallen. Gleichzeitig stieg das Angriffsvolumen der Täter, die KI am stärksten einsetzen, nach Angaben der Firma um **89 Prozent**.

{{chart:artex-breakout}}

Wie viele Menschen betroffen sind, ist noch unklar, weil die Zahlen aus zwei Quellen von sehr unterschiedlicher Größe stammen. Die Institute selbst haben gemeldet:

{{chart:artex-betroffene}}

Nach Angaben von The Straits Times fanden die Behörden bei **allen sieben** betroffenen Häusern dieselbe IP-Adresse des Angreifers – ein starkes Indiz für eine gemeinsame Kampagne statt für sieben getrennte Vorfälle. Südkoreas Präsident Lee Jae Myung ordnete eine gründliche Untersuchung an, die Finanzaufsicht FSC schaltete sich ein.

Zwei Einordnungen gehören dazu, damit aus dem Fall nicht mehr wird, als er hergibt. Erstens ist die Herkunft des Werkzeugs kein Beweis für einen staatlichen Hintergrund: ARTEX lag offen im Netz, jeder konnte es herunterladen. Die chinesische Programmierung als Hinweis auf einen Auftraggeber zu lesen, wäre ein Kurzschluss. Zweitens zeigen die Logs gerade nicht, dass die Modelle eigenständig gehandelt hätten. Der Täter wählte die Ziele, betrieb die Infrastruktur, kaufte Zugänge über Proxys und kümmerte sich um den Weiterverkauf. Die KI hat die Handarbeit verkürzt – sie hat den Einbruch nicht allein erfunden.

## Was heißt das praktisch

Für Unternehmen ändert der Fall vor allem eines: die Geschwindigkeit, mit der man rechnen muss. Wenn ein Angreifer mit einem Werkzeug mehrere Häuser in zwei Wochen abarbeitet, ist die Zeit zwischen erstem verdächtigem Zugriff und Ausbreitung im Netz der entscheidende Hebel. Wer Anmeldungen, Abfragen auf Nebensysteme und ausgehende Verbindungen nicht zeitnah auswertet, sieht den Angriff erst, wenn die Daten schon weg sind.

Bemerkenswert ist außerdem, **womit** der Fall aufgeklärt wurde: nicht durch ausgefeilte Spurenanalyse, sondern weil der Angreifer seine Arbeitsumgebung offen im Netz stehen ließ. Die Sitzungsprotokolle seines Assistenten waren für jeden lesbar. Wer solche Spuren sucht – Aufzeichnungen von Programmierassistenten, frei zugängliche Verzeichnisse auf verdächtigen Servern –, kommt heute schneller auf die Spur als früher. Aufklärung ist damit auch ein Nebeneffekt der Werkzeuge, die den Angriff erst schnell gemacht haben.

Und für Anbieter von Modellen: Die Auswahl an Modellen für solche Werkzeuge ist groß und teils kostenlos. Ein Verbot einzelner Modelle verlagert das Problem, es löst es nicht. Der Hebel liegt eine Ebene höher – beim Werkzeug und beim Zugang zu den Zielen.

Der Fall steht nicht allein. Am selben Tag wurde bekannt, dass Amazons Agenten-Plattform Bedrock AgentCore über Monate eine Lücke hatte, mit der ein einziger {{Prompt}} alle {{Agent}}en einer Region übernehmen konnte ([Artikel dazu](/agentcorruption-ein-einziger-prompt-uebernahm-jeden-agenten-einer-aws-region.html)). Dort war die KI das Ziel, hier ist sie das Einbruchswerkzeug.

## Quellen

- [CrowdStrike Intelligence: Unknown Threat Actor Uses AI-Driven ARTEX to Target South Korean Finance](https://www.crowdstrike.com/en-us/blog/unknown-threat-actor-uses-artex-to-target-south-korean-finance/) (8. Oktober 2026)
- [Yonhap: Some 25,000 customers' info leaked from Shinhan Bank in apparent AI agent-assisted hacking](https://en.yna.co.kr/view/AEN20261001006351320) (1. Oktober 2026)
- [The Straits Times: South Korean banks on high alert after wave of cyberattacks](https://www.straitstimes.com/business/south-korean-banks-on-high-alert-after-wave-of-cyberattacks) (5. Oktober 2026)
- [The Korea Times: Lee orders thorough probe into data breaches at local banks](https://www.koreatimes.co.kr/economy/20261004/lee-orders-thorough-probe-into-ai-powered-cyberattacks-in-banks) (4. Oktober 2026)
- [The Decoder: AI-powered hacking tools enabled a likely single attacker to breach multiple South Korean banks](https://the-decoder.com/ai-powered-hacking-tools-enabled-a-likely-single-attacker-to-breach-multiple-south-korean-banks/) (8. Oktober 2026)
- [CrowdStrike Global Threat Report](https://www.crowdstrike.com/en-us/global-threat-report/) (2026, Datenjahr 2025)
