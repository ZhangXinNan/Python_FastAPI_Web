# 【示例7.2】 第七章 第7.2节 models.py
from sqlalchemy import Column, String, Integer, Boolean
from .database import Base

class UserInDB(Base):  # 定义用户表，继承自Base
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    username = Column('username', String(50))
    full_name = Column('full_name', String(50))
    email = Column('email', String(100))
    hashed_password = Column('hashed_password', String(64))
