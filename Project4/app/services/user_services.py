from sqlalchemy.orm import Session


from app.models import User,Item
from app.schemas import UserCreate,UserRead
from app.utils.hash import hash_password, verify_password


def create_user(db : Session, user : UserCreate):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        return None
    hashed_password = hash_password(user.password)
    db_user = User(username = user.username, email = user.email, password_hash=hashed_password)

    db.add(db_user)
    db.commit()
    db.refresh()

    return db_user

def get_user(db: Session, user_id : int):
    db_user = db.query(User).filter(User.id==user_id).first()
    return db_user

def delete_user(db : Session, user_id : int):
    db_user = db.query(User).filter(User.id==user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return db_user
    return None

