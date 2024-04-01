# 【示例4.23】 第四章 第4.3节 code4_23.py
from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse  # 导入普通文本响应类
from starlette.exceptions import HTTPException as StarletteHTTPException # 使用别名导入
import uvicorn
app = FastAPI()

@app.exception_handler(StarletteHTTPException)   # 注册系统异常StarletteHTTPException
async def http_exception_handler(request, exc):  # 覆盖系统异常处理器，重写方法实现
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


@app.exception_handler(RequestValidationError)   # 注册系统异常RequestValidationError
async def validation_exception_handler(request, exc):  # 覆盖系统异常处理器，重写方法
    return PlainTextResponse(str(exc), status_code=400)


@app.get("/items/{item_id}")  # 注册路由路径，定义路径参数
async def read_item(item_id: int):
    if item_id == 3:                          # 如果item_id==3时，抛出异常HTTPException
        raise HTTPException(status_code=418, detail="禁止使用3")
    return {"item_id": item_id}

if __name__ == '__main__':
    uvicorn.run(app=app)