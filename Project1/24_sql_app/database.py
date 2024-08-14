from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm     import sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///./sql_app.db'
# my locals setup
# user : postgres
# password : Ajeet%40123
# postgresserver : localhost -- can change whaever we want
# db : sql_app
# SQLALCHEMY_DATABASE_URL = 'postgresql://user:password@postgreserver/db'

# user : root
# password : Ajeet%40123
# server : 127.0.0.1:3306
# db : sql_app
# SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://user:password@mysqlserver/db'

engine = create_engine(SQLALCHEMY_DATABASE_URL,
                       connect_args={'check_same_thread': False} # for sqliteonly
                       )

SessionLocal = sessionmaker(autocommit = False,autoflush=False,bind = engine)

Base = declarative_base()