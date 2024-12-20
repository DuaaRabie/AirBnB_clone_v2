#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from os import getenv


class State(BaseModel, Base):
    """ State class 
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    def __init__(self, *args, **kwargs):
        params = {}
        if kwargs:
            self.__dict__.update(kwargs)
        super().__init__()

    def get_cities(self):
        """ get cities we could also use get_cities instead of @property """
        if getenv('HBNB_TYPE_STORAGE') != 'db':
            return self.session.query(City).filter_by(state_id=self.id).all()
