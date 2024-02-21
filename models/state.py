#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    def __init__(self, *args, **kwargs):
        self.__dict__.update(kwargs)
        super().__init__()
