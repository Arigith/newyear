from typing import List
from pydantic import BaseModel

class PhoneModel(BaseModel):
    phone_maker:str
    
class PhoneMake(BaseModel):
    phone_make:str

class PhoneMakeAdd(PhoneMake):
    phone_model:str
    phone_price:int
    phone_pic:str
    
    class Config():
        orm_mode=True