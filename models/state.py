#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state", cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            """ Returns all cities corresponding to the given state """
            from models import storage
            ret_lst = []
            for city in storage.all(City).values():
                if self.id == city.state_id:
                    ret_lst.append(city)
            return ret_lst
