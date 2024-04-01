# 【示例3.10】 第三章 第3.3节 code3_10.py
from datetime import datetime
from typing import Optional
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn

class Item(BaseModel):  # 定义数据模型
    title: str
    timestamp: datetime
    description: Optional[str] = None

app = FastAPI()

@app.post("/item/")  # 注册路由路径
def update_item(item: Item):
    json_compatible_item_data = jsonable_encoder(item)  # 使用jsonable_encoder转换数据模型
    return JSONResponse(content=json_compatible_item_data)  # 直接返回JSONResponse对象

if __name__ == '__main__':
    uvicorn.run(app=app)