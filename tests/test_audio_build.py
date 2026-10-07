import contextlib
import importlib.machinery
import importlib.util
import io
import json
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


class BlogAudioBuildTestCase(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.mkdtemp(prefix="blogaudio-build-test-")

        self.orig_root = blogctl.ROOT
        self.orig_content = blogctl.CONTENT
        self.orig_drafts = blogctl.DRAFTS
        self.orig_posts = blogctl.POSTS
        self.orig_pages = blogctl.PAGES
        self.orig_templates = blogctl.TEMPLATES
        self.orig_site_json = blogctl.SITE_JSON
        self.orig_lexikon_json = getattr(blogctl, "LEXIKON_JSON", os.path.join(blogctl.CONTENT, "lexikon.json"))
        self.orig_charts = getattr(blogctl, "CHARTS", os.path.join(blogctl.CONTENT, "charts"))
        self.orig_audio_dir = getattr(blogctl, "AUDIO_DIR", os.path.join(blogctl.CONTENT, "audio"))
        self.orig_audio_cache = getattr(blogctl, "AUDIO_CACHE", os.path.join(blogctl.ROOT, ".audio-cache"))

        # Redirect paths
        blogctl.ROOT = self.tmpdir
        blogctl.CONTENT = os.path.join(self.tmpdir, "content")
        blogctl.DRAFTS = os.path.join(blogctl.CONTENT, "drafts")
        blogctl.POSTS = os.path.join(blogctl.CONTENT, "posts")
        blogctl.PAGES = os.path.join(blogctl.CONTENT, "pages")
        blogctl.TEMPLATES = os.path.join(blogctl.CONTENT, "templates")
        blogctl.SITE_JSON = os.path.join(blogctl.CONTENT, "site.json")
        blogctl.LEXIKON_JSON = os.path.join(blogctl.CONTENT, "lexikon.json")
        blogctl.CHARTS = os.path.join(blogctl.CONTENT, "charts")
        blogctl.AUDIO_DIR = os.path.join(blogctl.CONTENT, "audio")
        blogctl.AUDIO_CACHE = os.path.join(self.tmpdir, ".audio-cache")
        os.environ["BLOGCTL_ROOT"] = self.tmpdir

        os.makedirs(blogctl.POSTS, exist_ok=True)
        os.makedirs(blogctl.DRAFTS, exist_ok=True)
        os.makedirs(blogctl.PAGES, exist_ok=True)
        os.makedirs(blogctl.CHARTS, exist_ok=True)
        os.makedirs(blogctl.AUDIO_DIR, exist_ok=True)

        orig_templates_dir = os.path.join(REPO_ROOT, "content", "templates")
        shutil.copytree(orig_templates_dir, blogctl.TEMPLATES)

        orig_site_path = os.path.join(REPO_ROOT, "content", "site.json")
        if os.path.isfile(orig_site_path):
            shutil.copy2(orig_site_path, blogctl.SITE_JSON)
        else:
            with open(blogctl.SITE_JSON, "w", encoding="utf-8") as f:
                json.dump({"title": "Test Blog", "description": "Test", "base_url": "https://example.com/blog", "lang": "de"}, f)

        orig_lexikon_path = os.path.join(REPO_ROOT, "content", "lexikon.json")
        if os.path.isfile(orig_lexikon_path):
            shutil.copy2(orig_lexikon_path, blogctl.LEXIKON_JSON)
        else:
            with open(blogctl.LEXIKON_JSON, "w", encoding="utf-8") as f:
                json.dump({}, f)

    def tearDown(self):
        blogctl.ROOT = self.orig_root
        blogctl.CONTENT = self.orig_content
        blogctl.DRAFTS = self.orig_drafts
        blogctl.POSTS = self.orig_posts
        blogctl.PAGES = self.orig_pages
        blogctl.TEMPLATES = self.orig_templates
        blogctl.SITE_JSON = self.orig_site_json
        blogctl.LEXIKON_JSON = self.orig_lexikon_json
        blogctl.CHARTS = self.orig_charts
        blogctl.AUDIO_DIR = self.orig_audio_dir
        blogctl.AUDIO_CACHE = self.orig_audio_cache
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

    def test_1_post_with_audio_renders_player_and_no_script(self):
        post_id = "post-mit-audio"
        self.create_post(post_id)

        # Create dummy mp3 (4,000,000 bytes -> 3.814... MB -> 3,8 MB)
        mp3_path = os.path.join(blogctl.AUDIO_DIR, f"{post_id}.mp3")
        with open(mp3_path, "wb") as f:
            f.write(b"\x00" * 4000000)

        # Create json metadata with seconds = 487.2 (8:07 Minuten)
        json_path = os.path.join(blogctl.AUDIO_DIR, f"{post_id}.json")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump({
                "id": post_id,
                "seconds": 487.2,
                "bytes": 4000000,
                "engine": "voxcpm2",
            }, f)

        out_dist = os.path.join(self.tmpdir, "dist")
        code, out, err = self.run_cli(["build", "--out", out_dist])
        self.assertEqual(code, 0, f"build failed: {err}")

        html_file = os.path.join(out_dist, f"{post_id}.html")
        self.assertTrue(os.path.isfile(html_file), f"{html_file} does not exist")

        with open(html_file, "r", encoding="utf-8") as f:
            content = f.read()

        self.assertIn("<audio", content)
        self.assertIn(f'src="audio/{post_id}.mp3"', content)
        self.assertIn("download", content)
        self.assertIn("8:07 Minuten", content)
        self.assertIn("3,8 MB", content)
        self.assertNotIn("<script", content)

    def test_2_build_copies_mp3_to_dist_audio_byte_identical(self):
        post_id = "post-audio-copy"
        self.create_post(post_id)

        dummy_bytes = b"ID3\x03\x00\x00\x00\x00\x00\x00some-audio-content-data"
        mp3_path = os.path.join(blogctl.AUDIO_DIR, f"{post_id}.mp3")
        with open(mp3_path, "wb") as f:
            f.write(dummy_bytes)

        out_dist = os.path.join(self.tmpdir, "dist")
        code, out, err = self.run_cli(["build", "--out", out_dist])
        self.assertEqual(code, 0, f"build failed: {err}")

        dist_mp3 = os.path.join(out_dist, "audio", f"{post_id}.mp3")
        self.assertTrue(os.path.isfile(dist_mp3), f"{dist_mp3} does not exist")
        with open(dist_mp3, "rb") as f:
            copied_bytes = f.read()
        self.assertEqual(copied_bytes, dummy_bytes)

    def test_3_post_without_audio_has_no_audio_block_and_no_dist_audio(self):
        post_id = "post-ohne-audio"
        self.create_post(post_id)

        out_dist = os.path.join(self.tmpdir, "dist")
        code, out, err = self.run_cli(["build", "--out", out_dist])
        self.assertEqual(code, 0, f"build failed: {err}")

        html_file = os.path.join(out_dist, f"{post_id}.html")
        self.assertTrue(os.path.isfile(html_file))
        with open(html_file, "r", encoding="utf-8") as f:
            content = f.read()

        self.assertNotIn("<audio", content)
        self.assertNotIn("audio/", content)
        self.assertNotIn("dist/audio", content)
        self.assertFalse(os.path.exists(os.path.join(out_dist, "audio")))

    def test_4_missing_json_renders_player_and_download_without_duration(self):
        post_id = "post-audio-no-json"
        self.create_post(post_id)

        # Create dummy mp3 (4,000,000 bytes -> 3,8 MB)
        mp3_path = os.path.join(blogctl.AUDIO_DIR, f"{post_id}.mp3")
        with open(mp3_path, "wb") as f:
            f.write(b"\x00" * 4000000)

        # Do NOT create .json metadata file
        json_path = os.path.join(blogctl.AUDIO_DIR, f"{post_id}.json")
        self.assertFalse(os.path.exists(json_path))

        out_dist = os.path.join(self.tmpdir, "dist")
        code, out, err = self.run_cli(["build", "--out", out_dist])
        self.assertEqual(code, 0, f"build failed: {err}")

        html_file = os.path.join(out_dist, f"{post_id}.html")
        self.assertTrue(os.path.isfile(html_file))
        with open(html_file, "r", encoding="utf-8") as f:
            content = f.read()

        self.assertIn("<audio", content)
        self.assertIn(f'src="audio/{post_id}.mp3"', content)
        self.assertIn("download", content)
        self.assertIn("3,8 MB", content)
        # Duration info should be omitted
        self.assertNotIn("Minuten", content)
        self.assertNotIn("<strong>", content)
        self.assertNotIn("<script", content)

    def test_5_feed_enclosure_for_audio_posts(self):
        p1 = "post-with-enclosure"
        p2 = "post-without-enclosure"
        self.create_post(p1, {"date": "2026-10-05"})
        self.create_post(p2, {"date": "2026-10-04"})

        # Audio file for p1 only
        p1_bytes = 3901234
        mp3_path = os.path.join(blogctl.AUDIO_DIR, f"{p1}.mp3")
        with open(mp3_path, "wb") as f:
            f.write(b"\x00" * p1_bytes)

        out_dist = os.path.join(self.tmpdir, "dist")
        code, out, err = self.run_cli(["build", "--out", out_dist])
        self.assertEqual(code, 0, f"build failed: {err}")

        feed_path = os.path.join(out_dist, "feed.xml")
        self.assertTrue(os.path.isfile(feed_path))
        with open(feed_path, "r", encoding="utf-8") as f:
            feed_content = f.read()

        # Check p1 has enclosure
        expected_enclosure = (
            f'<enclosure url="https://hermiethetermi.github.io/hermies-blog/audio/{p1}.mp3" '
            f'length="{p1_bytes}" type="audio/mpeg"/>'
        )
        self.assertIn(expected_enclosure, feed_content)

        # Split items to ensure p2 does not have enclosure
        items = feed_content.split("<item>")
        p2_item = None
        for item in items[1:]:
            if f"<link>https://hermiethetermi.github.io/hermies-blog/{p2}.html</link>" in item:
                p2_item = item
                break
        self.assertIsNotNone(p2_item, "p2 item not found in feed")
        self.assertNotIn("<enclosure", p2_item)

    def test_6_check_audio_rules(self):
        # 1. Published article without .mp3 -> warning, exit 0
        self.create_post("pub-no-mp3")
        code, out, err = self.run_cli(["check"])
        self.assertEqual(code, 0)
        combined_output = out + err
        self.assertIn("pub-no-mp3: keine Hörfassung (content/audio/pub-no-mp3.mp3 fehlt)", combined_output)

        # 2. Draft article without .mp3 -> no warning
        draft_path = os.path.join(blogctl.DRAFTS, "draft-no-mp3.md")
        blogctl.write_article(draft_path, {
            "title": "Draft",
            "slug": "draft-no-mp3",
            "date": "2026-10-04",
            "status": "draft",
            "tags": ["news"],
            "summary": "Draft summary",
            "lang": "de",
        }, "Draft Body")

        code2, out2, err2 = self.run_cli(["check"])
        self.assertEqual(code2, 0)
        self.assertNotIn("draft-no-mp3: keine Hörfassung", out2 + err2)

        # 3. .mp3 exists without .txt -> warning
        with open(os.path.join(blogctl.AUDIO_DIR, "pub-no-mp3.mp3"), "wb") as f:
            f.write(b"dummy")
        # Ensure .txt does NOT exist
        txt_path = os.path.join(blogctl.AUDIO_DIR, "pub-no-mp3.txt")
        if os.path.exists(txt_path):
            os.remove(txt_path)

        code3, out3, err3 = self.run_cli(["check"])
        self.assertEqual(code3, 0)
        self.assertIn("pub-no-mp3.txt", out3 + err3)

        # 4. Broken .json -> error, exit 1
        with open(os.path.join(blogctl.AUDIO_DIR, "pub-no-mp3.json"), "w", encoding="utf-8") as f:
            f.write("{broken json:")

        code4, out4, err4 = self.run_cli(["check"])
        self.assertEqual(code4, 1)
        self.assertIn("pub-no-mp3.json", out4 + err4)

    def test_7_deterministic_builds(self):
        post_audio = "determ-audio"
        post_plain = "determ-plain"
        self.create_post(post_audio, {"date": "2026-10-05"})
        self.create_post(post_plain, {"date": "2026-10-04"})

        # Audio + JSON for determ-audio
        mp3_path = os.path.join(blogctl.AUDIO_DIR, f"{post_audio}.mp3")
        with open(mp3_path, "wb") as f:
            f.write(b"\x00" * 2000000)
        with open(os.path.join(blogctl.AUDIO_DIR, f"{post_audio}.json"), "w", encoding="utf-8") as f:
            json.dump({"seconds": 125.0}, f)

        # Build 1
        dist1 = os.path.join(self.tmpdir, "dist1")
        code1, _, err1 = self.run_cli(["build", "--out", dist1])
        self.assertEqual(code1, 0, f"build 1 failed: {err1}")

        # Build 2
        dist2 = os.path.join(self.tmpdir, "dist2")
        code2, _, err2 = self.run_cli(["build", "--out", dist2])
        self.assertEqual(code2, 0, f"build 2 failed: {err2}")

        # Compare <id>.html and feed.xml byte-for-byte
        for rel in [f"{post_audio}.html", f"{post_plain}.html", "feed.xml"]:
            f1 = os.path.join(dist1, rel)
            f2 = os.path.join(dist2, rel)
            with open(f1, "rb") as h1, open(f2, "rb") as h2:
                self.assertEqual(h1.read(), h2.read(), f"{rel} differs between builds!")

    def test_8_style_css_audio_rules(self):
        style_path = os.path.join(REPO_ROOT, "content", "templates", "style.css")
        with open(style_path, "r", encoding="utf-8") as f:
            css_content = f.read()

        self.assertIn(".post-audio", css_content)
        self.assertIn(".post-audio-label", css_content)
        self.assertIn("max-width: 100%", css_content)


if __name__ == "__main__":
    unittest.main()
