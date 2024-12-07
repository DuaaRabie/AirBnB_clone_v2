#!/usr/bin/python3
""" This Model for DBStorage """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
import os


class DBStorage:
    """ DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the engine and session"""
        user = os.getenv('HBNB_MYSQL_USER', 'hbnb_dev')
        pwd = os.getenv('HBNB_MYSQL_PWD', 'hbnb_dev_pwd')
        host = os.getenv('HBNB_MYSQL_HOST', 'localhost')
        db = os.getenv('HBNB_MYSQL_DB', 'hbnb_dev_db')

        dialect = 'mysql'
        driver = 'mysqldb'
        options = {'pool_pre_ping': True}
        db_uri = f'{dialect}+{driver}://{user}:{pwd}@{host}/{db}'
        self.__engine = create_engine(db_uri, echo=False, **options)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
        self.reload()

    def all(self, cls=None):
        """ This function query on the current db session"""
        #from models.user import User
        from models.state import State
        from models.city import City
        if cls is None:
            objs = []
            for model in [State, City]:
                objs += self.__session.query(model).all()
        else:
            objs = self.__session.query(cls).all()
        result = {}
        for obj in objs:
            result[f"{obj.__class__.__name__}.{obj.id}"] = obj
        return result

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

    def reload(self):
        """Create all tables in the database and
        create the current database session."""
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
                sessionmaker(bind=self.__engine, expire_on_commit=False))
