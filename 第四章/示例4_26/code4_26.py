# 【示例4.26】 第四章 第4.4节 code4_26.py
from fastapi import FastAPI
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware # 导入中间件
import uvicorn
app = FastAPI()

app.add_middleware(HTTPSRedirectMiddleware)  # 添加中间件，无其他参数

@app.get("/")
async def main():
    return {"message": "Hello World"}
if __name__ == '__main__':
    uvicorn.run(app=app)