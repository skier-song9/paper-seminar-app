#!/usr/bin/env python3
import argparse
import re
import shutil
import sys
import unicodedata
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen


def arxiv_pdf_url(value: str) -> str:
    value = value.strip()
    if re.fullmatch(r"\d{4}\.\d{4,5}(v\d+)?", value):
        return f"https://arxiv.org/pdf/{value}"
    parsed = urlparse(value)
    if "arxiv.org" not in parsed.netloc:
        return value
    paper_id = parsed.path.rstrip("/").split("/")[-1]
    if "/pdf/" in parsed.path:
        return value
    return f"https://arxiv.org/pdf/{paper_id}"


def slugify(title: str) -> str:
    ascii_title = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode()
    words = re.findall(r"[A-Za-z0-9]+", ascii_title.lower())
    return "-".join(words[:10]) or "paper"


def guess_title_from_pdf(path: Path) -> str:
    try:
        from pypdf import PdfReader

        reader = PdfReader(str(path))
        meta_title = (reader.metadata or {}).get("/Title")
        if meta_title and len(meta_title.strip()) > 5:
            return meta_title.strip()
        text = reader.pages[0].extract_text() or ""
        lines = [re.sub(r"\s+", " ", line).strip() for line in text.splitlines()]
        lines = [line for line in lines if 8 <= len(line) <= 180]
        return lines[0] if lines else path.stem
    except Exception:
        return path.stem


def download(url: str, dest: Path) -> None:
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(req, timeout=60) as resp, dest.open("wb") as f:
        shutil.copyfileobj(resp, f)


def require_pdf(path: Path) -> None:
    if path.read_bytes()[:4] != b"%PDF":
        raise SystemExit(f"not a PDF: {path}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Local PDF path, arXiv id, arXiv URL, or PDF URL")
    parser.add_argument("--output", default=".", help="Directory where the paper folder is created")
    parser.add_argument("--title", help="Short or full paper title for folder naming")
    args = parser.parse_args()

    output = Path(args.output).expanduser().resolve()
    output.mkdir(parents=True, exist_ok=True)

    source = args.input.strip()
    tmp_pdf = output / ".paper-download.tmp.pdf"
    if Path(source).expanduser().exists():
        source_pdf = Path(source).expanduser().resolve()
    else:
        pdf_url = arxiv_pdf_url(source)
        download(pdf_url, tmp_pdf)
        source_pdf = tmp_pdf

    require_pdf(source_pdf)
    title = args.title or guess_title_from_pdf(source_pdf)
    folder = output / slugify(title)
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "figures").mkdir(exist_ok=True)
    shutil.copyfile(source_pdf, folder / "paper.pdf")
    if tmp_pdf.exists():
        tmp_pdf.unlink()

    print(folder)
    return 0


if __name__ == "__main__":
    sys.exit(main())
