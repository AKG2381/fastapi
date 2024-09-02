from enum import Enum
from typing import Literal,Union
from typing import Optional
from fastapi import (Body,FastAPI,Query,Path,
                     Cookie,Header,Response,
                     status,Form
                    )

from pydantic import BaseModel,Field,HttpUrl,EmailStr
from uuid import UUID
from datetime import datetime,time,timedelta

app = FastAPI()

# Form : Fields
# data = payload


# body 
#  json = payload

@app.post('/login/')
async def login(username : str = Form(...),
                password : str = Form(...)):
    print("password :",password)
    return {'username': username}


class User(BaseModel):
    username : str
    password : str

@app.post('/login-json')
async def login_json(username : str = Body(...),
                password : str = Body(...)):
# async def login_json(user : User):
    print("password :",password)
    return {'username': username}
    

class User(BaseModel):
    username : str
    password : str

@app.post('/login-json')
async def login_json(user : User):
    print("password :",user.password)
    return {'username': user.username}