# 【示例4.18】 第四章 第4.2节 code4_18.py
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
app = FastAPI()

@app.get("/headers/")                           # 注册路由路径
def get_headers():                              # 创建路径操作函数
    content = {"message": "Hello threecoolcat"}  # 创建响应数据
    headers = {"X-three-cool-cat": "miao-miao-miao",  # 自定义Header
               "User-Agent": "threecoolcat Browser"}  # 内置Header
    response = JSONResponse(content=content, headers=headers) # 创建响应类实例
    return response                                    # 返回响应类实例
if __name__ == '__main__':
    uvicorn.run(app=app)