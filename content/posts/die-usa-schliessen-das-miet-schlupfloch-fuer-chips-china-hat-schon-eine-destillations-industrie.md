---
title: "Die USA schließen das Miet-Schlupfloch für Chips, China hat schon eine Destillations-Industrie"
slug: "die-usa-schliessen-das-miet-schlupfloch-fuer-chips-china-hat-schon-eine-destillations-industrie"
date: 2026-11-17
status: published
tags: [news, distillation, llm, openai]
summary: "Eine Eilverordnung vom 16. November verlangt US-Lizenzen für Rechenzentren, die gemietete Rechenleistung an chinesische Firmen weitergeben. Einen Tag später zeigt eine Reuters-Recherche, dass China den Chipmangel längst mit einer eigenen Industrie aus abgeschöpften Modellantworten umgeht."
source_url: "https://www.bis.gov/press-release/bis-issues-rule-addressing-remote-access-american-super-intelligence-technology"
source_name: "Bureau of Industry and Security"
lang: de
---

## TL;DR

- Das US-Handelsministerium hat am 16. November eine Eilverordnung veröffentlicht. Wer ein {{Rechenzentrum}} irgendwo auf der Welt mit KI-Chips beliefert, braucht dafür eine US-Lizenz, wenn dort mehr als zwölf Millionen aggregierte Rechenleistung für Firmen mit Sitz in China, Macau oder der Ländergruppe D:5 bereitsteht.
- Für fünf Länder gilt eine eigene Lizenzpflicht, die zusätzlich greift: Indonesien, Malaysia, Singapur, Thailand und Brasilien. Das Ministerium nennt sie Ziele mit erhöhtem Umleitungsrisiko.
- Auslöser ist der Schmuggelverdacht gegen den Chip-Händler Megaspeed. Nvidia verlor am Handelstag bis zu 2,9 Prozent, der Philadelphia-Halbleiterindex bis zu 5,5 Prozent.
- Einen Tag später veröffentlichte Reuters eine Recherche über mehr als 300 chinesische Dokumente: {{Destillation}} ist dort keine Forschung mehr, sondern ein Industriezweig mit Arbeitsteilung.
- Ein Beispiel aus den Akten: Rund 5.000 Antworten von OpenAIs o1-Modell, übersetzt mit GPT-4o mini, ergaben 10.750 zweisprachige Trainingsbeispiele für Qwen2.5-72B.
- Destillation ist nicht illegal, verstößt aber gegen die Nutzungsbedingungen der US-Anbieter. Chinesische Regulierer verteidigen sie als Standardverfahren der Branche.

## Eine Lizenz für gemietete Rechenleistung

Die Regel heißt „Addressing Remote Access to Advanced Semiconductors", trägt die Nummer RIN 0694-AK50 und wurde laut der [Pressemitteilung des Bureau of Industry and Security](https://www.bis.gov/press-release/bis-issues-rule-addressing-remote-access-american-super-intelligence-technology) vom 16. November „written by and at the direction of" von Finanzministerium und Nationalem Sicherheitsrat. Diese Formulierung ist ungewöhnlich offen. Sie sagt, wer in Washington die Feder geführt hat, und sie sagt, wie ungeduldig die Urheber waren.

Inhaltlich schließt der Erlass eine Lücke, die seit Jahren offenstand. Bisher kontrollierten die USA, welche Chips physisch in welches Land gehen. Wer die Hardware nicht importieren durfte, mietete stattdessen Rechenzeit in einem Datenzentrum in Singapur oder Malaysia, das die Chips legal gekauft hatte. Die neue Regel knüpft die Lizenz an das Wissen des Lieferanten über den Endabnehmer. Daneben gilt eine separate Lizenzpflicht für Lieferungen in die fünf genannten Länder, mit Einzelfallprüfung.

Die Schwelle liegt bei zwölf Millionen „aggregate TPP". TPP steht für Total Processing Performance, eine Kennzahl, mit der das Ministerium die Rechenleistung von KI-Chips bewertet. Die Summe zählt über ein Gebäude hinaus auch verbundene Standorte zusammen. Wer bereits heute solche Kapazität an chinesische Firmen vermittelt, muss innerhalb von 90 Tagen nach Inkrafttreten eine Lizenz beantragen oder damit rechnen, künftig gesperrt zu werden. Ausgenommen sind Töchter von US-Firmen, die monatlich Meldung erstatten, und Rechenzentren, die ausschließlich Empfehlungssysteme für Online-Händler oder soziale Netze betreiben.

Der Erlass hebt außerdem die „AI Diffusion Rule" der Biden-Regierung förmlich auf. Er tritt mit der Veröffentlichung im Federal Register in Kraft, danach sind 60 Tage Stellungnahme vorgesehen. Eine Kanzleizusammenfassung mit den Details hat [Nixon Peabody am 16. November veröffentlicht](https://www.nixonpeabody.com/insights/alerts/2026/11/16/bis-targets-remote-access-to-advanced-chips-through-overseas-data-centers).

## Warum der Umweg über Mietrechenzeit zählt

Der politische Auslöser war kein Handelsstreit, sondern ein Skandal. Nvidia-Chef Jensen Huang trat zurück, nachdem eine Affäre mit einer ehemaligen Managerin des Singapurer Händlers Megaspeed bekannt wurde. Die Frau lebt inzwischen in China, die Behörden ermitteln wegen Spionage, und Megaspeed soll gesperrte Nvidia-Chips in ein chinesisches Rechenzentrum vermittelt haben. Die Firma bestreitet das. Wie es zu dem Rücktritt kam, steht in [unserem Artikel zu den vier Tagen danach](https://hermiethetermi.github.io/hermies-blog/nvidia-ohne-jensen-huang-der-ruecktritt-kam-vier-tage-nach-dem-vertrauensvotum.html).

An der Börse kam die Regel schlecht an. Nvidia verlor nach der Ankündigung bis zu 2,9 Prozent, der Philadelphia Semiconductor Index bis zu 5,5 Prozent, wie [The Decoder unter Berufung auf Bloomberg berichtet](https://the-decoder.com/the-us-wants-to-block-china-from-renting-ai-power-abroad-but-china-already-built-a-parallel-supply-chain-from-us-ai-output/). Ein Index, der die ganze Branche abbildet, fällt selten stärker als der Einzelwert, um den es geht. Das ist der Hinweis darauf, dass Anleger hier keine Nvidia-Geschichte sehen, sondern eine Nachfragegeschichte.

Denn Rechenzeit ist für chinesische Entwickler der knappe Faktor, nicht der Chip an sich. Wer mietet, umgeht Zoll, Lieferkette und Stückzahlenbegrenzung in einem Schritt. Die Regel trifft damit nicht den Warenaustausch, sondern den Zugang zu einem Dienst. Genau deshalb steht in der BIS-Mitteilung, man wolle den Schutz „align" mit den bestehenden Kontrollen für physische Lieferungen. Kontrollen für Datenströme gab es vorher nicht.

## Aus Forschungsnot wurde eine Branche

Am Tag nach der Regel veröffentlichte Reuters eine Recherche, die das Gegenstück beschreibt. Das Reuters-Team hat mehr als 300 chinesische Fachartikel, Patente, Unternehmensangaben, Stellenanzeigen und Regierungsdokumente durchgesehen. Sein Befund verschiebt die ganze Debatte: Die Chipsperre hat die chinesische KI nicht ausgebremst. Sie hat eine eigene Industrie hervorgebracht, die aus den Antworten amerikanischer Modelle Trainingsmaterial macht.

{{Destillation}} funktioniert so: Ein großes Lehrermodell beantwortet Fragen, schreibt Code oder löst Aufgaben. Diese Ausgaben werden gesammelt und ein kleineres Schülermodell darauf trainiert. Der Schüler erreicht einen Teil der Fähigkeiten zu einem Bruchteil der Kosten. Was als akademischer Notbehelf begann, ist laut Reuters heute arbeitsteilig organisiert: Firmen bauen Software, die das Abschöpfen automatisiert, Fachkräfte bereiten die Daten auf, kleinere Modelle werden damit trainiert.

{{zeitleiste:destillation-china}}

Ein Detail aus der Recherche verdient Hervorhebung. Forscher der Shanghai Jiao Tong University haben im November 2024 etwa 5.000 Antworten des OpenAI-Modells o1 gesammelt, mit GPT-4o mini übersetzt und daraus 10.750 zweisprachige Trainingsbeispiele gebaut, um Alibabas Qwen2.5-72B weiterzutrainieren. Die Autoren warnten in dem Paper selbst vor einer Abhängigkeit von fremden Innovationen.

Der Rest ist Politik. Acht Ministerien veröffentlichten im Januar ein Paket namens „AI+Manufacturing", das Verfahren zur Senkung des Rechenbedarfs ausdrücklich empfiehlt. Programme in Shanghai und Shenzhen tun dasselbe. Offizielle Dokumente sagen nirgends, man solle amerikanische Modelle kopieren. Sie fördern Effizienz, und Effizienz heißt in der Praxis: das stärkste verfügbare Modell als Datenquelle nutzen.

## Der Haken: legal, aber nicht erlaubt

{{Destillation}} ist in keinem Land verboten und wird überall betrieben, auch in Europa und den USA. Sie verstößt aber gegen die Nutzungsbedingungen von OpenAI, Anthropic und Google. Die Anbieter haben die Praxis wiederholt dokumentiert. Anthropic erklärte zuletzt, es blockiere inzwischen „bis zu 99 Prozent" der Versuche, Reasoning-Tokens abzuschöpfen. OpenAI veröffentlichte Berichte über Kampagnen, die Tausende Konten umfassten.

Auf chinesischer Seite ist die Rechtslage unklar, und das ist der eigentliche Grund für die Aufregung. Im Juli trafen sich US-Beamte in Chengdu mit chinesischen Regulierern, wie Reuters aus drei Quellen erfährt. Die Amerikaner warnten, einige Formen der Destillation kämen Wirtschaftsspionage gleich. Die chinesischen Vertreter antworteten, Destillation sei ein übliches Entwicklungsverfahren, und man werde einschreiten, wenn sie tatsächlich Diebstahl geistigen Eigentums darstelle. Konkrete Zusagen gab es nicht. In den vergangenen Monaten fragten chinesische Entwickler laut Reuters beim Ministerium für Industrie nach Leitlinien, weil sie selbst nicht wissen, wo die Grenze liegt.

Finanzminister Scott Bessent droht inzwischen mit Sanktionen und Aufnahme in die Entity List, falls Destillation in Diebstahl übergeht. Ein Werkzeug der Exportkontrolle ist das nicht mehr. Es ist Strafrecht auf Verdacht.

## Was das praktisch heißt

Für Betreiber von Rechenzentren in den fünf Ländern ändert sich der Alltag sofort: Kundenprüfung, Meldepflichten, Wartezeit auf Lizenzen. Wer nicht weiß, wem die Muttergesellschaft seines Mieters gehört, kann die Lieferung nicht mehr sauber dokumentieren. Für chinesische Entwickler ändert sich dagegen wenig an der Strategie. Kleinere Modelle auf Basis abgeschöpfter Daten brauchen weniger Chips, nicht mehr, und sie laufen auf Hardware, die längst im Land ist.

Die Regel schließt also den Zugang zu gemieteter Rechenleistung und lässt den zweiten Weg offen, der laut Reuters schon industriell genutzt wird. Ob das reicht, hängt an einer Frage, die keine der beiden Quellen beantwortet: Wie viel von dem Vorsprung, den amerikanische Modelle haben, steckt in den Antworten, die man abschöpfen kann? Die Paper der chinesischen Forscher deuten auf viel. Die Anbieter, die ihre Ausgaben drosseln, deuten auf weniger.

Klar ist nur die Richtung. Washington verschiebt den Kontrollpunkt vom Hafen in die Cloud. Der Aufwand dafür wächst mit jedem Dienst, den man nicht sieht.

## Quellen

- Bureau of Industry and Security, Pressemitteilung „BIS Issues Rule Addressing Remote Access to American Super Intelligence Technology", 16.11.2026: https://www.bis.gov/press-release/bis-issues-rule-addressing-remote-access-american-super-intelligence-technology
- Interim Final Rule RIN 0694-AK50 (Entwurf als PDF), BIS: https://www.bis.gov/media/documents/rin-0694-ak50.pdf
- Nixon Peabody, „BIS targets remote access to advanced chips through overseas data centers", 16.11.2026 (Schwelle 12 Mio. TPP, 90 Tage, 60 Tage Kommentarfrist, Aufhebung der AI Diffusion Rule): https://www.nixonpeabody.com/insights/alerts/2026/11/16/bis-targets-remote-access-to-advanced-chips-through-overseas-data-centers
- CBS News, „After Nvidia scandal, Commerce Department moves to curb remote access to AI chips", 16.11.2026 (fünf Länder, erhöhtes Umleitungsrisiko): https://www.cbsnews.com/news/nvidia-jensen-huang-commerce-department-limit-remote-access-ai-chips/
- Reuters, „EXCLUSIVE: China taps US AI models to train homegrown rivals as chip curbs bite", 17.11.2026: https://www.reuters.com/world/china/china-taps-us-ai-models-train-homegrown-rivals-chip-curbs-bite-2026-11-17/
- The Decoder, „The US wants to block China from renting AI power abroad but China already built a parallel supply chain from US AI output", 17.11.2026 (Kursverluste nach Bloomberg, Anthropics 99-Prozent-Angabe): https://the-decoder.com/the-us-wants-to-block-china-from-renting-ai-power-abroad-but-china-already-built-a-parallel-supply-chain-from-us-ai-output/
