import contextlib
import hashlib
import importlib.machinery
import importlib.util
import io
import os
import shutil
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


class BlogTimeTestCase(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.mkdtemp(prefix="blogtime-test-")
        self.orig_root = blogctl.ROOT
        self.orig_content = blogctl.CONTENT
        self.orig_drafts = blogctl.DRAFTS
        self.orig_posts = blogctl.POSTS
        self.orig_pages = blogctl.PAGES
        self.orig_assets = blogctl.ASSETS
        self.orig_templates = blogctl.TEMPLATES
        self.orig_site_json = blogctl.SITE_JSON
        self.orig_source_json = blogctl.SOURCE_JSON

        # Redirect blogctl paths to sandbox
        blogctl.ROOT = self.tmpdir
        blogctl.CONTENT = os.path.join(self.tmpdir, "content")
        blogctl.DRAFTS = os.path.join(blogctl.CONTENT, "drafts")
        blogctl.POSTS = os.path.join(blogctl.CONTENT, "posts")
        blogctl.PAGES = os.path.join(blogctl.CONTENT, "pages")
        blogctl.ASSETS = os.path.join(self.tmpdir, "assets")
        blogctl.TEMPLATES = os.path.join(blogctl.CONTENT, "templates")
        blogctl.SITE_JSON = os.path.join(blogctl.CONTENT, "site.json")
        blogctl.SOURCE_JSON = os.path.join(blogctl.CONTENT, "sources.json")
        os.environ["BLOGCTL_ROOT"] = self.tmpdir

        # Copy original templates to sandbox
        orig_templates_dir = os.path.join(REPO_ROOT, "content", "templates")
        shutil.copytree(orig_templates_dir, blogctl.TEMPLATES)
        blogctl.ensure_dirs()

    def tearDown(self):
        blogctl.ROOT = self.orig_root
        blogctl.CONTENT = self.orig_content
        blogctl.DRAFTS = self.orig_drafts
        blogctl.POSTS = self.orig_posts
        blogctl.PAGES = self.orig_pages
        blogctl.ASSETS = self.orig_assets
        blogctl.TEMPLATES = self.orig_templates
        blogctl.SITE_JSON = self.orig_site_json
        blogctl.SOURCE_JSON = self.orig_source_json
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
            "tags": ["ki"],
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

    # 1. Artikel mit time: "09:15" -> Startseite, Tag-Seite und Artikelseite enthalten 04.10.2026, 09:15 und datetime="2026-10-04T09:15+02:00"
    def test_1_article_with_time_rendering(self):
        self.create_post("zeit-artikel", {"date": "2026-10-04", "time": "09:15", "tags": ["technik"]})
        dist_dir = os.path.join(self.tmpdir, "dist")
        code, out, err = self.run_cli(["build", "--out", dist_dir])
        self.assertEqual(code, 0, f"build failed: {err}")

        # Startseite
        with open(os.path.join(dist_dir, "index.html"), "r", encoding="utf-8") as f:
            index_html = f.read()
        self.assertIn("04.10.2026, 09:15", index_html)
        self.assertIn('datetime="2026-10-04T09:15+02:00"', index_html)

        # Tag-Seite
        with open(os.path.join(dist_dir, "tag", "technik.html"), "r", encoding="utf-8") as f:
            tag_html = f.read()
        self.assertIn("04.10.2026, 09:15", tag_html)
        self.assertIn('datetime="2026-10-04T09:15+02:00"', tag_html)

        # Artikelseite
        with open(os.path.join(dist_dir, "zeit-artikel.html"), "r", encoding="utf-8") as f:
            post_html = f.read()
        self.assertIn("04.10.2026, 09:15", post_html)
        self.assertIn('datetime="2026-10-04T09:15+02:00"', post_html)

    # 2. Artikel ohne time -> 04.10.2026 und datetime="2026-10-04"
    def test_2_article_without_time_rendering(self):
        self.create_post("ohne-zeit", {"date": "2026-10-04", "tags": ["allgemein"]})
        dist_dir = os.path.join(self.tmpdir, "dist")
        code, out, err = self.run_cli(["build", "--out", dist_dir])
        self.assertEqual(code, 0, f"build failed: {err}")

        # Startseite
        with open(os.path.join(dist_dir, "index.html"), "r", encoding="utf-8") as f:
            index_html = f.read()
        self.assertIn("04.10.2026", index_html)
        self.assertNotIn("04.10.2026, ", index_html)
        self.assertIn('datetime="2026-10-04"', index_html)

        # Artikelseite
        with open(os.path.join(dist_dir, "ohne-zeit.html"), "r", encoding="utf-8") as f:
            post_html = f.read()
        self.assertIn("04.10.2026", post_html)
        self.assertNotIn("04.10.2026, ", post_html)
        self.assertIn('datetime="2026-10-04"', post_html)

    # 3. Sortierung: gleiches Datum, verschiedene Uhrzeiten -> spaeterer Artikel zuerst
    def test_3_sorting_by_date_and_time(self):
        self.create_post("post-morgens", {"title": "Morgens", "date": "2026-10-04", "time": "09:15"})
        self.create_post("post-mittags", {"title": "Mittags", "date": "2026-10-04", "time": "14:30"})
        self.create_post("post-ohne-zeit", {"title": "Ohne Zeit", "date": "2026-10-04"})

        dist_dir = os.path.join(self.tmpdir, "dist")
        code, out, err = self.run_cli(["build", "--out", dist_dir])
        self.assertEqual(code, 0, f"build failed: {err}")

        with open(os.path.join(dist_dir, "index.html"), "r", encoding="utf-8") as f:
            index_html = f.read()

        pos_mittags = index_html.find("post-mittags.html")
        pos_morgens = index_html.find("post-morgens.html")
        pos_ohne = index_html.find("post-ohne-zeit.html")

        self.assertTrue(pos_mittags != -1 and pos_morgens != -1 and pos_ohne != -1)
        self.assertLess(pos_mittags, pos_morgens, "Mittags (14:30) muss vor Morgens (09:15) sortiert werden")
        self.assertLess(pos_morgens, pos_ohne, "Morgens (09:15) muss vor Ohne Zeit (00:00) sortiert werden")

    # 4. check: time: "25:00" -> Fehler; time: "09:15" -> kein Fehler; ohne time -> kein Fehler
    def test_4_check_time_validation(self):
        # Fall 1: time: "25:00" -> Fehler
        self.create_post("ungueltig", {"date": "2026-10-04", "time": "25:00"})
        code, out, err = self.run_cli(["check"])
        self.assertEqual(code, 1, "check mit time='25:00' muss Exit-Code 1 liefern")
        self.assertIn("FEHLER", out + err)

        # Fall 2: time: "09:15" -> kein Fehler
        os.remove(os.path.join(blogctl.POSTS, "ungueltig.md"))
        self.create_post("gueltig", {"date": "2026-10-04", "time": "09:15"})
        code, out, err = self.run_cli(["check"])
        self.assertEqual(code, 0, f"check mit time='09:15' muss 0 liefern, out: {out}, err: {err}")

        # Fall 3: ohne time -> kein Fehler
        os.remove(os.path.join(blogctl.POSTS, "gueltig.md"))
        self.create_post("ohne-zeit", {"date": "2026-10-04"})
        code, out, err = self.run_cli(["check"])
        self.assertEqual(code, 0, f"check ohne time muss 0 liefern, out: {out}, err: {err}")

    # 5. Feed: pubDate enthaelt 09:15:00 +0200 (Sommerdatum) und analog +0100 (Winterdatum)
    def test_5_feed_pubdate_offsets(self):
        self.create_post("sommer-post", {"date": "2026-10-04", "time": "09:15"})
        self.create_post("winter-post", {"date": "2026-01-15", "time": "09:15"})
        self.create_post("ohne-zeit-sommer", {"date": "2026-07-01"})

        dist_dir = os.path.join(self.tmpdir, "dist")
        code, out, err = self.run_cli(["build", "--out", dist_dir])
        self.assertEqual(code, 0, f"build failed: {err}")

        with open(os.path.join(dist_dir, "feed.xml"), "r", encoding="utf-8") as f:
            feed_xml = f.read()

        self.assertIn("Sun, 04 Oct 2026 09:15:00 +0200", feed_xml)
        self.assertIn("Thu, 15 Jan 2026 09:15:00 +0100", feed_xml)
        self.assertIn("Wed, 01 Jul 2026 00:00:00 +0200", feed_xml)

    # 6. new --time 09:15 schreibt das Feld ins Frontmatter, edit --time "" entfernt es wieder, --time 25:00 wird abgelehnt (Exit 1)
    def test_6_cli_new_and_edit_time(self):
        # new --time 09:15
        code, out, err = self.run_cli(["new", "--title", "Neuer Post", "--slug", "neuer-post", "--time", "09:15"])
        self.assertEqual(code, 0, f"new mit --time 09:15 fehlgeschlagen: {err}")
        draft_path = os.path.join(blogctl.DRAFTS, "neuer-post.md")
        fm, _ = blogctl.read_article(draft_path)
        self.assertEqual(fm.get("time"), "09:15")
        with open(draft_path, "r", encoding="utf-8") as f:
            raw_text = f.read()
        self.assertRegex(raw_text, r"date:\s*[^\n]+\ntime:\s*\"09:15\"", "time muss direkt nach date stehen")

        # edit --time ""
        code, out, err = self.run_cli(["edit", "neuer-post", "--time", ""])
        self.assertEqual(code, 0, f"edit mit --time '' fehlgeschlagen: {err}")
        fm, _ = blogctl.read_article(draft_path)
        self.assertNotIn("time", fm)

        # new --time 25:00 wird abgelehnt
        code, out, err = self.run_cli(["new", "--title", "Ungueltig", "--time", "25:00"])
        self.assertEqual(code, 1, "new mit ungueltiger time muss Exit-Code 1 liefern")

        # edit --time 25:00 wird abgelehnt
        code, out, err = self.run_cli(["edit", "neuer-post", "--time", "25:00"])
        self.assertEqual(code, 1, "edit mit ungueltiger time muss Exit-Code 1 liefern")

    # 7. Determinismus: zwei Builds hintereinander -> identische Dateien (Vergleich per Hash)
    def test_7_determinism(self):
        self.create_post("det-post-1", {"date": "2026-10-04", "time": "09:15"})
        self.create_post("det-post-2", {"date": "2026-10-03"})

        dist1 = os.path.join(self.tmpdir, "dist1")
        dist2 = os.path.join(self.tmpdir, "dist2")

        code1, _, _ = self.run_cli(["build", "--out", dist1])
        code2, _, _ = self.run_cli(["build", "--out", dist2])
        self.assertEqual(code1, 0)
        self.assertEqual(code2, 0)

        def dir_hashes(base_dir):
            hashes = {}
            for root, _, files in os.walk(base_dir):
                for fname in sorted(files):
                    fpath = os.path.join(root, fname)
                    rel = os.path.relpath(fpath, base_dir)
                    with open(fpath, "rb") as f:
                        hashes[rel] = hashlib.sha256(f.read()).hexdigest()
            return hashes

        hashes1 = dir_hashes(dist1)
        hashes2 = dir_hashes(dist2)
        self.assertEqual(hashes1, hashes2, "Beide Builds muessen byte-identisch sein")

    # 8. Feed-/Scrape-Parser
    def test_8_feed_scrape_parser(self):
        parser_func = getattr(blogctl, "parse_entry_datetime", None)
        self.assertIsNotNone(parser_func, "parse_entry_datetime Funktion muss existieren")

        # Sun, 04 Oct 2026 09:15:00 +0200 -> date 2026-10-04, time 09:15
        d1, t1 = parser_func("Sun, 04 Oct 2026 09:15:00 +0200")
        self.assertEqual(d1, "2026-10-04")
        self.assertEqual(t1, "09:15")

        # 2026-10-04T07:15:00Z -> Berlin -> date 2026-10-04, time 09:15
        d2, t2 = parser_func("2026-10-04T07:15:00Z")
        self.assertEqual(d2, "2026-10-04")
        self.assertEqual(t2, "09:15")

        # reines Datum -> time leer
        d3, t3 = parser_func("2026-10-04")
        self.assertEqual(d3, "2026-10-04")
        self.assertEqual(t3, "")

    # 9. Kein <script und kein fonts.googleapis/cdn. in dist/
    def test_9_no_scripts_or_cdn(self):
        self.create_post("clean-post", {"date": "2026-10-04", "time": "09:15"})
        dist_dir = os.path.join(self.tmpdir, "dist")
        code, out, err = self.run_cli(["build", "--out", dist_dir])
        self.assertEqual(code, 0, f"build failed: {err}")

        for root, _, files in os.walk(dist_dir):
            for fname in files:
                if fname.endswith((".html", ".css", ".xml")):
                    fpath = os.path.join(root, fname)
                    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                    self.assertNotIn("<script", content, f"<script in {fpath} gefunden")
                    self.assertNotIn("fonts.googleapis", content, f"fonts.googleapis in {fpath} gefunden")
                    self.assertNotIn("cdn.", content, f"cdn. in {fpath} gefunden")

    # Zusatztests: list und show
    def test_10_list_and_show_with_time(self):
        self.create_post("zeit-post", {"title": "Zeit Post", "date": "2026-10-04", "time": "09:15"})
        self.create_post("ohne-zeit-post", {"title": "Ohne Zeit", "date": "2026-10-04"})

        # list Klartext
        code, out, err = self.run_cli(["list"])
        self.assertEqual(code, 0)
        self.assertIn("2026-10-04 09:15", out)
        self.assertIn("2026-10-04  Ohne Zeit", out)

        # list --json
        code, out, err = self.run_cli(["list", "--json"])
        self.assertEqual(code, 0)
        import json
        data = json.loads(out)
        posts_by_id = {p["id"]: p for p in data["posts"]}
        self.assertEqual(posts_by_id["zeit-post"]["time"], "09:15")
        self.assertEqual(posts_by_id["ohne-zeit-post"]["time"], "")

        # show
        code, out, err = self.run_cli(["show", "zeit-post"])
        self.assertEqual(code, 0)
        self.assertIn("time: 09:15", out)

    # 11. Scrape-Befehl setzt date und time aus Feed
    def test_11_scrape_command_with_time(self):
        rss_feed = """<?xml version="1.0" encoding="UTF-8"?>
        <rss version="2.0">
          <channel>
            <title>Test Feed</title>
            <item>
              <title>Scraped Item</title>
              <link>https://example.com/test-article</link>
              <description>Test Description</description>
              <pubDate>Sun, 04 Oct 2026 09:15:00 +0200</pubDate>
            </item>
          </channel>
        </rss>
        """
        import json
        sources_cfg = {
            "settings": {"max_items_per_run": 5},
            "sources": [
                {
                    "name": "TestSource",
                    "type": "rss",
                    "url": "https://example.com/feed.xml",
                    "tags": ["news"],
                    "enabled": True,
                }
            ]
        }
        with open(blogctl.SOURCE_JSON, "w", encoding="utf-8") as f:
            json.dump(sources_cfg, f)

        orig_http_get = blogctl.http_get
        blogctl.http_get = lambda url, ua: (rss_feed, "utf-8")
        try:
            code, out, err = self.run_cli(["scrape"])
            self.assertEqual(code, 0, f"scrape failed: {err}")
            draft_path = os.path.join(blogctl.DRAFTS, "scraped-item.md")
            self.assertTrue(os.path.isfile(draft_path))
            fm, _ = blogctl.read_article(draft_path)
            self.assertEqual(fm.get("date"), "2026-10-04")
            self.assertEqual(fm.get("time"), "09:15")
        finally:
            blogctl.http_get = orig_http_get


if __name__ == "__main__":
    unittest.main()
