# 【示例10.2】 第十章 第10.1节 main_test.py
from fastapi.testclient import TestClient
import main
client = TestClient(main.app)              # 创建TestClient实例

def test_index():                     # 定义测试方法
    response = client.get("/")        # 使用TestClient的实例发起请求，接收返回数据
    assert response.status_code == 200                  # 断言： 状态码
    assert response.json() == {"name": "threecoolcat"}  # 断言：返回对象

