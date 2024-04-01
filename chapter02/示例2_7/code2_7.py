# 【示例2.7】 第二章 第2.3.3节 code2_7.py
from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get("/items/{item_id}")                       # 注册路由路径，定义了路径参数item_id
async def read_user_item(                          # 定义路径操作函数
        item_id: str,                              # 定义路径参数
        q: str                                     # 定义查询参数
):
    return {"item_id": item_id, "q": q}            # 返回参数值

if __name__ == '__main__':
    uvicorn.run(app=app)