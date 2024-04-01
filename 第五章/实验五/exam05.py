# 第五章 实验代码 exam05.py
import uvicorn
from fastapi import Depends, FastAPI
from pydantic import BaseModel  # 导入基础模型类

class Goods(BaseModel):  # 定义数据模型类，继承自BaseModel类
    name: str  # 定义字段name，类型 str
    num: float  # 定义字段num，类型float
    unit: str  # 定义字段unit，类型 str
    price: float  # 定义字段price，类型float

app = FastAPI()

# async def StatMoney(good: Goods):  # 定义统计金额的依赖函数
#     return good.num * good.price

class StatMoney:                     # 定义统计金额的依赖类
    def __init__(self, good: Goods):
        self.amount = good.num * good.price

async def logger():
    with open('log_stat.txt', 'a') as f:
        yield f
        f.close()

@app.put("/goods/")  # 注册路由路径
async def findGoods(stat:StatMoney = Depends(), log = Depends(logger)):  # 定义路径操作函数
    result = str(stat.amount) + '元'
    log.write(result)
    return result

if __name__ == '__main__':
    uvicorn.run(app=app)
