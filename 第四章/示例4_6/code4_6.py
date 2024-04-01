# 【示例4.6】 第四章 第4.1节 code4_6.py
from typing import Optional
import uvicorn
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    q: Optional[str] = Query(               # 定义查询参数q，默认值为Query类
        None,                               # 可选参数默认值None
        min_length=3,                       # 定义规则
        description="根据此参数查找匹配的数据",  # 参数详细说明
    ),
    name: Optional[str] = Query(            # 定义查询参数name
        None,                               # 可选参数默认值None
        deprecated=True,                    # 标记为弃用
        description="按名称查询"              # 参数说明
    )
):
    return {"q": q, "name": name}

if __name__ == '__main__':
    uvicorn.run(app=app)