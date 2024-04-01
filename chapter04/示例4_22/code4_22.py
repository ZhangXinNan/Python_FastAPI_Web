# 【示例4.22】 第四章 第4.3节 code4_22.py
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

class MyException(Exception):                    # 定义异常类，继承自Exception
    def __init__(self, name: str):
        self.name = name

@app.exception_handler(MyException)               # 注册全局异常管理器
async def my_exception_handler(                   # 定义异常处理函数
        request: Request,                        # 请求类实例
        exc: MyException                         # 异常类实例
        ):
    return JSONResponse(                                 # 返回响应类实例
        status_code=418,                                  # 响应状态码
        content={"message": f"OMG，{exc.name}又迷路了"},    # 状态文本
    )

@app.get("/cats/{name}")                        # 注册路由路径，定义路径参数
async def find_cats(name: str):
    if name == "三酷猫":
        raise MyException(name=name)            # 抛出自定义异常
    return {"cat": name}

if __name__ == '__main__':
    uvicorn.run(app=app)