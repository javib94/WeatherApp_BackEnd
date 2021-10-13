# coding=utf-8

from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

db_url = os.environ.get('DB_URL')
db_port = os.environ.get('DB_PORT')
db_name = os.environ.get('DB_NAME')
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')
engine = create_engine(f'mariadb+mariadbconnector://{db_user}:{db_password}@{db_url}:{db_port}/{db_name}')

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

Base = declarative_base()


class Entity():
    id = Column(Integer, primary_key=True)
    created_at = Column('created_at',DateTime)
    updated_at = Column('updated_at',DateTime)
    last_updated_by = Column('last_updated_by',String(length=255))

    def __init__(self, created_by):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.last_updated_by = created_by