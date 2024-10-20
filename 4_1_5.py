import aiohttp
import asyncio

class WebScraper:
    def __init__(self, urls):
        self.urls = urls

    async def fetch(self, session, url):
        async with session.get(url) as response:
            return await response.text()

    async def scrape(self):
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch(session, url) for url in self.urls]
            results = await asyncio.gather(*tasks)
            return results

async def main():
    with open('urls.txt') as f:
        urls = [line.strip() for line in f.readlines()]
    
    scraper = WebScraper(urls)
    results = await scraper.scrape()
    for idx, result in enumerate(results):
        print(f"Результат для URL {urls[idx]}:\n{result[:200]}...")  # выводим первые 200 символов

if __name__ == "__main__":
    asyncio.run(main())
