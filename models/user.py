#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    _password = Column("password", String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    
    def __init__(self, *args, **kwargs):
        if kwargs:
            self.__dict__.update(kwargs)
        super().__init__()

    @property
    def password(self):
        """ getter for password """
        return self._password.replace("_", " ")
