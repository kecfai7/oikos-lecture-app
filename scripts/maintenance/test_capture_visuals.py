import asyncio
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

from playwright.async_api import async_playwright

async def verify():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': 1920, 'height': 1080})
        for s_num in range(1, 6):
            url = f"https://oikos-lecture-app.vercel.app/?session=1&slide={s_num}"
            await page.goto(url, wait_until="networkidle")
            await asyncio.sleep(0.5)
            await page.evaluate("""() => {
                const header = document.querySelector('header');
                if (header) header.style.display = 'none';
            }""")
            img_path = rf"c:\Oikos Univ\duo_videos\slide_images\session_1_slide_{s_num:02d}.png"
            await page.screenshot(path=img_path)
            print(f"Captured Slide {s_num}: {img_path} ({os.path.getsize(img_path)} bytes)")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify())
