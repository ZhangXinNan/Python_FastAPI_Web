# 【示例6.1】 第六章 第6.1节 code6_1.py
# 连接SQLAlchemy
# 第一步，导入SQLAlchemy组件包
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 第二步，创建数据连接引擎
engine = create_engine("mysql://user:password@mysqlsserver/db?charset=utf8")
# engine = create_engine("postgresql://user:password@postgresserver/db")
# engine = create_engine("sqlite:///./sql_app.db", connect_args={"check_same_thread": False})
# 第三步，创建本地会话
session = sessionmaker(autocommit=False, bind=engine)

