from sqlalchemy import Column, Integer, String, ForeignKey, Float
from database import Base

class PhoneMaker(Base):
    __tablename__='phonemake'
    id=Column(Integer, primary_key=True, index=True)
    phone_maker=Column(String, unique=True)

class PhoneDetails(Base):
    __tablename__='phonedetail'
    id=Column(Integer, primary_key=True, index=True)
    phone_make=Column(String, ForeignKey('phonemake.id'))
    phone_model=Column(String, unique=True)
    phone_price=Column(Float)
    phone_pic=Column(String)