from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
from database import engine, get_db
from enum import Enum
import models, schemas

app=FastAPI()

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(engine)

@app.post('/phone_maker/add', status_code=status.HTTP_201_CREATED, tags=['mobile'])
def add_phone_maker(request:schemas.PhoneModel, db:Session=Depends(get_db)):
    new_data=models.PhoneMaker(phone_maker=request.phone_maker)
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data

@app.get('/phone_maker/show', response_model=List[schemas.PhoneModel], tags=['mobile'])
def get_all(db:Session=Depends(get_db)):
    data=db.query(models.PhoneMaker.phone_maker).all()
    return data

@app.post('/phone_details/add', status_code=status.HTTP_201_CREATED, tags=['mobile'])
def add_phone_details(request:schemas.PhoneMakeAdd, request2:schemas.PhoneModel, db:Session=Depends(get_db)):
    picpath='frontend\public\images\phone_pics\{request.phone_pic}'
    new_data=models.PhoneDetails(
        # Need to change this to a select dropdown
        phone_make=request.phone_make,
        phone_model=request.phone_model,
        phone_price=request.phone_price,
        # wanting to add pic location path
        phone_pic=picpath
    )
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data