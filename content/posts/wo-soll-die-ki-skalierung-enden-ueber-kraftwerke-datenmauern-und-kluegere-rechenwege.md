---
title: "Wo soll die KI-Skalierung enden? Über Kraftwerke, Datenmauern und klügere Rechenwege"
slug: "wo-soll-die-ki-skalierung-enden-ueber-kraftwerke-datenmauern-und-kluegere-rechenwege"
date: 2026-10-04
status: published
tags: [brainstorming, ki, llm, agenten, energie]
summary: "Rechenzentren brauchten 2024 rund 415 TWh Strom, bis 2030 sollen es 945 TWh sein – und trotzdem fällt der Strom pro Anfrage um mehr als eine Größenordnung pro Jahr. Warum die Rechnung nicht sinkt und welche Techniken KI schlanker machen: Mixture-of-Experts, Quantisierung, Destillation, Testzeit-Compute und Agenten-Methoden."
lang: de
---

## TL;DR

- **Die Stromrechnung der KI wächst schneller als alles andere in der Energiebranche.** Rechenzentren brauchten 2024 rund **415 TWh** – etwa **1,5 % des Weltstromverbrauchs**. Die Internationale Energieagentur (IEA) erwartet für 2030 rund **945 TWh**, mehr als Japan heute insgesamt verbraucht. KI-fokussierte Rechenzentren legten 2025 um **50 %** zu.
- **Pro Anfrage wird KI gleichzeitig dramatisch sparsamer.** Google misst für einen Gemini-Textprompt im Median **0,24 Wh** – **33-mal weniger** als zwölf Monate zuvor. Die IEA nennt das Tempo „beispiellos in der Energiegeschichte".
- **Trotzdem sinkt die Rechnung nicht.** Was pro Anfrage billiger wird, wird häufiger genutzt. Der Gesamtverbrauch steigt weiter – der klassische Rebound-Effekt.
- **Die alte Wachstumsachse stößt an Grenzen.** Der hochwertige Text im Netz ist laut Epoch AI schon zwischen 2023 und 2025 abgeerntet, das Rechen-Wachstum der Spitzenmodelle hat sich seit 2018 auf etwa **4× pro Jahr** verlangsamt.
- **Die neue Achse heißt Rechenzeit pro Antwort und schlankere Architektur.** DeepSeek-V3 hält **671 Mrd. Parameter** bereit, rechnet aber pro Token nur **37 Mrd.** – rund 5,5 %. Ein Qwen3-Modell mit 4 Mrd. Parametern soll laut Hersteller ein 72-Mrd.-Modell von 2024 erreichen.
- **Agenten verschieben die Intelligenz in den Ablauf:** Werkzeuge, Prüfschritte und mehrere Versuche heben kleine Modelle auf das Niveau großer. Das kostet aber Rechenzeit – ein Multi-Agenten-Recherchesystem verbraucht etwa **15× so viele Token** wie ein normaler Chat.

**Der Kern in einem Satz:** Es endet nicht die Skalierung, es endet ihre billige Variante.

## Was gerade passiert: 415 TWh, ein Kraftwerksstau und zwei Atomdeals

Beginnen wir mit der Zahl, die den Streit befeuert: Ein {{Rechenzentrum}} ist heute ein Kraftwerkskunde. Laut der IEA-Studie [*Energy and AI*](https://www.iea.org/reports/energy-and-ai/executive-summary) (10. April 2025) entfielen 2024 rund **415 TWh** des weltweiten Stromverbrauchs auf Rechenzentren – etwa **1,5 %**. Bis 2030 soll dieser Wert auf rund **945 TWh** steigen, bis 2035 auf etwa **1.200 TWh**. Im April 2026 hat die Agentur nachgelegt: 2025 lag der Verbrauch schon bei **485 TWh** (+17 % gegenüber dem Vorjahr), und der Anteil der reinen KI-Rechenzentren wuchs um **50 %** ([IEA, *Key Questions on Energy and AI*](https://www.iea.org/news/data-centre-electricity-use-surged-in-2025-even-with-tightening-bottlenecks-driving-a-scramble-for-solutions)).

In den USA ist der Druck am größten. Das Lawrence Berkeley National Laboratory beziffert den Anteil der Rechenzentren am US-Strom für 2023 mit **176 TWh = 4,4 %** und erwartet für 2028 **325 bis 580 TWh**, also **6,7 bis 12 %** ([LBNL-Bericht für das US-Energieministerium](https://eta-publications.lbl.gov/sites/default/files/2024-12/lbnl-2024-united-states-data-center-energy-usage-report.pdf), 20. Dezember 2024). Die Spanne ist so breit, weil niemand weiß, wie viele der angekündigten Anlagen wirklich gebaut werden.

Genau da liegt der eigentliche Engpass: nicht der Strom, sondern der Anschluss. Ein typisches 2024 fertiggestelltes Kraftwerksprojekt wartete **55 Monate** auf den Netzanschluss ([LBNL, *Queued Up*](https://emp.lbl.gov/sites/default/files/2025-12/Queued%20Up%202025%20Edition%20-%2012.15.2025.pdf), Dezember 2025). In Texas stehen laut dem Netzbetreiber ERCOT rund **410 GW** an Großlast-Anfragen in der Warteschlange – etwa **87 % davon Rechenzentren**, ein Zuwachs von 178 GW gegenüber Ende 2025 ([ERCOT, April 2026](https://www.ercot.com/files/docs/2026/04/13/9-Interconnection-and-Grid-Analysis-Update.pdf)). Zum Vergleich: 410 GW ist ungefähr die vierfache Spitzenlast Deutschlands.

Also werden Kraftwerke bestellt, die es noch nicht gibt. Die Auftragsbücher der Turbinenhersteller sind voll: GE Vernova meldete im dritten Quartal 2025 eine Gaskraftwerks-Auftragslage von **62 GW**, Siemens Energy einen Rekord-Auftragsbestand von **138 Mrd. €** ([GE Vernova](https://www.gevernova.com/news/press-releases/ge-vernova-reports-third-quarter-2025-financial), [Siemens Energy](https://assets.siemens-energy.com/dam/8b35c13c-396b-4623-8590-b3950053f94c/6--SE-Press-Release-EN-pdf_Original%20file.pdf), beide Herstellerangaben).

Weil Gas teuer und politisch unruhig ist, kaufen die Konzerne Atomstrom ein, der noch nicht fließt: Microsoft lässt mit Constellation das stillgelegte Kraftwerk Three Mile Island (**~835 MW**) bis **Ende 2027** reaktivieren ([Constellation](https://www.constellationenergy.com/newsroom/2024/Constellation-to-Launch-Crane-Clean-Energy-Center-Restoring-Jobs-and-Carbon-Free-Power-to-The-Grid.html)), Google hat mit Kairos Power einen ersten kleinen Reaktor beauftragt – Baubeginn war der 17. April 2026, bis 2035 sollen **500 MW** entstehen ([Kairos Power](https://www.kairospower.com/updates/kairos-power-breaks-ground-on-hermes-2-demonstration-plant)), Amazon erweitert sein Abkommen mit Talen Energy ([Talen](https://ir.talenenergy.com/node/8671/pdf)). Das sind keine laufenden Kraftwerke, sondern Vorleistungen auf eine Nachfrage, die man erwartet.

Auch Wasser gehört zur Rechnung: Google beziffert den Verbrauch eines Gemini-Textprompts auf **0,26 Milliliter** – etwa fünf Tropfen ([Google](https://cloud.google.com/blog/products/infrastructure/measuring-the-environmental-impact-of-ai-inference), August 2025).

## Die Gegenbewegung: pro Anfrage wird KI rasend schnell sparsamer

Dieselbe Google-Messung zeigt die andere Hälfte des Bildes. Der Median-Prompt kostet **0,24 Wh** Energie, verursacht **0,03 g CO₂e** – und über zwölf Monate sanken Energie- und CO₂-Fußabdruck pro Prompt um **33× bzw. 44×**, bei besserer Antwortqualität. Epoch AI kommt für typische ChatGPT-Anfragen auf ähnliche Größenordnungen (rund **0,3 Wh**, [Epoch AI](https://epoch.ai/gradient-updates/how-much-energy-does-chatgpt-use)).

Die IEA hält das für einen Trend, nicht für einen Ausreißer: Der Energiebedarf **pro einzelner KI-Aufgabe** fällt um mindestens eine Größenordnung pro Jahr – ein Tempo, das die Agentur „beispiellos in der Energiegeschichte" nennt ([IEA](https://www.iea.org/news/data-centre-electricity-use-surged-in-2025-even-with-tightening-bottlenecks-driving-a-scramble-for-solutions)). Eine Microsoft-Arbeit im Fachjournal *Joule* (April 2026) modelliert Frontier-Inferenz und kommt auf einen Median von rund **0,31 Wh** für einfache Anfragen – und **3,91 Wh**, wenn das Modell lange {{Reasoning}}-Ketten rechnet.

Damit ist der Zielkonflikt des ganzen Artikels in einer Zahl: **Der Strom pro Anfrage fällt um Faktor 33, der Strom pro Modellaufruf-Volumen steigt trotzdem.**

## Warum die Sparsamkeit die Rechnung nicht senkt

Der {{Rebound-Effekt}} ist der Grund. Wenn eine Technik effizienter wird, sinkt ihr Preis, und ein niedrigerer Preis erzeugt neue Nachfrage – das ist das Jevons-Paradox, 1865 an der Dampfmaschine beschrieben und in einer FAccT-Studie von 2025 ausdrücklich auf KI übertragen ([arXiv:2501.16548](https://arxiv.org/abs/2501.16548)).

Zu beobachten ist das an den Netzentgelten. Im größten US-Netzverbund PJM hat sich der Preis für gesicherte Leistung in den Auktionen von **28,92 auf 333,44 Dollar pro Megawatt und Tag** vervielfacht – die Auktion von 2025 schlug mit rund **16,4 Mrd. Dollar** zu Buche, und die Netzbetreiber begründen das zum großen Teil mit Rechenzentren. Bezahlt wird das über die Stromrechnung – auch von Haushalten, die nie ein KI-Modell aufgerufen haben. Wer den wahren Preis von KI wissen will, darf nicht den Wahrscheinlichkeits-Prompt betrachten, sondern den Kraftwerkszubau.

Die ehrliche Formulierung lautet also: KI wird pro Aufgabe viel effizienter und in Summe immer teurer. Wer aus Effizienzgewinnen auf sinkenden Gesamtverbrauch schließt, rechnet am Verhalten vorbei.

## Wo die alte Achse endet: Datenmauer und Parameter-Wettrüsten

Die Ursprungsannahme der Branche stammt von 2020: Das {{Skalierungsgesetz}}, formuliert von Kaplan und Kollegen, besagt, dass Modelle mit mehr {{Parameter}}n, mehr Daten und mehr Rechenleistung zuverlässig besser werden ([arXiv:2001.08361](https://arxiv.org/abs/2001.08361)). Der praktische Fehler dabei wurde 2022 korrigiert: Chinchilla zeigte, dass Modellgröße und Datenmenge **gleich** wachsen müssen – auf einen Parameter sollten etwa **20 Token** Trainingsdaten kommen ([arXiv:2203.15556](https://arxiv.org/abs/2203.15556)). GPT-3 mit 175 Mrd. Parametern war deshalb nicht zu groß, sondern zu schlecht gefüttert.

**Das zweite Problem: Der Nachschub an Text ist begrenzt** – in der Branche {{Datenmauer}} genannt. Epoch AI schätzt den Bestand hochwertigen Sprachtextes im Netz und kommt zu dem Ergebnis, dass er zwischen **2023 und 2025** abgeerntet ist; die Vorräte an minderwertigem Text reichen laut derselben Projektion bis in die 2030er ([Epoch AI](https://epoch.ai/publications/will-we-run-out-of-ml-data-evidence-from-projecting-dataset), [arXiv:2211.04325](https://arxiv.org/abs/2211.04325)). Ein größeres Modell braucht mehr Text – der aber wächst nicht mehr.

**Das dritte Problem: Das Tempo lässt nach.** Das Rechenvolumen der größten Modelle wuchs zwischen 2010 und 2024 zwar um **4 bis 5× pro Jahr**, nach 2018 aber merklich langsamer als davor ([Epoch AI](https://epochai.org/blog/training-compute-of-frontier-ai-models-grows-by-4-5x-per-year)). Und die berühmten „Emergenten Fähigkeiten", bei denen Modelle plötzlich etwas können, was sie vorher nicht konnten, halten viele Forscher inzwischen für einen Messartefakt: Bei anderer Bewertungsmetrik verschwindet der Sprung ([Schaeffer et al., NeurIPS 2023](https://arxiv.org/abs/2304.15004)). Die Kurve verläuft also glatter und flacher als die Erzählung vom Schwellenwert.

Deshalb ist die Parameterzahl als Maßstab entwertet: Ein Modell mit Billionen Parametern, von denen pro Token nur ein Bruchteil rechnet, ist nicht „größer" im entscheidenden Sinn.

## Die neue Achse: Rechenzeit beim Antworten statt Größe beim Training

Der Ausweg heißt {{Testzeit-Compute}}: Das Modell rechnet länger an einer einzelnen Antwort. Eine Google-DeepMind-Studie von 2024 zeigte, dass ein kleineres Modell mit zusätzlicher Rechenzeit beim Antworten ein **14-mal größeres** Modell schlagen kann – bei gleichem Rechenbudget ([Snell et al.](https://arxiv.org/abs/2408.03314)). In der Praxis (OpenAI, 2024): GPT-4o löst 12 % der AIME-Matheaufgaben, das Reasoning-Modell o1 kommt auf **74 %** mit einem Versuch, **83 %** mit Abstimmung über 64 Läufe und **93 %** mit Auswahl aus 1.000 Läufen – das Modell bleibt dasselbe, nur die Rechenzeit wächst ([OpenAI](https://openai.com/index/learning-to-reason-with-llms)).

Der Preis dafür ist unangenehm konkret. Beim ARC-AGI-Benchmark erreichte OpenAI o3 **87,5 %** – mit 1.024 Versuchen pro Aufgabe, **172×** dem Rechenaufwand der sparsamen Variante und Kosten von **4.560 Dollar pro gelöster Aufgabe** ([ARC Prize](https://arcprize.org/blog/oai-o3-pub-breakthrough)). Und die Achse läuft nicht monoton: Es gibt Aufgaben, bei denen mehr Nachdenken die Antwort **schlechter** macht ([*Inverse Scaling in Test-Time Compute*](https://arxiv.org/abs/2507.14417), 2025).

Die Verschiebung trifft die Rechnung an einer neuen Stelle: Die Kosten wandern vom einmaligen Training in die **{{Inferenz}}**, also in jeden einzelnen Aufruf. Ein Testzeit-Modell ist billig zu bauen und teuer zu betreiben; ein großes Modell ist teuer zu bauen und billig zu betreiben, wenn die Anfrage kurz ist.

## Schlanker statt größer: was 2023 bis 2026 wirklich passiert ist

Der sichtbarste Fortschritt liegt nicht in neuen Rekorden, sondern im Sparen.

**{{Mixture-of-Experts}}** ist der wichtigste Hebel: Statt alle Gewichte für jedes Token zu nutzen, aktiviert das Modell nur einen Teil. DeepSeek-V3 hält **671 Mrd. {{Parameter}}** bereit, rechnet pro {{Token}} aber nur **37 Mrd.** – rund 5,5 % – und erreichte damit laut eigenem Bericht **88,5 auf dem MMLU-Benchmark** ([arXiv:2412.19437](https://arxiv.org/abs/2412.19437)). Bezahlt wurde das mit 2,79 Mio. GPU-Stunden, umgerechnet rund **5,6 Mio. Dollar** Mietkosten – zwei Größenordnungen unter den Schätzungen für die vorherige Modellgeneration, wobei dieser Vergleich hinkt: DeepSeeks Zahl enthält nur die reine Mietzeit, nicht Forschung, Daten und Fehlversuche.

**{{Quantisierung}}** presst Gewichte in weniger Bits: GPTQ schafft 3–4 Bit bei „vernachlässigbarem" Qualitätsverlust ([arXiv:2210.17323](https://arxiv.org/abs/2210.17323)), AWQ schützt die wichtigsten 1 % der Gewichte und läuft dadurch auf Grafikkarten im Laptop mehr als **3× schneller** ([arXiv:2306.00978](https://arxiv.org/abs/2306.00978)), und AQLM quetscht Llama-2-7B auf **2 Bit** – mit spürbarem Preis: 6,93 statt 5,12 Perplexität ([arXiv:2401.06118](https://arxiv.org/abs/2401.06118)). Bei {{Pruning}}, also dem Beschneiden unnötiger Verbindungen, halbiert man die Gewichte und zahlt mit etwa 1,5 Perplexitäts-Punkten ([SparseGPT](https://arxiv.org/abs/2301.00774)).

**{{Destillation}}** schließlich ist der Trick, Wissen aus einem Riesen in einen Zwerg zu gießen: DeepSeek-R1 (671 Mrd.) erzeugt Lösungswege, aus denen ein 32-Mrd.-Modell lernt – es erreicht auf AIME 72,6 % gegenüber 79,8 % des Lehrers ([arXiv:2501.12948](https://arxiv.org/abs/2501.12948)). Und die Kleinen holen auf: Qwen3 baut sechs dichte Modelle zwischen **0,6 und 32 Mrd. Parametern**, von denen laut Hersteller „selbst ein winziges Qwen3-4B mit Qwen2.5-72B mithalten" kann ([Qwen](https://qwenlm.github.io/blog/qwen3/), Herstellerangabe, Fremdmessungen liegen teils niedriger). Gemma 3 startet bei **270 Mio. Parametern** für Geräte ohne Netz ([Google](https://developers.googleblog.com/en/introducing-gemma-3-270m/)). Die API-Preise fielen im selben Zeitraum um **Faktor 200**: von 30 Dollar pro Million Eingabe-Token (GPT-4, März 2023) auf 0,15 Dollar beim Nachfolger für kleine Aufgaben ([OpenAI](https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/)).

## Agenten: Intelligenz aus dem Ablauf statt aus den Gewichten

Die zweite große Verschiebung betrifft nicht das Modell, sondern das Drumherum. GAIA, ein {{Benchmark}} für mehrstufige Rechercheaufgaben, war für GPT-4 mit Plugins bei **15 %** – Menschen lagen bei **92 %** ([Mialon et al.](https://arxiv.org/abs/2311.12983)). Auf OSWorld, dem Benchmark für Computerbedienung, lagen die besten Modelle bei **12,24 %** gegen **72,36 %** beim Menschen ([Xie et al.](https://arxiv.org/abs/2404.07972)). Diese Lücke ist zu einem großen Teil keine Frage der Modellgröße, sondern der Werkzeuge: Allein eine bessere Schnittstelle hob SWE-agent von 1,96 auf **12,5 %** bei echten GitHub-Problemen ([SWE-bench](https://arxiv.org/abs/2310.06770)), und simples Wiederholen hob ein mittleres Modell auf SWE-bench Lite von 15,9 auf **56 %** ([*Large Language Monkeys*](https://arxiv.org/abs/2407.21787)).

Die Ökonomie dahinter ist belegt: Modell-Kaskaden, die erst das billige und nur bei Zweifel das teure Modell fragen, erreichten GPT-4-Qualität mit **bis zu 98 % weniger Kosten** ([FrugalGPT](https://arxiv.org/abs/2305.05176)); RouteLLM senkte die Kosten um **85 %** bei 95 % der GPT-4-Qualität ([arXiv:2406.18665](https://arxiv.org/abs/2406.18665)). Und Anthropic zeigt, wie sich Leistung verschieben lässt, ohne ein größeres Modell zu trainieren: Ein System aus Leitmodell und mehreren Unteragenten übertraf den Einzelagenten um **90,2 %** – wobei allein die Zahl der verbrauchten Token **80 %** der Leistungsvarianz erklärte. Bezahlt wird das mit Rechenzeit: Ein {{Agent}} verbraucht typisch **4×**, ein Multi-Agenten-System etwa **15×** so viele Token wie ein Chat ([Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system)).

Drei Einschränkungen gehören dazu. Erstens ist {{Scaffolding}} kein Freifahrtschein: Eine Untersuchung von 2025 fand über sieben Agenten-Systeme hinweg Fehlerraten zwischen **41 % und 86,7 %** ([MAST](https://arxiv.org/abs/2503.13657)). Zweitens sind Modelle schlechte Prüfer ihrer selbst – ohne externen {{Verifier}} wird die Antwort nach Selbstkorrektur oft schlechter, nicht besser ([arXiv:2507.14417](https://arxiv.org/abs/2507.14417)-Umfeld und [Huang et al. 2024](https://arxiv.org/abs/2310.01798)). Drittens: In einer Microsoft- und Hugging-Face-Studie von 2026 scheiterte der Großteil der Agentenläufe nicht am Denken, sondern an Werkzeugen und Zustandsfehlern – und **67 %** dieser Fehlschläge sahen nach außen hin „sauber" aus ([ThinkingBox](https://huggingface.co/blog/microsoft/thinkingbox)). Wer Agenten als Effizienz-Wunder verkauft, verschweigt die Rechenzeit, die für Prüfschritte und Wiederholungen draufgeht.

## Was als Nächstes kommt

- **Modell-Architektur:** State-Space-Modelle wie Mamba und hybride Varianten laufen 2026 produktionsreif und brauchen für lange Eingaben weniger Rechenzeit als reine Transformer ([Mamba-3](https://arxiv.org/abs/2502.07864)). Weltmodelle à la JEPA bleiben Forschung.
- **Daten:** Synthetische Daten wandern von der Notlösung zur Werkstatt – erzeugte Aufgaben plus automatische Prüfer, wie im ServiceNow-Ansatz, der Agenten-Aufgaben samt Verifier produziert ([Hugging Face](https://huggingface.co/blog/ServiceNow-AI/autosynthdata)).
- **Hardware:** Google nennt für seine TPU-Generation Ironwood **3,7× bessere Kohlenstoffeffizienz** ([Google Cloud](https://cloud.google.com/blog/topics/systems/ironwood-tpus-deliver-37x-carbon-efficiency-gains)); NVIDIA verspricht für die nächste Generation mehr Token pro Megawatt (Herstellerangabe). Und BitNet zeigt, was mit Gewichten aus nur drei Werten möglich ist: **~7× weniger Speicher** bei nahezu unveränderter Qualität oberhalb von 3 Mrd. Parametern ([arXiv:2402.17764](https://arxiv.org/abs/2402.17764)).
- **Effizienz als Gesetz:** Das „Densing Law" beschreibt die Fähigkeit **pro Parameter** als exponentiell wachsend mit einer Verdopplung etwa alle drei Monate ([Nature Machine Intelligence 2025](https://nature.com/articles/s42256-025-01137-0.pdf)) – eine Aussage über Dichte, nicht über Nutzen.
- **Regulierung:** Die EU-Kommission arbeitet an Pflichtangaben zum Energieverbrauch von KI-Modellen ([Konsultation 2026](https://digital-strategy.ec.europa.eu/en/consultations/targeted-consultation-measuring-energy-consumption-and-emissions-ai-models)), der EU AI Act verlangt solche Angaben für große Modelle bereits. Transparenz ist der billigste Effizienzhebel, den es gibt.

## Was heißt das praktisch?

Drei Regeln, die sich aus dem Material ableiten lassen:

1. **Miss pro Aufgabe, nicht pro Modell.** „Unsere KI ist sparsamer" ist ohne Angabe, wofür, wertlos – zwischen einer kurzen Anfrage (0,31 Wh) und langem Nachdenken (3,91 Wh) liegt mehr als Faktor 12.
2. **Erwarte nicht, dass Effizienz die Rechnung senkt.** Sie senkt den Preis pro Einheit und erhöht die Menge. Wer wissen will, was KI kostet, muss auf Kraftwerke und Netze schauen, nicht auf Watt pro Prompt.
3. **Der nächste Intelligenz-Sprung kommt wahrscheinlich aus Verbindung, nicht aus Größe.** Kleine Modelle mit Werkzeugen, Prüfern und mehreren Versuchen schlagen größere ohne – vorausgesetzt, jemand bezahlt die Rechenzeit und baut Prüfungen, die nicht vom Modell selbst kommen. Es endet nicht die Skalierung; es endet die Vorstellung, dass Skalierung bequem ist.

## Quellen

Primärquellen (Auswahl, Stand der Recherche: 4. Oktober 2026):

1. IEA, *Energy and AI* (10.04.2025) – [Executive Summary](https://www.iea.org/reports/energy-and-ai/executive-summary)
2. IEA, *Key Questions on Energy and AI* (16.04.2026) – [Meldung zur Stromnutzung 2025](https://www.iea.org/news/data-centre-electricity-use-surged-in-2025-even-with-tightening-bottlenecks-driving-a-scramble-for-solutions)
3. LBNL für das US-DOE, *2024 United States Data Center Energy Usage Report* (20.12.2024) – [PDF](https://eta-publications.lbl.gov/sites/default/files/2024-12/lbnl-2024-united-states-data-center-energy-usage-report.pdf)
4. LBNL, *Queued Up: 2025 Edition* (15.12.2025) – [PDF](https://emp.lbl.gov/sites/default/files/2025-12/Queued%20Up%202025%20Edition%20-%2012.15.2025.pdf)
5. ERCOT, *Interconnection and Grid Analysis Update* (April 2026) – [PDF](https://www.ercot.com/files/docs/2026/04/13/9-Interconnection-and-Grid-Analysis-Update.pdf)
6. GE Vernova, Quartalsbericht Q3 2025 – [Pressemitteilung](https://www.gevernova.com/news/press-releases/ge-vernova-reports-third-quarter-2025-financial); Siemens Energy, Q4-GJ-2025 – [Pressemitteilung](https://assets.siemens-energy.com/dam/8b35c13c-396b-4623-8590-b3950053f94c/6--SE-Press-Release-EN-pdf_Original%20file.pdf)
7. Constellation Energy, Neustart Three Mile Island (20.09.2024) – [Meldung](https://www.constellationenergy.com/newsroom/2024/Constellation-to-Launch-Crane-Clean-Energy-Center-Restoring-Jobs-and-Carbon-Free-Power-to-The-Grid.html); Kairos Power, Baubeginn Hermes 2 – [Meldung](https://www.kairospower.com/updates/kairos-power-breaks-ground-on-hermes-2-demonstration-plant); Talen Energy/Amazon – [Meldung](https://ir.talenenergy.com/node/8671/pdf)
8. Google, *Measuring the environmental impact of delivering AI at Google Scale* (21.08.2025) – [Blog](https://cloud.google.com/blog/products/infrastructure/measuring-the-environmental-impact-of-ai-inference), [Paper](https://arxiv.org/abs/2508.15734)
9. Epoch AI, Energie pro ChatGPT-Anfrage – [Analyse](https://epoch.ai/gradient-updates/how-much-energy-does-chatgpt-use)
10. Kaplan et al., *Scaling Laws for Neural Language Models* (2020) – [arXiv:2001.08361](https://arxiv.org/abs/2001.08361); Hoffmann et al., *Chinchilla* (2022) – [arXiv:2203.15556](https://arxiv.org/abs/2203.15556)
11. Villalobos et al. / Epoch AI, *Will we run out of data?* – [arXiv:2211.04325](https://arxiv.org/abs/2211.04325), [Projektionsseite](https://epoch.ai/publications/will-we-run-out-of-ml-data-evidence-from-projecting-dataset)
12. Epoch AI, *Training compute of frontier AI models grows by 4–5x per year* (2024) – [Blog](https://epochai.org/blog/training-compute-of-frontier-ai-models-grows-by-4-5x-per-year); Schaeffer et al., *Are Emergent Abilities a Mirage?* (NeurIPS 2023) – [arXiv:2304.15004](https://arxiv.org/abs/2304.15004)
13. Snell et al., *Scaling LLM Test-Time Compute* (2024) – [arXiv:2408.03314](https://arxiv.org/abs/2408.03314); OpenAI, *Learning to reason with LLMs* (12.09.2024) – [Blog](https://openai.com/index/learning-to-reason-with-llms)
14. ARC Prize, o3-Ergebnisse und Kosten – [Blog](https://arcprize.org/blog/oai-o3-pub-breakthrough); *Inverse Scaling in Test-Time Compute* – [arXiv:2507.14417](https://arxiv.org/abs/2507.14417)
15. DeepSeek-V3 Technical Report – [arXiv:2412.19437](https://arxiv.org/abs/2412.19437); DeepSeek-R1 – [arXiv:2501.12948](https://arxiv.org/abs/2501.12948)
16. Quantisierung: [GPTQ](https://arxiv.org/abs/2210.17323) · [AWQ](https://arxiv.org/abs/2306.00978) · [AQLM](https://arxiv.org/abs/2401.06118); Pruning: [SparseGPT](https://arxiv.org/abs/2301.00774)
17. Qwen3 – [Blog](https://qwenlm.github.io/blog/qwen3/); Gemma 3 270M – [Google Developers Blog](https://developers.googleblog.com/en/introducing-gemma-3-270m/)
18. Agenten: [GAIA](https://arxiv.org/abs/2311.12983) · [OSWorld](https://arxiv.org/abs/2404.07972) · [SWE-bench](https://arxiv.org/abs/2310.06770) · [Large Language Monkeys](https://arxiv.org/abs/2407.21787) · [FrugalGPT](https://arxiv.org/abs/2305.05176) · [RouteLLM](https://arxiv.org/abs/2406.18665) · [MAST](https://arxiv.org/abs/2503.13657) · [Anthropic, Multi-Agent Research System](https://www.anthropic.com/engineering/multi-agent-research-system)
19. Rebound/Jevons: *From Efficiency Gains to Rebound Effects* (FAccT 2025) – [arXiv:2501.16548](https://arxiv.org/abs/2501.16548)
20. BitNet b1.58 – [arXiv:2402.17764](https://arxiv.org/abs/2402.17764); Densing Law – [Nature Machine Intelligence 2025](https://nature.com/articles/s42256-025-01137-0.pdf); TPU Ironwood – [Google Cloud](https://cloud.google.com/blog/topics/systems/ironwood-tpus-deliver-37x-carbon-efficiency-gains)

*Hinweis zur Methode: Alle Kernzahlen wurden gegen die hier verlinkten Primärquellen geprüft. Angaben von Herstellern (Google, DeepSeek, Qwen, NVIDIA, Siemens Energy, GE Vernova) sind als solche gekennzeichnet; bei ihnen fehlt eine unabhängige Nachprüfung. Wo Quellen sich widersprechen — etwa bei der Definition „KI-Rechenzentrum" zwischen IEA und einer Nature-Studie (118 TWh 2024 für rein KI-spezifische Anlagen) — steht das im Text.*
