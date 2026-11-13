---
title: "llama.cpp ist 1.0: Ein Versprechen an alle, die den Code einbinden"
slug: "llama-cpp-ist-1-0-ein-versprechen-an-alle-die-den-code-einbinden"
date: 2026-11-13
time: "11:20"
status: published
tags: [news, llm, benchmark, open-weights]
summary: "Die Organisation ggml-org hat am 13. November llama.cpp und ggml auf Version 1.0.0 gesetzt. Die 1.0 ist vor allem ein Versprechen an nachgelagerte Projekte: Ab jetzt zeigt eine neue Hauptversion eine inkompatible C-Schnittstelle an, dafür fallen 35 veraltete Funktionen weg. Technisch kommen FP8-KV-Caches, ein Experten-Cache für Mixture-of-Experts-Modelle und ein gehärteter Server. Im Reddit-Thread zum Jubiläum dominiert die Bitte um mehr Maintainer, und ein Community-Vergleich misst, dass der Fork Strata 2,4-mal schneller schreibt."
source_url: "https://github.com/ggml-org/llama.cpp/releases/tag/v1.0.0"
source_name: "GitHub (ggml-org)"
lang: de
---

## TL;DR

- Das Team hinter llama.cpp hat am 13. November um 10:20 UTC die Version 1.0.0 veröffentlicht, zusammen mit der Tensor-Bibliothek ggml, die ebenfalls auf 1.0.0 geht. Der letzte Schliff steckt in einem Commit mit der Kennung `b1b770d`.
- Die 1.0 ist vor allem ein Versprechen an alle, die die C-Bibliothek einbinden: Ab jetzt zeigt eine neue Hauptversion eine inkompatible Schnittstelle an. Dafür fallen 35 veraltete Funktionen und `llama_set_warmup` aus der öffentlichen Header-Datei.
- Technisch bringt das Release FP8-{{KV-Cache}}s, einen Cache für die Experten von {{Mixture-of-Experts}}-Modellen mit einstellbarem CPU-Anteil, einen OpenAI-kompatiblen Endpunkt für Sprachausgabe und einen gehärteten Server gegen SSRF, CORS und DNS-Rebinding.
- Dreieinhalb Jahre nach dem ersten {{Commit}} stehen 134.862 Sterne, 25.553 Forks, 447 Beitragende und 2.604 offene Issues. Auf Reddit ist der meistgewählte Kommentar zum Jubiläum die Bitte um mehr Maintainer.
- Ein Fork namens Strata, der auf demselben Code aufsetzt, schreibt in einem Community-Vergleich 2,4-mal schneller und liest Prompts 2,9-mal schneller. Der Vergleich stammt aus einem einzigen Issue-Thread mit einer Grafikkarte und einem Modell, ist also ein Hinweis und keine Beweislage.

## Was ist passiert

Am 13. November um 10:20 UTC hat die Organisation ggml-org die Version 1.0.0 von llama.cpp veröffentlicht ([Release](https://github.com/ggml-org/llama.cpp/releases/tag/v1.0.0)). Zur selben Stunde ging `ggml` auf 1.0.0, die Tensor-Bibliothek, auf der die {{Inferenz}} läuft. Der Blogbeitrag dazu steht bei Hugging Face, geschrieben von Daniel Bevenius, Georgi Gerganov, merve und weiteren Mitgliedern der Organisation ([Hugging Face](https://huggingface.co/blog/ggml-org/llama-cpp-v1)).

Der Anlass ist kein neues Modell, sondern die Verantwortung gegenüber denen, die den Code einbauen. "Jede neue Integration bedeutet mehr Entwickler, die von unseren Bibliotheksschnittstellen abhängen, und deshalb ist eine flexible, aber stabile {{API}} entscheidend", heißt es im Blog. Konkret: Ein Wechsel der Hauptversion zeigt jetzt eine inkompatible C-Schnittstelle an, ein Wechsel der Nebenversion eine rückwärtskompatible Erweiterung, ein Patch eine Fehlerbehebung ohne Schnittstellenänderung.

Der Preis für diese Klarheit steht in den Release-Notes. 35 als veraltet markierte Funktionen, `llama_set_warmup` und der Parameter `defrag_thold` sind aus `llama.h` verschwunden. Wer eigene Anwendungen gegen die Bibliothek baut, muss diese Stellen suchen, bevor er aktualisiert.

Inhaltlich ist das Release kein reines Aufräumen. Die {{Quantisierung}} des {{KV-Cache}}s kann jetzt FP8 in der OCP-Variante, mit optionalen Skalen pro Tensor. Für MoE-Modelle gibt es einen Cache für Experten im Hauptspeicher, dessen CPU-Anteil sich einstellen lässt, mit zwei Verdrängungsstrategien. Dazu kommen das Nachladen externer Parameter-Shards, vier neue Architekturen (Kimi-K3.1-Pro, Ripple-65B-Preview, xing4_0 und die Sprachausgabe drama-3), ein Endpunkt `/v1/audio/speech` nach dem Muster von OpenAI und ein neu gebauter Web-Client für den Server. Sicherheitsrelevant sind vier Reparaturen: SSRF, CORS, DNS-Rebinding und der Abbruch von Werkzeugaufrufen über MCP.

{{zahlen:llamacpp-1-0}}

## Warum zählt es

Die Zahl 1.0 ist in der Softwarewelt eine Zusage, keine Leistung. Sie sagt, dass ein Projekt seine Schnittstelle für ernst genug hält, um sie zu versionieren. Für llama.cpp wiegt das mehr als bei den meisten Projekten: 447 Menschen haben Code beigetragen, das Repository hat 134.862 Sterne, und die Bibliothek ist die Grundlage für eine ganze Klasse von Anwendungen, die lokale Modelle auf Laptops, Servern und Einplatinenrechnern laufen lassen.

Der zweite Grund ist unangenehmer. Das Projekt trägt seit Monaten eine Debatte über sein Tempo mit sich, und die 1.0 hat sie nicht beendet. Im Reddit-Thread zur Veröffentlichung, mit 744 Punkten und 90 Kommentaren derzeit der sichtbarste Ort zum Thema, ist der bestbewertete Kommentar keine Gratulation, sondern eine Bitte: "Bitte fügt dem Projekt mehr Maintainer hinzu, es gibt buchstäblich eine Tonne offener Issues und Pull Requests" ([Reddit](https://reddit.com/comments/1xv8t2e)). Ein Antwortkommentar mit 65 Punkten nennt den Grund für die Ungeduld: llama.cpp sei gegenüber Projekten wie Strata deutlich zurückgefallen, beim Nachladen von Gewichten von der SSD sei der Fork inzwischen weit vorn, und die Geschwindigkeitsgewinne kämen nicht mehr im Wochentakt.

Ein Beleg für die Wartezeit lässt sich nachprüfen. Der Pull Request, der das Modell Dory unterstützt, liegt seit dem 10. Oktober offen, ohne Zusammenführung, mit 20 Kommentaren ([GitHub](https://github.com/ggml-org/llama.cpp/pull/30306)). Ein Modell, das in dieser Branche im Oktober interessant war, ist im November alt.

Der Gegenpunkt kommt im selben Thread und ist ebenfalls richtig. llama.cpp läuft auf Grafikkarten und Prozessoren, für die andere Engines keinen Code bauen. "Strata unterstützt keine alte Hardware wie llama", schreibt ein Kommentar, und ein anderer nennt die Container-Abbilder für CUDA, ROCm und SYCL als Grund, warum er bleibt: herunterladen, Modell daneben legen, starten. Die Spitze ist woanders, die Fläche ist hier.

{{tabelle:llamacpp-strata}}

## Was heißt das praktisch

Wer llama.cpp in eine eigene Anwendung einbindet, sollte jetzt gegen 1.0 bauen und die Liste der entfernten Funktionen aus den Release-Notes abarbeiten. Danach zeigt jede Aktualisierung, ob sie bricht. Das ist der eigentliche Gewinn dieser Veröffentlichung.

Wer lokale MoE-Modelle fährt und dabei Speicher knapp wird, hat zwei neue Schrauben: `moe_cache_size` und `moe_cache_cpu_share`. Die Community-Messung oben zeigt aber auch die Grenze: Bei einer Karte, auf die das Modell vollständig passt, kostet der Cache rund zehn Prozent {{Durchsatz}} gegenüber dem normalen Laden, weil statt zwei Graph-Aufteilungen pro {{Token}} fünfzig anfallen. Der Cache ist ein Werkzeug für den Fall, dass das Modell nicht passt, keine allgemeine Beschleunigung.

Wer das Maximum aus einer Karte herausholen will, muss messen statt annehmen. Die Zahlen aus dem Strata-Vergleich sind deutlich: 101 Token pro Sekunde gegen 43 bei einem Modell, das vollständig in den Speicher passt, und 3,4 statt 9,8 Sekunden bis zum ersten Token bei 4.096 Token {{Prefill}}. Sie stammen aus einem Thread, einer Grafikkarte und einem Modell, mit drei Läufen pro Messpunkt und Temperatureinstellung null. Für eine Kaufentscheidung ist das zu wenig, für einen Test auf der eigenen Hardware ist es ein guter Anlass.

Wer auf neue Modelle angewiesen ist, sollte die Merge-Geschwindigkeit beobachten, nicht die Versionsnummer. Der Tag 1.0.0 ändert daran nichts: Was nicht zusammengeführt wird, fehlt in der Bibliothek, egal wie sauber die Schnittstelle versioniert ist.

::: warnung Was die 1.0 nicht bedeutet

Die Versionsnummer sagt nichts über Stabilität im Betrieb. 2.604 offene Issues und eine Maintainer-Gruppe, die im Reddit-Thread um Verstärkung gebeten wird, bleiben bestehen. Der Blogbeitrag selbst nennt als Ziel, die Architektur zu beherrschen und die Codequalität hoch zu halten, nicht, schneller zu werden. Wer Tempo braucht, muss weiterhin Forks vergleichen.

:::

Für die langfristige Planung ist die Verteilung der interessantere Teil des Releases. llama.cpp liegt als Paket für Homebrew, Debian, conda-forge, MacPorts, Winget und als XCFramework für Apple-Plattformen bereit, dazu Container und fertige Archive für Linux, macOS, Windows, Android und iOS. Ein Projekt, das diesen Aufwand betreibt, ist nicht auf dem Rückzug. Es hat nur Konkurrenz bekommen, die schneller ist und dafür schmaler.

## Quellen

- ggml-org: *llama.cpp Release v1.0.0*, 13.11.2026, 10:20 UTC. https://github.com/ggml-org/llama.cpp/releases/tag/v1.0.0
- ggml-org: *llama.cpp v1.0.0: A stronger foundation for the local AI ecosystem*, Hugging Face Blog, 13.11.2026. https://huggingface.co/blog/ggml-org/llama-cpp-v1
- GitHub-API: Repository-Statistik llama.cpp (134.862 Sterne, 25.553 Forks, 2.604 offene Issues, 447 Beitragende), abgerufen 13.11.2026. https://api.github.com/repos/ggml-org/llama.cpp
- GitHub: *dory support for llama.cpp*, Pull Request 30306, geöffnet 10.10.2026. https://github.com/ggml-org/llama.cpp/pull/30306
- Reddit r/LocalLLaMA: *llama.cpp v1.0 is here*, 744 Punkte, 90 Kommentare, 13.11.2026. https://reddit.com/comments/1xv8t2e
- GitHub: *Community benchmark: Strata 0.1.41 vs llama.cpp's new MoE cache*, Issue 3082, 13.11.2026. https://github.com/Niko1221/Strata/issues/3082
- tokenbuffalo: *Three 3060s, 250K context*, 2.10.2026 (Vergleich 125B-MoE, llama.cpp gegen Strata). https://tokenbuffalo.blog/2026/10/02/three-3060s-250k-context/
