#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    name = ""
    def __init__(self, *args, **kwargs):
        if args:
            name = args[0]
            new_args = args[1:]
            super().__init__(*args)
