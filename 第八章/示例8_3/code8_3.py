# 【示例8.3】 第八章 第8.3节 code8_3.py
import asyncio
from datetime import datetime
async def my_print(timeout, txt):
    await asyncio.sleep(timeout)
    print(txt)

async def main():
    task1 = asyncio.create_task(my_print(1, 'hello'))
    task2 = asyncio.create_task(my_print(2, 'three cool cat'))
    print(f"task start {datetime.now().strftime('%X')}")
    await task1
    await task2
    print(f"end {datetime.now().strftime('%X')}")

asyncio.run(main())