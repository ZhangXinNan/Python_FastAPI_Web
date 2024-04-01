# 【示例2.1】 第二章 第2.2.1节 code2_1.py
from fastapi import FastAPI
import uvicorn
app = FastAPI()                  # 创建应用实例

@app.get("/items/{item_id}")     # 注册路由路径，使用{}定义路径参数，参数名为item_id
async def read_item(item_id):    # 函数操作函数中定义同名的路径参数
    print(item_id)               # 打印路径参数值
    return {"item_id": item_id}  # 用return关键字，将得到的参数返回给浏览器端

if __name__ == '__main__':
    uvicorn.run(app=app)