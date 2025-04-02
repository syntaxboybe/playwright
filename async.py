import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto('https://www.itechmedialogic.com/')
        await page.screenshot(path="itml.png")
        await browser.close()

asyncio.run(main())
