from fastapi import APIRouter

router = APIRouter()

@router.get('/users/',tags=['users'])
async def read_users():
    return [{'username' : 'Rick'},{'username' : 'Modi'}]

@router.get('/users/me/',tags=['users'])
async def read_user_me():
    return {'username' : 'currentuser'}

@router.get('/users/{username}/',tags=['users'])
async def read_user_me(username : str):
    return {'username' : username}