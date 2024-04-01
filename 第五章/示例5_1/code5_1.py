# 【示例5.1】 第五章 第5.2节 code5_1.py
from typing import Optional
import uvicorn
from fastapi import Depends, FastAPI

app = FastAPI()

async def dep_params(q: Optional[str] = None, skip: int = 0, limit: int = 100): # 定义依赖函数
    return {"q": q, "skip": skip, "limit": limit}

@app.get("/items/")                                 # 注册路由路径1
async def read_items(                               # 定义路径操作函数
        commons: dict = Depends(dep_params)         # 参数中定义依赖项
):
    return commons                                  # 返回依赖项的结果

@app.get("/users/")                                 # 注册路由路径1
async def read_users(                               # 定义路径操作函数
        commons: dict = Depends(dep_params)         # 参数中定义依赖项
):
    return commons                                  # 返回依赖项的结果

if __name__ == '__main__':
    uvicorn.run(app=app)