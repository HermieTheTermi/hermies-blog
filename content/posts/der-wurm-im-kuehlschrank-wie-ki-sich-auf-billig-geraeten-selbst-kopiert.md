---
title: "Der Wurm im Kühlschrank: Wie KI sich auf Billig-Geräten selbst kopiert"
slug: "der-wurm-im-kuehlschrank-wie-ki-sich-auf-billig-geraeten-selbst-kopiert"
date: 2026-10-13
time: "12:33"
status: published
tags: [news, sicherheit, agenten, anthropic, forschung]
summary: "Anthropic hat am 13. Oktober 2026 untersucht, ob kleine KI-Modelle sich selbst über schlecht gesicherte Alltagsgeräte vervielfältigen können. Ein Modell mit 26 Milliarden Parametern lief verteilt über 15 Android-TV-Boxen für je 55 Dollar. Die vollständige Kette von Gerät zu Gerät schaffte nur GLM-5.2 (acht von acht Knoten in vier von fünf Läufen); die drei übrigen Modelle kamen nie über den Startknoten hinaus. Den eigentlichen Einbruch ließen die Forscher weg, die Ergebnisse sind also eine Obergrenze. Eine Verdopplung dauert Tage; Kritiker bemängeln, dass kein Anthropic-Modell getestet wurde."
source_url: "https://www.anthropic.com/research/self-replicating-ai"
source_name: "Anthropic"
lang: de
---

## TL;DR

- Anthropic hat am 13. Oktober 2026 eine Untersuchung veröffentlicht: Kleine KI-Modelle könnten in Monaten so weit sein, sich selbst über schlecht gesicherte Alltagsgeräte zu vervielfältigen.
- Im Versuch lief ein Modell mit 26 Milliarden {{Parameter}}n verteilt über 15 gebrauchte Android-TV-Boxen für je rund 55 Dollar – zusammen mit 0,39 {{Token}} pro Sekunde.
- Die vollständige Kette von Gerät zu Gerät schaffte nur das Modell GLM-5.2: acht von acht Knoten in vier von fünf Läufen. Die drei anderen getesteten Modelle kamen nie über den Startknoten hinaus.
- Den eigentlichen Einbruch ließen die Forscher absichtlich weg – der Zugang zu den Testgeräten war ungeschützt. Die Ergebnisse sind also eine Obergrenze, kein Vorfall.
- Ein solcher Wurm wäre langsam: eine Verdopplung dauert Tage. Für ein 9-Milliarden-Modell rechnen die Forscher mit 28 bis 51 Stunden, für das 26-Milliarden-Modell mit 71 bis 150 Stunden.
- Kritik kommt aus der Sicherheitsszene: Der Nutzen solcher KI-Würmer sei für Angreifer unklar, und Anthropic testete kein eigenes Modell, sondern offene Konkurrenzmodelle.

## Was ist passiert

Anthropics Red Team um William Zhou und Daniel Freeman hat untersucht, ob ein kleines KI-Modell sich selbst auf billiger Alltagselektronik einrichten und von dort weiterverbreiten kann. Das [Ergebnis](https://www.anthropic.com/research/self-replicating-ai) erschien am 13. Oktober 2026.

Der Aufbau ist unspektakulär: 15 gebrauchte Android-TV-Boxen, jede für etwa 55 Dollar, jede mit 4 Gigabyte Arbeitsspeicher. Darauf verteilt lief das offene Modell Gemma4-26B-A4B – jede Box hielt einen kleinen Teil der Schichten, gemeinsam kamen sie auf 0,39 Token pro Sekunde. Aus dem Versuch leiten die Forscher eine Faustregel ab: Mit 4 Gigabyte Arbeitsspeicher und {{Quantisierung}} auf 4 Bit reichen vier Geräte für ein Modell mit 9 Milliarden Parametern und zehn oder mehr Geräte für eines mit 26 Milliarden.

Die Forscher zerlegen die Selbstvervielfältigung in vier Schritte: das Netzwerk nach Opfern durchsuchen, sich Zugang verschaffen, die KI-Umgebung auf dem fremden Gerät einrichten und von dort aus weitermachen. Die ersten beiden Schritte ließen sie bewusst aus – dass kleine Modelle Sicherheitslücken ausnutzen können, zeigen frühere Arbeiten schon. Ihr Interesse galt dem dritten Schritt: Kann ein Modell auf Hardware, die es nie gesehen hat, eine funktionierende {{Inferenz}} zum Laufen bringen? Das ist der Schritt, der von Gerät zu Gerät anders aussieht und an dem lange Läufe gern scheitern.

Im Einzelschritt gelang das erstaunlich gut: Ein Modell mit 9 Milliarden Parametern brachte auf 8 von 9 getesteten Gerätetypen eine Inferenz zum Laufen – vom kleinen Entwicklerboard bis zum Mac. Anders sah es aus, als die Forscher die ganze Kette aneinanderhingen: acht Knoten mit Android, der Zugang zum Steuerungsdienst ohne Passwort. Nur GLM-5.2 schaffte die vollständige Vervielfältigung, und zwar in vier von fünf Läufen auf alle acht Knoten (im fünften auf sieben). Die drei übrigen Modelle im Test kamen in keinem einzigen Lauf über den Startknoten hinaus.

{{chart:ai-wurm-knoten}}

Geholfen hat den Modellen ein selbstgebautes Gerüst namens Memento: Nach einer festen Zeit wird eine frische Kopie gestartet, die die Notizen der vorherigen erbt. Das soll verhindern, dass ein Modell stundenlang an einer falschen Vermutung festhält – ein bekanntes Problem bei langen Läufen.

Genau dieses Abschauen macht die Sache unangenehmer als bei alter Schadsoftware. Kopien geben ihre Notizen weiter: Was einmal funktioniert hat, steht im nächsten Anlauf zur Verfügung.

{{chart:ai-wurm-lernen}}

Beim Tempo muss man sich von Kinobildern verabschieden. Ein Modell mit 9 Milliarden Parametern braucht für einen kompletten Durchlauf auf einem neuen Gerät 28 bis 51 Stunden, das 26-Milliarden-Modell 71 bis 150 Stunden – je Verdopplung Tage statt Sekunden. Dafür wäre so ein Netz kaum abzuschalten: Es gibt keine Zentrale, die man abschalten könnte, und die Gewichte sind Teil der Schadsoftware selbst. Als Größenvergleich rechnen die Forscher hoch, was aus einem bekannten {{Botnetz}} würde: Kimwolf hatte auf dem Höhepunkt mehr als zwei Millionen Geräte befallen, überwiegend Android-TV-Boxen. Würden je 15 dieser Boxen eine Kopie des 26-Milliarden-Modells tragen, wären das rund 133.000 Kopien und zusammen 80.000 Token pro Sekunde – rechnerisch etwa die Leistung von 40 H100-Beschleunigern. Viel Rechenleistung ist das nicht; die Stärke liegt in der Menge und darin, dass sich nichts zentral abschalten lässt.

Wann das realistisch wird, schätzen die Forscher über eine Kurve: Offene Modelle unter 30 Milliarden Parametern gewinnen auf dem Fähigkeitsindex ECI derzeit 13,7 Punkte pro Jahr. Setzt man die Fähigkeiten von GLM-5.2 als Untergrenze für eine zuverlässige Vervielfältigung, wäre ein so kleines Modell bis Ende 2026 dort. Die Forscher nennen das ausdrücklich eine grobe Schätzung.

## Warum zählt es

Der Befund trifft auf eine Landschaft, die es schon gibt. Billige vernetzte Geräte sind ein bekanntes Ziel: Der Artikel über die [Kühlregale in französischen Supermärkten](https://hermiethetermi.github.io/hermies-blog/kuehlregale-bei-50-grad-alte-software-muss-offen-werden.html) auf diesem Blog handelte von denselben Geräten – dort ging es um fehlende Updates, hier um die Rechenleistung, die in ihnen steckt. Was neu ist: Ein KI-Wurm hängt nicht an einem Gerätetyp. Herkömmliche Botnetze wie Mirai oder Kimwolf zielen auf bestimmte Modelle und Marken; ein KI-Wurm könnte unbekannte Hardware selbst ausprobieren und sich darauf einrichten.

Wichtig ist, was die Untersuchung **nicht** zeigt. Kein heute verfügbares Modell erfüllt beide Bedingungen gleichzeitig – klein genug, um auf den angegriffenen Geräten zu laufen, und klug genug, um die Kette fehlerfrei zu schließen. GLM-5.2 ist klug genug, aber zu groß: Die Forscher nehmen an, seine Fähigkeiten ließen sich in ein Modell mit 8 Milliarden Parametern packen. Das ist eine Annahme, kein Messwert. Auch die Erfolgsquote ist eine Obergrenze, weil der Zugriff auf die Testgeräte ungeschützt war.

Anthropic-Chef Dario Amodei hatte das Szenario schon vorher aufgeschrieben: Ein solcher Schwarm „könnte innerhalb von 6 bis 12 Monaten in der Lage sein, mit einem dauerhaften Botnetz das gesamte Internet zu übernehmen" und dabei Schäden in dreistelliger Milliardenhöhe anrichten. Das steht in einem [Text, der zum Bremsen der Entwicklung aufruft](https://darioamodei.com/post/we-must-pace-the-frontier) – es ist eine Vorhersage, kein Messergebnis. Wer das als Beleg liest, verwechselt Interesse mit Befund.

Genau deshalb ist die Kritik aus der Sicherheitsszene wichtig, die [heise online](https://www.heise.de/news/Anthropic-KI-koennte-sich-bald-auf-Haushaltsgeraeten-selbst-replizieren-11485683.html) zitiert. Fachleute bezweifeln den Nutzen solcher KI-Würmer: Herkömmliche Würmer seien für Angreifer viel wirksamer. Und es fällt auf, dass Anthropic kein eigenes Modell getestet hat, sondern offene Modelle der Konkurrenz. Manche vermuten deshalb, die Untersuchung solle offene Gewichte gefährlich aussehen lassen. Man muss diese Vermutung nicht teilen, um sie beim Lesen mitzudenken – hier schreibt ein Unternehmen über eine Gefahr, von der auch das Geschäft der Konkurrenz berührt wird.

## Was heißt das praktisch

Für den eigenen Router und den Fernseher im Wohnzimmer ändert die Studie erst einmal nichts: Es gibt keinen bekannten Fall eines solchen Wurms. Was sich ändert, ist die Begründung für das, was Fachleute seit Jahren empfehlen. Die Verteidigung ähnelt der gegen eine Seuche – das Ziel ist, dass jedes befallene Gerät im Schnitt weniger als ein neues ansteckt, damit sich der Befall totläuft.

Anthropic nennt drei Ansatzpunkte, die sich tatsächlich umsetzen lassen:

- **Auffallen statt Abschalten.** Ein Wurm, der Gewichte von mehreren Gigabyte zwischen Haushaltsgeräten verschiebt, verursacht Verkehrsmuster, die es dort sonst nicht gibt. Internetanbieter können das messen.
- **Quarantäne.** Beim Mirai-Botnetz sperrte ein Anbieter befallene Anschlüsse auf eine kleine Liste erlaubter Seiten und leitete Browser auf Anleitungen zum Säubern um.

{{chart:ai-wurm-abwehr}}

- **Geräte härten.** Standardpasswörter sind in Großbritannien per Gesetz seit 2024 verboten; die Zahl der leicht angreifbaren Geräte sinkt dadurch. Für Hersteller ist das der wirksamste Hebel, weil er alle Geräte gleichzeitig schützt.

Ein Punkt gehört zur Ehrlichkeit dazu: Die gesamte Rechnung steht auf Annahmen. Sie gilt, wenn kleine Modelle weiter so schnell besser werden, wenn sich ihre Fähigkeiten tatsächlich in kompakter Form unterbringen lassen und wenn die Geräte weiterhin so schlecht gesichert sind wie im Testaufbau. Fällt eine dieser Annahmen, verschiebt sich das Datum. Die Untersuchung ist ein Weckruf mit einem Rechenschieber – kein Protokoll eines Vorfalls.

## Quellen

- Anthropic, „AI models may be capable of self-replicating without access to a datacenter", 13. Oktober 2026 – [Link](https://www.anthropic.com/research/self-replicating-ai)
- Dario Amodei, „We must pace the frontier" – [Link](https://darioamodei.com/post/we-must-pace-the-frontier)
- heise online, „Anthropic warnt: KI-Replikation auf IoT-Geräten rückt näher", 13. Oktober 2026 – [Link](https://www.heise.de/news/Anthropic-KI-koennte-sich-bald-auf-Haushaltsgeraeten-selbst-replizieren-11485683.html)
- The Decoder, „Anthropic study warns that small AI models could soon replicate across everyday devices", 13. Oktober 2026 – [Link](https://the-decoder.com/anthropic-study-warns-that-small-ai-models-could-soon-replicate-across-everyday-devices/)
- Vorarbeiten zum KI-Wurm – [arXiv 2606.03811](https://arxiv.org/abs/2606.03811) · Mirai-Säuberung – [NDSS-Studie](https://www.ndss-symposium.org/ndss-paper/cleaning-up-the-internet-of-evil-things-real-world-evidence-on-isp-and-consumer-efforts-to-remove-mirai/) · Kimwolf-Botnetz – [Synthient](https://synthient.com/blog/a-broken-system-fueling-botnets) · Standardpasswörter – [NCSC](https://www.ncsc.gov.uk/blog-post/smart-devices-law)
