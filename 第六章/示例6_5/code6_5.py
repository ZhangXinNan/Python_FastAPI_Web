# 【示例6.5】 第六章 第6.1节 code6_5.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
engine = create_engine(                              # 创建数据库连接引擎
    "sqlite:///./sql_app.db",
    connect_args={"check_same_thread": False}
)
LocalSession = sessionmaker(autocommit=False, bind=engine) # 创建本地会话

Base = declarative_base()   # 定义数据模型基类


class User(Base):            # 定义数据模型，用户
    __tablename__ = 'user'   # 数据库中的表名
    id = Column(Integer, primary_key=True)  # id列，主键
    name = Column('name', String(50))  # 定义字段name，字符串型，对应数据库中的name列
    phone = Column('phone', String(50)) # 定义字段phone，字符串型，对应数据库中的phone列
    bookrecords = relationship('BookRecord', backref='user')  # 图书列表字段

class BookRecord(Base):            # 定义数据模型，图书
    __tablename__ = 'book_record'   # 数据库中的表名
    id = Column(Integer, primary_key=True)  # id列，主键
    book_name = Column('book_name', String(50))   # 书名
    borrow_time = Column('borrow_time', DateTime)   # 借书时间
    user_id = Column(Integer, ForeignKey('user.id'))   # user_id ，外键

Base.metadata.create_all(bind=engine)                 # 在数据库中创建表结构


# 数据库操作 增加
def create(session):
    user = User(name='三酷猫')
    session.add(user)                           # 增加一条数据
    session.flush()                             # 执行插入数据语句
    session.refresh(user)                       # 增加完成后刷新数据的ID字段
    print(f'增加：id={user.id},name={user.name},phone={user.phone}')       # 打印user对象数据
    bookrecords = [BookRecord(book_name='book_'+str(i), user_id=1) for i in range(10)]
    session.bulk_save_objects(bookrecords)      # 批量插入数据
    session.commit()                            # 提交事务，将数据保存到数据库


# 数据为串的操作 检索
def retrieve(session):
    queryuser = session.query(User)                 # 创建query对象
    print('获取：记录条数:',queryuser.count())              # 打印记录数量
    first = queryuser.get(1)                        # 根据主键获取第一条记录
    print('获取：第一条记录的name字段值:',first.name)        # 打印第一条记录的name字段值
    querybook = session.query(BookRecord)           # 创建query对象
    all = querybook.all()                           # 获取全部记录
    print('获取：全部图书记录的name字段值:',[book.book_name for book in all])   # 全部记录的name值
    books = querybook.filter(BookRecord.id > 5).all()            # 获取ID大于的图书记录
    print('获取：ID大于5的图书记录:', [book.book_name for book in books])

def update(session):
    query = session.query(User)
    query.filter(User.name == '三酷猫').update({User.phone:'18600000000'})
    session.commit()
    user = query.filter(User.name == '三酷猫').first()
    print(f'更新后：id={user.id},name={user.name},phone={user.phone}')  # 打印user对象数据

def delete(session):
    query = session.query(BookRecord)                 # 创建query对象
    query.filter(BookRecord.id > 5).delete()          # 查询图书ID大于5的数据后删除数据
    session.commit()                                  # 提交事务
    all = query.all()  # 获取全部记录
    print('删除后：全部图书记录的name字段值:', [book.book_name for book in all])  # 全部记录的name值

if __name__ == '__main__':
    session = LocalSession()   # 创建会话实例
    create(session)
    retrieve(session)
    update(session)
    delete(session)

