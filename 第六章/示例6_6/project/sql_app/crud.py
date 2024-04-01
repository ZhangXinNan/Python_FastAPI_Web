# 【示例6.6】第六章 6.2 小节 crud.py
# 第一步，导入会话组件
from sqlalchemy.orm import Session
# 第二步，导入前两步定义的models和schemas模块
from . import models, schemas

# 第三步，读取数据的函数
# 读取单个用户
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

# 通过email读取单个用户
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# 读取带分页的用户列表
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

# 读取图书列表
def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Book).offset(skip).limit(limit).all()

# 第四步，创建数据的函数
# 创建一个用户
def create_user(db: Session, user: schemas.UserCreate):
    # 模拟生成密码的过程，并没有真正生成加密值
    fake_hashed_password = user.password + "notreallyhashed"
    # 第一步，根据数据创建数据库模型的实例
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    # 第二步，将实例添加到会话
    db.add(db_user)
    # 第三步，提交会话
    db.commit()
    # 第四步，刷新实例，用于获取数据或者生成数据库中的ID
    db.refresh(db_user)
    return db_user

# 创建用户相关的一本图书
def create_user_book(db: Session, book: schemas.BookCreate, user_id: int):
    db_row = models.Book(**book.dict(), owner_id=user_id)
    db.add(db_row)
    db.commit()
    db.refresh(db_row)
    return db_row

# 更新图书的标题
def update_book_title(db: Session, book: schemas.Book):
    db.query(models.Book).filter(models.Book.id==book.id).update({"title": book.title})
    db.commit()
    return 1

# 删除图书
def delete_book(db: Session, book: schemas.Book):
    res = db.query(models.Book).filter(models.Book.id==book.id).delete()
    print(res)
    db.commit()
    return 1