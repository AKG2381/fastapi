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
from datetime import datetime,timedelta
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import jwt,JWTError
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.middleware.cors import CORSMiddleware
import time


description = """
Chimichang API helps you do awsome stuff. 🖋️

## Items

You can **read items**

## Users

You will be able to:
* **create users** (_not implemented_).
* **read users** (_not implemented_).
"""

tags_metadata = [
    dict(name="users", 
    description='Operation with users. the **login** logic is also here.'
    ),
    dict(name="items", 
    description='Manage Items. So _fancy_ they have their own docs',
    externalDocs= dict(
        description='Items external docs',
        url='https://www.ajeet.com',
    )
    ),
]

app = FastAPI(
    title="ChimichangApp",
    description=description,
    version="0.0.1",
    terms_of_service='http://example.com/terms/',
    contact=dict(
        name="deadppolio the Amazing",
        url='http://x-force.example.com/contact',
        email='dp@x-force.example.com'
    ),
    license_info=dict(
        name='Apache 2.0',
        url='https://www.apache.org/licenses/LICENSE-2.0.html'
    ),
    openapi_tags=tags_metadata,
    openapi_url="/api/v1/openapi.json",
    docs_url='/hello-world',
    redoc_url=None
)

@app.get('/users',tags=['users'])
async def get_users():
    return [dict(name="Harry"),dict(name='Ron')]


@app.get('/items/',tags=['items'])
async def read_items():
    return [dict(name='wand'),dict(name='flying broom')]