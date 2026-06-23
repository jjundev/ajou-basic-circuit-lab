"""Convert measurement checklist HTML to PDF via Playwright."""
from pathlib import Path

HERE = Path(__file__).parent
WEEK = HERE.parent.name
HTML = HERE / f"{WEEK} 측정체크리스트.html"
PDF = HERE / f"{WEEK} 측정체크리스트.pdf"


def main():
    from playwright.sync_api import sync_playwright

    if not HTML.exists():
        raise SystemExit(f"HTML not found: {HTML}")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(HTML.resolve().as_uri(), wait_until="load")
        page.pdf(
            path=str(PDF),
            format="A4",
            print_background=True,
            display_header_footer=False,
            prefer_css_page_size=True,
        )
        browser.close()
    print(f"PDF written: {PDF}")


if __name__ == "__main__":
    main()
