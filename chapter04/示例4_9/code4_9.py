# 【示例4.9】 第四章 第4.1节 code4_9.py
from typing import Optional
import uvicorn
from fastapi import Cookie, FastAPI

app = FastAPI()

@app.get("/items/")
async def read_items(user_id: Optional[str] = Cookie(None)):  # 定义Cookie参数，默认为空
    return {"user_id": user_id}

if __name__ == '__main__':
    uvicorn.run(app=app)