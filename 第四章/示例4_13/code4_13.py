# 【示例4.13】 第四章 第4.1节 code4_13.py
from typing import Optional, List
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):                   #定义数据模型类
    name: str                           #定义字段，类型str
    description: Optional[str] = None       #定义可选字段，类型str
    price: float                         #定义字段，类型float
    tax: Optional[float] = None           # 定义可选字段，类型float
    tags: List[str] = []                # 定义字段，列表泛型，默认为[]

@app.put("/items/{item_id}")  # 定义路径参数
async def update_item(item_id: int, item: Item):  # 路径参数和Body参数
    return {"item_id": item_id, "item": item}  #直接返回结果

if __name__ == '__main__':
    uvicorn.run(app=app)