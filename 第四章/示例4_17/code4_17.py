# 【示例4.17】 第四章 第4.2节 code4_17.py
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
app = FastAPI()

@app.post("/cookie/")
def create_cookie():
    content = {"message": "threecoolcats like cookies"}                        # 创建响应数据
    response = JSONResponse(content=content)                                   # 创建响应类实例
    response.set_cookie(key="user_id", value="9527")  # 设置Cookie
    return response                                                            # 返回响应类实例

if __name__ == '__main__':
    uvicorn.run(app=app)