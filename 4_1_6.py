import aiohttp
import asyncio

class AsyncWebScraper:
    def __init__(self, urls):
        self.urls = urls

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def fetch(self, url):
        async with self.session.get(url) as response:
            return await response.text()

    async def scrape(self):
        tasks = [self.fetch(url) for url in self.urls]
        results = await asyncio.gather(*tasks)
        return results

    async def __aexit__(self, exc_type, exc, tb):
        await self.session.close()

async def main():
    with open('urls.txt') as f:
        urls = [line.strip() for line in f.readlines()]

    async with AsyncWebScraper(urls) as scraper:
        results = await scraper.scrape()
        for idx, result in enumerate(results):
            print(f"Результат для URL {urls[idx]}:\n{result[:200]}...")

if __name__ == "__main__":
    asyncio.run(main())
