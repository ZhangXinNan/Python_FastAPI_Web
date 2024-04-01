# 【示例10.3】 第十章 第10.1节 main1_test.py
from fastapi.testclient import TestClient
import main1

@main1.app.on_event("startup")
async def startup_event():
    main1.data["cat"] = "小猫"
    main1.data["dog"] = "小狗"

def test_index():                     # 定义测试方法
    with TestClient(main1.app) as client:  # 创建TestClient实例
        response = client.get("/cat")        # 使用TestClient的实例发起请求，接收返回数据
        assert response.status_code == 200                  # 断言： 状态码
        assert response.json() == {"name": "小猫"}  # 断言：返回对象

