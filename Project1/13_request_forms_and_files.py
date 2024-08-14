from enum import Enum
from typing import Literal,Union
from typing import Optional
from fastapi import (Body,FastAPI,Query,Path,
                     Cookie,Header,Response,
                     status,Form,File,UploadFile,
                    )
from fastapi.responses import HTMLResponse

from pydantic import BaseModel,Field,HttpUrl,EmailStr
from uuid import UUID
from datetime import datetime,time,timedelta

app = FastAPI()


# request Files


@app.post('/files/')
async def create_file(files : 
                      list[bytes] = File(...,description="A file read as bytes")):
    if not files:
        return {'message' : 'No file sent'}
    return {'file': [len(file) for file in files]}

@app.post('/uploadfile/')
async def create_upload_file(
            files :list[UploadFile] = File(...,description="A file read as uploadfile")):
    return {'filename': [file.filename for file in files]}


@app.get('/')
async def main():
    conetnt = """
    <body>
        <form action="/files/" method="post" enctype="multipart/form-data">
            <input type="file" name="files" multiple<br>
            <input type="submit">
        </form>
        <form action="/uploadfiles/" method="post" enctype="multipart/form-data">
            <input type="file" name="files" multiple<br>
            <input type="submit">
        </form>
    </body>
    """
    return HTMLResponse(conetnt = conetnt)


@app.post("/filesb/")
async def create_files(
    file : bytes = File(...),
    fileb : UploadFile = File(...),
    token :str = Form(...),
    hello : str = Body(...)):
    return {
        'file_sze' : len(file),
        'token' : token,
        'fileb_content_type' : fileb.content_type,
        'hello' : hello
    }