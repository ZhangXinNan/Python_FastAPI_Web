# 【示例5.2】 第五章 第5.2节 code5_2.py
from typing import Optional
import uvicorn
from fastapi import Depends, FastAPI

app = FastAPI()

class DepParams:                                         # 定义依赖类
    def __init__(self, q: Optional[str] = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit

@app.get("/items/")                                     # 注册路由路径
async def read_items(                                   # 定义路径操作函数
        params: DepParams = Depends(DepParams)         # 参数中定义依赖项
):
    return params                                      # 返回依赖项的结果

if __name__ == '__main__':
    uvicorn.run(app=app)