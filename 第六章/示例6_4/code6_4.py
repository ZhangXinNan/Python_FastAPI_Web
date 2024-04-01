# 【示例6.4】 第六章 第6.1节 code6_4.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey, Table, String
from sqlalchemy.orm import relationship
engine = create_engine(                              # 创建数据库连接引擎
    "sqlite:///./sql_app.db",
    connect_args={"check_same_thread": False}
)
session = sessionmaker(autocommit=False, bind=engine) # 创建本地会话

Base = declarative_base()   # 定义数据模型基类

user_action_rel = Table(      # 定义中间表
    'user_action_rel',        # 数据库中的表名
    Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),   # 外键，关联到user.id
    Column('action_id', Integer, ForeignKey('action.id'))  # 外键，关联到action.id
)

class User(Base):            # 定义数据模型，用户
    __tablename__ = 'user'   # 数据库中的表名
    id = Column(Integer, primary_key=True)  # id列，主键
    name = Column('name', String(50))
    actions = relationship('Action', secondary=user_action_rel, backref='user')

class Action(Base):            # 定义数据模型，功能点
    __tablename__ = 'action'   # 数据库中的表名
    id = Column(Integer, primary_key=True)
    name = Column('name', String(50))
    users = relationship('User', secondary=user_action_rel, backref='actions')

Base.metadata.create_all(bind=engine)                 # 在数据库中创建表结构