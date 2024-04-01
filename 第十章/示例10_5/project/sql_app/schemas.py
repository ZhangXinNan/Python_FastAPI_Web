# 【示例6.5】第六章 6.2 小节 schemas.py
# 第一步，导入相关的模块
from typing import List, Optional
from pydantic import BaseModel

# 第二步，声明BookBase模型，从BaseModel继承
class BookBase(BaseModel):
    # 第三步，声明模型的属性
    title: str
    description: Optional[str] = None

# 第四步，声明ItemCreate模型，从ItemBase继承
class BookCreate(BookBase):
    pass
# 第五步，声明Item模型，从ItemBase继承
class Book(BookBase):
    id: int
    owner_id: int
    # 第六步，配置项中起用orm模式
    class Config:
        orm_mode = True

# 第七步，同样的方式声明一组User模型
class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    books: List[Book] = []
    # 配置项中起用orm模式
    class Config:
        orm_mode = True