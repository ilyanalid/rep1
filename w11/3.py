import aiohttp
import asyncio
import aiofile
import re


async def func(session, service):
    async with session.get(service) as response:
        html = response.text()
        html = re.split(r'[\r\n]', html)
        for i in html:
            if i.startswith('<a >'):
                async with aiofile.async_open('found.txt', 'w') as f:
                    f.write(i)


async def main(name):
    async with aiofile.async_open(name, 'r') as f:
        async for line in aiofile.LineReader(f):
            async with aiohttp.ClientSession() as session:
                asyncio.ensure_future(func(session, line))
        print('Finished')


loop = asyncio.get_event_loop()
loop.run_until_complete(main('urls.txt'))
