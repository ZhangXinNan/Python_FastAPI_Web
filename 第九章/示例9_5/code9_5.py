# 【示例9.5】 第九章 第9.2节 code9_5.py
from fastapi import APIRouter

router = APIRouter(                           # 定义路由类的实例
    prefix="/child",                          # 路由的路径前缀
    tags=["child"],                           # API文档中显示的名称
    dependencies=[],                          # 给当前路由类实例指定依赖项
    responses={404: {"detail": "未找到项目"}},  # 自定义响应
)

@router.get("/hello")                         # 使用router实例的装饰器定义路由
async def hello(name: str):                   # 定义路径操作函数
    return {"message": f"hello {name}"}

