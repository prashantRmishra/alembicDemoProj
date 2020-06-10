from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class IFrame(Base):
    __tablename__='tb_iframe_details'
    id=Column(Integer,primary_key=True)
    iframeID=Column(Integer)
    iframeURL=Column(String(100))