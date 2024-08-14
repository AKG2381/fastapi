from enum import Enum
from typing import Optional
from fastapi import Body,FastAPI,Query,Path,Cookie,Header,Response
from pydantic import BaseModel,Field,HttpUrl
from uuid import UUID
from datetime import datetime,time,timedelta

app = FastAPI()

# Cookie and Header Parameter


@app.get("/set_cookie/")
async def set_cookie(response: Response):
    response.set_cookie(key="cookie_id", value="your_cookie_value")
    return {"message": "Cookie set"}

@app.put('/items')
async def read_items(cookie_id : str | None = Cookie(None),
                      accept_encoding : str | None = Header(None),
                      sec_ch_ua : str | None = Header(None), 
                      user_agent : str | None = Header(None), 
                      x_token : list[str] | None = Header(None), 

                        ):
    return {"cookie_id":cookie_id,
            "Accept-Encoding": accept_encoding,
            "sec-ch-ua" : sec_ch_ua,
            "User-Agent" : user_agent,
            "X-Token-Values" : x_token,
            }