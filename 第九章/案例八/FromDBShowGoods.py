# FromDBShowGoods.py
from fastapi import FastAPI, Request
# 连接SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel  # 导入基础模型类
from fastapi import Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates  # 导入Jinja2模块
from fastapi.staticfiles import StaticFiles  # 导入静态资源组件
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


def get_goods(db: session, skip: int = 0, limit: int = 100):  # 读取t_order表里的数据
    return db.query(Order).offset(skip).limit(limit).all()


templates = Jinja2Templates(directory="templates")  # 定义模板引擎实例，并指定模板目录


@app.get("/goods/", response_class=HTMLResponse)  # 设置路径路由，指定响应数据格式
def read_goods(request: Request, skip: int = 0, limit: int = 100, db: session = Depends(get_db)):  # 定义路径操作函数
    goods = get_goods(db, skip=skip, limit=limit)
    name = "三酷猫！你的订单来啦！"
    return templates.TemplateResponse("index.html",  # 返回模板响应
                                      {"request": request, "name": name, "goods": goods})  # 传递给模板的数据


if __name__ == '__main__':
    uvicorn.run(app=app)