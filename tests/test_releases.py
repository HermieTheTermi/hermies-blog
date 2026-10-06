import contextlib
import importlib.machinery
import importlib.util
import io
import json
import os
import re
import shutil
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


class FakeProcess:
    def __init__(self, returncode=0, stdout="", stderr=""):
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr


class BlogReleasesTestCase(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.mkdtemp(prefix="blogreleases-test-")
        self.bare_origin = tempfile.mkdtemp(prefix="fake-origin-")

        # Initialize bare remote repository
        subprocess.run(["git", "init", "--bare", self.bare_origin], check=True, capture_output=True)

        self.orig_root = blogctl.ROOT
        self.orig_content = blogctl.CONTENT
        self.orig_drafts = blogctl.DRAFTS
        self.orig_posts = blogctl.POSTS
        self.orig_pages = blogctl.PAGES
        self.orig_assets = blogctl.ASSETS
        self.orig_templates = blogctl.TEMPLATES
        self.orig_site_json = blogctl.SITE_JSON
        self.orig_source_json = blogctl.SOURCE_JSON
        self.orig_lexikon_json = getattr(blogctl, "LEXIKON_JSON", os.path.join(blogctl.CONTENT, "lexikon.json"))
        self.orig_releases_json = getattr(blogctl, "RELEASES_JSON", os.path.join(blogctl.CONTENT, "releases.json"))
        self.orig_run_gh = getattr(blogctl, "run_gh", None)

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
        blogctl.LEXIKON_JSON = os.path.join(blogctl.CONTENT, "lexikon.json")
        blogctl.RELEASES_JSON = os.path.join(blogctl.CONTENT, "releases.json")
        os.environ["BLOGCTL_ROOT"] = self.tmpdir

        # Copy original templates to sandbox
        orig_templates_dir = os.path.join(REPO_ROOT, "content", "templates")
        shutil.copytree(orig_templates_dir, blogctl.TEMPLATES)

        # Copy original pages to sandbox
        orig_pages_dir = os.path.join(REPO_ROOT, "content", "pages")
        if os.path.isdir(orig_pages_dir):
            shutil.copytree(orig_pages_dir, blogctl.PAGES)
        else:
            os.makedirs(blogctl.PAGES, exist_ok=True)

        # Copy original lexikon.json to sandbox
        orig_lexikon_path = os.path.join(REPO_ROOT, "content", "lexikon.json")
        os.makedirs(blogctl.CONTENT, exist_ok=True)
        if os.path.isfile(orig_lexikon_path):
            shutil.copy2(orig_lexikon_path, blogctl.LEXIKON_JSON)

        # Copy site.json if present
        orig_site_path = os.path.join(REPO_ROOT, "content", "site.json")
        if os.path.isfile(orig_site_path):
            shutil.copy2(orig_site_path, blogctl.SITE_JSON)

        blogctl.ensure_dirs()

        # Initialize git repo in sandbox and push main to bare remote
        subprocess.run(["git", "init"], cwd=self.tmpdir, check=True, capture_output=True)
        subprocess.run(["git", "config", "user.name", "Test User"], cwd=self.tmpdir, check=True, capture_output=True)
        subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=self.tmpdir, check=True, capture_output=True)
        subprocess.run(["git", "remote", "add", "origin", self.bare_origin], cwd=self.tmpdir, check=True, capture_output=True)
        subprocess.run(["git", "checkout", "-b", "main"], cwd=self.tmpdir, check=True, capture_output=True)
        subprocess.run(["git", "add", "-A"], cwd=self.tmpdir, check=True, capture_output=True)
        subprocess.run(["git", "commit", "-m", "Init test repo"], cwd=self.tmpdir, check=True, capture_output=True)
        subprocess.run(["git", "push", "-u", "origin", "main"], cwd=self.tmpdir, check=True, capture_output=True)

        self.gh_calls = []

        def default_mock_run_gh(argv):
            self.gh_calls.append(list(argv))
            return FakeProcess(returncode=0, stdout="", stderr="")

        blogctl.run_gh = default_mock_run_gh

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
        blogctl.LEXIKON_JSON = self.orig_lexikon_json
        blogctl.RELEASES_JSON = self.orig_releases_json
        if self.orig_run_gh is not None:
            blogctl.run_gh = self.orig_run_gh
        elif hasattr(blogctl, "run_gh"):
            delattr(blogctl, "run_gh")
        os.environ.pop("BLOGCTL_ROOT", None)
        shutil.rmtree(self.tmpdir, ignore_errors=True)
        shutil.rmtree(self.bare_origin, ignore_errors=True)

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

    def _extract_nav_blocks(self, html):
        header_match = re.search(r'<nav class="site-nav"[^>]*>(.*?)</nav>', html, re.DOTALL)
        footer_match = re.search(r'<nav class="footer-links"[^>]*>(.*?)</nav>', html, re.DOTALL)
        header_nav = header_match.group(1) if header_match else ""
        footer_nav = footer_match.group(1) if footer_match else ""
        return header_nav, footer_nav

    # 1. Erstlauf ohne content/releases.json: Basisstand wird gesetzt, run_gh wird nicht aufgerufen.
    def test_1_first_run_creates_baseline_without_gh_calls(self):
        self.create_post("artikel-1")
        self.create_post("artikel-2")

        rel_path = blogctl.RELEASES_JSON
        self.assertFalse(os.path.exists(rel_path), "releases.json sollte vor Erstlauf nicht existieren")

        code, out, err = self.run_cli(["deploy"])
        self.assertEqual(code, 0, f"deploy fehlgeschlagen: {err}")

        # run_gh darf nicht aufgerufen worden sein
        self.assertEqual(len(self.gh_calls), 0, "run_gh darf beim Erstlauf nicht aufgerufen werden")

        # releases.json muss jetzt existieren und beide Artikel enthalten
        self.assertTrue(os.path.exists(rel_path), "releases.json muss nach Erstlauf existieren")
        with open(rel_path, "r", encoding="utf-8") as f:
            state = json.load(f)

        self.assertIn("released", state)
        self.assertIn("artikel-1", state["released"])
        self.assertIn("artikel-2", state["released"])
        self.assertEqual(state["released"]["artikel-1"], "artikel-1")
        self.assertEqual(state["released"]["artikel-2"], "artikel-2")
        self.assertIn("Release-Basisstand gesetzt", out)

    # 2. Neuer Artikel nach gesetztem Basisstand: genau ein gh release create mit Tag, Titel und Notes
    def test_2_new_article_after_baseline_creates_release(self):
        self.create_post("basis-artikel")
        # Erstlauf
        code, out, err = self.run_cli(["deploy"])
        self.assertEqual(code, 0)
        self.assertEqual(len(self.gh_calls), 0)

        # Neuer Artikel
        self.create_post("neuer-artikel", {
            "title": "Neuer Artikel Titel",
            "date": "2026-10-06",
            "time": "14:30",
            "summary": "Kurze Zusammenfassung für Release.",
        })

        self.gh_calls.clear()
        code, out, err = self.run_cli(["deploy"])
        self.assertEqual(code, 0, f"deploy fehlgeschlagen: {err}")

        # Prüfe Aufrufe: genau ein release create
        rel_create_calls = [c for c in self.gh_calls if len(c) > 1 and c[0] == "release" and c[1] == "create"]
        self.assertEqual(len(rel_create_calls), 1, f"Erwartet genau 1 'release create', Aufrufe: {self.gh_calls}")

        cmd = rel_create_calls[0]
        self.assertEqual(cmd[2], "neuer-artikel")
        self.assertIn("--title", cmd)
        title_idx = cmd.index("--title") + 1
        self.assertEqual(cmd[title_idx], "Neuer Artikel Titel")

        self.assertIn("--notes", cmd)
        notes_idx = cmd.index("--notes") + 1
        notes = cmd[notes_idx]
        self.assertIn("Kurze Zusammenfassung für Release.", notes)
        self.assertIn("Artikel: https://hermiethetermi.github.io/hermies-blog/neuer-artikel.html", notes)
        self.assertIn("Veröffentlicht: 06.10.2026, 14:30", notes)

        # releases.json muss nun neuer-artikel enthalten
        with open(blogctl.RELEASES_JSON, "r", encoding="utf-8") as f:
            state = json.load(f)
        self.assertIn("neuer-artikel", state["released"])

    # 3. Idempotenz: zweiter Lauf ruft run_gh nicht erneut auf, Datei unverändert
    def test_3_idempotent_second_run_does_not_call_gh(self):
        self.create_post("artikel-a")
        self.run_cli(["deploy"])

        self.create_post("artikel-b")
        code, _, _ = self.run_cli(["deploy"])
        self.assertEqual(code, 0)

        with open(blogctl.RELEASES_JSON, "r", encoding="utf-8") as f:
            content_before = f.read()

        self.gh_calls.clear()
        code, out, err = self.run_cli(["deploy"])
        self.assertEqual(code, 0)
        rel_create_calls = [c for c in self.gh_calls if len(c) > 1 and c[0] == "release" and c[1] == "create"]
        self.assertEqual(len(rel_create_calls), 0, "Zweiter Lauf darf kein 'release create' ausführen")

        with open(blogctl.RELEASES_JSON, "r", encoding="utf-8") as f:
            content_after = f.read()
        self.assertEqual(content_before, content_after, "Zustandsdatei darf sich bei unverändertem Stand nicht ändern")

    # 4. run_gh schlägt fehl: deploy bleibt ok (Exit 0), Slug wird nicht eingetragen, nächster Lauf versucht erneut
    def test_4_gh_failure_retains_slug_for_retry(self):
        self.create_post("basis-artikel")
        self.run_cli(["deploy"])

        self.create_post("problem-artikel", {"title": "Problem Artikel"})

        # Simuliere Fehlschlag bei release create
        def failing_mock_run_gh(argv):
            self.gh_calls.append(list(argv))
            if len(argv) > 1 and argv[0] == "release" and argv[1] == "create":
                return FakeProcess(returncode=1, stderr="GitHub API error: rate limited")
            return FakeProcess(returncode=0)

        blogctl.run_gh = failing_mock_run_gh
        code, out, err = self.run_cli(["deploy"])
        self.assertEqual(code, 0, "deploy muss trotz Release-Fehler mit 0 beenden")
        self.assertIn("Warnung", err)

        with open(blogctl.RELEASES_JSON, "r", encoding="utf-8") as f:
            state = json.load(f)
        self.assertNotIn("problem-artikel", state["released"], "Fehlgeschlagener Slug darf nicht eingetragen werden")

        # Nächster Lauf gelingt
        blogctl.run_gh = lambda argv: (self.gh_calls.append(list(argv)), FakeProcess(returncode=0))[1]
        self.gh_calls.clear()
        code, out, err = self.run_cli(["deploy"])
        self.assertEqual(code, 0)

        rel_create_calls = [c for c in self.gh_calls if len(c) > 1 and c[0] == "release" and c[1] == "create"]
        self.assertEqual(len(rel_create_calls), 1)

        with open(blogctl.RELEASES_JSON, "r", encoding="utf-8") as f:
            state = json.load(f)
        self.assertIn("problem-artikel", state["released"])

    # 5. gh fehlt/nicht angemeldet: Warnung, Exit 0, Basisstand wird trotzdem gesetzt
    def test_5_gh_missing_or_unauthenticated_warns_and_sets_baseline(self):
        self.create_post("start-artikel")

        def missing_gh(argv):
            raise FileNotFoundError("No such file or directory: 'gh'")

        blogctl.run_gh = missing_gh
        code, out, err = self.run_cli(["deploy"])
        self.assertEqual(code, 0, "Erstlauf mit fehlendem gh muss Exit 0 liefern")
        self.assertTrue(os.path.exists(blogctl.RELEASES_JSON))
        with open(blogctl.RELEASES_JSON, "r", encoding="utf-8") as f:
            state = json.load(f)
        self.assertIn("start-artikel", state["released"])

        # Neuer Artikel bei fehlgeschlagener Authentifizierung
        self.create_post("weiterer-artikel")

        def unauth_gh(argv):
            self.gh_calls.append(list(argv))
            if argv == ["auth", "status"]:
                return FakeProcess(returncode=1, stderr="You are not logged into any GitHub hosts.")
            return FakeProcess(returncode=1, stderr="Not logged in")

        blogctl.run_gh = unauth_gh
        code, out, err = self.run_cli(["deploy"])
        self.assertEqual(code, 0, "deploy muss bei nicht angemeldetem gh mit 0 beenden")
        self.assertIn("Warnung", err)

        with open(blogctl.RELEASES_JSON, "r", encoding="utf-8") as f:
            state2 = json.load(f)
        self.assertNotIn("weiterer-artikel", state2["released"])

    # 6. --no-releases: keine run_gh-Aufrufe, Zustandsdatei unverändert
    def test_6_no_releases_flag_skips_releases(self):
        self.create_post("artikel-1")
        # Erstlauf mit Basisstand
        self.run_cli(["deploy"])
        self.assertTrue(os.path.exists(blogctl.RELEASES_JSON))
        with open(blogctl.RELEASES_JSON, "r", encoding="utf-8") as f:
            content_before = f.read()

        self.create_post("artikel-2")
        self.gh_calls.clear()

        code, out, err = self.run_cli(["deploy", "--no-releases"])
        self.assertEqual(code, 0, f"deploy --no-releases fehlgeschlagen: {err}")
        self.assertEqual(len(self.gh_calls), 0, "--no-releases darf keine gh-Aufrufe machen")

        with open(blogctl.RELEASES_JSON, "r", encoding="utf-8") as f:
            content_after = f.read()
        self.assertEqual(content_before, content_after, "Zustandsdatei muss unverändert bleiben")

    # 7. abonnieren.html wird gebaut und ist aus Kopf- und Fußzeile verlinkt (auch Unterseiten)
    def test_7_abonnieren_page_built_and_linked_in_header_and_footer(self):
        self.create_post("artikel-nav")
        dist_dir = os.path.join(self.tmpdir, "dist")
        code, out, err = self.run_cli(["build", "--out", dist_dir])
        self.assertEqual(code, 0, f"build fehlgeschlagen: {err}")

        abonnieren_html_path = os.path.join(dist_dir, "abonnieren.html")
        self.assertTrue(os.path.isfile(abonnieren_html_path), "abonnieren.html wurde nicht gebaut")

        # Prüfe index.html Links
        index_path = os.path.join(dist_dir, "index.html")
        with open(index_path, "r", encoding="utf-8") as f:
            index_html = f.read()

        sub_link = '<a href="abonnieren.html">Abonnieren</a>'
        self.assertEqual(index_html.count(sub_link), 2, f"Erwartet 2 Links zu {sub_link} in index.html")
        header_nav, footer_nav = self._extract_nav_blocks(index_html)
        self.assertIn(sub_link, header_nav, "Abonnieren-Link fehlt in Hauptnavigation")
        self.assertIn(sub_link, footer_nav, "Abonnieren-Link fehlt in Fußzeile")

        # Prüfe Reihenfolge im Header: ... Lexikon, Abonnieren, Impressum, Datenschutz
        lex_link = '<a href="lexikon.html">Lexikon</a>'
        imp_link = '<a href="impressum.html">Impressum</a>'
        ds_link = '<a href="datenschutz.html">Datenschutz</a>'
        self.assertIn(lex_link, header_nav)
        self.assertIn(imp_link, header_nav)
        self.assertIn(ds_link, header_nav)
        lex_idx = header_nav.find(lex_link)
        sub_idx = header_nav.find(sub_link)
        imp_idx = header_nav.find(imp_link)
        ds_idx = header_nav.find(ds_link)
        self.assertLess(lex_idx, sub_idx, "Lexikon muss vor Abonnieren stehen")
        self.assertLess(sub_idx, imp_idx, "Abonnieren muss vor Impressum stehen")
        self.assertLess(imp_idx, ds_idx, "Impressum muss vor Datenschutz stehen")

        # Prüfe Reihenfolge in Fußzeile: vor dem RSS-Link
        rss_link = '<a href="feed.xml">RSS</a>'
        self.assertIn(rss_link, footer_nav)
        footer_sub_idx = footer_nav.find(sub_link)
        footer_rss_idx = footer_nav.find(rss_link)
        self.assertLess(footer_sub_idx, footer_rss_idx, "Abonnieren muss in Fußzeile vor RSS stehen")

        # Prüfe Unterseite tag/news.html mit relativen Pfaden ../
        tag_path = os.path.join(dist_dir, "tag", "news.html")
        self.assertTrue(os.path.isfile(tag_path))
        with open(tag_path, "r", encoding="utf-8") as f:
            tag_html = f.read()

        rel_sub_link = '<a href="../abonnieren.html">Abonnieren</a>'
        self.assertEqual(tag_html.count(rel_sub_link), 2, f"Erwartet 2 Links zu {rel_sub_link} in tag/news.html")
        self.assertNotIn('<a href="abonnieren.html">Abonnieren</a>', tag_html)
        self.assertNotIn('<a href="/abonnieren.html">Abonnieren</a>', tag_html)


if __name__ == "__main__":
    unittest.main()
