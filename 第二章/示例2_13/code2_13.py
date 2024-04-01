# 【示例2.13】 第二章 第2.4.4节 code2_13.py
from typing import Optional
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):                # 定义数据模型Item，继承自BaseModel
    name: str                         # 字义字段name， 类型 str
    description: Optional[str] = None # 定义可选字段description， 类型str
    price: float                      # 定义字段price， 类型float
    tax: Optional[float] = None       # 定义可选字段tax 类型float

class User(BaseModel):                # 定义数据模型User，继承自BaseModel
    username: str                     # 定义字段username，类型str
    full_name: Optional[str] = None   # 定义可选字段full_name，类型str

@app.put("/items/{item_id}")          # 注册路由路径，使用PUT方法，定义路径参数item_id
async def update_item(                # 定义路径操作函数
        item_id: int,                 # 定义路径参数
        item: Item,                   # 定义第一个请求体
        user: User                    # 定义第二个请求体
):
    results = {"item_id": item_id, "item": item, "user": user}
    return results

if __name__ == '__main__':
    uvicorn.run(app=app)