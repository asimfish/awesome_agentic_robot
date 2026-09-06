#!/usr/bin/env python3
"""Export docs/slides/index.html to PDF (one page per slide) and PNG previews using Playwright/Chromium."""
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
        await page.emulate_media(media="screen")
        n = await page.evaluate("document.querySelectorAll('section.slide').length")
        for i in [1, 2, 4, 6, 13, 18]:
            if i <= n:
                await page.goto(HTML.as_uri() + f"#{i}"); await page.wait_for_timeout(200)
                await page.screenshot(path=str(PREVIEW / f"slide_{i:02d}.png"))
        await b.close()
    print("pdf:", PDF, "slides:", n)

if __name__ == "__main__":
    asyncio.run(main())
