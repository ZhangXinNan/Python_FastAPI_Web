# 【示例6.8】第六章 6.4 小节 myredis.py
from typing import Optional
from pydantic import BaseModel
import uvicorn
from fastapi import Depends, FastAPI
from redis import Redis, ConnectionPool
import json
app = FastAPI()

def get_rdb():                                       # 定义依赖函数，用于连接redis
    pool = ConnectionPool(host='127.0.0.1', port=6379,)
    rdb = Redis(connection_pool=pool)
    try:
        yield rdb
    finally:
        rdb.close()

class Item(BaseModel):                                  # 定义数据模型
    title: str
    description: Optional[str] = None

@app.post('/item/', response_model=Item)                 # 注册路由路径
async def create_item(item: Item,                        # 定义路径操作函数，定义参数item
                      rdb: Redis = Depends(get_rdb)     # 定义依赖项数据库
                      ):                                 # 获取集合
    obj = rdb.set('item_name', json.dumps(item.dict()))   # 将对象转换成JSON字符串并保存
    return item

@app.get('/item/', response_model=Item)                 # 注册路由路径
async def get_item(rdb: Redis = Depends(get_rdb)):     # 定义路径操作函数，定义依赖项数据库
    obj = rdb.get('item_name')                               # 获取集合
    return json.loads(obj)               # 将数据库中的对象转换为dict并返回

if __name__ == '__main__':
    uvicorn.run(app=app)