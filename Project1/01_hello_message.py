from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def first_api():
    return {"message" : "hello ajeet"}

# uvicorn main:app --reload
# fastapi dev main.py -- can also be used to run the app

