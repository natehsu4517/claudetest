import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1200, "height": 900})
        await page.goto("https://matrixmasterygroup.com", wait_until="networkidle", timeout=30000)

        # Take full page screenshot
        await page.screenshot(path="c:/Users/hsuna/Caude_v1Site/mmg_screenshot.png", full_page=True)

        # Extract all visible text
        text = await page.evaluate("""() => {
            return document.body.innerText;
        }""")

        with open("c:/Users/hsuna/Caude_v1Site/mmg_text.txt", "w", encoding="utf-8") as f:
            f.write(text)

        # Extract all image sources
        images = await page.evaluate("""() => {
            return Array.from(document.querySelectorAll('img')).map(img => ({
                src: img.src,
                alt: img.alt,
                width: img.naturalWidth,
                height: img.naturalHeight
            }));
        }""")

        with open("c:/Users/hsuna/Caude_v1Site/mmg_images.txt", "w", encoding="utf-8") as f:
            for img in images:
                f.write(f"src: {img['src']}\nalt: {img['alt']}\nsize: {img['width']}x{img['height']}\n---\n")

        # Extract all links
        links = await page.evaluate("""() => {
            return Array.from(document.querySelectorAll('a')).map(a => ({
                text: a.innerText.trim(),
                href: a.href
            })).filter(l => l.text);
        }""")

        with open("c:/Users/hsuna/Caude_v1Site/mmg_links.txt", "w", encoding="utf-8") as f:
            for link in links:
                f.write(f"{link['text']} -> {link['href']}\n")

        await browser.close()
        print("Done")

asyncio.run(main())
