# 【示例4.15】 第四章 第4.1节 code4_15.py
from typing import Dict
import uvicorn
from fastapi import FastAPI
app = FastAPI()

@app.post("/scores/")
async def create_scores(scores: Dict[int, float]):  # 使用字典泛型接收键值对数据
    return scores
if __name__ == '__main__':
    uvicorn.run(app=app)