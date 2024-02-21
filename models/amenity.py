#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ for Amenity"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            self.__dict__.update(kwargs)
        super().__init__()
