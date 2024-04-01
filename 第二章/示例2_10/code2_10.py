# 【示例2.10】 第二章 第2.4.1节 code2_10.py
from typing import Optional
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel         #导入基础模型类

class Item(BaseModel):                 # 定义数据模型类，继承自BaseModel类
    name: str                          #定义字段name，类型 str
    description: Optional[str] = None  #定义可选字段description，类型str
    price: float                       #定义字段price，类型float
    tax: Optional[float] = None        #定义可选字段tax，类型float

app = FastAPI()

@app.post("/items/")                  #注册路由路径，请求方式为post，不是get
async def create_item(item: Item):    #定义请求体，类型是数据模型类Item
    return item                       #直接返回请求体数据

if __name__ == '__main__':
    uvicorn.run(app=app)