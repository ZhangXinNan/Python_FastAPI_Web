# 【示例3.2】 第三章 第3.2节 code3_2.py
from typing import Optional
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserIn(BaseModel):                   # 定义数据模型
    username: str                        # 定义字段用户名，类型str
    password: str                        # 定义字段密码，类型str
    email: str                            # 定义邮箱邮箱，类型str
    full_name: Optional[str] = None         # 定义可选字段全名，类型str

class UserOut(BaseModel):                 # 定义数据模型
    username: str                       # 定义字段用户名，类型str
    email: str                              # 定义邮箱邮箱，类型str
    full_name: Optional[str] = None     # 定义可选字段全名，类型str

@app.post("/user/", response_model=UserOut)  # 注册路由路径，定义响应模型为UserOut
async def create_user(user: UserIn):         # 定义请求模型为UserIn
    return user  # 返回请求数据

if __name__ == '__main__':
    uvicorn.run(app=app)