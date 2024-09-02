from enum import Enum
from typing import Literal,Union
from typing import Optional
from fastapi import (Body,FastAPI,Query,Path,
                     Cookie,Header,Response,
                    )

from pydantic import BaseModel,Field,HttpUrl,EmailStr
from uuid import UUID
from datetime import datetime,time,timedelta

app = FastAPI()

# Extra Models
class UserBase(BaseModel):
    username : str
    email : EmailStr
    full_name : str | None = None

class UserIn(UserBase):
    password : str

class UserOut(UserBase):
    pass

class UserInDB(UserBase):
    hashed_password : str

def fake_password_hasher(raw_password : str):
    return f'supersecret{raw_password}'

def fake_save_user(userin : UserIn):
    hashed_password = fake_password_hasher(userin.password)
    user_in_db = UserInDB(**userin.model_dump(),hashed_password=hashed_password)
    print('UserIn dict',userin.model_dump(''))
    print("User saved")
    return user_in_db


@app.post('/user/', response_model= UserOut)
async def  create_user(userin : UserIn):
    user_saved = fake_save_user(userin)
    return user_saved

class BaseItem(BaseModel):
    desciption : str
    type : str

class CarItem(BaseItem):
    type : str = 'car'

class PlaneItem(BaseItem):
    type : str = 'plane'
    size : int

items = {
    'item1' : {'desciption' : 'All my frinds a low rider','type' : 'car'},
    'item2' : {'desciption' : 'Music is my appreciation','type' : 'plane', 'size' : 5},
}

@app.get('/items/{itemid}',response_model=Union[PlaneItem,CarItem])
async def read_item(itemid : Literal['item1', 'item2']):
    return items[itemid]


class ListItem(BaseModel):
    name : str
    description  : str

list_item = [
    {'name'  : 'Foo','description' : "There comes my hero"},
    {'name'  : 'Red','description' : "Its my aeroplane"},
]


@app.get("/list_items/",response_model=ListItem)
async def read_items():
    return list_item

@app.get('/arbitrary',response_model=dict[str,float])
async def get_arbitrary():
    return {'foo' : 1,'bar' :'12.4'}