# FindSeaGoods_Ext.py
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi import Query
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse  # 导入普通文本响应类
from pydantic import BaseModel
from starlette.exceptions import HTTPException as StarletteHTTPException  # 使用别名导入

app = FastAPI()


@app.exception_handler(StarletteHTTPException)  # 注册系统异常StarletteHTTPException
async def http_exception_handler(request, exc):  # 覆盖系统异常处理器，重写方法实现
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


@app.exception_handler(RequestValidationError)  # 注册系统异常RequestValidationError
async def validation_exception_handler(request, exc):  # 覆盖系统异常处理器，重写方法
    return PlainTextResponse(str(exc), status_code=400)


class One(BaseModel):
    name: str
    num: int
    unit: str
    price: float


goods_table = {'野生大黄鱼': [20, '斤', 168],
               '对虾': [100, '斤', 48],
               '比目鱼': [200, '斤', 69],
               '黄花鱼': [500, '斤', 21]}


# @app.get("/goods/")                     # 注册路由路径
@app.post("/goods/", response_model=One)
async def findGoods(one: One, name: str = Query(..., max_length=10, min_length=2)):  # 定义路径操作函数
    if name in goods_table.keys():
        values = goods_table[name]
        one.name = name
        one.num = values[0]
        one.unit = values[1]
        one.price = values[2]
        return one
    else:
        raise HTTPException(status_code=418, detail="海鲜" + name + "不存在！")


if __name__ == '__main__':
    uvicorn.run(app=app)
