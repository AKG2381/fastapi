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

# 17_dependencies_intro
async def hello():
      return 'world'

async def common_parameters(q : str | None = None,skip : int =0,limit : int = 100,blah : str = Depends(hello)):
        return {'q': q,'skip': skip,'limit' : limit, 'hello' : blah}             


# @app.get("/items/")
# async def read_items(q : str | None = None,skip : int =0,limit : int = 100):
#     return {'q': q,'skip': skip,'limit' : limit}

# all the parameters of coommon_paramets_will bw available for below tow api's in swagger ui
@app.get("/items/")
async def read_items(commons : dict = Depends(common_parameters)):
     return commons

@app.get("/users/")
async def read_users(commons : dict = Depends(common_parameters)):
      return commons