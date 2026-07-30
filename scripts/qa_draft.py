#!/usr/bin/env python3
"""QA checks for page drafts (skills/seo-content-drafting).

The check that matters: every quoted passage must string-match text actually retrieved and saved
to the client's sources/ directory. An unmatched quote means a fabricated or altered attribution,
which is the most damaging thing this pipeline can produce.

    python scripts/qa_draft.py draft.md --sources .seo-ops/clients/<slug>/sources/
    python scripts/qa_draft.py --demo
"""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import unicodedata
from pathlib import Path

PLACEHOLDER_RE = re.compile(r"\[NEEDS:[^\]]*\]|`\[[A-Z_ /]+\]`")
NUM_RE = re.compile(r"(?<![\w-])\d+(?:[.,]\d+)*\s?(?:%|[a-zA-Z]{1,6})?(?![\w-])")


def normalise(text: str) -> str:
    """Collapse the differences that survive a copy-paste but are not content."""
    text = unicodedata.normalize("NFKC", text)
    for a, b in [("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'),
                 ("–", "-"), ("—", "-"), ("…", "..."), (" ", " ")]:
        text = text.replace(a, b)
    return re.sub(r"\s+", " ", text).strip().lower()


def read_source(path: Path) -> tuple[str, str | None]:
    """Return (text, error). PDFs go through pdftotext — most standards and journal sources are PDFs,
    and reading one as raw bytes guarantees every quote in it fails to match."""
    if path.suffix.lower() == ".pdf":
        if not shutil.which("pdftotext"):
            return "", (f"{path.name}: pdftotext not installed, PDF source unreadable "
                        "(brew install poppler)")
        try:
            out = subprocess.run(["pdftotext", "-q", str(path), "-"],
                                 capture_output=True, text=True, timeout=60)
        except (subprocess.SubprocessError, OSError) as exc:
            return "", f"{path.name}: pdftotext failed ({exc})"
        if out.returncode != 0:
            return "", f"{path.name}: pdftotext exited {out.returncode}"
        return out.stdout, None
    try:
        return path.read_text(encoding="utf-8", errors="ignore"), None
    except OSError as exc:
        return "", f"{path.name}: unreadable ({exc})"


def extract_quotes(text: str) -> list[str]:
    """Blockquote runs, excluding '> —' attribution lines."""
    quotes, current = [], []
    for line in text.split("\n"):
        stripped = line.strip()
        if stripped.startswith(">"):
            body = stripped[1:].strip()  # prefix strip, not character-set strip
            if body.startswith("—") or body.startswith("--"):
                continue  # attribution, not quoted material
            if body:
                current.append(body)
                continue
        if current:
            quotes.append(" ".join(current))
            current = []
    if current:
        quotes.append(" ".join(current))
    return quotes


def qa_draft(path: Path, sources_dir: Path | None, min_quote_words: int = 8) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []

    if ">> GEN" in text:
        errors.append("Draft still contains generation instructions (>> GEN:)")

    leftover = PLACEHOLDER_RE.findall(text)
    if leftover:
        errors.append("Unresolved placeholders: " + ", ".join(leftover[:10]))

    words = len(re.findall(r"\b[\w'-]+\b", text))
    figures = len(NUM_RE.findall(text))
    if words and figures * 100 / words < 1.0:
        errors.append(f"Thin on evidence: {figures} figures in {words} words (want >=1 per 100). "
                      "Usually means the research step was skipped.")

    quotes = [q for q in extract_quotes(text) if len(q.split()) >= min_quote_words]
    if quotes:
        if sources_dir is None or not sources_dir.is_dir():
            errors.append(f"{len(quotes)} quoted passage(s) present but no readable --sources "
                          "directory given; quotes cannot be verified")
        else:
            chunks = []
            for p in sorted(sources_dir.rglob("*")):
                if not p.is_file():
                    continue
                body, err = read_source(p)
                if err:
                    errors.append(f"SOURCE UNREADABLE — {err}")
                chunks.append(normalise(body))
            corpus = "\n".join(chunks)
            for q in quotes:
                # Drafts wrap quotes in quotation marks; the source text does not carry them.
                needle = normalise(q).strip('"\'' + " ")
                if needle not in corpus:
                    errors.append(f'UNVERIFIED QUOTE — no source match: "{q[:90]}..."')
    return errors


def demo() -> None:
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        src = tmp / "sources"
        src.mkdir()
        (src / "a.txt").write_text(
            "Design intent does not close the credit; the assessment requires measured levels "
            "across ninety per cent of net lettable area.", encoding="utf-8")
        good = tmp / "good.md"
        # Quotation marks and curly punctuation must not defeat the match — the real-world shape.
        good.write_text(
            "Cost runs about RM180 per sqm across 2,000 sqm on a 12 month payback.\n\n"
            "> “Design intent does not close the credit; the assessment requires measured levels\n"
            "> across ninety per cent of net lettable area.”\n"
            "> — A Real Person, Trade Journal\n", encoding="utf-8")
        bad = tmp / "bad.md"
        bad.write_text(
            "Cost runs about RM180 per sqm across 2,000 sqm on a 12 month payback.\n\n"
            "> Acoustic zoning is widely regarded as the single most important factor.\n"
            "> — A Real Person, Trade Journal\n", encoding="utf-8")

        assert qa_draft(good, src) == [], qa_draft(good, src)
        bad_errors = qa_draft(bad, src)
        assert any("UNVERIFIED QUOTE" in e for e in bad_errors), bad_errors
        assert any("no readable --sources" in e for e in qa_draft(good, None))
        print("OK: verified quote passes, fabricated quote caught, missing sources dir caught")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("draft", nargs="?", type=Path)
    ap.add_argument("--sources", type=Path, default=None,
                    help="directory of retrieved source text for quote verification")
    ap.add_argument("--demo", action="store_true")
    args = ap.parse_args()

    if args.demo:
        demo()
        return 0
    if args.draft is None:
        ap.error("a draft path is required (or use --demo). "
                 "Refusing to exit 0 without checking anything.")

    errors = qa_draft(args.draft, args.sources)
    for e in errors:
        print(f"FAIL  {e}")
    if not errors:
        print(f"PASS  {args.draft}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
