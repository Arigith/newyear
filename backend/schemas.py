from datetime import date
from pydantic import BaseModel
from passlib.context import CryptContext

pwd_ctxt=CryptContext(schemes=['bcrypt'],deprecated='auto')

class Hash():
    def bcrypt(password:str):
        return pwd_ctxt.hash(password)
    
    def verify(plain_password, hashed_password):
        return pwd_ctxt.verify(plain_password, hashed_password)

class PhoneMake(BaseModel):
    phone_supplier:str
    phone_model:str
    phone_price:int
    phone_picture:str

class PhoneDetails(PhoneMake):
    class Config():
        orm_mode=True

class CreateWorkLog(BaseModel):
    worklog_title: str
    date_created: date
    worklog_info: str

class WorkLogContinue(CreateWorkLog):
    class Config():
        orm_mode=True

class CreateUser(BaseModel):
    user_name:str
    user_email:str
    user_password:str

class ShowUserBase(BaseModel):
    user_name:str
    user_email:str
    class Config():
        orm_mode=True

    
# class ShowUserWorklogs(BaseModel):
#     name:str
#     email:str
#     Worklog:List[Worklog] = []
#     class Config():
#         orm_mode=True

class Login(BaseModel):
    username:str
    password:str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None