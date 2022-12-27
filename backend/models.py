from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from enum import Enum
from database import Base
from datetime import date

class PhoneMakers(Enum):
    ALCATEL='ALCATEL'
    CAT='CAT'
    Huawei='Huawei'
    iPhone='iPhone'
    Nokia='Nokia'
    OPPO='OPPO'
    Samsung='Samsung'

class PhoneDetails(Base):
    __tablename__='phonedetail'
    phone_id=Column(Integer, primary_key=True, index=True)
    phone_supplier=Column(String)
    phone_model=Column(String, unique=True)
    phone_price=Column(Float, comment='What is the buy now price')
    phone_picture=Column(String)

class User(Base):
    __tablename__='Userdetails'
    user_id=Column(Integer, primary_key=True, index=True)
    user_name=Column(String)
    user_email=Column(String, unique=True, index=True)
    user_password=Column(String)
    user_date_created=Column(Date, default=date.today())
    worklogs=relationship('WorkLog', back_populates='creator')

class WorkLog(Base):
    __tablename__='Worklogdetails'
    worklog_id=Column(Integer, primary_key=True, index=True)
    worklog_title=Column(String)
    worklog_date_created=Column(Date, default=date.today())
    worklog_info=Column(String)
    user_id=Column(Integer, ForeignKey('Userdetails.user_id'))
    creator=relationship('User', back_populates='worklogs')