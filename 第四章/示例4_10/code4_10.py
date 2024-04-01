# 【示例4.10】 第四章 第4.1节 code4_10.py
from typing import Optional
import uvicorn
from fastapi import FastAPI, Header

app = FastAPI()

@app.get("/items/")
async def read_items(user_agent: Optional[str] = Header(None)):  # 定义Header参数，类型str，默认值为空
    return {"User-Agent": user_agent}                            # 返回User-Agent的值

if __name__ == '__main__':
    uvicorn.run(app=app)