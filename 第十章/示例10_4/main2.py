# 【示例10.4】 第十章 第10.1节 main2.py
from fastapi import FastAPI, Depends
import uvicorn
app = FastAPI()

async def sms_sender(text: str):                   # 定义依赖函数
    print(f'调用短信平台发送短信，内容为：{text}')      # 发送短信的代码
    return f'成功发送内容：{text}'                   # 返回值

@app.get("/sendsms")                           # 注册路由路径，定义路径参数
async def sendsms(sms = Depends(sms_sender)):      # 定义路径操作函数
    return {'data': sms}

if __name__ == '__main__':
    uvicorn.run(app)