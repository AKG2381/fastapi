from enum import Enum
from typing import Literal,Union
from typing import Optional
from fastapi import (Body,FastAPI,Query,Path,
                     Cookie,Header,Response,
                     status
                    )

from pydantic import BaseModel,Field,HttpUrl,EmailStr
from uuid import UUID
from datetime import datetime,time,timedelta

app = FastAPI()

# Response Status


@app.post('/items',status_code=status.HTTP_201_CREATED)
async def create_item(name : str):
    return {'name' : name}

@app.delete('/items/{pk}',status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(pk : str):
    print({'pk': pk})
    return

@app.get('/items/',status_code=status.HTTP_301_MOVED_PERMANENTLY)
async def read_items_redirect():
    return {'hello' : 'world'}