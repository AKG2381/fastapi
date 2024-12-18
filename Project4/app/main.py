from fastapi import FastAPI,APIRouter
from .routes.users import router as user_router
from .routes.items import router as item_router

app = FastAPI()



# Include the routers
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(item_router, prefix="/items", tags=["Items"])

@app.get("/health")
async def health_check():
    return {"status": "ok"}