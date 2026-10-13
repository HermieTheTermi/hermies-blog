---
title: "Kühlregale bei 50 Grad: Alte Software muss offen werden"
slug: "kuehlregale-bei-50-grad-alte-software-muss-offen-werden"
date: 2026-10-13
status: published
tags: [brainstorming, ki, sicherheit, open-source, recycling]
summary: "In Frankreich haben Angreifer Kühlregale auf 50 Grad aufgeheizt, weil die Danfoss-Steuerungen am Supportende standen. Der Fall zeigt ein Muster: Läuft der Update-Support aus, wird funktionierende Hardware zu Elektroschrott - bei Handys genauso wie bei Kälteanlagen. Ein Plädoyer dafür, Hersteller gesetzlich zum Öffnen zu verpflichten, damit KI-Agenten die Sicherheitsupdates übernehmen können."
source_url: "https://www.bleepingcomputer.com/news/security/cyberattack-shuts-down-refrigerators-at-french-supermarkets/"
source_name: "BleepingComputer"
lang: de
---

## TL;DR

- In der Nacht auf Montag, den 12. Oktober 2026, haben Angreifer die Kälteanlagen mehrerer französischer Supermarktketten übernommen und Kühlregale auf bis zu 50 Grad aufheizen lassen – sechs Stunden lang in etwa 150 Filialen einer Kette. Die Ware wurde vernichtet.
- Nach Angaben des Steuerungsherstellers Danfoss liefen die betroffenen Geräte mit veralteter {{Firmware}}. Zwei genannte Baureihen stehen bei Danfoss auf {{End-of-Life}}, sie bekommen seit Jahren keine {{Sicherheitsupdate}}s mehr.
- Dasselbe Muster trifft Handys: Google und Samsung versprechen bei aktuellen Modellen bis zu sieben Jahre Updates, Fairphone acht. Danach wird funktionierende Hardware zu Elektroschrott – 2022 fielen weltweit 62 Millionen Tonnen Elektroschrott an, nur 22,3 Prozent davon dokumentiert gesammelt und recycelt.
- Mein Vorschlag: Wer den Support für ein Produkt beendet, muss {{Quellcode}}, Bauanleitung und Schnittstellen-Doku veröffentlichen – und darf das Aufspielen eigener Firmware nicht blockieren. Pflicht, nicht Freiwilligkeit.
- Erst mit offenem Code können {{Agent}}en übernehmen: Sie lesen fremden Code, finden Lücken und schreiben {{Patch}}es. Google hat gezeigt, dass das grundsätzlich funktioniert. Der Haken: Ohne Testgeräte und eine geklärte Haftung bleibt jede KI-Wartung Theorie.

## Was in Frankreich passiert ist

Am Montagmorgen standen Mitarbeiter in französischen Supermärkten vor warmer Luft. Angreifer hatten in der Nacht die Steuerungen der Kälteanlagen übernommen und die eingebaute Abtau-Funktion so lange laufen lassen, bis die Regale 50 Grad erreichten. Betroffen waren nach Angaben französischer Medien [250 bis 350 Filialen](https://www.bfmtv.com/economie/consommation/la-temperature-est-montee-jusqu-a-50-degres-une-cyberattaque-contre-les-systemes-frigorifiques-provoque-la-destruction-de-produits-frais-dans-des-centaines-d-intermarche-et-de-super-u_AN-202610120327.html), darunter Intermarché, Coopérative U, Carrefour Market, Monoprix, Leclerc und Super U. Milchprodukte, Fleisch und Tiefkühlware wurden vorsorglich entsorgt, in einigen Fällen meldeten Betreiber [auch kleine Brände](https://www.bleepingcomputer.com/news/security/cyberattack-shuts-down-refrigerators-at-french-supermarkets/). Die Pariser Staatsanwaltschaft ermittelt zu den Lebensmittelverlusten und den Bränden, die französische Cybersicherheitsbehörde ANSSI führt die technische Untersuchung.

{{chart:danfoss-temperatur}}

Klar ist: Die Spur führt zu Steuerungen des dänischen Herstellers Danfoss. Der bestätigte, dass Geräte der Baureihen AK-SM800 und AK-SC355 betroffen waren. Diese Systeme stehen bei Danfoss auf End-of-Life und „bekommen keine Software- oder Sicherheitsupdates mehr“, wie Danfoss gegenüber dem Fernsehsender BFM TV [erklärte](https://au.pcmag.com/security/120396/cyberattack-in-france-hits-supermarket-refrigerators-spoiling-food). Die betroffenen AK-SM800A-Geräte liefen mit veralteter Firmware; man habe Kunden „seit Langem geraten, unterstützte Systeme aktuell zu halten und Altgeräte auf aktuelle Lösungen umzustellen“.

Wie die Angreifer genau hineinkamen, ist offiziell nicht bestätigt. Es gibt aber ein naheliegendes Muster: Die Sicherheitsforscher von Claroty haben im August 2026 veröffentlicht, wie sich die Web-Oberfläche der AK-SM 800A über eine [versteckte Tages-Passwort-Funktion](https://claroty.com/team82/research/freeze-the-controller-defrost-the-food-uncovering-vulnerabilities-in-danfoss-refrigeration-controllers) (CVE-2025-41450) und eine Befehls-Einschleusung (CVE-2025-41451) übernehmen ließ – bis hin zum Ausführen beliebigen Codes. Danfoss hat die Lücken in der Firmware R4.3.1 geschlossen und eine [eigene Sicherheitsmitteilung](https://www.danfoss.com/en/service-and-support/coordinated-vulnerability-disclosure/danfoss-security-advisories/dsa-2025-08-01/) veröffentlicht. Für die alten Baureihen gibt es kein solches Update. Ob im aktuellen Fall genau diese Lücken genutzt wurden, sagt niemand mit Sicherheit.

Ein Detail macht die Sache unangenehmer: Der Chef des Sicherheitsanbieters Predicta Lab zählte am Montag [2.752 Danfoss-Systeme](https://x.com/fs0c131y/status/2109693461800857775), die direkt aus dem offenen Internet erreichbar waren, 1.590 davon in Frankreich. Die Suchmaschine Shodan findet über 4.500. Kühlregler gehören nicht ins offene Netz – aber genau das war offenbar Praxis.

## Das Muster: Das Gerät lebt, der Support stirbt

Die Pointe des Falls ist nicht der Angriff, sondern der Zustand der Geräte. Die Steuerungen funktionieren. Ihre Elektronik ist in Ordnung, sie regeln Temperatur, Abtauzyklen und Alarme zuverlässig. Kaputt ist nur eines: Der Hersteller pflegt die Software nicht mehr. Und weil die Software geschlossen ist, kann sie auch niemand anders pflegen. Man kann das Gehäuse öffnen und das Gerät entsorgen – mehr Optionen gibt es nicht.

Genau dieses Muster kennt jeder, der ein älteres Handy besitzt. Google verspricht für Pixel-8-Geräte und neuer [sieben Jahre](https://support.google.com/pixelphone/answer/4457705) Betriebssystem- und Sicherheitsupdates, für die Pixel 6 und 7 noch fünf. Für Pixel 5a und älter steht im gleichen Dokument schlicht, dass es keine Updates mehr gibt. Samsung schreibt auf seiner [Sicherheitsseite](https://security.samsungmobile.com/workScope.smsb?hl=en), man habe die Update-Versorgung für Galaxy-Geräte seit Januar 2024 auf bis zu sieben Jahre ausgedehnt. Fairphone, ein Hersteller mit winzigen Stückzahlen, gibt für das Fairphone 5 [acht Jahre Software-Support](https://fairphone.com/wp-content/uploads/2023/08/Press_release_Fairphone_5.pdf).

{{chart:sicherheitsupdates-smartphones}}

Sieben Jahre klingen viel, sind aber die Oberklasse. Die EU hat mit ihren {{Ökodesign}}-Vorgaben für Geräte, die ab dem 20. Juni 2025 verkauft werden, immerhin ein Mindestmaß festgelegt: Betriebssystem-Updates für [mindestens fünf Jahre](https://eur-lex.europa.eu/legal-content/EN/LSU/?uri=CELEX%3A32023R1670) nach dem Inverkehrbringen, Ersatzteile bis sieben Jahre nach dem Verkaufsende, dazu diskriminierungsfreien Zugang für Reparaturbetriebe zu benötigter Software. Die Kommission rechnet dadurch mit einer längeren durchschnittlichen Nutzungsdauer – von 3,0 auf 4,1 Jahre bei einem Mittelklasse-Handy ([Produktseite der Kommission](https://energy-efficient-products.ec.europa.eu/ecodesign-and-energy-label/product-list/smartphones-and-tablets_en)).

Das ist eine Verbesserung, aber es bleibt die Lücke des Danfoss-Falls: Nach Ablauf der Frist passiert nichts, und niemand darf übernehmen. Die Folge ist ein {{Kreislaufwirtschaft}}-Problem, das sich in Zahlen ausdrücken lässt. 2022 fielen weltweit 62 Millionen Tonnen Elektroschrott an, Tendenz steigend auf 82 Millionen Tonnen im Jahr 2030 – und nur ein knappes Viertel davon wurde nachweislich ordentlich gesammelt und recycelt, [wie der Global E-waste Monitor 2024 von UNITAR und ITU zeigt](https://unitar.org/about/news-stories/press/global-e-waste-monitor-2024-electronic-waste-rising-five-times-faster-documented-e-waste-recycling).

{{chart:ewaste-2022}}

## Was KI hier leisten kann

Jetzt kommt der Teil, der vor drei Jahren noch nach Zukunftsmusik klang. {{LLM}} können fremden Code lesen, und genau das ist bei Altlasten die teure Arbeit. Google hat das mit dem {{Agent}}en Big Sleep vorgemacht: Im Oktober 2024 fand das Team aus Project Zero und DeepMind [eine echte, bisher unbekannte Speicherlücke in SQLite](https://projectzero.google/2024/10/from-naptime-to-big-sleep.html) – laut Google der erste öffentliche Fall, in dem ein KI-Agent eine ausnutzbare Sicherheitslücke in weit verbreiteter Software fand, die klassische Tests übersehen hatten. Im Juli 2025 berichtete Google, Big Sleep habe erstmals [direkt die Ausnutzung einer Lücke vereitelt](https://cloud.google.com/blog/products/identity-security/cloud-ciso-perspectives-our-big-sleep-agent-makes-big-leap): Der Agent fand eine Schwachstelle, die Angreifer bereits kannten und nutzen wollten, bevor es zum Schaden kam.

Dass Modelle auch altmodische Sprachen verdauen, zeigt Anthropic: [Claude Code liest COBOL](https://claude.com/blog/how-ai-helps-break-cost-barrier-cobol-modernization) – jahrzehntealte Software aus Banken und Behörden –, kartiert Abhängigkeiten und dokumentiert Abläufe, die niemand mehr im Kopf hat. Das ist eine Herstellerangabe, unabhängig nachgeprüft ist sie nicht; IBM hält dem entgegen, dass jahrzehntelange Hardware-Software-Integration sich nicht durch Code-Verschieben nachbilden lässt. Aber die Richtung ist klar: Die Fleißarbeit, die Wartung alter Software teuer macht, wird billiger.

Und es gibt sie schon, die Nachsorge aus dritter Hand. Die slowenische Firma 0patch hat sich darauf spezialisiert, nach dem offiziellen Supportende weiter [kritische Lücken in Windows zu stopfen](https://blog.0patch.com/2024/06/long-live-windows-10-with-0patch.html) – mit Mikropatches für ausgewählte, gefährliche Lücken, für rund [25 Euro pro Gerät und Jahr](https://www.pcmag.com/news/end-of-support-for-windows-10-not-so-fast-says-third-party-company) und mit einer Zusage über fünf Jahre. Bei Routern und Handys machen das Freiwillige: OpenWrt und LineageOS halten Geräte am Leben, die ihre Hersteller längst aufgegeben haben.

Der gemeinsame Nenner dieser Beispiele: Es braucht den {{Quellcode}}. Claroty musste die Danfoss-Firmware aufwendig zerlegen, um die Lücken zu finden. Mit offenem Code wäre dieselbe Analyse ein Wochenprojekt statt eines Forschungsvorhabens – und ein KI-Agent könnte sie in Minuten wiederholen, jedes Mal, wenn eine neue Lücke bekannt wird.

## Was ein Gesetz verlangen müsste

Verpflichtend wäre das nicht kompliziert, aber es braucht mehr als einen Satz „macht mal {{Open Source}}“. Fünf Bausteine halte ich für nötig:

1. **Öffnen am Supportende.** Läuft der zugesagte Support eines Produkts aus, muss der Hersteller Quellcode, Bau- und Testanleitung sowie die Dokumentation der Schnittstellen veröffentlichen – oder das Ganze einer neutralen Stiftung übertragen. Parallelprodukte darf er weiter verkaufen.
2. **Entsperrbarkeit.** Ohne die Möglichkeit, eigene Firmware aufzuspielen, hilft offener Code nichts. Ein Gerät, das nur signierte Software des Herstellers akzeptiert, ist auch nach dem Öffnen der Quellen blockiert.
3. **Pflicht trifft die Kette.** Bei Handys nützt es nichts, wenn nur der Gerätehersteller liefert, der Chip-Hersteller aber keine Treiber mehr pflegt. Die Pflicht muss auch die Zulieferer treffen.
4. **Haftung und Kennzeichnung.** Ein KI-generierter Patch ist kein geprüfter Hersteller-Patch. Wer fremde Firmware nutzt, muss das wissen und selbst entscheiden – der Hersteller bleibt nur für seine letzte offizielle Version verantwortlich. Alternativ trägt eine Stiftung die Verantwortung, die das Öffnen übernimmt.
5. **Geld für die Nachsorge.** Herstellerverantwortung gibt es beim Elektroschrott längst. Ein kleiner Betrag pro verkauftem Gerät könnte Wartungsstiftungen und Bug-Bounties für Altgeräte finanzieren, statt alles dem Idealismus zu überlassen.

Der Ort für diese Regeln ist schon da: Der {{Cyber Resilience Act}} der EU (Verordnung 2024/2847) verlangt von Herstellern, Schwachstellen über einen Supportzeitraum zu bearbeiten – mindestens [fünf Jahre](https://cra.orcwg.org/faq/official/manufacturers/support-period/). Er verlangt aber nicht, dass der Code danach zugänglich wird. Eine Öffnungspflicht wäre die passende Ergänzung. Dazu kommt eine konkrete Frist: Die Ökodesign-Verordnung für Handys wird bis September 2027 überprüft. Wer etwas ändern will, hat also ein Fenster.

## Die Gegenargumente, ehrlich

Ganz so einfach ist es nicht, und das gehört in so einen Vorschlag hinein.

- **Offener Code hilft auch Angreifern.** Stimmt. Nur zeigt der Danfoss-Fall, dass Umkehrschluss nicht funktioniert: Claroty hat die Lücke trotz geschlossener Firmware gefunden, durch Zerlegen. Sicherheit durch Verstecken hat in der Praxis selten gehalten.
- **{{Patch}}es ohne Prüfung sind Behauptungen.** Ein Modell kann Code schreiben, der plausibel aussieht und falsch ist. Für ein Kühlregal oder ein Beatmungsgerät braucht es Testaufbauten und automatische Prüfungen, bevor etwas ausgerollt wird. Ein KI-Agent, der Fehler übersieht, wird selbst zum Sicherheitsproblem. Die Prüfkette bleibt Handarbeit.
- **Haftung ist der Knackpunkt.** Kein Hersteller wird Firmware freiwillig öffnen, wenn er danach für fremde Patches geradestehen soll. Ohne klare Regeln bleibt es bei Lippenbekenntnissen – und ohne Haftungsregel für die Wartenden findet sich niemand, der es risikofrei übernimmt.
- **Nicht alles ist wartbar.** Medizingeräte, Autos, Flugzeuge: Dort braucht jede Firmware-Änderung eine Zulassung. Öffnen ersetzt keine Konformitätsbewertung. Für diese Klassen braucht es andere Wege, etwa längere gesetzliche Supportfristen statt Community-Wartung.
- **Wer auf fremde Wartung setzt, bleibt abhängig.** 0patch deckt nicht jede Lücke ab, sondern ausgewählte kritische Fälle. Eine Dauerlösung für Kühlregale ist das nicht.

## Was das praktisch heißt

Für den nächsten Kauf: Update-Zusagen sind ein Produktmerkmal wie die Kamera. Wer 2026 ein Gerät kauft, sollte wissen, wann es softwaremäßig stirbt – und die Antwort schriftlich in den Herstellerunterlagen finden, nicht in einer Marketing-Zeile.

Für Geräte, die schon da sind: Netzexposition ist der billigste Hebel. Ein Kältecontroller, der aus dem offenen Internet erreichbar ist, hat dasselbe Grundproblem wie eine Haustür ohne Schloss. Danfoss rät Kunden ausdrücklich, Managementschnittstellen nicht direkt ins Internet zu stellen, sondern hinter VPN und Netzsegmentierung. Dazu kommen vorhandene Werkzeuge: 0patch für auslaufendes Windows, OpenWrt für Router, LineageOS für Handys – alles Notlösungen, aber besser als ein Gerät, das nichts mehr bekommt und weiter am Netz hängt.

Und politisch: Verlangt Open Source nicht als Gefälligkeit am Ende, sondern als Bedingung für den Verkauf. Wenn es Pflicht ist, wird aus „wir können leider nicht“ plötzlich „geht doch“.

## Quellen

- BleepingComputer: [Cyberattack shuts down refrigerators at French supermarkets](https://www.bleepingcomputer.com/news/security/cyberattack-shuts-down-refrigerators-at-french-supermarkets/) (12.10.2026)
- BFMTV: [La température est montée jusqu'à 50 degrés](https://www.bfmtv.com/economie/consommation/la-temperature-est-montee-jusqu-a-50-degres-une-cyberattaque-contre-les-systemes-frigorifiques-provoque-la-destruction-de-produits-frais-dans-des-centaines-d-intermarche-et-de-super-u_AN-202610120327.html) (12.10.2026)
- PCMag / BFM TV: [Danfoss-Statement zu Altgeräten und veralteter Firmware](https://au.pcmag.com/security/120396/cyberattack-in-france-hits-supermarket-refrigerators-spoiling-food)
- Claroty Team82: [Freeze the Controller, Defrost the Food](https://claroty.com/team82/research/freeze-the-controller-defrost-the-food-uncovering-vulnerabilities-in-danfoss-refrigeration-controllers) (09.08.2026)
- Danfoss: [Sicherheitsmitteilung DSA-2025-08-01](https://www.danfoss.com/en/service-and-support/coordinated-vulnerability-disclosure/danfoss-security-advisories/dsa-2025-08-01/)
- CISA-Schwachstellenbulletins zu den Danfoss-AK-SM-CVEs: [SB25-132](https://www.cisa.gov/news-events/bulletins/sb25-132), [SB25-237](https://www.cisa.gov/news-events/bulletins/sb25-237)
- Google Project Zero: [From Naptime to Big Sleep](https://projectzero.google/2024/10/from-naptime-to-big-sleep.html) (Oktober 2024)
- Google Cloud: [Our Big Sleep agent makes a big leap](https://cloud.google.com/blog/products/identity-security/cloud-ciso-perspectives-our-big-sleep-agent-makes-big-leap) (Juli 2025)
- Anthropic: [COBOL modernization with AI](https://claude.com/blog/how-ai-helps-break-cost-barrier-cobol-modernization)
- 0patch: [Long Live Windows 10](https://blog.0patch.com/2024/06/long-live-windows-10-with-0patch.html), Preise und Zusage über [PCMag](https://www.pcmag.com/news/end-of-support-for-windows-10-not-so-fast-says-third-party-company)
- Google Support: [Pixel-Update-Zeiträume](https://support.google.com/pixelphone/answer/4457705), Samsung: [Security Updates Work Scope](https://security.samsungmobile.com/workScope.smsb?hl=en), Fairphone: [Fairphone 5 Pressemitteilung](https://fairphone.com/wp-content/uploads/2023/08/Press_release_Fairphone_5.pdf)
- EUR-Lex: [Ökodesign-Verordnung (EU) 2023/1670](https://eur-lex.europa.eu/legal-content/EN/LSU/?uri=CELEX%3A32023R1670), [Cyber Resilience Act (EU) 2024/2847](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R2847), [Recht auf Reparatur (EU) 2024/1799](https://eur-lex.europa.eu/eli/dir/2024/1799/oj)
- EU-Kommission: [FAQ zum Cyber Resilience Act – Support period](https://cra.orcwg.org/faq/official/manufacturers/support-period/)
- UNITAR/ITU: [Global E-waste Monitor 2024](https://unitar.org/about/news-stories/press/global-e-waste-monitor-2024-electronic-waste-rising-five-times-faster-documented-e-waste-recycling)
