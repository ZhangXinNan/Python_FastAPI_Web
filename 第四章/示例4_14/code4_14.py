# 【示例4.14】 第四章 第4.1节 code4_14.py
from typing import List
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Image(BaseModel):  # 定义数据模型
    url: str
    name: str

@app.post("/images/")
async def create_multiple_images(images: List[Image]):  # 定义请求体，列表泛型
    return images

if __name__ == '__main__':
    uvicorn.run(app=app)