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

app = FastAPI()


#  path operation configuration
# 15_path_operation_configuration


class Item(BaseModel):
    name : str
    description : str | None = None
    price : float
    tax : float | None = None
    tags : set[str] = set()

class Tags(Enum):
    items = 'items'
    users = 'users'

@app.post('/items/',
          response_model=Item,
          status_code=status.HTTP_201_CREATED,
          tags=[Tags.items],
          summary="Create an item type Item",
        #   description="Create an item with all the information:" 
        #   "name; description; price; tax;and a set of unique tags "
          response_description='The created Item'
          )
async def create_item(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if a item doesn't have tax you can omit this
    - **tags** : a set of unique tag string fon this item
    """
    return item


# we ca add multiple tags
@app.get('/items/',tags=[Tags.items])
async def read_items():
    return [{'name' : "Foo",'price': 42}]

@app.get('/users/',tags=[Tags.users])
async def read_users():
    return [{'username' : "Ajeetkumar"}]


@app.get('/elements/',tags=[Tags.items],deprecated=True)
async def read_elements():
    return [{'item_id' : 'Foo'}]