import contextlib
import hashlib
import importlib.machinery
import importlib.util
import io
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


class BlogNewsNavTestCase(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.mkdtemp(prefix="blognewsnav-test-")
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
            "tags": ["news", "brainstorming"],
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

    def test_1_news_nav_in_index_html(self):
        self.create_post("erster-artikel", {"tags": ["news", "brainstorming"]})
        dist_dir = os.path.join(self.tmpdir, "dist")
        code, out, err = self.run_cli(["build", "--out", dist_dir])
        self.assertEqual(code, 0, f"build failed: {err}")

        index_path = os.path.join(dist_dir, "index.html")
        self.assertTrue(os.path.isfile(index_path))
        with open(index_path, "r", encoding="utf-8") as f:
            index_html = f.read()

        news_link = '<a href="tag/news.html">News</a>'
        brainstorming_link = '<a href="tag/brainstorming.html">Brainstorming</a>'

        # Link must be present
        self.assertIn(news_link, index_html)

        # Count must be exactly 2 (header and footer)
        self.assertEqual(index_html.count(news_link), 2, f"Expected 2 occurrences of {news_link} in index.html")

        # Check navigation blocks
        header_nav, footer_nav = self._extract_nav_blocks(index_html)
        self.assertIn(news_link, header_nav, "News link missing in header nav")
        self.assertIn(news_link, footer_nav, "News link missing in footer nav")

        # Order check: News must come before Brainstorming
        header_news_idx = header_nav.find(news_link)
        header_brain_idx = header_nav.find(brainstorming_link)
        self.assertNotEqual(header_news_idx, -1)
        self.assertNotEqual(header_brain_idx, -1)
        self.assertLess(header_news_idx, header_brain_idx, "News must precede Brainstorming in header")

        footer_news_idx = footer_nav.find(news_link)
        footer_brain_idx = footer_nav.find(brainstorming_link)
        self.assertNotEqual(footer_news_idx, -1)
        self.assertNotEqual(footer_brain_idx, -1)
        self.assertLess(footer_news_idx, footer_brain_idx, "News must precede Brainstorming in footer")

    def test_2_news_nav_in_article_page(self):
        self.create_post("erster-artikel", {"tags": ["news", "brainstorming"]})
        dist_dir = os.path.join(self.tmpdir, "dist")
        code, out, err = self.run_cli(["build", "--out", dist_dir])
        self.assertEqual(code, 0, f"build failed: {err}")

        article_path = os.path.join(dist_dir, "erster-artikel.html")
        self.assertTrue(os.path.isfile(article_path))
        with open(article_path, "r", encoding="utf-8") as f:
            article_html = f.read()

        news_link = '<a href="tag/news.html">News</a>'
        brainstorming_link = '<a href="tag/brainstorming.html">Brainstorming</a>'

        self.assertIn(news_link, article_html)
        self.assertEqual(article_html.count(news_link), 2, f"Expected 2 occurrences of {news_link} in article page")

        header_nav, footer_nav = self._extract_nav_blocks(article_html)
        self.assertIn(news_link, header_nav, "News link missing in header nav")
        self.assertIn(news_link, footer_nav, "News link missing in footer nav")

        header_news_idx = header_nav.find(news_link)
        header_brain_idx = header_nav.find(brainstorming_link)
        self.assertLess(header_news_idx, header_brain_idx, "News must precede Brainstorming in header")

        footer_news_idx = footer_nav.find(news_link)
        footer_brain_idx = footer_nav.find(brainstorming_link)
        self.assertLess(footer_news_idx, footer_brain_idx, "News must precede Brainstorming in footer")

    def test_3_news_nav_in_subfolder_tag_page(self):
        self.create_post("erster-artikel", {"tags": ["news", "brainstorming"]})
        dist_dir = os.path.join(self.tmpdir, "dist")
        code, out, err = self.run_cli(["build", "--out", dist_dir])
        self.assertEqual(code, 0, f"build failed: {err}")

        tag_news_path = os.path.join(dist_dir, "tag", "news.html")
        self.assertTrue(os.path.isfile(tag_news_path))
        with open(tag_news_path, "r", encoding="utf-8") as f:
            tag_html = f.read()

        rel_news_link = '<a href="../tag/news.html">News</a>'
        rel_brainstorming_link = '<a href="../tag/brainstorming.html">Brainstorming</a>'

        # Must use relative link with ../
        self.assertIn(rel_news_link, tag_html)
        self.assertEqual(tag_html.count(rel_news_link), 2, f"Expected 2 occurrences of {rel_news_link} in tag/news.html")

        # No broken absolute links or missing ../ in nav
        self.assertNotIn('<a href="/tag/news.html">News</a>', tag_html)
        header_nav, footer_nav = self._extract_nav_blocks(tag_html)
        self.assertNotIn('<a href="tag/news.html">News</a>', header_nav)
        self.assertNotIn('<a href="tag/news.html">News</a>', footer_nav)

        # Order in header and footer
        header_news_idx = header_nav.find(rel_news_link)
        header_brain_idx = header_nav.find(rel_brainstorming_link)
        self.assertNotEqual(header_news_idx, -1)
        self.assertNotEqual(header_brain_idx, -1)
        self.assertLess(header_news_idx, header_brain_idx, "News must precede Brainstorming in header on tag page")

        footer_news_idx = footer_nav.find(rel_news_link)
        footer_brain_idx = footer_nav.find(rel_brainstorming_link)
        self.assertNotEqual(footer_news_idx, -1)
        self.assertNotEqual(footer_brain_idx, -1)
        self.assertLess(footer_news_idx, footer_brain_idx, "News must precede Brainstorming in footer on tag page")

    def test_4_no_marker_remnants_and_no_scripts(self):
        self.create_post("test-artikel", {"tags": ["news", "brainstorming"]})
        dist_dir = os.path.join(self.tmpdir, "dist")
        code, out, err = self.run_cli(["build", "--out", dist_dir])
        self.assertEqual(code, 0, f"build failed: {err}")

        for root, _, files in os.walk(dist_dir):
            for file in files:
                if file.endswith((".html", ".css", ".xml")):
                    path = os.path.join(root, file)
                    with open(path, "r", encoding="utf-8", errors="ignore") as f:
                        text = f.read()
                    # Check for unrendered template markers like {{NEWS_HREF}}
                    self.assertNotIn("{{NEWS_HREF}}", text, f"Unrendered {{NEWS_HREF}} found in {file}")
                    # No marker remnants in HTML
                    if file.endswith(".html"):
                        self.assertNotIn("{{", text, f"Unrendered '{{{{' found in {file}")
                        self.assertNotIn("<script", text.lower(), f"<script found in {file}")
                    for ext_pattern in ["fonts.googleapis.com", "fonts.gstatic.com", "cdnjs.cloudflare.com", "unpkg.com"]:
                        self.assertNotIn(ext_pattern, text.lower(), f"External resource {ext_pattern} in {file}")

    def test_5_build_determinism(self):
        self.create_post("det-post-1", {"tags": ["news", "brainstorming"]})
        self.create_post("det-post-2", {"tags": ["news"]})

        dist1 = os.path.join(self.tmpdir, "dist1")
        dist2 = os.path.join(self.tmpdir, "dist2")

        code1, _, _ = self.run_cli(["build", "--out", dist1])
        self.assertEqual(code1, 0)
        code2, _, _ = self.run_cli(["build", "--out", dist2])
        self.assertEqual(code2, 0)

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
                self.assertEqual(h1, h2, f"Builds are not byte-identical for {filename}")


if __name__ == "__main__":
    unittest.main()
