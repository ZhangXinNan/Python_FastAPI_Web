# 【示例7.2】 第七章 第7.2节 utils.py
from passlib.context import CryptContext
_pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# 验证密码
def verify_password(plain_password, hashed_password):
    return _pwd_context.verify(plain_password, hashed_password)
# 生成密码
def get_password_hash(password):
    return _pwd_context.hash(password)

