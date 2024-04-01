# 【示例4.20】 第四章 第4.2节 code4_20.py
from fastapi import FastAPI, Response, status  # 导入Response对象
import uvicorn
app = FastAPI()

items = {"1": "cat"}                                      # 模拟数据

@app.get("/items/{item_id}", status_code=200)              # 默认响应状态码
def get_or_create_item(item_id: str, response: Response):  # 路径操作函数中定义Response类实例
    if item_id not in items:
        items[item_id] = "dog"
        response.status_code = status.HTTP_201_CREATED     # 自定义的响应状态码
    return items[item_id]
if __name__ == '__main__':
    uvicorn.run(app=app)