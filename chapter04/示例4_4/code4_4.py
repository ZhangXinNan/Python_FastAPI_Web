# 【示例4.4】 第四章 第4.1节 code4_4.py
from typing import List, Optional
import uvicorn
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/")
async def read_items(q: Optional[List[str]] = Query(None)):  # 定义列表类型的查询参数
    return {"q": q}

if __name__ == '__main__':
    uvicorn.run(app=app)