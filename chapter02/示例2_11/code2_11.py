# 【示例2.11】 第二章 第2.4.2节 code2_11.py
from typing import Optional
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):                    # 定义数据模型类，继承自BaseModel类
    name: str                             # 定义字段name 类型str
    description: Optional[str] = None     # 定义可选字段description 类型str
    price: float                          # 定义字段price 类型float
    tax: Optional[float] = None           # 定义可选字段tax 类型float
app = FastAPI()
@app.post("/items/{item_id}")               # 注册路由，定义路径参数item_id
async def create_item(                      # 定义路径操作函数
item_id: int,                               # 定义路径参数，类型int
item: Item,                                 # 定义请求体，类型是数据模型
q: Optional[str] = None                     # 定义可选查询参数，类型str
):
    result = {"item_id": item_id, **item.dict()}  # 将路径参数和请求体参数组合为数据对象
    if q:
        result.update({"q": q})                   # 如果传入了查询参数，则更新查询参数
    return result                                 # 返回组合好的数据对象
if __name__ == '__main__':
    uvicorn.run(app=app)