import aiohttp
import asyncpg
import asyncio
import json

WEB_SERVER_URL = "https://rnacentral.org/api/v1/rna/"
DB_CONNECTION_STRING = "postgres://reader:NWDMCE5xdipIjRrp@hh-pgsql-public.ebi.ac.uk:5432/pfmegrnargs"

async def fetch_from_web():
    async with aiohttp.ClientSession() as session:
        async with session.get(WEB_SERVER_URL) as response:
            data = await response.json()
            return json.dumps(data, indent=4)

async def fetch_from_db():
    conn = await asyncpg.connect(DB_CONNECTION_STRING)
    result = await conn.fetch("SELECT * FROM rnc_complete LIMIT 1;")
    await conn.close()
    return result

async def main():
    web_data, db_data = await asyncio.gather(fetch_from_web(), fetch_from_db())
    print(f"Данные с веб-сервера:\n{web_data}")
    print(f"Данные из базы данных:\n{db_data}")

if __name__ == "__main__":
    asyncio.run(main())
