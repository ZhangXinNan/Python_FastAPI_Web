# 【示例1.1】 第一章 第1.3.1节
from fastapi import FastAPI               # 导入FastAPI类
import uvicorn                            # 导入uvicorn，ASGI容器

app = FastAPI()                           # 创建应用实例

@app.get("/")                             # 定义路由路径
async def root():                         # 定义路径操作函数
    return {"message": "Hello 三酷猫！"}   # 返回“Hello 三酷猫！”信息到浏览器上

if __name__ == "__main__":
    uvicorn.run(app=app)                  # 在ASGI容器中起动FastAPI应用实例