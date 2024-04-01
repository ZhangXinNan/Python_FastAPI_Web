# 【示例3.7】 第三章 第3.3节 code3_7.py
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse  # 导入响应类
import uvicorn
app = FastAPI()

@app.get("/", response_class=PlainTextResponse)  # 设置响应类为纯文本
async def main():
    return "Hello World"
if __name__ == '__main__':
    uvicorn.run(app=app)