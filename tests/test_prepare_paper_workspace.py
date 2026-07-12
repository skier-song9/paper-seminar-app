import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = (
    Path(__file__).resolve().parents[1]
    / ".codex/skills/paper-seminar/scripts/prepare_paper_workspace.py"
)
sys.path.insert(0, str(SCRIPT.parent))

import prepare_paper_workspace as ppw  # noqa: E402

FAKE_PDF = b"%PDF-1.4\n%fake minimal pdf for tests\n"


class TestArxivPdfUrl(unittest.TestCase):
    def test_bare_new_style_id(self):
        self.assertEqual(
            ppw.arxiv_pdf_url("2401.12345"), "https://arxiv.org/pdf/2401.12345"
        )

    def test_bare_new_style_id_with_version(self):
        self.assertEqual(
            ppw.arxiv_pdf_url("2401.12345v2"), "https://arxiv.org/pdf/2401.12345v2"
        )

    def test_bare_old_style_id(self):
        self.assertEqual(
            ppw.arxiv_pdf_url("cs/0301012"), "https://arxiv.org/pdf/cs/0301012"
        )

    def test_abs_url_new_style(self):
        self.assertEqual(
            ppw.arxiv_pdf_url("https://arxiv.org/abs/2401.12345"),
            "https://arxiv.org/pdf/2401.12345",
        )

    def test_abs_url_old_style_keeps_category(self):
        self.assertEqual(
            ppw.arxiv_pdf_url("https://arxiv.org/abs/cs/0301012"),
            "https://arxiv.org/pdf/cs/0301012",
        )

    def test_pdf_url_passthrough(self):
        url = "https://arxiv.org/pdf/2401.12345"
        self.assertEqual(ppw.arxiv_pdf_url(url), url)

    def test_non_arxiv_url_passthrough(self):
        url = "https://example.com/some/paper.pdf"
        self.assertEqual(ppw.arxiv_pdf_url(url), url)


class TestSlugify(unittest.TestCase):
    def test_basic_title(self):
        self.assertEqual(
            ppw.slugify("Attention Is All You Need"), "attention-is-all-you-need"
        )

    def test_unicode_and_symbols(self):
        self.assertEqual(ppw.slugify("Résumé: A+B & C!"), "resume-a-b-c")

    def test_truncates_to_ten_words(self):
        slug = ppw.slugify("one two three four five six seven eight nine ten eleven")
        self.assertEqual(slug, "one-two-three-four-five-six-seven-eight-nine-ten")

    def test_empty_falls_back_to_paper(self):
        self.assertEqual(ppw.slugify("한국어만 있는 제목"), "paper")


class TestCollisionHandling(unittest.TestCase):
    def run_script(self, *args):
        return subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            capture_output=True,
            text=True,
        )

    def test_refuses_overwrite_without_force(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "input.pdf"
            source.write_bytes(FAKE_PDF)
            output = str(Path(tmp) / "seminars")
            first = self.run_script(str(source), "--output", output, "--title", "My Paper")
            self.assertEqual(first.returncode, 0, first.stderr)
            second = self.run_script(str(source), "--output", output, "--title", "My Paper")
            self.assertNotEqual(second.returncode, 0)
            self.assertIn("--force", second.stderr)

    def test_force_overwrites(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "input.pdf"
            source.write_bytes(FAKE_PDF)
            output = str(Path(tmp) / "seminars")
            self.run_script(str(source), "--output", output, "--title", "My Paper")
            result = self.run_script(
                str(source), "--output", output, "--title", "My Paper", "--force"
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((Path(output) / "my-paper" / "paper.pdf").exists())

    def test_rejects_non_pdf(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "input.pdf"
            source.write_bytes(b"not a pdf")
            output = str(Path(tmp) / "seminars")
            result = self.run_script(str(source), "--output", output, "--title", "Bad")
            self.assertNotEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
