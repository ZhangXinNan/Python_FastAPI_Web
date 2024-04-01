# 【示例4.24】 第四章 第4.4节 code4_24.py
import time
import uvicorn
from fastapi import FastAPI, Request

app = FastAPI()

@app.middleware("http")                                          # 使用装饰器，将函数注册为中间件函数
async def add_process_time_header(request: Request, call_next):  # 定义中间件函数，包含两个参数
    # 此处在路径操作收到请求之前
    start_time = time.time()                                     # 记录时间点1
    response = await call_next(request)                          # 获取响应类实例
    # 此处在生成响应数据但返回之前
    process_time = time.time() - start_time                      # 计算处理时间
    response.headers["X-Process-Time"] = str(process_time)       # 修改响应Header
    return response                                              # 返回响应实例

if __name__ == '__main__':
    uvicorn.run(app=app)