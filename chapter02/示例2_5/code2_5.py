# 【示例2.5】 第二章 第2.3.1节 code2_5.py
from fastapi import FastAPI
import uvicorn

app = FastAPI()

# 定义列表items
items= [{"name": "泰迪"}, {"name": "科基"}, {"name": "加菲"}, {"name": "斗牛"}, {"name": "英短"}]

@app.get("/items/")                                   # 注册路由路径，未定义路径参数
async def read_item(skip: int = 0, limit: int = 10):  # 定义了两个参数，参数类型 int
    print('参数skip:', skip)
    print('参数limit:', limit)
    return items[skip : skip + limit]  # 用下标方式从列表items中取出数据

if __name__ == '__main__':
    uvicorn.run(app=app)