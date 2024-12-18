from sqlalchemy import  create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.settings import settings  # Import settings for DATABASE_URL


DATABASE_URL = 'sqlite:///./sql_app.db'
# my locals setup

# user : postgres
# password : Ajeet%40123
# postgresserver : localhost -- can change whenever we want
# db : sql_app
# SQLALCHEMY_DATABASE_URL = 'postgresql://user:password@postgreserver/db'

# user : root
# password : Ajeet%40123
# server : 127.0.0.1:3306
# db : sql_app
# SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://user:password@mysqlserver/db'

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
