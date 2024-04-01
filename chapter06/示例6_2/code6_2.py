# 【示例6.2】 第六章 第6.1节 code6_2.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine(                              # 创建数据库连接引擎
    "sqlite:///./sql_app.db",
    connect_args={"check_same_thread": False}
)
session = sessionmaker(autocommit=False, bind=engine) # 创建本地会话
Base = declarative_base()                             # 创建模型基类

class User(Base):                                     # 定义数据模型类
    __tablename__ = 'user'                            # 数据库中对应的表名
    id = Column('id', Integer, primary_key=True)      # 定义字段id，整型，对应数据库的id列
    name = Column('name', String(50), primary_key=True)   # 定义字段name，字符串型，对应数据库中的name列

Base.metadata.create_all(bind=engine)                 # 在数据库中创建表结构
