from sqlalchemy import Column,String,Integer,TEXT
from job.models import Base

#数据表
class JobMsg(Base):
    __tablename__='jobmsg'
    id = Column(Integer, primary_key=True)
    jobname = Column(TEXT)
    jobsalary = Column(TEXT)
    jobplace = Column(TEXT)
    comparyname = Column(TEXT)
    comparyattr = Column(TEXT)
    jobtag = Column(TEXT)
    jobweal = Column(TEXT)
    jobrequired = Column(TEXT)
    def __init__(self,**items):
        for key in items:
            if items[key]==None:
                items[key]='none'
            if hasattr(self,key):
                setattr(self,key,items[key])
