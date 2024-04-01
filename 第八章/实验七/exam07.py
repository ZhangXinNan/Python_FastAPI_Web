import asyncio
from datetime import datetime
import aiohttp

async def get(session, url, dt):
    try:
        async with session.get(url) as r:
            dt1 = datetime.now()
            print(f'{datetime.now().strftime("%X")}完成爬取 {url},状态为：{r.status}，用时为{dt1 - dt}')
            return await r.text()
    except:
        print(f'{datetime.now().strftime("%X")}爬取出错{url}')

async def touch(url):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        dt = datetime.now()
        print(f'{dt.strftime("%X")}开始爬取：{url}')
        html = await get(session, url, dt)

urls = [
    'https://www.python.org',
    'https://baidu.com',
    'https://fastapi.tiangolo.com/',
    'https://www.starlette.io/',
    'https://pydantic-docs.helpmanual.io/',
]

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [asyncio.ensure_future(touch(url)) for url in urls]
    tasks = asyncio.gather(*tasks)
    loop.run_until_complete(tasks)