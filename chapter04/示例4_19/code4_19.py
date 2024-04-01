# 【示例4.19】 第四章 第4.2节 code4_19.py
from fastapi import FastAPI, status
import uvicorn
app = FastAPI()
@app.get("/items/", status_code=201)  # 注册路由路径，设置状态码
async def create_item(name: str):      # 定义路径操作函数
    return {"name": name}
if __name__ == '__main__':
    uvicorn.run(app=app)