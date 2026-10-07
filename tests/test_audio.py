import contextlib
import importlib.machinery
import importlib.util
import io
import json
import os
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest

# Load blogctl dynamically
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOGCTL_PATH = os.path.join(REPO_ROOT, "blogctl")

loader = importlib.machinery.SourceFileLoader("blogctl", BLOGCTL_PATH)
spec = importlib.util.spec_from_loader("blogctl", loader)
blogctl = importlib.util.module_from_spec(spec)
sys.modules["blogctl"] = blogctl
loader.exec_module(blogctl)


class BlogAudioTestCase(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.mkdtemp(prefix="blogaudio-test-")

        self.orig_root = blogctl.ROOT
        self.orig_content = blogctl.CONTENT
        self.orig_drafts = blogctl.DRAFTS
        self.orig_posts = blogctl.POSTS
        self.orig_site_json = blogctl.SITE_JSON
        self.orig_audio_dir = getattr(blogctl, "AUDIO_DIR", os.path.join(blogctl.CONTENT, "audio"))
        self.orig_audio_cache = getattr(blogctl, "AUDIO_CACHE", os.path.join(blogctl.ROOT, ".audio-cache"))
        self.orig_tts_cmd_env = os.environ.get("BLOGCTL_TTS_CMD")

        # Redirect blogctl paths to sandbox
        blogctl.ROOT = self.tmpdir
        blogctl.CONTENT = os.path.join(self.tmpdir, "content")
        blogctl.DRAFTS = os.path.join(blogctl.CONTENT, "drafts")
        blogctl.POSTS = os.path.join(blogctl.CONTENT, "posts")
        blogctl.SITE_JSON = os.path.join(blogctl.CONTENT, "site.json")
        blogctl.AUDIO_DIR = os.path.join(blogctl.CONTENT, "audio")
        blogctl.AUDIO_CACHE = os.path.join(self.tmpdir, ".audio-cache")
        os.environ["BLOGCTL_ROOT"] = self.tmpdir

        os.makedirs(blogctl.POSTS, exist_ok=True)
        os.makedirs(blogctl.DRAFTS, exist_ok=True)
        os.makedirs(blogctl.AUDIO_DIR, exist_ok=True)

        # Set up fake TTS script
        self.tts_log_path = os.path.join(self.tmpdir, "tts.log")
        self.fake_tts_path = os.path.join(self.tmpdir, "fake-tts.sh")
        script_content = (
            "#!/bin/sh\n"
            "echo \"$1\" >> \"" + self.tts_log_path + "\"\n"
            "ffmpeg -y -f lavfi -i sine=frequency=440:duration=2 -ac 1 -ar 24000 \"$2\" >/dev/null 2>&1\n"
        )
        with open(self.fake_tts_path, "w", encoding="utf-8") as f:
            f.write(script_content)
        st = os.stat(self.fake_tts_path)
        os.chmod(self.fake_tts_path, st.st_mode | stat.S_IEXEC)
        os.environ["BLOGCTL_TTS_CMD"] = self.fake_tts_path

    def tearDown(self):
        blogctl.ROOT = self.orig_root
        blogctl.CONTENT = self.orig_content
        blogctl.DRAFTS = self.orig_drafts
        blogctl.POSTS = self.orig_posts
        blogctl.SITE_JSON = self.orig_site_json
        blogctl.AUDIO_DIR = self.orig_audio_dir
        blogctl.AUDIO_CACHE = self.orig_audio_cache
        if self.orig_tts_cmd_env is not None:
            os.environ["BLOGCTL_TTS_CMD"] = self.orig_tts_cmd_env
        else:
            os.environ.pop("BLOGCTL_TTS_CMD", None)
        os.environ.pop("BLOGCTL_ROOT", None)
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    def run_cli(self, argv):
        out_buf = io.StringIO()
        err_buf = io.StringIO()
        with contextlib.redirect_stdout(out_buf), contextlib.redirect_stderr(err_buf):
            code = blogctl.main(argv)
        return code, out_buf.getvalue(), err_buf.getvalue()

    def create_post(self, post_id, fm_extra=None, body="Inhalt des Artikels."):
        fm = {
            "title": f"Test {post_id}",
            "slug": post_id,
            "date": "2026-10-04",
            "status": "published",
            "tags": ["news"],
            "summary": f"Zusammenfassung fuer {post_id}",
            "cover": "",
            "source_url": "",
            "source_name": "",
            "lang": "de",
        }
        if fm_extra:
            fm.update(fm_extra)
        path = os.path.join(blogctl.POSTS, f"{post_id}.md")
        blogctl.write_article(path, fm, body)
        return path

    # 1. audio <id> mit vorhandener .txt erzeugt .mp3 + .json, Status ok, seconds > 0, chunks == erwartet, .txt bleibt unverändert.
    def test_1_audio_creates_mp3_and_json(self):
        self.create_post("test-artikel")
        p1 = "Erster Absatz fuer die Hoerfassung. " + ("Text " * 200).strip()
        p2 = "Zweiter Absatz fuer die Hoerfassung. " + ("Mehr " * 200).strip()
        script_text = p1 + "\n\n" + p2
        txt_path = os.path.join(blogctl.AUDIO_DIR, "test-artikel.txt")
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(script_text)

        code, out, err = self.run_cli(["audio", "test-artikel"])
        self.assertEqual(code, 0, f"audio command failed: stderr={err}, stdout={out}")

        mp3_path = os.path.join(blogctl.AUDIO_DIR, "test-artikel.mp3")
        json_path = os.path.join(blogctl.AUDIO_DIR, "test-artikel.json")
        self.assertTrue(os.path.isfile(mp3_path), "MP3-Datei wurde nicht erzeugt")
        self.assertTrue(os.path.isfile(json_path), "JSON-Datei wurde nicht erzeugt")

        # Check MP3 size > 5KB
        self.assertGreaterEqual(os.path.getsize(mp3_path), 5000)

        # Check JSON content
        with open(json_path, "r", encoding="utf-8") as f:
            meta = json.load(f)

        self.assertEqual(meta["id"], "test-artikel")
        self.assertEqual(meta["engine"], "voxcpm2")
        self.assertEqual(meta["backend"], "voxcpm2-tts")
        self.assertEqual(meta["chunks"], 2)
        self.assertGreater(meta["seconds"], 0)
        self.assertEqual(meta["chars"], len(script_text))
        self.assertEqual(meta["words"], len(script_text.split()))
        self.assertEqual(meta["bytes"], os.path.getsize(mp3_path))
        self.assertIn("created", meta)

        # .txt remains unchanged
        with open(txt_path, "r", encoding="utf-8") as f:
            self.assertEqual(f.read(), script_text)

        # Output text check
        self.assertIn("test-artikel: ok", out)

    # 2. Fehlende .txt ohne --derive → Exit 1, Fehlermeldung nennt den Pfad content/audio/<id>.txt.
    def test_2_missing_txt_without_derive_exits_1(self):
        self.create_post("ohne-audio")
        code, out, err = self.run_cli(["audio", "ohne-audio"])
        self.assertEqual(code, 1)
        expected_rel_path = os.path.join("content", "audio", "ohne-audio.txt")
        self.assertIn(expected_rel_path, err)
        self.assertIn("--derive", err)
        mp3_path = os.path.join(blogctl.AUDIO_DIR, "ohne-audio.mp3")
        json_path = os.path.join(blogctl.AUDIO_DIR, "ohne-audio.json")
        self.assertFalse(os.path.exists(mp3_path))
        self.assertFalse(os.path.exists(json_path))

    # 3. --derive erzeugt .txt aus dem Artikel: erster Absatz = summary; {{chart:…}}, Links-URLs, ##-Zeichen und {{…}}-Marker kommen im Text nicht mehr vor.
    def test_3_derive_creates_clean_script(self):
        body = (
            "## TL;DR\n\n"
            "- Erster wichtiger Punkt ([Quelle](https://example.com/tldr)) über ein {{Sprachmodell}}.\n"
            "- Zweiter wichtiger Punkt ohne Link.\n\n"
            "## Hintergrund\n\n"
            "Hier ist ein Absatz mit einem Diagramm:\n\n"
            "{{chart:test-diagramm}}\n\n"
            "Und einer Tabelle:\n"
            "| Spalte 1 | Spalte 2 |\n"
            "| --- | --- |\n"
            "| Wert A | Wert B |\n\n"
            "## Details\n\n"
            "Mehr Text mit einem [Link](https://example.com/details) und einem direkten Link https://example.com/plain sowie {{Fachbegriff}}.\n"
        )
        self.create_post("derive-artikel", {"summary": "Zusammenfassung des Test-Artikels."}, body=body)

        code, out, err = self.run_cli(["audio", "derive-artikel", "--derive"])
        self.assertEqual(code, 0, f"Fehler bei audio --derive: stderr={err}, stdout={out}")

        txt_path = os.path.join(blogctl.AUDIO_DIR, "derive-artikel.txt")
        self.assertTrue(os.path.isfile(txt_path), ".txt wurde durch --derive nicht erzeugt")
        with open(txt_path, "r", encoding="utf-8") as f:
            derived_content = f.read()

        paragraphs = [p.strip() for p in derived_content.strip().split("\n\n") if p.strip()]
        self.assertGreaterEqual(len(paragraphs), 3)

        # Erster Absatz == summary
        self.assertEqual(paragraphs[0], "Zusammenfassung des Test-Artikels.")

        # Keine URLs, keine Marker, keine ##, kein {{chart:}}
        self.assertNotIn("https://", derived_content)
        self.assertNotIn("http://", derived_content)
        self.assertNotIn("{{chart:", derived_content)
        self.assertNotIn("{{", derived_content)
        self.assertNotIn("}}", derived_content)
        self.assertNotIn("##", derived_content)
        self.assertNotIn("|", derived_content)

        # Begriff und Fachbegriff sind ohne geschweifte Klammern erhalten
        self.assertIn("Sprachmodell", derived_content)
        self.assertIn("Fachbegriff", derived_content)
        self.assertIn("Quelle", derived_content)

    # 4. Zweiter Lauf ohne --force → status: skipped, Cache-Dateien unverändert (mtime), Fake-TTS wurde nicht erneut aufgerufen.
    def test_4_second_run_without_force_skips_and_does_not_call_tts(self):
        self.create_post("skip-artikel")
        txt_path = os.path.join(blogctl.AUDIO_DIR, "skip-artikel.txt")
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write("Ein kurzer Text für den Skip-Test.")

        # Erstlauf
        code, out, err = self.run_cli(["audio", "skip-artikel"])
        self.assertEqual(code, 0, f"Erstlauf fehlgeschlagen: {err}")

        mp3_path = os.path.join(blogctl.AUDIO_DIR, "skip-artikel.mp3")
        cache_chunk = os.path.join(blogctl.AUDIO_CACHE, "skip-artikel", "001.mp3")
        self.assertTrue(os.path.isfile(mp3_path))
        self.assertTrue(os.path.isfile(cache_chunk))

        mp3_mtime = os.path.getmtime(mp3_path)
        cache_mtime = os.path.getmtime(cache_chunk)

        with open(self.tts_log_path, "r", encoding="utf-8") as f:
            tts_calls_first = len(f.readlines())
        self.assertGreater(tts_calls_first, 0)

        # Zweitlauf ohne --force
        code, out, err = self.run_cli(["audio", "skip-artikel"])
        self.assertEqual(code, 0, f"Zweitlauf fehlgeschlagen: {err}")
        self.assertIn("skip-artikel: übersprungen (aktuell)", out)

        self.assertEqual(os.path.getmtime(mp3_path), mp3_mtime)
        self.assertEqual(os.path.getmtime(cache_chunk), cache_mtime)

        with open(self.tts_log_path, "r", encoding="utf-8") as f:
            tts_calls_second = len(f.readlines())
        self.assertEqual(tts_calls_first, tts_calls_second, "Fake-TTS darf bei skipped nicht aufgerufen werden")

    # 5. --force → wird neu gebaut, Fake-TTS wird erneut aufgerufen.
    def test_5_force_rebuilds_and_calls_tts(self):
        self.create_post("force-artikel")
        txt_path = os.path.join(blogctl.AUDIO_DIR, "force-artikel.txt")
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write("Ein kurzer Text für den Force-Test.")

        # Erstlauf
        code, out, err = self.run_cli(["audio", "force-artikel"])
        self.assertEqual(code, 0)
        with open(self.tts_log_path, "r", encoding="utf-8") as f:
            tts_calls_first = len(f.readlines())
        self.assertGreater(tts_calls_first, 0)

        # Zweitlauf mit --force
        code, out, err = self.run_cli(["audio", "force-artikel", "--force"])
        self.assertEqual(code, 0)
        self.assertIn("force-artikel: ok", out)
        with open(self.tts_log_path, "r", encoding="utf-8") as f:
            tts_calls_second = len(f.readlines())
        self.assertGreater(tts_calls_second, tts_calls_first, "Fake-TTS muss bei --force erneut aufgerufen werden")

    # 6. Cache-Teilnutzung: Cache-Verzeichnis mit einer fehlenden Abschnittsdatei füllen → nur dieser Abschnitt wird neu erzeugt (Zähler im Fake-TTS-Log).
    def test_6_partial_cache_synthesizes_only_missing_chunk(self):
        self.create_post("partial-cache")
        p1 = "Erster langer Absatz für Abschnitt eins. " + ("Eins " * 200).strip()
        p2 = "Zweiter langer Absatz für Abschnitt zwei. " + ("Zwei " * 200).strip()
        txt_path = os.path.join(blogctl.AUDIO_DIR, "partial-cache.txt")
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(p1 + "\n\n" + p2)

        # Erstlauf erzeugt 001.mp3 und 002.mp3
        code, out, err = self.run_cli(["audio", "partial-cache"])
        self.assertEqual(code, 0)

        cache_dir = os.path.join(blogctl.AUDIO_CACHE, "partial-cache")
        c1 = os.path.join(cache_dir, "001.mp3")
        c2 = os.path.join(cache_dir, "002.mp3")
        self.assertTrue(os.path.isfile(c1))
        self.assertTrue(os.path.isfile(c2))

        # Lösche 002.mp3 und das fertige mp3 (damit kein skip greift)
        os.remove(c2)
        final_mp3 = os.path.join(blogctl.AUDIO_DIR, "partial-cache.mp3")
        os.remove(final_mp3)

        c1_mtime_before = os.path.getmtime(c1)

        # TTS-Log leeren
        with open(self.tts_log_path, "w", encoding="utf-8") as f:
            f.write("")

        # Lauf mit fehlendem Abschnitt 2
        code, out, err = self.run_cli(["audio", "partial-cache"])
        self.assertEqual(code, 0, f"Fehler bei partiellem Cache-Lauf: {err}")

        # 001.mp3 muss unberührt geblieben sein
        self.assertEqual(os.path.getmtime(c1), c1_mtime_before)

        # 002.mp3 muss neu erzeugt worden sein
        self.assertTrue(os.path.isfile(c2))

        # Fake-TTS darf genau 1-mal aufgerufen worden sein
        with open(self.tts_log_path, "r", encoding="utf-8") as f:
            tts_calls = len(f.readlines())
        self.assertEqual(tts_calls, 1, f"Erwartet genau 1 TTS-Aufruf fuer den fehlenden Chunk, erhalten: {tts_calls}")

    # 7. --all verarbeitet nur content/posts/, meldet missing für Artikel ohne .txt und bricht nicht ab; Exit 0.
    def test_7_all_processes_only_posts_and_reports_missing(self):
        # 1 Draft mit .txt (darf von --all ignoriert werden)
        draft_path = os.path.join(blogctl.DRAFTS, "draft-artikel.md")
        blogctl.write_article(draft_path, {"title": "Draft", "slug": "draft-artikel", "date": "2026-10-01", "status": "draft", "lang": "de"}, "Draft Body")
        with open(os.path.join(blogctl.AUDIO_DIR, "draft-artikel.txt"), "w", encoding="utf-8") as f:
            f.write("Draft Audio Text")

        # 1 Post mit .txt
        self.create_post("post-mit-audio", {"date": "2026-10-02"})
        with open(os.path.join(blogctl.AUDIO_DIR, "post-mit-audio.txt"), "w", encoding="utf-8") as f:
            f.write("Post Audio Text")

        # 1 Post ohne .txt
        self.create_post("post-ohne-audio", {"date": "2026-10-03"})

        code, out, err = self.run_cli(["audio", "--all", "--json"])
        self.assertEqual(code, 0, f"--all fehlgeschlagen: stderr={err}, stdout={out}")

        data = json.loads(out)
        self.assertTrue(data.get("ok"))
        self.assertIn("post-ohne-audio", data.get("missing", []))
        self.assertNotIn("post-mit-audio", data.get("missing", []))

        # Warnung in stderr
        self.assertIn("post-ohne-audio.txt", err)

        # post-mit-audio erzeugt
        self.assertTrue(os.path.isfile(os.path.join(blogctl.AUDIO_DIR, "post-mit-audio.mp3")))
        # post-ohne-audio nicht erzeugt
        self.assertFalse(os.path.isfile(os.path.join(blogctl.AUDIO_DIR, "post-ohne-audio.mp3")))
        # draft-artikel nicht erzeugt
        self.assertFalse(os.path.isfile(os.path.join(blogctl.AUDIO_DIR, "draft-artikel.mp3")))

    # 8. Abschnitts-Aufteilung: Absatz > chunk_chars wird an Satzgrenzen geteilt, jeder Abschnitt <= chunk_chars (bis auf den harten Notfall), Reihenfolge bleibt erhalten.
    def test_8_chunking_splits_at_sentence_boundaries(self):
        s1 = "Das ist der erste Satz."
        s2 = "Hier folgt der zweite Satz, der etwas ausfuehrlicher formuliert ist."
        s3 = "Und hier kommt der dritte Satz zum Abschluss."
        long_para = f"{s1} {s2} {s3}"
        # Set chunk_chars so that s1 fits, but s1 + s2 exceeds chunk_chars
        chunk_limit = 80
        chunks = blogctl.chunk_text(long_para, chunk_chars=chunk_limit)
        self.assertGreater(len(chunks), 1)
        for c in chunks:
            self.assertLessEqual(len(c), chunk_limit, f"Abschnitt zu lang: '{c}' ({len(c)} > {chunk_limit})")

        # Prüfe Reihenfolge
        joined = " ".join(chunks)
        self.assertIn("erste Satz", chunks[0])
        self.assertIn("dritte Satz", chunks[-1])

        # Test harter Notfall: Einzelner Satz laenger als chunk_limit
        giant_sentence = "Wort" * 30 + "."  # 121 Zeichen
        emergency_chunks = blogctl.chunk_text(giant_sentence, chunk_chars=50)
        self.assertGreater(len(emergency_chunks), 2)
        for c in emergency_chunks:
            self.assertLessEqual(len(c), 50)
        self.assertEqual("".join(emergency_chunks), giant_sentence)

    # 9. --json-Struktur wie oben; Fehlerfall liefert ok: false + error und Exit 1.
    def test_9_json_structure_success_and_error(self):
        # 1. Erfolgsfall
        self.create_post("json-erfolg")
        with open(os.path.join(blogctl.AUDIO_DIR, "json-erfolg.txt"), "w", encoding="utf-8") as f:
            f.write("Text fuer JSON-Erfolgsfall.")

        code, out, err = self.run_cli(["audio", "json-erfolg", "--json"])
        self.assertEqual(code, 0, f"JSON-Erfolg fehlgeschlagen: stderr={err}")
        data = json.loads(out)
        self.assertTrue(data.get("ok"))
        self.assertEqual(data.get("missing"), [])
        self.assertEqual(len(data.get("audio", [])), 1)
        item = data["audio"][0]
        for key in ("id", "mp3", "script", "seconds", "bytes", "chars", "words", "chunks", "engine", "status"):
            self.assertIn(key, item, f"Key '{key}' fehlt im audio JSON-Objekt")
        self.assertEqual(item["status"], "ok")

        # 2. Fehlerfall: fehlendes .txt ohne --derive
        self.create_post("json-fehler")
        code_err, out_err, err_err = self.run_cli(["audio", "json-fehler", "--json"])
        self.assertEqual(code_err, 1)
        data_err = json.loads(out_err)
        self.assertFalse(data_err.get("ok"))
        self.assertIn("error", data_err)
        self.assertIn("content/audio/json-fehler.txt", data_err["error"])
        self.assertIn("audio", data_err)
        self.assertIn("missing", data_err)

    # 10. Unbekannte Engine → Exit 1 mit Liste der bekannten Engines.
    def test_10_unknown_engine_exits_1_with_known_engines(self):
        self.create_post("eng-test")
        with open(os.path.join(blogctl.AUDIO_DIR, "eng-test.txt"), "w", encoding="utf-8") as f:
            f.write("Text fuer Engine-Test.")

        code, out, err = self.run_cli(["audio", "eng-test", "--engine", "nichtvorhanden"])
        self.assertEqual(code, 1)
        self.assertIn("Unbekannte Engine 'nichtvorhanden'", err)
        self.assertIn("voxcpm2", err)
        self.assertIn("qwen3", err)

    # 11. Fehlendes BLOGCTL_TTS_CMD/nicht ausführbar → klarer Fehler, kein Absturz, kein halbfertiges .mp3 (Exit 1).
    def test_11_missing_or_nonexecutable_tts_cmd_exits_1(self):
        self.create_post("tts-fail")
        with open(os.path.join(blogctl.AUDIO_DIR, "tts-fail.txt"), "w", encoding="utf-8") as f:
            f.write("Text fuer fehlschlagendes TTS.")

        # 1. Datei existiert gar nicht
        os.environ["BLOGCTL_TTS_CMD"] = os.path.join(self.tmpdir, "does_not_exist.sh")
        code, out, err = self.run_cli(["audio", "tts-fail"])
        self.assertEqual(code, 1)
        self.assertIn("TTS-Befehl nicht gefunden oder nicht ausführbar", err)
        mp3_path = os.path.join(blogctl.AUDIO_DIR, "tts-fail.mp3")
        tmp_path = os.path.join(blogctl.AUDIO_DIR, "tts-fail.mp3.tmp")
        self.assertFalse(os.path.exists(mp3_path))
        self.assertFalse(os.path.exists(tmp_path))

        # 2. Datei existiert, ist aber nicht ausführbar
        non_exec_path = os.path.join(self.tmpdir, "non_exec.sh")
        with open(non_exec_path, "w", encoding="utf-8") as f:
            f.write("#!/bin/sh\necho hi\n")
        os.chmod(non_exec_path, 0o644)
        os.environ["BLOGCTL_TTS_CMD"] = non_exec_path

        code2, out2, err2 = self.run_cli(["audio", "tts-fail"])
        self.assertEqual(code2, 1)
        self.assertIn("TTS-Befehl nicht gefunden oder nicht ausführbar", err2)
        self.assertFalse(os.path.exists(mp3_path))
        self.assertFalse(os.path.exists(tmp_path))

    # 12. --script DATEI: übernimmt den Inhalt und speichert ihn als content/audio/<id>.txt
    def test_12_script_flag_copies_file_to_audio_txt(self):
        self.create_post("custom-script-post")
        ext_script = os.path.join(self.tmpdir, "external_script.txt")
        custom_text = "Externer Sprechtext, der übernommen werden soll."
        with open(ext_script, "w", encoding="utf-8") as f:
            f.write(custom_text)

        code, out, err = self.run_cli(["audio", "custom-script-post", "--script", ext_script])
        self.assertEqual(code, 0, f"--script fehlgeschlagen: {err}")

        txt_path = os.path.join(blogctl.AUDIO_DIR, "custom-script-post.txt")
        self.assertTrue(os.path.isfile(txt_path))
        with open(txt_path, "r", encoding="utf-8") as f:
            self.assertEqual(f.read(), custom_text)

        mp3_path = os.path.join(blogctl.AUDIO_DIR, "custom-script-post.mp3")
        self.assertTrue(os.path.isfile(mp3_path))

    # 13. audio.enabled = false in content/site.json bricht sofort mit Exit 1 ab, ohne etwas zu erzeugen.
    def test_13_audio_disabled_in_site_json_exits_1(self):
        # site.json mit audio.enabled = false schreiben
        site_cfg = {
            "title": "Test Blog",
            "audio": {
                "enabled": False,
            },
        }
        with open(blogctl.SITE_JSON, "w", encoding="utf-8") as f:
            json.dump(site_cfg, f)

        self.create_post("post-disabled")
        txt_path = os.path.join(blogctl.AUDIO_DIR, "post-disabled.txt")
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write("Audio Text für deaktivierten Artikel.")

        expected_msg = "Hörfassungen sind in content/site.json deaktiviert (audio.enabled = false)"

        # Aufruf mit Einzel-ID
        code, out, err = self.run_cli(["audio", "post-disabled"])
        self.assertEqual(code, 1)
        self.assertIn(expected_msg, err)

        mp3_path = os.path.join(blogctl.AUDIO_DIR, "post-disabled.mp3")
        json_path = os.path.join(blogctl.AUDIO_DIR, "post-disabled.json")
        self.assertFalse(os.path.exists(mp3_path))
        self.assertFalse(os.path.exists(json_path))

        # Aufruf mit --all
        code_all, out_all, err_all = self.run_cli(["audio", "--all"])
        self.assertEqual(code_all, 1)
        self.assertIn(expected_msg, err_all)
        self.assertFalse(os.path.exists(mp3_path))

        # Aufruf mit --json
        code_json, out_json, err_json = self.run_cli(["audio", "post-disabled", "--json"])
        self.assertEqual(code_json, 1)
        data_json = json.loads(out_json)
        self.assertFalse(data_json.get("ok"))
        self.assertIn(expected_msg, data_json.get("error", ""))

    # 14. --all mit drei Artikeln, mittlerer scheitert: die anderen beiden werden erzeugt, Exit 0, Warnung auf stderr, status: error
    def test_14_all_continues_on_failure_and_reports_error(self):
        self.create_post("art-1")
        self.create_post("art-2")
        self.create_post("art-3")

        with open(os.path.join(blogctl.AUDIO_DIR, "art-1.txt"), "w", encoding="utf-8") as f:
            f.write("Text fuer Artikel 1.")
        with open(os.path.join(blogctl.AUDIO_DIR, "art-2.txt"), "w", encoding="utf-8") as f:
            f.write("Text fuer Artikel 2 FAIL.")
        with open(os.path.join(blogctl.AUDIO_DIR, "art-3.txt"), "w", encoding="utf-8") as f:
            f.write("Text fuer Artikel 3.")

        # Fake-TTS Skript, das fuer art-2 (bzw. bei 'FAIL') einen Fehler wirft
        fail_tts_path = os.path.join(self.tmpdir, "fake-tts-fail2.sh")
        script_content = (
            "#!/bin/sh\n"
            "if grep -q 'FAIL' \"$1\"; then\n"
            "    echo 'Synthesefehler im Fake-TTS' >&2\n"
            "    exit 1\n"
            "fi\n"
            "ffmpeg -y -f lavfi -i sine=frequency=440:duration=2 -ac 1 -ar 24000 \"$2\" >/dev/null 2>&1\n"
        )
        with open(fail_tts_path, "w", encoding="utf-8") as f:
            f.write(script_content)
        os.chmod(fail_tts_path, 0o755)
        os.environ["BLOGCTL_TTS_CMD"] = fail_tts_path

        # 1. Test mit --json
        code, out, err = self.run_cli(["audio", "--all", "--json"])
        self.assertEqual(code, 0, f"--all muss Exit 0 liefern wenn mind. 1 Artikel erfolgreich war. err={err}")

        # Warnung auf stderr
        self.assertIn("Warnung: art-2 übersprungen:", err)

        # Dateien 1 und 3 existieren, 2 nicht
        self.assertTrue(os.path.isfile(os.path.join(blogctl.AUDIO_DIR, "art-1.mp3")))
        self.assertTrue(os.path.isfile(os.path.join(blogctl.AUDIO_DIR, "art-1.json")))
        self.assertFalse(os.path.exists(os.path.join(blogctl.AUDIO_DIR, "art-2.mp3")))
        self.assertFalse(os.path.exists(os.path.join(blogctl.AUDIO_DIR, "art-2.json")))
        self.assertTrue(os.path.isfile(os.path.join(blogctl.AUDIO_DIR, "art-3.mp3")))
        self.assertTrue(os.path.isfile(os.path.join(blogctl.AUDIO_DIR, "art-3.json")))

        # JSON-Auswertung
        data = json.loads(out)
        self.assertTrue(data.get("ok"))
        audio_items = {item["id"]: item for item in data.get("audio", [])}
        self.assertEqual(len(audio_items), 3)
        self.assertEqual(audio_items["art-1"]["status"], "ok")
        self.assertEqual(audio_items["art-2"]["status"], "error")
        self.assertIn("error", audio_items["art-2"])
        self.assertIn("Synthesefehler im Fake-TTS", audio_items["art-2"]["error"])
        self.assertEqual(audio_items["art-3"]["status"], "ok")

        # 2. Test ohne --json (Summenzeile pruefen)
        os.remove(os.path.join(blogctl.AUDIO_DIR, "art-1.mp3"))
        os.remove(os.path.join(blogctl.AUDIO_DIR, "art-3.mp3"))
        code_txt, out_txt, err_txt = self.run_cli(["audio", "--all", "--force"])
        self.assertEqual(code_txt, 0)
        self.assertIn("audio: 2 erzeugt, 0 übersprungen, 1 fehlgeschlagen, 0 fehlend", out_txt)

    # 15. --all, wenn alle scheitern: Exit 1, ok: false
    def test_15_all_fails_when_all_articles_fail(self):
        self.create_post("fail-1")
        self.create_post("fail-2")
        with open(os.path.join(blogctl.AUDIO_DIR, "fail-1.txt"), "w", encoding="utf-8") as f:
            f.write("Text fuer Fail 1.")
        with open(os.path.join(blogctl.AUDIO_DIR, "fail-2.txt"), "w", encoding="utf-8") as f:
            f.write("Text fuer Fail 2.")

        always_fail_path = os.path.join(self.tmpdir, "always-fail.sh")
        with open(always_fail_path, "w", encoding="utf-8") as f:
            f.write("#!/bin/sh\necho 'TTS Totalausfall' >&2\nexit 1\n")
        os.chmod(always_fail_path, 0o755)
        os.environ["BLOGCTL_TTS_CMD"] = always_fail_path

        # 1. Mit --json
        code_json, out_json, err_json = self.run_cli(["audio", "--all", "--json"])
        self.assertEqual(code_json, 1, f"--all muss Exit 1 liefern wenn alle scheitern. err={err_json}")
        data = json.loads(out_json)
        self.assertFalse(data.get("ok"))
        self.assertEqual(len(data.get("audio", [])), 2)
        for item in data["audio"]:
            self.assertEqual(item["status"], "error")
            self.assertIn("TTS Totalausfall", item.get("error", ""))

        # 2. Ohne --json
        code_txt, out_txt, err_txt = self.run_cli(["audio", "--all"])
        self.assertEqual(code_txt, 1)
        self.assertIn("audio: 0 erzeugt, 0 übersprungen, 2 fehlgeschlagen, 0 fehlend", out_txt)

    # 16. audio <id> mit expliziter ID, die scheitert: unverändert Exit 1 mit Fehlermeldung.
    def test_16_explicit_id_failure_exits_1(self):
        self.create_post("explicit-fail")
        with open(os.path.join(blogctl.AUDIO_DIR, "explicit-fail.txt"), "w", encoding="utf-8") as f:
            f.write("Text fuer expliziten Fehler-Test.")

        fail_script_path = os.path.join(self.tmpdir, "explicit-fail.sh")
        with open(fail_script_path, "w", encoding="utf-8") as f:
            f.write("#!/bin/sh\necho 'TTS Engine gecrashed' >&2\nexit 1\n")
        os.chmod(fail_script_path, 0o755)
        os.environ["BLOGCTL_TTS_CMD"] = fail_script_path

        # Ohne --json
        code, out, err = self.run_cli(["audio", "explicit-fail"])
        self.assertEqual(code, 1)
        self.assertIn("Fehler: Synthese fehlgeschlagen für explicit-fail", err)
        self.assertIn("TTS Engine gecrashed", err)

        mp3_path = os.path.join(blogctl.AUDIO_DIR, "explicit-fail.mp3")
        json_path = os.path.join(blogctl.AUDIO_DIR, "explicit-fail.json")
        self.assertFalse(os.path.exists(mp3_path))
        self.assertFalse(os.path.exists(json_path))

        # Mit --json
        code_json, out_json, err_json = self.run_cli(["audio", "explicit-fail", "--json"])
        self.assertEqual(code_json, 1)
        data = json.loads(out_json)
        self.assertFalse(data.get("ok"))
        self.assertIn("TTS Engine gecrashed", data.get("error", ""))


if __name__ == "__main__":
    unittest.main()
