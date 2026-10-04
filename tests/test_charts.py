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


class BlogChartsTestCase(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.mkdtemp(prefix="blogcharts-test-")
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
        self.orig_charts = getattr(blogctl, "CHARTS", os.path.join(blogctl.CONTENT, "charts"))

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
        blogctl.CHARTS = os.path.join(blogctl.CONTENT, "charts")
        os.environ["BLOGCTL_ROOT"] = self.tmpdir

        # Copy original templates to sandbox
        orig_templates_dir = os.path.join(REPO_ROOT, "content", "templates")
        shutil.copytree(orig_templates_dir, blogctl.TEMPLATES)

        # Copy original lexikon.json to sandbox if exists
        orig_lexikon_path = os.path.join(REPO_ROOT, "content", "lexikon.json")
        os.makedirs(blogctl.CONTENT, exist_ok=True)
        if os.path.isfile(orig_lexikon_path):
            shutil.copy2(orig_lexikon_path, blogctl.LEXIKON_JSON)

        os.makedirs(blogctl.CHARTS, exist_ok=True)
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
        blogctl.CHARTS = self.orig_charts
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
        lines = ["---"]
        for k in blogctl.FIELD_ORDER:
            if k in fm and fm[k] is not None:
                val = fm[k]
                if isinstance(val, list):
                    lines.append(f"{k}: [{', '.join(str(x) for x in val)}]")
                else:
                    lines.append(f"{k}: {val}")
        lines.append("---")
        lines.append("")
        lines.append(body)
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        return path

    def create_chart(self, chart_name, data):
        os.makedirs(blogctl.CHARTS, exist_ok=True)
        chart_path = os.path.join(blogctl.CHARTS, f"{chart_name}.json")
        with open(chart_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return chart_path

    # 1. Komma-Formatierung deutscher Zahlen (1.200, 5,5)
    def test_1_german_number_formatting(self):
        self.assertTrue(hasattr(blogctl, "format_german_number"), "blogctl muss format_german_number implementieren")
        fn = getattr(blogctl, "format_german_number")
        self.assertEqual(fn(415), "415")
        self.assertEqual(fn(1200), "1.200")
        self.assertEqual(fn(5.5), "5,5")
        self.assertEqual(fn(7.9), "7,9")
        self.assertEqual(fn(0.24), "0,24")
        self.assertEqual(fn(72.36), "72,36")
        self.assertEqual(fn(1200000), "1.200.000")
        self.assertEqual(fn(1200.5), "1.200,5")

    # 2. Balken aus werte erzeugen SVG mit allen Labels und Werten
    def test_2_balken_single_series(self):
        chart_data = {
            "titel": "Stromverbrauch der Rechenzentren weltweit",
            "einheit": "TWh",
            "typ": "balken",
            "werte": [
                {"label": "2024", "wert": 415},
                {"label": "2025", "wert": 485},
                {"label": "2030", "wert": 945},
                {"label": "2035", "wert": 1200}
            ],
            "quelle": "IEA",
            "quelle_url": "https://www.iea.org",
            "hinweis": "Projektion"
        }
        self.create_chart("strom", chart_data)
        self.create_post("strom-post", body="Hier ist das Diagramm:\n\n{{chart:strom}}\n\nEnde.")

        dist_dir = os.path.join(self.tmpdir, "dist")
        code, out, err = self.run_cli(["build", "--out", dist_dir])
        self.assertEqual(code, 0, f"build failed: {err}")

        post_path = os.path.join(dist_dir, "strom-post.html")
        with open(post_path, "r", encoding="utf-8") as f:
            post_html = f.read()

        # Check inline SVG
        self.assertIn("<svg", post_html)
        self.assertIn('viewBox="', post_html)
        self.assertIn('role="img"', post_html)
        self.assertIn("<title>Stromverbrauch der Rechenzentren weltweit</title>", post_html)

        # Check all labels and formatted values are present in SVG
        self.assertIn("2024", post_html)
        self.assertIn("2025", post_html)
        self.assertIn("2030", post_html)
        self.assertIn("2035", post_html)
        self.assertIn("415", post_html)
        self.assertIn("485", post_html)
        self.assertIn("945", post_html)
        self.assertIn("1.200", post_html)

        # Check unit and hint
        self.assertIn("TWh", post_html)
        self.assertIn("Projektion", post_html)

    # 3. Gruppierte Balken mit Legende
    def test_3_balken_grouped_with_legend(self):
        chart_data = {
            "titel": "Mensch gegen Modell",
            "einheit": "%",
            "typ": "balken",
            "gruppen": ["GAIA", "OSWorld"],
            "reihen": [
                {"name": "Mensch", "werte": [92, 72.36]},
                {"name": "Bestes Modell", "werte": [15, 12.24]}
            ],
            "quelle": "Benchmarking Org",
            "quelle_url": "https://example.org/bench"
        }
        self.create_chart("mensch-modell", chart_data)
        self.create_post("benchmark-post", body="Ergebnisse:\n\n{{chart:mensch-modell}}\n")

        dist_dir = os.path.join(self.tmpdir, "dist")
        code, out, err = self.run_cli(["build", "--out", dist_dir])
        self.assertEqual(code, 0, f"build failed: {err}")

        post_path = os.path.join(dist_dir, "benchmark-post.html")
        with open(post_path, "r", encoding="utf-8") as f:
            post_html = f.read()

        # Check group labels
        self.assertIn("GAIA", post_html)
        self.assertIn("OSWorld", post_html)

        # Check series values formatted
        self.assertIn("92", post_html)
        self.assertIn("72,36", post_html)
        self.assertIn("15", post_html)
        self.assertIn("12,24", post_html)

        # Check legend exists with series names
        self.assertIn("Mensch", post_html)
        self.assertIn("Bestes Modell", post_html)

    # 4. Liniendiagramm mit mehreren Reihen
    def test_4_linie_multi_series(self):
        chart_data = {
            "titel": "Energie pro Anfrage",
            "einheit": "Wh",
            "typ": "linie",
            "x": ["2024", "2025", "2026"],
            "reihen": [
                {"name": "Modell A", "werte": [7.9, 0.24, 0.2]},
                {"name": "Modell B", "werte": [12.0, 3.5, 1.1]}
            ],
            "quelle": "Google (2025)",
            "quelle_url": "https://cloud.google.com"
        }
        self.create_chart("energie", chart_data)
        self.create_post("energie-post", body="Verlauf:\n\n{{chart:energie}}\n")

        dist_dir = os.path.join(self.tmpdir, "dist")
        code, out, err = self.run_cli(["build", "--out", dist_dir])
        self.assertEqual(code, 0, f"build failed: {err}")

        post_path = os.path.join(dist_dir, "energie-post.html")
        with open(post_path, "r", encoding="utf-8") as f:
            post_html = f.read()

        # Check x labels
        self.assertIn("2024", post_html)
        self.assertIn("2025", post_html)
        self.assertIn("2026", post_html)

        # Check values
        self.assertIn("7,9", post_html)
        self.assertIn("0,24", post_html)
        self.assertIn("0,2", post_html)
        self.assertIn("12", post_html)
        self.assertIn("3,5", post_html)
        self.assertIn("1,1", post_html)

        # Check legend
        self.assertIn("Modell A", post_html)
        self.assertIn("Modell B", post_html)

        # Check line elements and points
        self.assertIn("<polyline", post_html)
        self.assertIn("<circle", post_html)

    # 5. <figure>/<figcaption> mit Titel und Quellenlink
    def test_5_figure_and_figcaption(self):
        chart_data = {
            "titel": "Stromverbrauch der Rechenzentren weltweit",
            "einheit": "TWh",
            "typ": "balken",
            "werte": [{"label": "2024", "wert": 415}],
            "quelle": "IEA, Energy and AI",
            "quelle_url": "https://www.iea.org/reports/energy-and-ai",
            "hinweis": "2024 Schätzung"
        }
        self.create_chart("strom-fig", chart_data)
        self.create_post("fig-post", body="Test:\n\n{{chart:strom-fig}}\n")

        dist_dir = os.path.join(self.tmpdir, "dist")
        code, out, err = self.run_cli(["build", "--out", dist_dir])
        self.assertEqual(code, 0, f"build failed: {err}")

        post_path = os.path.join(dist_dir, "fig-post.html")
        with open(post_path, "r", encoding="utf-8") as f:
            post_html = f.read()

        # Check <figure> and <figcaption>
        self.assertIn("<figure", post_html)
        self.assertIn("<figcaption", post_html)

        # Check title is in SVG, but NOT in figcaption
        fig_match = re.search(r"<figcaption[\s\S]*?</figcaption>", post_html)
        self.assertIsNotNone(fig_match)
        caption_html = fig_match.group(0)
        self.assertNotIn("Stromverbrauch der Rechenzentren weltweit", caption_html)

        # Check source link with rel="noopener"
        self.assertIn('href="https://www.iea.org/reports/energy-and-ai"', post_html)
        self.assertIn('rel="noopener"', post_html)
        self.assertIn("IEA, Energy and AI", post_html)
        self.assertIn("2024 Schätzung", post_html)

        # Check hint appears exactly once in figure (only in figcaption, not in SVG)
        figure_match = re.search(r"<figure[\s\S]*?</figure>", post_html)
        self.assertIsNotNone(figure_match)
        figure_html = figure_match.group(0)
        self.assertEqual(figure_html.count("2024 Schätzung"), 1)

    # 6. Kaputte/fehlende Chart-Datei -> check schlägt fehl; Backtick-Code wird ignoriert
    def test_6_check_validation(self):
        # A: Missing chart file
        self.create_post("missing-chart-post", body="Hier fehlt was:\n\n{{chart:nichtda}}\n")
        code, out, err = self.run_cli(["check"])
        self.assertNotEqual(code, 0, "check muss bei fehlender Chart-Datei fehlschlagen")
        self.assertIn("nichtda", out + err)

        # Clean up
        os.remove(os.path.join(blogctl.POSTS, "missing-chart-post.md"))

        # B: Broken JSON
        broken_path = os.path.join(blogctl.CHARTS, "kaputt.json")
        with open(broken_path, "w", encoding="utf-8") as f:
            f.write("{ ungueltiges json: 123")
        self.create_post("broken-chart-post", body="Hier ist kaputt:\n\n{{chart:kaputt}}\n")
        code, out, err = self.run_cli(["check"])
        self.assertNotEqual(code, 0, "check muss bei kaputtem JSON fehlschlagen")
        self.assertIn("kaputt", out + err)

        # Clean up
        os.remove(os.path.join(blogctl.POSTS, "broken-chart-post.md"))
        os.remove(broken_path)

        # C: Backtick code is ignored
        self.create_post("backtick-chart-post", body="Code: `{{chart:nichtda}}` im Text.")
        code, out, err = self.run_cli(["check"])
        self.assertEqual(code, 0, f"check darf bei Marker in Backticks keinen Fehler werfen: {out} {err}")

    # 7. Kein <script, kein <img, kein http-Verweis außer dem Quellenlink des Diagramms
    def test_7_no_script_no_img_external_resources(self):
        chart_data = {
            "titel": "Testdiagramm",
            "einheit": "x",
            "typ": "balken",
            "werte": [{"label": "A", "wert": 10}],
            "quelle": "Testquelle",
            "quelle_url": "https://example.com/source"
        }
        self.create_chart("clean-test", chart_data)
        self.create_post("clean-post", body="Diagramm:\n\n{{chart:clean-test}}\n")

        dist_dir = os.path.join(self.tmpdir, "dist")
        code, out, err = self.run_cli(["build", "--out", dist_dir])
        self.assertEqual(code, 0, f"build failed: {err}")

        post_path = os.path.join(dist_dir, "clean-post.html")
        with open(post_path, "r", encoding="utf-8") as f:
            post_html = f.read()

        # No <script> tags anywhere
        self.assertNotIn("<script", post_html)
        # No <img> tags
        self.assertNotIn("<img", post_html)

        # Extract figure block
        fig_match = re.search(r"<figure[\s\S]*?</figure>", post_html)
        self.assertIsNotNone(fig_match)
        fig_html = fig_match.group(0)

        # Inside SVG, no external http links (xmlns="http://www.w3.org/2000/svg" is allowed)
        svg_match = re.search(r"<svg[\s\S]*?</svg>", fig_html)
        self.assertIsNotNone(svg_match)
        svg_html = svg_match.group(0)
        svg_urls = re.findall(r'https?://[^\s"\'<>]+', svg_html)
        for u in svg_urls:
            self.assertEqual(u, "http://www.w3.org/2000/svg", f"Unerwartete externe URL in SVG: {u}")

        # In figure outside SVG, only quelle_url
        non_svg_fig = fig_html.replace(svg_html, "")
        fig_urls = re.findall(r'https?://[^\s"\'<>]+', non_svg_fig)
        self.assertEqual(fig_urls, ["https://example.com/source"])

    # 8. Zwei Builds -> identische Hashes (Determinismus)
    def test_8_determinism(self):
        chart_data = {
            "titel": "Stromverbrauch",
            "einheit": "TWh",
            "typ": "balken",
            "werte": [
                {"label": "2024", "wert": 415},
                {"label": "2025", "wert": 485}
            ],
            "quelle": "IEA",
            "quelle_url": "https://www.iea.org",
            "hinweis": "Schätzung"
        }
        self.create_chart("determ-chart", chart_data)
        self.create_post("determ-post", body="Text:\n\n{{chart:determ-chart}}\n")

        dist1 = os.path.join(self.tmpdir, "dist1")
        dist2 = os.path.join(self.tmpdir, "dist2")

        code1, _, _ = self.run_cli(["build", "--out", dist1])
        code2, _, _ = self.run_cli(["build", "--out", dist2])
        self.assertEqual(code1, 0)
        self.assertEqual(code2, 0)

        with open(os.path.join(dist1, "determ-post.html"), "rb") as f:
            h1 = hashlib.sha256(f.read()).hexdigest()
        with open(os.path.join(dist2, "determ-post.html"), "rb") as f:
            h2 = hashlib.sha256(f.read()).hexdigest()

        self.assertEqual(h1, h2, "Zwei Builds muessen byte-identische Ausgaben erzeugen")

    # 9. blogctl charts [--json]
    def test_9_charts_command(self):
        c1 = {"titel": "Strom", "typ": "balken", "werte": [{"label": "A", "wert": 1}]}
        c2 = {"titel": "Kosten", "typ": "linie", "x": ["A"], "reihen": [{"name": "R1", "werte": [1]}]}
        self.create_chart("strom", c1)
        self.create_chart("kosten", c2)

        # Test text output
        code, out, err = self.run_cli(["charts"])
        self.assertEqual(code, 0, f"blogctl charts failed: {err}")
        self.assertIn("strom", out)
        self.assertIn("Strom", out)
        self.assertIn("balken", out)
        self.assertIn("kosten", out)
        self.assertIn("Kosten", out)
        self.assertIn("linie", out)

        # Test json output
        code, out, err = self.run_cli(["charts", "--json"])
        self.assertEqual(code, 0, f"blogctl charts --json failed: {err}")
        parsed = json.loads(out)
        self.assertIn("charts", parsed)
        charts_by_name = {c["name"]: c for c in parsed["charts"]}
        self.assertIn("strom", charts_by_name)
        self.assertEqual(charts_by_name["strom"]["titel"], "Strom")
        self.assertEqual(charts_by_name["strom"]["typ"], "balken")
        self.assertIn("kosten", charts_by_name)
        self.assertEqual(charts_by_name["kosten"]["titel"], "Kosten")
        self.assertEqual(charts_by_name["kosten"]["typ"], "linie")

    # 10. Titelumbruch bei langem Titel, <tspan>, keine Ellipse bei normal langem Titel, viewBox-Höhe gewachsen
    def test_10_long_title_wrap_and_viewbox(self):
        c_short = {
            "titel": "Stromverbrauch",
            "einheit": "TWh",
            "typ": "balken",
            "werte": [{"label": "2024", "wert": 415}]
        }
        long_title = "Energie pro Anfrage: kurz antworten oder lange rechnen"
        c_long = {
            "titel": long_title,
            "einheit": "Wh",
            "typ": "balken",
            "werte": [{"label": "kurz", "wert": 0.31}, {"label": "lang", "wert": 3.91}],
            "hinweis": "Medianwerte"
        }
        self.create_chart("c-short", c_short)
        self.create_chart("c-long", c_long)
        self.create_post("title-post", body="{{chart:c-short}}\n\n{{chart:c-long}}")

        dist_dir = os.path.join(self.tmpdir, "dist")
        code, out, err = self.run_cli(["build", "--out", dist_dir])
        self.assertEqual(code, 0, f"build failed: {err}")

        post_path = os.path.join(dist_dir, "title-post.html")
        with open(post_path, "r", encoding="utf-8") as f:
            post_html = f.read()

        svgs = re.findall(r"<svg[\s\S]*?</svg>", post_html)
        self.assertEqual(len(svgs), 2)
        svg_short, svg_long = svgs[0], svgs[1]

        # 1. Langer Titel erscheint vollstaendig in mindestens einem <tspan>-Element, ohne "…"
        self.assertIn("<tspan", svg_long)
        self.assertNotIn("…", svg_long)

        tspans_long = re.findall(r"<tspan[^>]*>(.*?)</tspan>", svg_long)
        self.assertTrue(len(tspans_long) >= 2, "Zweizeiliger Titel muss mindestens zwei tspans haben")
        combined_title = " ".join(t.strip() for t in tspans_long)
        self.assertEqual(combined_title, long_title, "Langer Titel muss vollstaendig in tspans stehen")

        # Vollstaendiger Titel steht zusaetzlich im <title>-Element
        self.assertIn(f"<title>{long_title}</title>", svg_long)

        # 2. viewBox-Hoehe bei langem Titel > bei kurzem Titel
        vb_short = re.search(r'viewBox="0 0 (\d+) (\d+)"', svg_short)
        vb_long = re.search(r'viewBox="0 0 (\d+) (\d+)"', svg_long)
        self.assertIsNotNone(vb_short)
        self.assertIsNotNone(vb_long)
        h_short = int(vb_short.group(2))
        h_long = int(vb_long.group(2))
        self.assertGreater(h_long, h_short, f"viewBox-Hoehe bei langem Titel ({h_long}) muss groesser sein als bei kurzem Titel ({h_short})")

    # 11. Keine Dopplung: Titel steht nicht in figcaption, Hinweis nicht im SVG und genau 1x in figure
    def test_11_no_duplication_in_caption_and_svg(self):
        title = "Energie pro Anfrage: kurz antworten oder lange rechnen"
        hint = "Medianwerte der Modellierung"
        chart_data = {
            "titel": title,
            "einheit": "Wh",
            "typ": "balken",
            "werte": [{"label": "A", "wert": 1}],
            "quelle": "Joule (2026)",
            "quelle_url": "https://example.com/joule",
            "hinweis": hint
        }
        self.create_chart("no-dup", chart_data)
        self.create_post("no-dup-post", body="{{chart:no-dup}}")

        dist_dir = os.path.join(self.tmpdir, "dist")
        code, out, err = self.run_cli(["build", "--out", dist_dir])
        self.assertEqual(code, 0, f"build failed: {err}")

        post_path = os.path.join(dist_dir, "no-dup-post.html")
        with open(post_path, "r", encoding="utf-8") as f:
            post_html = f.read()

        figure_match = re.search(r"<figure[\s\S]*?</figure>", post_html)
        self.assertIsNotNone(figure_match)
        fig_html = figure_match.group(0)

        svg_match = re.search(r"<svg[\s\S]*?</svg>", fig_html)
        self.assertIsNotNone(svg_match)
        svg_html = svg_match.group(0)

        caption_match = re.search(r"<figcaption[\s\S]*?</figcaption>", fig_html)
        self.assertIsNotNone(caption_match)
        caption_html = caption_match.group(0)

        # Titel steht im SVG, aber NICHT in der <figcaption>
        self.assertIn("<title>" + title + "</title>", svg_html)
        self.assertNotIn(title, caption_html)
        self.assertNotIn("chart-title", caption_html)

        # Hinweis erscheint NICHT im SVG, sondern nur in der <figcaption>
        self.assertNotIn(hint, svg_html)
        self.assertIn(hint, caption_html)

        # Hinweis kommt genau einmal in der Figure vor
        self.assertEqual(fig_html.count(hint), 1)

    # 12. Sehr langer Titel (> 110 Zeichen) darf am Ende der 2. Zeile mit "…" gekuerzt werden; <title> bleibt vollstaendig
    def test_12_very_long_title_truncation(self):
        very_long_title = "Dies ist ein ausserordentlich langer Diagrammtitel der weit ueber einhundertzehn Zeichen enthaelt und daher zweizeilig gekuerzt werden muss"
        self.assertGreater(len(very_long_title), 110)
        chart_data = {
            "titel": very_long_title,
            "typ": "balken",
            "werte": [{"label": "A", "wert": 1}]
        }
        self.create_chart("very-long", chart_data)
        self.create_post("very-long-post", body="{{chart:very-long}}")

        dist_dir = os.path.join(self.tmpdir, "dist")
        code, out, err = self.run_cli(["build", "--out", dist_dir])
        self.assertEqual(code, 0, f"build failed: {err}")

        post_path = os.path.join(dist_dir, "very-long-post.html")
        with open(post_path, "r", encoding="utf-8") as f:
            post_html = f.read()

        svg_match = re.search(r"<svg[\s\S]*?</svg>", post_html)
        self.assertIsNotNone(svg_match)
        svg_html = svg_match.group(0)

        # <title> enthaelt vollstaendigen Titel
        self.assertIn(f"<title>{very_long_title}</title>", svg_html)

        # SVG enthaelt tspans, und die 2. Zeile endet mit "…"
        tspans = re.findall(r"<tspan[^>]*>(.*?)</tspan>", svg_html)
        self.assertEqual(len(tspans), 2)
        self.assertTrue(tspans[1].endswith("…"))

    # 13. balken-horizontal: liegende Balken, alle Labels vollständig ohne Kürzung, deutsche Werte
    def test_13_balken_horizontal(self):
        chart_data = {
            "titel": "Agenten-Benchmarks im Vergleich",
            "einheit": "% Erfolgsrate",
            "typ": "balken-horizontal",
            "werte": [
                {"label": "WebArena (Webaufgaben)", "wert": 35.8},
                {"label": "SWE-bench Verified", "wert": 48.9},
                {"label": "GAIA (multimodal)", "wert": 67.2},
                {"label": "OSWorld (Desktop)", "wert": 12.5}
            ],
            "quelle": "Benchmarking Report 2026",
            "quelle_url": "https://example.org/benchmarks",
            "hinweis": "Stand Q3 2026"
        }
        self.create_chart("benchmarks-horiz", chart_data)
        self.create_post("horiz-post", body="Vergleich:\n\n{{chart:benchmarks-horiz}}\n")

        dist_dir = os.path.join(self.tmpdir, "dist")
        code, out, err = self.run_cli(["build", "--out", dist_dir])
        self.assertEqual(code, 0, f"build failed: {err}")

        post_path = os.path.join(dist_dir, "horiz-post.html")
        with open(post_path, "r", encoding="utf-8") as f:
            post_html = f.read()

        # Check inline SVG
        self.assertIn("<svg", post_html)
        self.assertIn('role="img"', post_html)
        self.assertIn("<title>Agenten-Benchmarks im Vergleich</title>", post_html)
        self.assertNotIn("{{", post_html)
        self.assertNotIn("<script", post_html)
        self.assertNotIn("<img", post_html)

        # Labels muessen vollstaendig im SVG sein (kein Abschneiden, kein "…")
        svg_match = re.search(r"<svg[\s\S]*?</svg>", post_html)
        self.assertIsNotNone(svg_match)
        svg_html = svg_match.group(0)

        self.assertIn("WebArena (Webaufgaben)", svg_html)
        self.assertIn("SWE-bench Verified", svg_html)
        self.assertIn("GAIA (multimodal)", svg_html)
        self.assertIn("OSWorld (Desktop)", svg_html)
        self.assertNotIn("…", svg_html)

        # Formattierte Werte in deutscher Notation
        self.assertIn("35,8", svg_html)
        self.assertIn("48,9", svg_html)
        self.assertIn("67,2", svg_html)
        self.assertIn("12,5", svg_html)

        # Einheit
        self.assertIn("% Erfolgsrate", svg_html)

    # 14. gestapelt: gestapelte Balken mit Summe ueber dem Balken und Legende
    def test_14_gestapelt(self):
        chart_data = {
            "titel": "Energiebedarf nach Quellen",
            "einheit": "TWh",
            "typ": "gestapelt",
            "gruppen": ["2024", "2030"],
            "reihen": [
                {"name": "Solar und Wind", "werte": [120, 450]},
                {"name": "Kernkraft", "werte": [80, 110]},
                {"name": "Fossile", "werte": [215, 385]}
            ],
            "quelle": "Energieagentur",
            "quelle_url": "https://example.org/energy",
            "hinweis": "Prognose fuer 2030"
        }
        self.create_chart("energie-gestapelt", chart_data)
        self.create_post("gestapelt-post", body="Gestapelt:\n\n{{chart:energie-gestapelt}}\n")

        dist_dir = os.path.join(self.tmpdir, "dist")
        code, out, err = self.run_cli(["build", "--out", dist_dir])
        self.assertEqual(code, 0, f"build failed: {err}")

        post_path = os.path.join(dist_dir, "gestapelt-post.html")
        with open(post_path, "r", encoding="utf-8") as f:
            post_html = f.read()

        self.assertIn("<svg", post_html)
        self.assertIn('role="img"', post_html)
        self.assertIn("<title>Energiebedarf nach Quellen</title>", post_html)
        self.assertNotIn("{{", post_html)
        self.assertNotIn("<script", post_html)
        self.assertNotIn("<img", post_html)

        svg_match = re.search(r"<svg[\s\S]*?</svg>", post_html)
        self.assertIsNotNone(svg_match)
        svg_html = svg_match.group(0)

        # Gruppen
        self.assertIn("2024", svg_html)
        self.assertIn("2030", svg_html)

        # Legende mit allen Reihennamen
        self.assertIn("Solar und Wind", svg_html)
        self.assertIn("Kernkraft", svg_html)
        self.assertIn("Fossile", svg_html)

        # Segmentwerte formatiert
        self.assertIn("120", svg_html)
        self.assertIn("450", svg_html)
        self.assertIn("80", svg_html)
        self.assertIn("110", svg_html)
        self.assertIn("215", svg_html)
        self.assertIn("385", svg_html)

        # Summe ueber den Balken (2024: 120+80+215=415, 2030: 450+110+385=945)
        self.assertIn("415", svg_html)
        self.assertIn("945", svg_html)

    # 15. flaeche: Flaechendiagramm mit halbtransparenter Fuellung und Legende
    def test_15_flaeche(self):
        chart_data = {
            "titel": "Token-Verbrauch über Zeit",
            "einheit": "Mrd. Token",
            "typ": "flaeche",
            "x": ["Jan", "Feb", "Mär", "Apr"],
            "reihen": [
                {"name": "Eingabe", "werte": [12.5, 18.0, 24.3, 31.5]},
                {"name": "Ausgabe", "werte": [3.2, 5.1, 8.4, 11.2]}
            ],
            "quelle": "Nutzungsstatistik 2026",
            "quelle_url": "https://example.org/tokens"
        }
        self.create_chart("token-flaeche", chart_data)
        self.create_post("flaeche-post", body="Verlauf:\n\n{{chart:token-flaeche}}\n")

        dist_dir = os.path.join(self.tmpdir, "dist")
        code, out, err = self.run_cli(["build", "--out", dist_dir])
        self.assertEqual(code, 0, f"build failed: {err}")

        post_path = os.path.join(dist_dir, "flaeche-post.html")
        with open(post_path, "r", encoding="utf-8") as f:
            post_html = f.read()

        self.assertIn("<svg", post_html)
        self.assertIn('role="img"', post_html)
        self.assertIn("<title>Token-Verbrauch über Zeit</title>", post_html)
        self.assertNotIn("{{", post_html)
        self.assertNotIn("<script", post_html)
        self.assertNotIn("<img", post_html)

        svg_match = re.search(r"<svg[\s\S]*?</svg>", post_html)
        self.assertIsNotNone(svg_match)
        svg_html = svg_match.group(0)

        # X-Labels
        self.assertIn("Jan", svg_html)
        self.assertIn("Feb", svg_html)
        self.assertIn("Mär", svg_html)
        self.assertIn("Apr", svg_html)

        # Legende
        self.assertIn("Eingabe", svg_html)
        self.assertIn("Ausgabe", svg_html)

        # Werte formatiert
        self.assertIn("12,5", svg_html)
        self.assertIn("18", svg_html)
        self.assertIn("24,3", svg_html)
        self.assertIn("31,5", svg_html)
        self.assertIn("3,2", svg_html)
        self.assertIn("5,1", svg_html)
        self.assertIn("8,4", svg_html)
        self.assertIn("11,2", svg_html)

        # Halbtransparente Flaeche (Polygon oder Flaeche mit Opacity)
        self.assertTrue("<polygon" in svg_html or 'fill-opacity="' in svg_html or 'opacity="' in svg_html)

    # 16. punkte: Punktdiagramm ohne Verbindungslinie, nur Marker und Legende
    def test_16_punkte(self):
        chart_data = {
            "titel": "Latenz vs. Benchmark",
            "einheit": "ms",
            "typ": "punkte",
            "x": ["Task A", "Task B", "Task C"],
            "reihen": [
                {"name": "Modell Flash", "werte": [120, 180.5, 95]},
                {"name": "Modell Pro", "werte": [450, 620, 380]}
            ],
            "quelle": "Latenzmessung 2026",
            "quelle_url": "https://example.org/latency"
        }
        self.create_chart("punkte-latenz", chart_data)
        self.create_post("punkte-post", body="Messpunkte:\n\n{{chart:punkte-latenz}}\n")

        dist_dir = os.path.join(self.tmpdir, "dist")
        code, out, err = self.run_cli(["build", "--out", dist_dir])
        self.assertEqual(code, 0, f"build failed: {err}")

        post_path = os.path.join(dist_dir, "punkte-post.html")
        with open(post_path, "r", encoding="utf-8") as f:
            post_html = f.read()

        self.assertIn("<svg", post_html)
        self.assertIn('role="img"', post_html)
        self.assertIn("<title>Latenz vs. Benchmark</title>", post_html)
        self.assertNotIn("{{", post_html)
        self.assertNotIn("<script", post_html)
        self.assertNotIn("<img", post_html)

        svg_match = re.search(r"<svg[\s\S]*?</svg>", post_html)
        self.assertIsNotNone(svg_match)
        svg_html = svg_match.group(0)

        # X-Labels
        self.assertIn("Task A", svg_html)
        self.assertIn("Task B", svg_html)
        self.assertIn("Task C", svg_html)

        # Legende
        self.assertIn("Modell Flash", svg_html)
        self.assertIn("Modell Pro", svg_html)

        # Werte formatiert
        self.assertIn("120", svg_html)
        self.assertIn("180,5", svg_html)
        self.assertIn("95", svg_html)
        self.assertIn("450", svg_html)
        self.assertIn("620", svg_html)
        self.assertIn("380", svg_html)

        # Marker vorhanden, aber keine polyline/path fuer Verbindungslinien
        self.assertIn("<circle", svg_html)
        self.assertNotIn("<polyline", svg_html)

    # 17. anteil: Einzelwert mit wert/von und optionalem label
    def test_17_anteil_single(self):
        chart_data = {
            "titel": "Aktive Parameter pro Token",
            "einheit": "%",
            "typ": "anteil",
            "wert": 5.5,
            "von": 100,
            "label": "der Parameter pro Token",
            "quelle": "DeepSeek-V3 Report",
            "quelle_url": "https://arxiv.org/abs/2412.19437"
        }
        self.create_chart("anteil-single", chart_data)
        self.create_post("anteil-single-post", body="Anteil:\n\n{{chart:anteil-single}}\n")

        dist_dir = os.path.join(self.tmpdir, "dist")
        code, out, err = self.run_cli(["build", "--out", dist_dir])
        self.assertEqual(code, 0, f"build failed: {err}")

        post_path = os.path.join(dist_dir, "anteil-single-post.html")
        with open(post_path, "r", encoding="utf-8") as f:
            post_html = f.read()

        self.assertIn("<svg", post_html)
        self.assertIn('role="img"', post_html)
        self.assertIn("<title>Aktive Parameter pro Token</title>", post_html)
        self.assertNotIn("{{", post_html)
        self.assertNotIn("<script", post_html)
        self.assertNotIn("<img", post_html)

        svg_match = re.search(r"<svg[\s\S]*?</svg>", post_html)
        self.assertIsNotNone(svg_match)
        svg_html = svg_match.group(0)

        # Prozentwert korrekt formatiert
        self.assertIn("5,5 %", svg_html)
        # Label vorhanden
        self.assertIn("der Parameter pro Token", svg_html)

    # 18. anteil: Mehrere Anteile mit Legende, Segment-Prozentwerten und Normalisierung
    def test_18_anteil_multi(self):
        chart_data = {
            "titel": "Verbleib von Plastikmüll",
            "typ": "anteil",
            "anteile": [
                {"label": "Recycelt", "wert": 9},
                {"label": "Verbrennung", "wert": 40}
            ],
            "quelle": "OECD Global Plastics Outlook",
            "quelle_url": "https://example.org/plastics"
        }
        self.create_chart("anteil-multi", chart_data)
        self.create_post("anteil-multi-post", body="Verteilung:\n\n{{chart:anteil-multi}}\n")

        dist_dir = os.path.join(self.tmpdir, "dist")
        code, out, err = self.run_cli(["build", "--out", dist_dir])
        self.assertEqual(code, 0, f"build failed: {err}")

        post_path = os.path.join(dist_dir, "anteil-multi-post.html")
        with open(post_path, "r", encoding="utf-8") as f:
            post_html = f.read()

        self.assertIn("<svg", post_html)
        self.assertIn('role="img"', post_html)
        self.assertIn("<title>Verbleib von Plastikmüll</title>", post_html)
        self.assertNotIn("{{", post_html)
        self.assertNotIn("<script", post_html)
        self.assertNotIn("<img", post_html)

        svg_match = re.search(r"<svg[\s\S]*?</svg>", post_html)
        self.assertIsNotNone(svg_match)
        svg_html = svg_match.group(0)

        # Legende mit allen Reihen-/Anteilsnamen
        self.assertIn("Recycelt", svg_html)
        self.assertIn("Verbrennung", svg_html)

        # Summe != 100 (9 + 40 = 49) -> tatsaechliche Werte 9 und 40 sowie normierte Prozentwerte
        self.assertIn("9", svg_html)
        self.assertIn("40", svg_html)
        # 9/49 = 18.4% -> 18,4 %, 40/49 = 81.6% -> 81,6 %
        self.assertIn("18,4 %", svg_html)
        self.assertIn("81,6 %", svg_html)

    # 19. Unbekannter Typ in JSON-Datei -> check und build schlagen fehl mit klarer Meldung
    def test_19_unknown_type_validation(self):
        chart_data = {
            "titel": "Falscher Typ",
            "typ": "unbekannt-typ",
            "werte": [{"label": "A", "wert": 1}]
        }
        self.create_chart("invalid-type", chart_data)
        self.create_post("invalid-post", body="Ungueltig:\n\n{{chart:invalid-type}}\n")

        # 1. check muss fehlschlagen
        code, out, err = self.run_cli(["check"])
        self.assertNotEqual(code, 0, "check muss bei unbekanntem Chart-Typ fehlschlagen")
        self.assertIn("unbekannt-typ", out + err)

        # 2. build muss fehlschlagen
        dist_dir = os.path.join(self.tmpdir, "dist")
        code, out, err = self.run_cli(["build", "--out", dist_dir])
        self.assertNotEqual(code, 0, "build muss bei unbekanntem Chart-Typ fehlschlagen")
        self.assertIn("unbekannt-typ", out + err)

    # 20. Determinismus fuer gestapelt-Diagramme: zwei Builds liefern byte-identische Ausgaben
    def test_20_determinism_gestapelt(self):
        chart_data = {
            "titel": "Energiebedarf nach Quellen",
            "einheit": "TWh",
            "typ": "gestapelt",
            "gruppen": ["2024", "2030"],
            "reihen": [
                {"name": "Solar & Wind", "werte": [120, 450]},
                {"name": "Kernkraft", "werte": [80, 110]}
            ]
        }
        self.create_chart("determ-gestapelt", chart_data)
        self.create_post("determ-gestapelt-post", body="Text:\n\n{{chart:determ-gestapelt}}\n")

        dist1 = os.path.join(self.tmpdir, "dist1")
        dist2 = os.path.join(self.tmpdir, "dist2")

        code1, _, _ = self.run_cli(["build", "--out", dist1])
        code2, _, _ = self.run_cli(["build", "--out", dist2])
        self.assertEqual(code1, 0)
        self.assertEqual(code2, 0)

        with open(os.path.join(dist1, "determ-gestapelt-post.html"), "rb") as f:
            h1 = hashlib.sha256(f.read()).hexdigest()
        with open(os.path.join(dist2, "determ-gestapelt-post.html"), "rb") as f:
            h2 = hashlib.sha256(f.read()).hexdigest()

        self.assertEqual(h1, h2, "Zwei Builds von gestapelt-Diagrammen muessen byte-identisch sein")


if __name__ == "__main__":
    unittest.main()

