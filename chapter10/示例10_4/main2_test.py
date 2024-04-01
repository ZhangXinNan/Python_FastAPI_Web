# 【示例10.4】 第十章 第10.1节 main2_test.py
from fastapi.testclient import TestClient
import main2

client = TestClient(main2.app)                     # 创建TestClient实例

async def override_sms_sender(text: str):             # 定义依赖函数，仅输出消息，不发送短信
    print(f'需发送短信内容为：{text}，仅记录，未发送')
    return f'成功发送内容：{text}'
main2.app.dependency_overrides[main2.sms_sender] = override_sms_sender

def test_sendsms():                     # 定义测试方法
    response = client.get("/sendsms?text=验证码")        # 使用TestClient的实例发起请求，接收返回数据
    assert response.status_code == 200                  # 断言： 状态码

