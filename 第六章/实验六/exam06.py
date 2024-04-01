# 第六章 实验代码 exam06.py

import uvicorn
from fastapi import Depends
from fastapi import FastAPI
from pydantic import BaseModel  # 导入基础模型类
from pymongo import MongoClient

app = FastAPI()

MONGO_DATABASE_URL = 'mongodb://localhost:27017/'  # mongodb 连接字符串

def get_db():  # 定义依赖注入函数，用于连接mongodb
    client = MongoClient(MONGO_DATABASE_URL)
    db = client['test']
    try:
        yield db
    finally:
        client.close()

class Order(BaseModel):  # 定义数据模型类，继承自BaseModel类
    name: str  # 定义字段name，类型 str
    num: float  # 定义字段num，类型float
    unit: str  # 定义字段unit，类型 str
    price: float  # 定义字段price，类型float

class OrderCreate(Order):
    id: int = 0

def create_NewRecord(db: MongoClient, order: OrderCreate):  # 写入数据库表中
    mycol = db['orders']
    mycol.insert_one(order.dict())
    return order

@app.post("/order/", response_model=Order)  # 注册路由路径
async def createorder(order: OrderCreate,  # 定义路径操作函数
                      db: MongoClient = Depends(get_db)):
    return create_NewRecord(db=db, order=order)

if __name__ == '__main__':
    uvicorn.run(app=app)
