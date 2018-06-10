from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#创建对象的基类
Base=declarative_base()

#初始化数据库的链接
engine=create_engine("mysql+mysqldb://root:love512105@localhost/spider?charset=utf8")

#创建一个会话对象
def create_session():
    Session=sessionmaker(bind=engine)
    session=Session()
    return session