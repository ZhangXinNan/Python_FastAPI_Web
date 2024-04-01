# 【示例2.8】 第二章 第2.3.4节 code2_8.py
from typing import Optional
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")      # 注册路由路径，定义路径参数item_id
async def read_item(              # 定义路径操作函数
        item_id: str,             # 定义路径参数， 类型str
        q: Optional[str] = None,  # 定义可选查询参数， 类型str
        short: bool = False       # 定义查询参数，类型bool，默认值False
):
    item = {"item_id": item_id}   # 创建对象item，赋值路径参数
    if q:                         # 当传入了可选查询参数q时，更新item
        item.update({"q": q})
    if not short:                 # 当传入了查询参数short，并且其值为True时，更新数据
        item.update(
            {"description": "这是一个神奇的东西，而且名字还特别长"}
        )
    return item                   # 返回数据

if __name__ == '__main__':
    uvicorn.run(app=app)