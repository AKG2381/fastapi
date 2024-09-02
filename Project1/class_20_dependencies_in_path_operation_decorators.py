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

#  20_dependencies_in_path_operation_decorators

async def verify_token(x_token: str = Header(...)):
    if x_token != 'fake-super-secret-token':
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="X-Token header invalid")

async def verify_key(x_key : str  = Header(...)):
    if x_key != 'fake-super-secret-key':
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="X-Key header invalid")
    return x_key
    
@app.get('/items',dependencies=[Depends(verify_token),Depends(verify_key)])
async def  read_items():
    return [{"item" : "Foo"},{"item" : "Bar"}]


@app.get('/users/')
async def read_users():
    return [{'username' : 'Ajeet'},{'username' : 'Ashu'}]



# global_dependencies
"""
app = FastAPI(dependencies=[Depends(verify_token),Depends(verify_key)])
@app.get('/items')
async def  read_items():
    return [{"item" : "Foo"},{"item" : "Bar"}]

@app.get('/users/')
async def read_users():
    return [{'username' : 'Ajeet'},{'username' : 'Ashu'}]
"""