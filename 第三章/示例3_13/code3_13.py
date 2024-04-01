# 【示例3.13】 第三章 第3.3节 code3_13.py
from fastapi import FastAPI
from fastapi.responses import FileResponse  # 导入文件响应
import uvicorn
some_file_path = "large-video-file.mp4"  # 运行代码时请替换成真实的视频文件路径
app = FastAPI()

@app.get("/")                            # 注册路由路径
async def main():
    return FileResponse(some_file_path)  # 直接使用文件名参数返回文件响应
if __name__ == '__main__':
    uvicorn.run(app=app)