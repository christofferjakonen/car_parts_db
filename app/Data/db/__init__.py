import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .db_settings import *
from pymongo import MongoClient

engine = sqlalchemy.create_engine(f'mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}')
Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

client = MongoClient(f'mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}')
mdb = client.model_db
