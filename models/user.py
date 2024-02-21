#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class defines a user by various attributes"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            self.__dict__.update(kwargs)
        super().__init__()
