# 【示例4.25】 第四章 第4.4节 code4_25.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware   # 导入CORSMiddleware
import uvicorn
app = FastAPI()


origins = [                 # 定义可用域列表
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(        # 在应用上添加中间件
    CORSMiddleware,         # 内置中间件类
    allow_origins=origins,  # 参数1 可用域列表
    allow_credentials=True, # 参数2 允许cookie， 是
    allow_methods=["*"],    # 参数3 允许的方法， 全部
    allow_headers=["*"],    # 参数4 允许的Header，全部
)

@app.get("/")               # 注册路由路径
async def main():
    return {"message": "Hello World"}

if __name__ == '__main__':
    uvicorn.run(app=app)