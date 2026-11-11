---
title: "Drei Tage statt sechs Monate: Anthropics AMD-Zahl und ihre Fußnote"
slug: "drei-tage-statt-sechs-monate-anthropics-amd-zahl-und-ihre-fussnote"
date: 2026-11-11
time: "15:25"
status: published
tags: [news, llm, modelle, labs]
summary: "Im Börsengang-Video von Anthropic sagt Mitgründer Tom Brown, sein Modell Mythos habe Claude in drei Tagen auf AMD-GPUs gebracht, praktisch ohne menschliches Eingreifen. Die Fußnote derselben Folie schränkt das ein: rund drei Tage für die Prompt-Verarbeitung eines einzigen Modells auf MI355X-Chips, kein Training. Der Prospekt nennt keine Tage, dafür eine Aktienzusage von AMD über bis zu 5,0 Milliarden Dollar und einen Umsatzanstieg von 1.127 Prozent im dritten Quartal."
source_url: "https://ipo.anthropic.com/us"
source_name: "Anthropic (Investorenseite)"
lang: de
---

## TL;DR

- Anthropics Mitgründer Tom Brown sagt im Börsengang-Video des Unternehmens: „It got Claude running on AMD in just three days, with basically no human intervention. Claude ported or wrote almost 100% of the kernels." Das Video steht seit dem 10. November auf der Investorenseite und läuft 42 Minuten und 43 Sekunden.
- Die Fußnote auf derselben Folie schränkt das ein: Die rund drei Tage gelten für die Prompt-Verarbeitung eines einzigen Anthropic-Modells auf AMD-MI355X-Grafikprozessoren, „at a useful level of performance". Trainingsläufe deckt die Angabe nicht ab.
- Die Schlagzeile, die daraus wurde, steht nicht im Video. Ein Post auf X eröffnet mit „The Nvidia CUDA moat is gone" und hatte am 11. November rund 573.000 Aufrufe. Die Sprechspur nennt weder Nvidia noch CUDA, gezählt null Mal.
- Der Börsenprospekt formuliert vorsichtiger: Anthropic könne neue Chip-Plattformen „in a fraction of the time" in Betrieb nehmen. Eine Zahl von Tagen steht dort nicht.
- Belegt ist etwas anderes, und es ist beachtlich genug: Claude läuft auf vier Chip-Familien. Im dritten Quartal 2026 wuchs der Umsatz um 1.127 Prozent gegenüber dem Vorjahr, die Compute- und Infrastrukturkosten um 382 Prozent.

## Was ist passiert

Anthropic hat am 10. November seine Investorenpräsentation zum geplanten Börsengang veröffentlicht, ein Video von 42 Minuten Länge mit elf Kapiteln. Im Abschnitt „Approach to compute" erklärt Mitgründer Tom Brown, wie das Unternehmen mit Rechenleistung umgeht. Die Passage, die anschließend durch das Netz ging, steht bei Minute 20:42.

Brown sagt dort, Anthropic trainiere und betreibe Claude inzwischen auf allen vier großen Chip-Familien: AWS Trainium, Google TPUs, Nvidia-GPUs und AMD-GPUs. Das sei nur möglich, weil man früh auf eine Mehrchip-Strategie gesetzt habe, zu einer Zeit, als viele das für die Mühe nicht wert hielten. Jede Chip-Familie brauche einen eigenen Software- und Inferenz-Stack, und das sei teuer und schwierig. Man mache das seit Jahren und sei darin „incredibly good" geworden.

Dann folgt das Beispiel. Man habe in diesem Jahr erstmals mit AMD-GPUs gearbeitet. Früher habe es Dutzende Ingenieure und Monate gekostet, eine neue Chip-Plattform in Betrieb zu nehmen. „This time, we had Mythos try it out. It got Claude running on AMD in just three days, with basically no human intervention. Claude ported or wrote almost 100% of the kernels."

{{vergleich:amd-claim}}

Auf der Folie, die während des Satzes läuft, steht ein Balkendiagramm: rund drei Tage mit Mythos gegen rund sechs bis zwölf Monate mit herkömmlicher Ingenieursarbeit. Der Vergleichswert stammt aus der eigenen Erfahrung des Unternehmens, nicht aus einer Messung an einem Fremdprojekt.

## Warum zählt es

Der Grund, warum ein Satz über Kernel-Portierung so weit reist, liegt in der Ökonomie der Branche. Nvidias Vorsprung besteht nicht nur aus Silizium. Er besteht aus CUDA, der Programmierschicht, auf die fast jede KI-Software zugeschnitten ist. Wer ein Modell auf einen anderen Chip bringt, muss die rechenintensiven Kernroutinen neu schreiben, und das war bisher Arbeit für Spezialisten über Monate. Diese Kosten sind der Grund, warum viele Firmen den Wechsel gar nicht erst versuchen.

Wenn ein Modell diese Arbeit selbst erledigt, ändert sich die Rechnung an zwei Stellen. Erstens sinkt der Preis für Unabhängigkeit: Wer zwischen Anbietern wechseln kann, verhandelt anders über Rechenzeit. Zweitens wird die Fähigkeit selbst zum Produkt. Brown rahmt sie ausdrücklich so. Anthropic spreche von „Compute-Multiplikatoren", also Verbesserungen, die aus derselben Hardware mehr effektive Rechenleistung machen. Ein Vervierfacher bedeutet: Ein Modell, das 100 Einheiten braucht, lässt sich mit 25 trainieren. Brown sagt im Video, Claude werde solche Multiplikatoren künftig „entirely by itself" finden.

Das ist die eigentliche Botschaft der Passage: nicht, dass Nvidia entthront ist, sondern dass ein Labor seine eigene Werkzeugkette mit dem eigenen Modell beschleunigt. Die drei Tage sind dafür das anschaulichste Beispiel.

Anthropics Abhängigkeit von Nvidia endet damit ohnehin nicht. Nvidia steht auf der Folie als eine der vier Chip-Familien. Nvidia kauft außerdem im Rahmen des Börsengangs Aktien des Unternehmens: Der Prospekt nennt eine Privatplatzierung über insgesamt 26,0 Milliarden Dollar, an der sich unter anderem Micron, Microsoft, Nvidia und TSMC Partners beteiligen. Mit AMD besteht seit Juli 2026 ein Rahmenvertrag über Helios-Rack-Systeme mit Instinct-GPUs der MI450-Serie, dazu eine Aktienzusage von AMD über bis zu 5,0 Milliarden Dollar, die nach Liefermeilensteinen abrufbar wird. Die ersten Meilensteine erwartet Anthropic 2027.

## Was heißt das praktisch

Was die Fußnote wegnimmt, ist der Anspruch auf einen allgemeinen Durchbruch. Sie gilt für ein Modell, nicht für alle. Sie deckt die Prompt-Verarbeitung ab, also das Verarbeiten der Eingabe, und nicht das Training. Sie nennt den MI355X und nicht die ganze AMD-Palette. Zu Geschwindigkeit und Kosten steht dort nichts, und ein Vergleich mit Nvidia fehlt ebenfalls. Ob das Modell auf dem Chip so schnell läuft wie auf dem, für den es ursprünglich gebaut wurde, sagt niemand.

Der Prospekt, also das Dokument mit rechtlicher Bindung, bleibt noch vorsichtiger. Er sagt, die Mehrchip-Architektur erlaube es, neue Chip-Plattformen „in a fraction of the time this once required" in Betrieb zu nehmen, und führt als Beleg das Geschäftswachstum an. Das Wort „days" kommt in diesem Zusammenhang nicht vor. Auch die Chips differieren: Die Folie nennt MI355X, der Prospekt für die AMD-Lieferung MI450. Die Bezeichnung MI355X findet sich im Prospekt nicht.

::: methode
Diese Prüfung folgt drei Quellen: der Sprechspur des Videos in einer von Simon Willison erstellten Transkription, den Zitaten der Fußnote aus einer vollständigen Auswertung des Unternehmens CellCog, und dem geänderten Registrierungsdokument bei der US-Börsenaufsicht SEC (Amendment No. 2). Die Fußnote selbst steht nur im Bild, nicht im Text; zitiert wird sie hier nach CellCog, das die Einblendung wörtlich wiedergibt und die Aufrufzahlen der X-Posts mit Zeitstempel dokumentiert. CellCog betreibt eigene Angebote auf Anthropics Modellen und legt diese Interessenlage offen. Eigene Messungen gibt es keine, und Mythos ist kein öffentlich zugängliches Modell.
:::

Bemerkenswert ist, wie die Zahl gereist ist. Aus „in drei Tagen lief Claude auf AMD" wurde in Sozialen Netzen „der CUDA-Graben ist weg". Letzteres ist eine Aussage über Nvidia, über AMD, über Marktanteile. Im Video fällt sie nicht. Dort beschreibt Brown einen Betriebsablauf: Test, Portierung, Inbetriebnahme.

Für die Bewertung des Börsengangs ist die Passage trotzdem relevant, und zwar unabhängig von der Fußnote. Anthropic legt offen, dass die Kosten für Rechenleistung langsamer wachsen als der Umsatz. Im dritten Quartal 2026 stieg der Umsatz um 1.127 Prozent gegenüber dem Vorjahr, die Ausgaben für Compute und Infrastruktur um 382 Prozent. Die bereinigte operative Marge lag laut Investorenseite bei 15 Prozent in diesem Quartal, das langfristige Ziel nennt das Unternehmen mehr als 35 Prozent. Wenn ein Modell die Anpassung an neue Hardware verbilligt, ist das ein Hebel auf genau diese Zahlen.

Was fehlt, ist die Gegenprobe. Niemand außerhalb von Anthropic hat die Portierung gesehen, das Tempo gemessen oder die Kernel geprüft. Das Unternehmen nennt weder Ingenieursstunden noch die Leistung auf dem MI355X. Solange das so bleibt, ist die Drei-Tage-Zahl eine Angabe aus einer Verkaufspräsentation, die zufällig auch technisch interessant ist.

## Quellen

- Anthropic, Roadshow-Video zum Börsengang, 10. November 2026: https://ipo.anthropic.com/us
- Transkription der Sprechspur von Simon Willison, 11. November 2026: https://gist.github.com/simonw/9806757fe8acec6221cb0a5cce4d720d
- Anthropic, „Anthropic launches roadshow for proposed initial public offering", 10. November 2026: https://www.anthropic.com/news/roadshow-launch
- Anthropic, geänderte Registrierungserklärung (Amendment No. 2), SEC/EDGAR: https://www.sec.gov/Archives/edgar/data/2130357/000162828026072484/anthropicpbc-sx1ax2.htm
- CellCog, „Anthropic Roadshow Video: The AMD and Disease Claims", 11. November 2026 (Fußnote, Zeitmarken, Aufrufzahlen): https://cellcog.ai/blog/anthropic-roadshow-video-amd-cancer-claims/
- The Decoder, „Anthropic says AI is eroding Nvidia's CUDA lead", 11. November 2026: https://the-decoder.com/anthropic-says-ai-is-eroding-nvidias-cuda-lead-cutting-an-amd-chip-switch-from-months-to-three-days/
- Umsatz-, Kosten- und Margenzahlen: Registrierungserklärung Amendment No. 2 sowie Investorenseite, Stand 11. November 2026. Herstellerangaben, nicht unabhängig geprüft.
