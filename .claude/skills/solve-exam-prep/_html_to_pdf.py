"""Convert an explain-lab-preview HTML file to a clean A4 PDF.

Uses Playwright + Chromium (not Edge --print-to-pdf, which always stamps a
file:// path / page-number footer that cannot be suppressed). Waits for MathJax
to finish typesetting before printing so formulas never render as raw `$...$`.

Usage:
    python _html_to_pdf.py "<input.html>" "<output.pdf>"
"""
from __future__ import annotations

import sys
from pathlib import Path


def html_to_pdf(html_path: Path, pdf_path: Path) -> None:
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(html_path.resolve().as_uri(), wait_until="networkidle")
        # Block B2 fix: wait for MathJax to finish typesetting. The template sets
        # window.__mathjaxDone = true inside MathJax.startup.promise.then(...).
        # If the page has no math at all, MathJax may still set the flag; if MathJax
        # failed to load (offline + no local bundle), fall back after a short timeout
        # so we still emit a PDF (formulas will show as raw text).
        try:
            page.wait_for_function("window.__mathjaxDone === true", timeout=15000)
        except Exception:
            print("WARN: MathJax typeset wait timed out — math may render as raw text.",
                  file=sys.stderr)
        # Ensure the bundled Pretendard @font-face has finished loading before
        # printing, otherwise the intended 300/500/600 weights can fall back to
        # Malgun Gothic (400/700 only) and emphasis renders abruptly heavy.
        try:
            page.evaluate("document.fonts.ready")
        except Exception:
            print("WARN: document.fonts.ready wait failed — body font may fall back.",
                  file=sys.stderr)
        page.pdf(
            path=str(pdf_path),
            format="A4",
            print_background=True,
            display_header_footer=False,   # Block B1 fix: no stamped header/footer
            prefer_css_page_size=True,     # honor the template's @page rule
        )
        browser.close()


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print("usage: python _html_to_pdf.py <input.html> <output.pdf>", file=sys.stderr)
        return 2
    html_path = Path(argv[1])
    pdf_path = Path(argv[2])
    if not html_path.exists():
        print(f"ERROR: HTML not found: {html_path}", file=sys.stderr)
        return 1
    try:
        html_to_pdf(html_path, pdf_path)
    except ImportError:
        print("ERROR: playwright 미설치. `pip install playwright` 후 "
              "`python -m playwright install chromium` 실행 필요. HTML은 유지됨.",
              file=sys.stderr)
        return 1
    print(f"OK: {pdf_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
