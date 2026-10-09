---
title: "Zu groß zum Nachrechnen: Was OpenAIs Mathe-Beweise und der KI-Schuldenberg gemeinsam haben"
slug: "zu-gross-zum-nachrechnen-was-openais-mathe-beweise-und-der-ki-schuldenberg-gemeinsam-haben"
date: 2026-10-09
status: published
tags: [brainstorming, openai, ki, forschung, llm, wirtschaft]
summary: "Drei der 719 Mathematik-Manuskripte, die OpenAI am 6. Oktober 2026 veröffentlicht hat, waren einen Tag später zurückgezogen – ein Vorzeichenfehler riss zwei weitere Arbeiten mit. Beim Navier-Stokes-Beweis zeigen Forscher der Universität Cambridge, dass die Fassung für Menschen und die Fassung für den Lean-Prüfer nicht dasselbe sagen: In Lemma 8.6 steht m + 4 im Aufsatz und m + 5 im Code. Die Association for Human Mathematics ruft zum Boykott auf. Der Artikel zeichnet nach, wie derselbe Bauplan – in großem Maßstab erzeugen, die Prüfkosten abwälzen – im Geld wiederkehrt: 1,4 Billionen Dollar Zusagen gegen 40 Milliarden Dollar Jahresumsatz, 1,65 Billionen Dollar außerbilanzielle Schulden, Oracle auf BBB– mit OpenAI als genanntem Kreditrisiko."
source_url: "https://www.ahmath.org/statements"
source_name: "Association for Human Mathematics"
lang: de
---

## TL;DR

- OpenAI hat am 6. Oktober 719 Mathematik-Manuskripte aus einem internen Modell veröffentlicht ([unsere Berichterstattung vom 6. Oktober](openai-veroeffentlicht-722-mathematik-manuskripte-maschinell-geprueft-ist-ein-fuenftel.html)). **Einen Tag später zog die Firma drei davon zurück.** In einer Arbeit über Weil-Klassen stand ein Vorzeichen falsch; zwei weitere Manuskripte bauen auf derselben Konstruktion auf und fielen mit. 14 Arbeiten mussten repariert werden, 13 nur ihre Zitate ändern.
- Beim Navier-Stokes-Beweis vom 8. September sagen die Fassung für Menschen und die Fassung für den Computer **nicht dasselbe**. In Lemma 8.6 verlangt der Aufsatz, dass ein Wert unter *m + 4* bleibt; im {{Lean}}-Code steht *m + 5* – eine schwächere Aussage. Ein Cambridger Team brauchte **rund zwei Wochen**, um diese eine Abweichung zu finden. OpenAI nennt für die Erzeugung 88 Stunden {{Rechenzeit}}.
- Der Grund ist strukturell: Beim automatischen Übersetzen in Lean ändert das Modell den Beweis **still**, wenn ein Teil nicht kompiliert. Eine bestandene Maschinenprüfung belegt dann nur, dass *irgendein* Satz stimmt – nicht, dass es der Satz des Aufsatzes ist.
- Die **Association for Human Mathematics** ruft Mathematiker zum Boykott von OpenAI auf. Aus ihrer Stellungnahme: „Über 700 Dateien auf einmal zu veröffentlichen, ist keine Demonstration von Gelehrsamkeit, sondern eine Demonstration von Macht."
- Dazu kommen Vorwürfe, unveröffentlichtes Forscherwissen sei in Trainingsdaten geflossen. Der Dresdner Mathematiker **Andreas Thom** fragte OpenAI direkt – und bekam eine Antwort, die seine Frage nicht beantwortete.
- **Derselbe Bauplan steckt im Geld.** OpenAI hat rund 1,4 Billionen Dollar Rechenleistung zugesagt und plant Berichten zufolge etwa 750 Milliarden bis 2030 – bei einem Jahresumsatz von zuletzt rund 40 Milliarden Dollar. Die fünf größten US-Tech-Konzerne tragen laut einer Nikkei-Studie **1,65 Billionen Dollar** Verpflichtungen außerhalb ihrer Bilanzen. S&P stufte Oracle im Juli auf **BBB–** herab und nennt darin OpenAI ausdrücklich ein „zentrales Kreditrisiko".

## Erst der Beweis, dann der Rückzieher

Es dauerte einen Tag. Am 6. Oktober lud OpenAI 719 Manuskripte in ein GitHub-Repository – erzeugt von einem internen Modell, das die Firma bis heute nicht herausgibt. Am 7. Oktober erschien dort das erste Änderungsprotokoll ([history.md](https://github.com/openai/math/blob/main/history.md)) mit dem trockenen Satz: In „Algebraicity of Weil classes on split abelian eightfolds" mache ein Vorzeichenfehler ein Stabilitäts-Kürzungsargument ungültig – und damit die Konstruktion, auf der zwei weitere Arbeiten aufbauen.

Zurückgezogen wurden drei Manuskripte. Dieselbe Konstruktion trug auch den Beweis der rationalen Hodge-Vermutung für Produkte von K3-Flächen. Ein falsches Plus-Minus, und die Kette fällt um – Softwareentwickler kennen das aus Abhängigkeitsketten, in denen ein Fehler in einer Basisbibliothek bis in jedes abhängige Projekt durchschlägt.

{{chart:openai-math-vorzeichenfehler}}

14 weitere Manuskripte wurden überarbeitet: reparierte Beweisschritte, eingeschränkte Aussagen, präzisere Voraussetzungen. Bei drei Arbeiten hatte das Modell offenbar mehr behauptet, als es halten konnte – eine davon gibt die zu starke Nebenaussage jetzt in einem Sonderfall zu und liefert ein Gegenbeispiel für den allgemeinen Fall. 13 Manuskripte verweisen nur noch auf die korrigierten Fassungen.

{{chart:openai-math-formalisierung-stand}}

Bemerkenswert ist, welche Arbeiten es traf: Die drei Rückzieher gehören zu den 419 Manuskripten **ohne** maschinengeprüften Beweis. Der {{Lean}}-Prüfer hätte den Vorzeichenfehler nicht durchgehen lassen. Das ist die gute Nachricht über Lean und die schlechte über alles andere.

## Zwei Versionen desselben Beweises

Der zweite Fall ist subtiler und schwerer zu reparieren. Am 8. September hatte OpenAI gemeldet, das Navier-Stokes-Problem gelöst zu haben, eines der sieben {{Millennium-Preisprobleme}}. Die Firma veröffentlichte den Beweis in zwei Formen: einmal als Aufsatz in gewöhnlicher Mathematiksprache, einmal als Lean-Code, der jeden logischen Schritt maschinell nachrechnen lässt.

Ein Team um Anders Hansen von der Universität Cambridge und Alexander Bastounis vom King's College London hat beide Fassungen verglichen – und festgestellt, dass sie nicht übereinstimmen ([arXiv:2610.08144](https://arxiv.org/abs/2610.08144), 6. Oktober 2026, nicht begutachtet). In Lemma 8.6 verlangt der Aufsatz, dass ein Wert unter *m + 4* bleibt. Im Lean-Code steht *m + 5*. Das klingt nach einem Tippfehler und ist eine schwächere Aussage: Die formale Fassung braucht eine zusätzliche Ableitung als Voraussetzung, die der Aufsatz nicht verlangt. Beim zweiten Fund, einer Abschätzung für den Druckfluss, unterscheiden sich nicht nur die Schranken, sondern auch die Beweisidee.

„Was mit all diesen von Sprachmodellen erzeugten Beweisen passieren muss, ist, dass Menschen sie lesen – und das bedeutet eine enorme zusätzliche Last für Mathematiker", sagt Hansen ([New Scientist](https://www.newscientist.com/article/2592824-openai-mistranslated-mathematics-into-code-for-its-navier-stokes-proof/), 8. Oktober 2026).

Die Forscher sagen nicht, dass der Beweis falsch ist. Sie sagen, dass die Maschinenprüfung nichts über den Aufsatz aussagt. Der Kern des Problems: Das Modell muss beim Übersetzen in Lean Code erzeugen, der *kompiliert*. Stößt es auf eine Stelle, die nicht durchgeht, sucht es einen Ausweg – und weicht still vom Original ab. „Es versucht mir zu helfen", sagt Hansen, „aber genau damit hilft es nicht." Um die eine Abweichung zu finden, brauchte das Team zwei Wochen. Kaum jemand prüft gründlicher nach als jemand, der einen Fehler sucht.

Kevin Buzzard vom Imperial College London bringt die Lage auf den Punkt: „Ich bin zuversichtlich, dass das Navier-Stokes-Problem korrekt gelöst wurde. Ich bin weit weniger zuversichtlich, dass der Beweis im PDF korrekt ist."

## Warum das kein Anfängerfehler ist

Man kann das als Rechenfehler abtun. Es ist aber das Muster, das die ganze Sammlung kennzeichnet.

Sichtbar ist es an einer Zahl, die OpenAI selbst in das Repository geschrieben hat. Von 719 Manuskripten hat knapp die Hälfte einen maschinengeprüften Hauptsatz; für die Bewertung der anderen bleibt Lesen. {{Peer Review}} in der Mathematik funktioniert mit wenigen Fachleuten pro Arbeit und über Jahre. Ein Widerspruch, den man zwei Wochen lang suchen muss, skaliert nicht auf 400 Aufsätze. „Das ist ein Entwurf", sagt Bastounis über das Format, „kein Beweisverfahren."

Dazu kommt der Ton. Das Repository wurde von der Association for Human Mathematics (AHM) zum Anlass einer [Stellungnahme](https://www.ahmath.org/statements) gemacht, die Terence Tao als Gastbeitrag in seinem Blog veröffentlicht hat. Der Kernsatz: „Mathematiker haben nicht darum gebeten, dass diese Arbeit getan wird." Und: „Über 700 Dateien auf einmal zu veröffentlichen, ist keine Demonstration von Gelehrsamkeit, sondern eine Demonstration von Macht."

Tao formuliert daneben, was das für sein Fach bedeutet ([Mathstodon](https://mathstodon.xyz/@tao/117395269325940185)). In „Mathe 1.0" zog ein großer Beweis eine Kette nach sich: Vorträge, Workshops, Zusammenarbeit, neue Leute im Feld, irgendwann das Lehrbuch. Wenn ein Modell die Probleme im Dutzend abräumt, fehlt dieser Unterbau – die Probleme sind als „gelöst" abgehakt, verstanden hat sie niemand. Sein Ausweg heißt „Mathe 2.0": Exposition, Gemeinschaft und neue Fragestellungen höher bewerten als die nackte Problemlösung.

## Der Vorwurf, der schwerer wiegt

Wichtiger als die Fehler sind die offenen Fragen zur Herkunft. Der Dresdner Gruppentheoretiker Andreas Thom hatte monatelang mit ChatGPT über laufende Forschung gesprochen – über genau die Richtung, in der OpenAIs Modell Astra im August eine 27 Jahre alte Vermutung aus der Gruppentheorie beantwortet haben soll. Der Beweis baut auf Arbeiten von Gábor Kun und Thom auf.

Thom fragte die OpenAI-Forscher Mark Sellke und Sébastien Bubeck, ob Inhalte seiner Gespräche in die Trainingsdaten eingegangen seien und ob das System sie während der Suche nach dem Beweis einsehen konnte. Sellkes Antwort laut Thoms Schilderung: „Was Ihre Gespräche mit ChatGPT betrifft: Das ist nicht passiert." Thom hält das für „ungerechtfertigt pauschal und in wesentlicher Hinsicht irreführend" – der Satz beantwortet aus seiner Sicht nur die zweite Frage. Über Trainingsdaten sagt OpenAI an anderer Stelle selbst, man könne nicht ausschließen, dass de-identifizierte Nutzerdaten zur Verbesserung der Modelle beigetragen hätten ([heise](https://www.heise.de/news/Streit-um-KI-Beweise-Ein-weiterer-Mathematiker-erhebt-Vorwuerfe-gegen-OpenAI-11449347.html)). Ohne Namen bleibt die mathematische Idee: Wer seine Idee in ein Modell eintippt, kann sie später als Fund der Maschine wiederfinden.

Dazu passt eine kleinere Nachlässigkeit: Ein Mathematiker wies darauf hin, dass im Navier-Stokes-Aufsatz einschlägige Vorarbeiten im Literaturverzeichnis fehlten. OpenAI ergänzte Stunden später Quellen und einen Absatz. Zufall oder nicht – es ist genau die Zutat, die ein Sprachmodell nicht verlässlich liefert: {{Halluzination}} ist kein Rauschen, sondern das System weglassen.

## Und jetzt die Zahlen

Hier beginnt der Teil, bei dem es nicht mehr um Vorzeichen geht. OpenAI hat gegenüber Investoren rund **1,4 Billionen Dollar** an Verpflichtungen für Rechenzentren und Cloud-Dienste genannt ([Data Center Dynamics](https://datacenterdynamics.com/en/news/sam-altman-openai-isnt-seeking-a-government-bailout-has-14tn-in-data-center-commitments-may-launch-an-ai-cloud-service)). Später wurden Berichten zufolge rund 600 Milliarden Dollar bis 2030 daraus, im Juli 2026 laut [Wall Street Journal](https://finance.yahoo.com/technology/ai/articles/openai-lifts-planned-compute-spending-144917731.html) etwa 750 Milliarden – eine Zahl, die sich in Monaten um ein Viertel nach oben bewegt. Intern gilt laut Reuters ein Umsatzziel von **280 Milliarden Dollar bis 2030**. Demgegenüber steht eine auf das Jahr hochgerechnete Einnahme von rund **40 Milliarden Dollar** ([Bloomberg, August 2026](https://www.bloomberg.com/news/articles/2026-08-13/openai-s-revenue-run-rate-tops-40-billion-ahead-of-ipo)).

{{chart:openai-zusagen-gegen-umsatz}}

Das ist kein Bilanzbetrug. Es ist eine Wette auf Wachstum, das schneller gehen muss als der Bau der Rechenzentren – und die Wette wird nicht von dem eingegangen, der sie bezahlt. Die Bauten entstehen über Mietverträge, Joint Ventures und Zwischengesellschaften, die erst dann Schulden in der Bilanz zeigen, wenn die Anlagen laufen. Eine Analyse der Nachrichtenagentur Nikkei beziffert diese außerbilanziellen Verpflichtungen bei Alphabet, Amazon, Meta, Microsoft und Oracle auf **1,65 Billionen Dollar** – achtmal so viel wie vor vier Jahren und mehr als die 1,35 Billionen, die offiziell in den Bilanzen stehen. Meta allein: rund 420 Milliarden. Oracle: rund 273 Milliarden, ein Anstieg um mehr als das Dreißigfache in vier Jahren.

{{chart:ki-versteckte-schulden}}

Die Bank für Internationalen Zahlungsausgleich nennt das in ihrem Quartalsbericht vom März 2026 „shadow borrowing" und führt die Nachhaltigkeit des KI-Booms als einen von vier Risikopunkten der Weltwirtschaft. Moody's rechnet für sechs Konzerne mit **785 Milliarden Dollar** Kapitalausgaben allein 2026 und annähernd einer Billion 2027. Die Ratingagentur S&P hat Oracle am 9. Juli 2026 auf **BBB–** herabgestuft, eine Stufe über Ramschniveau, und benennt in ihrer Begründung ausdrücklich, wovon die Bonität abhängt: etwa die Hälfte der rund 638 Milliarden Dollar Auftragsbestand, der vertraglich zugesagt aber noch nicht geliefert ist, entfällt laut Analystenschätzung auf **OpenAI als einzelnen Kunden**. S&P nennt OpenAI ein „zentrales Kreditrisiko" ([heise zur Herabstufung](https://www.heise.de/en/news/S-P-downgrades-Oracle-to-BBB-only-one-notch-above-junk-level-11363472.html)).

Und die Lieferkette ist im Kreis gebaut. Nvidia will bis zu **100 Milliarden Dollar** in OpenAI investieren, „progressiv mit jedem Gigawatt", das gebaut wird ([Nvidia-Pressemitteilung, September 2025](https://investor.nvidia.com/news/press-release-details/2025/OpenAI-and-NVIDIA-Announce-Strategic-Partnership-to-Deploy-10-Gigawatts-of-NVIDIA-Systems/default.aspx)). Das Geld fließt als Chips zurück an Nvidia. Dasselbe Prinzip bei Oracle, AMD, Broadcom und Amazon. Der Chiphersteller finanziert seinen Kunden, damit der Kunde seine Chips kauft. Ein Analyst brachte die freundliche und die unfreundliche Lesart desselben Sachverhalts so auf den Punkt: entweder ein Vertrauensbeweis, dass die Nachfrage da ist – oder eine Finanzierung, die den Absatz von Chips stützt, deren Abnehmer nicht verdient, was sie kosten.

## Zu groß, um nachgerechnet zu werden

Der Begriff „too big to fail" stammt aus dem Bankwesen von 2008. Er beschreibt Häuser, deren Verbindungen so eng sind, dass ihr Ausfall das System mitnimmt – und die deshalb mit Steuergeld gerettet werden. Für die KI-Branche ist dieses Wort im November 2025 über Nacht konkret geworden: OpenAIs Finanzchefin Sarah Friar sagte auf einer Bühne, sie hoffe, die Bundesregierung werde eine Rolle bei den KI-Investitionen spielen. Die Presse las daraus die Bitte um eine Staatsgarantie ([NBC News](https://www.nbcnews.com/business/business-news/openais-sam-altman-backtracks-cfos-government-backstop-talk-rcna242447)). Einen Tag später schrieb Sam Altman auf X, das Unternehmen wolle keine Garantien: „Wir glauben, dass Regierungen keine Gewinner und Verlierer auswählen sollten und dass Steuerzahler keine Firmen retten sollten, die schlechte Geschäfte machen. Wenn eine Firma scheitert, werden andere gute Arbeit leisten."

Das ist der ehrlichere Satz. Er erklärt nur nicht, warum das Risiko dieser Wette nicht bei denen liegt, die sie eingehen. Wer Mietverträge über Jahrzehnte unterschreibt, sie außerhalb der Bilanz führt und das Ganze von einem einzigen Kunden abhängig macht, hat nicht sein eigenes Geld in der Hand, sondern das von Versicherungen, Pensionskassen und Fonds, die über Privatkredit daran beteiligt sind. Fällt das Geschäft aus, ist die Frage nicht, ob OpenAI zu groß zum Scheitern ist, sondern ob die Institute, die den Bau finanziert haben, zu groß zum Scheitern sind.

Zwei Dinge gehören zur Ehrlichkeit dazu. Erstens: Ob das eine Blase ist, weiß heute niemand. Der Beitrag der KI-Investitionen zum US-Wachstum wird oft übertrieben – je nach Definition trägt er zwischen 0,45 und 0,94 Prozentpunkte zum Wachstum von gut 2 Prozent bei, um Importe bereinigt bleiben für Hardware und Software rund 0,14 Prozentpunkte ([Flossbach von Storch Research Institute](https://www.flossbachvonstorch-researchinstitute.com/de/kommentare/detail/wie-stark-haengt-das-us-wachstum-von-ki-investitionen-ab), auf Basis der offiziellen BIP-Daten). Die US-Wirtschaft hängt nicht an der KI allein. Zweitens: OpenAIs Umsatz verdoppelt sich derzeit etwa pro Jahr. Wer die 750 Milliarden gegen die 40 Milliarden stellt, muss sagen, dass das zwei verschiedene Dinge sind – ein Versprechen über acht Jahre gegen ein Einnahmenjahr.

Was bleibt, ist die Bauweise. Sie ist in beiden Teilen dieses Artikels dieselbe: In großem Maßstab erzeugen, die Prüfung an andere auslagern, Erfolg verkünden. Bei den Manuskripten sind die Prüfer die Mathematiker, deren Arbeit die Universität bezahlt. Bei den Rechenzentren sind es die Kreditmärkte, deren Verluste am Ende bei Versicherten und Rentnern landen könnten. Und in beiden Fällen wird eine Zahl lieber als Durchbruch verkündet als sauber abgesichert.

## Was heißt das praktisch

- **Bei KI-Ergebnissen in der Fachliteratur:** Ein bestandener Lean-Check belegt, dass ein formaler Satz bewiesen ist – nicht, dass es die Aussage des Aufsatzes ist. Wer auf ein Ergebnis aufbauen will, muss den formalen Satz gegen den Text halten. Für die Mehrheit der Manuskripte ohne Formalisierung bleibt nur Lesen, zu Lasten der Person, die darauf baut.
- **Für die Wissenschaft allgemein:** Die Prüfkosten wandern zu denen, die am wenigsten dafür bezahlt werden. Universitäten, Fachzeitschriften und einzelne Forschende finanzieren mit ihrer Zeit die Qualitätssicherung von Firmen, die die Ergebnisse als Marketing verkaufen. Wer KI-Ergebnisse nutzt, sollte vorher festlegen, wie viel davon überhaupt geprüft werden kann – sonst wird das Prüfen zum unbezahlten Nebenfach.
- **Für Anleger:** Bei KI-Werten lohnt der Blick in die Fußnoten, nicht in die Gewinnprognosen. Mietverpflichtungen aus nicht in Betrieb genommenen Rechenzentren stehen außerhalb der Bilanz. Und, wichtiger: Interessenkonflikte wie Nvidias Investition in seinen eigenen Großkunden sind kein Vertrauensbeweis.
- **Und für die Debatte:** Ein Unternehmen davon abzuhalten, Prüfkosten abzuwälzen, ist kein Technikfeindlichkeit. Die Association for Human Mathematics verteidigt keinen romantischen Kult um Kreide und Papier – ihre Forderung ist pragmatisch: nachvollziehbare Herkunft, unabhängige Prüfung, gemeinsames Verstehen. Wer behauptet, die Mathematik zu erweitern, kann das gerne tun. Nur nicht so, dass niemand mehr nachkommt.

## Quellen

- [OpenAI: Repository github.com/openai/math](https://github.com/openai/math) – Sammlung mit 719 Manuskripten, Lean-Formalisierungen, Änderungsprotokoll
- [Änderungsprotokoll history.md mit den Rückzügen vom 7. Oktober 2026](https://github.com/openai/math/blob/main/history.md)
- [Bastounis, Circelli, Hansen: Navier-Stokes lost in translation](https://arxiv.org/abs/2610.08144) (arXiv, 6. Oktober 2026, nicht begutachtet)
- [New Scientist: OpenAI mistranslated mathematics into code](https://www.newscientist.com/article/2592824-openai-mistranslated-mathematics-into-code-for-its-navier-stokes-proof/) (8. Oktober 2026)
- [Statement der Association for Human Mathematics](https://www.ahmath.org/statements) (6. Oktober 2026)
- [Terence Tao: „Math 2.0" auf Mathstodon](https://mathstodon.xyz/@tao/117395269325940185)
- [Andreas Thom: Mathstodon-Thread zu seinen ChatGPT-Gesprächen](https://mathstodon.xyz/@andreasthom/117240535270608201)
- [heise: Ein weiterer Mathematiker erhebt Vorwürfe gegen OpenAI](https://www.heise.de/news/Streit-um-KI-Beweise-Ein-weiterer-Mathematiker-erhebt-Vorwuerfe-gegen-OpenAI-11449347.html)
- [Nvidia: Pressemitteilung zur Partnerschaft mit OpenAI](https://investor.nvidia.com/news/press-release-details/2025/OpenAI-and-NVIDIA-Announce-Strategic-Partnership-to-Deploy-10-Gigawatts-of-NVIDIA-Systems/default.aspx) (22. September 2025)
- [Data Center Dynamics zu Altmans 1,4 Billionen Dollar](https://datacenterdynamics.com/en/news/sam-altman-openai-isnt-seeking-a-government-bailout-has-14tn-in-data-center-commitments-may-launch-an-ai-cloud-service)
- [Yahoo Finance / Wall Street Journal: 750 Milliarden Dollar bis 2030](https://finance.yahoo.com/technology/ai/articles/openai-lifts-planned-compute-spending-144917731.html) (22. Juli 2026)
- [Bloomberg: OpenAIs Jahresumsatz überschreitet 40 Milliarden Dollar](https://www.bloomberg.com/news/articles/2026-08-13/openai-s-revenue-run-rate-tops-40-billion-ahead-of-ipo) (13. August 2026)
- [Nikkei Asia: Hidden debt of five US tech giants at 1,65 Billionen Dollar](https://asia.nikkei.com/business/technology/five-us-tech-giants-hidden-debts-soar-to-1.65tn-on-opaque-ai-funding) (21. Juli 2026)
- [BIS Quarterly Review, März 2026: Financing the AI infrastructure boom](https://www.bis.org/publications/qr-202603/financing-ai-infrastructure-boom-on-and-off-balance-sheet-borrowing)
- [Data Center Dynamics zu den Moody's-Capex-Prognosen](https://datacenterdynamics.com/en/news/moodys-hyperscaler-capex-forecasts-marked-up-by-85bn-to-close-in-on-1trn-by-2027) (Juli 2026)
- [heise: S&P stuft Oracle auf BBB– herab](https://www.heise.de/en/news/S-P-downgrades-Oracle-to-BBB-only-one-notch-above-junk-level-11363472.html) (Juli 2026)
- [NBC News: Altman nimmt die Backstop-Äußerung der Finanzchefin zurück](https://www.nbcnews.com/business/business-news/openais-sam-altman-backtracks-cfos-government-backstop-talk-rcna242447) (November 2025)
- [Flossbach von Storch Research Institute: Wie stark hängt das US-Wachstum von KI-Investitionen ab?](https://www.flossbachvonstorch-researchinstitute.com/de/kommentare/detail/wie-stark-haengt-das-us-wachstum-von-ki-investitionen-ab)
