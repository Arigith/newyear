from fastapi import FastAPI, HTTPException, status, Depends, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import List
from database import engine, get_db
import models, schemas, jwt_token

app=FastAPI()

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:8000",
    "http://localhost:8000/",
    "http://newyearmeetup.netlify.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(engine)

# Mobile Requests
@app.post('/phone_details/add', status_code=status.HTTP_201_CREATED, tags=['mobile'])
def add_phone_details(request:schemas.PhoneDetails, db:Session=Depends(get_db)):
    new_data=models.PhoneDetails(
        # Need to change this to a select dropdown if I can work this out
        phone_supplier=request.phone_supplier,
        phone_model=request.phone_model,
        phone_price=request.phone_price,
        phone_picture=request.phone_picture,
    )
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data

@app.get('/phone_details/list_all', response_model=list[schemas.PhoneDetails], status_code=status.HTTP_201_CREATED, tags=['mobile'])
def list_all(db:Session=Depends(get_db)):
    mobiledetails=db.query(models.PhoneDetails).all()
    return mobiledetails

# User Requests
@app.post('/user/create', response_model=schemas.ShowUserBase, status_code=status.HTTP_201_CREATED, tags=['user'])
def create_user(request:schemas.CreateUser, db:Session=Depends(get_db)):
    new_user=models.User(
        user_name=request.user_name,
        user_email=request.user_email,
        user_password=schemas.Hash.bcrypt(request.user_password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Authentication Requests
@app.post('/login', tags=['login'])
def user_login(request: OAuth2PasswordRequestForm=Depends(), db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.user_email==request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail='Something went wrong. Please check your details and try again'
        )
    if not schemas.Hash.verify(request.password, user.user_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail='Something went wrong. Please check your details and try again'
        )
        
    access_token_expires=jwt_token.timedelta(minutes=jwt_token.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token=jwt_token.create_access_token(
        data={'sub':user.user_email},
        expires_delta=access_token_expires,
    )
    return {'access_token': access_token, 'token_type':'bearer'}

# Create a worklog
@app.post('/worklog/create', tags=['worklog'])
def create_new_worklog(request:schemas.WorkLogContinue, db:Session=Depends(get_db)):
    new_worklog=models.WorkLog(
        worklog_title=request.worklog_title,
        worklog_info=request.worklog_info,
        # TODO associate user_id to logged in user
        user_id='1',
        )
    db.add(new_worklog)
    db.commit()
    db.refresh(new_worklog)
    return new_worklog

# Get a users worklog
@app.get('/worklog/{id}', response_model=List[schemas.show_worklog], status_code=status.HTTP_200_OK, tags=['worklog'])
def show_user_worklog(id, response:Response, db:Session=Depends(get_db)):
    worklog=db.query(models.WorkLog).filter(models.WorkLog.user_id==id).all()
    if not worklog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Something went wrong. Please check your details and try again')
    return worklog

# Delete a worklog
@app.delete('/worklog/delete/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['worklog'])
def delete_blog(id, db:Session=Depends(get_db)):
    worklog=db.query(models.WorkLog).filter(models.WorkLog.worklog_id==id)
    if not worklog.first():
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail=f'Worklog post with id {id} was not found')
    worklog.delete(synchronize_session=False)
    db.commit()
    return {'detail', 'The blog has been removed as requested'}