from fastapi import Depends, FastAPI

from .dependencies import get_token_header, get_query_token

# method1
# from .routers import users, items

# method2 
# from .routers.users import router as user_router
# from .routers.items import router as item_router

# method3
# import routers in init file
from .routers import users_router, items_router



# todo : import routers

app = FastAPI(dependencies=[Depends(get_query_token)])

# app.include_router(users.router)
# app.include_router(items.router)

# app.include_router(user_router)
# app.include_router(item_router)

app.include_router(users_router)
app.include_router(items_router)

@app.get('/')
async def root():
    return {'message' : 'Hello Bigger Applications!'}