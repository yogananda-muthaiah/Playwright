import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://sap.com")
        print(await page.title())
        await page.screenshot(path="example.png")
        await context.close()
        await browser.close()

asyncio.run(run())
