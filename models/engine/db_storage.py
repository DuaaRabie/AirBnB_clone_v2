#!/usr/bin/python3
""" This Model for DBStorage """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb
        ://hbnb_dev:hbnb_dev_pwd@localhost:3306/hbnb_dev_db', pool_pre_ping=True)
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')

        if os.getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(engine)

        Base.metadata.create_all(engine)

    def all(self, cls=None):
        """ This function query on the current db session """
        if cls is :
        self.__session = sessionmaker(bind=self.__engine, expire_on_commit=False))

