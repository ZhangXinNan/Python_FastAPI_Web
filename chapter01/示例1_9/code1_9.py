# 【示例1.9】 第一章 第1.4.3节 code1_9.py
from pydantic import BaseModel                      # 从pydantic模块中导入BaseModel

class User(BaseModel):                              # 定义数据模型User，继承BaseModel
    id: int                                         # 字段 id 类型int
    name = '三酷猫'                                  # 字段 name 未指定类型 值为 '三酷猫'

user = User(id='123')                               # 创建数据模型实例
assert user.id == 123                               # 断言 实例的字段 id
assert user.name == '三酷猫'                         # 断言 实例的字段 name
assert user.__fields_set__ == {'id'}                # 断言 user的字段集合
assert user.dict() == dict(user)                    # 断言 实例获取的字典数据
assert user.dict() == {'id': 123, 'name': '三酷猫'}  # 断言 实例获取的字典数据
user.id = 321                                       # 修改 实例的字段值
assert user.id == 321                               # 断言 实例的字段 id