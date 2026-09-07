#!/usr/bin/env python3
"""Export docs/slides/index.html to PDF (one page per slide) with Playwright/Chromium, then render README preview PNGs from it."""
import asyncio, pathlib, sys
from playwright.async_api import async_playwright
ROOT = pathlib.Path(__file__).resolve().parents[1]
HTML = ROOT / "docs" / "slides" / "index.html"
PDF = ROOT / "docs" / "slides" / "index.pdf"
PREVIEW = ROOT / "docs" / "assets" / "slides_preview"

async def main():
    PREVIEW.mkdir(parents=True, exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch()
        page = await b.new_page(viewport={"width": 1280, "height": 720})
        await page.goto(HTML.as_uri())
        await page.wait_for_timeout(500)
        await page.emulate_media(media="print")
        await page.pdf(path=str(PDF), width="1280px", height="720px", print_background=True, margin={"top": "0", "bottom": "0", "left": "0", "right": "0"}, prefer_css_page_size=True)
        n = await page.evaluate("document.querySelectorAll('section.slide').length")
        await b.close()
    import fitz  # PyMuPDF: README preview images rendered from the exported PDF
    doc = fitz.open(str(PDF))
    for i in (1, 13):
        if i <= doc.page_count:
            doc.load_page(i - 1).get_pixmap(matrix=fitz.Matrix(0.8, 0.8)).save(str(PREVIEW / f"pdf_{i:02d}.png"))
    print("pdf:", PDF, "slides:", n)

if __name__ == "__main__":
    asyncio.run(main())
