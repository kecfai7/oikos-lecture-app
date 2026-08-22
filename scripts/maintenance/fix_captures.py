import asyncio
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

from playwright.async_api import async_playwright

async def fix_slides():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={'width': 1920, 'height': 1080})
        page = await context.new_page()
        for s_num in [6, 13, 19]:
            url = f'https://oikos-lecture-app.vercel.app/?session=1&slide={s_num}'
            await page.goto(url, wait_until='networkidle')
            await asyncio.sleep(1.2)
            await page.evaluate("""() => {
                const header = document.querySelector('header');
                if (header) header.style.display = 'none';
                return true;
            }""")
            img_path = rf'c:\Oikos Univ\duo_videos\slide_images\session_1_slide_{s_num:02d}.png'
            await page.screenshot(path=img_path, full_page=False)
            print(f"Recaptured Slide {s_num}: size {os.path.getsize(img_path)}")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(fix_slides())
