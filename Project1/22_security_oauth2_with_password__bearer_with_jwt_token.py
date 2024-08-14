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


app = FastAPI()


#  22_security_oauth2_with_password__bearer_with_jwt_token


# hashing algorithm
SECRET_KEY = "thequickbrownfoxjumpsoverthelazydog"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


fake_users_db = dict (
    ajeetgupta = dict(
        username  = 'ajeetgupta',
        full_name = "Ajeet Gupta",
        email = 'ajeetgupta@example.com',
        hashed_password = '$2b$12$88Lmwkz71ymBafvRWf4XN.4w8JXeFWCi3JmjKf28eguRnIxhucZwy', # password1234
        disabled = False
    ),
    alice = dict(
        username  = 'alice',
        full_name = "Alice Wonderson",
        email = 'alice@example.com',
        hashed_password = '$2b$12$VoLsGGO/Zq6mcbfHkUc24OmYxrnyCzAxBRb91BGyEU9H.yDcQ/NUe' , # password12345
        disabled = True
    )
)

class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    username : str | None = None

class User(BaseModel):
    username : str 
    email : str | None = None
    full_name : str  | None = None
    disabled : bool = False

class UserInDB(User):
    hashed_password : str

pwd_context = CryptContext(schemes=['bcrypt'],deprecated = 'auto')

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = 'token')

def verify_password(plain_password ,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(db, username : str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def authenticate_user(fake_db, username : str,password : str):
    user = get_user(fake_db,username)
    if not user:
        return False
    if not verify_password(password,user.hashed_password):
        return False
    return user

def create_access_token(data : dict ,expires_delta : timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=15)
    to_encode.update({'exp' : expire})
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token : str = Depends(oauth2_scheme)):
    credentials_exceptions = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate user",
            headers={'WWW-Authenticate':"Bearer"}
    )
    try :
        payload = jwt.decode(token, SECRET_KEY, algorithms = [ALGORITHM])
        username = payload.get('sub')
        if username is None:
            raise credentials_exceptions
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exceptions
    user = get_user(fake_users_db,username=token_data.username)
    if not user:
        raise credentials_exceptions
    return user


async def get_current_active_user(current_user : User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Inactive User'
        )
    return current_user

@app.post('/token',response_model=Token)
async def login_for_access_token(form_data : OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db,form_data.username,form_data.password)
    if not user:
        raise HTTPException (
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail= "Incorrect username or password",
             headers={'WWW-Authenticate':"Bearer"}
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data = {'sub' : user.username},expires_delta = access_token_expires
    )
    return {'access_token': access_token, 'token_type': 'bearer'}

@app.get("/users/me")
async def get_me(current_user : User = Depends(get_current_active_user)):
    return current_user

@app.get("/users/me/items")
async def read_own_items(current_user : User = Depends(get_current_active_user)):
    return [{'item_id' : "Foo",'owner' : current_user.username}]