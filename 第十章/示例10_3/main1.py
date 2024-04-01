# 【示例10.3】 第十章 第10.1节 main1.py
from fastapi import FastAPI
import uvicorn
app = FastAPI()
data = {                         # 应用中的模拟数据
    "cat": "猫",
    "dog": "狗"
}
@app.get("/{name}")              # 注册路由法就很难，定义路径参数
async def index(name: str):      # 定义路径操作函数
    return {"name": data[name]}  # 返回数据

if __name__ == '__main__':
    uvicorn.run(app)