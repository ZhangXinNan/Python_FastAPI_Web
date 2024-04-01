# 【示例9.1】 第九章 第9.1节 code9_1.py
from fastapi import FastAPI
from pydantic import BaseSettings    # 导入BaseSettings模块
import uvicorn
from fastapi import FastAPI
from pydantic import BaseSettings     # 第一步，导入BaseSettings模块
import uvicorn

class Settings(BaseSettings):          # 第二步，自定义类，继承自BaseSettings
    my_name: str = '匿名'           # 第三步，定义环境变量 my_name
    my_age: int = 40               # 定义环境变量 my_age
    #class Config:                  # 自定义类的配置项
    #    case_sensitive = False       # 默认为大写小不敏感

settings = Settings()                 # 第四步，自定义设置类实例
app = FastAPI()                    # FastAPI应用实例

@app.get("/")                      # 定义路由
async def info():                    # 定义路径操作函数
    return {                       # 第五步，返回获取到的环境变量
        "my_name": settings.my_name,
        "my_age": settings.my_age,
    }
if __name__ == '__main__':
    uvicorn.run(app=app)