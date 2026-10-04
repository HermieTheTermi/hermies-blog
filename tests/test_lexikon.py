import contextlib
import hashlib
import importlib.machinery
import importlib.util
import io
import json
import os
import re
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


class BlogLexikonTestCase(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.mkdtemp(prefix="bloglexikon-test-")
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
        os.environ["BLOGCTL_ROOT"] = self.tmpdir

        # Copy original templates to sandbox
        orig_templates_dir = os.path.join(REPO_ROOT, "content", "templates")
        shutil.copytree(orig_templates_dir, blogctl.TEMPLATES)

        # Copy original lexikon.json to sandbox
        orig_lexikon_path = os.path.join(REPO_ROOT, "content", "lexikon.json")
        os.makedirs(blogctl.CONTENT, exist_ok=True)
        if os.path.isfile(orig_lexikon_path):
            shutil.copy2(orig_lexikon_path, blogctl.LEXIKON_JSON)

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
        blogctl.LEXIKON_JSON = self.orig_lexikon_json
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

    # 1. Artikel mit {{Token}} -> Artikelseite enthaelt <a class="lex" href="lexikon.html#token"
    #    und data-tip="..." mit dem Text aus lexikon.json
    def test_1_article_with_marker_rendering(self):
        body = "Ein Sprachmodell zerlegt Text in {{Token}}. Roboter brauchen einen {{Greifpunkt}}."
        self.create_post("marker-post", body=body)
        dist_dir = os.path.join(self.tmpdir, "dist")
        code, out, err = self.run_cli(["build", "--out", dist_dir])
        self.assertEqual(code, 0, f"build failed: {err}")

        post_path = os.path.join(dist_dir, "marker-post.html")
        self.assertTrue(os.path.isfile(post_path), "Artikelseite nicht erzeugt")
        with open(post_path, "r", encoding="utf-8") as f:
            html_content = f.read()

        with open(blogctl.LEXIKON_JSON, "r", encoding="utf-8") as f:
            lex_data = json.load(f)

        token_tip = lex_data["Token"]
        greifpunkt_tip = lex_data["Greifpunkt"]

        # Link and data-tip for Token
        self.assertIn('<a class="lex" href="lexikon.html#token"', html_content)
        self.assertIn(f'data-tip="{token_tip}"', html_content)
        self.assertIn('>Token</a>', html_content)

        # Link and data-tip for Greifpunkt
        self.assertIn('<a class="lex" href="lexikon.html#greifpunkt"', html_content)
        self.assertIn(f'data-tip="{greifpunkt_tip}"', html_content)
        self.assertIn('>Greifpunkt</a>', html_content)

    # 2. Marker in Backtick-Code bleibt unveraendert; nach dem Build keine {{-Reste in dist/
    def test_2_backtick_code_and_no_marker_remnants(self):
        body = (
            "## TL;DR: {{Token}} und {{Mixture-of-Experts}}\n\n"
            "Normaler Text mit `{{Token}}` im Code-Span und {{Greifpunkt}} im Text.\n\n"
            "```python\n"
            "def test():\n"
            "    return '{{Token}}'\n"
            "```\n\n"
            "- Liste mit {{Quantisierung}}\n"
            "- Zweiter Punkt mit `{{Greifpunkt}}`\n\n"
            "> Zitat mit {{Kontextfenster}}\n"
        )
        self.create_post("backtick-post", body=body)
        dist_dir = os.path.join(self.tmpdir, "dist")
        code, out, err = self.run_cli(["build", "--out", dist_dir])
        self.assertEqual(code, 0, f"build failed: {err}")

        post_path = os.path.join(dist_dir, "backtick-post.html")
        with open(post_path, "r", encoding="utf-8") as f:
            post_html = f.read()

        # Marker in backtick code remains unchanged (wrapped in <code>)
        self.assertIn("<code>{{Token}}</code>", post_html)
        self.assertIn("<code>{{Greifpunkt}}</code>", post_html)

        # In code blocks, {{Token}} is literal
        self.assertIn("return &#x27;{{Token}}&#x27;", post_html)

        # Check all HTML files in dist: outside <code> tags, there should be NO {{ remnants
        for root, dirs, files in os.walk(dist_dir):
            for file in files:
                if not file.endswith(".html"):
                    continue
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                # Strip out <code>...</code> and <pre>...</pre>
                stripped = re.sub(r"<code>.*?</code>", "", content, flags=re.DOTALL)
                stripped = re.sub(r"<pre>.*?</pre>", "", stripped, flags=re.DOTALL)
                remnants = re.findall(r"\{\{.*?\}\}", stripped)
                self.assertEqual(remnants, [], f"Unerwartete {{{{...}}}}-Reste in {file}: {remnants}")

    # 3. dist/lexikon.html existiert, enthaelt jeden Begriff mit korrekter Anker-id, alphabetisch sortiert
    def test_3_lexikon_page_structure_and_sorting(self):
        dist_dir = os.path.join(self.tmpdir, "dist")
        code, out, err = self.run_cli(["build", "--out", dist_dir])
        self.assertEqual(code, 0, f"build failed: {err}")

        lexikon_path = os.path.join(dist_dir, "lexikon.html")
        self.assertTrue(os.path.isfile(lexikon_path), "dist/lexikon.html existiert nicht")

        with open(lexikon_path, "r", encoding="utf-8") as f:
            lex_html = f.read()

        with open(blogctl.LEXIKON_JSON, "r", encoding="utf-8") as f:
            lex_data = json.load(f)

        sorted_terms = sorted(lex_data.keys(), key=lambda t: t.lower())
        last_pos = -1

        for term in sorted_terms:
            slug = blogctl.slugify(term)
            anchor_pattern = f'id="{slug}"'
            self.assertIn(anchor_pattern, lex_html, f"Anker fuer {term} ({slug}) fehlt in lexikon.html")
            self.assertIn(f"<h2>{term}</h2>", lex_html, f"Ueberschrift fuer {term} fehlt in lexikon.html")
            self.assertIn(lex_data[term], lex_html, f"Erklaerungstext fuer {term} fehlt in lexikon.html")

            pos = lex_html.find(anchor_pattern)
            self.assertGreater(pos, last_pos, f"Begriff {term} nicht alphabetisch sortiert in lexikon.html")
            last_pos = pos

    # 4. Nav- und Footer-Link "Lexikon" sind auf allen Seiten vorhanden (grep ueber dist/*.html)
    def test_4_nav_and_footer_links_present_on_all_pages(self):
        self.create_post("nav-test-post", {"tags": ["rubrik"]})
        dist_dir = os.path.join(self.tmpdir, "dist")
        code, out, err = self.run_cli(["build", "--out", dist_dir])
        self.assertEqual(code, 0, f"build failed: {err}")

        html_files = []
        for root, dirs, files in os.walk(dist_dir):
            for file in files:
                if file.endswith(".html"):
                    html_files.append(os.path.join(root, file))

        self.assertGreaterEqual(len(html_files), 4, "Zu wenige HTML-Dateien generiert")

        for file_path in html_files:
            rel = os.path.relpath(file_path, dist_dir)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Root pages link to lexikon.html, subpages (tag/) link to ../lexikon.html
            expected_href = "../lexikon.html" if "/" in rel else "lexikon.html"
            lex_link_snippet = f'href="{expected_href}">Lexikon</a>'

            self.assertIn(lex_link_snippet, content, f"Lexikon-Link fehlt in {rel}")
            # Count must be at least 2: once in header nav, once in footer
            count = content.count(lex_link_snippet)
            self.assertGreaterEqual(count, 2, f"Lexikon-Link nicht in Nav UND Footer in {rel} (count={count})")

    # 5. sitemap.xml enthaelt lexikon.html
    def test_5_sitemap_contains_lexikon(self):
        dist_dir = os.path.join(self.tmpdir, "dist")
        code, out, err = self.run_cli(["build", "--out", dist_dir])
        self.assertEqual(code, 0, f"build failed: {err}")

        sitemap_path = os.path.join(dist_dir, "sitemap.xml")
        self.assertTrue(os.path.isfile(sitemap_path), "sitemap.xml existiert nicht")
        with open(sitemap_path, "r", encoding="utf-8") as f:
            sitemap_content = f.read()

        self.assertIn("lexikon.html</loc>", sitemap_content, "lexikon.html fehlt in sitemap.xml")

    # 6. check: unbekannter Marker -> Fehler; bekannter Marker -> kein Fehler; kaputtes lexikon.json -> Fehler
    def test_6_check_validation(self):
        # A: Known marker -> check passes
        self.create_post("valid-post", body="Text mit {{Token}}.")
        code, out, err = self.run_cli(["check"])
        self.assertEqual(code, 0, f"check sollte mit gueltigem Marker erfolgreich sein: {out} {err}")

        # B: Unknown marker -> check fails with article id and term
        self.create_post("invalid-post", body="Text mit {{UnbekannterBegriff123}}.")
        code, out, err = self.run_cli(["check"])
        self.assertEqual(code, 1, "check muss bei unbekanntem Marker fehlschlagen")
        self.assertIn("invalid-post", out + err)
        self.assertIn("UnbekannterBegriff123", out + err)

        # Cleanup invalid post
        os.remove(os.path.join(blogctl.POSTS, "invalid-post.md"))

        # C: Unknown marker in backticks must NOT cause an error
        self.create_post("code-post", body="Hier steht `{{UnbekannterBegriff123}}` im Code.")
        code, out, err = self.run_cli(["check"])
        self.assertEqual(code, 0, f"check darf bei Marker in Backtick-Code keinen Fehler werfen: {out} {err}")

        # D: Broken lexikon.json (missing file)
        os.remove(blogctl.LEXIKON_JSON)
        code, out, err = self.run_cli(["check"])
        self.assertEqual(code, 1, "check muss fehlschlagen wenn lexikon.json fehlt")

        # E: Broken lexikon.json (empty explanation text)
        with open(blogctl.LEXIKON_JSON, "w", encoding="utf-8") as f:
            json.dump({"Token": "   "}, f)
        code, out, err = self.run_cli(["check"])
        self.assertEqual(code, 1, "check muss fehlschlagen bei leerem Erklaerungstext")

        # F: Broken lexikon.json (duplicate terms with differing casing)
        with open(blogctl.LEXIKON_JSON, "w", encoding="utf-8") as f:
            json.dump({"Token": "Erklaerung 1", "token": "Erklaerung 2"}, f)
        code, out, err = self.run_cli(["check"])
        self.assertEqual(code, 1, "check muss fehlschlagen bei Begriffen die sich nur in Gross/Klein unterscheiden")

        # G: Broken lexikon.json (not a flat string->string dict)
        with open(blogctl.LEXIKON_JSON, "w", encoding="utf-8") as f:
            json.dump({"Token": 12345}, f)
        code, out, err = self.run_cli(["check"])
        self.assertEqual(code, 1, "check muss fehlschlagen wenn lexikon.json kein String->String-Objekt ist")

    # 7. Entwicklungsumrechnung im Tooltip: &, ", < im Erklaerungstext bleiben escaped
    def test_7_tooltip_special_chars_escaping(self):
        special_text = 'Erklaerung mit <tag>, "Anfuehrungszeichen" & Ampersand sowie Zeilenumbruch\nzweite Zeile.'
        with open(blogctl.LEXIKON_JSON, "w", encoding="utf-8") as f:
            json.dump({"Sonder": special_text}, f)

        self.create_post("special-post", body="Hier wird {{Sonder}} getestet.")
        dist_dir = os.path.join(self.tmpdir, "dist")
        code, out, err = self.run_cli(["build", "--out", dist_dir])
        self.assertEqual(code, 0, f"build failed: {err}")

        with open(os.path.join(dist_dir, "special-post.html"), "r", encoding="utf-8") as f:
            html = f.read()

        # Check escaped characters in data-tip
        self.assertIn('&lt;tag&gt;', html)
        self.assertIn('&quot;Anfuehrungszeichen&quot;', html)
        self.assertIn('&amp; Ampersand', html)
        # Newline normalized to space
        self.assertIn('Zeilenumbruch zweite Zeile.', html)
        self.assertNotIn('\nzweite Zeile', html)

    # 8. Determinismus: zwei Builds byte-identisch. Kein <script, keine externen Ressourcen in dist/
    def test_8_determinism_and_no_external_resources(self):
        self.create_post("det-post-1", body="Artikel 1 mit {{Token}}.")
        self.create_post("det-post-2", body="Artikel 2 mit {{Greifpunkt}} und {{LLM}}.")

        dist1 = os.path.join(self.tmpdir, "dist1")
        dist2 = os.path.join(self.tmpdir, "dist2")

        code1, _, _ = self.run_cli(["build", "--out", dist1])
        code2, _, _ = self.run_cli(["build", "--out", dist2])
        self.assertEqual(code1, 0)
        self.assertEqual(code2, 0)

        # Compare files
        files1 = sorted(os.listdir(dist1))
        files2 = sorted(os.listdir(dist2))
        self.assertEqual(files1, files2)

        for filename in files1:
            p1 = os.path.join(dist1, filename)
            p2 = os.path.join(dist2, filename)
            if os.path.isfile(p1):
                with open(p1, "rb") as f1, open(p2, "rb") as f2:
                    h1 = hashlib.sha256(f1.read()).hexdigest()
                    h2 = hashlib.sha256(f2.read()).hexdigest()
                self.assertEqual(h1, h2, f"Builds sind fuer {filename} nicht byte-identisch")

        # Verify no <script and no external resources in dist1
        for root, dirs, files in os.walk(dist1):
            for file in files:
                if file.endswith((".html", ".css", ".xml")):
                    p = os.path.join(root, file)
                    with open(p, "r", encoding="utf-8", errors="ignore") as f:
                        text = f.read()
                    self.assertNotIn("<script", text.lower(), f"<script in {file} gefunden")
                    # Check for external fonts, CDNs, external scripts/links
                    for ext_pattern in ["fonts.googleapis.com", "fonts.gstatic.com", "cdnjs.cloudflare.com", "unpkg.com"]:
                        self.assertNotIn(ext_pattern, text.lower(), f"Externe Ressource {ext_pattern} in {file}")

    # 9. lexikon-Befehl: Klartext und --json liefern alle Begriffe; Exit 0
    def test_9_lexikon_cli_command(self):
        with open(blogctl.LEXIKON_JSON, "r", encoding="utf-8") as f:
            lex_data = json.load(f)

        # Plain text
        code, out, err = self.run_cli(["lexikon"])
        self.assertEqual(code, 0, f"lexikon fehlgeschlagen: {err}")
        lines = [line.strip() for line in out.strip().split("\n") if line.strip()]
        self.assertEqual(len(lines), len(lex_data), "Anzahl Begriffe im Klartext stimmt nicht")
        for term in lex_data.keys():
            self.assertIn(term, lines)

        # JSON
        code, out, err = self.run_cli(["lexikon", "--json"])
        self.assertEqual(code, 0, f"lexikon --json fehlgeschlagen: {err}")
        parsed = json.loads(out)
        self.assertIn("terms", parsed)
        terms = parsed["terms"]
        self.assertEqual(len(terms), len(lex_data))

        terms_dict = {t["term"]: t for t in terms}
        for term, text in lex_data.items():
            self.assertIn(term, terms_dict)
            item = terms_dict[term]
            self.assertEqual(item["slug"], blogctl.slugify(term))
            self.assertEqual(item["text"], text)


if __name__ == "__main__":
    unittest.main()
