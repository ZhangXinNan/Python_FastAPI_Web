# 【示例3.11】 第三章 第3.3节 code3_11.py
from fastapi import FastAPI, Response
from typing import Optional
import uvicorn
app = FastAPI()

@app.get("/document/")                   # 注册路由路径路径
def get_legacy_data(id: Optional[int] = None):  # 定义可选查询参数
    data = """<?xml version="1.0" encoding="utf-8" ?>
    <Document>
        <Header>
            这里是页头
        </Header>
        <Body>
            这里是内容
        </Body>
        <Footer>
            这里是页脚
        </Footer>
    </Document>
    """
    # 直接返回Response对象，并指定media_type="application/xml"
    return Response(content=data, media_type="application/xml")

if __name__ == '__main__':
    uvicorn.run(app=app)