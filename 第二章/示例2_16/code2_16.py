# 【示例2.16】 第二章 第2.5.2节 code2_16.py
from fastapi import FastAPI, File, UploadFile
import uvicorn
app = FastAPI()

@app.post("/files/")                 # 注册路由路径
async def create_file(               # 定义路径操作函数，第一种上传方式
        file: bytes = File(...)      # 定义文件参数，数据类型为bytes，初始值是File
):
    return {"file_size": len(file)}  # 返回文件大小

@app.post("/uploadfile/")            # 注册路由路径
async def create_upload_file(        # 定义路径操作函数，第二种上传方式
        file: UploadFile = File(...) # 定义文件参数，数据类型为UploadFile，初始值为File
):
    return {"filename": file.filename}  # 返回原始文件名
if __name__ == '__main__':
    uvicorn.run(app=app)