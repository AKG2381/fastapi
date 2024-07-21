from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Ajeet%40123@localhost/TodoApplicationDatabase'
# SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:Ajeet%40123@127.0.0.1:3306/todoapplicationdatabase'
SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosappnew.db'  # sqlite database


engine = create_engine(SQLALCHEMY_DATABASE_URL
                       , connect_args={"check_same_thread": False} #this is for sqlite only
                       ) 

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()