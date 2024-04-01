# SeaGoods_asyncio.py
import asyncio

from pydantic import BaseModel  # 导入基础模型类


class Goods(BaseModel):  # 定义数据模型类，继承自BaseModel类
    name: str = '对虾'  # 定义字段name，类型 str
    num: float = 10  # 定义字段num，类型float
    unit: str = '斤'  # 定义字段unit，类型 str
    price: float = 48  # 定义字段price，类型float


async def stat(good: Goods):  # 定义协程函数,统计金额
    print(good.num * good.price, '元')
    return good.num * good.price


async def Count_users():  # 定义协程函数,写入提交次数

    with open(r'E:\c1.txt', 'r+') as f:
        num = f.read()
        if num == '':
            num = 0
        f.write(str(int(num) + 1))
    print(str(int(num) + 1) + '次')


async def main():
    good = Goods()
    task1 = asyncio.create_task(stat(good))
    task2 = asyncio.create_task(Count_users())
    await task1
    await task2


asyncio.run(main())
