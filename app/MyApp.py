from sqlalchemy import Column,Integer,String,TIMESTAMP,ForeignKey,Boolean
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class IFrame(Base):
    __tablename__='tb_iframe_details'
    id=Column(Integer,primary_key=True)
    iframeID=Column(Integer,nullable=False)
    iframeURL=Column(String(),nullable=False)

class UserMaster(Base):
    __tablename__='tb_user_master'
    id=Column(Integer,primary_key=True)
    loginID=Column(Integer,nullable=False)
    emailID=Column(String(),nullable=False)
    password=Column(String(),nullable=False)
    created_dt=Column(TIMESTAMP,nullable=False)

class UserToken(Base):
    __tablename__='tb_user_token'
    id=Column(Integer,primary_key=True)
    loginID=Column(Integer,ForeignKey('tb_user_master.id'))#has to be foreign key
    userToken=Column(String(),nullable=False)
    expiryTimeStamp=Column(TIMESTAMP,nullable=False)
    createdTimeStamp=Column(TIMESTAMP,nullable=False)

class UserLoginAudit(Base):
    __tablename__='tb_user_login_audit'
    id=Column(Integer,primary_key=True)
    loginID=Column(Integer,ForeignKey('tb_user_master.id'))#foreign key
    attemptedTimeStamp=Column(TIMESTAMP,nullable=False)
    statusFlag=Column(Boolean(),nullable=False)
