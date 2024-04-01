# 【示例3.9】 第三章 第3.3节 code3_9.py
from fastapi import FastAPI
from fastapi.responses import RedirectResponse  # 导入重定向类
import uvicorn
app = FastAPI()

@app.get("/three")
async def read_three():
    return RedirectResponse("https://github.com/threecoolcat")  # 返回重定向响应
if __name__ == '__main__':
    uvicorn.run(app=app)