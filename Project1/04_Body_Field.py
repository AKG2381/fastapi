from enum import Enum
from typing import Optional
from fastapi import Body,FastAPI,Query,Path
from pydantic import BaseModel,Field

app = FastAPI()


#  Body - Field


class Item(BaseModel):
    name : str
    description : str | None = Field(None,title='the description of the itme',max_length=100)
    price : float = Field(...,gt=0, description='price must be greater than equals to zero')
    tax : float | None = None

@app.put('/items/{item_id}')
async def update_item(
    item_id : int = Path(...,title ='The id of the item to get',ge=0,le=100),
    item :Item  = Body(...,embed=True),
):
    results = {'item_id' : item_id,'item' : item}
    return results