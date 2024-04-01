# 【示例6.5】第六章 6.2 小节 models.py
# 第一步，导入SQLAlchemy组件包
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
# 第二步，从database模块中导入基类Base
from .database import Base
# 声明User模型，继承自Base
class User(Base):
    # 指定数据库中的表名
    __tablename__ = "user"
    # 定义类的属性，对应表中的字段
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), unique=True, index=True)
    hashed_password = Column(String(50))
    is_active = Column(Boolean, default=True)
    # 定义一对多关系
    books = relationship("Book", back_populates="owner")

# 声明Book模型，继承自Base类
class Book(Base):
    # 指定数据库中对应的表名
    __tablename__ = "book"
    # 定义类的属性，对应表中的字段
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True)
    description = Column(String(200), index=True)
    owner_id = Column(Integer, ForeignKey("user.id"))
    # 定义关联
    owner = relationship("User", back_populates="books")
