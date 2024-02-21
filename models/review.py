#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review classto store review information """
    def __init__(self, *args, **kwargs):
        if kwargs:
            self.__dict__.update(kwargs)
        super().__init__()
