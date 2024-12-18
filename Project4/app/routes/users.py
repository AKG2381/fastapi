from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session


from app.schemas import UserCreate,UserRead,UserWithItem,IteamRead,ItemCreate
from app.services.user_services import create_user, get_user, delete_user
from ..database import get_db

router = APIRouter()



@router.post('/users',response_model=UserRead)
async def register_user(user : UserCreate, db : Session = Depends(get_db)):
    db_user = create_user(db=db, user=user)
    if db_user:
        return db_user
    raise HTTPException(status_code=400, detail="User Already Exists")


@router.get("/users/{userid}", response_model=UserRead)
async def get_user_details(userid : int , db : Session = Depends(get_db)):
    db_user = get_user(db=db, user_id= userid)
    if db_user:
        return db_user
    raise HTTPException(status_code=404, detail="User Not Found")

@router.delete("/users/{userid}", response_model=UserRead)
async def delete_user_details(userid : int , db : Session = Depends(get_db)):
    db_user = delete_user(db=db, user_id= userid)
    if db_user:
        return db_user
    raise HTTPException(status_code=404, detail="User Not Found")