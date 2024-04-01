# 【示例10.5】第十章 10.1 小节 main_test.py
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sql_app.database import Base
from main import app,get_db
# 第一部分，连接数据库
# 创建数据库引擎，用于测试
engine = create_engine("mysql://root:123456@localhost/cat_test")
# 创建数据库会话，用于测试
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# 创建测试数据库的表结构
Base.metadata.create_all(bind=engine)
# 第二部分，替换依赖项
def get_test_db():                      # 定义依赖函数
    try:
        db = TestingSessionLocal()      # 开启事务
        db.begin(subtransactions=True)
        yield db
    finally:
        db.rollback()                   # 回滚事务
        db.close()
app.dependency_overrides[get_db] = get_test_db
# 第三部分，写测试函数
client = TestClient(app)
def test_create_user():                # 测试函数1
    response = client.post(            # 创建用户
        "/users/",
        json={"email": "cnanyi@qq.com", "password": "123456"},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "cnanyi@qq.com"
    assert "id" in data