# 【示例3.8】 第三章 第3.3节 code3_8.py
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
app = FastAPI()

html_content = """
    <html>
        <head>
            <title>浏览器顶部的标题</title>
        </head>
        <body>
            <h1>三酷猫</h1>
        </body>
    </html>
    """
@app.get("/html/", response_class=HTMLResponse)  # 设置响应类为HTML响应
async def read_items1():
    # 直接返回HTML文本
    return html_content

@app.get("/default/")  # 未设置响应类
async def read_items2():
    # 使用HTMLResponse对象返回数据
    return HTMLResponse(content=html_content)
if __name__ == '__main__':
    uvicorn.run(app=app)