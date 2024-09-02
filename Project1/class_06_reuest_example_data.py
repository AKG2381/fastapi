from enum import Enum
from typing import Optional
from fastapi import Body,FastAPI,Query,Path
from pydantic import BaseModel,Field,HttpUrl

app = FastAPI()


#  Declare requewst example data

# Method 1
# class Item(BaseModel):
#     name : str
#     description : str | None = None
#     price : float
#     tax : float | None = None
#     class Config:
#         json_schema_extra ={
#             "example" :{
#                 "name" : "foo",
#                 "description" : "nice item",
#                 "price" : 16.25,
#                 "tax" : 1.67
#             }
#         }

# Method 2
# class Item(BaseModel):
#     name : str = Field(..., example="foo")
#     description : str = Field(None, example="nice item")
#     price : float = Field(..., example=16.25)
#     tax : float = Field(None, example=1.67)


# Method 3 using Body()
class Item(BaseModel):
    name : str 
    description : str | None = None
    price : float 
    tax : float | None = None

@app.put("/items/{item_id}")
async def update_items(item_id : int,item : Item = Body(...,example={"name" : "foo","description" : "nice item","price" : 16.25,"tax" : 1.67})):
    result = {"item_id" : item_id,"item" : item}
    return result


@app.put("/item/{item_id}")
async def update_new_item(item_id : int,item : Item = Body(...,
                                                       openapi_examples={
                                                           "normal": {
                                                                    "summary": "A normal example",
                                                                    "description": "A __normal__ item",
                                                                    "value": {
                                                                        "name": "foo",
                                                                        "description": "nice item",
                                                                        "price": 16.25,
                                                                        "tax": 1.67
                                                                    }
                                                                },
                                                           "converted" :{
                                                               "summary" :"A sample with converted data",
                                                               "description" :"Fastapi can convert price `strings` to actual `numbers`",
                                                               "value" :{"name" : "Bar","price" :"16.21" }
                                                           },
                                                           "invalid" :{
                                                               "summary" :"Invalid data is rejected with an Error",
                                                               "description" :"Hello guys",
                                                               "value" :{"name" : "Bar", "price" :"sixteen point two five"}},
                                                       }
                                                       )):
    result = {"item_id" : item_id,"item" : item}
    return result

