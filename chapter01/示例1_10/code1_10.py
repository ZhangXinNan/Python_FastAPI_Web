# 【示例1.10】 第一章 第1.4.3节 code1_10.py
from typing import List
from pydantic import BaseModel, Field

class Blackboard(BaseModel):          # 定义数据模型类继承自BaseModel
    size = 4000                       # 字段类型int
    color: str = Field(..., alias='颜色', gt=1, description='黑板的颜色，可选green和black')

class Table(BaseModel):                # 定义数据模型类继承自BaseModel
    position: str                      # 字段默认白

class ClassRoom(BaseModel):            # 定义数据模型类继承自BaseModel
    blackboard: Blackboard             # 字段类型使用数据模型类Body
    tables: List[Table]                # 字段类型使用列表泛型

m = ClassRoom(                        # 创建数据模型实例
    blackboard={'color': 'green' },
    tables=[{'position': '第一排左1'}, {'position': '第一排左2'}]
)

print(m)
print(m.dict())
