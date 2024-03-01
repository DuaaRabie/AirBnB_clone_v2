#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(string(60), Foreignkey=('states.id'), nullable=False)
    
    def __init__(self, *arg, **kwargs):
        if kwargs:
            self.__dict__.update(kwargs)
        super().__init__()
