---
title: "AgentCorruption: Ein einziger Prompt übernahm jeden Agenten einer AWS-Region"
slug: "agentcorruption-ein-einziger-prompt-uebernahm-jeden-agenten-einer-aws-region"
date: 2026-10-08
time: "15:01"
status: published
tags: [news, sicherheit, agenten, ki]
summary: "Ein einziger Prompt an einen öffentlich erreichbaren Agenten genügte, um jeden Agenten derselben AWS-Region zu übernehmen: Die Sicherheitsfirma Zenity Labs hat am 8. Oktober 2026 eine Kette von Lücken in Amazons Agenten-Plattform Bedrock AgentCore veröffentlicht. Der Agent durfte den internen AWS-Metadatendienst abfragen und gab seine Zugangsdaten heraus – die gehörten zu einer Standardrolle mit regionweiter Berechtigung: fremde Agenten aufrufen, alle privaten Gespräche lesen, Erinnerungen schreiben, Schlüssel aus dem Secrets Manager holen. Amazon hat die Rolle Ende September 2026 entschärft; Zenity rät weiterhin zu eigenen Rollen mit minimalen Rechten."
source_url: "https://labs.zenity.io/post/agentcorruption-how-a-single-prompt-collapsed-the-entire-cloud-security-model"
source_name: "Zenity Labs"
lang: de
---

## TL;DR

- Die Sicherheitsfirma Zenity Labs hat am 8. Oktober 2026 eine Kette von Lücken in Amazons Agenten-Plattform **Bedrock AgentCore** veröffentlicht. Ihr Name: „AgentCorruption".
- Ein einziger {{Prompt}} an **einen** öffentlich erreichbaren Agenten genügte, um jeden Agenten derselben AWS-Region zu übernehmen.
- Der Einstieg ist ein Klassiker: Der Agent durfte die interne AWS-Adresse `169.254.169.254` abfragen – den Metadatendienst – und gab dabei seine eigenen, kurzlebigen Zugangsdaten heraus.
- Diese Zugangsdaten gehörten zu einer Standardrolle, die nicht auf einen einzelnen Agenten beschränkt war, sondern regionweit galt: fremde Agenten aufrufen, alle privaten Gespräche lesen, Erinnerungen schreiben, Schlüssel aus dem AWS Secrets Manager holen.
- Weil sich auch das Langzeitgedächtnis beschreiben ließ, konnten Angreifer Agenten dauerhaft umprogrammieren. Nutzer hätten weiter mit einem vertrauten Agenten gesprochen, der im Hintergrund Befehle Fremder ausführt.
- Amazon hat nachgebessert: Neue Agenten laufen seit dem **14. Februar 2026** nur noch mit der strengeren Metadaten-Variante IMDSv2, und seit **Ende September 2026** ist die Standardrolle deutlich enger. Monatelang war sie es nicht.

## Was ist passiert

Amazon Bedrock AgentCore ist Amazons Baukasten für Firmen, die {{Agent}}en betreiben wollen. Man lädt seinen Agenten hoch und bekommt Werkzeuge, Zugriffsverwaltung, Protokolle und ein Langzeitgedächtnis dazu. Genau dort fanden die Forscher von Zenity Labs eine Lücke, die sie in einer fünfteiligen Reihe aufschreiben; die Übersicht erschien am 8. Oktober 2026, vorgestellt wurde die Arbeit auf der Sicherheitskonferenz SecTor in Toronto.

Der erste Schritt ist altbekannt und heißt SSRF, zu Deutsch etwa „gefälschte Serveranfrage". Ein Agent läuft bei AgentCore in einer kleinen virtuellen Maschine vom Typ Firecracker. Diese Maschine war laut Zenity nicht ausreichend vom Netz abgeschottet. Jedes Werkzeug, das eine Abfrage ins Netz stellen kann, stellt sie also direkt aus der Maschine heraus. Ein Angreifer musste den Agenten nur bitten, die Adresse `169.254.169.254` abzufragen – den internen Metadatendienst von AWS. Der antwortet nur Anfragen von der Maschine selbst und liefert dabei die kurzlebigen Zugangsdaten der Rolle, mit der diese Maschine läuft.

„Die {{Sandbox}}-Grenze, gegen die wir eigentlich kämpfen sollten, war einfach nicht da", schreiben die Forscher.

Das wäre halb so wild, wenn diese Rolle nur für den einen Agenten gegolten hätte. Tat sie aber nicht. Die Standardrolle von AgentCore galt laut Zenity für **alle** AgentCore-Ressourcen in der gesamten Region. Über die Berechtigung `DescribeLogGroups` ließen sich alle Agenten samt Kennungen auflisten. Weil die Namen der Container-Register denselben Kennungen entsprechen, ließen sich damit auch die Abbilder der Agenten herunterladen und lesen. Über `bedrock-agentcore:InvokeAgentRuntime` durfte man fremde Agenten aufrufen, über `ListEvents` alle privaten Gespräche aller Agenten, Nutzer und Sitzungen mitlesen. Und `CreateEvent` auf dem Gedächtnis erlaubte es, neue Erinnerungen anzulegen.

Der Rest ist Beute: Die Rolle enthielt zusätzlich `GetResourceApiKey` und `secretsmanager:GetSecretValue`. Damit ließen sich genau jene Schlüssel holen, die AgentCore eigentlich von den Agenten fernhalten soll – API-Schlüssel, OAuth-Token und Zugangsdaten zu Diensten außerhalb von AWS.

## Warum zählt es

Der Angriff ist kein Einbruch, sondern ein Umzug. Wer über den öffentlich erreichbaren Kundenservice-Agenten hineinkam, konnte in derselben Region weiter zu einem internen Finanzagenten gehen, ihn aufrufen und an seine Daten kommen. Die Forscher beschreiben das als das eigentliche Muster: Firmen betreiben nach außen offene und interne Agenten oft im selben Umfeld, und dann reicht eine einzige Schwachstelle, um die Grenze zwischen beiden einzureißen.

Am unangenehmsten ist der Teil mit dem Gedächtnis. Wer Erinnerungen anlegen darf, kann einem fremden Agenten dauerhaft Anweisungen mitgeben. Der Agent verhält sich danach weiter wie ein vertrauter Firmenagent – nur dass er im Hintergrund die Ziele Fremder verfolgt. Solche Manipulationen seien kaum zu bemerken, schreibt Zenity.

Bemerkenswert ist auch, wie lange es dauerte:

{{chart:agentcorruption-offenlegung}}

Zenity meldete den Metadaten-Zugriff am **25. Dezember 2025**. AWS antwortete am 12. April 2026 und schloss den Bericht als „informativ"; immerhin liefen neue Agenten ab dem 14. Februar 2026 nur noch mit IMDSv2. Die überprivilegierte Standardrolle meldeten die Forscher am **12. Januar 2026**. Am 25. Februar 2026 hieß es, man arbeite an der zugrunde liegenden Ursache, im Juni 2026 war die Rolle unverändert. Erst bei einer letzten Prüfung am 29. September 2026, kurz vor der Veröffentlichung, war sie entschärft. Zum Vergleich führt The Decoder an, dass OpenAI eine Schwachstelle im eigenen Umfeld binnen vier Tagen behoben habe. Ein Hinweis gehört zur Fairness dazu: Zenity verkauft selbst Software, mit der Unternehmen ihre Agenten absichern, hat also ein geschäftliches Interesse daran, auf solche Lücken zu zeigen. Die technischen Belege sind in der Reihe aber nachvollziehbar dokumentiert, bis hin zu den einzelnen Berechtigungen.

## Was heißt das praktisch

Für Unternehmen, die Agenten in der Cloud betreiben – nicht nur bei AWS –, ergeben sich daraus fünf Punkte:

- **Eigene Rolle statt Standardrolle.** Zenity empfiehlt ausdrücklich, jedem Agenten eine selbst gebaute Rolle mit minimalen Rechten zu geben statt der vom Anbieter mitgelieferten.
- **Öffentlich und intern trennen.** Ein nach außen erreichbarer Agent sollte nicht dieselbe Identität und dasselbe Umfeld haben wie ein interner. Sonst ist der erste die Eintrittstür zum zweiten.
- **Ausgehende Verbindungen begrenzen.** Der Angriff begann mit einer Abfrage an eine interne Adresse. Wer den Datenverkehr aus der {{Sandbox}} heraus einschränkt, nimmt diesem Angriff den Anfang. Solche Regeln heißen in der Branche {{Guardrail}}s.
- **Zugangsdaten nicht ins Umfeld des Agenten legen.** Auch der Secrets Manager schützt nicht, wenn der Agent selbst die Erlaubnis hat, dort zu lesen.
- **Schreibzugriff auf das Gedächtnis prüfen.** Erinnerungen sind ein Angriffsweg: Was ein Agent einmal „gelernt" hat, bleibt.

Wer AgentCore nutzt, hat es heute leichter als noch im Frühjahr. Amazon hat die Standardrolle nach Zenitys Angaben deutlich verschärft: regionweite Aufrufe, das Lesen privater Gespräche und der Zugriff auf Secrets wurden entfernt, IMDSv2 ist für neue Agenten Standard. Die Forscher betonen trotzdem, dass eine angepasste Rolle weiter die bessere Wahl bleibt – und dass das Muster nicht auf AWS beschränkt ist. Wer Agenten mit Zugriff auf echte Systeme betreibt, sollte davon ausgehen, dass ein Angreifer über den schwächsten von ihnen kommt.

Der Fall steht nicht allein. Ebenfalls am 8. Oktober wurde bekannt, dass ein mutmaßlich einzelner Angreifer mit einem offenen KI-Werkzeug mehreren südkoreanischen Banken Kundendaten abgenommen hat ([Artikel dazu](/artex-und-die-suedkorea-hacks-ein-angreifer-sieben-banken-viele-ki-modelle.html)). Dort war die KI das Einbruchswerkzeug, hier ist sie das Ziel.

## Quellen

- [Zenity Labs: AgentCorruption – How A Single Prompt Collapsed The Entire Cloud Security Model](https://labs.zenity.io/post/agentcorruption-how-a-single-prompt-collapsed-the-entire-cloud-security-model) (8. Oktober 2026)
- [Zenity Labs, Teil 1: SSRF und Zugriff auf den Metadatendienst](https://labs.zenity.io/post/agentcorruption-initial-imds-access)
- [Zenity Labs, Teil 2: Die Standardrolle und ihr Radius](https://labs.zenity.io/post/agentcorruption-one-role-to-rule-them-all)
- [Zenity Labs, Teil 3: Gedächtnis als Angriffsweg](https://labs.zenity.io/post/agentcorruption-weaponizing-agent-memory-for-persistent-hijacking)
- [Zenity Labs, Teil 4: Zugangsdaten aus dem Secrets Manager](https://labs.zenity.io/post/agentcorruption-credential-theft-from-aws-secrets-manager-and-more)
- [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [The Decoder: A single prompt was enough to hijack every AI agent in an AWS account](https://the-decoder.com/a-single-prompt-was-enough-to-hijack-every-ai-agent-in-an-aws-account-zenity-researchers-found/) (8. Oktober 2026)
