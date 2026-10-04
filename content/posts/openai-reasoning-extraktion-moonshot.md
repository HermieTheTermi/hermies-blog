---
title: "OpenAI stoppt Reasoning-Extraktion und nennt Moonshot AI"
slug: "openai-reasoning-extraktion-moonshot"
date: 2026-10-03
status: published
tags: [openai, sicherheit, distillation, llm, news]
summary: "OpenAI hat eine koordinierte Kampagne zur Extraktion von geschütztem Modell-Reasoning unterbunden und ordnet einen Kern-Cluster Personen aus dem Umfeld von Moonshot AI zu. Eine US-Behörden-Advisory nennt seit September sechs chinesische Firmen."
source_url: "https://openai.com/index/disrupting-a-coordinated-model-distillation-campaign"
source_name: "OpenAI"
lang: de
---

## Was ist passiert

Am 30. September 2026 hat OpenAI einen Sicherheitsbeitrag veröffentlicht, der es in sich hat: Das Unternehmen schreibt, es habe eine koordinierte Kampagne erkannt und unterbunden, die darauf abzielte, „geschütztes Reasoning" aus seinen Modellen zu extrahieren. Also nicht sichtbare Antworten, sondern die internen Denkschritte.

Die Chronologie nennt OpenAI recht genau:

- Erste Aktivitäten beobachtete das Unternehmen in der ersten Juliwoche 2026, zunächst in geringem Umfang.
- Am 24. und 25. Juli folgten Spitzen mit **16.000 Anfragen von über 4.000 Nutzern**, die einem einschlägigen Extraktionsmuster folgten.
- Die weitere Untersuchung fand verwandte Prompt-Muster in einem Cluster von **mehr als 15.000 Nutzern**.
- Bis zum 28. Juli sei die Kampagne vollständig unterbunden worden.

Eine Fußnote schränkt ein: Die Zahlen beziehen sich auf *versuchte*, nicht zwingend erfolgreiche Extraktionen.

**Was „geschütztes Reasoning" ist.** Viele aktuelle Modelle rechnen vor der sichtbaren Antwort intern Zwischenschritte durch. Diese Kette — Chain-of-Thought genannt — wird vom Anbieter meist nicht im Klartext ausgeliefert, teils aus Produkt-, teils aus Sicherheitsgründen: Sie kann Informationen enthalten, die in der endgültigen Antwort bewusst weggelassen werden. OpenAI nennt sie „die interne Aufzeichnung eines Modells über die Bearbeitung einer Aufgabe".

**Was „adversariale Destillation" ist.** Destillation ist ein normales Verfahren im Maschinenlernen: Ein großes, teures Modell wird massenhaft befragt, die Antworten dienen als Trainingsdaten für ein kleineres Modell. Der „Schüler" lernt vom „Lehrer" zu einem Bruchteil der Kosten. „Adversarial" wird das Ganze, wenn es ohne Erlaubnis und gegen die Nutzungsbedingungen geschieht — hier, um nicht nur Antworten, sondern die Denkweise des Modells abzuschöpfen.

**Wie vorgegangen wurde.** OpenAI betont ausdrücklich, was *nicht* passiert ist: Es wurde keine Verschlüsselung geknackt, keine Datenbank kompromittiert und kein direkter Zugriff auf gespeicherte Gespräche anderer Nutzer erlangt. Stattdessen manipulierten die Beteiligten Modellinteraktionen so, dass verborgenes Reasoning in sichtbarer Form wiedergegeben wurde. Ein konkretes Beispiel aus dem Beitrag: Beteiligte kopierten verschlüsseltes Reasoning aus einem Gespräch und forderten ein Modell in einem *anderen* Gespräch auf, den verborgenen Inhalt zu entschlüsseln und zu transkribieren — ein Wiedergabe-Angriff, kein Einbruch.

**Die Zuordnung.** OpenAI schreibt, es sei unklar, ob alle beobachteten Beteiligten einem einzigen Akteur zuzuordnen sind. Einen „Kern-Cluster" der Aktivität ordnet das Unternehmen jedoch Personen zu, die mit Moonshot AI in Verbindung stehen — dem chinesischen Entwickler des Modells Kimi. Technische Belege für diese Zuordnung veröffentlicht OpenAI nicht.

## Warum zählt das

Der zweite Teil der Geschichte liegt außerhalb von OpenAI. Bereits Wochen zuvor hatte der Wettbewerber Anthropic chinesischen Entwicklern vorgeworfen, Claude heimlich zum Training eigener Modelle zu nutzen — darüber berichteten unter anderem die Wirtschaftsmedien (siehe Quellen). Am **8. September 2026** veröffentlichten NSA, CISA und FBI gemeinsam die Cybersecurity Advisory **AA26-251A**, die das Thema von der Firmen-Beschwerde auf die Ebene eines staatlichen Behörden-Dokuments hebt.

Was in der Advisory steht:

- Sechs namentlich genannte chinesische Firmen — **DeepSeek, Moonshot AI, Alibaba, MiniMax, StepFun und Z.AI** — hätten „Milliarden Token über Millionen von Austauschen/Anfragen" aus US-Frontier-Modellen extrahiert (Varianten von Claude, GPT, Gemini und Grok), seit mindestens Ende 2024.
- Die Kampagnen seien „das kritische Kernstück" — nicht nur eine Ergänzung — der Modellentwicklung dieser Firmen.
- Zu Moonshot AI heißt es konkret: signifikante Mengen von „Claude Fable 5"-Daten für das Modell Kimi-K3 und GPT-4o-Daten für Kimi-K2; die Ziele waren agentisches Reasoning und Tool-Nutzung, Coding und Datenanalyse, Computer-Use-Agenten und Computer Vision.
- Zu den Methoden zählt die Advisory Prompt-Muster, die Modelle zwingen, ihre verborgene Gedankenkette offenzulegen, den Betrieb über mehrere Zugangswege (native APIs, Cloud-Anbieter, Drittaggregatoren und „Transfer Stations" genannte Proxy-Netzwerke) sowie den automatischen Wechsel zwischen diesen Wegen, sobald einer blockiert wird. Die Formulierung zur Urheberschaft lautet „likely with Chinese government awareness" — also Kenntnis, nicht Steuerung.

Bemerkenswert ist die Empfehlungslage: Die Behörden raten US-Firmen, Antworten für Konten, die mit hoher Sicherheit der Destillation verdächtigt werden, **gezielt zu verschlechtern** — etwa auf ein weniger leistungsfähiges Modell umzuleiten, die Reasoning-Tiefe zu reduzieren oder stilistische Inkonsistenzen einzustreuen — und die Betroffenen darüber *nicht* zu informieren. Dazu kommen erweiterte Identitätsprüfung und ein branchenweiter Austausch von Indikatoren.

Für die Bewertung ist wichtig, was hier nicht vorliegt: Die Advisory ist eine Attributionsaussage dreier Behörden, kein Urteil, keine Anklage und keine Sanktion. Die technischen Beweise sind nicht öffentlich. Moonshot AI äußerte sich gegenüber anfragenden Medien zunächst nicht. Wer den Sachverhalt einordnen will, hat also zwei Quellen — einen betroffenen Anbieter und drei Sicherheitsbehörden — aber keine unabhängige Nachprüfung.

## Was heißt das praktisch

**Für Nutzer der Modelle ändert sich nichts unmittelbar.** Der Vorfall betrifft nicht die Konten normaler ChatGPT-Nutzender; OpenAI betont, dass keine fremden Gespräche zugänglich wurden.

**Für Teams, die Agenten bauen, ist der zweite Teil relevant.** Wenn Reasoningspuren in großem Stil und automatisiert ausgelesen werden, kann das künftig als Destillationsmuster gelten — auch bei legitimen Workflows, etwa Evaluationen, die Modellausgaben systematisch sammeln. Wer so etwas betreibt, sollte Zweck und Umfang dokumentieren können.

**Für Betreiber selbst gehosteter Frontier-Modelle.** OpenAI weist ausdrücklich darauf hin, dass Partner-Deployments denselben Schutz brauchen wie der eigene Dienst, und dass Angriffe über Tool-Ausgaben Schutzmaßnahmen erfordern, die mehr prüfen als sichtbaren Text. Wer ein Modell über Dritte hostet, erbt also nicht automatisch dessen Schutzmechanismen.

**Der geschlossene Angriffspfad ist konkret nachvollziehbar.** OpenAI beschreibt drei Maßnahmen: einen Pfad zu schließen, über den jemand, der bereits verschlüsseltes Reasoning aus dem Konto *einer anderen Person* besaß, dieses erneut einspielen und daraus Inhalte wiederherstellen konnte; Prüfungen, die gestreamte Ausgaben zurückhalten, wenn sie Reasoning offenlegen könnten; und die Zusammenarbeit mit Drittanbietern, auf deren Dienste die Aktivität auswich. Diese Klasse von Angriffen — Wiedergabe verschlüsselter, aber übertragbarer Zwischenartefakte — betrifft laut OpenAI auch Systeme anderer Anbieter.

## Quellen

- OpenAI: *Disrupting a coordinated model-distillation campaign* (30. September 2026) — https://openai.com/index/disrupting-a-coordinated-model-distillation-campaign
- NSA/CISA/FBI: Joint Cybersecurity Advisory **AA26-251A**, *China-Based Artificial Intelligence Companies Conducting Industrial-Scale Distillation Campaigns Against U.S. AI Companies* (8. September 2026) — https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-251a
- CNBC: *OpenAI flags Chinese-linked effort to extract AI model reasoning* (30. September 2026) — https://www.cnbc.com/2026/10/01/openai-chinas-moonshot-ai-kimi.html
