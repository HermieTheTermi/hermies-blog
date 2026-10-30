import json
import os
import shutil
import sys
import tempfile
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO_ROOT, "tests"))
from test_time import blogctl  # laedt blogctl als Modul und stellt Pfade bereit


class BausteineTestCase(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.mkdtemp(prefix="blogbausteine-test-")
        self._orig = {
            name: getattr(blogctl, name)
            for name in ("ROOT", "CONTENT", "DRAFTS", "POSTS", "PAGES", "ASSETS",
                         "TEMPLATES", "SITE_JSON", "SOURCE_JSON", "WIDGETS", "CHARTS",
                         "AUDIO_DIR", "RELEASE_STATE")
            if hasattr(blogctl, name)
        }
        blogctl.ROOT = self.tmpdir
        blogctl.CONTENT = os.path.join(self.tmpdir, "content")
        blogctl.DRAFTS = os.path.join(blogctl.CONTENT, "drafts")
        blogctl.POSTS = os.path.join(blogctl.CONTENT, "posts")
        blogctl.PAGES = os.path.join(blogctl.CONTENT, "pages")
        blogctl.ASSETS = os.path.join(self.tmpdir, "assets")
        blogctl.TEMPLATES = os.path.join(blogctl.CONTENT, "templates")
        blogctl.SITE_JSON = os.path.join(blogctl.CONTENT, "site.json")
        blogctl.SOURCE_JSON = os.path.join(blogctl.CONTENT, "sources.json")
        blogctl.WIDGETS = os.path.join(blogctl.CONTENT, "widgets")
        blogctl.CHARTS = os.path.join(blogctl.CONTENT, "charts")
        blogctl.AUDIO_DIR = os.path.join(blogctl.CONTENT, "audio")
        blogctl.RELEASE_STATE = os.path.join(blogctl.CONTENT, "releases.json")

        shutil.copytree(os.path.join(REPO_ROOT, "content", "templates"), blogctl.TEMPLATES)
        blogctl.ensure_dirs()

    def tearDown(self):
        for name, value in self._orig.items():
            setattr(blogctl, name, value)
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    def write_widget(self, name, data):
        with open(os.path.join(blogctl.WIDGETS, name + ".json"), "w", encoding="utf-8") as fh:
            json.dump(data, fh, ensure_ascii=False)

    # --- Bausteine ---------------------------------------------------------

    def test_widgets_render_without_markers(self):
        self.write_widget("zahlen1", {"typ": "zahlen", "werte": [{"wert": "4,1", "label": "SIC"}]})
        self.write_widget("zeit1", {"typ": "zeitleiste",
                                    "ereignisse": [{"datum": "15.10.2026", "titel": "Start"}]})
        self.write_widget("schritt1", {"typ": "schritte", "schritte": [{"titel": "Erstens"}]})
        self.write_widget("tab1", {"typ": "tabelle", "spalten": ["A", "B"],
                                   "zeilen": [["eins", "zwei"]], "betont": 1})
        self.write_widget("skala1", {"typ": "skala",
                                     "werte": [{"label": "klein", "wert": 1},
                                               {"label": "gross", "wert": 1000}]})
        self.write_widget("vergleich1", {"typ": "vergleich",
                                         "links": {"titel": "Alt", "punkte": ["a"]},
                                         "rechts": {"titel": "Neu", "punkte": ["b"]}})

        body = "\n\n".join([
            "Text davor.",
            "{{zahlen:zahlen1}}",
            "{{zeitleiste:zeit1}}",
            "{{schritte:schritt1}}",
            "{{tabelle:tab1}}",
            "{{skala:skala1}}",
            "{{vergleich:vergleich1}}",
        ])
        html = blogctl.render_markdown(body)
        self.assertNotIn("{{", html)
        self.assertNotIn("<script", html)
        for cls in ("stat-value", "timeline", "step-num", "data-table",
                    "scale-fill", "compare-col", "col-emphasis"):
            self.assertIn(cls, html)
        # Marker duerfen nicht als Fließtext im Absatz landen
        self.assertNotIn("<p>{{", html)

    def test_boxes_render(self):
        body = "\n".join([
            "::: merk",
            "Kurz und knapp.",
            ":::",
            "",
            "::: warnung Der Haken",
            "Es fehlt die Fehlerrechnung.",
            ":::",
            "",
            "::: definition",
            "Ein Grundmodell ist einmal breit trainiert.",
            ":::",
            "",
            "::: zitat Eine Quelle",
            "Ein Satz zum Zitieren.",
            ":::",
            "",
            "::: aufklappen Details",
            "Mehr Text.",
            ":::",
        ])
        html = blogctl.render_markdown(body)
        self.assertIn("box-merk", html)
        self.assertIn("box-warnung", html)
        self.assertIn("Der Haken", html)
        self.assertIn("box-definition", html)
        self.assertIn("pullquote", html)
        self.assertIn("Eine Quelle", html)
        self.assertIn("<details", html)
        self.assertNotIn(":::", html)

    def test_lexikon_marker_inside_box_is_rendered(self):
        lexikon = {"Testbegriff": "Kurze Erklaerung."}
        orig = blogctl.load_lexikon
        blogctl.load_lexikon = lambda path=None: lexikon
        try:
            html = blogctl.render_markdown("::: merk\nEin {{Testbegriff}} im Kasten.\n:::")
        finally:
            blogctl.load_lexikon = orig
        self.assertIn('class="lex"', html)
        self.assertIn("lex-testbegriff", html)

    def test_unclosed_box_is_an_error(self):
        with self.assertRaises(ValueError):
            blogctl.render_markdown("::: merk\nText ohne Ende\n")
        self.assertTrue(blogctl.validate_markup("::: merk\nText ohne Ende"))

    def test_stray_closer_is_an_error(self):
        self.assertTrue(blogctl.validate_markup("Text\n:::\nmehr Text"))

    def test_unknown_box_type_is_an_error(self):
        self.assertTrue(blogctl.validate_markup("::: kaffee\nText\n:::"))

    def test_widget_marker_must_stand_alone(self):
        errs = blogctl.validate_markup("Ein Satz {{zahlen:foo}} im Fließtext.")
        self.assertTrue(errs)
        self.assertIn("allein", errs[0])
        self.assertEqual(blogctl.validate_markup("{{zahlen:foo}}"), [])

    def test_missing_widget_file_is_reported(self):
        err = blogctl.validate_widget("zahlen", "gibtsnicht")
        self.assertIsNotNone(err)
        self.assertIn("fehlt", err)

    def test_widget_type_mismatch_is_reported(self):
        self.write_widget("falsch1", {"typ": "tabelle", "spalten": ["A"], "zeilen": [["x"]]})
        with self.assertRaises(ValueError):
            blogctl.render_widget("zahlen", "falsch1")

    def test_widget_requires_fields(self):
        self.write_widget("leer1", {"typ": "zahlen"})
        with self.assertRaises(ValueError):
            blogctl.render_widget("zahlen", "leer1")

    def test_skala_rejects_zero_on_log_scale(self):
        self.write_widget("null1", {"typ": "skala", "werte": [{"label": "null", "wert": 0}]})
        with self.assertRaises(ValueError):
            blogctl.render_widget("skala", "null1")

    def test_tabelle_row_length_must_match(self):
        self.write_widget("tab2", {"typ": "tabelle", "spalten": ["A", "B"], "zeilen": [["nur eine"]]})
        with self.assertRaises(ValueError):
            blogctl.render_widget("tabelle", "tab2")

    def test_build_is_deterministic(self):
        self.write_widget("zahlen2", {"typ": "zahlen", "werte": [{"wert": "1", "label": "x"}]})
        post_id = "demo-bausteine"
        with open(os.path.join(blogctl.POSTS, post_id + ".md"), "w", encoding="utf-8") as fh:
            fh.write("---\ntitle: Demo\nslug: %s\ndate: 2026-10-30\nstatus: published\n"
                     "tags: [news]\nsummary: Demo\nlang: de\n---\n\n"
                     "## TL;DR\n\n- Eins.\n\n::: merk\nKern.\n:::\n\n{{zahlen:zahlen2}}\n" % post_id)
        out_a = os.path.join(self.tmpdir, "dist_a")
        out_b = os.path.join(self.tmpdir, "dist_b")
        blogctl.do_build(out_a)
        blogctl.do_build(out_b)
        self._assert_same_tree(out_a, out_b)
        with open(os.path.join(out_a, post_id + ".html"), encoding="utf-8") as fh:
            html = fh.read()
        self.assertIn("box-merk", html)
        self.assertIn("stat-value", html)
        self.assertNotIn("{{", html)
        self.assertNotIn("<script", html)

    def _assert_same_tree(self, one, two):
        names_one = sorted(os.listdir(one))
        names_two = sorted(os.listdir(two))
        self.assertEqual(names_one, names_two)
        for name in names_one:
            if name.endswith(".html") or name.endswith(".css"):
                with open(os.path.join(one, name), "rb") as fa, open(os.path.join(two, name), "rb") as fb:
                    self.assertEqual(fa.read(), fb.read(), "Build ist nicht deterministisch: %s" % name)


if __name__ == "__main__":
    unittest.main(verbosity=2)
