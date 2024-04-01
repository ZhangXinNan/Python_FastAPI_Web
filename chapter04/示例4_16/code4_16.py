# 【示例4.16】 第四章 第4.1节 code4_16.py
from fastapi import FastAPI, Request
import uvicorn
app = FastAPI()

@app.get("/host/")  # 定义路径参数
def read_root(request: Request):  # 直接使用Request对象
    client_host = request.client.host  # 从请求对象中获取
    return {"客户端主机地址": client_host}

if __name__ == '__main__':
    uvicorn.run(app=app)