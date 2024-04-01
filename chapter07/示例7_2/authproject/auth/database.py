# 【示例7.2】 第七章 第7.2节 database.py
# 第一步，导入SQLAlchemy库
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
# 第二步，创建数据连接引擎
engine = create_engine("sqlite:///./data.db",connect_args={"check_same_thread": False})
# 第三步，创建本地会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# 第四步，创建数据模型基类
Base = declarative_base()
