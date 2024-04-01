# 【示例3.6】 第三章 第3.2节 code3_6.py
from typing import Union
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class BaseItem(BaseModel):      # 定义数据模型基类，包含公用的字段
    description: str
    type: str

class Cat(BaseItem):         # 定义数据模型
    type = "cat"                # 定义字段type，默认值为cat

class Dog(BaseItem):       # 定义数据模型
    type = "dog"              # 定义字段type，默认值为dog
    color: str                 # 定义字段color

items = {                      # 模拟数据，分别对应两个数据模型
    "item1": {
        "description": "三酷猫",
        "type": "cat"
    },
    "item2": {
        "description": "中华田园犬",
        "type": "dog",
        "color": "yellow",
    },
}

@app.get("/items/{item_id}",
         response_model=Union[Dog, Cat]  # 使用Union返回多个数据模型
         )
async def read_item(item_id: str):
    return items[item_id]

if __name__ == '__main__':
    uvicorn.run(app=app)