# 【示例2.9】 第二章 第2.3.5节 code2_9.py
from typing import Optional
from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get("/users/{user_id}/items/{item_id}")  # 注册路由路径，定义两个路径参数
async def read_user_item(      # 定义路径操作函数
    user_id: int,              # 定义路径参数，类型int
    item_id: str,              # 定义路径参数，类型str
    q: Optional[str] = None,   # 定义可选查询参数，类型str
    short: bool = False        # 定义带默认值的查询参数，类型bool
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "这是一个神奇的东西，而且名字还特别长"}
        )
    else:
        item.update({'short': short})
    return item

if __name__ == '__main__':
    uvicorn.run(app=app)