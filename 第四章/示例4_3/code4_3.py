# 【示例4.3】 第四章 第4.1节 code4_3.py
from typing import Optional
from fastapi import FastAPI, Query  # 导入Query类
import uvicorn
app = FastAPI()

@app.get("/")
async def read_items(q: Optional[str] = Query(None, regex='^[\w\d]{3,10}$')):  #使用Query定义规则
    return {"q": q}

if __name__ == '__main__':
    uvicorn.run(app=app)