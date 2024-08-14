from enum import Enum
from typing import Optional
from fastapi import Body,FastAPI,Query,Path
from pydantic import BaseModel,Field,HttpUrl
from uuid import UUID
from datetime import datetime,time,timedelta

app = FastAPI()


# Extra DataTypes

@app.put('/items/{item_id}')
async def read_items(item_id : UUID,
                     start_date : datetime | None = Body(None),
                     end_date : datetime | None = Body(None),
                     repeat_at : time | None = Body(None),
                     process_after : timedelta | None = Body(None)
                     ):
    start_process = start_date + process_after
    duration = end_date - start_process
    result = {'item_id' : item_id,
              'start_date' : start_date,
              'end_date' : end_date,
              'repeat_at': repeat_at,
              'process_after': process_after,
              'start_process' : start_process,
              'duration' : duration
             }
    return result