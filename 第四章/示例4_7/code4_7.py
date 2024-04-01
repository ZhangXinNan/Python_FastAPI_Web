# 【示例4.7】 第四章 第4.1节 code4_7.py
from typing import Optional
import uvicorn
from fastapi import FastAPI, Path  # 导入Path类

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(
    item_id: int = Path(                 #定义路径参数，设置默认值为Path函数
        ...,                             # 路径参数是必选参数
        description="项目ID是路径的一部分"  # 设置描述信息
    ),
):
    return {"item_id": item_id}

if __name__ == '__main__':
    uvicorn.run(app=app)