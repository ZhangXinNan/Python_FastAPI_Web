# 【示例6.5】第六章 6.2 小节 main.py
import sys
print (sys.path)
from typing import List
import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
# 导入本程序的模块
from sql_app import crud, models, schemas
from sql_app.database import SessionLocal, engine
# 生成数据库中的表
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# 创建依赖项
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 定义路径操作函数，并注册路由路径 创建用户
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

# 定义路径操作函数，并注册路由路径 获取用户列表
@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

# 定义路径操作函数，并注册路由路径 获取用户信息
@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# 定义路径操作函数，并注册路由路径 创建用户相关的项目
@app.post("/users/{user_id}/books/", response_model=schemas.Book)
def create_book_for_user(
    user_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)
):
    return crud.create_user_book(db=db, book=book, user_id=user_id)

# 定义路径操作函数，并注册路由路径 获取项目列表
@app.get("/books/", response_model=List[schemas.Book])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = crud.get_books(db, skip=skip, limit=limit)
    return books

if __name__ == '__main__':
    uvicorn.run(app=app)