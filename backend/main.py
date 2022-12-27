from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
from database import engine, get_db
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

@app.post('/phone_details/add', status_code=status.HTTP_201_CREATED, tags=['mobile'])
def add_phone_details(request:schemas.PhoneDetails, db:Session=Depends(get_db)):
    new_data=models.PhoneDetails(
        # Need to change this to a select dropdown if I can work this out
        phone_supplier=request.phone_supplier,
        phone_model=request.phone_model,
        phone_price=request.phone_price,
        # wanting to add pic location path
        phone_picture=request.phone_picture
    )
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data

@app.get('/phone_details/list_all', response_model=list[schemas.PhoneDetails], status_code=status.HTTP_201_CREATED, tags=['mobile'])
def list_all(db:Session=Depends(get_db)):
    mobiledetails=db.query(models.PhoneDetails).all()
    return mobiledetails