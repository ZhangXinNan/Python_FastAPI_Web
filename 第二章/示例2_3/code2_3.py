# 【示例2.3】 第二章 第2.2.4节 code2_3.py
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/users/me")                       # 注册静态路由路径 /users/me
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")               # 注册路由路径 /users/{user_id}
async def read_user(user_id: str):         # 定义路径参数user_id,类型str
    return {"user_id": user_id}

if __name__ == '__main__':
    uvicorn.run(app=app)