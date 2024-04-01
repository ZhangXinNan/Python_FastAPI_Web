# 【示例4.12】 第四章 第4.1节 code4_12.py
from typing import Optional
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):                   #定义数据模型类
    name: str                           #定义字段，类型str
    description: Optional[str] = None       #定义可选字段，类型str
    price: float                         #定义字段，类型float
    tax: Optional[float] = None           # 定义可选字段，类型float

    class Config:  # 定义配置类，必须命名为Config
        schema_extra = {  # 元数据
            "example": {  # 定义元数据中的示例数据
                "name": "三酷猫",
                "description": "这是一个非常不错的项目",
                "price": 35.4,
                "tax": 3.2,
            }
        }


@app.put("/items/{item_id}")  # 定义路径参数
async def update_item(item_id: int, item: Item):  # 路径参数和Body参数
    return {"item_id": item_id, "item": item}  #直接返回结果
if __name__ == '__main__':
    uvicorn.run(app=app)