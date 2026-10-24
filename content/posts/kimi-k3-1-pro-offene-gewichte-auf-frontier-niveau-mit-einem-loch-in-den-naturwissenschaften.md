---
title: "Kimi K3.1 Pro: Offene Gewichte auf Frontier-Niveau — mit einem Loch in den Naturwissenschaften"
slug: "kimi-k3-1-pro-offene-gewichte-auf-frontier-niveau-mit-einem-loch-in-den-naturwissenschaften"
date: 2026-10-23
status: published
tags: [news, ki, llm, modelle, open-weights, sicherheit, benchmark]
summary: "Moonshot AI veröffentlicht Kimi K3.1 Pro: 3-Billionen-Klasse, eine Million Token Kontext, 65,7 Prozent auf Terminal-Bench 4.0 und Preise von 2 auf 10 Dollar. Die Gewichte kommen bis 4. November — und dem Modell wurden gezielt Cyber-Fähigkeiten wegtrainiert."
source_url: "https://www.kimi.ai/blog/kimi-k3-1-pro"
source_name: "Moonshot AI"
lang: de
---

## TL;DR

- **Moonshot AI hat Kimi K3.1 Pro veröffentlicht** — das erste Modell der neuen K3.1-Serie, ein Modell der 3-Billionen-Parameter-Klasse mit einem {{Kontextfenster}} von einer Million {{Token}}.
- **Coding:** 65,7 Prozent auf Terminal-Bench 4.0 — 0,7 Punkte hinter Claude Opus 5.5 (66,4 Prozent), aber klar vor GPT-6 Astra (58,2 Prozent). Alles Herstellerangaben.
- **Preis:** 2 Dollar pro Million Eingabe-Token, 10 Dollar pro Million Ausgabe-Token — deutlich billiger als der Vorgänger K3 (3 und 15 Dollar).
- **Die Gewichte kommen erst:** Moonshot verspricht die vollständigen {{Offene Gewichte}} bis zum 4. November. Selbst hosten geht heute nicht.
- **Der Haken:** Auf wissenschaftlichen Terminal-Aufgaben liegt K3.1 Pro bei 38,1 Prozent, GPT-6 Astra bei 68,1 Prozent.
- **Sicherheit:** Moonshot hat dem Modell Cyber-Fähigkeiten wegtrainiert — von 90,5 auf 81,0 Prozent auf dem eigenen Exploit-Benchmark.

Am Freitagabend europäischer Zeit hat Moonshot AI aus Peking sein neues Flaggschiff vorgestellt. Kimi K3.1 Pro ist keine neue Architektur, sondern eine deutlich weiter trainierte Version von Kimi K3 aus dem Juli. Der Unterschied steckt im Nachtraining: Moonshot spricht von „substanziell größerem Post-Training-Compute" und einem gemeinsamen {{Reinforcement Learning}} über „hunderte nachgelagerte Domänen" — also viele Fachgebiete gleichzeitig statt nacheinander.

Das ist der Punkt, an dem sich die chinesischen Labore gerade messen: nicht mehr die Größe des Grundmodells, sondern wie viel Verstärkungslernen man obendrauf bekommt. Moonshot beschreibt, dass dafür die ganze Kette optimiert wurde — RL-Framework, Inferenz über lange Kontexte, Trainings-Effizienz, {{Sandbox}}-Infrastruktur und die Reihenfolge, in der Trainingsläufe eingeplant werden.

## Was in der Kiste steckt

Laut einem von Moonshot verlinkten Post sind es 2,8 Billionen Gesamt{{Parameter}}, von denen 104 Milliarden pro Token aktiv werden — ein {{Mixture-of-Experts}}-Modell, bei dem pro Anfrage nur ein Bruchteil des Netzes rechnet. Die Architektur stammt aus K3: Kimi Delta Attention, Attention Residuals, 16 von 896 Experten pro Schritt. Moonshot selbst spricht nur von „3T-Klasse" und nennt die genauen Zahlen im Blog nicht.

Dazu gibt es eine zweite Variante, **K3.1 Pro Highspeed**, die laut Hersteller zwei- bis dreimal so schnell antwortet bei gleichen Fähigkeiten. Beide laufen ab sofort auf kimi.ai, in den Kimi-Apps, in Kimi Work (Windows und Apple Silicon), in Kimi Code und über die {{API}} unter den IDs `kimi-k3.1-pro` und `kimi-k3.1-pro-highspeed`, die zur OpenAI-Schnittstelle kompatibel ist.

## Die Coding-Zahlen

{{chart:kimi-k31-terminal-bench}}

Auf Terminal-Bench 4.0, einem {{Benchmark}} für Programmier-{{Agent}}en in der Kommandozeile, kommt K3.1 Pro auf 65,7 Prozent. Claude Opus 5.5 liegt bei 66,4 Prozent, GPT-6 Astra bei 58,2 Prozent. Auf SWE-Marathon führt Moonshot mit 51,7 gegenüber 46,3 für Opus 5.5. Auf dem eigenen, internen Kimi Code Bench 3.0 Long-horizon steigert sich das Modell von 55,95 auf 61,2 Prozent.

Wichtig zur Einordnung: Alle Werte sind Herstellerangaben, gemessen mit maximaler Denkstufe und dem Claude-Code-{{Harness}}. Moonshot weist selbst darauf hin, dass bei den Vergleichsmodellen teilweise Werte aus deren eigenen Berichten oder aus Leaderboards übernommen wurden — also nicht zwingend unter identischen Bedingungen. Unabhängig nachgeprüft ist davon nichts.

## 3D, CAD und Finanzen

{{chart:kimi-k31-benchcad}}

Die zweite auffällige Stärke ist räumliches Arbeiten. Auf BenchCAD, das aus mehreren Ansichten eines Objekts CAD-Code rekonstruiert, erreicht K3.1 Pro 92,7 Prozent mit Werkzeugen — knapp hinter Opus 5.5 (96,2) und GPT-6 Astra (95,9). Ohne Werkzeuge liegt es mit 72,8 Prozent praktisch gleichauf mit Opus (73,0).

Moonshot zeigt dazu Beispiele, die nach echter Arbeit klingen: ein Turbofan-Modell in FreeCAD mit 2.100 Einzelkörpern, eine druckbare Lampe aus fünf Teilen, eine Kathedrale mit 3,3 Millionen Dreiecken. Dazu ist auf kimi.ai ein Werkzeug namens „3D Make" live, das Modelle direkt im Browser bearbeitbar macht und als druckfertige Datei exportiert.

Im Finanzbereich meldet Moonshot einen Bestwert von 64,4 auf OfficeQA Pro v2, das Kennzahlen aus echten Geschäftsberichten herausziehen muss. Auf den eigenen Finanz-Tests legt das Modell gegenüber K3 um 7,2 Punkte beim Financial Modeling und 11,6 Punkte bei der Recherche zu, im Geschäftsbetrieb auf das 4,2-Fache.

## Der Haken: Naturwissenschaften

Eine Zahl fällt aus dem Muster. Auf Terminal-Bench Science 0.1 — Aufgaben aus Biologie, Physik, Geowissenschaften, Mathematik und Ingenieurwesen — steht K3.1 Pro bei 38,1 Prozent. GPT-6 Astra kommt laut der Vergleichstabelle auf 68,1, Claude Opus 5.5 auf 63,3. Das ist ein Rückstand von 25 bis 30 Punkten, nicht von einem.

Für alle, die das Modell für Laborarbeit, Simulationen oder Messdatenauswertung einsetzen wollen, ist das die entscheidende Einschränkung. Moonshots eigene Beispiele kommen fast alle aus Software, Spielentwicklung und Konstruktion — Bereiche, in denen Fehler sichtbar werden und sich billig korrigieren lassen. In der Wissenschaft ist ein falscher Rechenschritt teuer.

## Sicherheit: Moonshot nimmt dem Modell das Hacken

{{chart:kimi-k31-cyber}}

Der bemerkenswerteste Teil der Ankündigung ist kein Benchmark, sondern eine Trainingsentscheidung. Moonshot beobachtete, dass die Fähigkeit, Sicherheitslücken zu finden und auszunutzen, mit jedem Schritt Nachtraining stieg. Die Ursache: Cyber-Inhalte steckten ohnehin im allgemeinen Trainingskorpus, und Exploit-Aufgaben waren in der Lernumgebung.

Für die Veröffentlichung der Gewichte hat Moonshot diese Daten aus beiden Trainingsphasen entfernt — und dann gemessen, was das kostet. Auf dem hauseigenen xdev-bench-hard, der echte Schwachstellen in Linux-Kernel, Node.js, JavaScriptCore, Exim und VirGL nachbaut, löst der unbereinigte Zwischenstand 90,5 Prozent der Aufgaben. Das ausgelieferte K3.1 Pro kommt auf 81,0 Prozent. Der Vorgänger K3 lag bei 33,3 Prozent.

Moonshot formuliert die Regel so: Man wolle keine offenen Gewichte veröffentlichen, die die absolute Grenze der Cyber-Fähigkeit verschieben. Das Modell bleibt also absichtlich unter dem, was die eigene Pipeline könnte — und nach eigener Aussage hinter geschlossenen Frontier-Modellen, die seit mindestens drei Monaten öffentlich sind. Gleichzeitig kündigt das Unternehmen an, die verfügbare Cyber-Fähigkeit in offenen Gewichten schrittweise anzuheben.

Das Argument dafür ist nachvollziehbar und trotzdem unbequem: Wer die Gewichte heruntergeladen hat, kann sie nicht mehr filtern, überwachen oder zurückrufen. Der Hinweis von Reuters, dass offene Modelle zentrale Kontrolle erschweren, ist keine Kritik an der Absicht, sondern eine Beschreibung der Mechanik.

## Was es kostet

- Eingabe: **2,00 Dollar** pro Million Token (Cache-Treffer: 0,20 Dollar)
- Ausgabe: **10,00 Dollar** pro Million Token
- Highspeed-Variante: 4,00 und 20,00 Dollar
- Zum Vergleich K3: 3,00 und 15,00 Dollar

Dazu kommen einige Eigenheiten, die man kennen sollte. Die Denkstufe lässt sich nur über `reasoning_effort` mit `low`, `high` oder `max` steuern, Standard ist `max`; abschalten lässt sich das Nachdenken nicht. Temperatur (1,0) und Top-p (0,95) sind fest verdrahtet. Bilder und Videos nimmt das Modell nur als Base64 oder über Datei-IDs, nicht als öffentliche URL. Die Web-Suche bezeichnet Moonshot selbst als „in Überarbeitung" und rät von produktivem Einsatz ab. Und ab dem 31. Oktober 2026 wird die K2-Serie für neue Nutzer geschlossen, zum Jahresende soll sie ganz verschwinden.

Eine kleine Unstimmigkeit am Rand: Der Blog nennt für den Halluzinations-Test Kimi Hallu Bench Hard einen Rückgang von 23,4 auf 8,3 Prozent, die API-Dokumentation für eine andere Auswertung 23,35 auf 6,85 Prozent. Beide Zahlen sind plausibel, sie messen unterschiedliche Dinge — aber wer die Ankündigung liest, sollte wissen, dass zwei offizielle Seiten verschiedene {{Halluzination}}en nennen.

## Was das praktisch heißt

Für Teams, die Coding-Agenten betreiben, ist K3.1 Pro derzeit das günstigste Modell, das laut Herstellerangaben an die geschlossene Spitze heranreicht: 2 Dollar Eingabe sind ein Drittel dessen, was Frontier-Anbieter verlangen. Ob die 65,7 Prozent auf Terminal-Bench 4.0 halten, wenn unabhängige Tester mit eigenem Harness nachmessen, ist offen — bei früheren Kimi-Releases lagen die eigenen Werte meist im Rahmen, aber selten exakt.

Selbst hosten ist keine Option für Workstations. 2,8 Billionen {{Parameter}} bedeuten Rechenzentrums-Hardware; Moonshot empfahl für K3 Cluster mit 64 und mehr Beschleunigern. Die offenen Gewichte sind damit vor allem für Anbieter interessant, die das Modell als Dienst betreiben — nicht für den Rechner unter dem Schreibtisch.

Und wer über offene Gewichte als Sicherheitsfrage diskutiert, bekommt hier ein sauber dokumentiertes Beispiel: Ein Hersteller kann Fähigkeiten vor der Veröffentlichung gezielt reduzieren und den Effekt beziffern. Was er nicht kann, ist sie nach der Verteilung wieder einsammeln.

## Quellen

- Moonshot AI, „Introducing Kimi K3.1 Pro": https://www.kimi.ai/blog/kimi-k3-1-pro
- Kimi API, K3.1-Pro-Schnellstart (Grenzen, Denkstufen, Vision): https://platform.kimi.ai/docs/guide/kimi-k3-1-pro-quickstart
- Kimi API, Modellpreise: https://platform.kimi.ai/docs/pricing/chat
- MarkTechPost, „Moonshot AI Releases Kimi K3.1 Pro" (Parameter, Einordnung): https://www.marktechpost.com/2026/10/23/moonshot-ai-kimi-k3-1-pro-open-weight-model/
- Unite.AI, „Moonshot AI Releases Kimi K3.1 Pro" (Produktverfügbarkeit, Kimi-Code-Details): https://www.unite.ai/moonshot-ai-releases-kimi-k3-1-pro-first-model-in-new-k3-1-series/
- Reuters über Rappler, „Moonshot curbs hacking ability in new Kimi model": https://www.rappler.com/technology/moonshot-curbs-hacking-ability-kimi-model/
