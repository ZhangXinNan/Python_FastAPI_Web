# 【示例7.2】 第七章 第7.2节 main.py
import uvicorn
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError
from sqlalchemy.orm import Session
from auth import schemas, services, database

# 创建安全模式-密码模式
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
# 创建应用实例
app = FastAPI()

# 创建依赖项
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 获取当前用户信息的依赖函数
async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    invalid_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="无效的用户任据",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        username: str = services.extract_token(token)
        if username is None:
            raise invalid_exception
    except JWTError:
        raise invalid_exception
    user = services.get_user(db, username=username)
    if user is None:
        raise invalid_exception
    return user

# 登录的请求接口
@app.post("/login", response_model=schemas.Token)
async def login(
        form: OAuth2PasswordRequestForm = Depends(),   # 依赖项，登录表单
        db: Session = Depends(get_db)                  # 依赖项，数据库会话
):
    user = services.authenticate_user(db, form.username, form.password)   # 验证用户有效性
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码无效",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = services.create_token(data={"username": user.username})  # 发放令牌
    return {"access_token": access_token, "token_type": "bearer"}           # 返回令牌

# 创建新用的接口
@app.post("/user/create/", response_model=schemas.User)                        # 创建用户
async def create_user(user: schemas.UserCreate,
                      db: Session = Depends(get_db)):
    dbuser = services.get_user(db, user.username)
    if dbuser:                                                                 # 判断用户名是否存在
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="用户名已存在",
            # headers={"WWW-Authenticate": "Bearer"},                          # 非Auth2，无需添加
        )
    return services.create_user(db, user)                                      # 在数据库中创建用户

# 获取用户当前信息，安全模式
@app.get("/user/", response_model=schemas.User)
async def read_current_user(current_user: schemas.User = Depends(get_current_user)):
    return current_user
# 获取其他信息， 安全模式
@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"item_id": "cool",}

if __name__ == '__main__':
    # 生成数据库中的表
    database.Base.metadata.create_all(bind=database.engine)
    uvicorn.run(app=app)