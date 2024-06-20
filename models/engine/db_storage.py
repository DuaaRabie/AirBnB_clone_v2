#!/usr/bin/python3
""" This Model for DBStorage """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
import os


Base = declarative_base()

class DBStorage:
    """ DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the engine and session"""
        self.__engine = self._get_engine()
        self.__session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
        
    @staticmethod
    def _get_engine():
        """ Create the engine linked to the MySQL database """
        user = os.getenv('HBNB_MYSQL_USER', 'hbnb_dev')
        pwd = os.getenv('HBNB_MYSQL_PWD', 'hbnb_dev_pwd')
        host = os.getenv('HBNB_MYSQL_HOST', 'localhost')
        db = os.getenv('HBNB_MYSQL_DB', 'hbnb_dev_db')

        dialect = 'mysql'
        driver = 'mysqldb'
        options = {'pool_pre_ping': True}

        if os.getenv('HBNB_ENV', '') == 'test':
            options['drop_all'] = True
        
        db_uri = f'{dialect}+{driver}://{user}:{pwd}@{host}/{db}'
        engine = create_engine(db_uri, echo=True, **options)
        return engine

    def all(self, cls=None):
        """ This function query on the current db session"""
        if cls is None:
            return {cls.__name__: obj for cls in Base._decl_class_registry.values() for obj in self.__session.query(cls)}
        else:
            return {obj.id: obj for obj in self.__session.query(cls)}
        
    def new(self, obj):
        """Add the object to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session."""
        if obj is not None:
            self.__session.delete(obj)
            self.save()

    @classmethod
    def reload(cls):
        """Create all tables in the database and create the current database session."""
        if cls.__engine is not None:
            cls._get_engine().dispose()
        cls.__engine = cls._get_engine()
        Base.metadata.create_all(cls.__engine)
        cls.__session = scoped_session(sessionmaker(bind=cls.__engine, expire_on_commit=False))
