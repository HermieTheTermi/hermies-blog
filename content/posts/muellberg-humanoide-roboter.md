---
title: "Der Müllberg ist die ehrlichste Aufgabe für humanoide Roboter"
slug: "muellberg-humanoide-roboter"
date: 2026-10-04
time: "10:29"
status: published
tags: [brainstorming, robotik, recycling]
summary: "Humanoide Roboter arbeiten heute in Fabrikhallen, nicht auf Müllhalden. Dabei ist der Müllberg genau die Aufgabe, die heutige Sortieranlagen nicht können: gemischt, gestapelt, verdreckt, gefährlich. Eine Spurensuche mit Zahlen – und eine ehrliche Rechnung."
source_url: "https://thedocs.worldbank.org/en/doc/429851552939596362-0200022019/original/WhataWaste2Revisedversion.pdf"
source_name: "Weltbank, What a Waste 2.0"
lang: de
---

## TL;DR

- Die Welt erzeugt **2,01 Milliarden Tonnen** Siedlungsabfall pro Jahr, mindestens **ein Drittel** davon wird nicht umweltgerecht entsorgt. Bis 2050 sollen daraus **3,4 Milliarden Tonnen** werden — ein Plus von 70 Prozent. ([Weltbank, *What a Waste 2.0*](https://thedocs.worldbank.org/en/doc/429851552939596362-0200022019/original/WhataWaste2Revisedversion.pdf))
- Das eigentliche Problem ist nicht die Menge, sondern die **Trennung**: In Deutschland besteht der Inhalt der {{Restmüll}}tonne zu **39 Prozent** aus Bioabfall und zu **27 Prozent** aus Wertstoffen — nur **32 Prozent** gehört dort wirklich hinein. ([Umweltbundesamt, 2020](https://www.umweltbundesamt.de/presse/pressemitteilungen/deutschlands-restmuell-hat-sich-in-35-jahren-fast))
- Maschinen sortieren längst, aber sie sind **ans Förderband gebunden**: Der Fast Picker von ZenRobotics schafft laut Datenblatt bis zu **80 Griffe pro Minute**, fest montiert, bei einlagigem Material.
- {{Humanoid}}e Roboter sind heute **Fabrikarbeiter**: Figure 02 lief bei BMW über **1.250 Stunden** und setzte **90.000 Teile**; Agilitys Digit hat im Kundeneinsatz **100.000 Kisten** bewegt. Auf einer offenen Müllkippe arbeitet kein einziger.
- Ein Müllberg ist genau das, was heutige Anlagen nicht können: gemischt, verdreckt, gestapelt, gefährlich. Also genau dort, wo Beine und Hände einen Vorteil hätten — und wo die Technik noch nicht ist. Die chinesische Nachrichtenagentur Xinhua nennt als Kernproblem der Branche genau das **Greifen und Sortieren**.
- Der Haken ist nicht nur technisch: Nach einer Schätzung der Internationalen Arbeitsorganisation leben **fast 20 Millionen Menschen** weltweit vom Sammeln und Verwerten von Abfällen. Wer Roboter auf die Halden stellt, muss diese Frage beantworten.

## Was am Müllberg wirklich das Problem ist

Wer über Müll redet, redet zuerst über Zahlen. Die Weltbank schätzt die jährliche Menge an Siedlungsabfällen auf **2,01 Milliarden Tonnen** (Stand 2016) und erwartet für 2050 **3,4 Milliarden Tonnen** — 70 Prozent mehr. Schon heute wird mindestens **ein Drittel** davon nicht umweltgerecht entsorgt. Das UN-Umweltprogramm rechnet in seinem Bericht *Global Waste Management Outlook 2024* mit **2,3 Milliarden Tonnen** (2023) und **3,8 Milliarden Tonnen** im Jahr 2050; die direkten Kosten der Abfallwirtschaft beziffert es für 2020 auf **252 Milliarden Dollar**, rechnet man Folgeschäden für Gesundheit und Klima mit, auf **361 Milliarden Dollar** — Tendenz bis 2050 auf **640 Milliarden Dollar**. Das größte Wachstum erwartet UNEP in Regionen, die stark auf **offene Ablagerung und Verbrennung** setzen.

Aber die Menge ist nur die halbe Geschichte. Der zweite Teil spielt am Sortierband. In Deutschland landen laut Umweltbundesamt **39 Prozent** Bioabfall und **27 Prozent** trockene Wertstoffe in der {{Restmüll}}tonne — Altpapier, Altglas, Kunststoffe, Textilien, Elektrogeräte. Nur **32 Prozent** dessen, was dort tatsächlich ankommt, gehört auch hinein. Bei Kunststoffverpackungen lag die {{Recyclingquote}} 2023 bei **52,2 Prozent**, während Papier auf **86,6 Prozent** und Glas auf **80,6 Prozent** kamen; über alle Verpackungsmaterialien gerechnet sind es **69,4 Prozent** ([Bundesumweltministerium](https://www.bundesumweltministerium.de/themen/kreislaufwirtschaft/statistiken/verpackungsabfaelle/aufkommen-und-recyclingquoten-von-verpackungen)).

Global sieht es härter aus. Die OECD beziffert den Kunststoffabfall auf **353 Millionen Tonnen** im Jahr 2019 — doppelt so viel wie im Jahr 2000 — und stellt fest: nur **9 Prozent** werden recycelt. 15 Prozent werden überhaupt zum Recycling gesammelt, und von diesem Anteil landen wiederum 40 Prozent als Reste in der Verbrennung oder auf der Deponie ([OECD, 2022](https://www.oecd.org/en/about/news/press-releases/2022/02/plastic-pollution-is-growing-relentlessly-as-waste-management-and-recycling-fall-short.html)).

Es gibt also zwei Müllberge: den, der nie getrennt wurde, und den, der getrennt werden sollte und es nicht wird. Beide sind Sortierprobleme.

## Warum Sortieren so schwer ist

Man könnte denken, Sortieren sei gelöst — schließlich gibt es {{NIR-Sensor}}en, Magnetabscheider und {{Wirbelstromabscheider}}. In der Praxis scheitert es an vier Dingen:

**Erstens: die Oberfläche.** Nahinfrarot erkennt Kunststoffsorten am zurückgeworfenen Licht — aber nur an der Oberfläche. Etiketten und Sleeves verfälschen das Ergebnis. Schwarz eingefärbter Kunststoff enthält **0,5 bis 3 Masseprozent Ruß**; das reicht, um die übliche Nahinfrarot-Erkennung unbrauchbar zu machen, weshalb Forschende auf den mittleren Infrarotbereich ausweichen ([Übersichtsarbeit, 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6418689/)).

**Zweitens: die {{Verbundmaterial}}ien.** Chipstüte und Getränkekarton bestehen aus mehreren Materialschichten, die fest verklebt sind. Das Fraunhofer-Institut für Verfahrenstechnik und Verpackung (IVV) schreibt es offen hin: Mehrschichtverpackungen waren „bislang nicht recycelbar“ ([Fraunhofer IVV](https://www.ivv.fraunhofer.de/en/recycling-environment/recycling-multilayer.html)). Solche Ware fliegt aussortiert in die Verbrennung.

**Drittens: der Dreck.** Nasse Folie, verschmutzte Becher, Kleinteile unter fünf Zentimetern — alles Feinde der Erkennung und der Reinheit der sortierten Fraktion.

**Viertens: der Mensch am Band.** Die Nachsortierung macht bis heute Handarbeit. Das ist eintönig, körperlich belastend und gefährlich: spitze Gegenstände, aber auch Akkus, die in Sortieranlagen Brände auslösen.

Kurz: Müll ist kein Material, sondern ein Gemisch aus unbekannten, verformten, verdreckten Objekten. Genau darin liegt die Schwierigkeit.

## Was heute schon läuft — und was es nicht kann

Maschinelle Sortierung ist Realität, nicht Zukunftsmusik. Der Fast Picker 4.0 von ZenRobotics schafft laut [Datenblatt](https://www.terex.com/docs/zenroboticslibraries/brochures/Fast-Picker.pdf) **bis zu 80 Griffe pro Minute** und lässt sich platzsparend mehrfach über einem Band installieren. Optische Sortierer arbeiten mit Druckluft und schießen erkannte Objekte aus dem Strom. In China bewirbt der Anbieter QKM zusammen mit Gongye Technology eine Anlage namens PiCKiNG·Ai, die laut eigener Beschreibung „gemischte, gestapelte, dichte und gefährliche Abfälle“ mit hoher Treffsicherheit sortieren soll ([QKM](https://www.qkmtech.com/en/case-detail/470.html)) — eine Herstellerangabe, die sich ohne unabhängige Messung nicht überprüfen lässt.

Und doch verraten alle diese Anlagen durch ihre Bauform, wo ihre Grenze liegt: **Sie stehen.** Sie sind über einem Förderband verschraubt, sie brauchen vereinzeltes, einlagiges Material im gleichmäßigen Fluss, und sie greifen, was ihnen auf einer definierten Bahn vorbeikommt. Ein Haufen ist kein Fall für sie. Steht der Abfall in einer Wand aus gepressten Folienballen, einer Böschung auf einer Deponie oder in einem Container voller gemischter Gewerbeabfälle, ist die Technik am Ende.

Genau hier liegt meine These: **Der Müllberg ist die ehrlichere Aufgabe für einen Roboter mit Beinen und Händen als jede Fabrikhalle.**

## Was humanoide Roboter heute wirklich leisten

Man muss dabei ehrlich bleiben — auch gegenüber der eigenen Idee. Der Stand der Technik ist der einer Fabrikhalle, nicht einer Halde.

Beim Autobauer BMW lief Figure 02 nach Angaben des Herstellers über **1.250 Stunden** und setzte **90.000 Teile** ([Figure](https://www.figure.ai/news/production-at-bmw)). Agility Robotics meldet für seinen Roboter Digit **mehr als 100.000 bewegte Kisten** im kommerziellen Einsatz ([Agility Robotics](https://www.agilityrobotics.com/content/digit-moves-over-100k-totes)). Mercedes-Benz testet den Humanoiden Apollo in der Produktion ([Mercedes-Benz](https://group.mercedes-benz.com/company/production/production-network/mbdfc-humanoid-robots.html)). Apollo hebt nach Herstellerangaben **25 Kilogramm** und läuft vier Stunden pro Akkuladung ([Apptronik](https://www.apptronik.com/apollo)), Boston Dynamics' elektrischer Atlas hebt **50 Kilogramm** kurzzeitig und ebenfalls vier Stunden ([Boston Dynamics](https://bostondynamics.com/products/atlas/)).

Beeindruckend — und trotzdem ist der wichtigste Satz über diese Branche ein nüchterner: Das schwierige Problem ist die Manipulation, also das wiederholte Greifen, Wenden und Sortieren von Objekten, ohne an Genauigkeit zu verlieren. Das sagt nicht ein Kritiker, sondern die staatliche chinesische Nachrichtenagentur Xinhua, deren Land die Fertigung von Humanoiden forciert: Sie beschreibt das Jahr 2026 als den Beginn der Serienfertigung und nennt genau das Greifen als Kerntest der Branche ([Xinhua, 24.07.2026](https://english.news.cn/20260724/b9c5a91b473c445bbd9a0c2de28a5493/c.html)). Flexible, rutschige Materialien — Stoff, Folie, Tüte — bleiben besonders schwierig: zu viel Kraft verformt sie, zu wenig lässt sie durchrutschen.

Die Forschung weiß das seit Jahren. Das MIT stellte 2019 mit „RoCycle“ eine Hand vor, die Materialien über Tastsensoren an den Fingerspitzen erkennt — {{Reinforcement Learning}} und {{Sim-to-Real}} hin oder her: Die Trefferquote lag **stationär bei 85 Prozent, auf einem simulierten Förderband nur noch bei 63 Prozent** ([MIT News](https://news.mit.edu/2019/mit-robots-can-sort-recycling-0416)). Sechs Jahre später ist daraus kein Serienprodukt geworden. Und wenn das Greifen schon auf einem sauberen Band schwerfällt, ahnt man, wie es in einem nassen Haufen aussieht.

## Die Idee, zu Ende gedacht

Warum also ausgerechnet Müllberge? Weil die Anforderungen dort mit den Stärken eines Humanoiden zusammenfallen — wenn man die Aufgabe richtig schneidet:

1. **Es gibt keine Anlage, also gibt es keinen Band-Zwang.** Auf einer offenen Kippe existiert keine Infrastruktur, die man nachrüsten müsste. Ein Roboter auf Beinen braucht keinen Stahlbau, kein Rüttelband, kein Fördergerüst.
2. **Die Arbeit ist gefährlich, und zwar für Menschen.** Offene Ablagerungen brennen, entgasen Methan, enthalten spitze und infektiöse Abfälle. Das ist die Art Arbeit, bei der Automatisierung nicht „Jobs klauen“ heißt, sondern „Körper raushalten“.
3. **Der Wertstoff liegt schon da.** Jede Tonne, die an der Halde sortiert wird, muss nicht erst transportiert, umgeschlagen und in einer Anlage verarbeitet werden. Bei Deponiebergbau — dem gezielten Zurückholen von Wertstoffen aus alten Ablagerungen — ist das seit Jahren ein Thema.
4. **Beine statt Schienen.** Ein Humanoide kann an der Böschung entlanglaufen, in einen Container steigen, vor einer Wand aus Ballen stehen. Er kann dort hinfassen, wo die {{Greifpunkt}}e unvorhersehbar sind.

Und jetzt der Haken, in derselben Reihenfolge:

- **Der Haufen ist der feindlichste Arbeitsplatz, den man sich denken kann.** Staub setzt Sensoren zu, Nässe und Hitze setzen Dichtungen zu, die Griffigkeit von Folie und Glas ist erbärmlich. Was in der Fabrikhalle 1.250 Stunden hält, ist in einem Müllhaufen eine offene Frage.
- **Vier bis fünf Stunden Akku** sind für eine Schicht zu wenig — und auf einer Kippe gibt es keine Ladeinfrastruktur.
- **Kein einziger humanoider Roboter arbeitet heute in der Abfallsortierung.** Es gibt Pilotprojekte, es gibt Forschung (auch in Europa), aber marktverfügbar ist das nicht. Wer das Gegenteil behauptet, verkauft eine Demo.
- **Die Kostenrechnung ist offen.** Belastbare Stundensätze für humanoide Arbeit veröffentlicht kaum jemand; die viel zitierte Zahl von rund 25 Dollar pro Roboterstunde bei BMW stammt aus einer Drittanalyse und ist von BMW und Figure nicht bestätigt.
- **Und die politische Frage.** Nach einer Schätzung der Internationalen Arbeitsorganisation leben weltweit **fast 20 Millionen Menschen** vom Sammeln und Verwerten von Abfällen ([WIEGO mit ILO-Zahlen](https://wiego.org/project/waste-pickers-and-human-rights)); Studien zeigen, dass sie einen erheblichen Teil des Kunststoffs überhaupt erst in den Kreislauf bringen. In Entwicklungs- und Schwellenländern wären Roboter auf den Halden zuerst eine Konkurrenz für die Ärmsten — nicht für die Verursacher des Mülls.

## Was zuerst passieren müsste

Wenn die Idee etwas taugen soll, dann nicht als Sprung auf die offene Kippe, sondern in drei Stufen, die technisch aufeinander aufbauen:

**Stufe 1 — aus dem Haufen greifen.** Der ehrlichste erste Schritt ist nicht der Humanoide, sondern der fest montierte Arm, der aus einem gepackten Haufen greift statt von einem Band. Dass Anbieter das inzwischen als Produktversprechen formulieren — gemischt, gestapelt, dicht — zeigt, wo der Bedarf liegt. Wer hier robuste Griffe aus ungeordnetem Material lernt, hat den harten Teil gelöst.

**Stufe 2 — halb autonom auf kontrollierten Halden.** Deponiebergbau und Altanlagen sind der Zwischenschritt: Strom vorhanden, Fläche abgesperrt, Gefahr trotzdem real. Hier ließe sich zeigen, ob ein Humanoide eine Schicht durchhält, und zwar mit einem Menschen in der Ferne, der eingreift, wenn es klemmt — {{Teleoperation}} als Rückfallebene, nicht als Geschäftsmodell.

**Stufe 3 — der Humanoide als Werkzeug für unwegsame Halden.** Erst wenn Greifen, Robustheit und Akkulaufzeit stimmen, ist der beinlose Roboterarm der limitierende Faktor und der Humanoide die logische Antwort. Vorher ist er eine teure Lösung für ein Problem, das noch niemand zu Ende formuliert hat.

## Fazit

Ich halte die These für tragfähig, aber nicht als PR-Idee — als Forschungsauftrag. Der Müllberg ist die eine Aufgabe, bei der der Aufwand für humanoide Roboter nicht aus Bequemlichkeit entsteht, sondern aus Notwendigkeit: Es gibt keine bestehende Anlage, die man nachrüsten könnte, und es gibt keine Menschen, denen man diese Arbeit guten Gewissens weiterhin zumutet. Die Fabrikhalle ist der einfache Testfall; der Abfallhaufen ist die Prüfung, die eine ganze Branche noch bestehen muss. Für die Sortierung spricht außerdem ein politischer Rückenwind: Die EU-Verpackungsverordnung PPWR ist seit dem 12. August 2026 anwendbar und verlangt mehr Recyclingfähigkeit und höhere Rezyklatanteile ([Überblick IHK](https://www.ihk.de/duesseldorf/innovation-umwelt-energie/umwelt/abfall2/die-europaeische-verpackungsverordnung-2025-ppwr--6459764)) — was nur funktioniert, wenn sich Müll überhaupt sauber trennen lässt.

Wem das zu technisch klingt, dem sei ein Satz des MIT aus der RoCycle-Studie mitgegeben: Computer-Vision allein reiche nicht, um Maschinen menschenähnliche Wahrnehmung zu geben. Genau deshalb ist der Müllberg der bessere Test als jede Fabrikhalle. Dort lässt sich nichts bescheißen, weil nichts gerade liegt.

## Quellen

- Weltbank, *What a Waste 2.0* (2018): 2,01 Mrd. t, ≥33 % nicht umweltgerecht, 3,4 Mrd. t bis 2050 (+70 %) — [PDF](https://thedocs.worldbank.org/en/doc/429851552939596362-0200022019/original/WhataWaste2Revisedversion.pdf)
- UNEP, *Global Waste Management Outlook 2024*: 2,3 → 3,8 Mrd. t, Kosten 252/361 → 640,3 Mrd. USD — [Pressemitteilung](https://www.unep.org/news-and-stories/press-release/world-must-move-beyond-waste-era-and-turn-rubbish-resource-un-report)
- OECD, *Global Plastics Outlook* (2022): 353 Mio. t Kunststoffabfall, 9 % recycelt — [Pressemitteilung](https://www.oecd.org/en/about/news/press-releases/2022/02/plastic-pollution-is-growing-relentlessly-as-waste-management-and-recycling-fall-short.html)
- Umweltbundesamt/Bundesumweltministerium (2020): Restmüllzusammensetzung, 32/39/27 Prozent — [Pressemitteilung](https://www.umweltbundesamt.de/presse/pressemitteilungen/deutschlands-restmuell-hat-sich-in-35-jahren-fast)
- Bundesumweltministerium, Verpackungsstatistik 2023: Recyclingquoten — [Tabelle](https://www.bundesumweltministerium.de/themen/kreislaufwirtschaft/statistiken/verpackungsabfaelle/aufkommen-und-recyclingquoten-von-verpackungen)
- Fraunhofer IVV: Mehrschichtverpackungen bislang nicht recycelbar — [Projektseite](https://www.ivv.fraunhofer.de/en/recycling-environment/recycling-multilayer.html)
- Übersichtsarbeit zu schwarzen Kunststoffen und Infrarot-Spektroskopie (2019) — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6418689/)
- ZenRobotics/Terex, Fast-Picker-Datenblatt — [PDF](https://www.terex.com/docs/zenroboticslibraries/brochures/Fast-Picker.pdf)
- QKM/Gongye Technology, PiCKiNG·Ai (Herstellerangabe) — [Anwendungsseite](https://www.qkmtech.com/en/case-detail/470.html)
- Xinhua (24.07.2026): Stand und Kernproblem der Humanoiden-Branche — [Artikel](https://english.news.cn/20260724/b9c5a91b473c445bbd9a0c2de28a5493/c.html)
- MIT News (2019): RoCycle, 85 % / 63 % Trefferquote — [Artikel](https://news.mit.edu/2019/mit-robots-can-sort-recycling-0416)
- Figure: Figure 02 bei BMW, 1.250+ Stunden, 90.000+ Teile — [Meldung](https://www.figure.ai/news/production-at-bmw)
- Agility Robotics: 100.000+ bewegte Kisten — [Meldung](https://www.agilityrobotics.com/content/digit-moves-over-100k-totes)
- Apptronik Apollo: 25 kg Nutzlast, 4 h Laufzeit — [Produktseite](https://www.apptronik.com/apollo)
- Boston Dynamics Atlas: 50 kg kurzzeitig, 4 h Laufzeit — [Produktseite](https://bostondynamics.com/products/atlas/)
- Mercedes-Benz: Test von Apollo in der Produktion — [Seite](https://group.mercedes-benz.com/company/production/production-network/mbdfc-humanoid-robots.html)
- WIEGO mit ILO-Schätzung: fast 20 Millionen Menschen leben vom Verwerten von Abfällen — [Projektseite](https://wiego.org/project/waste-pickers-and-human-rights)
- IHK Düsseldorf: PPWR seit 12.08.2026 anwendbar — [Übersicht](https://www.ihk.de/duesseldorf/innovation-umwelt-energie/umwelt/abfall2/die-europaeische-verpackungsverordnung-2025-ppwr--6459764)
