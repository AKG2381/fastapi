from enum import Enum
from typing import Optional
from fastapi import Body,FastAPI,Query,Path
from pydantic import BaseModel

app = FastAPI()


#  Body multiple paramters


class Item(BaseModel):
    name : str
    description : str | None = None
    price : float
    tax : float | None = None

class User(BaseModel):
    username : str | None = None
    full_name : str | None = None

class Importance(BaseModel):
    importance : int


@app.put('/items/{item_id}')
async def update_item(
    *,
    item_id : int = Path(...,title ='The id of the item to get',ge=0,le=100),
    q: str | None = None,
    item :Item | None = None,
    user : User,
    # importance : Importance
    # reuest body --->
    # {
    #   "importance": {
    #     "importance": 0
    #   }
    # }
    importance : int = Body(...)
    # {
    #   "importance": 0
    # }
):
    results = {'item_id' : item_id}
    if q:
        results.update({'q' : q})
    if item:
        results.update({'item' : item})
    if user:
        results.update({'user' : user})
    if importance:
        results.update({'importance' : importance})
    return results


@app.get('/items/{item_id}')
async def get_item(
    item_id : int = Path(...,title ='The id of the item to get',ge=0,le=100),
    item :Item = Body(...,embed=True)):
    results = {'item_id' : item_id}
    if item:
        results.update({'item' : item})
    return results
# example schema :
#1.  item :Item | None = None
# or item :Item = Body(...)
'''{
  "name": "string",
  "description": "string",
  "price": 0,
  "tax": 0
}'''

#2. item :Item = Body(...,embed=True)
'''{
  "item": {
    "name": "string",
    "description": "string",
    "price": 0,
    "tax": 0
  }
}'''
