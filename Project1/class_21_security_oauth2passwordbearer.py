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
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm


app = FastAPI()

#  21_security_oauth2passwordbearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = 'token')

fake_users_db = {
    "ajeetgupta" : dict(
        username  = 'ajeetgupta',
        full_name = "Ajeet Gupta",
        email = 'ajeetgupta@example.com',
        hashed_password = 'fakehashedsecret',
        disabled = False
    ),
    "alice" : dict(
        username  = 'alice',
        full_name = "Alice Wonderson",
        email = 'alice@example.com',
        hashed_password = 'fakehashedsecret2',
        disabled = True
    )
}


class User(BaseModel):
    username : str 
    email : str | None = None
    full_name : str  | None = None
    disabled : bool | None = None

class UserInDB(User):
    hashed_password : str

def get_user(db, username : str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def fake_decode_token(token):
    return get_user(fake_users_db,token)

def fake_hashed_password(password : str ):
    return f"fakehashed{password}"

async def get_current_user(token : str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={'WWW-Authenticate':"Bearer"}
        )
    return user

async def get_current_active_user(current_user : User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Inactive User'
        )
    return current_user

@app.post('/token')
async def login(form_data : OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException (
            status_code= status.HTTP_400_BAD_REQUEST,
            detail= "Incorrect username or password"
        )
    user = UserInDB(**user_dict)
    hashed_password = fake_hashed_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException (
            status_code= status.HTTP_400_BAD_REQUEST,
            detail= "Incorrect username or password"
        )
    return {'access_token': user.username, 'token_type': 'Bearer'}


@app.get("/users/me")
async def get_me(current_user : User = Depends(get_current_active_user)):
    return current_user


@app.get('/items/')
async def read_items(token : str = Depends(oauth2_scheme)):
    return {'token' : token}




    

