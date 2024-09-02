from pydantic import BaseModel




"""
    class Config:
        orm_mode = True
if orm_mode is false: 
    - and you want to fetch particular user items ==> users.items (rlatioship with Item Model)
    - it won't hit the database until we acess the `items` ==> users.items
    
on the other side
if orm mode is true:
    - it will fetch items as well 

"""

class ItemBase(BaseModel):
    title : str
    description : str | None = None

class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id : int
    owner_id : int
    class Config:
        orm_mode = True



class UserBase(BaseModel):
    email : str

class UserCreate(UserBase):
    password : str

class User(UserBase):
    id : int
    is_active  : bool 
    items : list[Item] = []
    class Config:
        orm_mode = True

    