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
from fastapi.staticfiles import StaticFiles
from fastapi.encoders import jsonable_encoder
from fastapi.exception_handlers import http_exception_handler,request_validation_exception_handler
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel
from starlette.exceptions import HTTPException as StarletteHTTPException
from datetime import datetime,timedelta
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import jwt,JWTError
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.middleware.cors import CORSMiddleware
import time

app = FastAPI()

fake_secret_token = 'coneofsilence'
fake_db = dict(
    foo=dict(
        id='foo', title='Foo', description="There goes my hero"
    ),
    bar=dict(
        id='bar', title="Bar", description="The bartenders"
    )
)


class Item(BaseModel):
    id: str
    title: str
    description: Optional[str] = None


@app.get('/items/{item_id}')
async def read_main(item_id: str, x_token: str = Header(...)):
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_db[item_id]


@app.post('/items/', response_model=Item)
async def create_item(item: Item, x_token: str = Header(...)):
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    if item.id in fake_db:
        raise HTTPException(status_code=400, detail="Item already exists")
    fake_db[item.id] = item.dict()  # Convert Pydantic model to dict
    return item