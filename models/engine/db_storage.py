#!/usr/bin/python3
""" This Model for DBStorage """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
import os


class DBStorage:
    """ DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the engine and session"""
        self.__engine = create_engine('mysql+mysqldb://hbnb_dev:hbnb_dev_pwd@localhost:3306/hbnb_dev_db', pool_pre_ping=True)
        self.__session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')

        if os.getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(engine)

        Base.metadata.create_all(engine)

    def all(self, cls=None):
        """ This function query on the current db session """
        if cls is None:
            return {cls.__name__: obj for cls in Base._decl_class_registry.values() if isinstance(obj, cls)}
        else:
            return {obj.id: obj for obj in self.__session.query(cls)}

