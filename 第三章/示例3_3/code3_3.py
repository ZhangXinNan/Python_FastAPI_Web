# 【示例3.3】 第三章 第3.2节 code3_3.py
from typing import List, Optional
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Data(BaseModel):                      # 定义数据模型
    name: str                              # 定义字段，无默认值
    description: Optional[str] = None          # 定义可选字段，默认值为None
    price: float                            # 定义字段，无默认值
    tax: float = 10.5                        # 定义字段，默认值为10.5
    tags: List[str] = []                       # 定义字段，默认值为[]

datas = {                                  # 模拟数据，包含3个对象的字典
    "min": {"name": "最小化", "price": 50.2},  # 仅设置了无默认值字段，其他字段均为默认值
    "max": {"name": "最大化", "description": "都有值", "price": 62, "tax": 20.2},  # 设置了字段值，与默认值不同
    "same": {"name": "默认", "description": None, "price": 50.2, "tax": 10.5, "tags": []},  # 设置了与默认值相同的字段
}

@app.get("/data/{data_id}",                 # 定义路径参数
         response_model=Data,              # 定义响应模型
         response_model_exclude_unset=True  # 使用属性忽略默认值
        )
async def read_item(data_id: str):
    return datas[data_id]                    # 返回模型数据中的某个对象

if __name__ == '__main__':
    uvicorn.run(app=app)