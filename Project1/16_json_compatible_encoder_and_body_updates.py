from enum import Enum
from typing import Literal,Union
from typing import Optional
from fastapi import (Body,FastAPI,Query,Path,
                     Cookie,Header,Response,
                     status,Form,File,UploadFile,
                     HTTPException,Request,
                    )
from fastapi.responses import (
                HTMLResponse,
                JSONResponse,
                PlainTextResponse)
from fastapi.encoders import jsonable_encoder
from fastapi.exception_handlers import http_exception_handler,request_validation_exception_handler
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel
from starlette.exceptions import HTTPException as StarletteHTTPException
from datetime import datetime

app = FastAPI()

#  JSON Compatible encoder and body updates

# 16_json_compatible_encoder_and_body_updates


# fake_db = {}

# class Item(BaseModel):
#     title : str
#     timestamp : datetime
#     description : str | None = None


# @app.put('/items/{id}')
# async def update_item(id : str,item : Item):
#     json_compatible_item_data = jsonable_encoder(item)
#     fake_db[id] = json_compatible_item_data
#     print(fake_db)
#     return "Success"


class Item(BaseModel):
    name : str
    description : str | None = None
    price : float
    tax : float | None = None
    tags : list[str] = set()

items = {
    'foo' :{'name' : 'Foo','price': 50.2},
    'bar' :{'name' : 'Bar','description': 'The bartenders','price' : 62, 'tax' : 20.2},
    'baz' :{'name' : 'Baz',
            'description': None,
            'price' : 50.2, 
            'tax' : 10.5,
            'tags' : []}
}


@app.get('/items/{item_id}',response_model=Item)
async def read_item(item_id : str):
    return items.get(item_id)


@app.put('/items/{item_id}')
async def update_item(item_id : str,item : Item):
    updated_item_encoded = jsonable_encoder(item)
    items[item_id] = updated_item_encoded
    return updated_item_encoded


@app.patch('/item/{item_id}',response_model=Item)
async def patch_item(item_id : str,item : Item):
     stored_item_data = items.get(item_id)
     if stored_item_data is not None:
         stored_item_model = Item(**stored_item_data)
     else:
         stored_item_model = Item()
    #  update_data = item.dict()
     update_data = item.dict(exclude_unset=True)

     updated_item = stored_item_model.copy(update=update_data)
     items[item_id] = jsonable_encoder(updated_item)
     print(items)
     return updated_item