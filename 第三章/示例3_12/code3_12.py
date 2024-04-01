# 【示例3.12】 第三章 第3.3节 code3_12.py
from fastapi import FastAPI
from fastapi.responses import StreamingResponse  # 导入流响应
import uvicorn
some_file_path = "large-video-file.mp4"  # 运行代码时请替换成真实的视频文件路径
app = FastAPI()

@app.get("/")                                   # 注册路由路径
def main():
    file_like = open(some_file_path, mode="rb")  # 打开文件
    return StreamingResponse(file_like, media_type="video/mp4")  # 返回流并指定媒体类型
if __name__ == '__main__':
    uvicorn.run(app=app)