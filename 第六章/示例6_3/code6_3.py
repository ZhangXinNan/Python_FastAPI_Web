# 【示例6.3】 第六章 第6.1节 code6_3.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
engine = create_engine(                              # 创建数据库连接引擎
    "sqlite:///./sql_app.db",
    connect_args={"check_same_thread": False}
)
session = sessionmaker(autocommit=False, bind=engine) # 创建本地会话

Base = declarative_base()   # 定义数据模型基类

class User(Base):            # 定义数据模型，用户
    __tablename__ = 'user'   # 数据库中的表名
    id = Column(Integer, primary_key=True)  # id列，主键
    name = Column('name', String(50))  # 定义字段name，字符串型，对应数据库中的name列
    bookrecords = relationship('BookRecord', backref='user')  # 图书列表字段

class BookRecord(Base):            # 定义数据模型，图书记录
    __tablename__ = 'book_record'   # 数据库中的表名
    id = Column(Integer, primary_key=True)  # id列，主键
    book_name = Column('book_name', String(50))   # 书名
    borrow_time = Column('borrow_time', DateTime)   # 借书时间
    user_id = Column(Integer, ForeignKey('user.id'))   # user_id ，外键

Base.metadata.create_all(bind=engine)                 # 在数据库中创建表结构
