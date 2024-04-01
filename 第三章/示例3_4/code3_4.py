# 【示例3.4】 第三章 第3.2节 code3_4.py
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

class UserIn(BaseModel):                   # 定义请求模型，用于接收请求数据
    username: str
    password: str
    phone: Optional[str]
    email: Optional[str]
    address: Optional[str]

class UserOut(BaseModel):                  # 定义响应模型，用于输出响应数据
    username: str
    phone: Optional[str]
    email: Optional[str]
    address: Optional[str]

class UserDB(BaseModel):                # 定义业务模型，用于逻辑处理
    username: str
    password_md5: str
    phone: Optional[str]
    email: Optional[str]
    address: Optional[str]

def get_md5(raw_password: str):            #生成密码哈希的模拟函数
    return "密码md5值" + raw_password

def save_user_logic(user_in: UserIn):          # 保存用户的逻辑处理
    password_md5 = get_md5(user_in.password)  # 生成模拟密码
    user_db = UserDB(**user_in.dict(), password_md5=password_md5) # 将请求模型的数据转换为业务模型
    print("此处应该是将user_db保存到数据库的操作代码")
    return user_db

@app.post("/user/", response_model=UserOut)   # 定义响应数据模型为UserOut
async def create_user(user_in: UserIn):         # 定义请求数据模型为UserIn
    user_saved = save_user_logic(user_in)    # 调用逻辑处理函数，执行数据保存动作
    return user_saved

if __name__ == '__main__':
    uvicorn.run(app=app)