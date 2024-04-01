# 【示例7.1】 第七章 第7.2节 code7_1.py
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer         # 导入安全模块
import uvicorn
app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")    # 创建依赖类实例

@app.get("/items/")                                        # 注册路由路径
async def read_items(                                      # 定义路径操作函数
        token: str = Depends(oauth2_scheme)                # 定义依赖项
):
    return {"token": token}

if __name__ == '__main__':
    uvicorn.run(app=app)