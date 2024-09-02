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


# 19_sub_dependencies

def query_extractor(q : str | None = None):
    return q

def query_or_body_etractor(q : str = Depends(query_extractor),last_query : str | None = Body(None)):
    if not q:
        return last_query
    return q

@app.post('/items/')
async def try_query(query_or_body : str = Depends(query_or_body_etractor)):
     return {'q_or_body' : query_or_body}