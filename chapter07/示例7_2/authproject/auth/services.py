# 【示例7.2】 第七章 第7.2节 services.py
from sqlalchemy.orm import Session
from . import models
from . import schemas
from .utils import get_password_hash, verify_password
from datetime import datetime, timedelta
from jose import jwt

# 获取单个用户
def get_user(db: Session, username: str):
    return db.query(models.UserInDB).filter(models.UserInDB.username == username).first()

# 创建一个用户
def create_user(db: Session, user: schemas.UserCreate):
    # 计算密码的哈希值
    hashed_password = get_password_hash(user.password)
    db_user = models.UserInDB(username=user.username,
                              hashed_password=hashed_password,
                              email=user.email,
                              full_name=user.full_name
                              )
    # 第二步，将实例添加到会话
    db.add(db_user)
    # 第三步，提交会话
    db.commit()
    # 第四步，刷新实例，用于获取数据或者生成数据库中的ID
    db.refresh(db_user)
    return db_user

# 验证用户和密码
def authenticate_user(db, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

# 使用命令获取SECRET_KEY:
# openssl rand -hex 32
# 密钥
SECRET_KEY = "0bb93eb8c00be764e8dc60b001091987bd50c41f18bd2fee1c6d8239f0b23048"
ALGORITHM = "HS256" # 算法
ACCESS_TOKEN_EXPIRE_MINUTES = 5  # 令牌有效期 5分钟

# 创建令牌，将用户名放进令牌
def create_token(data: dict):
    to_encode = data.copy()
    expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    expire = datetime.now() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# 解析令牌，返回用户名
def extract_token(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload.get("username")