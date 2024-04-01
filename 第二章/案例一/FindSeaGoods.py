# FindSeaGoods.py
from fastapi import FastAPI
import uvicorn

app = FastAPI()
goods_table = {'野生大黄鱼': [20, '斤', 168],
               '对虾': [100, '斤', 48],
               '比目鱼': [200, '斤', 69],
               '黄花鱼': [500, '斤', 21]}


@app.get("/goods/")  # 注册路由路径
async def findGoods(name):  # 定义路径操作函数

    return name + '' + str(goods_table[name])


if __name__ == '__main__':
    uvicorn.run(app=app)