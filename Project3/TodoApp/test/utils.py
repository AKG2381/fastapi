from sqlalchemy import create_engine,text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from fastapi.testclient import TestClient
import pytest


from ..database import Base
from ..models import Todos,Users
from ..main import app
from ..routers.auth import bcrypt_context



SQLALCHEMY_DATABASE_URL = 'sqlite:///./todostestdb.db'  # sqlite database


engine = create_engine(SQLALCHEMY_DATABASE_URL
                       , connect_args={"check_same_thread": False} #this is for sqlite only
                       ,poolclass= StaticPool
                       ,
                       ) 

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


def override_get_current_user():
    return {'username' : 'ajeetkumargupta', 'id' : 1, 'user_role' : 'admin'}



client = TestClient(app)


@pytest.fixture
def test_todo():
    todo = Todos(
        title = "Learn to code!",
        description="Need to learn everyday!",
        priority=5,
        complete=False,
        owner_id=1
    )
    db = TestingSessionLocal()
    db.add(todo)
    db.commit()
    yield todo
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM todos;"))
        connection.commit()


@pytest.fixture
def test_user():
    user = Users(
        email = "ajeettest@gmail.com",
        username = 'ajeetkumarguptatest',
        first_name = 'ajeettest',
        last_name = 'guptatest',
        hashed_password = bcrypt_context.hash('testpassword'),
        role = 'admin',
        phone_number = '+91-7440885722'
    )
    db = TestingSessionLocal()
    db.add(user)
    db.commit()
    yield user
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM users;"))
        connection.commit()