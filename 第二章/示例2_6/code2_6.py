# 【示例2.6】 第二章 第2.3.2节 code2_6.py
from typing import Optional
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")         # 注册路由路径，定义路径参数
async def read_item(                 # 定义路径操作函数
        item_id: str,                # 定义路径参数item_id,参数类型str
        q: Optional[str] = None      # 定义可选查询参数q，参数类型str，默认值None
):
    if q:                            # 传入可选查询参数时，并返回item_id, q
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}      # 未传入可选查询参数时，返回item_id

if __name__ == '__main__':
    uvicorn.run(app=app)