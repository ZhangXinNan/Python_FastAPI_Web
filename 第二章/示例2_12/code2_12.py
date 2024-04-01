# 【示例2.12】 第二章 第2.4.3节 code2_12.py
from typing import Optional
import uvicorn
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):                # 定义数据模型类，继承自BaseModel
    name: str                         # 定义字段name，类型str
    description: Optional[str] = None # 定义可选字段description，类型str
    price: float                      # 定义字段price，类型float
    tax: Optional[float] = None       # 定义可选字段tax，类型float

@app.put("/items/{item_id}")          # 注册路由路径，使用PUT方法，定义路径参数
async def update_item(
    *,                                # python语法，表示后面的参数都是键值对
    item_id: int = Path(..., title="元素ID", ge=0, le=1000),  #路径参数，类型int，大于等于0小于等于1000
    q: Optional[str] = None,          # 可选查询参数，类型str
    item: Optional[Item] = None,      # 请求体，可选参数
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results                 #  将各个请求参数组合在一起返回
if __name__ == '__main__':
    uvicorn.run(app=app)