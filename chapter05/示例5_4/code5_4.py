# 【示例5.5】 第五章 第5.5节 code5_4.py
from fastapi import Depends, FastAPI, Header, Cookie, HTTPException
import uvicorn
app = FastAPI()

async def verify_token(x_token: str = Header(...)):     # 定义依赖函数1
    if x_token != "my-token":                           # 取值不合法时抛出异常
        raise HTTPException(status_code=400, detail="Token已失效")
    # 没有返回值

async def check_userid(userid: str = Cookie(...)):        # 定义依赖函数2
    if userid != "9527":                                  # 取值不合法时抛出异常
        raise HTTPException(status_code=400, detail="无效的用户")
    return userid                                         # 有返回值

@app.get("/items/",                                                   # 装饰器中注册路由路径
         dependencies=[Depends(verify_token), Depends(check_userid)]) # 装饰器中设置依赖项列表
async def read_items():
    return "hello 三酷猫"

if __name__ == '__main__':
    uvicorn.run(app=app)