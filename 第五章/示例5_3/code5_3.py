# 【示例5.4】 第五章 第5.4节 code5_3.py
from typing import Optional
import uvicorn
from fastapi import Cookie, Depends, FastAPI

app = FastAPI()

def query_extractor(q: Optional[str] = None):    # 定义依赖函数1
    return q

def params_extractor(                            # 定义依赖函数2
        q: str = Depends(query_extractor),       # 定义依赖项
        last_q: Optional[str] = Cookie(None)     # Cookie参数
):
    if not q:                                    # 如果未传入参数q则使用Cookie中的参数
        return last_q
    return q

@app.get("/items/")                              # 注册路由路径
async def read_query(                            # 定义路径操作函数
        params: str = Depends(params_extractor)  # 定义依赖项
):
    return {"params": params}

if __name__ == '__main__':
    uvicorn.run(app=app)