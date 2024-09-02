from enum import Enum
from typing import Literal,Union
from typing import Optional
from fastapi import (Body,FastAPI,Query,Path,
                     Cookie,Header,Response,
                     status,Form,File,UploadFile,
                     HTTPException,Request,Depends
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


# 18_classes_as_dependencies


# class Cat:
#     def __init__(self,name):
#         self.name = name
        

# fluffy = Cat('Mr Fluffy')

fake_items_db = [{"item_name" : "Foo"},{"item_name" : "Bar"},{"item_name" : "Baz"}]

class CommonQueryParams:
    def __init__(self,q : str | None = None,skip : int =0,limit : int = 100 ):
        self.q = q
        self.skip = skip
        self.limit = limit
        

@app.get("/items/")
async def read_items(commons = Depends(CommonQueryParams)):
# async def read_items(commons : CommonQueryParams= Depends(CommonQueryParams)):
# async def read_items(commons = Depends()):
    response = {}
    if commons.q:
        response.update({'q' : commons.q})
    items = fake_items_db[commons.skip : commons.skip+commons.limit]
    response.update({'items' : items})
    return response

