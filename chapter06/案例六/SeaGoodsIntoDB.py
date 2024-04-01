# SeaGoodsIntoDB.py
# 连接SQLAlchemy
import pymysql
from fastapi import FastAPI

pymysql.install_as_MySQLdb()
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel  # 导入基础模型类
from fastapi import Depends
import uvicorn

app = FastAPI()


class Goods(BaseModel):  # 定义数据模型类，继承自BaseModel类

    name: str  # 定义字段name，类型 str
    num: float  # 定义字段num，类型float
    unit: str  # 定义字段unit，类型 str
    price: float  # 定义字段price，类型float


engine = create_engine("mysql://root:cats123.@127.0.0.1:3306/cat?charset=utf8")
session = sessionmaker(autocommit=False, bind=engine)  # 创建本地会话


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


Base = declarative_base()  # 创建数据模型基础类


class Order(Base):  # 数据库表模型
    # 指定数据库中的表名
    __tablename__ = "t_order"
    # 定义类的属性，对应表中的字段
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20))
    num = Column(Float)
    unit = Column(String(4))
    price = Column(Float)


Base.metadata.create_all(bind=engine)


class OrderCreate(BaseModel):  # ORM模式读写字段
    # 配置项中起用orm模式
    id: int = 0
    name: str  # 定义字段name，类型 str
    num: float  # 定义字段num，类型float
    unit: str  # 定义字段unit，类型 str
    price: float  # 定义字段price，类型float

    class Config:
        orm_mode = True


def create_NewRecord(db: session, good: Goods):  # 写入数据库表中

    db_order = Order(name=good.name, num=good.num, unit=good.unit, price=good.price)
    # 第二步，将数据模型实例添加到会话
    db.add(db_order)
    # 第三步，提交会话
    # db.flush()
    db.commit()
    # 第四步，刷新实例，用于获取数据或者生成数据库中的ID
    db.refresh(db_order)

    return db_order


@app.post("/goods/", response_model=OrderCreate)  # 注册路由路径
async def findGoods(good: Goods,  # 定义路径操作函数
                    db: session = Depends(get_db)):
    return create_NewRecord(db=db, good=good)


if __name__ == '__main__':
    uvicorn.run(app=app)
