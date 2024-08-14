from enum import Enum
from typing import Optional
from fastapi import Body,FastAPI,Query,Path
from pydantic import BaseModel,Field,HttpUrl

app = FastAPI()


#  Body - Nested Models

class Image(BaseModel):
    # url : str = Field(...,pattern="^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)$")
    url : HttpUrl
    name : str


class Item(BaseModel):
    name : str
    description : str | None = None
    price : float
    tax : float | None = None
    tags : list[str] = []
    # tags : set[str] = set()
    image : Image | None = None
    # image : list[Image] | None = None #list 0f images

class Offer(BaseModel):
    name : str
    description : str | None = None
    price : float
    items : list[Item]

@app.put('/items/{item_id}')
async def  update_item(item_id : int,item : Item):
    results = {'item_id' : item_id,'item' : item}
    return results

@app.post("/offers")
async def  create_offer(offer : Offer = Body(...,embed=True)):
    return offer

@app.post("/images/multiple")
async def create_mulitple_images(images : list[Image]):
    return images

@app.post('/blah')
async def create_some_blahs(blahs : dict[int,float]):
    return blahs