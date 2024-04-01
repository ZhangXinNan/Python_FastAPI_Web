# 【示例1.11】 第一章 第1.4.4节 code1_11.py
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
import uvicorn

async def root(request):                       # 定义异步函数，参数为请求对象
    return JSONResponse({'hello': '三酷猫'})    # 返回JSON响应

app = Starlette(debug=True, routes=[           # 创建服务实例
    Route('/', root),                          # 定义路由，将路径 / 指向异步函数root
])

if __name__ == '__main__':
    uvicorn.run(app=app)                       # 使用uvicorn起动服务