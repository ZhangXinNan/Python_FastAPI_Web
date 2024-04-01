# 【示例2.17】 第二章 第2.5.3节 code2_17.py
from fastapi import FastAPI, File, Form, UploadFile
import uvicorn
app = FastAPI()

@app.post("/files/")                  # 注册路由路径
async def create_file(                # 定义路径操作函数
        file: UploadFile = File(...), # 定义文件，类型UploadFile
        file2: UploadFile = File(...), # 定义文件2，类型UploadFile
        token: str = Form(...)        # 定义表单数据
):
    return {
        "token": token,
        "fileb_content_type": file.filename,
        "fileb_content_type": file.content_type,
    }
if __name__ == '__main__':
    uvicorn.run(app=app)