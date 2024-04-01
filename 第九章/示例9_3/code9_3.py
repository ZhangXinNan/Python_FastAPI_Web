# 【示例9.3】 第九章 第9.1节 code9_3.py
from fastapi import FastAPI
import uvicorn
app = FastAPI()              # 定义主应用

@app.get("/app")
def read_main():
    return {"message": "Hello 三酷猫"}

catapp = FastAPI()            # 定义第一个子应用
@catapp.get("/hello")         # 在第一个子应用中定义路由
def read_sub():
    return {"message": "喵"}
app.mount("/cat", catapp)    # 在路径/cat下挂载子应用

dogapp = FastAPI()           # 定义第二个子应用
@dogapp.get("/hello")        # 在第二个子应用中定义路由
def read_sub():
    return {"message": "汪"}
app.mount("/dog", dogapp)    # 在路径/dog下挂载子应用

if __name__ == '__main__':
    uvicorn.run(app=app)