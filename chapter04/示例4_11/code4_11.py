# 【示例4.11】 第四章 第4.1节 code4_11.py
from typing import Optional
import uvicorn
from fastapi import Body, FastAPI
from pydantic import BaseModel, Field    # 导入Field函数

app = FastAPI()

class Item(BaseModel):                 # 定义数据模型类、继承自BaseModel
    name: str                         # 定义字段，类型str
    description: Optional[str] = Field(    # 定义可选字段，类型str，默认值是Field函数
        None,                       # 字段默认值
        title="一大段说明信息",       # 字段标题
        max_length=300,              # 字段内容最大长度
    )
    price: float = Field(                # 定义字段，类型float
        ...,                          # 必选字段
        gt=0,                        # 验证规则，数值大于0
        description="单价必须大于0")   # 字段描述
    tax: Optional[float] = None           # 定义可选字段，类型float

@app.post("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(...)):
    return {"item_id": item_id, "item": item}

if __name__ == '__main__':
    uvicorn.run(app=app)