import asyncio
import time
from aiohttp import ClientSession


async def print_requested(url: str, session: ClientSession) -> None:
    async with session.get(url) as resp:
        print(await resp.text(), end='')


async def bulk_request(n) -> None:
    async with ClientSession() as session:
        tasks = [print_requested('http://127.0.0.1:8000', session)
                 for _ in range(n)]
        await asyncio.gather(*tasks)


start = time.time()
asyncio.run(bulk_request(100))
print(f'\n\n runtime: {time.time() - start:.3f} seconds')
