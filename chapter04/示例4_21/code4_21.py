# 【示例4.21】 第四章 第4.3节 code4_21.py
from fastapi import FastAPI, HTTPException
import uvicorn
app = FastAPI()

items = {"1": "cat"}                                  # 定义模拟数据

@app.get("/items/{item_id}")                          # 注册路由路径，定义路径参数
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="未找到指定项目",headers={"X-Error": "访问项目出错"})  # 使用raise抛出异常
    return {"item": items[item_id]}
if __name__ == '__main__':
    uvicorn.run(app=app)