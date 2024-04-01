# 【示例4.27】 第四章 第4.4节 code4_27.py
from fastapi import FastAPI
from fastapi.middleware.trustedhost import TrustedHostMiddleware          # 导入中间件
import uvicorn
app = FastAPI()

app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=["example.com", "*.example.com"] # 添加中间件
)

@app.get("/")
async def main():
    return {"message": "Hello World"}

if __name__ == '__main__':
    uvicorn.run(app=app)