# 【示例8.2】 第八章 第8.3节 code8_2.py
import asyncio
from datetime import datetime

async def my_print(timeout, txt):
    await asyncio.sleep(timeout)
    print(txt)

async def main():
    print(f"start: {datetime.now().strftime('%X')}")
    await my_print(1, 'hello')
    print(f"end hello：{datetime.now().strftime('%X')}")
    await my_print(2, 'three cool cat')
    print(f"end name：{datetime.now().strftime('%X')}")
asyncio.run(main())