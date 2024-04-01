# 【示例10.1】 第十章 第10.1节 main.py
from fastapi import FastAPI
from fastapi.testclient import TestClient
import uvicorn
app = FastAPI()

@app.get("/")                         # 注册路由路径
async def index():                    # 定义路径操作函数
    return {"name": "threecoolcat"}   # 返回一个对象

client = TestClient(app)              # 创建TestClient实例

def test_index():                     # 定义测试函数
    response = client.get("/")        # 使用TestClient的实例发起请求，接收返回数据
    assert response.status_code == 200                  # 断言： 状态码
    assert response.json() == {"name": "dog"}  # 断言：返回对象


if __name__ == '__main__':
    uvicorn.run(app)                  # 起动Web服务