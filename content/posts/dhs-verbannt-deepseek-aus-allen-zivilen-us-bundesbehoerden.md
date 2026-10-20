---
title: "DHS verbannt DeepSeek aus allen zivilen US-Bundesbehörden"
slug: "dhs-verbannt-deepseek-aus-allen-zivilen-us-bundesbehoerden"
date: 2026-10-20
status: published
tags: [news, ki, llm, sicherheit, open-weights, usa]
summary: "Das US-Heimatschutzministerium schließt DeepSeek aus allen zivilen Bundesbehörden aus: keine neuen Verträge, bestehende Installationen müssen raus — auch Software Dritter, die mit DeepSeek gebaut wurde. Was das genau heißt, bleibt offen; Ausnahmen sind beantragbar. Der Erlass datiert auf den 26. Juni, veröffentlicht wurde er erst am 20. Oktober."
source_url: "https://www.federalregister.gov/documents/2026/10/20/2026-21447/notice-of-order-regarding-exclusion-and-removal-of-deepseek-products-from-federal-civilian-executive"
source_name: "Federal Register / DHS"
lang: de
---

## TL;DR

- Das US-Heimatschutzministerium (DHS) hat DeepSeek aus allen zivilen Bundesbehörden verbannt: keine neuen Verträge mehr, bestehende Installationen müssen aus den IT-Systemen verschwinden. Die Anordnung steht seit dem 20. Oktober im [Federal Register](https://www.federalregister.gov/documents/2026/10/20/2026-21447/notice-of-order-regarding-exclusion-and-removal-of-deepseek-products-from-federal-civilian-executive) (Docket DHS-2026-0628).
- Sie trifft nicht nur die App und die Schnittstellen von DeepSeek, sondern auch Software von Dritten, die „unter Verwendung von DeepSeek-Implementierungen" gebaut wurde. Was genau darunter fällt, definiert der Text nicht.
- Begründet wird das mit Daten auf Servern in China, chinesischen Sicherheitsgesetzen und der Gefahr, dass Modelle Schadsoftware enthalten. Aus einer Behördenanfrage könne „verwertbare Erkenntnis" über US-Bürger und Regierungsprogramme werden.
- Ausnahmen sind möglich, müssen aber beantragt werden. Über sie entscheidet die Cyberbehörde CISA schriftlich.
- Der Erlass von Minister Markwayne Mullin trägt laut CyberScoop das Datum 26. Juni 2026. Bekannt wurde er erst jetzt — die Sperre lag Monate im Aktenschrank.
- DeepSeek ist damit der erste große KI-Anbieter, der über das US-Beschaffungsrecht vollständig aus der zivilen Bundesverwaltung fliegt.

## Was ist passiert

Am 20. Oktober 2026 hat das DHS im amtlichen US-Bekanntmachungsblatt Federal Register eine Anordnung veröffentlicht, die es in dieser Form noch nicht gab. Sie besteht aus zwei Teilen und beide sind weit gefasst: Erstens werden „Informationstechnologie-Produkte und -Dienstleistungen", die von Hangzhou DeepSeek Artificial Intelligence Co., Ltd. oder verbundenen Firmen entwickelt wurden, von der Beschaffung ziviler Bundesbehörden ausgeschlossen. Zweitens müssen „alle DeepSeek- und DeepSeek-Partnerprodukte sowie Produkte und Dienste Dritter, die unter Verwendung von DeepSeek-Implementierungen entwickelt wurden," aus der Behörden-IT entfernt werden.

Rechtsgrundlage ist der Federal Acquisition Supply Chain Security Act von 2018 (41 U.S.C. 1321–1328) mit seinen Durchführungsregeln in 41 CFR 201-1. Danach darf der Heimatschutzminister Technik, die er als Risiko für die Lieferkette einstuft, aus der zivilen Bundesverwaltung werfen. Vorausgegangen war eine Empfehlung des Federal Acquisition Security Council, eines Gremiums mehrerer Bundesbehörden, samt zugehöriger Beweismittel. Der Erlass ist als Anhang im PDF des Federal Register abgedruckt; unterzeichnet hat ihn Minister Markwayne Mullin. Nach Angaben von [CyberScoop](https://cyberscoop.com/dhs-bans-deepseek-federal-agencies/) datiert das Schreiben auf den 26. Juni 2026 — die Anordnung existierte also rund vier Monate, bevor sie öffentlich wurde.

Die Begründung stützt sich auf mehrere Punkte. DeepSeek speichere Daten auf Servern in China, und chinesische Sicherheitsgesetze erlaubten es staatlichen Stellen, auf private Infrastruktur zuzugreifen. Die Modelle sammelten personenbezogene Daten und „digitale Fingerabdrücke" ihrer Nutzer. Und weil jeder Aufruf eines {{LLM}} aus Frage und Antwort besteht, könne dabei sensibles Material dorthin wandern, wo es nicht hingehört: „Die Übermittlung der genannten Informationen nach China, allein oder in Kombination mit öffentlich verfügbaren Daten, könnte verwertbare Erkenntnis über US-Personen und/oder Regierungsprogramme erzeugen", zitiert CyberScoop aus dem Schreiben. Zusätzlich warnt das DHS, die Modelle selbst könnten Schadsoftware oder Sicherheitslücken enthalten, so das Fachportal [GovInfoSecurity](https://www.govinfosecurity.com/dhs-bans-deepseek-from-federal-civilian-agencies-a-33146).

Ausnahmen sind ausdrücklich vorgesehen: Behörden können sie beantragen, die CISA prüft und genehmigt oder lehnt schriftlich ab. GovInfoSecurity nennt dafür ein Fenster von 60 Tagen ab Erlass. Die Anordnung fordert die Behörden außerdem auf, den Netzwerkverkehr auf Anzeichen für abfließende Daten zu beobachten und die Protokollierung zu verschärfen.

## Warum zählt es

Der wichtigste Punkt steht im Kleingedruckten: Die Sperre gilt nicht nur für DeepSeek, sondern für alles, was mit DeepSeek gebaut wurde. Das ist genau die Vertriebsform von {{Offene Gewichte}}-Modellen. Wer die Gewichte herunterlädt, kann sie auf eigener Hardware betreiben, anpassen und in eigene Produkte einbauen. DeepSeeks Modelle sind bei Entwicklern gerade deshalb beliebt. Eine Behörde, die solche Software einkauft, sieht auf dem Datenblatt selten, welches Modell darunter arbeitet.

Damit trifft die Anordnung eine Stelle, an der KI-Beschaffung bisher blind war. Wer bisher fragte „Ist das Produkt sicher?", muss jetzt fragen: „Welches Modell steckt drin, wo wurde es trainiert, und wer kann es zur Laufzeit austauschen?" Genau diese Frage ist in Vergabeverfahren kaum standardisiert.

Zweitens ist der Zeitpunkt bemerkenswert. In den vergangenen Wochen hat China einen Entwurf veröffentlicht, der den Export von 23 KI-Technologien beschränken soll, darunter Chipdesigns und bestimmte fortgeschrittene Modelle — wir haben am 16. Oktober [darüber berichtet](china-will-23-ki-technologien-unter-exportkontrolle-stellen.html). Peking reagierte umgehend auf die US-Sperre: Außenamtssprecherin Mao Ning sagte am Dienstag laut [TechCrunch](https://techcrunch.com/2026/10/20/us-orders-federal-agencies-to-remove-chinas-deepseek-ai-from-their-systems/), China lehne es ab, „den Begriff der nationalen Sicherheit zu überdehnen und Technologie- und Handelsfragen zu politisieren". Man werde die Rechte chinesischer Unternehmen „entschlossen schützen".

Drittens ist das Instrument selbst interessant. Der Federal Acquisition Supply Chain Security Act war bisher wenig sichtbar. Dass das Verteidigungsministerium dieselbe Rechtsgrundlage laut GovInfoSecurity auch gegen den US-Anbieter Anthropic eingesetzt hat, zeigt: Hier entsteht ein allgemeines Werkzeug, mit dem die Verwaltung Software ganzer Hersteller aussperren kann, ohne dass ein Gericht oder der Kongress mitreden muss.

Und schließlich: DeepSeek ist nicht irgendein Anbieter. Im Januar 2025 löste das Modell R1 einen Kurssturz bei Nvidia aus, weil es zeigte, dass gute {{Reasoning}}-Leistung auch mit deutlich weniger Rechenaufwand geht. Die USA werfen DeepSeek und fünf weiteren chinesischen KI-Firmen vor, mit massenhafter {{Destillation}} Informationen aus amerikanischen Modellen abgeschöpft zu haben — OpenAI und Anthropic haben ähnliche Vorwürfe separat erhoben, wie TechCrunch zusammenfasst. Der Streit um die Modelle ist also längst auch ein Streit um Herkunft und Beweislage.

## Was heißt das praktisch

Für die betroffenen Behörden beginnt eine Bestandsaufnahme. Sie müssen nicht nur die DeepSeek-App löschen, sondern jedes Werkzeug durchgehen, in dem ein DeepSeek-Modell stecken könnte — und danach den Datenverkehr beobachten. Der unangenehmste Teil ist die Beweislast: Wer nicht dokumentiert hat, welches Modell in welcher Anwendung läuft, kann nicht sagen, ob er betroffen ist.

Für Anbieter, die an Behörden verkaufen, wird die Modellherkunft zum Vergabekriterium. Wer eine Anwendung auf einem offenen Modell aufbaut, muss damit rechnen, dass die Behörde einen Nachweis verlangt — und im Zweifel lieber ein Modell aus einem Land ohne solches Zugriffsrecht nimmt. Die Anordnung erstreckt sich laut GovInfoSecurity über die Umsetzungsregeln des Beschaffungsrats auch auf Haupt- und Nachunternehmer.

Ein zweites praktisches Problem sind Vermittlungsdienste. Gateways wie OpenRouter oder das Vercel AI Gateway leiten Anfragen automatisch an den günstigsten oder leistungsfähigsten Anbieter weiter. Wer solche Dienste nutzt, ohne die Auswahl festzulegen, kann laut [heise online](https://www.heise.de/news/USA-verbannen-DeepSeek-aus-allen-zivilen-Bundesbehoerden-11494370.html) unbeabsichtigt bei DeepSeek landen. Für Behörden heißt das: Provider-Listen sperren oder den Dienst ganz meiden.

Und was ist mit den Gewichten selbst? Die Anordnung regelt, was Behörden kaufen und betreiben — nicht, was im Internet liegt. DeepSeek-Modelle bleiben herunterladbar und lokal lauffähig. Eine Sperre per Beschaffungsrecht wirkt nur dort, wo der Staat einkauft. Für alle anderen bleibt die Frage offen, ob sie einem Modell aus einem Land trauen wollen, dessen Sicherheitsbehörden Zugriff auf die Server des Anbieters haben. DeepSeek selbst arbeitet unterdessen daran, die Abhängigkeit von Nvidia zu verringern und hat Programmierwerkzeuge für Huaweis Ascend-Beschleuniger als {{Open Source}} veröffentlicht, berichtet heise.

Offen bleibt vieles. Der Text nennt keine Produktliste und keine Frist, bis wann die Systeme sauber sein müssen. Er sagt nicht, welche Folgen ein Verstoß hat. Und er definiert nicht, ob eine Anwendung betroffen ist, deren Entwickler DeepSeek nur beim Programmieren als Hilfsmittel benutzt hat — ein Unterschied, der über ganze Softwareportfolios entscheiden kann.

## Quellen

- [Federal Register: Notice of Order Regarding Exclusion and Removal of DeepSeek Products (20.10.2026, Docket DHS-2026-0628)](https://www.federalregister.gov/documents/2026/10/20/2026-21447/notice-of-order-regarding-exclusion-and-removal-of-deepseek-products-from-federal-civilian-executive)
- [CyberScoop: DHS to ban DeepSeek from federal civilian agencies (19.10.2026)](https://cyberscoop.com/dhs-bans-deepseek-federal-agencies/)
- [GovInfoSecurity: DHS Bans DeepSeek From Federal Civilian Agencies (19.10.2026)](https://www.govinfosecurity.com/dhs-bans-deepseek-from-federal-civilian-agencies-a-33146)
- [heise online: USA verbannen DeepSeek aus allen zivilen Bundesbehörden (20.10.2026)](https://www.heise.de/news/USA-verbannen-DeepSeek-aus-allen-zivilen-Bundesbehoerden-11494370.html)
- [TechCrunch: US orders federal agencies to remove China's DeepSeek AI from their systems (20.10.2026)](https://techcrunch.com/2026/10/20/us-orders-federal-agencies-to-remove-chinas-deepseek-ai-from-their-systems/)
