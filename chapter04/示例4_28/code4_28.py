# 【示例4.27】 第四章 第4.4节 code4_27.py
from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware  # 导入中间件
import uvicorn
app = FastAPI()

app.add_middleware(GZipMiddleware, minimum_size=1000)  # 添加中间件，设置压缩参数

@app.get("/")
async def main():
    return "somebigcontent"
if __name__ == '__main__':
    uvicorn.run(app=app)