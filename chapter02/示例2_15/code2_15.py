# 【示例2.15】 第二章 第2.5.1节 code2_15.py
from fastapi import FastAPI, Form  # 导入Form对象
import uvicorn
app = FastAPI()

@app.post("/login/")              # 注册路由路径
async def login(                  # 定义路径操作函数
        username: str = Form(...), # 定义查询参数，数据类型是str，初始值Form
        password: str = Form(...)  # 定义查询参数，数据类型是str，初始值Form
):
    ...                            # 处理登录的代码
    return {"username": username}

if __name__ == '__main__':
    uvicorn.run(app=app)