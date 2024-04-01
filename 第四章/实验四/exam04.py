# 第四章 实验代码 exam04.py
from fastapi import FastAPI, Request
import uvicorn
from fastapi.middleware.trustedhost import TrustedHostMiddleware

app = FastAPI()

app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=["127.0.0.1"]   # 添加中间件
)

goods_table = {'野生大黄鱼': [20, '斤', 168],
               '对虾': [100, '斤', 48],
               '比目鱼': [200, '斤', 69],
               '黄花鱼': [500, '斤', 21]}

@app.get("/goods/")  # 注册路由路径
async def findGoods(name, request: Request):  # 定义路径操作函数， 添加request
    client_host = request.client.host
    with open('log.txt', 'a') as f:               # 追加模型打开文件
        f.write('来访地址：' + client_host + '\n')  # 写入内容
        f.close()                                 # 关闭文件
    return name + '' + str(goods_table[name])

if __name__ == '__main__':
    uvicorn.run(app=app)