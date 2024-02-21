#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel


class Place(BaseModel):
    """ A place to stay """
    
    def __init__(self, *args, **kwargs):
        self.city_id = ""
        self.user_id = ""
        if kwargs:
            self.__dict__.update(kwargs)
        super().__init__()
