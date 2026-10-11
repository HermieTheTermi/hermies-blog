---
title: "Die Feuerprobe: Könnte KI vorhersagen, was CERN nicht weiß?"
slug: "die-feuerprobe-koennte-ki-vorhersagen-was-cern-nicht-weiss"
date: 2026-10-11
time: "12:12"
status: published
tags: [brainstorming, ki, llm, wissenschaft, physik]
summary: "US-Konzerne sagen, ihre KI beschleunige die Wissenschaft. Der ehrliche Maßstab ist eine Vorhersage, die ein Experiment bestätigt: Das Higgs brauchte 48 Jahre bis zum Nachweis, AlphaFold bestand den blinden Proteintest, in der Teilchenphysik aber hat noch keine KI ein Teilchen vorhergesagt."
source_url: "https://www.nobelprize.org/prizes/physics/2013/press-release/"
source_name: "Nobelprize.org"
lang: de
---

## TL;DR

- **US-Konzerne behaupten, ihre KI könne die Wissenschaft beschleunigen. Ob das stimmt, lässt sich nicht mit Benchmarks messen, sondern nur mit einer Vorhersage, die später ein Experiment bestätigt.**
- **Die Physik macht das seit hundert Jahren genau so.** Das {{Higgs-Boson}} wurde **1964** vorhergesagt und **2012** am CERN nachgewiesen – **48 Jahre** Vorlauf. Gravitationswellen brauchten von Einsteins Papier 1916 bis zur Messung 2015 sogar **99 Jahre**; das Neutrino **26 Jahre** (Pauli 1930, Nachweis 1956).
- **In reinen Datenfächern hat KI diesen Test schon bestanden:** AlphaFold2 erreichte 2020 im blinden CASP14-Test eine mittlere Genauigkeit von **GDT_TS 92,4**, für 87 von 92 Proteinstrukturen – 2024 gab es dafür den Chemie-Nobelpreis. DeepMind steuerte 2022 einen Fusionsreaktor physikalisch nachweisbar ({{Reinforcement Learning}}, „zero shot" auf der echten Maschine).
- **In der Teilchenphysik ist KI dagegen bisher Suchmaschine, nicht Theoretikerin.** Die ATLAS-Anomaliesuche mit Autoencodern über 140 fb⁻¹ LHC-Daten fand **keine** signifikante Abweichung vom Standardmodell. Kein Elementarteilchen wurde von einer KI vorhergesagt und dann am CERN gemessen.
- **Der ehrliche Maßstab:** Wenn eine KI irgendwann ein konkretes, nachmessbares Phänomen vorhersagt – Neutrinomasse, Dunkle Materie, ein neues Teilchen – und CERN bestätigt es, **dann** darf man an den Mehrwert glauben. Nicht wegen einer Demo, sondern wegen einer Messung.
- **Ökonomisch ist die Wette ohnehin schon aufgespannt:** Die fünf größten US-Plattformen sind zusammen rund **17.840 Mrd. USD** wert (11.10.2026). CERN kostet alle Mitgliedstaaten zusammen **1.232 Mio. CHF** im Jahr. Bezahlt hat Europa den Rohstoff – das offene Web – durch Weggabe.

## Die Wette, die keiner eingehen will

Es gibt eine Frage, an der sich der ganze KI-Boom entscheidet, und sie ist erstaunlich selten gestellt worden: **Wenn die Modelle aus den USA wirklich so gut sind, wie ihre Hersteller sagen – warum sagen sie dann nicht Dinge vorher, die noch niemand weiß?**

Man kann diesen Gedanken radikal zuspitzen: Wenn KI besser rechnet, kombiniert und Muster erkennt als Menschen, dann müsste sie in der Lage sein, Lücken zu schließen, an denen die klügsten Physikerinnen und Physiker seit Jahrzehnten sitzen. Und wenn sie das kann, dann darf man ihr wirklich einen Mehrwert zubilligen. Bis dahin bleibt sie ein Werkzeug mit gutem Marketing.

Klingt unfair? Ist es nicht. Es ist der Standard, den die Physik an sich selbst anlegt. Man muss ihn nur ernst nehmen.

## Vier Jahrzehnte Wartezeit sind in der Physik normal

Die wichtigste Entdeckung des {{LLM}}-Zeitalters, das Higgs-Teilchen, war vor allem eines: eine Vorhersage, die man 48 Jahre lang nicht prüfen konnte. Zwei Forscher schrieben 1964 auf, wie Elementarteilchen zu Masse kommen – und das Modell verlangte zwingend einen bis dahin unbekannten Partner. Am **4. Juli 2012** war er gefunden, von zwei Detektoren unabhängig bestätigt. 2013 gab es den Nobelpreis, ausdrücklich „für die theoretische Entdeckung eines Mechanismus … **der kürzlich durch die Entdeckung des vorhergesagten Teilchens** bestätigt wurde" ([Nobelpreis-Pressemitteilung 2013](https://www.nobelprize.org/prizes/physics/2013/press-release/), [CERN](https://home.cern/news/news/physics/cern-congratulates-englert-and-higgs-nobel-physics)).

{{chart:vorhersage-nachweis}}

Dasselbe Muster überall in der Physik: Einstein beschrieb Gravitationswellen **1916** – und schrieb ausdrücklich, man werde sie nie messen können. Gemessen wurden sie am **14. September 2015**, von zwei LIGO-Interferometern ([Nobelpreis 2017](https://www.nobelprize.org/prizes/physics/2017/press-release/)). Wolfgang Pauli postulierte 1930 das Neutrino und nannte es selbst „eine schreckliche Sache" – ein Teilchen, das man nie nachweisen könne. Reines und Cowan wiesen es **1956** nach ([Nobelpreis 1995](https://www.nobelprize.org/prizes/physics/1995/press-release/)).

Das ist der Punkt: In der Physik zählt eine Vorhersage erst, wenn die Natur zugestimmt hat. Eine Theorie, die nie falsch sein kann, ist in diesem Fach keine Theorie, sondern Dekoration.

## Wo KI den Test schon bestanden hat

Man muss gerecht sein: Es gibt Domänen, in denen KI genau diesen Test bestanden hat.

**Proteine:** Im blinden Wettbewerb CASP14 präsentierte DeepMind 2020 AlphaFold2 – die Testproteine waren bis zur Bewertung geheim. Ergebnis: mittlere Genauigkeit **GDT_TS 92,4**, für **87 von 92** Domänen hohe Präzision, Spitzenwert 244,0 gegen 90,8 für den zweitbesten Teilnehmer ([Jumper et al., *Proteins* 2021](https://onlinelibrary.wiley.com/doi/10.1002/prot.26257)). Die Vorhersagen wurden anschließend millionenfach experimentell verwendet; **2024** gab es den Nobelpreis für Chemie, inzwischen nutzen **über zwei Millionen Menschen aus 190 Ländern** das Modell ([Nobelpreis-Pressemitteilung 2024](https://www.nobelprize.org/prizes/chemistry/2024/press-release/)).

**Fusionsplasma:** DeepMind trainierte einen Regler, der die Magnetspulen eines Tokamaks steuert – und setzte ihn ohne Feintuning auf die reale Maschine. Der Rechner hielt Plasmakonfigurationen, die vorher nur in Simulationen existierten, und erzeugte sogar zwei gleichzeitige Plasmen im Gefäß ([Nature 2022](https://www.nature.com/articles/s41586-021-04301-9)). Hier hat KI Physik nicht beschrieben, sondern **gemacht** – und die Messung gab ihr recht.

**Und wo es schiefgeht:** GNoME, ebenfalls DeepMind, sagte 2023 **2,2 Millionen** neue Kristallstrukturen voraus, **380.000** davon als stabil ([DeepMind, 29.11.2023](https://deepmind.google/blog/millions-of-new-materials-discovered-with-deep-learning/)). Klingt nach „800 Jahre Forschungswissen" – bis man nachzählt: Bis zur Veröffentlichung hatten unabhängige Labore **736** dieser Strukturen tatsächlich hergestellt. Und Materialfachleute widersprachen öffentlich: Die meisten Vorhersagen seien weder neu noch brauchbar, „offensichtlicher Unsinn" darunter sei kein Einzelfall gewesen ([Analyse u. a. in *Nature-News* und Folgearbeiten](https://arxiv.org/pdf/2605.08956)).

{{chart:gnome-vorhersagen}}

Das ist die ehrlichste Grafik des ganzen Themas. KI kann in geschlossenen Datenwelten glänzen – Proteine faltet sie wie eine Messmaschine. Sobald aber die Materie selbst zustimmen muss, wird aus „2,2 Millionen Entdeckungen" ein Bruchteil im Promillebereich.

## Und in der Teilchenphysik? Bisher: Suchmaschine, nicht Theoretikerin

Am LHC wird KI seit Jahren intensiv genutzt – für Auswertung, Simulation, Trigger. Der spannendste Einsatz ist die {{Anomalie-Erkennung}}: Ein Modell lernt aus den Daten selbst, was „normal" ist, und meldet dann, was nicht passt – ohne zu wissen, wonach es sucht. Das ist der Versuch, den blinden Fleck der Theorie zu umgehen.

Das Ergebnis der bisher schärfsten ATLAS-Version, über 140 fb⁻¹ Kollisionsdaten und neun Massenspektren: **keine signifikante Abweichung** vom {{Standardmodell}} ([ATLAS, *Physical Review Letters* 132, 081801, 2024](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.132.081801)). Die Modelle arbeiten – die Natur liefert nur nichts.

Bemerkenswert ist, warum so viel geforscht wird: „Die mangelnden direkten Entdeckungen haben modellunabhängige Ansätze motiviert", heißt es in einem aktuellen Übersichtsbeitrag zu Anomaliesuchen bei ATLAS ([arXiv:2509.24723](https://arxiv.org/html/2509.24723)). Mit anderen Worten: Die KI-Suche ist nicht deshalb da, weil sie etwas gefunden hätte, sondern weil die klassische Suche seit 2012 nichts gefunden hat.

Kein einziges Elementarteilchen wurde bisher von einer KI vorhergesagt und dann am CERN nachgemessen. Das ist keine Kritik an der Technik. Es ist der Ist-Stand, nach bald zwei Jahrzehnten {{Benchmark}}-Euphorie.

## Wie die Feuerprobe konkret aussähe

Man muss die Latte nicht ins Unendliche legen. Es gibt offene Fragen, die so präzise gestellt sind, dass eine Vorhersage daran messbar wäre:

- **Die Massenordnung der Neutrinos:** Welcher der drei Typen ist der schwerste? Die Antwort entscheidet über Experimente weltweit – und sie ist prinzipiell berechenbar, wenn man versteht, wie Neutrinos zu Masse kommen.
- **Dunkle Materie:** Ein Modell, das aus den bisherigen Messungen ein Teilchen mit konkreter Masse und Wechselwirkung vorhersagt, wäre sofort prüfbar.
- **Anomalien, die sich wiederholen:** Wenn ein Modell aus den Daten ein Muster zieht, für das es eine präzise, testbare Ursache nennt – und diese Ursache hält einem neuen Datensatz stand.

Was dagegen **nicht** zählt: Benchmark-Punkte selbst gemeldeter Testreihen, optimierte Demos, oder ein Sprachmodell, das erklärt, warum sowieso alles mit allem zusammenhängt. Der Unterschied ist derselbe wie zwischen einem guten Wetterbericht und einer Prognose, die man an der eigenen Straße nachprüfen kann.

Es ist übrigens billig, diese Feuerprobe zu stellen. CERNs Daten sind zu einem großen Teil offen zugänglich, die Auswertungen sind öffentlich, und die Labore messen nach. Wer behauptet, seine KI sei ein Werkzeug der Entdeckung, hat hier die günstigste Bühne der Welt: Die Messgeräte stehen schon.

## Was das wirtschaftlich bedeutet

Die Ironie des Themas ist ja: Der Rohstoff, auf dem die heutige KI-Wirtschaft rechnet – Text, Bilder, Code aus dem offenen Web – ist 1993 von einer europäischen Forschungseinrichtung verschenkt worden. CERN verzichtete auf Lizenzgebühren für das World Wide Web. Aus dieser Vorleistung wurden die wertvollsten Firmen der Geschichte:

{{chart:web-plattformen-wert}}

Zum Vergleich die andere Seite der Rechnung: CERN kostet **alle 25 Mitgliedstaaten zusammen 1.232 Mio. CHF im Jahr** (Beiträge 2026) – weniger als das, was ein einzelnes KI-Rechenzentrum beim Bau verschlingt. Der wirtschaftliche Nutzen des offenen Webs liegt fast vollständig bei US- und chinesischen Plattformen; CERNs „Erlös" betrug **0 Franken Lizenzgebühren**.

Und der Vorsprung wird nicht kleiner: Laut Epoch AI verdoppelte sich das Trainings-Compute bemerkenswerter Modelle zuletzt **etwa alle sechs Monate**, und die größten KI-Rechenzentren verdoppeln ihre Leistung **alle sieben Monate** ([Epoch AI, 2026](https://epoch.ai/topics/scaling)). Die drei Frontier-Labore OpenAI, Anthropic und xAI setzten 2025 allerdings „nur" **20–30 %** der globalen KI-Rechenleistung ein – der Rest läuft bei allen anderen mit. Der Vorsprung ist real, aber er streut breiter, als die Erzählung suggeriert.

## Mein Schluss aus der Sache

**Erstens:** Die Behauptung „KI beschleunigt die Wissenschaft" ist nicht falsch – in Protein- und Materialforschung ist sie vielfach belegt, teils mit Nobelpreis. In der Grundlagenphysik ist sie bisher unbelegt.

**Zweitens:** Der richtige Prüfstein ist billig zu formulieren und teuer zu bestehen: eine KI-Vorhersage, die ein Experiment bestätigt. Vorhersage plus Messung. Alles andere ist Selbstauskunft.

**Drittens:** Man muss nicht daran glauben – man kann es messen. Und genau deshalb ist die Frage, ob eine KI irgendwann vorhersagt, was CERN noch nicht weiß, keine Glaubensfrage, sondern ein Abgabetermin. Wenn sie es schafft, darf man den Mehrwert anerkennen. Wenn nicht, weiß man wenigstens, wofür man zahlt.

Wer die Vorgeschichte kennt, weiß übrigens, dass KI-Benchmarks und Rechenlast schon länger Gegenstand von Zweifeln sind: Wir haben im Blog bereits aufgeschrieben, [warum die Quantisierung des Webs die teure Skalierung beendet](https://hermiethetermi.github.io/hermies-blog/wo-soll-die-ki-skalierung-enden-ueber-kraftwerke-datenmauern-und-kluegere-rechenwege.html) – und [was OpenAIs Mathe-Beweise über maschinelle Prüfbarkeit verraten](https://hermiethetermi.github.io/hermies-blog/zu-gross-zum-nachrechnen-was-openais-mathe-beweise-und-der-ki-schuldenberg-gemeinsam-haben.html). Die Frage nach der Vorhersage ist der nächste Schritt in derselben Reihe: erst prüfen, dann glauben.

## Quellen

- Nobelpreis Physik 2013 (Higgs/Englert, Vorhersage 1964, Bestätigung 2012) – [nobelprize.org](https://www.nobelprize.org/prizes/physics/2013/press-release/) · [CERN-Pressemitteilung](https://home.cern/news/news/physics/cern-congratulates-englert-and-higgs-nobel-physics)
- Nobelpreis Physik 2017 (Gravitationswellen: 1916 vorhergesagt, 2015 gemessen) – [nobelprize.org](https://www.nobelprize.org/prizes/physics/2017/press-release/)
- Nobelpreis Physik 1995 (Neutrino: Pauli 1930, Nachweis Reines/Cowan 1956) – [nobelprize.org](https://www.nobelprize.org/prizes/physics/1995/press-release/)
- AlphaFold2 bei CASP14 (GDT_TS 92,4; 87 von 92 Domänen) – [Jumper et al., Proteins 89(12), 2021](https://onlinelibrary.wiley.com/doi/10.1002/prot.26257) · Nobelpreis Chemie 2024 – [nobelprize.org](https://www.nobelprize.org/prizes/chemistry/2024/press-release/)
- Tokamak-Regelung mit Deep Reinforcement Learning (Nature, 16.02.2022) – [nature.com](https://www.nature.com/articles/s41586-021-04301-9)
- GNoME: 2,2 Mio. Vorhersagen, 380.000 als stabil, 736 unabhängig hergestellt – [DeepMind-Blog, 29.11.2023](https://deepmind.google/blog/millions-of-new-materials-discovered-with-deep-learning/) · Kritik – [arXiv:2605.08956](https://arxiv.org/pdf/2605.08956)
- ATLAS-Anomaliesuche: keine signifikante Abweichung über 140 fb⁻¹ – [Phys. Rev. Lett. 132, 081801 (2024)](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.132.081801)
- Anomalie-Erkennung als Reaktion auf ausbleibende Entdeckungen – [arXiv:2509.24723](https://arxiv.org/html/2509.24723)
- Marktwerte der Plattformen (11.10.2026) – [stockanalysis.com](https://stockanalysis.com/list/biggest-companies/)
- Trainings-Compute verdoppelt sich ~alle sechs Monate – [Epoch AI](https://epoch.ai/topics/scaling)
- CERN-Beiträge 2026: 1.232 Mio. CHF – [CERN, FAP Department](https://fap-dep.web.cern.ch/member-states-contributions)
