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
    parser.add_argument("--output", default="seminars", help="Directory where paper folders are created")
    parser.add_argument("--title", help="Short or full paper title for folder naming")
    args = parser.parse_args()

    output = Path(args.output).expanduser().resolve()
    if output.name != "seminars":
        raise SystemExit("--output must point to a seminars directory")
    output.mkdir(parents=True, exist_ok=True)

    source = args.input.strip()
    source_path = Path(source).expanduser()
    fallback_title = args.title or source_path.stem or source.rstrip("/").split("/")[-1] or "paper"
    folder = output / slugify(fallback_title)
    folder.mkdir(parents=True, exist_ok=True)
    partial_pdf = folder / ".paper-download.partial.pdf"
    paper_pdf = folder / "paper.pdf"

    if Path(source).expanduser().exists():
        shutil.copyfile(source_path.resolve(), paper_pdf)
    else:
        pdf_url = arxiv_pdf_url(source)
        try:
            download(pdf_url, partial_pdf)
            partial_pdf.replace(paper_pdf)
        finally:
            if partial_pdf.exists():
                partial_pdf.unlink()

    require_pdf(paper_pdf)
    if not args.title:
        guessed_folder = output / slugify(guess_title_from_pdf(paper_pdf))
        if guessed_folder != folder and not guessed_folder.exists():
            folder.rename(guessed_folder)
            folder = guessed_folder
            paper_pdf = folder / "paper.pdf"

    (folder / "figures").mkdir(exist_ok=True)

    print(folder)
    return 0


if __name__ == "__main__":
    sys.exit(main())
