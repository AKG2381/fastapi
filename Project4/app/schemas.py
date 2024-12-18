from pydantic import BaseModel
from typing import List, Optional


class UserCreate(BaseModel):
    username : str
    password : str
    email : str

class UserRead(BaseModel):
    id : int
    username : str
    email : str

    class config:
        orm_mode = True

class ItemCreate(BaseModel):
    name : str
    description : str | None = None

class IteamRead(BaseModel):
    id : int
    name : str
    description : str | None= None
    owner_id : int

    class config:
        orm_mode = True


class UserWithItem(UserRead):
    items : List[IteamRead] = []

