from enum import Enum
from typing import Literal
from typing import Optional
from fastapi import (Body,FastAPI,Query,Path,
                     Cookie,Header,Response,
)

from pydantic import BaseModel,Field,HttpUrl,EmailStr
from uuid import UUID
from datetime import datetime,time,timedelta

app = FastAPI()

# Response Model

class Item(BaseModel):
    name : str 
    description : str | None = None
    price : float 
    tax : float = 10.5
    tags : list[str] = []

items = {
    'foo' :{'name' : 'Foo','price': 50.2},
    'bar' :{'name' : 'Bar','description': 'The Bartenders','price' : 62, 'tax' : 20.2},
    'baz' :{'name' : 'Baz','description': None,'price' : 50.2, 'tax' : 10.5,'tags' : []}
}

@app.post('/items/{item_id}', \
          response_model=Item,
          response_model_exclude_unset=True
          )
async def  redd_item(item_id : Literal['foo','bar','baz'] ):
    return items[item_id]


@app.post('/items', response_model=Item)
async def  create_item(item : Item):
    return item


class UserBase(BaseModel):
    username : str
    email : EmailStr
    full_name : str | None = None

class UserIn(UserBase):
    password : str

class UserOut(UserBase):
    pass



@app.post('/user',response_model=UserOut)
async def create_user(user : UserIn):
    return user


@app.get('/items/{itemid}/name',response_model=Item,response_model_include={'name','description'})
async def read_item_name(itemid : Literal['foo','bar','baz']):
    return items[itemid]


@app.get('/items/{itemid}/public',response_model=Item,response_model_exclude={'tax'})
async def read_item_public_data(itemid : Literal['foo','bar','baz']):
    return items[itemid]
