# 【示例9.2】 第九章 第9.1节 code9_2.py
from fastapi import FastAPI
import uvicorn
app = FastAPI()
def send_msg_manager(action):
    print(f'通知管理员，XX主机的XX程序于XX时间{action}了')

@app.on_event("startup")
async def startup_event():
    # raise Exception('ss')
    send_msg_manager('起动')

@app.on_event("startup")
async def startup_event():
    send_msg_manager('起动2')

@app.on_event("shutdown")
async def shutdown_event():
    raise Exception(1)
    send_msg_manager('关闭2')

@app.on_event("shutdown")
async def shutdown_event():
    send_msg_manager('关闭')


@app.get("/")
async def read_items(item_id: str):
    return "hello, threecoolcat"

if __name__ == '__main__':
    uvicorn.run(app)