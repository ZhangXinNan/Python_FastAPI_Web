from fastapi.testclient import TestClient
import FromDBShowGoods
client = TestClient(FromDBShowGoods.app)      # 创建TestClient实例

def test_index():                             # 定义测试方法
    response = client.get("/goods")       # 使用TestClient的实例发起请求，接收返回数据
    assert response.status_code == 200          # 断言： 状态码