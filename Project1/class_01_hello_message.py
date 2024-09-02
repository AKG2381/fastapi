from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def first_api():
    return {"message" : "hello ajeet"}


@app.get('/',description='This is our first rout')
async def root():
    return {'message' : "Hello world"}


@app.post('/')
async def post():
    return {'message' : "Hello from post route"}


@app.put('/')
async def put():
    return {'message' : "Hello from put route"}


@app.get('/users')
async def list_users():
    return {'message' : "list users route"}

# put specific endpoint before dynamic endpoint
@app.get('/users/me')
async def get_current_user():
    return {'message' : "This is the current user"}


@app.get('/users/{user_id}')
async def get_users(user_id : str):
    return {'user_id' : user_id}

# uvicorn main:app --reload
# fastapi dev main.py -- can also be used to run the app

