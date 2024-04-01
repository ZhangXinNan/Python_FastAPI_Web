# 【示例8.1】 第八章 第8.3节 code8_1.py
import asyncio
from datetime import datetime
async def main():
    print(f'start: {datetime.now().strftime("%X")}')
    print('hello')
    await asyncio.sleep(1)
    print(f'end: {datetime.now().strftime("%X")}')
    print(f'three cool cat')
asyncio.run(main())
