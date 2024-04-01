# 【示例6.7】第六章 6.3 小节 mongo.py
from typing import Optional, List
from pydantic import BaseModel
import uvicorn
from fastapi import Depends, FastAPI
from pymongo import MongoClient
from bson.json_util import dumps
import json
app = FastAPI()

MONGO_DATABASE_URL = 'mongodb://localhost:27017/'     # mongodb 连接字符串


def get_db():                                          # 定义依赖函数，用于连接mongodb
    client = MongoClient(MONGO_DATABASE_URL)
    db = client['test']
    try:
        yield db
    finally:
        client.close()


class Item(BaseModel):                                  # 定义数据模型
    title: str
    description: Optional[str] = None

@app.post('/item/', response_model=Item)                 # 注册路由路径
async def create_item(item: Item,                        # 定义路径操作函数，定义参数item
                      db: MongoClient = Depends(get_db)  # 依赖数据库
                      ):
    mycol = db['items']                                  # 获取集合
    obj = mycol.insert_one(item.dict())                  # 保存一条数据
    return item

@app.get('/item/', response_model=List[Item])            # 注册路由路径路径
async def get_item(db: MongoClient = Depends(get_db)):   # 定义路径操作函数，依赖数据库
    mycol = db['items']                                  # 获取集合
    return json.loads(dumps(mycol.find()))               # 将数据库中的对象转换为dict并返回

if __name__ == '__main__':
    uvicorn.run(app=app)