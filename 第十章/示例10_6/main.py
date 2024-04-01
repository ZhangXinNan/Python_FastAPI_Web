# 【示例10.6】 第十章 第10.1节 async_test.py
from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get("/")                         # 定义路由
async def index():                    # 定义路径操作函数
    return {"name": "threecoolcat"}   # 返回一个对象

if __name__ == '__main__':            # 当本文件为入口文件时
    uvicorn.run(app)