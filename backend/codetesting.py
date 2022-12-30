from typing import List
from enum import Enum
from fastapi import FastAPI, Form, Depends, status, HTTPException
from sqlalchemy.orm import Session, session
from database import get_db
import models, schemas

testapp=FastAPI()
# I am trying to make a select dropdown using Culumn models.PhoneMaker.phone_maker as the data

# making a fixed dataset first
DynamicEnum = Enum('DynamicEnum', names={'item1':'Apple', 'item2': 'Samsung', 'item3': 'Huawei', 'item4': 'OnePlus'})

# Making a basic post request to see if it works
@testapp.post("/select")
async def select_item(item: DynamicEnum = Form(...)):
    return item

# Attempt to get data from needed column
# first I made a query to get all data

'''def get_all(db:Session=Depends(get_db)):
    data=db.query(models.PhoneMaker.phone_maker).all()
    return data'''

# Then I tried using this in the same way as line 11

'''phone_data=Enum('phone_data', names=List(get_all()))'''

# got error 
'''
Process SpawnProcess-3:
Traceback (most recent call last):
  File "C:\Users\tumbl\AppData\Local\Programs\Python\Python311\Lib\multiprocessing\process.py", line 314, in _bootstrap     
    self.run()
  File "C:\Users\tumbl\AppData\Local\Programs\Python\Python311\Lib\multiprocessing\process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "C:\Users\tumbl\AppData\Local\Programs\Python\Python311\Lib\site-packages\uvicorn\_subprocess.py", line 76, in subprocess_started
    target(sockets=sockets)
  File "C:\Users\tumbl\AppData\Local\Programs\Python\Python311\Lib\site-packages\uvicorn\server.py", line 60, in run        
    return asyncio.run(self.serve(sockets=sockets))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\tumbl\AppData\Local\Programs\Python\Python311\Lib\asyncio\runners.py", line 190, in run
    return runner.run(main)
           ^^^^^^^^^^^^^^^^
  File "C:\Users\tumbl\AppData\Local\Programs\Python\Python311\Lib\asyncio\runners.py", line 118, in run
    return self._loop.run_until_complete(task)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\tumbl\AppData\Local\Programs\Python\Python311\Lib\asyncio\base_events.py", line 650, in run_until_complete 
    return future.result()
           ^^^^^^^^^^^^^^^
  File "C:\Users\tumbl\AppData\Local\Programs\Python\Python311\Lib\site-packages\uvicorn\server.py", line 67, in serve      
    config.load()
  File "C:\Users\tumbl\AppData\Local\Programs\Python\Python311\Lib\site-packages\uvicorn\config.py", line 474, in load      
    self.loaded_app = import_from_string(self.app)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\tumbl\AppData\Local\Programs\Python\Python311\Lib\site-packages\uvicorn\importer.py", line 21, in import_from_string
    module = importlib.import_module(module_str)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\tumbl\AppData\Local\Programs\Python\Python311\Lib\importlib\__init__.py", line 126, in import_module       
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1206, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1178, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1149, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 940, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "D:\VScode\projects\newyearpresentation\backend\codetesting.py", line 26, in <module>
    phone_data=Enum('phone_data', names=List(get_all()))      
                                             ^^^^^^^^^        
  File "D:\VScode\projects\newyearpresentation\backend\codetesting.py", line 22, in get_all
    data=db.query(models.PhoneMaker.phone_maker).all()        
         ^^^^^^^^
AttributeError: 'Depends' object has no attribute 'query'
'''

# Asked chatGPT and was advised
'''
You will need to retrieve the list of phone makers from the other table and use it to populate the enum field of the PhoneMakeAdd schema.
To do this, you will need to perform a database query to retrieve the list of phone makers from the other table. You can then use this list to set the enum field of the PhoneMakeAdd schema.

For example:
# Retrieve the list of phone makers from the other table
phone_makers = db.query(OtherTable.phone_maker).all()

Set the enum field of the PhoneMakeAdd schema using the retrieved list of phone makers
class PhoneMakeAdd(BaseModel):
    phone_make: str = Field(..., enum=phone_makers)
    phone_model: str = Field(...)
    phone_price: float = Field(...)
    phone_pic: str = Field(...)

Finally, you will need to modify the add_phone_details function to use the modified PhoneMakeAdd schema.

For example:

@app.post('/phone_details/add', status_code=status.HTTP_201_CREATED, tags=['mobile'])
def add_phone_details(request: schemas.PhoneMakeAdd, db: Session = Depends(get_db)):
    new_data = models.PhoneDetails(
        phone_make=request.phone_make,
        phone_model=request.phone_model,
        phone_price=request.phone_price,
        phone_pic=request.phone_pic
    )
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data

This should allow you to create a select option for the phone_make field that gets its data from the other table's phone_maker column.
'''

# created query
phone_makers = Session.query(models.PhoneMaker.phone_maker).all()

# Added schema to schemas.py
# Last code was writen almost the same way as I originally wrote it so used that

@testapp.post('/phone_details/add', status_code=status.HTTP_201_CREATED, tags=['mobile'])
def add_phone_details(request: schemas.PhoneMakeAdd, db: Session = Depends(get_db)):
    new_data = models.PhoneDetails(
        phone_make=request.phone_make,
        phone_model=request.phone_model,
        phone_price=request.phone_price,
        phone_pic=request.phone_pic
    )
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data

# receieved error
'''
Traceback (most recent call last):
  File "C:\Users\tumbl\AppData\Local\Programs\Python\Python311\Lib\site-packages\sqlalchemy\sql\elements.py", line 854, in __getattr__
    return getattr(self.comparator, key)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'Comparator' object has no attribute '_query_cls'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\tumbl\AppData\Local\Programs\Python\Python311\Lib\site-packages\sqlalchemy\orm\attributes.py", line 327, in __getattr__
    return getattr(self.comparator, key)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\tumbl\AppData\Local\Programs\Python\Python311\Lib\site-packages\sqlalchemy\util\langhelpers.py", line 1244, in __getattr__
    return self._fallback_getattr(key)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\tumbl\AppData\Local\Programs\Python\Python311\Lib\site-packages\sqlalchemy\orm\properties.py", line 420, in _fallback_getattr
    return getattr(self.__clause_element__(), key)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\tumbl\AppData\Local\Programs\Python\Python311\Lib\site-packages\sqlalchemy\sql\elements.py", line 856, in __getattr__
    util.raise_(
  File "C:\Users\tumbl\AppData\Local\Programs\Python\Python311\Lib\site-packages\sqlalchemy\util\compat.py", line 208, in raise_
    raise exception
AttributeError: Neither 'AnnotatedColumn' object nor 'Comparator' object has an attribute '_query_cls'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\tumbl\AppData\Local\Programs\Python\Python311\Lib\multiprocessing\process.py", line 314, in _bootstrap     
    self.run()
  File "C:\Users\tumbl\AppData\Local\Programs\Python\Python311\Lib\multiprocessing\process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "C:\Users\tumbl\AppData\Local\Programs\Python\Python311\Lib\site-packages\uvicorn\_subprocess.py", line 76, in subprocess_started
    target(sockets=sockets)
  File "C:\Users\tumbl\AppData\Local\Programs\Python\Python311\Lib\site-packages\uvicorn\server.py", line 60, in run        
    return asyncio.run(self.serve(sockets=sockets))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\tumbl\AppData\Local\Programs\Python\Python311\Lib\asyncio\runners.py", line 190, in run
    return runner.run(main)
           ^^^^^^^^^^^^^^^^
  File "C:\Users\tumbl\AppData\Local\Programs\Python\Python311\Lib\asyncio\runners.py", line 118, in run
    return self._loop.run_until_complete(task)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\tumbl\AppData\Local\Programs\Python\Python311\Lib\asyncio\base_events.py", line 650, in run_until_complete 
    return future.result()
           ^^^^^^^^^^^^^^^
  File "C:\Users\tumbl\AppData\Local\Programs\Python\Python311\Lib\site-packages\uvicorn\server.py", line 67, in serve      
    config.load()
  File "C:\Users\tumbl\AppData\Local\Programs\Python\Python311\Lib\site-packages\uvicorn\config.py", line 474, in load      
    self.loaded_app = import_from_string(self.app)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\tumbl\AppData\Local\Programs\Python\Python311\Lib\site-packages\uvicorn\importer.py", line 21, in import_from_string
    module = importlib.import_module(module_str)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\tumbl\AppData\Local\Programs\Python\Python311\Lib\importlib\__init__.py", line 126, in import_module       
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1206, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1178, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1149, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 940, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "D:\VScode\projects\newyearpresentation\backend\codetesting.py", line 113, in <module>
    phone_makers = Session.query(models.PhoneMaker.phone_maker).all()
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\tumbl\AppData\Local\Programs\Python\Python311\Lib\site-packages\sqlalchemy\orm\session.py", line 2161, in query
    return self._query_cls(entities, self, **kwargs)
           ^^^^^^^^^^^^^^^
  File "C:\Users\tumbl\AppData\Local\Programs\Python\Python311\Lib\site-packages\sqlalchemy\orm\attributes.py", line 329, in __getattr__
    util.raise_(
  File "C:\Users\tumbl\AppData\Local\Programs\Python\Python311\Lib\site-packages\sqlalchemy\util\compat.py", line 208, in raise_
AttributeError: Neither 'InstrumentedAttribute' object nor 'Comparator' object associated with PhoneMaker.phone_maker has an attribute '_query_cls'
'''

# google search did this suggested doing
phone_makers = session.query(models.PhoneDetails).join(models.PhoneMaker).filter(models.PhoneMaker.phone_maker=='')

# asking for assistance from Kris
import main
def get_active_user(current_user: schemas.ShowUserBase=Depends(main.user_login)):
  if current_user.disabled:
    raise HTTPException(status=status.HTTP_401_UNAUTHORIZED, detail='Inactive USer')
  return current_user

