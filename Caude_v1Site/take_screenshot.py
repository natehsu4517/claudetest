import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 500, "height": 900})
        await page.goto("file:///c:/Users/hsuna/Caude_v1Site/index.html", wait_until="networkidle")
        await page.screenshot(path="c:/Users/hsuna/Caude_v1Site/screenshot.png", full_page=True)
        await browser.close()
        print("Done")

asyncio.run(main())
