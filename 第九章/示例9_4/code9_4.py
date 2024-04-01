# 【示例9.4】 第九章 第9.1节 code9_4.py
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
##### 开始 Flask App #####
from flask import Flask, escape, request
flaskapp = Flask(__name__)
@flaskapp.route("/")
def flask_main():
    name = request.args.get("name", "Flask")
    return f"Hello, {escape(name)} !"
##### 结束 Flask App #####

app = FastAPI()                               # 定义主应用

@app.get("/app")                              # 定义路由
def read_main():
    return {"message": "Hello 三酷猫"}

app.mount("/flask", WSGIMiddleware(flaskapp))   # 挂载外部应用
if __name__ == '__main__':
    uvicorn.run(app=app)