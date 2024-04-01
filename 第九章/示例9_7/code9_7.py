# 【示例9.6】 第九章 第9.3节 code9_6.py
from typing import Optional
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates  # 导入Jinja2模块
from fastapi.staticfiles import StaticFiles     # 导入静态资源组件
import uvicorn
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static") # 挂载静态资源
templates = Jinja2Templates(directory="templates")  # 定义模板引擎实例，并指定模板目录

@app.get("/", response_class=HTMLResponse)          # 定义路由路径，并指定响应类型为HTML
async def index(request: Request, name: Optional[str] = '！'):
    return templates.TemplateResponse("index.html", # 返回模板响应
             {"request": request, "name": name})    # 传递给模板的数据

if __name__ == '__main__':
    uvicorn.run(app=app)