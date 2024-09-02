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

# Handling errors

# 15_handling_errors

items = {'foo': "The foo wrestlers"}

@app.get('/items/{item_id}')
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Item not found',
                            headers={"X-Error" : "there goes my error"})
    return {'item' : items[item_id]}


class UnicornException(Exception):
    def __init__(self, name,*args: object) -> None:
        super().__init__(*args)
        self.name = name

@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request : Request, exc : UnicornException):
    return JSONResponse(status_code=418,
                        content={'message' : f"oops! {exc.name} did something. There goes a rainbow"})

@app.get("/unicorn/{name}")
async def read_unicorn(name : str):
    if name == 'yolo':
        raise UnicornException(name=name)
    return {'unicorn_name' : name}


# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request,  exc):
#     return PlainTextResponse(str(exc),status_code=400)
# # [{'type': 'int_parsing', 'loc': ('path', 'item_id'), 'msg': 'Input should be a valid integer, unable to parse string as an integer', 'input': 'foo'}]

# @app.exception_handler(StarletteHTTPException)
# async def http_handler_exception_handler(request,exc):
#     return PlainTextResponse(str(exc.detail),status_code=exc.status_code)

# @app.get('/validation_items/{item_id}')
# async def read_validation_items(item_id : int):
#     if item_id == 3:
#         raise HTTPException(status_code=418,
#                             detail="Nope! I don't like 3."
#                             )
#     return {'item_id' : item_id}








# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request: Request,  exc: RequestValidationError):
#     return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
#                         content=jsonable_encoder({'detail':exc.errors(),'body': exc.body }))


# class Item(BaseModel):
#     title : str
#     size : int


# @app.post('/items/')
# async def create_item(item : Item):
#     return item




@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request,  exc):
    print(f"OMG! an HTTP error")
    return await http_exception_handler(request,exc)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request,  exc : RequestValidationError):
    print(f"OMG! The client send invlaid data : {exc}")
    return await request_validation_exception_handler(request,exc)



@app.get("/blah_items/{item_id}")
async def read_items(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=418,
                        detail="Nope! I don't like 3."
                        )
    return {'item_id' : item_id}