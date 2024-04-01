# 第十章、10.1节 code7_test.py
import pytest
from httpx import AsyncClient                     # 导入异步测试模块
import main

@pytest.mark.asyncio
async def test_index():                           # 定义测试方法
    async with AsyncClient(app=main.app,               # 创建异步客户端实例
        base_url='http://127.0.0.1:8000') as ac:
        response = await ac.get("/")              # 发起异步请求，接收返回数据
    assert response.status_code == 200                  # 断言： 状态码
    assert response.json() == {"name": "threecoolcat"}  # 断言：返回值

